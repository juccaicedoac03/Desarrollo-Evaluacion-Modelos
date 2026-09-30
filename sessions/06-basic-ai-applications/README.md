# Sesión 06 — Introduction to Basic Application Development
*Introducción al desarrollo de aplicaciones básicas*

**RAE asociados:** RAE 3, RAE 4 · **Duración:** 3 horas (virtual)

## Objetivos de la sesión

Al terminar la sesión podrás:

1. Plantear una funcionalidad de IA como producto: usuario, trabajo por hacer (*job to be done*), entradas y salidas, y restricciones (RAE 4).
2. Esbozar el diseño conceptual y la arquitectura de una app de clasificación y de un chatbot: servicio del modelo, interfaz, enrutador, registros y retroalimentación (RAE 3).
3. Aplicar pautas de UX para IA (Amershi et al., 2019; *People + AI Guidebook*): fijar expectativas, mostrar la confianza de forma útil, fallar con elegancia y facilitar el paso a una persona (RAE 3).
4. Elegir un umbral de confianza que minimice el costo esperado, con una persona en el ciclo (*human in the loop*) (RAE 4).
5. Construir una app en Gradio y publicar y llamar por API un agente de Startti ADP (RAE 3).

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Calentamiento | 10' | Tres preguntas de repaso de la S05 (BLEU, umbral de decisión, validación y conjunto de prueba) |
| Teoría | 60' | Del modelo al producto · UX para IA · umbrales de confianza y humano en el ciclo · Gradio, Streamlit y plataformas no-code. Simuladores: umbral de enrutamiento y detector de anti-patrones de UX. Sala de trabajo: *AI Product Canvas* |
| Descanso | 10' | — |
| Lab guiado | 60' | Clasificador de intenciones (Banking77) con umbral, app en Gradio con registro de retroalimentación y generador de texto, y primer agente en Startti llamado desde Kaggle |
| Challenge | 40' | Caso personal: umbral de mínimo costo, app en Gradio, asistente en Startti o en Python y decisión código vs. no-code |

**Diálogo formativo del proyecto:** hoy se devuelve la **retroalimentación escrita de las propuestas** (hito H2). Revísenla en grupo y ajusten el alcance antes de la S09.

## Antes de la clase (≈2 h)

