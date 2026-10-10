# Suplementos Spartans — guía para generar y publicar contenido

Este repositorio es la biblioteca de imágenes y el kit de diseño de la cuenta de Instagram **@spartan_fitness_spa** (Suplementos Spartans, Caldera, Chile). Todo lo que se publica sale de aquí: las imágenes se suben a este repo y Metricool las toma desde su URL raw.

Idioma de todo el contenido: español de Chile, cercano, con energía "espartana". Sin garabatos.

## La tienda

- Instagram: @spartan_fitness_spa · Metricool blogId **7278335** · zona horaria **America/Santiago**.
- Entregas: delivery en Caldera por $1.500 o retiro en domicilio. Entregas en Copiapó. Envíos a todo Chile por pagar, con la empresa que elija el cliente (Starken, Chilexpress, Blue Express); el plazo depende de la ciudad.
- Pago: transferencia, efectivo, tarjeta y Mercado Pago.
- Compra: por DM de Instagram. El dueño responde rápido.
- Productos originales y sellados. No hay devoluciones una vez abierto.
- Público: hombres y mujeres que entrenan, sin un nicho particular.
- El dueño puede salir en video, pero por defecto se muestran manos, brazos y producto, sin cara.

## Catálogo vigente (precios del dueño — no cambiarlos)

| Producto | Precio | Porciones | Imagen recortada |
| --- | --- | --- | --- |
| Whey USN Premium Whey+ 5 lb chocolate (22 g proteína/porción) | $70.000 | — | kit/build/p_whey.png |
| Creatina USN 300 g sin sabor (5 g/porción) | $25.000 | 60 | kit/build/p_usn_crea.png |
| Creatina MuscleTech Platinum 400 g sin sabor (micronizada, 5 g) | $39.000 | 80 | kit/build/p_mt_sin.png |
| Creatina MuscleTech Platinum 392 g uva Grape Freeze (5 g) | $43.000 | 60 | kit/build/p_mt_uva.png |
| Lipo 6 Black Ultra Concentrate, Nutrex, 60 cápsulas (222 mg cafeína/cápsula) | $30.000 | 60 | kit/build/p_lipo.png |
| Multivitamínico USN Super Daily Formula, 60 tabletas (2 por porción) | $30.000 | 30 | kit/build/p_multi.png |

Promoción real vigente: **por compra de proteína + creatina, shaker C4 de regalo** (kit/build/p_shaker.png).

Productos que pueden llegar (Dymatize ISO 100, Nitro Tech, Finaflex 1 kg, Ostrovit 21 g, Omega 3 USN, barras Space Protein, shots de guaraná): **no publicarlos** hasta que el dueño mande foto y precio.

## Reglas de confianza (obligatorias)

- Nunca inventar precios, stock, descuentos, testimonios, resultados ni escasez ("quedan pocas", "últimas unidades"). Urgencia solo si es real (fecha de una promoción que el dueño definió, llegada de stock real).
- Nada de promesas de cambios físicos ni curas. Lipo 6: presentarlo como termogénico con cafeína para energía al entrenar, nunca "baja X kilos"; incluir siempre la nota "Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas."
- Afirmaciones de suplementos solo las bien respaldadas (creatina 3–5 g/día, cualquier hora, todos los días, fase de carga opcional, retención de agua intramuscular, segura en personas sanas a dosis recomendadas). Ante enfermedad o medicamentos: "consulta a tu médico".
- Imágenes de producto: las oficiales de la marca que aprobó el dueño (kit/build/p_*.png; sus fotos originales quedan como p_*_real.png). Los textos siempre describen el producto que él vende (gramos y porciones de la tabla del catálogo), aunque la imagen oficial muestre otra versión del envase. No inventar envases ni modificar etiquetas. Fotos 4:5 listas en fotos/; catálogo en feed/catalogo/, serie de creatina en historias/serie_creatina/.
- Marcar `isAiGenerated: false` (son fotos reales con diseño gráfico).

## Identidad visual

