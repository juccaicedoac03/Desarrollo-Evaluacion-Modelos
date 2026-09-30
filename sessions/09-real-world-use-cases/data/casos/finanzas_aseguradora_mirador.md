# Aseguradora Mirador — Monitoreo de noticias del portafolio y reputación

*Organización ficticia creada para el curso. Todas las cifras, nombres y reglas son inventadas. Este documento no es asesoría financiera.*

**Sector:** finanzas · **Tipo de solución:** clasificador de sentimiento de noticias financieras (alcista, bajista o neutral) para vigilar inversiones y riesgo reputacional

## Contexto

Aseguradora Mirador invierte las reservas de sus pólizas en un portafolio de bonos y acciones. Su equipo de riesgos vigila las noticias sobre las empresas del portafolio y sobre la propia aseguradora. Recibe entre 10.000 y 30.000 titulares en inglés al mes.

## Proceso actual

Un equipo de tres personas lee los titulares, marca los que pueden afectar al portafolio o a la reputación de la aseguradora y prepara un informe semanal. Revisar un titular toma en promedio 1,2 minutos. Un titular mal clasificado obliga a volver a la fuente y corregir su marca en el informe, lo que toma unos 2 minutos adicionales.

## Qué quiere lograr la aseguradora

Aseguradora Mirador quiere clasificar automáticamente los titulares en alcistas, bajistas o neutrales, y concentrar el trabajo del equipo en los bajistas.

## Reglas del servicio (lo que el asistente debe saber)

- Las decisiones de inversión las toma el Comité de Inversiones, que se reúne todos los martes.
- Una alerta reputacional (noticia negativa sobre la aseguradora) debe escalarse al equipo de comunicaciones en un máximo de 2 horas.
- El sistema solo analiza noticias públicas; nunca datos de clientes ni de pólizas.
- El informe semanal de riesgos se entrega los lunes antes de las 12:00.
- Ninguna alerta automática puede ordenar la compra o venta de un activo.

## Restricciones y riesgos conocidos

- Los falsos negativos (noticias bajistas no detectadas) son el error más costoso para el equipo de riesgos.
- Las noticias sobre la aseguradora pueden estar en español; el piloto solo cubre titulares en inglés.
- La supervisión financiera exige poder explicar cómo se tomó una decisión de inversión.
- El equipo tiene poca experiencia técnica y depende de un proveedor externo.

## Preguntas abiertas para el análisis

¿Cómo se ajusta el sistema para no perder noticias bajistas, aunque aumenten las falsas alarmas? ¿Qué pasa con las noticias en español? ¿Quién mantiene el modelo cuando el proveedor termine el contrato?
