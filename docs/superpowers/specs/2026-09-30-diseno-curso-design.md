# Diseño del curso — Desarrollo y Evaluación de Modelos Propios

**Fecha:** 2026-09-30 · **Estado:** aprobado por el profesor · **Autor:** Julian Caicedo (con Claude Code)

## 1. Contexto

- **Programa:** Especialización en Inteligencia Artificial Generativa y Desarrollo de Negocios — Escuela de Administración (Rosario GSB), Universidad del Rosario.
- **Curso:** Desarrollo y Evaluación de Modelos Propios · 3 créditos · 36 h con el profesor + 108 h de trabajo independiente · obligatorio · sin prerrequisitos.
- **Modalidad:** virtual. 12 sesiones sincrónicas de 3 horas (una por semana).
- **Audiencia:** profesionales de perfil mixto (negocio y técnico). Usan asistentes de IA (ChatGPT, Codex, Claude) de forma habitual.
- **Fuentes:** sílabo oficial (12 unidades, 6 RAE, bibliografía) y el *Formato Guía de Asignatura* institucional.

## 2. Reglas de idioma

| Material | Idioma |
|---|---|
| Teoría: presentaciones HTML (incluidas las notas del profesor) | Inglés |
| Notebooks de práctica guiada (`lab.ipynb`) | Inglés |
| Evaluación: challenges, rúbricas, claves de calificación, política de IA, proyecto final | Español |
| Todo lo dirigido a estudiantes: Guía de Asignatura, README, guías de Kaggle y Startti, calendario, portal web | Español |

La diapositiva que presenta el challenge dentro de cada deck va en español, porque es contenido de evaluación.

## 3. Decisiones de diseño

| Tema | Decisión |
|---|---|
| Teoría | Decks reveal.js 5 (CDN jsDelivr) con tema propio y un JS compartido de componentes interactivos |
| Práctica | Notebooks en Kaggle (GPU T4 gratuita, 30 h/semana); badge *Open in Kaggle* y respaldo en Colab |
| Evaluación | Challenge calificable en **cada** sesión (1–11); sin parciales |
| Nota final | 70% sesiones (mejores 10 de 11 × 7%) + 30% proyecto final grupal |
| Chatbots | Rasa y Dialogflow CX se enseñan en la teoría; la práctica usa Startti ADP y un bot en Python como alternativa |
| Startti | Sesiones 6, 7 y 9, y opcional en el proyecto. Un workspace y un token de API por estudiante |
| Solucionarios | Carpeta local `instructor/` (git-ignored); el repo es público |
| Publicación | GitHub Pages desde `main` (raíz) con portal `index.html` |

## 4. Estructura de cada sesión (180 min)

| Bloque | Min | Actividad | Instrumento |
|---|---|---|---|
| Calentamiento | 10 | Quiz de repaso de la sesión anterior (diagnóstico, no calificado) | Quiz embebido en el deck / encuesta en Zoom |
| Teoría | 60 | Exposición interactiva: una interacción cada ~10 min (quiz, simulador, sala de grupo con temporizador, encuesta) | `slides.html` |
| Descanso | 10 | — | — |
| Práctica guiada | 60 | Live-coding en Kaggle con *checkpoints* | `lab.ipynb` |
| Challenge | 40 | Evaluación individual calificada + micro-sustentaciones en vivo | `challenge.ipynb` |

- **Entrega del challenge:** hasta las 23:59 del mismo día. El notebook se descarga (`.ipynb`) y se sube a e-Aulas con el nombre `S<NN>_<codigo>.ipynb`.
- **Trabajo independiente (9 h/semana):** preparación previa (~2 h), cierre del challenge (~2 h), práctica autónoma (~2 h) y proyecto final (~3 h).

## 5. Evaluación

### 5.1 Nota final (escala 0.0–5.0; se aprueba con 3.0)