- [ ] **Activa tu licencia de Startti** e inicia sesión en [app.startti.ai](https://app.startti.ai), siguiendo las secciones 1 y 12 de la [guía de configuración de Startti](../../docs/configuracion-startti.md). Si prefieres no crear una cuenta, la alternativa en Python cubre todo (sección 11 de la guía).
- [ ] Tu grupo entregó la **propuesta del proyecto (H2)** en e-Aulas a más tardar a las 23:59 del día anterior ([plantilla](../../proyecto-final/plantillas/propuesta.md)).
- [ ] Lee la tabla de las 18 pautas de Amershi et al. (2019) y el capítulo *Errors + Graceful Failure* del [People + AI Guidebook](https://pair.withgoogle.com/guidebook/) (≈45 min).
- [ ] Recorre el [inicio rápido de Gradio](https://www.gradio.app/guides/quickstart) (≈20 min).
- [ ] Repasa las métricas de clasificación y la separación validación/prueba de la S05.

## Materiales

| Material | Enlace |
|---|---|
| Presentación | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/06-basic-ai-applications/slides.html) |
| Lab guiado | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/06-basic-ai-applications/lab.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/06-basic-ai-applications/lab.ipynb) · [archivo](lab.ipynb) |
| Challenge | [Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/06-basic-ai-applications/challenge.ipynb) · [Colab](https://colab.research.google.com/github/juccaicedoac03/Desarrollo-Evaluacion-Modelos/blob/main/sessions/06-basic-ai-applications/challenge.ipynb) · [archivo](challenge.ipynb) |
| Plantilla del *AI Product Canvas* | [data/ai-product-canvas.md](data/ai-product-canvas.md) |
| Guía de configuración de Startti | [docs/configuracion-startti.md](../../docs/configuracion-startti.md) |
| Guía de Kaggle (Secrets) | [docs/configuracion-kaggle.md](../../docs/configuracion-kaggle.md) |

**Kaggle:** Internet activado; la CPU es suficiente (no gastes cuota de GPU). Para la parte de Startti: *Add-ons → Secrets* → `STARTTI_API_KEY`, adjunto al notebook.

## Challenge de la sesión (evaluación)

Cada estudiante recibe, a partir de su código, un **caso de servicio al cliente** (una de 6 empresas ficticias, con 10 intenciones de Banking77), dos **costos unitarios** (persona y error automático) y un **volumen mensual**.

1. **Umbral de mínimo costo esperado:** entrena el clasificador, calcula cobertura, exactitud y costo por 1.000 mensajes para umbrales de 0.30 a 0.90 en validación, compáralo con el umbral teórico y con la calibración del modelo, y repórtalo en prueba.
2. **App en Gradio** con tu umbral y tus textos de UX; úsala y deja el registro de interacciones como evidencia.
3. **Explica y decide:** construye el asistente de tu caso en Startti **o** con la alternativa en Python (ambos caminos valen lo mismo) y decide qué lanzarías primero, código o no-code, con tus números.
4. **Crítica a la IA:** encuentra, explica y corrige los 3 anti-patrones de UX de un flujo propuesto por una IA.

- **Rúbrica:** ejecución técnica 40% · análisis e interpretación 40% · reflexión y registro de IA 20% ([evaluación](../../docs/evaluacion.md)).
- **IA permitida con registro obligatorio**: sin registro, ese componente vale 0.0 ([política de uso de IA](../../docs/politica-uso-ia.md)). **Micro-sustentaciones** al azar: si no puedes explicar tu entrega, la nota máxima es 3.0.
- **Entrega:** `File → Download notebook` → súbelo a e-Aulas como **`S06_<codigo>.ipynb`** antes de las **23:59** de hoy.

## Después de la clase (trabajo independiente ≈7 h)

- [ ] Termina y entrega el challenge (23:59).
- [ ] **Antes de la S07:** crea tu API key de Startti (si no lo hiciste en el lab), guárdala en Kaggle Secrets como `STARTTI_API_KEY` y verifica que la celda del cliente imprima `Startti key found ✅` ([guía, secciones 5 y 6](../../docs/configuracion-startti.md)).
- [ ] **Proyecto (≈3 h):** lean en grupo la retroalimentación escrita de la propuesta, ajusten el alcance, los datos y la línea base, y decidan si la demo será una app de Gradio o un agente de Startti.
- [ ] Practica con los ejercicios 🧪 del lab: cambia los costos, agrega retroalimentación granular y prueba reglas nuevas en tu agente.
- [ ] Llena el [*AI Product Canvas*](data/ai-product-canvas.md) para el caso de tu proyecto.
- [ ] Lectura recomendada: Shneiderman (2020) sobre IA centrada en el ser humano (opcional).

## Lecturas y recursos

- Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for human-AI interaction. *Proceedings of CHI 2019*. https://doi.org/10.1145/3290605.3300233
- Google PAIR. (2019). *People + AI Guidebook*. https://pair.withgoogle.com/guidebook/
- Shneiderman, B. (2020). Human-centered artificial intelligence: Reliable, safe & trustworthy. *International Journal of Human–Computer Interaction, 36*(6), 495–504.
- Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *ICML*.
- Chow, C. K. (1970). On optimum recognition error and reject tradeoff. *IEEE Transactions on Information Theory, 16*(1), 41–46.
- Casanueva, I., Temčinas, T., Gerz, D., Henderson, M., & Vulić, I. (2020). Efficient intent detection with dual sentence encoders. *NLP4ConvAI workshop, ACL*. arXiv:2003.04807 (dataset Banking77).
- Abid, A., Abdalla, A., Abid, A., Khan, D., Alfozan, A., & Zou, J. (2019). Gradio: Hassle-free sharing and testing of ML models in the wild. arXiv:1906.02569.
- Documentación de [Gradio](https://www.gradio.app/docs) y de [Streamlit](https://docs.streamlit.io).
- **En español:** [documentación de Startti ADP](https://adp.startti.ai/docs) (constructor de agentes, conocimiento, publicación y API pública) y la [guía de configuración de Startti del curso](../../docs/configuracion-startti.md).
