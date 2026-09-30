# Metodología del curso

*Desarrollo y Evaluación de Modelos Propios · Especialización en Inteligencia Artificial Generativa y Desarrollo de Negocios · Universidad del Rosario*

Este curso es virtual, práctico y está pensado para profesionales de perfiles distintos: algunos vienen del mundo de los negocios, otros del mundo técnico, y casi todos usan asistentes de IA a diario. La metodología busca que **en cada sesión entiendas un concepto, lo construyas con código y tomes una decisión de negocio con tus propios resultados**.

---

## 1. Enfoque pedagógico

### Aprendizaje activo

En las sesiones no hay bloques largos de exposición sin participación. La teoría se interrumpe más o menos cada 10 minutos con una interacción: un quiz, un simulador, una pregunta en el chat o un trabajo en sala de grupo. La práctica se hace en vivo, con *checkpoints* en los que compartes tus resultados.

### Aula invertida ligera

Antes de cada sesión dedicas unas **2 horas** a una preparación corta (una lectura, un video o la revisión de un notebook) que indica la guía de la sesión. Como las dos sesiones del sábado van seguidas, la preparación de ambas debe estar lista antes del sábado a las 7:00. El calentamiento de 10 minutos al inicio de la clase retoma esa preparación y la sesión anterior. No se trata de estudiar todo por tu cuenta: la preparación te deja listo(a) para aprovechar la clase.

### Aprendizaje basado en proyectos

Desde la Sesión 03 trabajas en grupo en un **proyecto final**: un modelo propio, evaluado y mejorado, para un problema real de contexto colombiano o latinoamericano. Cada bloque del curso aporta una pieza (datos, afinamiento, métricas, interfaz, ética, mejora continua) y los hitos formativos te obligan a avanzar de forma constante. Ver el [enunciado del proyecto](../proyecto-final/README.md).

### La IA como copiloto, no como piloto

Puedes y debes usar asistentes de IA (ChatGPT, Claude, Codex, Copilot…): así se trabaja hoy. Pero tú eres responsable de lo que entregas. Por eso los challenges están diseñados para exigir criterio propio:

- tu **configuración personal** hace que tus números sean únicos;
- las tareas **"Explica y decide"** piden decisiones justificadas con esos números;
- las tareas **"Crítica a la IA"** te entrenan para detectar errores en lo que produce un asistente;
- el **registro de uso de IA** y las **micro-sustentaciones** hacen visible tu proceso.

Las reglas completas están en la [política de uso de IA](politica-uso-ia.md).

### Casos de negocio y contexto latinoamericano

Los ejemplos, escenarios y datos se enmarcan en decisiones reales de organizaciones: servicio al cliente, banca, salud, educación, telecomunicaciones. Las empresas de los casos son ficticias (por ejemplo, "Andes Bank" o "NovaTel"); los problemas no lo son.

### Dos idiomas, a propósito

La teoría (presentaciones) y los labs están en **inglés**, porque la documentación, las librerías y la literatura técnica de la disciplina están en inglés. Todo lo evaluativo —challenges, rúbricas, proyecto— y las guías están en **español**, para que puedas argumentar con precisión. En clase puedes preguntar y participar en el idioma que prefieras.

## 2. Calendario

El curso tiene 12 sesiones de 3 horas, entre el 2 y el 24 de octubre de 2026 (hora de Colombia). Los viernes hay una sesión, de 18:00 a 21:00; los sábados hay dos sesiones seguidas, de 7:00 a 10:00 y de 10:00 a 13:00.

| Sesión | Fecha | Hora |
|---|---|---|
| S01 | Viernes 2 de octubre | 18:00–21:00 |
| S02 · S03 | Sábado 3 de octubre | 7:00–10:00 · 10:00–13:00 |
| S04 | Viernes 9 de octubre | 18:00–21:00 |
| S05 · S06 | Sábado 10 de octubre | 7:00–10:00 · 10:00–13:00 |
| S07 | Viernes 16 de octubre | 18:00–21:00 |
| S08 · S09 | Sábado 17 de octubre | 7:00–10:00 · 10:00–13:00 |
| S10 | Viernes 23 de octubre | 18:00–21:00 |
| S11 · S12 | Sábado 24 de octubre | 7:00–10:00 · 10:00–13:00 |