| Componente | Peso | Detalle |
|---|---|---|
| Challenges de sesión (S1–S11) | 70% | Cuentan las mejores 10 de 11; cada una vale 7% |
| Proyecto final (grupos de 3) | 30% | Entregable técnico 15% · socialización y demo 10% · defensa individual 5% |
| Factor de coevaluación | ×0.7–1.0 | Se aplica a la nota individual del proyecto según la evaluación de pares del grupo |

### 5.2 Rúbrica general del challenge

- **Ejecución técnica (40%):** el notebook corre con la configuración personal y las tareas están completas.
- **Análisis e interpretación (40%):** las respuestas usan los números del propio estudiante y las decisiones están justificadas.
- **Reflexión y registro de IA (20%):** reflexión metacognitiva y registro de uso de IA verificable.

### 5.3 Diseño que anticipa el uso de asistentes de IA

1. **Personalización:** `STUDENT_ID` se convierte en una semilla (hash) que asigna a cada estudiante un subconjunto de datos, hiperparámetros, dominio o escenario. Así las respuestas no se pueden copiar entre compañeros.
2. **Huella de resultados:** una celda final genera un hash de `STUDENT_ID` + métricas clave, lo que permite detectar notebooks copiados o resultados inventados.
3. **Preguntas "Explica y decide":** decisiones técnicas o de negocio que exigen citar los resultados propios.
4. **Tareas de crítica a la IA:** a partir de una explicación o código "generado por un asistente" con errores sembrados, el estudiante debe encontrarlos y corregirlos, o verificar lo que responde su propio asistente.
5. **Registro de uso de IA obligatorio:** herramienta, prompts principales, qué verificó y qué corrigió. Si falta, la nota del componente es 0.
6. **Micro-sustentaciones:** en cada sesión, 3–4 estudiantes al azar comparten pantalla durante el bloque de challenge y explican una celda (2–3 min). Si no pueden explicar su propia entrega, la nota de ese challenge se limita a 3.0. Cada estudiante pasa al menos 2 veces en el semestre.

### 5.4 Tipos de evaluación (formato institucional)

- **Diagnóstica:** quiz de calentamiento (S1 incluye un diagnóstico de entrada).
- **Formativa:** checkpoints del lab, hitos del proyecto con retroalimentación, autoevaluación en las reflexiones.
- **Sumativa:** challenges y proyecto.
- **Autoevaluación:** reflexiones de cada challenge y autoevaluación del proyecto.
- **Coevaluación:** evaluación de pares dentro del grupo y retroalimentación entre grupos en S12.
- **Heteroevaluación:** calificación del profesor con rúbricas.

## 6. Proyecto final

- **Reto:** diseñar, entrenar o afinar, evaluar y mejorar un modelo propio para un problema contextualizado (de preferencia colombiano o latinoamericano). Se expone mediante una app (Gradio) o un agente (Startti).
- **Mínimos técnicos:**
  - modelo afinado o entrenado por el grupo;
  - línea base y comparación;
  - al menos 2 métricas justificadas;
  - análisis de errores;
  - una iteración de mejora documentada;
  - análisis ético y de sostenibilidad;
  - model card;
  - demo funcional.
- **Hitos formativos, obligatorios:**

  | Sesión | Hito |
  |---|---|
  | S3 | Grupos conformados |
  | S5→S6 | Propuesta (canvas) |
  | S9 | Canvas de caso de uso |
  | S11 | Iteración de mejora |
  | S12 | Entrega y socialización |

- **Socialización en S12:** 8 min de pitch, 3 min de demo y 4 min de preguntas por grupo. Se acepta demo pregrabada como respaldo.

## 7. Plan de sesiones

