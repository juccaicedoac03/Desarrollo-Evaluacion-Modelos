# Course Build — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete 12-session virtual course "Desarrollo y Evaluación de Modelos Propios" (Rosario GSB): interactive HTML theory decks, Kaggle lab + graded challenge notebooks, session guides, global methodology/assessment docs, final project kit, filled institutional course guide, and a GitHub Pages portal.

**Architecture:** Static repo published with GitHub Pages. Decks are reveal.js 5 pages sharing one theme (`assets/css/course.css`) and one component library (`assets/js/course.js`). Notebooks are authored in jupytext percent format and committed as clean `.ipynb`; shared code (setup, personalization, fingerprint, Startti client) is copied verbatim from `tools/snippets/`, and `tools/check_notebooks.py` enforces it. `tools/smoke_test.py` executes every notebook with `COURSE_FAST_DEV_RUN=1`.

**Tech Stack:** reveal.js 5.1.0 (jsDelivr CDN), KaTeX (reveal math plugin), vanilla JS/SVG; Python 3.11+ on Kaggle, PyTorch, Hugging Face transformers/datasets/evaluate/peft, scikit-learn, Gradio, CodeCarbon, Optuna, sacrebleu, rouge_score; Startti ADP API; jupytext/nbformat/nbclient for tooling; python-docx-free XML editing for the .docx.

**Spec:** `docs/superpowers/specs/2026-09-30-diseno-curso-design.md`

## Global Constraints

- Language: slides (`slides.html`, including speaker notes) and `lab.ipynb` in **English**. The single "Session Challenge" briefing slide inside each deck is in **Spanish**. `challenge.ipynb`, all rubrics, grading keys, session `README.md`, `docs/*.md`, `proyecto-final/**`, `guia-de-asignatura/**`, `index.html`, root `README.md` in **Spanish**.
- Session length: 180 min = warm-up 10' · theory 60' · break 10' · guided lab 60' · Session Challenge 40'.
- Grading: 0.0–5.0 scale, pass 3.0. 70% sessions (best 10 of 11 challenges × 7%) + 30% final project (technical deliverable 15%, presentation & demo 10%, individual defense 5%) × peer-evaluation factor 0.7–1.0.
- Challenge rubric: Ejecución técnica 40% · Análisis e interpretación 40% · Reflexión + registro de IA 20%. Missing AI log ⇒ that component = 0. Micro-viva failure ⇒ challenge capped at 3.0.
- Challenge submission: download `.ipynb` from Kaggle, upload to e-Aulas as `S<NN>_<codigo>.ipynb`, deadline 23:59 same day.
- Repo URL: `https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos` · Pages URL: `https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/`
- Open-in-Kaggle URL pattern: `https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/<path>.ipynb` · Colab fallback: `https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/<path>.ipynb`
- Startti API: base `https://api.startti.ai`, `POST /v1/run` with `Authorization: Bearer <key>`, body `{agentId, prompt, sessionKey?}`, response `{sessionId, sessionKey, output:{text, suspended, suspendQuestions, errorText}}`. Agent must be **published** (409 otherwise); 402 = plan limit; 401 = bad key. Key lives in Kaggle Secrets as `STARTTI_API_KEY`; never in code.
- Every Startti-dependent cell must degrade gracefully when no key is present (print instructions or fall back to the Python bot) so the smoke test and the no-account alternative work.
- Models (small, open, ungated only): `HuggingFaceTB/SmolLM2-135M-Instruct`, `HuggingFaceTB/SmolLM2-360M-Instruct`, `Qwen/Qwen2.5-0.5B-Instruct`, `distilbert/distilbert-base-uncased`, `google-bert/bert-base-uncased`, `openai-community/gpt2`, `distilbert/distilgpt2`, `google/flan-t5-small`, `Helsinki-NLP/opus-mt-en-es`, `sentence-transformers/all-MiniLM-L6-v2`, `dslim/bert-base-NER`, `distilbert/distilbert-base-uncased-finetuned-sst-2-english`, `ProsusAI/finbert`.
- Verified datasets (datasets 5.x; script-based ones fail): `legacy-datasets/banking77` (NOT `PolyAI/banking77`), `stanfordnlp/sst2`, `fancyzhx/ag_news`, `zalando-datasets/fashion_mnist`, `abisee/cnn_dailymail` config `3.0.0` (use `streaming=True`), `Helsinki-NLP/opus_books` config `en-es`, `zeroshot/twitter-financial-news-sentiment` (0 bearish, 1 bullish, 2 neutral), `gretelai/symptom_to_diagnosis` (`input_text`, `output_text`), `allenai/sciq`, `stanfordnlp/imdb`, `SetFit/amazon_reviews_multi_es`.
- transformers compatibility (Kaggle may run 4.4x–5.x; local is 5.17): never pass `torch_dtype`/`dtype`, `evaluation_strategy`, or `Trainer(tokenizer=...)`. Use `eval_strategy`, pass a `DataCollatorWithPadding(tokenizer)` instead of `tokenizer=`. `DEVICE` is `"cuda"` or `"cpu"` (no MPS).
- `FAST_DEV_RUN` must shrink every data size, epoch count, and generation length so each notebook runs on a CPU laptop in < 6 min. It must not change the code path (same functions, smaller numbers).
- Gradio: never call `.launch()` when `FAST_DEV_RUN` is true. Use `demo.launch(share=True)` otherwise.
- No notebook outputs committed (`check_notebooks.py` enforces).
- Instructor-only material goes in `instructor/` (git-ignored). Never put answer keys in public files.
- Bibliography: prefer primary sources; include women-authored work (template requirement) and at least one Spanish/LatAm source per session README where natural. No fabricated statistics, cases, or URLs — if unsure of a figure, omit it.
- Fictional companies only for scenarios (e.g., "Andes Bank", "NovaTel"); never impersonate real brands.

## File Structure

```
.gitignore  .nojekyll  index.html  README.md
assets/css/course.css                 # deck theme + component styles
assets/js/course.js                   # Course.init + components + chart helpers
tools/requirements-dev.txt
tools/snippets/setup_lab.py           # canonical lab setup cell (EN)
tools/snippets/setup_challenge.py     # canonical challenge header + personalization (ES)
tools/snippets/fingerprint.py         # canonical results fingerprint cell (ES)
tools/snippets/startti_client.py      # canonical Startti client cell
tools/snippets/ai_log.md              # canonical AI-log + reflection markdown (ES)
tools/snippets/course_snippets.py     # importable copy for unit tests
tools/tests/test_snippets.py          # pytest for snippets
tools/check_notebooks.py              # structure/language/snippet checks
tools/check_links.py                  # relative link checker
tools/smoke_test.py                   # executes notebooks in fast mode
sessions/_template/slides.html        # reference deck skeleton
sessions/NN-<slug>/{README.md,slides.html,lab.ipynb,challenge.ipynb,data/}
docs/{metodologia,evaluacion,politica-uso-ia,configuracion-kaggle,configuracion-startti}.md
proyecto-final/{README.md,rubrica.md,plantillas/*.md}
guia-de-asignatura/{guia-de-asignatura.docx,guia-de-asignatura.md}
instructor/README.md, instructor/sessions/NN-<slug>.md   (git-ignored)
```

