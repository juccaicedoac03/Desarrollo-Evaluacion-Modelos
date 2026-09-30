# TeleSalud Caribe — Priorización de la línea nocturna de orientación

*Organización ficticia creada para el curso. Todas las cifras, nombres y reglas son inventadas. Este documento no es consejo médico.*

**Sector:** salud · **Tipo de solución:** asistente que sugiere posibles condiciones para ordenar la fila de atención del médico de turno (no diagnostica)

## Contexto

TeleSalud Caribe es un operador de telemedicina con sede en Barranquilla. Su línea nocturna de orientación funciona por chat de 22:00 a 6:00, todos los días. Recibe entre 6.000 y 15.000 chats al mes; los picos coinciden con temporadas de lluvias y con brotes de enfermedades respiratorias.

## Proceso actual

Un auxiliar lee cada chat, lo clasifica como prioridad alta, media o baja y lo pone en la fila del médico de turno. Clasificar un chat toma en promedio 5 minutos. Si un chat queda con una prioridad equivocada, el médico debe reordenar la fila y contactar de nuevo al paciente, lo que toma unos 8 minutos.

## Qué quiere lograr la empresa

TeleSalud Caribe quiere que un asistente sugiera las **3 condiciones posibles** más parecidas a casos anteriores, para que el auxiliar asigne la prioridad más rápido y con más consistencia. El médico de turno siempre decide la conducta.

## Reglas del servicio (lo que el asistente debe saber)

- El médico de turno responde cada chat en un máximo de 30 minutos.
- Si la persona describe una señal de alarma (dolor en el pecho, dificultad para respirar, convulsiones o sangrado abundante), el asistente debe indicarle que llame a la línea de emergencias 123 sin esperar al médico.
- Las conversaciones se guardan cifradas y solo el equipo médico puede verlas.
- El asistente no receta medicamentos ni emite incapacidades.
- La línea atiende a afiliados de los planes Básico y Plus de TeleSalud Caribe.

## Restricciones y riesgos conocidos

- De noche hay un solo médico por cada 40 chats en espera: priorizar mal tiene consecuencias.
- El riesgo más grave es el de *subpriorizar*: dejar al final de la fila un caso urgente.
- Muchos pacientes escriben desde el celular, con mensajes cortos y poco detallados.
- Los datos de salud son datos sensibles y no pueden salir de la infraestructura contratada por la empresa.

## Preguntas abiertas para el análisis

¿Qué nivel de acierto es aceptable para un asistente que solo ordena la fila? ¿Cómo se detectarían los casos subpriorizados? ¿Quién responde si el asistente se equivoca?
