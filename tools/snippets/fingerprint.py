# --- Huella de resultados (no editar) ---
def results_fingerprint(results):
    payload = json.dumps({"session": SESSION, "student": STUDENT_ID.strip(), "results": results},
                         sort_keys=True, default=str, ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()[:12]

print(json.dumps({"CONFIG": CONFIG, "RESULTS": RESULTS}, indent=2, ensure_ascii=False, default=str))
print("🔏 Huella de resultados:", results_fingerprint({"CONFIG": CONFIG, "RESULTS": RESULTS}))
