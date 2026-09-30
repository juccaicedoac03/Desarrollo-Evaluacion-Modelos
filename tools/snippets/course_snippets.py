"""Importable, unit-testable mirror of the logic in the canonical notebook snippets.

The notebooks paste the snippet files (``setup_challenge.py``, ``fingerprint.py``,
``startti_client.py``) verbatim; those cells cannot be imported, so this module
re-implements the same logic as plain functions.  ``tools/tests/test_snippets.py`` runs
both copies against each other, so a change to a snippet that is not mirrored here (or
vice versa) fails the tests.  Notebooks never import this module.
"""
import hashlib
import json
import os
import random
from typing import Any, Callable, Sequence

import requests

STARTTI_BASE_URL = "https://api.startti.ai"

STARTTI_HINTS = {401: "invalid or revoked API key", 402: "plan limit reached",
                 403: "the key cannot access this agent", 404: "agent not found — check AGENT_ID",
                 409: "the agent is not published — publish it in ADP first"}


def personal_seed(session: str, student_id: str) -> int:
    """Deterministic 32-bit seed derived from the session id and the student code."""
    return int(hashlib.sha256(f"{session}:{student_id.strip()}".encode()).hexdigest()[:8], 16)


def make_picker(seed: int) -> Callable[[Sequence], Any]:
    """Return ``pick(options)``: a deterministic choice driven by ``random.Random(seed)``."""
    rng = random.Random(seed)

    def pick(options):
        return rng.choice(list(options))

    return pick


def results_fingerprint(session: str, student_id: str, results: Any) -> str:
    """12-hex-char digest of (session, student, results); stable across dict key order."""
    payload = json.dumps({"session": session, "student": student_id.strip(), "results": results},
                         sort_keys=True, default=str, ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()[:12]


def get_secret(name: str):
    """Read a secret from Kaggle Secrets, Colab userdata or an environment variable."""
    try:
        from kaggle_secrets import UserSecretsClient
        return UserSecretsClient().get_secret(name)
    except Exception:
        pass
    try:
        from google.colab import userdata
        return userdata.get(name)
    except Exception:
        pass
    return os.environ.get(name)


def startti_run(agent_id: str, prompt: str, session_key: str = None, timeout_s: int = 120,
                api_key: str = None, base_url: str = STARTTI_BASE_URL) -> str:
    """Send one message to a published Startti agent and return its text answer.

    Same request, response handling and error mapping as ``startti_client.py``.
    ``api_key`` defaults to the ``STARTTI_API_KEY`` secret / environment variable.
    """
    api_key = api_key or get_secret("STARTTI_API_KEY")
    if not api_key:
        raise RuntimeError("STARTTI_API_KEY not found. Kaggle: Add-ons → Secrets. Colab: Secrets (key icon). "
                           "On your own computer: set the STARTTI_API_KEY environment variable before starting Jupyter.")
    body = {"agentId": agent_id, "prompt": prompt}
    if session_key:
        body["sessionKey"] = session_key
    r = requests.post(f"{base_url}/v1/run", json=body, timeout=timeout_s,
                      headers={"Authorization": f"Bearer {api_key}"})
    if r.status_code >= 400:
        try:
            err = r.json()
        except ValueError:
            err = {"message": r.text[:300]}
        hint = STARTTI_HINTS.get(r.status_code, "")
        raise RuntimeError(f"Startti API {r.status_code} ({hint}): {err.get('code', '')} {err.get('message', err)}")
    out = r.json().get("output", {})
    if out.get("errorText"):
        raise RuntimeError(f"Agent error: {out['errorText']}")
    if out.get("suspended"):
        questions = "; ".join(q.get("text", "") for q in out.get("suspendQuestions", []))
        return f"[AGENT ASKED] {questions}"
    return out.get("text", "")