Session slugs: `01-intro-generative-models`, `02-training-generative-models`, `03-transfer-learning`, `04-fine-tuning`, `05-evaluating-generative-models`, `06-basic-ai-applications`, `07-chatbots-and-agents`, `08-generative-classifiers`, `09-real-world-use-cases`, `10-ethics-and-sustainability`, `11-continuous-improvement`, `12-integrative-project`.

---

## Shared interfaces (produced by Tasks 1–3, consumed by all session tasks)

### Deck skeleton (`sessions/_template/slides.html`)

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>S01 · Introduction to Generative and Pretrained Models</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/monokai.css">
<link rel="stylesheet" href="../../assets/css/course.css">
</head>
<body>
<div class="reveal"><div class="slides">
  <section class="title-slide" data-session="01"> ... </section>
  ...
</div></div>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/math/math.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/highlight.js"></script>
<script src="../../assets/js/course.js"></script>
<script>
  Course.init({ session: "01" });
  Course.onReady(() => { /* deck-specific simulators */ });
</script>
</body>
</html>
```

### CSS classes (`assets/css/course.css`)

- Layout: `.title-slide`, `.section-slide` (section divider, `data-block="theory|lab|challenge|warmup"`), `.cols` (2-col grid), `.cols-3`, `.card`, `.callout` (+ `.callout.warn`, `.callout.tip`, `.callout.business`), `.kicker` (small caps label above a title), `.small`, `.muted`, `.center`, `.big-number`, `.pill`, `.tag`.
- Block tags: `<span class="block-tag" data-block="theory">Theory · 60'</span>` (also `warmup`, `lab`, `challenge`, `break`).
- Agenda: `<ol class="agenda" data-current="theory"><li data-block="warmup">…</li>…</ol>` — current block highlighted.
- Buttons/links: `.btn`, `.btn-kaggle`, `.btn-colab`.
- Tables: `table.compact`.
- Interactive containers: `.quiz`, `.timer`, `.flip-card`, `.prompt-card[data-kind="poll|chat|breakout|think"]`, `.sim` (wrapper for a simulator: `.sim-controls` + `.sim-output`).

### JS API (`assets/js/course.js`, global `Course`)

```js
Course.init({ session: "01" })        // Reveal.initialize(...) with plugins + auto-init components
Course.onReady(fn)                    // run fn after Reveal is ready and components are mounted
Course.softmax(logits: number[], temperature = 1): number[]
Course.sample(probs: number[], rng = Math.random): number          // index
Course.topK(probs: number[], k: number): number[]                  // renormalized probs, zeros outside top-k
Course.seededRandom(seed: number): () => number                    // mulberry32 PRNG
Course.barChart(el: Element, labels: string[], values: number[],
                opts?: { max?: number, format?: (v)=>string, highlight?: number, color?: string }): void
Course.lineChart(el: Element, series: {name: string, points: [number, number][]}[],
                 opts?: { xLabel?: string, yLabel?: string, yMax?: number, yMin?: number }): void
Course.bindRange(input: HTMLInputElement, output: Element | null,
                 fmt?: (v:number)=>string, onChange?: (v:number)=>void): void // fires once on bind
Course.tokenize(text: string): string[]                            // lowercase word tokens
Course.ngrams(tokens: string[], n: number): string[]
```

Declarative components (auto-mounted):

```html
<div class="quiz" data-correct="b">
  <p class="quiz-q">Which model family predicts the next token?</p>
  <button class="quiz-opt" data-key="a">Autoencoding (BERT)</button>
  <button class="quiz-opt" data-key="b">Autoregressive (GPT)</button>
  <div class="quiz-explain">GPT-style models factorize p(x) left to right.</div>
</div>

<div class="timer" data-minutes="5" data-label="Breakout rooms"></div>

<div class="flip-card"><div class="front">Question</div><div class="back">Answer</div></div>

<div class="prompt-card" data-kind="breakout"><h4>Breakout · 6 min</h4><p>…</p></div>
```

### Canonical notebook snippets (`tools/snippets/`) — copy verbatim

`setup_lab.py` (first code cell of every `lab.ipynb`; add `ensure(...)` lines below the marked line as needed):

```python
# --- Course setup (do not edit) ---
import os, sys, random, subprocess, importlib
FAST_DEV_RUN = os.environ.get("COURSE_FAST_DEV_RUN") == "1"  # used by the course smoke test
IN_KAGGLE = "KAGGLE_KERNEL_RUN_TYPE" in os.environ
IN_COLAB = "google.colab" in sys.modules

def ensure(package, import_name=None):
    """Install a package only if it is missing (Kaggle already ships most of them)."""
    try:
        importlib.import_module(import_name or package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", package], check=True)

import numpy as np
import torch
SEED = 42
random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {DEVICE} | Kaggle: {IN_KAGGLE} | Colab: {IN_COLAB} | Fast dev run: {FAST_DEV_RUN}")
# --- end of course setup ---
```

`setup_challenge.py` (first code cell of every `challenge.ipynb`; set `SESSION` value per session):

```python
# ✏️ Escribe tu código estudiantil (como aparece en e-Aulas) y tu nombre completo.
STUDENT_ID = ""
STUDENT_NAME = ""

# --- Configuración del curso (no editar) ---
import os, sys, random, subprocess, importlib, hashlib, json
SESSION = "S01"
FAST_DEV_RUN = os.environ.get("COURSE_FAST_DEV_RUN") == "1"
IN_KAGGLE = "KAGGLE_KERNEL_RUN_TYPE" in os.environ
IN_COLAB = "google.colab" in sys.modules
if FAST_DEV_RUN and not STUDENT_ID.strip():
    STUDENT_ID, STUDENT_NAME = "000000", "Prueba automática"
assert STUDENT_ID.strip(), "⚠️ Escribe tu STUDENT_ID en la primera línea de esta celda y vuelve a ejecutarla."

def ensure(package, import_name=None):
    """Instala un paquete solo si falta."""
    try:
        importlib.import_module(import_name or package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", package], check=True)

PERSONAL_SEED = int(hashlib.sha256(f"{SESSION}:{STUDENT_ID.strip()}".encode()).hexdigest()[:8], 16)
rng = random.Random(PERSONAL_SEED)

def pick(options):
    """Elige una opción de forma determinística a partir de tu código estudiantil."""
    return rng.choice(list(options))

import numpy as np
import torch
random.seed(PERSONAL_SEED); np.random.seed(PERSONAL_SEED % (2**32)); torch.manual_seed(PERSONAL_SEED)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Sesión {SESSION} | Estudiante: {STUDENT_NAME} ({STUDENT_ID}) | Semilla personal: {PERSONAL_SEED} | Dispositivo: {DEVICE}")
# --- fin de la configuración ---
```

