# Andes Bank — Resumen matutino de noticias para asesores

*Organización ficticia creada para el curso. Todas las cifras, nombres y reglas son inventadas. Este documento no es asesoría financiera.*

**Sector:** finanzas · **Tipo de solución:** clasificador de sentimiento de noticias financieras (alcista, bajista o neutral) para priorizar lo que leen los asesores

## Contexto

Andes Bank es un banco digital que ofrece a sus clientes inversión en acciones y fondos internacionales. Su equipo de asesoría prepara cada mañana un resumen interno con las noticias relevantes sobre las empresas en las que invierten sus clientes. Entre agencias de noticias y redes sociales financieras llegan entre 20.000 y 60.000 titulares en inglés al mes.

## Proceso actual

Dos analistas leen los titulares de la noche anterior y marcan cuáles son alcistas (*bullish*), bajistas (*bearish*) o neutrales. Revisar un titular toma en promedio 1,5 minutos. Cuando un titular se marca mal, el asesor pierde tiempo o se entera tarde de una noticia importante; detectar y corregir cada titular mal marcado toma unos 2 minutos adicionales.

## Qué quiere lograr el banco

Andes Bank quiere clasificar automáticamente los titulares para que los analistas revisen primero los bajistas y alcistas, y dediquen menos tiempo a los neutrales, que son la mayoría.

## Reglas del servicio (lo que el asistente debe saber)

- El resumen matutino es de uso interno: no se comparte con clientes ni se publica.
- Solo se usan noticias de proveedores con licencia vigente.
- Toda noticia bajista sobre una empresa en la que invierte un cliente debe ser revisada por un analista en un máximo de 4 horas.
- Los asesores no pueden dar recomendaciones de inversión personalizadas por chat; solo en una asesoría agendada.
- El resumen se envía a los asesores a las 7:00, de lunes a viernes.

## Restricciones y riesgos conocidos

- Un titular bajista marcado como neutral puede retrasar una llamada importante a un cliente.
- Los modelos disponibles están entrenados con noticias en inglés; las noticias en español no están incluidas en el piloto.
- Las decisiones de inversión de los clientes están reguladas: el sistema no puede presentarse como recomendación.
- El lenguaje financiero cambia rápido (nuevas siglas, tickers y jerga).

## Preguntas abiertas para el análisis

¿Qué error es más costoso: un falso bajista o un bajista no detectado? ¿Cuánto tiempo real se ahorra si los analistas igual revisan todo lo bajista? ¿Cómo se monitorea el modelo cuando cambia el lenguaje del mercado?
