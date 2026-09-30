# Política de uso de inteligencia artificial

*Desarrollo y Evaluación de Modelos Propios · Especialización en Inteligencia Artificial Generativa y Desarrollo de Negocios · Universidad del Rosario*

## Principio general

> **Puedes usar asistentes de IA en este curso. Eres responsable de todo lo que entregas, debes declarar cómo los usaste y debes poder explicar tu trabajo sin ellos.**

Este es un curso sobre modelos generativos para profesionales que ya los usan en su trabajo. Prohibirlos no tendría sentido; usarlos sin criterio, tampoco. La política busca que la IA te haga más rápido(a) y mejor, sin reemplazar tu comprensión ni tu juicio.

La política aplica a los challenges de sesión, al proyecto final y a cualquier otra entrega del curso. Las reglas de evaluación asociadas están en [evaluacion.md](evaluacion.md).

---

## 1. Usos permitidos

| Uso | Ejemplo |
|---|---|
| **Entender conceptos** | Pedir una explicación alternativa de la atención en Transformers o del término KL en un VAE |
| **Programar y depurar** | Pedir ayuda para interpretar un error de `transformers`, escribir una función auxiliar o graficar resultados |
| **Traducir y resumir** | Traducir un fragmento de las slides o de un artículo en inglés; resumir una lectura para estudiarla |
| **Mejorar la redacción** | Hacer más clara una respuesta que ya escribiste con tus ideas y tus números |
| **Explorar ideas** | Generar alternativas de casos de uso para el proyecto o posibles riesgos éticos para discutir con tu grupo |
| **Verificar tu trabajo** | Pedir que revise tu código en busca de errores, o que te haga preguntas sobre tu análisis |

En todos los casos, **tú decides qué usar y qué descartar**, y lo declaras en el registro.

## 2. Declaración obligatoria: el registro de uso de IA

Cada challenge termina con una tabla de **registro de uso de IA**. Para cada uso relevante debes indicar:

1. **Herramienta** (ChatGPT, Claude, Codex, Copilot, Gemini…).
2. **¿Para qué la usaste?**
3. **Prompt principal** (resumido).
4. **¿Qué verificaste o corregiste de su respuesta?**

Si no usaste asistentes de IA, escribe: *"No usé asistentes de IA en este challenge."*

- **Sin registro, el componente "Reflexión y registro de IA" (20%) vale 0.0.**
- En el proyecto final, el grupo usa la [plantilla de registro de uso de IA del proyecto](../proyecto-final/plantillas/registro-uso-ia.md).
- Si un texto, una imagen o un fragmento de código importante de tu entrega fue generado por IA, indícalo también junto a ese contenido (por ejemplo, un comentario en la celda: `# Función generada con Claude y verificada con 3 casos de prueba`).

## 3. Responsabilidad

- **Eres el autor o la autora de tu entrega.** Si un asistente se equivoca y tú lo entregas, el error es tuyo.
- **Debes poder explicar todo lo que entregas.** En las micro-sustentaciones (2–3 minutos, sin asistentes) explicas una celda de tu trabajo. Si no puedes explicar tu propia entrega, la nota de ese challenge se limita a 3.0.
- **Tus respuestas deben basarse en tus resultados.** Cada challenge tiene una configuración personal; una respuesta genérica escrita por un asistente, que no cita tus números, no cumple la rúbrica.

## 4. Deber de verificación

Los asistentes de IA se equivocan con seguridad y con buena redacción. Antes de usar una respuesta:

- [ ] **Ejecuta el código** y confirma que hace lo que dice. Revisa que no use parámetros obsoletos o inventados de las librerías.
- [ ] **Compara con tus salidas:** los números que escribes en tus respuestas deben ser los que imprimió tu notebook.
- [ ] **Verifica afirmaciones y cifras** en fuentes primarias (artículos, documentación oficial, normas). Si no puedes verificar una estadística, no la uses.
- [ ] **Revisa las referencias:** los asistentes inventan artículos, autores y enlaces. Abre cada fuente que cites.
- [ ] **Revisa licencias y condiciones de uso** de los modelos y datos que te sugiera usar.
- [ ] **Lee críticamente:** busca contradicciones, supuestos no dichos y conclusiones que tus datos no respaldan. Las tareas "Crítica a la IA" de cada challenge entrenan exactamente esto.

## 5. Usos prohibidos