The second code cell of every challenge defines `CONFIG = {...}` using `pick(...)` and prints it under the heading "Tu configuración personal".

`fingerprint.py` (last code cell of every challenge; the challenge fills `RESULTS` before it):

```python
# --- Huella de resultados (no editar) ---
def results_fingerprint(results):
    payload = json.dumps({"session": SESSION, "student": STUDENT_ID.strip(), "results": results},
                         sort_keys=True, default=str, ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()[:12]

print(json.dumps({"CONFIG": CONFIG, "RESULTS": RESULTS}, indent=2, ensure_ascii=False, default=str))
print("🔏 Huella de resultados:", results_fingerprint({"CONFIG": CONFIG, "RESULTS": RESULTS}))
```

`startti_client.py` (used in S06, S07, S09 labs and challenges):

```python
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
```

`ai_log.md` (markdown cell right before the fingerprint cell in every challenge):

```markdown
## 🪞 Reflexión y registro de uso de IA (20%)

### Reflexión (responde en 3–5 líneas cada una)
1. ¿Qué aprendiste hoy que puedas aplicar en tu trabajo u organización?
2. ¿Qué fue lo más difícil y cómo lo resolviste?
3. Autoevaluación: ¿qué nota (0.0–5.0) te pondrías en este challenge y por qué?

### 🤖 Registro de uso de IA (obligatorio)
| # | Herramienta (ChatGPT, Claude, Codex, Copilot…) | ¿Para qué la usaste? | Prompt principal (resumido) | ¿Qué verificaste o corregiste de su respuesta? |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |

> Si no usaste asistentes de IA, escribe: *"No usé asistentes de IA en este challenge."* Recuerda: puedes usar IA, pero **eres responsable de todo lo que entregas** y podrías ser seleccionado(a) para una micro-sustentación.
```

### Challenge notebook anatomy (all sessions 01–11, Spanish)

