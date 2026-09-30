#!/usr/bin/env python3
"""Execute course notebooks end to end in fast-dev mode (a smoke test, sequential).

Usage:
    python tools/smoke_test.py                       # every sessions/*/lab.ipynb and challenge.ipynb
    python tools/smoke_test.py sessions/02-training-generative-models
    python tools/smoke_test.py path/to/lab.ipynb --timeout 1200

Each notebook is executed from an in-memory copy (the file on disk is never modified) in a
kernel started with *this* Python interpreter, working directory = the notebook's folder, and

    COURSE_FAST_DEV_RUN=1  KERAS_BACKEND=torch  TOKENIZERS_PARALLELISM=false
    PYTORCH_ENABLE_MPS_FALLBACK=1

``STARTTI_API_KEY`` is removed from the environment so the "no key" path of every Startti cell is
what gets exercised.  Notebooks run one after another (the target machine has 8 GB of RAM).

Prints ``PASS <path> <seconds>s`` or ``FAIL <path> <seconds>s`` followed by the failing cell's source
(first 40 lines) and the tail of the traceback, writes ``outputs/smoke_report.json`` (git-ignored)
and exits with status 1 if any notebook failed.
"""
import argparse
import json
import os
import re
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

import nbformat
from jupyter_client.kernelspec import KernelSpec, KernelSpecManager
from jupyter_client.manager import AsyncKernelManager
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError
from traitlets import default

from check_notebooks import KIND_BY_NAME, default_notebooks, discover

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "outputs" / "smoke_report.json"

KERNEL_NAME = "course-smoke"
KERNEL_ENV = {
    "COURSE_FAST_DEV_RUN": "1",
    "KERAS_BACKEND": "torch",
    "TOKENIZERS_PARALLELISM": "false",
    "PYTORCH_ENABLE_MPS_FALLBACK": "1",
}
SOURCE_LINES = 40
TRACEBACK_LINES = 30
ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")


# ------------------------------------------------------------------------------ kernel
class CurrentPythonSpecManager(KernelSpecManager):
    """Resolves KERNEL_NAME to ``sys.executable`` instead of whatever ``python3`` kernelspec is
    installed on the machine (a user-level ``python3`` spec would shadow the active virtualenv)."""

    def get_kernel_spec(self, kernel_name):
        if kernel_name != KERNEL_NAME:
            return super().get_kernel_spec(kernel_name)
        return KernelSpec(argv=[sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
                          display_name="Course smoke test (current Python)", language="python",
                          env=dict(KERNEL_ENV))


class CurrentPythonKernelManager(AsyncKernelManager):
    @default("kernel_spec_manager")
    def _kernel_spec_manager_default(self):
        return CurrentPythonSpecManager(data_dir=self.data_dir)


# ---------------------------------------------------------------------------- running
def clean(text):
    return ANSI.sub("", text)


def tail(text, n):
    lines = clean(text).rstrip().splitlines()
    return "\n".join(lines[-n:])


def error_output_traceback(cell):
    """Traceback text stored in the error output of a failed cell, if any."""
    for output in cell.get("outputs", []):
        if output.get("output_type") == "error":
            return "\n".join(output.get("traceback") or [f"{output.get('ename')}: {output.get('evalue')}"])
    return None


def run_notebook(path, timeout):
    """Execute one notebook copy.  Returns a result dict; never raises for notebook errors."""
    nb = nbformat.read(path, as_version=4)  # in-memory copy; never written back
    current = {"index": None}
    client = NotebookClient(
        nb, timeout=timeout, kernel_name=KERNEL_NAME, kernel_manager_class=CurrentPythonKernelManager,
        resources={"metadata": {"path": str(path.parent)}}, allow_errors=False,
        on_cell_start=lambda cell, cell_index, **_: current.update(index=cell_index))
    started = time.monotonic()
    result = {"status": "PASS", "failed_cell": None, "error": None}
    try:
        client.execute()
    except Exception as exc:  # CellExecutionError, CellTimeoutError, DeadKernelError, startup errors...
        idx = current["index"]
        if isinstance(exc, CellExecutionError):
            detail = (error_output_traceback(nb.cells[idx]) if idx is not None else None) or str(exc)
        elif isinstance(exc, TimeoutError):
            detail = f"{type(exc).__name__}: a cell ran longer than --timeout ({timeout} s)"
        else:
            detail = "".join(traceback.format_exception_only(type(exc), exc))
        result.update(status="FAIL", failed_cell=idx, error=tail(detail, TRACEBACK_LINES))
        if idx is not None:
            result["failed_cell_source"] = "\n".join(nb.cells[idx].source.splitlines()[:SOURCE_LINES])
    result["seconds"] = round(time.monotonic() - started, 1)
    return result


def display(path):
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(path)


def print_failure(result):
    if result.get("failed_cell") is not None:
        print(f"  Failing cell (index {result['failed_cell']}), first {SOURCE_LINES} lines:")
        print("\n".join(f"    | {line}" for line in result.get("failed_cell_source", "").splitlines()))
    print("  Traceback (tail):")
    print("\n".join(f"    {line}" for line in (result["error"] or "").splitlines()))


def collect(paths):
    """Expand CLI paths (files or directories) into notebooks; returns (notebooks, problems)."""
    notebooks, problems = [], []
    for p in paths:
        if not p.exists():
            problems.append(f"{p}: path not found")
        elif p.is_dir():
            found = discover(p)
            notebooks += found
            if not found:
                problems.append(f"{p}: no {' or '.join(KIND_BY_NAME)} found")
        else:
            notebooks.append(p)
    return notebooks, problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="*", type=Path,
                        help="notebook files or directories (default: sessions/*/lab.ipynb and challenge.ipynb)")
    parser.add_argument("--timeout", type=int, default=900, help="per-cell timeout in seconds (default 900)")
    args = parser.parse_args(argv)

    notebooks, problems = collect(args.paths) if args.paths else (default_notebooks(), [])
    for problem in problems:
        print(f"FAIL {problem}")
    if not notebooks and not problems:
        print("No sessions/*/lab.ipynb or challenge.ipynb found - nothing to run.")

    os.environ.pop("STARTTI_API_KEY", None)  # hermetic: exercise the no-key path of Startti cells
    print(f"Kernel Python: {sys.executable} | per-cell timeout: {args.timeout}s | notebooks: {len(notebooks)}")

    results = []
    for path in notebooks:
        result = run_notebook(path, args.timeout)
        result["path"] = display(path)
        results.append(result)
        print(f"{result['status']} {result['path']} {result['seconds']}s", flush=True)
        if result["status"] == "FAIL":
            print_failure(result)

    passed = sum(r["status"] == "PASS" for r in results)
    failed = len(results) - passed + len(problems)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps({
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "python": sys.executable, "timeout_s": args.timeout, "kernel_env": KERNEL_ENV,
        "passed": passed, "failed": failed,
        "problems": problems, "results": results,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{passed}/{len(results)} passed - report: {display(REPORT_PATH)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
