# Sesión 04 — Fine-Tuning Generative Models
*Afinamiento de modelos generativos*

**RAE asociados:** RAE 1, RAE 2 · **Duración:** 3 horas (virtual) · **Fecha:** viernes 9 de octubre de 2026, 18:00–21:00 (hora de Colombia)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. **Contrastar** el afinamiento completo (*full fine-tuning*) con el afinamiento eficiente en parámetros (PEFT: *adapters*, *prompt/prefix tuning*, LoRA y QLoRA) y **calcular** cuántos parámetros entrena LoRA (W = W₀ + BA). *(RAE 1)*
2. **Afinar** un codificador (DistilBERT) con `Trainer` de Hugging Face y **reportar** accuracy y F1 macro en un conjunto de test usado una sola vez. *(RAE 1, RAE 2)*
3. **Adaptar** un modelo de chat pequeño (SmolLM2-135M-Instruct) a una voz de marca con LoRA, usando plantillas de chat y enmascarando el *prompt* en la pérdida. *(RAE 1)*
4. **Diagnosticar** subajuste, sobreajuste y divergencia a partir de curvas de aprendizaje, y elegir hiperparámetros (tasa de aprendizaje, épocas, *batch*, *warmup*, *weight decay*, longitud máxima; r, α, *dropout* y módulos objetivo de LoRA). *(RAE 2)*
5. **Decidir** entre *prompting*, RAG y afinamiento para un caso de negocio, considerando datos, costo, privacidad y olvido catastrófico. *(RAE 1)*

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas sobre la S03 (extracción de características, *few-shot*, tokens) · balance de tus challenges S1–S3 (diálogo formativo) |
| Teoría interactiva | 60' | Afinamiento completo vs. PEFT y la matemática de LoRA (calculadora de parámetros LoRA) · ajuste por instrucciones, plantillas de chat y construcción de datasets (sala de trabajo: guía de etiquetado para 5 intents) · hiperparámetros, curvas, sobreajuste y olvido catastrófico (juego de hiperparámetros) · guía de decisión *prompting* → RAG → afinamiento; API alojada vs. modelo abierto |
| Descanso | 10' | — |
| Lab guiado | 60' | Banking77 (10 intents, validación estratificada, línea base TF-IDF) · afinamiento completo de DistilBERT con `Trainer` · LoRA sobre SmolLM2-135M-Instruct con 40 ejemplos de voz de marca de Andes Bank (antes/después, adaptador activado/desactivado) |
| Challenge | 40' | Afina, compara y decide (individual, evaluado) |

## Diálogo formativo: balance de los challenges S1–S3

Hoy se abre el **diálogo formativo** del curso (entre las sesiones 4 y 7), que no tiene nota propia:

- Antes de la sesión de hoy el profesor publica en **e-Aulas** el **balance de tus challenges S1–S3**, con **retroalimentación individual** por componente de la rúbrica. Compáralo con tus autoevaluaciones y elige un hábito para mejorar desde este challenge (por ejemplo, citar siempre tus propios números o llenar el registro de IA mientras trabajas).
- Si lo necesitas, agenda una **conversación breve con el profesor** en el horario de atención (virtual, con cita previa) entre las sesiones 4 y 7.
- Tu grupo entrega la **propuesta del proyecto (H2, canvas)** hasta el **miércoles 14 de octubre a las 23:59**; la retroalimentación escrita se devuelve en la S07 (viernes 16 de octubre).

Detalles en la [guía de asignatura](../../guia-de-asignatura/guia-de-asignatura.md) y en la [evaluación del curso](../../docs/evaluacion.md).

## Antes de la clase (≈2 h)