| # | Título (EN) | Teoría | Lab (Kaggle) | Challenge (personalizado) | Startti |
|---|---|---|---|---|---|
| 1 | Introduction to Generative and Pretrained Models | Generativo vs discriminativo; familias (AR, AE, VAE, GAN, difusión); modelos fundacionales; espectro *build vs buy*; PyTorch/TF/HF | Tensores y autograd; Keras; pipelines de HF; parámetros de muestreo | Muestreo con temperaturas asignadas, diversidad distinct-n, recomendación *build vs buy*, crítica a la IA | — |
| 2 | Training Generative Models | Ciclo de entrenamiento, pérdidas, optimizadores, LR, preprocesamiento, fuga de datos; autoencoders → VAE (ELBO, reparametrización) | VAE en Fashion-MNIST con PyTorch; curvas, reconstrucción, muestreo, interpolación | Latent dim, β y LR asignados; comparar; decisión; bug sembrado en el training loop | — |
| 3 | Pretrained Models and Transfer Learning | Transformer, atención, BERT/GPT/T5, tokenización, estrategias de transferencia, selección de modelos y licencias | Tokenización EN vs ES (costo); fill-mask; embeddings + LR; zero/few-shot con LLM | Curva de aprendizaje con k asignado; few-shot; decisión según datos disponibles | — |
| 4 | Fine-Tuning Generative Models | Full FT vs PEFT (LoRA/QLoRA), SFT e instruction tuning, hiperparámetros, datasets propios, olvido catastrófico, cuándo no afinar | DistilBERT en Banking77 con Trainer; LoRA sobre SmolLM2 con un dataset propio | Subconjunto de intents y grid asignados; comparar 2 configuraciones; FT vs RAG vs prompt | — |
| 5 | Evaluating Generative Models | Perplejidad, BLEU, ROUGE, chrF, similitud semántica, LLM-as-judge, métricas de clasificación, k-fold, fuga de datos, análisis de errores | Perplejidad; BLEU/chrF EN→ES; ROUGE en resúmenes; k-fold estratificado; análisis de errores | Métricas sobre muestras asignadas; caso de falla de la métrica; plan de evaluación de negocio | — |
| 6 | Introduction to Basic Application Development | Del modelo al producto; diseño conceptual de chatbots y clasificadores; UX para IA; umbrales y humano en el ciclo; Gradio vs no-code | App Gradio (clasificador con umbral de confianza + generador); primer agente Startti y llamada por API | Caso asignado: umbral cobertura/precisión; versión Startti; comparación | Primer agente + API |
| 7 | Implementing Basic Chatbots and Agents | Reglas → Rasa/Dialogflow CX (intents, entidades, slots, flows) → LLM + RAG → agentes; Startti ADP; diseño y evaluación conversacional | Bot en Python (NLU + slots + estado + LLM fallback) y agente Startti con base de conocimiento, evaluado desde Kaggle | Dominio y FAQ asignados; set de 12 conversaciones; métricas; 1 iteración; ¿listo para producción? | Eje del lab y del challenge |
| 8 | Building Classifiers with Generative Models | Clasificadores generativos vs discriminativos (Bayes, NB, LR; Ng & Jordan 2002); features de VAE; scoring por verosimilitud de LLM; zero-shot; datos sintéticos; calibración y costos | NB vs LR (curva de aprendizaje); MLP PyTorch sobre embeddings; zero-shot por log-likelihood; aumento sintético | Slice y tamaño asignados; aumento sintético; recomendación costo/latencia/privacidad; fuga de datos sembrada | — |
| 9 | Use Cases: Generative Models in Real Contexts | Marcos de análisis (valor × factibilidad, riesgo, KPIs, ROI); salud, finanzas, educación; éxitos y fracasos documentados | Prototipos rápidos: sentimiento financiero, síntomas (salud), tutor educativo; agente Startti sectorial | Sector y caso asignados; prototipo + canvas + ROI; go/no-go; verificación de estadística inventada | Agente sectorial |
| 10 | Ethics and Sustainability in Generative Models | Taxonomía de riesgos; sesgo y fairness; privacidad (Ley 1581/2012); EU AI Act, HLEG 2019, NIST AI RMF, UNESCO, CONPES 4144 (2025); huella de carbono; model cards y datasheets | Sondeo de sesgo con fill-mask; prueba contrafactual; detección y redacción de PII; CodeCarbon; model card | Atributo y plantillas asignados; métrica de disparidad; mitigación; clasificación regulatoria | — |
| 11 | Evaluation and Continuous Model Improvement | Ciclo MLOps; análisis de errores → hipótesis → correcciones; tracking; HPO (Optuna); robustez (CheckList); eficiencia (cuantización, destilación); monitoreo y drift | Baseline ruidoso → análisis por slices → limpieza/aumento → Optuna → pruebas de robustez → cuantización int8 → bitácora | Presupuesto de mejora asignado; bitácora; decisión de despliegue con restricciones asignadas | — |
| 12 | Integrative Project: Complete Solution | Deck de facilitación: agenda, criterios, formulario de pares, cierre del curso | — | Proyecto final | Opcional |

