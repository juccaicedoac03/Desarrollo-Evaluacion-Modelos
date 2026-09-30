#!/usr/bin/env python3
"""Structure checks for the course notebooks (no execution, no language heuristics).

Usage:
    python tools/check_notebooks.py                      # every sessions/*/lab.ipynb and challenge.ipynb
    python tools/check_notebooks.py sessions/03-transfer-learning
    python tools/check_notebooks.py path/to/lab.ipynb path/to/challenge.ipynb

A notebook is a *lab* or a *challenge* only when it is named ``lab.ipynb`` or
``challenge.ipynb``.  Other ``.ipynb`` files found while scanning a directory are skipped;
one passed explicitly as a file is still validated, and its kind can be forced with
``--kind`` when its name is not one of those two.

Checks (all notebooks):
  * valid nbformat 4 (nbformat validation, no cells missing an ``id``: nbformat reports that with
    a ``MissingIDFieldWarning``, which is turned into a failure);
  * no outputs and no execution counts in code cells;
  * if code calls ``startti_run(`` the notebook contains ``snippets/startti_client.py`` verbatim.

Labs: the first code cell starts with ``snippets/setup_lab.py`` verbatim.

Challenges (see the "Challenge notebook anatomy" in the course plan):
  * first code cell contains ``snippets/setup_challenge.py`` verbatim, except that the value of
    ``SESSION = "S<NN>"`` may differ (and must match the ``NN-slug`` folder name when there is one);
  * a code cell after the setup cell (and before the ``RESULTS`` cell) assigns ``CONFIG`` and calls
    ``pick(`` in code - a mention in a ``#`` comment does not count.  Other cells may sit between
    setup and CONFIG (Startti sessions put the ``startti_client.py`` cell there);
  * a later code cell assigns ``RESULTS`` (``RESULTS = ...`` or annotated ``RESULTS: dict = ...``);
  * last code cell contains ``snippets/fingerprint.py`` verbatim;
  * the markdown cell right before it contains ``snippets/ai_log.md`` verbatim.

A snippet is "contained" when its text is a substring of the cell source (line endings normalised).
Prints ``OK <path>`` or ``FAIL <path>: <reasons>`` per notebook; exit status 1 if any failed.
"""
import argparse
import io
import json
import re
import sys
import tokenize
import warnings
from pathlib import Path

import nbformat

try:
    from nbformat.warnings import MissingIDFieldWarning
except ImportError:  # older nbformat: the missing-id warning is a plain FutureWarning with a message
    MissingIDFieldWarning = None

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = TOOLS_DIR.parent
SNIPPETS_DIR = TOOLS_DIR / "snippets"

KIND_BY_NAME = {"lab.ipynb": "lab", "challenge.ipynb": "challenge"}
SESSION_LINE = re.compile(r'(?m)^SESSION = "(S\d\d)"$')
STARTTI_CALL = re.compile(r"(?m)^(?!\s*#).*\bstartti_run\(")
# ``NAME = ...`` and annotated ``NAME: type = ...`` (a bare ``NAME: type`` is not an assignment)
CONFIG_ASSIGN = re.compile(r"(?m)^CONFIG\s*(?::[^=\n]+)?=(?!=)")
RESULTS_ASSIGN = re.compile(r"(?m)^RESULTS\s*(?::[^=\n]+)?=(?!=)")
COMMENT = re.compile(r"(?m)#.*$")
FOLDER_SESSION = re.compile(r"^(\d\d)-")
MAX_LISTED = 8


# ----------------------------------------------------------------------------- helpers
def normalize(text):
    return text.replace("\r\n", "\n")


def strip_comments(source):
    """Source without ``#`` comments (a ``#`` inside a string is kept when the cell tokenizes)."""
    try:
        lines = source.split("\n")
        spans = [tok.start + tok.end for tok in tokenize.generate_tokens(io.StringIO(source).readline)
                 if tok.type == tokenize.COMMENT]
    except (tokenize.TokenError, SyntaxError, IndentationError):
        return COMMENT.sub("", source)  # e.g. cells with %magics: crude, but good enough
    for (row, col, _, end_col) in reversed(spans):
        lines[row - 1] = lines[row - 1][:col] + lines[row - 1][end_col:]
    return "\n".join(lines)


