# Universidad en Línea Colibrí — Banco de preguntas para cursos masivos

*Organización ficticia creada para el curso (la misma universidad del lab). Todas las cifras, nombres y reglas son inventadas.*

**Sector:** educación · **Tipo de solución:** generador de preguntas de práctica a partir de las lecturas de cada unidad, con verificación automática de que la pregunta se pueda responder con la lectura

## Contexto

La Universidad en Línea Colibrí ofrece cursos introductorios de ciencias con 12.000 estudiantes inscritos por periodo. Cada unidad tiene una lectura corta y un quiz de práctica. Para evitar que las preguntas circulen entre estudiantes, la universidad quiere renovar el banco de preguntas al inicio de cada periodo. Necesita entre 5.000 y 12.000 preguntas nuevas al mes durante la preparación de cada periodo.

## Proceso actual

Un equipo de tutores escribe las preguntas a partir de las lecturas. Escribir y revisar una pregunta toma en promedio 6 minutos. Si el generador propone una pregunta defectuosa, un tutor tarda unos 3 minutos adicionales en detectarla y corregirla o reemplazarla.

## Qué quiere lograr la universidad

La universidad quiere generar preguntas con su respuesta a partir de cada lectura, descartar automáticamente las que no se pueden responder con el texto y dejar a los tutores la revisión final y la clasificación por dificultad.

## Reglas del servicio (lo que el asistente debe saber)

- Los quices de práctica no cuentan para la nota final del curso.
- Cada pregunta del banco se etiqueta con un nivel de dificultad: básico, intermedio o avanzado.
- Los estudiantes pueden reportar una pregunta con el botón "Reportar error"; cada reporte se revisa en un máximo de 3 días hábiles.
- El banco de preguntas se renueva al inicio de cada periodo académico.
- Los tutores revisan una muestra de al menos el 20% de las preguntas generadas antes de publicarlas.

## Restricciones y riesgos conocidos

- Con miles de estudiantes, una pregunta errónea llega a muchas personas antes de que alguien la reporte.
- Revisar solo una muestra del 20% deja pasar errores en el resto.
- Las lecturas están en inglés y en español; el prototipo solo se ha probado en inglés.
- Hay que evitar sesgos culturales en los ejemplos de las preguntas.

## Preguntas abiertas para el análisis

¿Es suficiente revisar una muestra del 20%? ¿Qué indicador mostraría que las preguntas generadas ayudan a aprender y no solo a memorizar? ¿Cómo cambia el caso cuando se incluyan las lecturas en español?