## 3. Estructura de cada sesión (180 minutos)

| Bloque | Minutos | Qué pasa | Material |
|---|---|---|---|
| **Calentamiento** | 10 | Quiz de repaso de la sesión anterior (diagnóstico, no calificado) | Quiz en la presentación o encuesta en la plataforma de videoconferencia |
| **Teoría interactiva** | 60 | Exposición con una interacción cada ~10 minutos: quiz, simulador, sala de grupo con temporizador o encuesta | `slides.html` |
| **Descanso** | 10 | — | — |
| **Lab guiado** | 60 | *Live coding* en Kaggle con *checkpoints* para compartir resultados en el chat | `lab.ipynb` |
| **Challenge** | 40 | Evaluación individual calificada y micro-sustentaciones en vivo | `challenge.ipynb` |

El challenge se empieza en clase y se entrega hasta las **23:59 del mismo día** (ver [evaluación](evaluacion.md)). La Sesión 12 es distinta: está dedicada a la socialización de los proyectos finales.

## 4. Kit de interactividad para clases virtuales

| Herramienta | Qué es | Qué haces tú |
|---|---|---|
| **Quizzes embebidos** | Preguntas de opción múltiple dentro de las slides, con retroalimentación inmediata | Respondes en el chat o en la encuesta; el grupo discute la respuesta correcta y por qué |
| **Simuladores** | Pequeñas herramientas interactivas en las slides (por ejemplo, temperatura de muestreo, umbrales de decisión, costos y ROI) | Propones valores, predices qué va a pasar y lo comparas con lo que muestra el simulador |
| **Encuestas y chat** | Preguntas abiertas o de votación rápida | Escribes tu postura o tu resultado en una línea |
| **Salas de grupo** | Trabajo en grupos pequeños con un temporizador visible y una consigna concreta | Resuelves un caso con tu grupo y una persona comparte la conclusión al volver |
| **Live coding** | El profesor programa en vivo en Kaggle mientras tú ejecutas el mismo notebook | Ejecutas cada parte, respondes los *checkpoints* y resuelves los ejercicios *Try it* |
| **Micro-sustentaciones** | 2–3 minutos compartiendo pantalla para explicar una celda de tu challenge | Explicas con tus palabras qué hace tu código y qué significan tus resultados ([protocolo](evaluacion.md)) |

**Recomendaciones para participar:** ten Kaggle abierto y con sesión iniciada desde el inicio de la clase; usa audífonos; activa la cámara en las salas de grupo y en las micro-sustentaciones cuando tu conexión lo permita.

## 5. Herramientas

