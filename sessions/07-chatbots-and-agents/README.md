# Sesión 07 — Implementing Basic Chatbots and Agents
*Implementación de chatbots y agentes básicos*

**RAE asociados:** RAE 3, RAE 4, RAE 6 · **Duración:** 3 horas (virtual)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Explicar cuatro paradigmas de sistemas conversacionales (reglas, intenciones y flujos con Rasa o Dialogflow CX, LLM con RAG y agentes con herramientas) y elegir el adecuado para un caso de uso (RAE 4).
2. Construir un bot básico en Python (NLU, *slots*, estado del diálogo y política) y un agente con base de conocimiento en Startti ADP (RAE 3).
3. Diseñar una conversación que falle bien: reparación, *fallback*, paso a una persona, persona del asistente y *guardrails* (RAE 3).
4. Reconocer la inyección de prompts y la filtración del prompt del sistema, y mitigarlas con defensas en capas (RAE 6).
5. Evaluar un chatbot con un set de conversaciones de prueba (éxito por tipo, contención, errores no escalados, cifras inventadas) y decidir si está listo para producción (RAE 6).

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso de la S06 (umbral de mínimo costo, error 409 de Startti, pauta G10 de Amershi) |
| Teoría | 60' | Cuatro generaciones de chatbots · Rasa y Dialogflow CX · LLM, RAG y agentes (ReAct) · Startti ADP · comparación de plataformas · diseño conversacional · inyección de prompts · evaluación de chatbots. Simuladores: máquina de estados "bloquear mi tarjeta", quiz de paradigmas y demo de inyección de prompts. Sala de trabajo: diseño de un flujo |
| Descanso | 10' | — |
| Lab guiado | 60' | Bot en Python "por dentro" (Banking77, *slots*, estado, *fallback* con SmolLM2 y chat en Gradio), agente de Startti con la base de conocimiento de Andes Bank y un arnés de evaluación que prueba ambos |
| Challenge | 40' | Dominio personal: agente v1, set de 12 conversaciones, análisis de fallas, crítica de un prompt escrito por IA, v2 y decisión de salida a producción |

## Antes de la clase (≈2 h)

- [ ] Verifica que tu clave `STARTTI_API_KEY` esté en *Kaggle → Add-ons → Secrets* y que la celda del cliente imprima `Startti key found ✅` ([guía de configuración de Startti](../../docs/configuracion-startti.md), secciones 3 a 6). Repasa cómo crear una **colección de conocimiento** (sección 3). Si prefieres no usar Startti, el camino en Python cubre todo.
- [ ] Lee las secciones sobre la arquitectura de diálogo basada en estados y sobre la evaluación de chatbots del capítulo *Chatbots & Dialogue Systems* de Jurafsky y Martin (≈45 min).
- [ ] Lee el resumen de las entradas LLM01 (*Prompt Injection*) y LLM07 (*System Prompt Leakage*) del [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) (≈20 min).
- [ ] Repasa el lab de la S06: clasificador de Banking77 con umbral y llamada a Startti con `startti_run`.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/07-chatbots-and-agents/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/07-chatbots-and-agents/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/07-chatbots-and-agents/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/07-chatbots-and-agents/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/07-chatbots-and-agents/challenge.ipynb) · [archivo](challenge.ipynb) |
| Base de conocimiento del lab (Andes Bank, ficticia, en inglés) | [data/faq_andes_bank.md](data/faq_andes_bank.md) · pruebas: [data/test_conversations_andes.json](data/test_conversations_andes.json) |
| Bases de conocimiento del challenge (8 empresas ficticias, en español) | [data/dominios/](data/dominios/) |
| Guía de configuración de Startti | [docs/configuracion-startti.md](../../docs/configuracion-startti.md) |
| Guía de Kaggle (Secrets) | [docs/configuracion-kaggle.md](../../docs/configuracion-kaggle.md) |

**Kaggle:** Internet activado; la CPU es suficiente. Para Startti: *Add-ons → Secrets* → `STARTTI_API_KEY`, adjunto al notebook. Todas las empresas, precios y políticas de los archivos de `data/` son **inventados**.