## 8. Estructura del repositorio

```
index.html                  Portal (GitHub Pages) — ES
README.md                   Presentación del curso — ES
.nojekyll  .gitignore
assets/css/course.css       Tema de los decks
assets/js/course.js         Componentes interactivos (quiz, temporizador, sliders, gráficos)
docs/                       metodologia.md, evaluacion.md, politica-uso-ia.md,
                            configuracion-kaggle.md, configuracion-startti.md — ES
guia-de-asignatura/         Formato Guía de Asignatura diligenciado (.docx + .md) — ES
sessions/NN-<slug>/         README.md (ES), slides.html (EN), lab.ipynb (EN),
                            challenge.ipynb (ES), data/ (si aplica)
proyecto-final/             README.md, rubrica.md, plantillas/ — ES
tools/                      smoke_test.py, requirements-dev.txt
instructor/                 (git-ignored) claves de calificación y notas de facilitación
docs/superpowers/           especificación y plan (este documento)
```

## 9. Convenciones técnicas

- **Decks:**
  - reveal.js 5.1.0 desde `cdn.jsdelivr.net`, con los plugins notes, math (KaTeX) y highlight.
  - Rutas relativas `../../assets/...`.
  - Cada diapositiva lleva notas del profesor (`<aside class="notes">`).
  - Componentes declarativos: `.quiz`, `.timer`, `.reveal-card`, `.prompt-card`. Los simuladores se escriben con JS inline del deck, apoyados en los helpers de `course.js`.
- **Notebooks:**
  - Se escriben en formato *percent* y se convierten con jupytext; en el repo solo queda el `.ipynb`.
  - Celda de setup: instala solo lo que no trae Kaggle, detecta el dispositivo, fija la semilla y define `FAST_DEV_RUN` (variable de entorno `COURSE_FAST_DEV_RUN=1` para la prueba de humo con datos mínimos).
  - Se usan modelos pequeños y abiertos, sin gating: SmolLM2, Qwen2.5-0.5B, DistilBERT, BERT, GPT-2, flan-t5-small, opus-mt, MiniLM.
- **Secretos:**
  - `STARTTI_API_KEY` se guarda en Kaggle Secrets (en Colab, `userdata`; en local, variable de entorno). Nunca va en el código.
  - URL base de la API: `https://api.startti.ai`, endpoint `POST /v1/run` (`agentId`, `prompt`, `sessionKey`).
  - El agente debe estar publicado para ejecutarse por API.
- **Alternativa sin cuenta:** el harness de evaluación del S7 recibe cualquier `agent_fn(prompt, session_key) -> str`: el agente de Startti o el bot en Python.
- **Verificación:**
  - Todos los notebooks se ejecutan localmente con `COURSE_FAST_DEV_RUN=1`.
  - Los decks se revisan en navegador sin errores de consola.
  - Se validan todos los enlaces internos.

## 10. Datos que aporta el profesor

Código del curso, horario, perfil profesional, correo institucional, horario de atención y cantidad de licencias Startti. En la guía quedan marcados como `[POR COMPLETAR]`.

## 11. Fuera de alcance

- Grabación de videos.
- Configuración de e-Aulas.
- Creación de cuentas de Startti o Kaggle para los estudiantes.
- Solucionarios completos ejecutables: se reemplazan por claves de calificación con rangos esperados y respuestas modelo.