def load_snippet(name):
    """Canonical snippet text without its trailing newline."""
    return normalize((SNIPPETS_DIR / name).read_text(encoding="utf-8")).rstrip()


def mask_session(text):
    """Replace the value of the ``SESSION = "S..."`` line so any session number compares equal."""
    return SESSION_LINE.sub('SESSION = "S00"', text)


def listed(indices):
    shown = ", ".join(str(i) for i in indices[:MAX_LISTED])
    return shown + (f", ... ({len(indices)} total)" if len(indices) > MAX_LISTED else "")


def display(path):
    """Path relative to the current directory when possible (shared with smoke_test.py)."""
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(path)


def discover(directory):
    """lab.ipynb / challenge.ipynb files anywhere below ``directory`` (checkpoints excluded)."""
    return sorted(p for p in directory.rglob("*.ipynb")
                  if p.name in KIND_BY_NAME and ".ipynb_checkpoints" not in p.parts)


def default_notebooks():
    """sessions/*/lab.ipynb and sessions/*/challenge.ipynb."""
    return sorted(p for name in KIND_BY_NAME for p in (ROOT / "sessions").glob(f"*/{name}"))


# ------------------------------------------------------------------------------ checks
def is_missing_id_warning(warning):
    """True for nbformat's "cell has no id" warning (by category; by message on older nbformat)."""
    if MissingIDFieldWarning is not None:
        return issubclass(warning.category, MissingIDFieldWarning)
    return "missing an id" in str(warning.message)


def load_notebook(path):
    """Return (notebook, reasons).  ``notebook`` is None when it cannot be checked further."""
    try:
        text = path.read_text(encoding="utf-8")
        raw = json.loads(text)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return None, [f"cannot read notebook ({exc})"]
    if not isinstance(raw, dict) or raw.get("nbformat") != 4:
        found = raw.get("nbformat") if isinstance(raw, dict) else None
        return None, [f"nbformat must be 4 (found {found!r})"]
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            nb = nbformat.reads(text, as_version=4)
            nbformat.validate(nb)
    except Exception as exc:  # jsonschema / nbformat raise several unrelated classes
        first_line = (str(exc).strip().splitlines() or [type(exc).__name__])[0]
        return None, [f"nbformat validation failed: {first_line[:160]}"]
    if any(is_missing_id_warning(w) for w in caught):
        return None, ["nbformat validation failed: cells without an id field (nbformat_minor >= 5 requires ids)"]
    return nb, []


def check_generic(cells):
    reasons = []
    code = [(i, c) for i, c in enumerate(cells) if c.cell_type == "code"]
    with_outputs = [i for i, c in code if c.get("outputs")]
    if with_outputs:
        reasons.append(f"code cells with outputs (cell index {listed(with_outputs)})")
    with_counts = [i for i, c in code if c.get("execution_count") is not None]
    if with_counts:
        reasons.append(f"code cells with execution_count (cell index {listed(with_counts)})")
    calls_startti = any(STARTTI_CALL.search(normalize(c.source)) for _, c in code)
    if calls_startti:
        block = load_snippet("startti_client.py")
        if not any(block in normalize(c.source) for _, c in code):
            reasons.append("calls startti_run( but has no code cell with the exact startti_client.py block")
    return reasons


def check_lab(cells):
    code = [c for c in cells if c.cell_type == "code"]
    if not code:
        return ["no code cells (first code cell must start with the setup_lab.py block)"]
    if not normalize(code[0].source).startswith(load_snippet("setup_lab.py")):
        return ["first code cell does not start with the exact setup_lab.py block"]
    return []