1. **Lectura 1:** Hugging Face, [*LLM Course*, capítulo 3 en español: *fine-tuning* de un modelo preentrenado](https://huggingface.co/learn/llm-course/es/chapter3/1), en especial la sección sobre la API `Trainer`. *(≈45 min)*
2. **Lectura 2:** Hu et al. (2021), [*LoRA: Low-Rank Adaptation of Large Language Models*](https://arxiv.org/abs/2106.09685), secciones 1 a 4. No hace falta seguir todas las demostraciones: céntrate en la figura 1 y en la ecuación W₀ + BA. *(≈45 min)*
3. **Revisa tu configuración de Kaggle:** hoy conviene usar **GPU T4 x2** (ver la [guía de configuración de Kaggle](../../docs/configuracion-kaggle.md)); confirma que tu número de celular está verificado. *(≈10 min)*
4. **Revisa en e-Aulas** tus notas y comentarios de los challenges S1–S3 (se publican antes de la sesión de hoy) y anota una pregunta para el diálogo formativo. *(≈20 min)*

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/04-fine-tuning/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/04-fine-tuning/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/04-fine-tuning/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/04-fine-tuning/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/04-fine-tuning/challenge.ipynb) · [archivo](challenge.ipynb) |
| Datos de voz de marca | [data/brand_voice.jsonl](data/brand_voice.jsonl): 40 pares instrucción → respuesta de **Andes Bank**, un banco digital ficticio (en inglés) |

Modelos y datos de hoy (abiertos y sin restricciones de acceso): `distilbert/distilbert-base-uncased`, `HuggingFaceTB/SmolLM2-135M-Instruct` y el dataset `legacy-datasets/banking77`. En Kaggle activa **Settings → Accelerator → GPU T4 x2** e **Internet → On**; todo funciona también en CPU, pero el entrenamiento tarda varios minutos más.

Las slides y el lab están en inglés; el challenge y esta guía, en español. En las slides, presiona `S` para ver las notas del presentador y `Esc` para ver todas las diapositivas.

## Challenge de la sesión (evaluación)

**Afina, compara y decide.** Tu configuración personal (a partir de tu código estudiantil) te asigna **10 de los 77 intents** de Banking77, **dos configuraciones de entrenamiento** (A y B, combinaciones de tasa de aprendizaje ∈ {2e-5, 5e-5, 1e-4} y épocas ∈ {1, 2, 3}) y un **dominio de negocio** de una organización ficticia.

| Tarea | Qué haces | Componente |
|---|---|---|
| 1 · Ejecución | Afinas DistilBERT en tus 10 intents con la configuración A (validación estratificada, `max_length` justificado) y reportas accuracy y F1 macro | Ejecución técnica (40%) |
| 2 · Análisis | Entrenas la configuración B, comparas curvas de entrenamiento y validación, diagnosticas si hay subajuste, sobreajuste o ninguno, eliges con validación y evalúas en test **una sola vez** | Análisis e interpretación (40%) |
| 3 · Explica y decide | Recomiendas afinamiento, RAG o *prompting* (o una combinación) para tu dominio, con tus números como evidencia | Análisis e interpretación (40%) |
| 4 · Crítica a la IA | Encuentras, explicas y corriges 4 errores en unos `TrainingArguments` "óptimos" propuestos por un asistente de IA | Análisis e interpretación (40%) |
| Reflexión y registro de IA | Reflexión breve y tabla de uso de asistentes de IA | Reflexión y registro de IA (20%) |

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% (descriptores por nivel en la [evaluación del curso](../../docs/evaluacion.md)).
- **Entrega:** ejecuta todo el notebook, descárgalo (`Archivo → Descargar notebook`) y súbelo a **e-Aulas** como `S04_<codigo>.ipynb` antes de las **23:59 de hoy**. Verifica que se vean "Tu configuración personal" y la huella de resultados.
- **Reglas de IA:** puedes usar asistentes de IA, pero debes registrarlos (sin registro, ese 20% vale 0.0) y eres responsable de lo que entregas. En las **micro-sustentaciones** (2–3 minutos, sin IA) explicas una celda de tu trabajo; si no puedes hacerlo, la nota máxima del challenge es 3.0. Detalles en la [política de uso de IA](../../docs/politica-uso-ia.md).

## Después de la clase (trabajo independiente ≈7 h)

1. **Termina y entrega el challenge** si no alcanzaste en clase (hasta las 23:59). *(≈1 h)*
2. **Repite el lab por tu cuenta** y resuelve los ejercicios 🧪 *Try it* antes de abrir las soluciones; prueba otra combinación de `target_modules` y compara con la calculadora LoRA de las slides. *(≈1.5 h)*
3. **Proyecto final (H2):** con tu grupo, redacta la **propuesta en formato canvas** con la [plantilla de propuesta](../../proyecto-final/plantillas/propuesta.md). Define qué modelo afinarán (completo o LoRA), con qué datos, cómo los etiquetarán y cuál será la línea base. Entrega: miércoles 14 de octubre, 23:59; la retroalimentación escrita llega en la S07. *(≈2 h)*
4. **Diálogo formativo:** revisa tu balance S1–S3 en e-Aulas y, si lo necesitas, agenda una conversación en el horario de atención. *(≈0.5 h)*
5. **Lecturas de profundización** (elige dos): Dettmers et al. (2023) sobre QLoRA; Ouyang et al. (2022) sobre InstructGPT; Kirkpatrick et al. (2017) sobre olvido catastrófico; Gebru et al. (2021) sobre *datasheets* para documentar datasets. *(≈2 h)*
6. **Prepara las sesiones 05 y 06 antes del sábado a las 7:00:** el sábado 10 de octubre hay dos sesiones seguidas (7:00–10:00 y 10:00–13:00), así que haz antes la sección "Antes de la clase" de ambas guías ([Sesión 05](../05-evaluating-generative-models/README.md) y [Sesión 06](../06-basic-ai-applications/README.md)), incluida la **activación de tu licencia de Startti antes del sábado 10 de octubre**.

## Lecturas y recursos

**Lecturas de la sesión**

- Hugging Face. *LLM Course*, capítulo 3: *fine-tuning* de un modelo preentrenado (edición en español). https://huggingface.co/learn/llm-course/es/chapter3/1
- Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2021). LoRA: Low-rank adaptation of large language models. arXiv:2106.09685 (publicado en *ICLR* 2022). https://arxiv.org/abs/2106.09685

