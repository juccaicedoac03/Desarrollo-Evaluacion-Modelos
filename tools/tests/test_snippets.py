"""Unit tests for the canonical notebook snippets.

Two layers:

1. ``course_snippets`` (importable, testable functions) is tested for determinism,
   fingerprint stability and the ``startti_run`` error mapping (``requests.post`` is
   mocked, no network).
2. The *real* snippet files (``setup_challenge.py``, ``fingerprint.py``,
   ``startti_client.py``) are executed and compared against ``course_snippets`` so the
   two copies of the logic cannot drift apart.
"""
import hashlib
import json
import random
import sys
import types
from pathlib import Path

import pytest
import requests

SNIPPETS_DIR = Path(__file__).resolve().parents[1] / "snippets"
sys.path.insert(0, str(SNIPPETS_DIR))

import course_snippets as cs  # noqa: E402


# --------------------------------------------------------------------------- helpers
class FakeResponse:
    """Minimal stand-in for ``requests.Response``."""

    def __init__(self, status_code=200, payload=None, text=""):
        self.status_code = status_code
        self._payload = payload
        self.text = text if payload is None else json.dumps(payload)

    def json(self):
        if self._payload is None:
            raise ValueError("No JSON object could be decoded")
        return self._payload


class PostRecorder:
    """Replacement for ``requests.post`` that records calls and returns a canned response."""

    def __init__(self, response):
        self.response = response
        self.calls = []

    def __call__(self, url, **kwargs):
        self.calls.append((url, kwargs))
        return self.response


def ok(text="hello", **output):
    return FakeResponse(200, {"sessionId": "s1", "sessionKey": "k1",
                              "output": {"text": text, "suspended": False,
                                         "suspendQuestions": [], "errorText": None, **output}})


def read_snippet(name):
    return (SNIPPETS_DIR / name).read_text(encoding="utf-8")


# --------------------------------------------------------------------- personal_seed
def expected_seed(session, student_id):
    return int(hashlib.sha256(f"{session}:{student_id}".encode()).hexdigest()[:8], 16)


def test_personal_seed_is_deterministic():
    assert cs.personal_seed("S01", "202012345") == cs.personal_seed("S01", "202012345")


def test_personal_seed_matches_reference_formula():
    assert cs.personal_seed("S03", "1020304050") == expected_seed("S03", "1020304050")


def test_personal_seed_differs_by_session_and_student():
    base = cs.personal_seed("S01", "111")
    assert cs.personal_seed("S02", "111") != base
    assert cs.personal_seed("S01", "112") != base


def test_personal_seed_strips_student_id_whitespace():
    assert cs.personal_seed("S01", "  111 \n") == cs.personal_seed("S01", "111")


def test_personal_seed_fits_in_32_bits():
    # numpy.random.seed needs 0 <= seed < 2**32; the snippet also uses `% (2**32)` defensively.
    for sid in ("1", "22", "333", "4444", "abc", "Ñandú"):
        assert 0 <= cs.personal_seed("S05", sid) < 2**32


# ---------------------------------------------------------------------- make_picker
def test_picker_is_deterministic_for_same_seed():
    options = ["a", "b", "c", "d", "e"]
    p1, p2 = cs.make_picker(123), cs.make_picker(123)
    assert [p1(options) for _ in range(20)] == [p2(options) for _ in range(20)]


def test_picker_matches_random_choice_sequence():
    options = [10, 20, 30, 40]
    rng = random.Random(7)
    pick = cs.make_picker(7)
    assert [pick(options) for _ in range(15)] == [rng.choice(options) for _ in range(15)]


def test_picker_differs_across_seeds():
    options = list(range(1000))
    assert len({cs.make_picker(seed)(options) for seed in range(50)}) > 1


def test_picker_accepts_any_iterable_and_returns_member():
    pick = cs.make_picker(99)
    assert pick({"x": 1, "y": 2}.keys()) in {"x", "y"}
    assert pick(x for x in ("only",)) == "only"
    assert pick(("t1", "t2")) in {"t1", "t2"}