def check_challenge(cells, folder_name):
    reasons = []
    code = [(i, c) for i, c in enumerate(cells) if c.cell_type == "code"]
    if not code:
        return ["no code cells"]

    # 1. setup cell (first code cell), modulo the SESSION value
    first_src = normalize(code[0][1].source)
    if mask_session(load_snippet("setup_challenge.py")) not in mask_session(first_src):
        reasons.append("first code cell does not contain the exact setup_challenge.py block "
                       "(only the SESSION value may differ)")
    else:
        session = SESSION_LINE.search(first_src).group(1)
        folder = FOLDER_SESSION.match(folder_name)
        if folder and session != f"S{folder.group(1)}":
            reasons.append(f'SESSION = "{session}" does not match folder {folder_name!r} '
                           f'(expected "S{folder.group(1)}")')

    fp_idx, fp_cell = code[-1]

    # 2. CONFIG cell: any code cell between setup and fingerprint that assigns CONFIG and calls pick(
    #    in code (comments stripped).  It must come before the RESULTS cell (checked in 4).
    between = [(i, c) for i, c in code if code[0][0] < i < fp_idx]
    assigning = [(i, c) for i, c in between if CONFIG_ASSIGN.search(normalize(c.source))]
    personal = [i for i, c in assigning if "pick(" in strip_comments(normalize(c.source))]
    if personal:
        config_idx = personal[0]
    else:
        config_idx = None
        if assigning:
            reasons.append("CONFIG cell must call pick(...) in code (not only in a comment) "
                           "so the configuration is personal")
        else:
            reasons.append("no code cell after the setup cell assigns CONFIG = {...}")

    # 3. fingerprint cell = last code cell
    fingerprint = load_snippet("fingerprint.py")
    fp_ok = fingerprint in normalize(fp_cell.source)
    if not fp_ok:
        if any(fingerprint in normalize(c.source) for _, c in code):
            reasons.append("fingerprint.py block must be in the last code cell")
        else:
            reasons.append("no code cell with the exact fingerprint.py block")

    # 4. RESULTS assigned between CONFIG and fingerprint cells
    lo = config_idx if config_idx is not None else code[0][0]
    if not any(RESULTS_ASSIGN.search(normalize(c.source)) for i, c in code if lo < i < fp_idx):
        reasons.append("no code cell assigning RESULTS = {...} between the CONFIG and fingerprint cells")

    # 5. AI-log markdown cell right before the fingerprint cell
    ai_log = load_snippet("ai_log.md")
    md_with_log = [i for i, c in enumerate(cells)
                   if c.cell_type == "markdown" and ai_log in normalize(c.source)]
    if not md_with_log:
        reasons.append("no markdown cell with the exact ai_log.md text")
    elif fp_ok and fp_idx - 1 not in md_with_log:
        reasons.append("the ai_log.md markdown cell must be right before the fingerprint cell")
    return reasons


def check_notebook(path, kind=None):
    """Return a list of failure reasons (empty when the notebook is fine)."""
    kind = KIND_BY_NAME.get(path.name) or kind
    nb, reasons = load_notebook(path)
    if nb is None:
        return reasons
    reasons += check_generic(nb.cells)
    if kind == "lab":
        reasons += check_lab(nb.cells)
    elif kind == "challenge":
        reasons += check_challenge(nb.cells, path.resolve().parent.name)
    return reasons


# -------------------------------------------------------------------------------- main
def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="*", type=Path,
                        help="notebook files or directories (default: sessions/*/)")
    parser.add_argument("--kind", choices=["lab", "challenge"],
                        help="kind for explicit files not named lab.ipynb / challenge.ipynb")
    args = parser.parse_args(argv)

    failures = 0
    targets = []  # (path, failure reason or None)
    if args.paths:
        for p in args.paths:
            if not p.exists():
                targets.append((p, "path not found"))
            elif p.is_dir():
                found = discover(p)
                targets += [(f, None) for f in found] or [(p, "no lab.ipynb or challenge.ipynb found")]
            else:
                targets.append((p, None))
    else:
        targets = [(p, None) for p in default_notebooks()]
        if not targets:
            print("No sessions/*/lab.ipynb or challenge.ipynb found - nothing to check.")

    for path, problem in targets:
        reasons = [problem] if problem else check_notebook(path, args.kind)
        if reasons:
            failures += 1
            print(f"FAIL {display(path)}: {'; '.join(reasons)}")
        else:
            print(f"OK {display(path)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