| Herramienta | Para qué la usamos | Guía |
|---|---|---|
| **Portal y repositorio del curso** | Presentaciones, guías de sesión, notebooks y documentos | [Portal](https://juccaicedoac03.github.io/Desarrollo-Evaluacion-Modelos/) · [README](../README.md) |
| **Kaggle Notebooks** | Labs y challenges con GPU gratuita, sin instalar nada | [Configuración de Kaggle](configuracion-kaggle.md) |
| **Google Colab** | Plan B cuando Kaggle no está disponible | [Configuración de Kaggle, sección Colab](configuracion-kaggle.md) |
| **Startti ADP** | Construcción, publicación y evaluación de agentes (S06, S07, S09 y, opcionalmente, el proyecto) | [Configuración de Startti](configuracion-startti.md) |
| **e-Aulas** | Anuncios, entregas de challenges y del proyecto, notas y retroalimentación | Plataforma institucional |
| **Zoom o Teams** | Sesiones sincrónicas, salas de grupo, encuestas y micro-sustentaciones | La plataforma que indique la Universidad |
| **Asistentes de IA** | Apoyo para entender, programar y redactar, bajo la política del curso | [Política de uso de IA](politica-uso-ia.md) |

Todo funciona desde el navegador. No necesitas un computador potente ni instalar Python en tu equipo.

## 6. Trabajo independiente (9 horas por sesión)

El curso tiene 3 créditos: 36 horas con el profesor y **108 horas de trabajo independiente**, es decir, unas **9 horas por cada una de las 12 sesiones**. Como las sesiones se concentran en viernes y sábados, reserva ese tiempo de lunes a jueves y bloquéalo en tu agenda.

| Actividad | Horas por sesión | Qué incluye |
|---|---|---|
| Preparación previa | ≈ 2 | Lectura, video o notebook indicado en "Antes de la clase" de la guía de la sesión |
| Cierre del challenge | ≈ 2 | Terminar las tareas, la reflexión y el registro de IA; entregar antes de las 23:59 |
| Práctica autónoma | ≈ 2 | Repetir el lab con otros datos o parámetros, resolver los *Try it* pendientes, lecturas de la sesión |
| Proyecto final | ≈ 3 | Trabajo en grupo sobre los hitos del proyecto |

**El ciclo de cada sesión**

1. **Antes de la clase:** abre la guía de la sesión (`sessions/NN-<tema>/README.md`), haz la preparación y revisa que Kaggle funciona. Si la sesión es un sábado, deja lista antes de las 7:00 la preparación de las dos sesiones del día.
2. **Durante la clase:** participa en el calentamiento, la teoría y el lab; empieza el challenge.
3. **El mismo día:** termina y entrega el challenge antes de las 23:59.
4. **Entre un encuentro y otro:** práctica autónoma, lecturas y reunión con tu grupo del proyecto.

## 7. El proyecto a lo largo del curso

El proyecto va del 3 al 24 de octubre, de la S03 a la S12.

| Momento | Hito formativo |
|---|---|
| S03 (sábado 3 oct., 23:59) | H1 · Grupos conformados (3 integrantes) |
| Miércoles 14 oct., 23:59 | H2 · Propuesta del proyecto (canvas); retroalimentación escrita en la S07 (viernes 16 oct.) |
| S09 (sábado 17 oct., 23:59) | H3 · Canvas de caso de uso |
| Viernes 23 oct., 23:59 | Entrega final, que incluye el H4 · Iteración de mejora (sección 5 del informe técnico) |
| S12 (sábado 24 oct.) | Socialización (8' pitch + 3' demo + 4' preguntas) y defensa individual |

Los hitos no tienen nota propia, pero son obligatorios: cada hito (H1–H4) que el grupo no entregue en su plazo descuenta 0.3 de la nota del entregable técnico (máximo −1.2). Los detalles de entregables, plantillas y rúbrica están en [proyecto-final/README.md](../proyecto-final/README.md).

**Diálogo formativo (sesiones 4 a 7).** Entre la S04 y la S07 tienes un espacio para conocer tu desempeño y ajustar tu estrategia: en la S04 (viernes 9 de octubre) revisas el balance de tus challenges S01–S03; tu grupo entrega la propuesta (H2) hasta el miércoles 14 de octubre y recibe retroalimentación escrita en la S07 (viernes 16 de octubre); y, si lo necesitas, acuerdas una conversación breve con el profesor en el horario de atención.

## 8. Canales de soporte

| Canal | Úsalo para | Datos |
|---|---|---|
| **Foro y anuncios de e-Aulas** | Dudas generales sobre temas, labs o entregas; así la respuesta le sirve a todo el grupo | Espacio del curso en e-Aulas |
| **Horario de atención** | Resolver dudas en vivo, revisar tu proyecto o reprogramar una micro-sustentación | Virtual, con cita previa solicitada al correo institucional del profesor |
| **Correo institucional del profesor** | Asuntos personales o que no deben ser públicos | julian.caicedo@urosario.edu.co |
| **Issues del repositorio en GitHub** | Reportar errores en los materiales (un enlace roto, un notebook que falla) | [Repositorio](https://github.com/juccaicedoac03/Desarrollo-Evaluacion-Modelos) (requiere cuenta de GitHub; opcional) |
| **Compañeros y grupos de estudio** | Discutir conceptos y ayudarse con errores técnicos | Respetando la [política de uso de IA](politica-uso-ia.md): no se comparten resultados personalizados |

**Cómo pedir ayuda de forma efectiva:** indica la sesión y el notebook, la celda que falla, el mensaje de error completo (o una captura) y qué intentaste. Nunca compartas tu API key ni capturas donde aparezca.