## Challenge de la sesión (evaluación)

Cada estudiante recibe, a partir de su código, un **dominio** (una de 8 empresas ficticias: telecomunicaciones, comercio electrónico, universidad, clínica, aseguradora, aerolínea, servicios públicos o banco) con sus preguntas frecuentes y un set de **12 conversaciones de prueba** (4 en alcance, 3 fuera de alcance, 3 de varios turnos y 2 adversariales), además de un código canario y unos criterios de salida a producción.

1. **Agente v1:** constrúyelo en Startti con la base de conocimiento de tu dominio **o** con la alternativa en Python (recuperación sobre las preguntas frecuentes; ambos caminos valen lo mismo), usando las instrucciones que propuso un asistente de IA, y córrele el set de 12 casos.
2. **Análisis de fallas por tipo**, con tus números y las transcripciones.
3. **Crítica a la IA e iteración:** encuentra y corrige los 3 errores de las instrucciones, haz un cambio adicional (base de conocimiento, umbral, contexto o filtros), vuelve a medir y compara v1 contra v2.
4. **Explica y decide:** ¿está listo para producción? Contención vs. riesgo con la proyección a tu volumen mensual y tu **política de paso a una persona**.

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% ([evaluación](../../docs/evaluacion.md)).
- **IA permitida con registro obligatorio**: sin registro, ese componente vale 0.0 ([política de uso de IA](../../docs/politica-uso-ia.md)). **Micro-sustentaciones** al azar: si no puedes explicar tu entrega, la nota máxima es 3.0.
- **Entrega:** `File → Download notebook` → súbelo a e-Aulas como **`S07_<codigo>.ipynb`** antes de las **23:59** de hoy.

## Después de la clase (trabajo independiente ≈7 h)

- [ ] Termina y entrega el challenge (23:59).
- [ ] **Proyecto (≈3 h):** si la demo de tu grupo es un chatbot o un agente, escriban su propio set de 12 conversaciones de prueba (con al menos 2 adversariales) y córranlo con el arnés del lab. Si es una app de clasificación, definan qué pasa cuando el modelo no está seguro.
- [ ] Practica con los ejercicios 🧪 del lab: agrega un *slot* al flujo de bloqueo, un caso de varios turnos al set y compara el recuperador TF-IDF con el de *embeddings*.
- [ ] Opcional: en tu agente de Startti, prueba una herramienta adicional o una pregunta al usuario antes de una acción (humano en el ciclo) y vuelve a correr el arnés.
- [ ] Prepara la S08: repasa Naive Bayes y regresión logística (modelos generativos vs. discriminativos) y los *embeddings* de la S03.

## Lecturas y recursos

- Jurafsky, D., & Martin, J. H. (2025). *Speech and Language Processing* (3.ª ed., borrador), capítulo *Chatbots & Dialogue Systems*. https://web.stanford.edu/~jurafsky/slp3/
- Weizenbaum, J. (1966). ELIZA—A computer program for the study of natural language communication between man and machine. *Communications of the ACM, 9*(1), 36–45.
- Bocklisch, T., Faulkner, J., Pawlowski, N., & Nichol, A. (2017). Rasa: Open source language understanding and dialogue management. arXiv:1712.05181.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS*.
- Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. *ICLR*.
- Walker, M. A., Litman, D. J., Kamm, C. A., & Abella, A. (1997). PARADISE: A framework for evaluating spoken dialogue agents. *ACL*.
- Pearl, C. (2016). *Designing Voice User Interfaces*. O'Reilly.
- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *AISec '23*.
- OWASP. (2025). *Top 10 for LLM Applications*. https://genai.owasp.org/llm-top-10/
- Documentación de [Rasa](https://rasa.com/docs/) y de [Dialogflow CX](https://cloud.google.com/dialogflow/cx/docs).
- **En español:** [documentación de Startti ADP](https://adp.startti.ai/docs) (constructor de agentes, conocimiento, publicación y API pública) y la [guía de configuración de Startti del curso](../../docs/configuracion-startti.md).