**Fuentes primarias citadas en clase**

- Howard, J., & Ruder, S. (2018). Universal language model fine-tuning for text classification. *ACL*. https://arxiv.org/abs/1801.06146
- Houlsby, N., Giurgiu, A., Jastrzebski, S., Morrone, B., de Laroussilhe, Q., Gesmundo, A., Attariyan, M., & Gelly, S. (2019). Parameter-efficient transfer learning for NLP. *ICML*. https://arxiv.org/abs/1902.00751
- Li, X. L., & Liang, P. (2021). Prefix-tuning: Optimizing continuous prompts for generation. *ACL*. https://arxiv.org/abs/2101.00190
- Lester, B., Al-Rfou, R., & Constant, N. (2021). The power of scale for parameter-efficient prompt tuning. *EMNLP*. https://arxiv.org/abs/2104.08691
- Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). QLoRA: Efficient finetuning of quantized LLMs. *NeurIPS*. https://arxiv.org/abs/2305.14314
- Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS*. https://arxiv.org/abs/2203.02155
- Zhou, C., et al. (2023). LIMA: Less is more for alignment. *NeurIPS*. https://arxiv.org/abs/2305.11206
- Casanueva, I., Temčinas, T., Gerz, D., Henderson, M., & Vulić, I. (2020). Efficient intent detection with dual sentence encoders. *Proceedings of the 2nd Workshop on NLP for Conversational AI (ACL)*. https://arxiv.org/abs/2003.04807
- Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. *PNAS*, 114(13), 3521–3526. https://arxiv.org/abs/1612.00796
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL*. https://arxiv.org/abs/1810.04805 *(rejilla de hiperparámetros para afinamiento)*
- Loshchilov, I., & Hutter, F. (2019). Decoupled weight decay regularization. *ICLR*. https://arxiv.org/abs/1711.05101
- Rajbhandari, S., Rasley, J., Ruwase, O., & He, Y. (2020). ZeRO: Memory optimizations toward training trillion parameter models. *SC20*. https://arxiv.org/abs/1910.02054 *(memoria por parámetro al entrenar)*

**Datos, riesgos y documentación**

- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM*, 64(12), 86–92. https://arxiv.org/abs/1803.09010
- Qi, X., Zeng, Y., Xie, T., Chen, P.-Y., Jia, R., Mittal, P., & Henderson, P. (2024). Fine-tuning aligned language models compromises safety, even when users do not intend to! *ICLR*. https://arxiv.org/abs/2310.03693
- Congreso de Colombia (2012). Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales. https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981

**Recursos en español y de la región**

- Hugging Face. *LLM Course*, capítulo 3 (en español), citado arriba.
- Cañete, J., Chaperon, G., Fuentes, R., Ho, J.-H., Kang, H., & Pérez, J. (2020). Spanish pre-trained BERT model and evaluation data. *PML4DC Workshop, ICLR*. Modelo BETO (Universidad de Chile), útil para afinar clasificadores en español en el proyecto: https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased

**Documentación de herramientas**

- Hugging Face, `Trainer` y afinamiento: https://huggingface.co/docs/transformers/training
- Hugging Face, PEFT (LoRA y otros métodos): https://huggingface.co/docs/peft
- Hugging Face, plantillas de chat: https://huggingface.co/docs/transformers/chat_templating
- OpenAI, guía de *fine-tuning* (consultada en septiembre de 2026; la plataforma de *fine-tuning* de OpenAI está en proceso de cierre para usuarios nuevos): https://developers.openai.com/api/docs/guides/supervised-fine-tuning
- Dataset Banking77 en el Hub: https://huggingface.co/datasets/legacy-datasets/banking77
