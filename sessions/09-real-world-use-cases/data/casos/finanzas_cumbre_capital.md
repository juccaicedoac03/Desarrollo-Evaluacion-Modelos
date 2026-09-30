# Cumbre Capital — Alertas de noticias sobre emisores

*Organización ficticia creada para el curso. Todas las cifras, nombres y reglas son inventadas. Este documento no es asesoría financiera.*

**Sector:** finanzas · **Tipo de solución:** clasificador de sentimiento de noticias financieras (alcista, bajista o neutral) para generar alertas de investigación

## Contexto

Cumbre Capital es una firma comisionista de bolsa con un equipo de investigación económica de seis personas. Hoy hace seguimiento a 150 emisores (empresas que emiten acciones o bonos) y quiere ampliar la cobertura a 400 sin contratar más analistas. Recibe entre 15.000 y 45.000 titulares en inglés al mes.

## Proceso actual

Cada analista revisa los titulares de los emisores que tiene asignados y decide si generan una alerta. Revisar un titular toma en promedio 1 minuto. Un titular mal clasificado obliga al analista a volver a la fuente y corregir la marca antes de decidir la alerta, lo que toma unos 2 minutos adicionales. Una alerta equivocada que llega a los clientes es mucho más costosa: obliga a publicar una corrección.

## Qué quiere lograr la firma

Cumbre Capital quiere que un modelo clasifique los titulares en alcistas, bajistas o neutrales para que los analistas solo lean con detalle los que pueden generar una alerta.

## Reglas del servicio (lo que el asistente debe saber)

- Las alertas se envían a los clientes suscritos a las 7:30, de lunes a viernes.
- Toda alerta roja (noticia bajista de alto impacto) debe ser validada por un analista antes de enviarse.
- Las alertas son información de mercado, no recomendaciones de inversión, y así deben rotularse.
- El registro de cada alerta enviada se conserva durante 5 años.
- El equipo solo usa fuentes de noticias con licencia y nunca información privilegiada.

## Restricciones y riesgos conocidos

- Una alerta falsa enviada a clientes afecta la reputación de la firma.
- El volumen de titulares se dispara en temporada de resultados trimestrales.
- Los modelos disponibles no conocen los emisores locales ni sus siglas.
- Las comunicaciones con clientes están sujetas a supervisión regulatoria.

## Preguntas abiertas para el análisis

¿Qué exactitud mínima necesita el modelo para que la ampliación a 400 emisores sea viable? ¿Qué parte del trabajo sigue siendo humana? ¿Cómo se documentan las decisiones del modelo ante un supervisor?
