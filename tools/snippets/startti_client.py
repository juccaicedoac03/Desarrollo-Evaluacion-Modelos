# --- Startti ADP client ---
import os, requests
STARTTI_BASE_URL = "https://api.startti.ai"

def get_secret(name):
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

STARTTI_API_KEY = get_secret("STARTTI_API_KEY")
_STARTTI_HINTS = {401: "invalid or revoked API key", 402: "plan limit reached",
                  403: "the key cannot access this agent", 404: "agent not found — check AGENT_ID",
                  409: "the agent is not published — publish it in ADP first"}

def startti_run(agent_id, prompt, session_key=None, timeout_s=120):
    """Send one message to a published Startti agent and return its text answer."""
    if not STARTTI_API_KEY:
        raise RuntimeError("STARTTI_API_KEY not found. Add it in Kaggle → Add-ons → Secrets.")
    body = {"agentId": agent_id, "prompt": prompt}
    if session_key:
        body["sessionKey"] = session_key
    r = requests.post(f"{STARTTI_BASE_URL}/v1/run", json=body, timeout=timeout_s,
                      headers={"Authorization": f"Bearer {STARTTI_API_KEY}"})
    if r.status_code >= 400:
        try:
            err = r.json()
        except ValueError:
            err = {"message": r.text[:300]}
        hint = _STARTTI_HINTS.get(r.status_code, "")
        raise RuntimeError(f"Startti API {r.status_code} ({hint}): {err.get('code', '')} {err.get('message', err)}")
    out = r.json().get("output", {})
    if out.get("errorText"):
        raise RuntimeError(f"Agent error: {out['errorText']}")
    if out.get("suspended"):
        questions = "; ".join(q.get("text", "") for q in out.get("suspendQuestions", []))
        return f"[AGENT ASKED] {questions}"
    return out.get("text", "")

print("Startti key found ✅" if STARTTI_API_KEY else "No STARTTI_API_KEY — Startti cells will be skipped.")
# --- end of Startti client ---