| Prohibido | Ejemplos |
|---|---|
| **Suplantación** | Que otra persona, o un agente de IA que actúe por ti, resuelva tu challenge o presente tu micro-sustentación; entregar con el código estudiantil de otra persona; recibir ayuda de un asistente o de otra persona durante una micro-sustentación |
| **Resultados fabricados** | Escribir números que tu notebook no produjo; editar salidas a mano; ajustar resultados para que "se vean mejor"; citar estadísticas, casos o referencias que no existen o que no verificaste |
| **Compartir resultados personalizados** | Enviar a compañeros tu notebook ejecutado, tu configuración, tus resultados o tus respuestas; publicar soluciones de los challenges mientras el curso está en marcha |
| **Exponer datos personales o confidenciales** | Pegar en un asistente o en un agente datos personales o sensibles de personas reales (nombres, cédulas, teléfonos, datos de salud) o información confidencial de tu empresa. En Colombia, el tratamiento de datos personales está regulado por la Ley 1581 de 2012; en el curso usamos datos públicos o ficticios |
| **Ocultar el uso de IA** | Omitir usos relevantes en el registro o describirlos de forma engañosa |

Discutir conceptos con compañeros, ayudarse con un error de instalación o estudiar juntos **sí está permitido**. La línea está en compartir resultados y respuestas personalizadas.

## 6. Consecuencias

| Situación | Consecuencia |
|---|---|
| Falta el registro de uso de IA | El componente "Reflexión y registro de IA" (20%) vale 0.0 |
| Registro incompleto o genérico | Se refleja en el nivel de ese componente según la [rúbrica](evaluacion.md) |
| No puedes explicar tu entrega en la micro-sustentación | La nota de ese challenge se limita a 3.0 |
| Posible fraude académico: suplantación, resultados inventados o salidas personalizadas compartidas | Se tramita conforme al reglamento académico de la Universidad del Rosario; la entrega afectada puede calificarse con 0.0 |

Cuando se comparten salidas personalizadas, el proceso aplica tanto a quien las comparte como a quien entrega el trabajo compartido.

Si tienes dudas sobre si un uso está permitido, **pregunta antes de entregar**: declararlo y preguntar nunca te perjudica.

## 7. Ejemplos de registro de uso de IA

### Buenos registros

| # | Herramienta | ¿Para qué la usaste? | Prompt principal (resumido) | ¿Qué verificaste o corregiste? |
|---|---|---|---|---|
| 1 | ChatGPT | Entender por qué mi pérdida KL era negativa | "¿Por qué la divergencia KL de mi VAE da negativa? Este es mi código: …" | Me señaló el signo invertido en la fórmula. Lo corregí, volví a entrenar y la KL quedó positiva (0.84). Comprobé la fórmula con las slides de la sesión 02. |
| 2 | Claude | Mejorar la redacción de mi recomendación de negocio | "Haz más clara esta recomendación sin cambiar los números: …" | Revisé que los números siguieran siendo los de mi notebook (F1 = 0.71 y umbral 0.6). Eliminé una frase que añadió sobre "ahorros del 40%" porque no sale de mis datos. |
| 3 | Copilot | Autocompletar la función de la curva de aprendizaje | Sugerencias automáticas en la celda de la tarea 1 | La sugerencia entrenaba y evaluaba con los mismos datos. La cambié para evaluar en mi partición de prueba y lo verifiqué imprimiendo los tamaños de cada partición. |

### Registros insuficientes

| Registro | Por qué no sirve |
|---|---|
| "Usé ChatGPT para todo." | No dice para qué, ni cómo, ni qué verificaste. |
| "Claude — código — sí lo verifiqué." | La verificación no es verificable: ¿qué revisaste?, ¿qué encontraste? |
| "Le pedí la respuesta de la tarea 3 y la pegué." | Declara un uso que reemplaza tu análisis. La respuesta no citará tus números y no podrás defenderla en una micro-sustentación. |
| *(tabla vacía)* | Sin registro, el componente vale 0.0. Si no usaste IA, escribe la frase indicada. |

## 8. Por qué esta política

En tu trabajo, nadie te va a preguntar si usaste IA; te van a preguntar si el resultado es correcto, si lo puedes defender y si entiendes sus riesgos. Esta política practica esas tres cosas: **usar** la IA con propósito, **verificar** lo que produce y **responder** por el resultado.