def test_picker_state_is_per_picker_not_global():
    options = list(range(1000))
    p1 = cs.make_picker(5)
    first = p1(options)
    p1(options)
    assert cs.make_picker(5)(options) == first  # a fresh picker restarts the sequence


# ------------------------------------------------------------------------ fingerprint
def expected_fingerprint(session, student, results):
    payload = json.dumps({"session": session, "student": student, "results": results},
                         sort_keys=True, default=str, ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()[:12]


def test_fingerprint_is_12_hex_chars():
    fp = cs.results_fingerprint("S01", "111", {"acc": 0.9})
    assert len(fp) == 12 and all(c in "0123456789abcdef" for c in fp)


def test_fingerprint_is_stable_and_matches_reference():
    results = {"CONFIG": {"seed": 1}, "RESULTS": {"acc": 0.9123, "n": 3}}
    fp = cs.results_fingerprint("S02", "42", results)
    assert fp == cs.results_fingerprint("S02", "42", results)
    assert fp == expected_fingerprint("S02", "42", results)


def test_fingerprint_ignores_dict_key_order():
    a = {"x": 1, "y": {"b": 2, "a": 1}}
    b = {"y": {"a": 1, "b": 2}, "x": 1}
    assert cs.results_fingerprint("S01", "1", a) == cs.results_fingerprint("S01", "1", b)


def test_fingerprint_changes_with_session_student_and_results():
    base = cs.results_fingerprint("S01", "1", {"acc": 0.5})
    assert cs.results_fingerprint("S02", "1", {"acc": 0.5}) != base
    assert cs.results_fingerprint("S01", "2", {"acc": 0.5}) != base
    assert cs.results_fingerprint("S01", "1", {"acc": 0.5001}) != base


def test_fingerprint_strips_student_id_whitespace():
    assert (cs.results_fingerprint("S01", " 1 ", {"a": 1})
            == cs.results_fingerprint("S01", "1", {"a": 1}))


def test_fingerprint_keeps_non_ascii_unescaped_and_stringifies_unknown_types():
    results = {"comentario": "acción rápida", "path": Path("a/b")}
    assert (cs.results_fingerprint("S01", "1", results)
            == expected_fingerprint("S01", "1", results))


# ------------------------------------------------------------------------ startti_run
def test_startti_run_success_sends_expected_request(monkeypatch):
    post = PostRecorder(ok("hi there"))
    monkeypatch.setattr(requests, "post", post)
    out = cs.startti_run("agent-1", "hello", api_key="KEY", timeout_s=33)
    assert out == "hi there"
    (url, kwargs), = post.calls
    assert url == "https://api.startti.ai/v1/run"
    assert kwargs["json"] == {"agentId": "agent-1", "prompt": "hello"}
    assert kwargs["headers"] == {"Authorization": "Bearer KEY"}
    assert kwargs["timeout"] == 33


def test_startti_run_includes_session_key_only_when_given(monkeypatch):
    post = PostRecorder(ok())
    monkeypatch.setattr(requests, "post", post)
    cs.startti_run("a", "p", api_key="K")
    cs.startti_run("a", "p", session_key="sess-9", api_key="K")
    assert "sessionKey" not in post.calls[0][1]["json"]
    assert post.calls[1][1]["json"]["sessionKey"] == "sess-9"


def test_startti_run_custom_base_url(monkeypatch):
    post = PostRecorder(ok())
    monkeypatch.setattr(requests, "post", post)
    cs.startti_run("a", "p", api_key="K", base_url="http://localhost:9000")
    assert post.calls[0][0] == "http://localhost:9000/v1/run"


def test_startti_run_without_key_raises_and_does_not_call_network(monkeypatch):
    post = PostRecorder(ok())
    monkeypatch.setattr(requests, "post", post)
    monkeypatch.delenv("STARTTI_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="STARTTI_API_KEY"):
        cs.startti_run("a", "p")
    assert post.calls == []


def test_startti_run_reads_key_from_environment(monkeypatch):
    post = PostRecorder(ok())
    monkeypatch.setattr(requests, "post", post)
    monkeypatch.setenv("STARTTI_API_KEY", "ENVKEY")
    cs.startti_run("a", "p")
    assert post.calls[0][1]["headers"] == {"Authorization": "Bearer ENVKEY"}


@pytest.mark.parametrize("status,hint", [
    (401, "invalid or revoked API key"),
    (402, "plan limit reached"),
    (403, "the key cannot access this agent"),
    (404, "agent not found"),
    (409, "the agent is not published"),
])
def test_startti_run_maps_http_errors_to_hints(monkeypatch, status, hint):
    resp = FakeResponse(status, {"code": "E_X", "message": "boom"})
    monkeypatch.setattr(requests, "post", PostRecorder(resp))
    with pytest.raises(RuntimeError) as exc:
        cs.startti_run("a", "p", api_key="K")
    msg = str(exc.value)
    assert f"Startti API {status}" in msg and hint in msg
    assert "E_X" in msg and "boom" in msg


def test_startti_run_unknown_status_has_empty_hint(monkeypatch):
    monkeypatch.setattr(requests, "post",
                        PostRecorder(FakeResponse(500, {"message": "server exploded"})))
    with pytest.raises(RuntimeError, match=r"Startti API 500 \(\):.*server exploded"):
        cs.startti_run("a", "p", api_key="K")


def test_startti_run_non_json_error_body_is_truncated(monkeypatch):
    resp = FakeResponse(502, None, text="x" * 1000)
    monkeypatch.setattr(requests, "post", PostRecorder(resp))
    with pytest.raises(RuntimeError) as exc:
        cs.startti_run("a", "p", api_key="K")
    msg = str(exc.value)
    assert "Startti API 502" in msg
    assert "x" * 300 in msg and "x" * 301 not in msg


def test_startti_run_error_text_raises(monkeypatch):
    monkeypatch.setattr(requests, "post", PostRecorder(ok("", errorText="tool crashed")))
    with pytest.raises(RuntimeError, match="Agent error: tool crashed"):
        cs.startti_run("a", "p", api_key="K")


def test_startti_run_suspended_returns_agent_asked(monkeypatch):
    resp = ok("", suspended=True, suspendQuestions=[{"text": "Which region?"}, {"text": "Which year?"}])
    monkeypatch.setattr(requests, "post", PostRecorder(resp))
    assert cs.startti_run("a", "p", api_key="K") == "[AGENT ASKED] Which region?; Which year?"


def test_startti_run_missing_output_returns_empty_string(monkeypatch):
    monkeypatch.setattr(requests, "post", PostRecorder(FakeResponse(200, {"sessionId": "s"})))
    assert cs.startti_run("a", "p", api_key="K") == ""


# --------------------------------------------- parity with the real snippet files
def _fake_torch():
    torch = types.ModuleType("torch")
    torch.manual_seed = lambda seed: None
    torch.cuda = types.SimpleNamespace(is_available=lambda: False)
    return torch


def test_setup_challenge_snippet_agrees_with_course_snippets(monkeypatch, capsys):
    monkeypatch.setitem(sys.modules, "torch", _fake_torch())
    monkeypatch.setenv("COURSE_FAST_DEV_RUN", "1")  # snippet fills in a placeholder student id
    ns = {}
    exec(compile(read_snippet("setup_challenge.py"), "setup_challenge.py", "exec"), ns)
    assert ns["STUDENT_ID"] == "000000"
    assert ns["PERSONAL_SEED"] == cs.personal_seed(ns["SESSION"], ns["STUDENT_ID"])
    pick, ref = ns["pick"], cs.make_picker(ns["PERSONAL_SEED"])
    options = ["a", "b", "c", "d", "e", "f"]
    assert [pick(options) for _ in range(10)] == [ref(options) for _ in range(10)]
    assert "Semilla personal" in capsys.readouterr().out


def test_setup_challenge_snippet_requires_student_id(monkeypatch):
    monkeypatch.setitem(sys.modules, "torch", _fake_torch())
    monkeypatch.delenv("COURSE_FAST_DEV_RUN", raising=False)
    with pytest.raises(AssertionError, match="STUDENT_ID"):
        exec(compile(read_snippet("setup_challenge.py"), "setup_challenge.py", "exec"), {})


def test_fingerprint_snippet_agrees_with_course_snippets(capsys):
    config, results = {"dataset": "ag_news"}, {"acc": 0.8123, "f1": 0.79}
    ns = {"json": json, "hashlib": hashlib, "SESSION": "S04", "STUDENT_ID": " 777 ",
          "CONFIG": config, "RESULTS": results}
    exec(compile(read_snippet("fingerprint.py"), "fingerprint.py", "exec"), ns)
    expected = cs.results_fingerprint("S04", "777", {"CONFIG": config, "RESULTS": results})
    assert ns["results_fingerprint"]({"CONFIG": config, "RESULTS": results}) == expected
    assert expected in capsys.readouterr().out


@pytest.mark.parametrize("response,expected", [
    (ok("plain answer"), "plain answer"),
    (ok("", suspended=True, suspendQuestions=[{"text": "A?"}, {"text": "B?"}]), "[AGENT ASKED] A?; B?"),
    (FakeResponse(200, {}), ""),
    (ok("", errorText="bad"), RuntimeError),
    (FakeResponse(401, {"code": "UNAUTH", "message": "nope"}), RuntimeError),
    (FakeResponse(402, {"message": "limit"}), RuntimeError),
    (FakeResponse(403, {"message": "denied"}), RuntimeError),
    (FakeResponse(404, {"message": "missing"}), RuntimeError),
    (FakeResponse(409, {"message": "draft"}), RuntimeError),
    (FakeResponse(500, None, text="oops " * 200), RuntimeError),
])
def test_startti_client_snippet_behaves_like_course_snippets(monkeypatch, response, expected):
    monkeypatch.setenv("STARTTI_API_KEY", "KEY")
    ns = {}
    exec(compile(read_snippet("startti_client.py"), "startti_client.py", "exec"), ns)
    assert ns["STARTTI_API_KEY"] == "KEY"

    monkeypatch.setattr(requests, "post", PostRecorder(response))
    if expected is RuntimeError:
        with pytest.raises(RuntimeError) as snippet_exc:
            ns["startti_run"]("a", "p")
        with pytest.raises(RuntimeError) as lib_exc:
            cs.startti_run("a", "p", api_key="KEY")
        assert str(snippet_exc.value) == str(lib_exc.value)
    else:
        assert ns["startti_run"]("a", "p") == expected
        assert cs.startti_run("a", "p", api_key="KEY") == expected


def test_startti_client_snippet_sends_same_request_as_course_snippets(monkeypatch):
    monkeypatch.setenv("STARTTI_API_KEY", "KEY")
    ns = {}
    exec(compile(read_snippet("startti_client.py"), "startti_client.py", "exec"), ns)
    post = PostRecorder(ok())
    monkeypatch.setattr(requests, "post", post)
    ns["startti_run"]("agent", "prompt", session_key="sk", timeout_s=7)
    cs.startti_run("agent", "prompt", session_key="sk", timeout_s=7, api_key="KEY")
    assert post.calls[0] == post.calls[1]


def test_startti_client_snippet_without_key_raises_runtime_error(monkeypatch, capsys):
    monkeypatch.delenv("STARTTI_API_KEY", raising=False)
    ns = {}
    exec(compile(read_snippet("startti_client.py"), "startti_client.py", "exec"), ns)
    assert ns["STARTTI_API_KEY"] is None
    assert "No STARTTI_API_KEY" in capsys.readouterr().out
    with pytest.raises(RuntimeError, match="STARTTI_API_KEY"):
        ns["startti_run"]("a", "p")


def test_ai_log_snippet_mentions_the_three_reflection_questions_and_table():
    text = read_snippet("ai_log.md")
    assert text.startswith("## 🪞 Reflexión y registro de uso de IA (20%)")
    assert "### 🤖 Registro de uso de IA (obligatorio)" in text
    assert "| # | Herramienta" in text
