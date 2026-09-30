# Clínica Serena — Preclasificación de solicitudes de cita

*Organización ficticia creada para el curso. Todas las cifras, nombres y reglas son inventadas. Este documento no es consejo médico.*

**Sector:** salud · **Tipo de solución:** asistente de orientación que sugiere posibles condiciones para enrutar la solicitud (no diagnostica)

## Contexto

Clínica Serena es una clínica ambulatoria de tamaño mediano con consulta de medicina general, dermatología, neumología, gastroenterología y ortopedia. Los pacientes piden cita en un formulario web donde describen sus síntomas con sus propias palabras. Hoy recibe entre 4.000 y 9.000 solicitudes al mes, según la temporada.

## Proceso actual

Un equipo de enfermería lee cada solicitud y decide a qué agenda enviarla. En promedio tarda 6 minutos por solicitud. Cuando una solicitud llega a la especialidad equivocada, el paciente pierde la cita y el equipo debe reprogramarla, lo que toma unos 10 minutos adicionales.

## Qué quiere lograr la clínica

La clínica quiere un asistente que lea la descripción de síntomas y sugiera las **3 condiciones posibles** más parecidas a casos anteriores, para que enfermería elija la agenda más rápido. La decisión final siempre la toma una persona del equipo de enfermería.

## Reglas del servicio (lo que el asistente debe saber)

- Las citas se atienden de lunes a sábado, de 7:00 a 19:00.
- Una cita se puede cancelar sin costo hasta 24 horas antes; si se cancela más tarde, se cobra una multa de inasistencia.
- Si la persona describe dolor en el pecho, dificultad para respirar o pérdida de conciencia, el asistente debe indicarle que llame de inmediato a la línea de emergencias 123.
- El asistente nunca da diagnósticos ni recomienda medicamentos.
- Para usar el formulario, el paciente debe aceptar la autorización de tratamiento de datos sensibles de la clínica.

## Restricciones y riesgos conocidos

- Los datos de salud son datos sensibles: el tratamiento requiere autorización explícita del titular y medidas de seguridad reforzadas.
- Un error de enrutamiento en un caso grave puede retrasar la atención.
- Los pacientes escriben en español coloquial, con errores de ortografía y abreviaturas.
- El equipo de enfermería desconfía de herramientas que "decidan por ellas".

## Preguntas abiertas para el análisis

¿Cuántas sugerencias debe mostrar el asistente? ¿Qué pasa si la condición correcta no aparece entre las 3 sugeridas? ¿Cómo se medirá si la herramienta realmente ahorra tiempo?
