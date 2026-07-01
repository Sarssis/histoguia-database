# Histoguía Database

Base de datos editorial para Histoguía: una guía de podcasts de Historia en español organizada desde la Prehistoria hasta nuestros días.

## Principio clave
Solo se incluyen en `episodes.json` episodios con enlace verificado de Apple Podcasts a episodio concreto.

## Estructura
- `data/phases.json`: La Gran Ruta de la Historia, 16 fases.
- `data/podcasts.json`: podcasts admitidos o pendientes de verificación.
- `data/episodes.json`: episodios verificados publicables.
- `data/topics.json`: índice derivado de temas, personajes, lugares y batallas.
- `data/schema.json`: reglas y campos.
- `exports/episodes.csv`: exportación para revisión en Excel/Sheets.
- `exports/data.js`: exportación preparada para la app actual.
- `scripts/validate.py`: validación básica.

## Estado inicial
Esta versión incluye la arquitectura definitiva y un primer lote de episodios verificados. La base se ampliará por lotes.
