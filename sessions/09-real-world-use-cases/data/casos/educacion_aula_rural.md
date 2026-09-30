# Fundación Aula Rural — Preguntas de práctica para tabletas sin conexión

*Organización ficticia creada para el curso. Todas las cifras, nombres y reglas son inventadas.*

**Sector:** educación · **Tipo de solución:** generador de preguntas de práctica a partir de lecturas de ciencias, con verificación automática de que la pregunta se pueda responder con la lectura

## Contexto

La Fundación Aula Rural entrega tabletas con contenidos educativos a escuelas rurales multigrado, donde un solo docente enseña a estudiantes de varios grados al mismo tiempo. Las tabletas funcionan sin internet y se sincronizan una vez por semana. La fundación necesita entre 2.000 y 6.000 preguntas de práctica al mes para sus lecturas de ciencias naturales.

## Proceso actual

Un equipo de tres pedagogas adapta las lecturas y escribe las preguntas en español sencillo. Escribir, adaptar y revisar una pregunta toma en promedio 8 minutos. Si el generador propone una pregunta defectuosa, las pedagogas tardan unos 4 minutos adicionales en detectarla y reescribirla antes de la sincronización; si la detectan tarde, la pregunta confusa queda en las tabletas hasta la semana siguiente.

## Qué quiere lograr la fundación

La fundación quiere generar preguntas con su respuesta a partir de cada lectura, verificar automáticamente que se puedan responder con el texto y dejar a las pedagogas la adaptación final al contexto rural.

## Reglas del servicio (lo que el asistente debe saber)

- Las tabletas se sincronizan los viernes, cuando el docente visita la cabecera municipal.
- Cada escuela recibe 30 tabletas.
- Las preguntas deben estar en español sencillo, con frases cortas y ejemplos del entorno rural.
- Las tabletas no guardan datos personales de los estudiantes; solo el avance por lectura.
- El docente de cada escuela puede desactivar cualquier pregunta desde su tableta.

## Restricciones y riesgos conocidos

- El prototipo del curso se probó con lecturas en inglés: su desempeño en español no se ha medido.
- Los modelos grandes no caben en las tabletas y no hay internet en las escuelas: la generación debe hacerse en la oficina antes de sincronizar.
- Hay pocas lecturas y preguntas en español adaptadas al contexto rural para evaluar el sistema.
- Una pregunta confusa desmotiva a estudiantes que ya tienen barreras de acceso.

## Preguntas abiertas para el análisis

¿Qué datos en español necesitaría la fundación para validar el sistema? ¿Conviene traducir, usar un modelo multilingüe o afinar uno pequeño? ¿Cómo se mide el impacto en el aprendizaje, y no solo el ahorro de tiempo?
