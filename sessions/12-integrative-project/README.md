# Sesión 12 — Integrative Project: Complete Solution
*Proyecto integrador: desarrollo de solución completa*

**RAE asociados:** RAE 1, RAE 2, RAE 3, RAE 4, RAE 5, RAE 6 · **Duración:** 3 horas (virtual)

Esta sesión no tiene lab ni challenge: está dedicada a la **socialización de los proyectos finales**. Cada grupo presenta su modelo propio (pitch, demo en vivo y preguntas), cada integrante responde su defensa individual y cerramos el curso. El enunciado completo está en el [proyecto final](../../proyecto-final/README.md) y los criterios, en la [rúbrica](../../proyecto-final/rubrica.md). Esta guía reúne la logística del día.

## Objetivos de la sesión

1. Presentar a un público mixto un proyecto de IA generativa con una historia clara: problema, solución, evidencia frente a la línea base, valor de negocio y limitaciones (RAE 4, RAE 5).
2. Demostrar en vivo que el modelo afinado o entrenado por el grupo cumple un papel verificable en una app de Gradio o en un agente de Startti (RAE 1, RAE 3).
3. Defender de forma individual las decisiones de datos, modelo, evaluación, ética y uso de IA con los números del propio proyecto (RAE 2, RAE 6).
4. Dar y recibir retroalimentación específica, basada en evidencia, útil y respetuosa.
5. Integrar lo aprendido en las 12 sesiones y definir una ruta para seguir aprendiendo.

## Agenda

