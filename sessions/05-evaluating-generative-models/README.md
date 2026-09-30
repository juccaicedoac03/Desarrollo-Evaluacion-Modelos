# Sesión 05 — Evaluating Generative Models
*Evaluación de modelos generativos*

**RAE asociados:** RAE 2 · **Duración:** 3 horas (virtual)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Explicar por qué es difícil evaluar texto generado y distinguir la evaluación **intrínseca** (la salida en sí) de la **extrínseca** (su efecto en la tarea o en el negocio).
2. Calcular e interpretar **perplejidad, BLEU, ROUGE, chrF y similitud semántica**, y nombrar lo que cada métrica no ve.
3. Diseñar una evaluación **humana** o con **LLM como juez** que controle sus sesgos conocidos (posición, verbosidad, autopreferencia).
4. Elegir métricas de clasificación (**precisión, recall, F1**, matriz de confusión) y un esquema de validación (**holdout, k-fold estratificado**, conjunto de prueba sellado) sin **fuga de datos**.
5. Conectar una métrica *offline* con un **KPI de negocio** y un umbral de salida a producción (*go / no-go*).

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso sobre afinamiento (S04): LoRA, sobreajuste y uso del conjunto de prueba |
| Teoría | 60' | Por qué es difícil evaluar la generación · perplejidad y tokenizadores · BLEU, ROUGE, chrF · embeddings y BERTScore · evaluación humana y LLM como juez · HELM · matriz de confusión y umbrales · validación cruzada y fuga de datos · análisis de errores · métricas y KPI. **Simuladores:** calculadora BLEU/ROUGE y explorador de umbrales. **Sala de grupos:** elegir métricas para 4 productos |
| Descanso | 10' | — |
| Lab guiado | 60' | Perplejidad de GPT-2 (noticias, tuits, español) · traducción EN→ES con BLEU y chrF · resúmenes con ROUGE, línea base lead-3 y similitud semántica · validación cruzada estratificada y análisis de confusiones en Banking77 |
| Challenge | 40' | Métricas sobre tus muestras, un caso en el que la métrica falla, plan de evaluación de negocio y crítica a la IA |

## Antes de la clase (≈2 h)

- Lee en Jurafsky y Martin (2023), *Speech and Language Processing* (3.ª ed., borrador), la sección del capítulo 3 sobre evaluación de modelos de lenguaje y perplejidad.
- Repasa el módulo de clasificación del *Machine Learning Crash Course* de Google (exactitud, precisión, recall y umbrales). Está disponible en español.
- Vuelve a tu challenge de la S04: ¿cómo elegiste la mejor configuración y con qué datos? Trae esa respuesta al calentamiento.
- Con tu grupo, adelanten el bloque 6 del canvas de propuesta (*Métrica de éxito*): hoy verás cómo elegirla.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/05-evaluating-generative-models/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/05-evaluating-generative-models/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/05-evaluating-generative-models/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/05-evaluating-generative-models/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/05-evaluating-generative-models/challenge.ipynb) · [archivo](challenge.ipynb) |

**Configuración de Kaggle:** *Settings → Internet on*. Hoy no necesitas GPU: el lab y el challenge corren en CPU. Si es tu primera vez, sigue la [guía de Kaggle](../../docs/configuracion-kaggle.md).

**Modelos y datos:** `openai-community/gpt2`, `distilbert/distilgpt2`, `Helsinki-NLP/opus-mt-en-es`, `google/flan-t5-small`, `sentence-transformers/all-MiniLM-L6-v2`; conjuntos `Helsinki-NLP/opus_books` (en-es), `abisee/cnn_dailymail` (3.0.0, en *streaming*) y `legacy-datasets/banking77`. Métricas con `sacrebleu`, `rouge_score` y `scikit-learn`.

## Challenge de la sesión (evaluación)

Challenge **individual** con configuración personal: a partir de tu código estudiantil, el notebook te asigna 8 noticias de CNN/DailyMail, 20 oraciones de `opus_books`, un número de *folds* `k` ∈ {3, 5, 10} y un producto de negocio.