1. Markdown header: `# Challenge de la Sesión NN — <título en español>`, badges (Kaggle/Colab), and a box with: modalidad individual; 40 min en clase + entrega hasta 23:59; IA permitida con registro; micro-sustentaciones; rúbrica (40/40/20); instrucciones de entrega (`Archivo → Descargar notebook` → subir a e-Aulas como `SNN_<codigo>.ipynb`).
2. Code: `setup_challenge.py` verbatim (with the session's `SESSION`).
3. Code: `CONFIG = {...}` via `pick(...)`, printed as "Tu configuración personal".
4. 3–4 tasks, each a markdown heading `## Tarea N — <nombre> (<componente de rúbrica>)` with clear instructions, followed by code (`# ✏️ TU CÓDIGO AQUÍ` scaffolds that already run end-to-end in fast mode with sensible defaults) and/or a markdown answer cell starting with `**Tu respuesta:**`.
   - Always includes one **"Explica y decide"** task (business/technical decision citing own numbers) and one **"Crítica a la IA"** task (given AI-generated text/code with 2–3 planted errors: find, explain, fix).
5. Code: `RESULTS = {...}` collecting the student's key numbers (rounded to 4 decimals).
6. Markdown: `ai_log.md` verbatim.
7. Code: `fingerprint.py` verbatim.

### Lab notebook anatomy (sessions 01–11, English)

1. Markdown header: title, session, learning objectives, time plan (60 min, by part), Kaggle/Colab badges, **Kaggle checklist** (Settings → Accelerator GPU T4 x2 when needed; Internet on; for Startti sessions: Add-ons → Secrets → `STARTTI_API_KEY`).
2. Code: `setup_lab.py` verbatim + session `ensure(...)` lines.
3. Parts (`## Part 1 — …`), each with short explanations tied to the slides, runnable code, **✋ Checkpoint** markdown questions for the Zoom chat, and **🧪 Try it** mini-exercises with a `<details><summary>Show a solution</summary>…</details>` block.
4. `## Wrap-up` with key takeaways and a pointer to the challenge.

### Deck anatomy (sessions 01–11; ~30–45 slides, English except the challenge slide)

1. Title slide (session number, English title, Spanish subtitle, course, program, "Universidad del Rosario · Rosario GSB").
2. Agenda slide (`.agenda`, current = warmup).
3. Warm-up: 2–3 `.quiz` retrieval questions on the previous session (S01: diagnostic about participants' background + 2 AI-literacy quizzes).
4. Learning objectives mapped to RAE numbers (RAE 1–6 from the syllabus).
5. Theory in 3–4 sections (`.section-slide`), with an interaction at least every ~10 minutes: `.quiz`, a session-specific `.sim` simulator (≥ 2 per deck), `.prompt-card` poll/chat, a breakout activity with `.timer`.
6. At least one "Business lens" slide (`.callout.business`) per section.
7. Break slide with `.timer` (10').
8. Lab bridge slide: what we'll build + `.btn-kaggle`/`.btn-colab` links to `lab.ipynb`.
9. **Challenge slide in Spanish**: tareas, reglas de IA, micro-sustentaciones, entrega; `.btn-kaggle` to `challenge.ipynb`; `.timer` 40'.
10. Wrap-up: key takeaways, exit question, next session + pre-work, references.
11. Every slide has `<aside class="notes">` speaker notes (English) with timing cues.

### Session README anatomy (Spanish)

```markdown
# Sesión NN — <English title>
*<Título en español>*

**RAE asociados:** RAE x, RAE y · **Duración:** 3 horas (virtual)

## Objetivos de la sesión
## Agenda
| Bloque | Tiempo | Actividad |
## Antes de la clase (≈2 h)
## Materiales
| Material | Enlace |
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/NN-slug/slides.html) |
| Lab guiado | [Kaggle](<kaggle url>) · [Colab](<colab url>) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](<kaggle url>) · [Colab](<colab url>) · [archivo](challenge.ipynb) |
## Challenge de la sesión (evaluación)
(tareas resumidas, rúbrica 40/40/20, entrega, reglas de IA)
## Después de la clase (trabajo independiente ≈7 h)
## Lecturas y recursos
```

### Instructor file anatomy (`instructor/sessions/NN-slug.md`, Spanish, git-ignored)

Facilitation timeline (minute by minute), common student issues and fixes, expected result ranges per CONFIG option, model answers for every task, list of planted errors in the "Crítica a la IA" task with corrections, 5 micro-viva questions, grading guidance per rubric level (5.0 / 4.0 / 3.0 / <3.0).

---

## Task 1: Repository scaffolding and tooling

**Files:**
- Create: `.gitignore`, `.nojekyll`, `tools/requirements-dev.txt`, `tools/snippets/*` (5 files above + `course_snippets.py`), `tools/tests/test_snippets.py`, `tools/check_notebooks.py`, `tools/check_links.py`, `tools/smoke_test.py`

**Interfaces:**
- Produces: `python tools/check_notebooks.py [paths]` → exit 0 when all notebooks satisfy: valid nbformat 4; no outputs/execution counts; labs start with the exact `setup_lab.py` block; challenges contain exact `setup_challenge.py` (modulo `SESSION` value), a `CONFIG` cell, a `RESULTS` assignment, the exact `ai_log.md` text and the exact `fingerprint.py` block; Startti sessions contain the exact `startti_client.py` block when they call `startti_run`.
- Produces: `python tools/smoke_test.py [paths] [--timeout 900]` → executes each notebook (copy, not in place) with `COURSE_FAST_DEV_RUN=1`, `KERAS_BACKEND=torch`, prints `PASS/FAIL <path> <seconds>` and the failing cell source + traceback; exit 1 on any failure.
- Produces: `python tools/check_links.py` → verifies every relative `href`/`src` in `*.html` and every relative markdown link in `*.md` exists (ignores `http(s):`, `mailto:`, `#` anchors); exit 1 on broken links.

- [ ] Step 1: Write `tools/tests/test_snippets.py` (determinism of `PERSONAL_SEED`/`pick`, fingerprint stability, `startti_run` error mapping with a mocked `requests.post`) against `tools/snippets/course_snippets.py`.
- [ ] Step 2: Run `pytest tools/tests -q` → fails (module missing).
- [ ] Step 3: Implement snippets + `course_snippets.py`; run tests → pass.
- [ ] Step 4: Implement the three checkers; run `check_notebooks.py` on a hand-made good and bad notebook in a temp dir → exit 0 / exit 1.
- [ ] Step 5: Commit `chore: add course tooling and canonical notebook snippets`.

## Task 2: Deck framework

**Files:** Create `assets/css/course.css`, `assets/js/course.js`, `sessions/_template/slides.html`

- [ ] Step 1: Implement CSS (brand tokens: `--brand:#9E1B32; --ink:#1d1d1f; --muted:#5f6368; --accent:#0F766E; --accent-2:#B45309; --surface:#f6f4f2; --bg:#ffffff`; fonts Inter + JetBrains Mono from Google Fonts) and all classes listed above.
- [ ] Step 2: Implement `course.js` API exactly as specified above.
- [ ] Step 3: Build the template deck exercising every component (quiz, timer, flip-card, prompt-card, agenda, a softmax/temperature `.sim` with `barChart`, a `lineChart`).
- [ ] Step 4: Open the template in the browser pane; verify no console errors, quiz feedback works, timer counts, sliders update charts, speaker notes exist.
- [ ] Step 5: Commit `feat: add reveal.js deck theme and interactive components`.

## Task 3: Session 01 — reference implementation

Build all Session 01 files per the anatomies above, then review before the other sessions start (it is the style reference they copy).

**Content — S01 Introduction to Generative and Pretrained Models (RAE 1, 4, 5)**
- Deck sections: (1) What is generative AI — discriminative p(y|x) vs generative p(x), p(x,y); examples in text/image/audio/code. (2) Model families — autoregressive (GPT), autoencoding (BERT), seq2seq (T5), VAEs, GANs, diffusion; pretrained/foundation models and the pretrain → adapt paradigm (Bommasani et al., 2021). (3) Own models vs APIs — the adaptation spectrum prompting → RAG → fine-tuning → training from scratch; cost, control, privacy, IP; "build vs buy" business lens. (4) Tools & frameworks — PyTorch, TensorFlow/Keras, JAX, Hugging Face (Hub, transformers, datasets, PEFT), Kaggle/Colab compute; applications of AI across sectors; course roadmap & project preview & assessment model (one slide in Spanish summarizing 70/30 and AI policy).
- Simulators: next-token sampling (fixed toy vocabulary + logits; temperature and top-k sliders → `barChart` of probabilities + "sample 10 tokens" button); build-vs-buy decision widget (sliders for data sensitivity, volume, customization need → recommended position on the spectrum with explanation).
- Breakout (6'): classify 5 business scenarios on the adaptation spectrum.
- Lab parts: (1) Kaggle tour + PyTorch tensors & autograd (fit y = 3x + 2 with gradient descent, 20 lines); (2) same model in Keras (3 lines of model code; note Keras 3 multi-backend); (3) Hugging Face pipelines — sentiment (`distilbert-base-uncased-finetuned-sst-2-english`), zero-shot classification skipped if heavy (use `pipeline("fill-mask", "google-bert/bert-base-uncased")` instead), text generation with `HuggingFaceTB/SmolLM2-135M-Instruct` using the chat template; (4) tokenization peek (tokens, ids, English vs Spanish token counts) and generation parameters (temperature, top_k, top_p, max_new_tokens) with a side-by-side table.
- Challenge (SESSION="S01"): CONFIG picks `prompts` (3 of a pool of 9 business prompts), `temperatures` (2 of [0.2, 0.7, 1.0, 1.3]), `scenario` (1 of 8 build-vs-buy business scenarios, fictional companies). Tasks: T1 Ejecución — generate 5 samples per prompt × temperature with SmolLM2-135M-Instruct, compute distinct-1/distinct-2 and average length (helper provided); T2 Análisis — interpret how temperature changed diversity/quality in *their* numbers and pick the best temperature per prompt; T3 Explica y decide — recommend where on the adaptation spectrum their scenario should sit (cost, data, privacy, control; ≥ 1 risk); T4 Crítica a la IA — an "AI-written" paragraph comparing BERT vs GPT with 3 planted errors (e.g., "BERT generates text left-to-right", "GPT uses masked language modeling", "fine-tuning always requires training from scratch") to find/fix. RESULTS: distinct metrics per temperature.
- Instructor file per anatomy.

- [ ] Step 1: Write `sessions/01-intro-generative-models/slides.html`, `lab.ipynb`, `challenge.ipynb`, `README.md`, `instructor/sessions/01-intro-generative-models.md`.
- [ ] Step 2: `python tools/check_notebooks.py sessions/01-intro-generative-models` → exit 0.
- [ ] Step 3: `python tools/smoke_test.py sessions/01-intro-generative-models` → PASS both.
- [ ] Step 4: Open deck in browser; no console errors; simulators work.
- [ ] Step 5: Commit `feat: add session 01 materials`.

## Tasks 4–13: Sessions 02–11 (parallelizable after Task 3 is approved)

Each task: create `sessions/NN-slug/{slides.html, lab.ipynb, challenge.ipynb, README.md, data/*}` and `instructor/sessions/NN-slug.md` following the anatomies and Session 01 as the style reference; run `check_notebooks.py` on the folder (exit 0) and `python -m py_compile` on the jupytext `.py` export; commit `feat: add session NN materials`. Smoke tests are executed centrally and sequentially (8 GB RAM machine) in Task 18.

### Task 4 — S02 Training Generative Models (RAE 1, 2)
- Deck: training loop anatomy (forward → loss → backward → step); losses (cross-entropy, MSE, KL divergence); optimizers (SGD, momentum, Adam/AdamW), learning rate, schedules, batch size; overfitting, regularization, early stopping; data preprocessing (cleaning, normalization, tokenization, splits, leakage) with a business-data example; autoencoders → VAEs (latent space, reparameterization trick, ELBO = reconstruction − KL, β-VAE); short comparison VAE vs GAN vs diffusion.
- Simulators: learning-rate playground (gradient descent on a 1-D non-convex loss, LR + steps sliders, shows divergence/oscillation/convergence via `lineChart`); overfitting explorer (train vs validation curves for model-capacity slider, precomputed synthetic curves).
- Breakout: find 5 preprocessing pitfalls in a described CRM dataset.
- Lab: Fashion-MNIST (`zalando-datasets/fashion_mnist`) VAE in PyTorch — data → tensors normalized to [0,1]; MLP encoder/decoder, latent_dim=8; ELBO loss; train loop with loss curves; reconstructions grid; sampling from prior; latent interpolation between two items; quick SGD vs Adam comparison (1 epoch each).
- Challenge: CONFIG picks `latent_dim` ∈ {2, 4, 8, 16}, `beta` ∈ {0.5, 1, 2, 4}, `lr` ∈ {1e-3, 3e-3}, `classes` (3 of 10 garment classes). T1 train VAE on their classes; report recon loss and KL; T2 compare against baseline (latent 8, β 1) they also run; interpret trade-off reconstruction vs KL using their numbers; T3 Explica y decide — config for a fictional apparel retailer's "new product mock-up" generator; T4 Crítica a la IA — AI-written training loop with planted bugs (missing `optimizer.zero_grad()`, KL sign flipped, `model.eval()` left on during training); fix and rerun. RESULTS: losses.

### Task 5 — S03 Pretrained Models and Transfer Learning (RAE 1, 3)
- Deck: why pretraining works (self-supervision, scale); Transformer essentials (tokens, embeddings, self-attention with the QKᵀ/√d formula, multi-head, positional encoding, encoder vs decoder); BERT (MLM, [CLS]), GPT (causal LM), T5 (text-to-text); tokenization (WordPiece, BPE) and its cost impact for Spanish; transfer strategies: zero-shot, few-shot (in-context), feature extraction (frozen encoder + head), partial/full fine-tuning, domain adaptation; choosing a model (size, license, language, model card); Spanish models (BETO — Cañete et al., 2020).
- Simulators: attention heatmap for a fixed sentence (hover a token → its attention row; toy matrices for 2 heads); token-cost calculator (words → tokens ratio EN vs ES × price per 1K tokens × monthly volume).
- Breakout: choose a transfer strategy for 4 scenarios given labeled-data size, budget, latency.
- Lab: tokenization comparison (BERT vs GPT-2 tokenizers on EN/ES sentences); fill-mask with BERT; sentence embeddings (`sentence-transformers/all-MiniLM-L6-v2`) + logistic regression on `fancyzhx/ag_news` subset (feature extraction); zero-shot and few-shot classification by prompting `Qwen/Qwen2.5-0.5B-Instruct` with the chat template; accuracy/time comparison table. Announce project groups (groups of 3) at the end.
- Challenge: CONFIG picks `k_train` ∈ {16, 64, 256, 1024} (examples per class for feature extraction), `n_shots` ∈ {1, 2, 4}, `classes` (all 4 ag_news classes but a personal random test slice via seed), `business_case` from a pool of 6. T1 embeddings + LR with their k; plus learning curve over [16, 64, 256] (fast mode smaller); T2 few-shot LLM on the same 40-example test slice; compare accuracy/latency; T3 Explica y decide — strategy for their business case; T4 Crítica a la IA — AI explanation of attention/transfer learning with 3 planted errors.

### Task 6 — S04 Fine-Tuning Generative Models (RAE 1, 2)
- Deck: full fine-tuning vs PEFT (adapters, LoRA — W = W₀ + BA, QLoRA, prompt/prefix tuning); instruction tuning & SFT data format (chat templates); hyperparameters (lr, epochs, batch size, warmup, weight decay, max length; LoRA r, alpha, dropout, target modules); catastrophic forgetting; overfitting on small data; building custom datasets (collection, labeling guidelines, quality > quantity, splits, privacy); API fine-tuning (OpenAI docs) vs open models; decision guide "prompt → RAG → fine-tune".
- Simulators: LoRA parameter calculator (hidden size, layers, r, targeted matrices → trainable params and % of total, memory estimate); hyperparameter "tuning game" (choose lr/epochs → shows one of precomputed curve shapes: underfit/good/overfit/diverge with explanation).
- Breakout: draft labeling guidelines for a 5-intent customer-service dataset.
- Lab: Part A — `distilbert/distilbert-base-uncased` fine-tuned on a 10-intent subset of `legacy-datasets/banking77` with `Trainer` (tokenize, `DataCollatorWithPadding`, `TrainingArguments(eval_strategy="epoch")`, `compute_metrics` accuracy/F1 macro), inference on new messages. Part B — LoRA SFT (`peft.LoraConfig`) of `HuggingFaceTB/SmolLM2-135M-Instruct` on `sessions/04-fine-tuning/data/brand_voice.jsonl` (40 instruction→response pairs, fictional company "Andes Bank" friendly brand voice, English) with a manual PyTorch training loop or `Trainer`; before/after generations.
- Challenge: CONFIG picks `intents` (10 of 77 Banking77 labels via seed), `config_a`/`config_b` (two of lr ∈ {2e-5, 5e-5, 1e-4} × epochs ∈ {1, 2, 3}), `domain` for decision. T1 fine-tune DistilBERT on their intents with config A; report accuracy/macro-F1; T2 run config B, compare and interpret (overfitting? underfitting?); T3 Explica y decide — FT vs RAG vs prompting for their domain; T4 Crítica a la IA — AI-proposed `TrainingArguments` with bad choices (lr 5e-2, 50 epochs on 200 examples, no eval, test set used for model selection) to critique and fix.

### Task 7 — S05 Evaluating Generative Models (RAE 2)
- Deck: why evaluating generation is hard; intrinsic vs extrinsic; perplexity (definition exp(mean NLL), tokenizer dependence); BLEU (modified n-gram precision, brevity penalty), ROUGE-1/2/L, chrF (Popović, 2015), semantic similarity/BERTScore (Zhang et al., 2020); human evaluation and LLM-as-a-judge (Zheng et al., 2023) with its biases; classification metrics (precision, recall, F1, confusion matrix); validation (holdout, k-fold, stratification, leakage); error analysis workflow; linking metrics to business KPIs.
- Simulators: live BLEU/ROUGE calculator (two textareas; shows n-gram matches, precision per n, brevity penalty, BLEU, ROUGE-1/L recall/F1 — implemented with `Course.tokenize`/`Course.ngrams`); threshold explorer (slider over scores of 40 synthetic examples → precision/recall/F1 and confusion matrix).
- Breakout: pick metrics for 4 products (translation for a call center, meeting summarizer, FAQ bot, fraud flagger).
- Lab: perplexity of `openai-community/gpt2` on news vs tweets vs Spanish text; EN→ES translation with `Helsinki-NLP/opus-mt-en-es` on `Helsinki-NLP/opus_books` en-es samples → sacrebleu BLEU and chrF; summarization with `google/flan-t5-small` on `abisee/cnn_dailymail` (streaming) → ROUGE via `evaluate`/`rouge_score`; semantic similarity with MiniLM embeddings; stratified 5-fold CV of TF-IDF + LogisticRegression on a Banking77 subset; confusion analysis of top confused intent pairs.
- Challenge: CONFIG picks `sample_ids` (8 cnn_dailymail validation items via seed, streaming), `mt_ids` (20 opus_books pairs), `k` ∈ {3, 5, 10}, `product` for evaluation plan. T1 compute ROUGE/semantic similarity for their summaries and BLEU/chrF for their translations; T2 find one example where the metric disagrees with their human judgment and explain why; T3 Explica y decide — evaluation plan for their product (offline metrics, human eval, business KPI, thresholds); T4 Crítica a la IA — 3 planted errors ("BLEU measures recall", "lower perplexity across different tokenizers is always comparable", "k-fold removes the need for a test set").
- Project milestone: proposal canvas due before S06 (link `proyecto-final/plantillas/propuesta.md`).

### Task 8 — S06 Introduction to Basic Application Development (RAE 3, 4)
- Deck: from model to product (user, job-to-be-done, inputs/outputs, constraints); conceptual design of classifiers and chatbots; architecture patterns (model service, UI, logs, feedback); UX for AI (Amershi et al., 2019 guidelines; Google PAIR People + AI Guidebook): set expectations, show confidence, graceful failure, human handoff; confidence thresholds and human-in-the-loop routing; interface options: Gradio, Streamlit, no-code agent platforms — **Startti ADP** (canvas agents, publish, API); latency/cost; prototyping loop.
- Simulators: routing threshold simulator (slider → % automated vs % to human, accuracy of automated part, cost per 1,000 tickets with editable unit costs); UX anti-pattern spotter (flip-cards).
- Breakout: AI Product Canvas for an assigned case.
- Lab: Part A — Gradio `Blocks` app: Banking77 intent classifier (TF-IDF + LogisticRegression trained in-notebook for speed) with confidence threshold routing ("auto-answer" vs "send to human") and a feedback/flag log; text generator tab with SmolLM2-135M-Instruct + temperature slider. Part B — Startti: create first agent in ADP (step-by-step markdown with the Startti setup doc link), publish it, save API key in Kaggle Secrets, call it via `startti_run` (copy `startti_client.py` verbatim); wrap it in a Gradio `ChatInterface`.
- Challenge: CONFIG picks `use_case` (1 of 6 fictional customer-service contexts with intent subsets of Banking77), `cost_human` and `cost_error` values. T1 train classifier on their intents; compute coverage/accuracy for thresholds 0.3–0.9 and choose the threshold minimizing expected cost with their unit costs; T2 build the Gradio app with their threshold (screenshot or share link in answer); T3 build the equivalent assistant as a Startti agent (or Python alternative) and compare no-code vs code for their use case; T4 Crítica a la IA — AI-proposed UX copy/flow with 3 anti-patterns. Startti cells guarded.
- Homework: Startti account + API key ready for S07 (link `docs/configuracion-startti.md`).

### Task 9 — S07 Implementing Basic Chatbots and Agents (RAE 3, 4, 6)
- Deck: paradigms timeline — rule-based (ELIZA) → intent/entity/slot + dialogue management (**Rasa**: NLU pipeline, stories/rules, CALM flows; **Dialogflow CX**: agents, flows, pages, intents, entity types, webhooks/fulfillment) → LLM chatbots (system prompt, memory, RAG — Lewis et al., 2020) → agents (tools, ReAct — Yao et al., 2023; multi-agent; human-in-the-loop); **Startti ADP**: canvas agents on the Colmena engine, knowledge bases, tools/APIs, sub-agents, publish, API; comparison table Rasa vs Dialogflow CX vs Startti vs custom Python; conversation design (happy path, repair, fallback, human handoff, persona, guardrails, prompt injection); chatbot evaluation: task success, containment, groundedness/hallucination, turns, CSAT; test suites.
- Simulators: clickable dialogue state machine for a "block my card" flow (states highlight as user messages are chosen); paradigm quiz; prompt-injection demo slide (flip-card).
- Breakout: design the flow for an assigned use case (states, slots, fallbacks).
- Lab: Part A (20') — Python bot "under the hood": NLU (TF-IDF + LR on Banking77 subset), slot filling with regex (amounts, last-4 digits), dialogue state dictionary, LLM fallback with `HuggingFaceTB/SmolLM2-360M-Instruct` + chat history, Gradio `ChatInterface`. Part B (40') — Startti: build a customer-service agent with a knowledge base using `sessions/07-chatbots-and-agents/data/faq_andes_bank.md` (fictional bank FAQ, English, ~40 Q&A), publish, then run the **evaluation harness** from Kaggle: `evaluate_agent(agent_fn, test_cases)` where `agent_fn(prompt, session_key) -> str` is either `lambda p, s: startti_run(AGENT_ID, p, s)` or the Python bot; test cases in `data/test_conversations_andes.json` (in-scope, out-of-scope, multi-turn, adversarial); scoring = expected-keyword match for in-scope, refusal/handoff markers for out-of-scope, no system-prompt leakage for adversarial; metrics table.
- Data: create 8 domain FAQ files in Spanish for the challenge in `data/dominios/` (fictional: telecom "NovaTel", e-commerce "MercaLatam", universidad "Universidad Andina Virtual", clínica "Clínica Salud Norte" (citas, no diagnósticos), aseguradora "Seguros Cóndor", aerolínea "Vuela Sur", servicios públicos "EnerCol", banco "Banco Andino") each ~25 Q&A, plus `data/dominios/<dominio>_tests.json` with 12 test conversations each (4 in-scope, 3 out-of-scope, 3 multi-turn, 2 adversarial) with `expected_keywords`/`type`.
- Challenge: CONFIG picks `domain` (1 of 8). T1 build the agent in Startti with their domain FAQ (or Python alternative using the FAQ as retrieval source) and run the 12-case harness; T2 analyze failures by type with their numbers; T3 iterate once (change instructions/KB) and re-run; compare; T4 Explica y decide — is it ready for production? containment vs risk; include a human-handoff policy. (Crítica a la IA folded into T3: an AI-suggested system prompt with 3 flaws to fix.) RESULTS: success rates before/after by type.

### Task 10 — S08 Building Classifiers with Generative Models (RAE 1, 2, 3)
- Deck: generative vs discriminative classifiers (Bayes rule; Naive Bayes / Gaussian discriminant analysis vs logistic regression; Ng & Jordan, 2002 — generative models reach their asymptote faster with little data); neural generative classifiers: class-conditional likelihood scoring with an LM, VAE latent features (Kingma et al., 2014 semi-supervised VAE); LLM zero/few-shot classification (verbalizers, constrained outputs, log-probs); synthetic data augmentation with LLMs and its risks; calibration (Guo et al., 2017); cost/latency/privacy comparison; PyTorch vs TensorFlow implementation notes.
- Simulators: decision-boundary visualizer (2-D Gaussian classes; Gaussian NB vs logistic regression fitted in JS; sample-size slider shows data-efficiency effect); cost calculator (requests/day × tokens × price vs self-hosted small model).
- Breakout: recommend a classifier for 3 business constraints.
- Lab (PyTorch): dataset `zeroshot/twitter-financial-news-sentiment`; (1) MultinomialNB vs LogisticRegression on TF-IDF with learning curve (n = 20…full); (2) PyTorch MLP on MiniLM embeddings; (3) zero-shot classification by label log-likelihood scoring with `Qwen/Qwen2.5-0.5B-Instruct` (compute log p(label tokens | prompt)); (4) synthetic augmentation: generate 30 examples for the minority class with the LLM, retrain, compare; summary table accuracy/macro-F1/latency/est. cost.
- Challenge: CONFIG picks `n_train` ∈ {30, 60, 120, 240}, `minority_class`, `test_slice` (personal 60 examples), `constraint_profile` (budget/latency/privacy). T1 run NB vs LR vs LLM zero-shot on their slice; T2 augmentation experiment for their minority class and interpretation; T3 Explica y decide — recommendation under their constraint profile; T4 Crítica a la IA — AI code with data leakage (TF-IDF fit on full data, synthetic examples in test set, threshold tuned on test) to detect/fix.

### Task 11 — S09 Use Cases: Generative Models in Real Contexts (RAE 4, 5, 6)
- Deck: frameworks for analyzing GenAI use cases (value chain, value × feasibility matrix, risk × impact, KPIs, ROI); economic potential (McKinsey, 2023); productivity evidence (Brynjolfsson, Li & Raymond, "Generative AI at Work", NBER w31161 — customer support; Dell'Acqua et al., 2023 "jagged frontier"); sector deep-dives: health (clinical documentation, triage risk; Med-PaLM — Singhal et al., 2023, Nature), finance (customer service, document processing, fraud; knowledge assistants for advisors), education (tutoring like Khanmigo; feedback generation); documented failures (Moffatt v. Air Canada, 2024 — chatbot liability; NYC MyCity chatbot giving unlawful advice, 2024); success factors; LatAm/Colombia context and data availability; project use-case canvas.
- Simulators: value × feasibility matrix (click to place 6 cases, shows quadrant advice); ROI calculator (volume, time saved, cost per hour, implementation & run cost → payback months).
- Breakout: case analysis canvas for an assigned sector.
- Lab: finance — `ProsusAI/finbert` vs zero-shot LLM on `zeroshot/twitter-financial-news-sentiment`; health — symptom → condition retrieval with MiniLM embeddings on `gretelai/symptom_to_diagnosis` (top-3 accuracy, with explicit "not medical advice" framing); education — question generation from a `allenai/sciq` support paragraph with Qwen2.5-0.5B-Instruct and automatic answerability check; Startti — sector agent prototype with knowledge base (a provided document) called via `startti_run` (guarded).
- Challenge: CONFIG picks `sector` ∈ {salud, finanzas, educación}, `case` (1 of 3 per sector, fictional orgs), ROI parameters. T1 run the sector prototype on their personal sample and measure; T2 case canvas (value, feasibility, risks, KPIs) grounded in their measured numbers; T3 Explica y decide — go/no-go with ROI from the calculator cell with their parameters; T4 Crítica a la IA — AI-written case summary with an invented statistic and a wrong legal claim: verify with sources and correct. Project milestone: groups submit their project use-case canvas (formative).

### Task 12 — S10 Ethics and Sustainability in Generative Models (RAE 2, 6)
- Deck: risk taxonomy (bias, privacy, hallucination, IP/copyright, security — prompt injection & data poisoning, misuse, environmental cost, labor impact; Bender, Gebru et al., 2021); bias along the lifecycle; fairness metrics (demographic parity, equal opportunity) and counterfactual testing; privacy — PII, memorization, anonymization, Colombia's Ley 1581 de 2012 (habeas data), GDPR; frameworks & regulation — EU HLEG Ethics Guidelines for Trustworthy AI (2019), EU AI Act (Regulation (EU) 2024/1689; risk tiers; phased application 2025–2027 — tell students to check current status), NIST AI RMF 1.0 (2023), UNESCO Recommendation on the Ethics of AI (2021), OECD AI Principles, Colombia CONPES 4144 (2025) national AI policy; sustainability — energy/carbon of training and inference (Strubell et al., 2019; Luccioni, Jernite & Strubell, 2024), mitigation; documentation — model cards (Mitchell et al., 2019), datasheets (Gebru et al., 2021); governance practices.
- Simulators: counterfactual bias demo (toggle names/gender in template sentences → precomputed sentiment scores bar chart); carbon calculator (GPU type power, hours, PUE, grid intensity — presets for a hydro-heavy grid like Colombia's vs a coal-heavy grid → kg CO₂e and equivalences).
- Breakout: classify 5 use cases into EU AI Act risk tiers and propose controls.
- Lab: fill-mask bias probing with `google-bert/bert-base-uncased` (occupations × he/she); counterfactual fairness test of `distilbert-base-uncased-finetuned-sst-2-english` with name/gender swaps; PII detection & redaction with `dslim/bert-base-NER` + regex for Colombian formats (cédula, celular, correo — synthetic data only); CodeCarbon measurement of a small inference/fine-tune run; write a model card (markdown template filled programmatically).
- Challenge: CONFIG picks `attribute_pair` (gender, nationality/region, age), `templates` (6 of 15), `model` (sst-2 classifier or fill-mask), `use_case` for regulation. T1 run the bias audit and compute their disparity metric; T2 mitigation attempt (counterfactual augmentation of templates or threshold adjustment) and re-measure; T3 Explica y decide — classify their use case under EU AI Act + Colombian framework and recommend controls; T4 Crítica a la IA — AI-written ethics statement with 3 errors (e.g., "anonymized data is outside all data protection law", "the EU AI Act bans all facial recognition", "smaller models are always less biased"). Include a mini model-card section in the answer.

### Task 13 — S11 Evaluation and Continuous Model Improvement (RAE 2, 6)
- Deck: the ML lifecycle and continuous improvement loop (Sculley et al., 2015 technical debt; Huyen, 2022); error analysis → hypotheses → targeted fixes; data-centric vs model-centric improvement; label noise (confident learning — Northcutt et al., 2021); experiment tracking and reproducibility (seeds, versioning, MLflow/W&B concepts); hyperparameter optimization (grid, random, Bayesian/Optuna — Akiba et al., 2019; early stopping); robustness and behavioral testing (CheckList — Ribeiro et al., 2020), distribution shift; efficiency (quantization, distillation — Hinton et al., 2015; DistilBERT — Sanh et al., 2019; pruning; batching); monitoring in production (data drift, feedback loops, A/B tests); LLMOps (eval suites, regression tests for prompts/agents).
- Simulators: improvement-loop diagram (click stages to reveal practices); quantization demo (bits slider → model memory for 0.5B/7B params, and rounding error on a sample weight vector).
- Breakout: plan the improvement roadmap for your project (groups).
- Lab: baseline TF-IDF + LR on a Banking77 subset with injected label noise (10%); error analysis by slice (text length, intent); fixes: detect likely mislabeled examples via cross-validated predicted probabilities and relabel/drop; augmentation of weak intents; Optuna search (20 trials, fast mode 3) over C and n-gram range; CheckList-style tests (typos, casing, negation, adding irrelevant text) with pass rates; DistilBERT dynamic int8 quantization (`torch.quantization.quantize_dynamic`) size/latency/accuracy comparison on a small eval set (use a sentiment model to avoid training); experiment log DataFrame.
- Challenge: CONFIG picks `noise_rate` ∈ {0.05, 0.1, 0.2}, `intents` subset, `budget_trials`, `deploy_constraints` (max latency, min accuracy, max size). T1 improve over their baseline with ≥ 2 documented iterations in an experiment log; T2 robustness report with their pass rates; T3 Explica y decide — which version to deploy under their constraints; T4 Crítica a la IA — AI "improvement plan" with flawed steps (tuning on test set, dropping all hard examples, reporting best-of-20 seeds). Project milestone: groups document one improvement iteration of their project model (formative).

## Task 14: Session 12 — Integrative project session

**Files:** `sessions/12-integrative-project/{slides.html, README.md}`, `instructor/sessions/12-integrative-project.md`
- Deck (English, facilitation): agenda, presentation order (randomized live with a JS button), timing rules (8' pitch + 3' demo + 4' Q&A) with a `.timer`, evaluation criteria summary (Spanish slide), peer-feedback instructions (Spanish slide with link to the form template), course recap (12 sessions in one visual), what's next (learning paths), closing.
- README (Spanish): logistics, entregables, rubric links, coevaluación.
- [ ] Commit `feat: add session 12 materials`.

## Task 15: Global docs and portal (Spanish)

**Files:** `README.md`, `index.html`, `docs/metodologia.md`, `docs/evaluacion.md`, `docs/politica-uso-ia.md`, `docs/configuracion-kaggle.md`, `docs/configuracion-startti.md`
- `index.html`: standalone page (no reveal), uses brand tokens, lists 12 sessions (title EN + subtitle ES, links to slides, lab/challenge Kaggle buttons, README), links to docs, project and course guide; responsive to 375 px; light/dark via `prefers-color-scheme`.
- `metodologia.md`: pedagogical approach (active learning, light flipped classroom, project-based learning, AI as copilot), session structure, interactivity toolkit for virtual classes (quizzes, simulators, polls, breakout rooms, live coding, micro-vivas), tools (Kaggle, Startti, e-Aulas, Zoom/Teams), independent work distribution (9 h/week), support channels.
- `evaluacion.md`: full scheme (Global Constraints numbers), rubric table with level descriptors, micro-viva protocol, late policy (late ≤ 24 h: −0.5; later: 0 — best 10 of 11 absorbs one miss), fingerprint and personalization explanation, auto/co/heteroevaluación, RAE ↔ activities matrix, project weighting.
- `politica-uso-ia.md`: allowed uses, required disclosure, accountability, verification duty, prohibited (impersonation, fabricated results, sharing personalized outputs), consequences, examples of good/bad AI log entries.
- `configuracion-kaggle.md`: account, phone verification (GPU + internet), opening notebooks via badge, accelerator, internet, Secrets, saving/downloading, quotas (30 GPU h/week), troubleshooting; Colab fallback.
- `configuracion-startti.md`: activating the course license/workspace, creating an agent, knowledge base upload, publishing, creating an API key (shown once), saving it in Kaggle Secrets as `STARTTI_API_KEY`, finding the agent ID, calling `/v1/run`, errors table (401/402/403/404/409), data-protection note (no personal/sensitive data in agents), alternative without account.
- [ ] Commit `docs: add methodology, assessment, AI policy and setup guides`.

## Task 16: Final project kit (Spanish)

**Files:** `proyecto-final/README.md`, `proyecto-final/rubrica.md`, `proyecto-final/plantillas/{propuesta.md, informe-tecnico.md, model-card.md, coevaluacion.md, registro-uso-ia.md, retroalimentacion-pares.md}`
- README: reto, alcance mínimo (spec §6), hitos with sessions, entregables (repo o notebook Kaggle público/privado compartido, informe técnico ≤ 8 páginas, model card, demo Gradio/Startti, video de respaldo opcional ≤ 3 min, registro de IA), formato de socialización, reglas de IA, ideas de proyectos en contexto colombiano (10), recursos de datos.
- Rubric: detailed descriptors for technical deliverable (15%), presentation & demo (10%), individual defense (5%), peer factor formula.
- [ ] Commit `docs: add final project brief, rubric and templates`.

## Task 17: Institutional course guide

**Files:** `guia-de-asignatura/guia-de-asignatura.docx` (from `/Users/julian/Downloads/Formato Guía de asignatura_V.Actualizada.docx`), `guia-de-asignatura/guia-de-asignatura.md`
- Fill every section of the template in Spanish; remove grey guidance text and the annexes (template instruction); keep institutional header/footer and styles; professor name Julian Caicedo; unknown data as `[POR COMPLETAR]` (código, horario, perfil, correo institucional, horario de atención, monitor row removed); modality "Virtual"; conceptual map as a list; RAE 1–6 from syllabus (verbs verified); strategies; evaluation table (diagnóstica/formativa/sumativa with RAE and %); programación table 12 rows (sesión, temas, descripción, recursos, trabajo directo / independiente); factores de éxito; bibliography (syllabus 10 + complementary incl. women authors and Spanish sources; fix the HLEG year to 2019); acuerdos; respeto y no discriminación kept verbatim.
- [ ] Validate the .docx opens (zip integrity + XML well-formed) and render a PDF preview if LibreOffice is available.
- [ ] Commit `docs: add filled course guide`.

## Task 18: Verification

- [ ] `pytest tools/tests -q` → all pass.
- [ ] `python tools/check_notebooks.py` → exit 0.
- [ ] `python tools/smoke_test.py` (sequential, background) → all PASS; fix failures.
- [ ] `python tools/check_links.py` → exit 0.
- [ ] Open every deck in the browser pane: no console errors, simulators respond, notes present.
- [ ] Commit fixes.

## Task 19: Publish

- [ ] Push branch, open PR(s), merge to `main`.
- [ ] Enable GitHub Pages (`main`, `/`) via `gh api`; verify the portal URL returns 200.