Fondo negro (#060504) con brasas naranjas, naranjo Spartans #F26A1B, blanco. Títulos en Bebas Neue, textos en Barlow Condensed (mayúsculas). Casco naranjo (kit/build/helmet.png) + "SPARTANS" arriba. Feed 1080×1350 (4:5); historias 1080×1920 con lo importante fuera de los 250 px superiores e inferiores. Historias numeradas (2/5). No repetir el mismo formato en feed e historias; evitar que todo parezca catálogo.

## Cómo generar imágenes

Requisitos (ya presentes en el entorno): Python, Playwright con Chromium, Pillow.

- `kit/build/gen.py` — helpers: `FONTS`, `CSS` de feed, `FX` (brasas en canvas), `icon(nombre)` (íconos en `kit/npmw/node_modules/@tabler/icons/icons/outline`), `uri(ruta)`, `header()`, `bar_html()`, `product_slide(dict, seed)`, `render(pages)`.
- `kit/build/slides.py` — ejemplo de carrusel de producto (4:5). `python3 slides.py <carpeta_salida> [nombres]`.
- `kit/build/stories2.py` — ejemplo de serie de historias educativas 9:16 (gancho, mitos, costo por día, stack, objetivo). Úsalo como plantilla de estilo; escribe un script nuevo por serie.
- `kit/build/stock.py` — ejemplo de vitrina con repisas.
- `kit/build/destacadas.py` — portadas de destacadas (diseño centrado en un círculo de 500 px) e historias fijas "Cómo comprar" y "Cómo te llega". Salida en `destacadas/`.

Ejecuta los scripts desde `kit/build` (rutas relativas). Revisa SIEMPRE el render (abrirlo con Read) antes de publicar: textos que se salen, solapes, recortes.

## Cómo publicar

1. Guarda los JPG (calidad 90) en `historias/AAAA-MM-DD/` o `feed/AAAA-MM-DD/`, haz commit y push a `main`.
2. URL para Metricool: `https://raw.githubusercontent.com/matiasndc98-design/spartans-media/main/<ruta>`.
3. `createScheduledPost` con `blogId 7278335`, `providers [{"network":"instagram"}]`, `publicationDate {dateTime, timezone:"America/Santiago"}`.
   - Historia: `instagramData {"type":"STORY","isAiGenerated":false}`, sin `text`. Una historia por post, espaciadas 1 minuto en orden.
   - Carrusel: `instagramData {"type":"POST","isAiGenerated":false}`, varias URLs en `media`, con `text` (caption).
4. Antes de crear, revisa con `getScheduledPosts` para no duplicar.

## Calendario (horarios óptimos según Metricool)

| Día | Feed | Historias | Hora |
| --- | --- | --- | --- |
| Lunes | Carrusel educativo | Encuesta / tema de la semana | 10:00 |
| Martes | Reel (requiere video del dueño) | Pregunta frecuente | 18:00 |
| Miércoles | — | Producto de la semana con precio | 10:00 |
| Jueves | Reel (requiere video del dueño) | Detrás de la tienda | 18:00 |
| Viernes | Carrusel de producto o comparativa | Combo / promoción real | 10:00 |
| Sábado | Reel (requiere video del dueño) | Quiz o "esto o esto" | 10:00 |
| Domingo | — | Resumen y llamado al DM | 10:00 |

Temas: semana 11–17 oct creatina; 18–24 oct proteína; 25–31 oct energía para entrenar (Lipo 6); 1–7 nov base y constancia (multivitamínico, stacks). Plan detallado: https://claude.ai/code/artifact/1d8386c5-c08a-4f94-b6d2-ec741c11f133

Los reels necesitan video del dueño: no los publiques sin él. Las historias interactivas (encuestas, quiz) no se pueden publicar por API: diseña la pantalla con las opciones y el texto "Responde por DM" en vez de sticker.

## Registro de lo publicado

Agrega una línea por pieza en `registro.md` (fecha · formato · tema · archivos) para no repetir ideas.