| Tarea | Qué haces | Componente de la rúbrica |
|---|---|---|
| 1 | Resúmenes con `flan-t5-small` vs. la línea base lead-3 (ROUGE-1/2/L y similitud coseno), traducciones con `opus-mt-en-es` (BLEU y chrF) y validación cruzada estratificada con tu `k` | Ejecución técnica |
| 2 | Calificas tus resúmenes de 1 a 5, buscas un caso en el que la métrica y tu juicio no coinciden y explicas por qué | Análisis e interpretación |
| 3 | **Explica y decide:** plan de evaluación para tu producto (métricas, evaluación humana, LLM como juez, KPI, umbrales, validación y monitoreo), citando tus números | Análisis e interpretación |
| 4 | **Crítica a la IA:** encuentras, explicas y corriges 3 errores conceptuales en un plan de evaluación escrito por un asistente | Análisis e interpretación |

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% ([detalle](../../docs/evaluacion.md)).
- **Entrega:** ejecuta todo en orden, descarga el notebook (`Archivo → Descargar notebook`) y súbelo a e-Aulas como **`S05_<codigo>.ipynb`** antes de las **23:59** de hoy.
- **IA permitida con registro obligatorio** ([política de uso de IA](../../docs/politica-uso-ia.md)): sin registro, el componente de reflexión y registro vale 0.0. Puede tocarte una **micro-sustentación**: si no puedes explicar tu entrega, la nota de este challenge se limita a 3.0.

## Proyecto final · Hito H2: propuesta (canvas)

- Cada grupo entrega la **Parte A del [canvas de propuesta](../../proyecto-final/plantillas/propuesta.md)** (máximo 1 página) **antes de la Sesión 06**, hasta las 23:59 del día anterior, en e-Aulas como `PF_G<NN>_H2_propuesta`.
- Usen lo de hoy en el bloque 6 (*Métrica de éxito*): al menos una métrica técnica y una de negocio o de riesgo, con un umbral justificado y una línea base.
- La **retroalimentación escrita** del profesor se devuelve en la **Sesión 06**. El hito no tiene nota propia, pero no entregarlo descuenta 0.3 de la nota del entregable técnico ([enunciado del proyecto](../../proyecto-final/README.md)).

## Después de la clase (trabajo independiente ≈7 h)

- Termina y entrega el challenge (23:59 de hoy).
- Entrega con tu grupo el canvas de propuesta (H2) antes de la S06.
- **Activa tu licencia de Startti antes de la S06** y deja listo tu workspace siguiendo la [guía de configuración de Startti](../../docs/configuracion-startti.md): en la próxima sesión construiremos el primer agente.
- Repite la Parte 4 del lab con otras 10 intenciones de Banking77 o con otro `k`, y compara la dispersión entre *folds*.
- Prueba el prompt de "LLM como juez" del lab con un asistente: intercambia el orden de los resúmenes A y B y anota si el veredicto cambia.

## Lecturas y recursos

- Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). BLEU: A method for automatic evaluation of machine translation. *ACL*. [aclanthology.org/P02-1040](https://aclanthology.org/P02-1040/)
- Lin, C.-Y. (2004). ROUGE: A package for automatic evaluation of summaries. *Text Summarization Branches Out*. [aclanthology.org/W04-1013](https://aclanthology.org/W04-1013/)
- Popović, M. (2015). chrF: Character n-gram F-score for automatic MT evaluation. *WMT*. [aclanthology.org/W15-3049](https://aclanthology.org/W15-3049/)
- Post, M. (2018). A call for clarity in reporting BLEU scores. *WMT*. [aclanthology.org/W18-6319](https://aclanthology.org/W18-6319/)
- Zhang, T., Kishore, V., Wu, F., Weinberger, K. Q., & Artzi, Y. (2020). BERTScore: Evaluating text generation with BERT. *ICLR*. [arXiv:1904.09675](https://arxiv.org/abs/1904.09675)
- Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *NeurIPS Datasets and Benchmarks*. [arXiv:2306.05685](https://arxiv.org/abs/2306.05685)
- Liang, P., et al. (2022). Holistic evaluation of language models. [arXiv:2211.09110](https://arxiv.org/abs/2211.09110)
- Jelinek, F., Mercer, R. L., Bahl, L. R., & Baker, J. K. (1977). Perplexity: A measure of the difficulty of speech recognition tasks. *The Journal of the Acoustical Society of America, 62*(S1), S63.
- Jurafsky, D., & Martin, J. H. (2023). *Speech and language processing* (3.ª ed., borrador), cap. 3. [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/)
- Kohavi, R. (1995). A study of cross-validation and bootstrap for accuracy estimation and model selection. *IJCAI*.
- Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns, 4*(9).
- **En español:** Google. *Curso intensivo de aprendizaje automático*, módulo de clasificación (exactitud, precisión, recall y umbrales). [developers.google.com/machine-learning/crash-course/classification?hl=es](https://developers.google.com/machine-learning/crash-course/classification?hl=es)