| Bloque | Tiempo | Actividad |
|---|---|---|
| Apertura | 10' | Reglas, criterios de evaluación, sorteo del orden de presentación y asignación de la retroalimentación entre grupos |
| Socialización · ronda 1 | 16' por grupo | Primera mitad de los grupos: 8' de pitch + 3' de demo + 4' de preguntas, más 1' para cambiar de pantalla |
| Descanso | 10' (5' con 10 o más grupos) | Los grupos de la ronda 2 relanzan su demo y prueban la pantalla compartida |
| Socialización · ronda 2 | 16' por grupo | Segunda mitad de los grupos, con el mismo formato |
| Cierre | Tiempo restante (mínimo 5') | Preguntas pendientes de la defensa individual, recapitulación del curso y próximos pasos |

> **Presupuesto de tiempo:** 30' + 16' × número de grupos. Con hasta 9 grupos todo cabe en 3 horas con un descanso de 10'; con 10 grupos, el descanso y el cierre se reducen a 5' cada uno. Si el número de grupos no cabe en la sesión, el profesor anunciará con anticipación en e-Aulas cómo se ajusta el horario. Si las preguntas de un grupo se extienden, la defensa individual puede completarse en un espacio breve al final de la sesión.

## Antes de la clase

### Entrega final: 23:59 del día anterior a la S12

Un integrante sube a e-Aulas los archivos del grupo. Se califica la versión disponible al cierre del plazo: el último commit o la última versión guardada del notebook de Kaggle antes de la hora límite ([enunciado, §4](../../proyecto-final/README.md#4-entregables-finales-sesión-12)).

| Archivo | Contenido |
|---|---|
| `PF_G<NN>_informe.pdf` | Informe técnico (máximo 8 páginas, sin contar portada, referencias ni anexos) con el Anexo A de contribuciones. La portada reúne los enlaces al código, la demo y el video de respaldo |
| `PF_G<NN>_slides.pdf` | Diapositivas del pitch |
| `PF_G<NN>_model-card.md` | Model card |
| `PF_G<NN>_registro-ia.md` | Registro de uso de IA |

El código (repositorio de GitHub o notebook de Kaggle) debe correr de principio a fin, también **sin claves de API**. Si el repositorio es privado, agreguen como colaborador al usuario `juccaicedoac03`; si el notebook de Kaggle es privado, compártanlo con el usuario que el profesor publicó en e-Aulas. El video de respaldo (opcional, máximo 3 minutos) se entrega como enlace.

### Lista de verificación del grupo para el día de la socialización

- [ ] Ensayamos el pitch completo con cronómetro: 8' de pitch + 3' de demo, sin pasarnos.
- [ ] Cada integrante sabe qué parte presenta y puede explicar **cualquier** otra parte del proyecto, incluido lo que generó una IA.
- [ ] Probamos compartir pantalla en la plataforma de la clase y tenemos abiertas las diapositivas.
- [ ] **Demo en Gradio:** el enlace de `demo.launch(share=True)` solo funciona mientras el notebook está corriendo; lo relanzamos poco antes de nuestro turno (o usamos Hugging Face Spaces).
- [ ] **Demo con Startti:** el agente está publicado y la cuenta del grupo tiene la sesión iniciada (el profesor no puede usar sus Kaggle Secrets).
- [ ] Preparamos 2 o 3 casos de demo: uno típico, uno difícil y uno en el que el modelo falla, y sabemos explicar por qué falla.
- [ ] Tenemos a mano el enlace del video de respaldo.
- [ ] Repasamos nuestros números: modelo frente a línea base, métricas, categorías de error, iteración de mejora y emisiones.
- [ ] Cámara, micrófono y conexión funcionan; notificaciones desactivadas.
- [ ] Descargamos la [plantilla de retroalimentación entre grupos](../../proyecto-final/plantillas/retroalimentacion-pares.md).

## Materiales

| Material | Enlace |
|---|---|
| Presentación (facilitación de la sesión) | [Abrir slides](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/sessions/12-integrative-project/slides.html) · [archivo](slides.html) |
| Enunciado del proyecto final | [proyecto-final/README.md](../../proyecto-final/README.md) |
| Rúbrica del proyecto | [rubrica.md](../../proyecto-final/rubrica.md) |
| Plantilla de coevaluación | [coevaluacion.md](../../proyecto-final/plantillas/coevaluacion.md) |
| Plantilla de retroalimentación entre grupos | [retroalimentacion-pares.md](../../proyecto-final/plantillas/retroalimentacion-pares.md) |
| Evaluación del curso | [docs/evaluacion.md](../../docs/evaluacion.md) |
| Política de uso de IA | [docs/politica-uso-ia.md](../../docs/politica-uso-ia.md) |
| Configuración de Startti (demos con agente) | [docs/configuracion-startti.md](../../docs/configuracion-startti.md) |

## Socialización: formato y reglas

Cada grupo tiene **15 minutos: 8' de pitch + 3' de demo + 4' de preguntas**. El tiempo se controla con temporizador: al minuto 8 el profesor pide pasar a la demo y al minuto 11 empiezan las preguntas. Mientras ustedes comparten pantalla no verán el temporizador del profesor, que avisará por voz o en el chat; conviene que un integrante lleve también su propio cronómetro. La socialización se hace en español.

- **Orden aleatorio.** El orden se sortea en clase, al inicio de la sesión, con la herramienta de la presentación: un estudiante propone en el chat el número que sirve de semilla, así el sorteo se puede verificar. El profesor publica en el chat el orden, la hora aproximada de cada turno y la asignación de la retroalimentación entre grupos. Todos los grupos deben estar listos desde el inicio, con la pantalla compartida probada. **Si un grupo no está listo cuando lo llaman, pasa una sola vez al final de la lista.**
- **Todos hablan.** Cada integrante presenta una parte del pitch o de la demo.
- **Defensa individual.** En los 4' de preguntas, el profesor dirige al menos una pregunta a cada integrante, sobre cualquier parte del proyecto y no solo sobre "su" parte. Durante la defensa no se pueden consultar asistentes de IA ni leer respuestas preparadas. Responder *"no lo sé, pero lo verificaría así…"* es mejor que improvisar.
- **Cámara encendida** durante la propia intervención y la defensa individual.
- **Demo.** Muestren 2 o 3 casos (típico, difícil y un fallo explicado) y las decisiones de producto: umbral de confianza, escalamiento a una persona, mensajes de incertidumbre. Si la demo en vivo falla por causas técnicas, proyecten el video de respaldo, sin penalización; el profesor verifica después que la demo funcione con lo entregado. Presentar solo el video, sin intentar la demo en vivo, limita el criterio de demo al nivel Bueno (menos de 4.5).
- **Ausencias.** Quien falte a la S12 sin excusa válida obtiene 0.0 en socialización y en defensa individual. Con excusa válida según el reglamento, conserva la nota de socialización del grupo y presenta su defensa individual en otra fecha.
- **Mientras presentan los demás grupos**, cada estudiante diligencia la retroalimentación de los grupos que le asignaron.

### Estructura sugerida del pitch (8')

| Minutos | Contenido |
|---|---|
| 1' | Problema, usuario y por qué importa (con un dato o un caso) |
| 1.5' | Solución y datos |
| 1.5' | Modelo y entrenamiento: qué afinaron y por qué |
| 2' | Evaluación: resultados frente a la línea base, errores típicos y la iteración de mejora |
| 1' | Ética, sostenibilidad y limitaciones |
| 1' | Valor de negocio, recomendación (go / no-go) y siguiente paso |

## Evaluación del proyecto (30% de la nota final)

| Componente | Peso en la nota final | Tipo de nota | Criterios (peso dentro del componente) |
|---|---|---|---|
| Entregable técnico (T) | 15% | Grupal, después de descuentos por hitos y topes | 8 criterios: problema y contexto, datos, modelo y entrenamiento, evaluación, mejora iterativa, ética y model card, código y reproducibilidad, registro de uso de IA ([rúbrica, §2](../../proyecto-final/rubrica.md#2-entregable-técnico-15--nota-grupal)) |
| Socialización y demo (S) | 10% | Grupal | Claridad del pitch y valor de negocio (35%) · Demo funcional (30%) · Manejo del tiempo (15%) · Participación equitativa (20%) |
| Defensa individual (D) | 5% | Individual | Comprensión técnica de su parte y del todo (40%) · Capacidad de justificar decisiones (35%) · Uso crítico de IA (25%) |
| **Factor de coevaluación (F)** | **× 0.7–1.0** | Individual | Se aplica a la nota del proyecto de cada estudiante |

```text
Nota del proyecto             N  = (15 × T + 10 × S + 5 × D) / 30
Nota individual del proyecto  NI = N × F
Aporte a la nota final           = 0.30 × NI

F = 0.7 + 0.3 × (P − 1) / 3, con tope en 1.0
P = promedio de los puntajes (1–5) que cada estudiante recibe de sus compañeros de grupo en la coevaluación (sin su autoevaluación)
```

| P (promedio recibido) | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | ≥ 4.0 |
|---|---|---|---|---|---|---|---|
| **F** | 0.70 | 0.75 | 0.80 | 0.85 | 0.90 | 0.95 | **1.00** |

- F se redondea a dos decimales; es el único valor intermedio que se redondea.
- En el entregable técnico se aplican **primero** los descuentos por hitos (−0.3 por cada hito H1–H4 no entregado en su plazo, máximo −1.2) y **luego** los topes (p. ej., 3.0 si el grupo no afinó ni entrenó un modelo propio).
- Niveles de cada criterio: Excelente 4.5–5.0 · Bueno 4.0–<4.5 · Aceptable 3.0–<4.0 · Insuficiente <3.0.
- Ejemplo completo y reglas para casos extremos: [rúbrica, §5 y §6](../../proyecto-final/rubrica.md#5-factor-de-coevaluación). El esquema de todo el curso está en [evaluación del curso](../../docs/evaluacion.md).

## Coevaluación y retroalimentación entre grupos

Ambos formularios son **individuales** y se entregan hoy.

| | Coevaluación | Retroalimentación entre grupos |
|---|---|---|
| **Qué es** | Evaluación confidencial de tus compañeros de grupo (y autoevaluación) en 5 criterios, de 1 a 5 | Una ficha por cada grupo que el profesor te asigna al inicio de la sesión: 5 puntajes, 3 fortalezas, 1 pregunta y 1 sugerencia |
| **¿Cuenta para la nota?** | Sí: con los puntajes que recibes se calcula tu factor F. Tu autoevaluación no entra en F. **Es obligatoria:** si no la entregas, tu propio F baja 0.05 (sin bajar de 0.7) | No: es formativa. El profesor consolida las fichas y las comparte con cada grupo sin los nombres de quienes las escribieron |
| **Quién la ve** | Solo el profesor | El grupo evaluado, de forma anónima |
| **Archivo** | `PF_G<NN>_coev_<codigo>.md` o PDF | `PF_retro_<codigo>.md` o PDF |
| **Dónde** | Actividad "Coevaluación del proyecto" de e-Aulas | Actividad "Retroalimentación entre grupos" de e-Aulas |
| **Plazo** | 23:59 del día de la Sesión 12 | 23:59 del día de la Sesión 12 |
| **Plantilla** | [coevaluacion.md](../../proyecto-final/plantillas/coevaluacion.md) | [retroalimentacion-pares.md](../../proyecto-final/plantillas/retroalimentacion-pares.md) |

**Asignación de la retroalimentación entre grupos.** El profesor la anuncia al inicio de la sesión, junto con el sorteo. Por defecto, cada estudiante retroalimenta a los dos grupos que presentan justo después del suyo (los últimos grupos siguen con los primeros); el profesor puede ajustarla.

**Buena retroalimentación:** específica (un momento, una cifra o una diapositiva concreta), basada en lo que viste y oíste, útil para el grupo y respetuosa (habla del trabajo, no de las personas). En la coevaluación, califica con base en hechos: todo puntaje de 1 o 2 exige una justificación con ejemplos concretos.

## Después de la clase

- **Hoy, antes de las 23:59:** sube tu coevaluación (`PF_G<NN>_coev_<codigo>`) y tu retroalimentación entre grupos (`PF_retro_<codigo>`).
- **Notas y retroalimentación:** se publican en e-Aulas. Si recibes un P menor que 3.0, o si hay situaciones como las que describe la regla 4 de la [rúbrica](../../proyecto-final/rubrica.md#5-factor-de-coevaluación), el profesor revisa el factor con evidencia antes de confirmarlo y puede pedir una reunión breve. Las reclamaciones siguen el reglamento académico.
- **Sigue construyendo:** publica la model card (y el modelo, si los datos lo permiten) en el Hugging Face Hub; escribe un memo de una página con la recomendación go / no-go para tu organización; vuelve a evaluar el modelo con datos nuevos dentro de unos meses; agrega el proyecto a tu portafolio sin datos privados ni claves.

## Lecturas y recursos

**Rutas para seguir aprendiendo**

- Hugging Face Learn: [LLM Course](https://huggingface.co/learn/llm-course) (con [edición en español](https://huggingface.co/learn/llm-course/es/chapter1/1)) y [Agents Course](https://huggingface.co/learn/agents-course).
- fast.ai: [Practical Deep Learning for Coders](https://course.fast.ai).
- DeepLearning.AI: [cursos cortos](https://www.deeplearning.ai/short-courses/) sobre RAG, agentes, evaluación y afinamiento.
- Stanford: materiales públicos de [CS224N — Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/) y de [CS230 — Deep Learning](https://cs230.stanford.edu/).
- Startti ADP: [documentación](https://adp.startti.ai/docs), para llevar tu modelo a un agente con base de conocimiento, herramientas y API.
- [SomosNLP](https://somosnlp.org): comunidad internacional de procesamiento de lenguaje natural en español, con hackatones y recursos abiertos.

**Lecturas de cierre**

- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. En *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\* '19)* (pp. 220–229). [https://doi.org/10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596)
- Huyen, C. (2022). *Designing machine learning systems*. O'Reilly Media.
- Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for human-AI interaction. En *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*. [https://doi.org/10.1145/3290605.3300233](https://doi.org/10.1145/3290605.3300233)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [https://doi.org/10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
