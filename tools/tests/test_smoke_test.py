"""Tests for the reporting behaviour of tools/smoke_test.py (notebook execution is stubbed)."""
import json
import sys
from pathlib import Path

import pytest

pytest.importorskip("nbclient")
pytest.importorskip("jupyter_client")

TOOLS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

import check_notebooks  # noqa: E402
import smoke_test  # noqa: E402


def fake_result(status="PASS", seconds=1.0):
    return {"status": status, "failed_cell": None, "error": None, "seconds": seconds}


@pytest.fixture
def report(tmp_path, monkeypatch):
    path = tmp_path / "outputs" / "smoke_report.json"
    monkeypatch.setattr(smoke_test, "REPORT_PATH", path)
    monkeypatch.setenv("STARTTI_API_KEY", "restored-by-monkeypatch")
    return path


def install_fake_runner(monkeypatch, results):
    """run_notebook returns (or raises) the next item of ``results`` for each call."""
    queue = list(results)

    def run_notebook(path, timeout):
        item = queue.pop(0)
        if isinstance(item, BaseException):
            raise item
        return dict(item)

    monkeypatch.setattr(smoke_test, "run_notebook", run_notebook)


def make_notebooks(tmp_path, n):
    paths = []
    for i in range(n):
        p = tmp_path / f"nb{i}" / "lab.ipynb"
        p.parent.mkdir()
        p.write_text("{}")
        paths.append(p)
    return paths


def test_display_is_shared_with_check_notebooks():
    assert smoke_test.display is check_notebooks.display


def test_status_line_marks_slow_runs_next_to_the_status():
    assert smoke_test.status_line({"status": "PASS", "path": "a/lab.ipynb", "seconds": 12.5, "slow": False}) \
        == "PASS a/lab.ipynb 12.5s"
    assert smoke_test.status_line({"status": "PASS", "path": "a/lab.ipynb", "seconds": 400.0, "slow": True}) \
        == "PASS SLOW a/lab.ipynb 400.0s"
    assert smoke_test.status_line({"status": "FAIL", "path": "a/lab.ipynb", "seconds": 400.0, "slow": True}) \
        == "FAIL SLOW a/lab.ipynb 400.0s"


def test_slow_threshold_is_360_seconds_and_exclusive():
    assert smoke_test.SLOW_SECONDS == 360
    assert smoke_test.is_slow(360.1) and not smoke_test.is_slow(360.0) and not smoke_test.is_slow(0.5)


def test_slow_notebooks_are_flagged_in_json_and_console_but_do_not_fail(tmp_path, capsys, monkeypatch, report):
    fast, slow = make_notebooks(tmp_path, 2)
    install_fake_runner(monkeypatch, [fake_result(seconds=5.0), fake_result(seconds=361.0)])
    status = smoke_test.main([str(fast), str(slow)])
    out = capsys.readouterr().out
    assert status == 0
    lines = [l for l in out.splitlines() if l.startswith("PASS")]
    assert lines[0].startswith("PASS ") and "SLOW" not in lines[0]
    assert lines[1].startswith("PASS SLOW ") and lines[1].endswith("361.0s")
    data = json.loads(report.read_text())
    assert [r["slow"] for r in data["results"]] == [False, True]
    assert data["passed"] == 2 and data["failed"] == 0


def test_report_is_written_after_every_notebook(tmp_path, monkeypatch, report):
    paths = make_notebooks(tmp_path, 3)
    snapshots = []
    original = smoke_test.write_report

    def spy(*args, **kwargs):
        counts = original(*args, **kwargs)
        snapshots.append(json.loads(report.read_text()))
        return counts

    monkeypatch.setattr(smoke_test, "write_report", spy)
    install_fake_runner(monkeypatch, [fake_result(), fake_result("FAIL"), fake_result()])
    status = smoke_test.main([str(p) for p in paths])
    assert status == 1
    assert [len(s["results"]) for s in snapshots][:3] == [1, 2, 3]
    assert [s["passed"] for s in snapshots][:3] == [1, 1, 2]
    assert json.loads(report.read_text())["failed"] == 1


def test_interrupted_run_keeps_results_of_finished_notebooks(tmp_path, monkeypatch, report):
    paths = make_notebooks(tmp_path, 3)
    install_fake_runner(monkeypatch, [fake_result(seconds=2.0), KeyboardInterrupt()])
    with pytest.raises(KeyboardInterrupt):
        smoke_test.main([str(p) for p in paths])
    data = json.loads(report.read_text())
    assert len(data["results"]) == 1 and data["results"][0]["status"] == "PASS"
    assert data["results"][0]["path"].endswith("lab.ipynb")


def test_path_problems_still_count_as_failures_and_are_reported(tmp_path, capsys, monkeypatch, report):
    (good,) = make_notebooks(tmp_path, 1)
    install_fake_runner(monkeypatch, [fake_result()])
    status = smoke_test.main([str(tmp_path / "missing"), str(good)])
    capsys.readouterr()
    data = json.loads(report.read_text())
    assert status == 1 and data["failed"] == 1 and len(data["problems"]) == 1 and data["passed"] == 1
