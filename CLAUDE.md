# Suplementos Spartans — guía para generar y publicar contenido

Este repositorio es la biblioteca de imágenes y el kit de diseño de la cuenta de Instagram **@spartan_fitness_spa** (Suplementos Spartans, Caldera, Chile). Todo lo que se publica sale de aquí: las imágenes se suben a este repo y Metricool las toma desde su URL raw.

Idioma de todo el contenido: español de Chile, cercano, con energía "espartana". Sin garabatos. Horas en los diseños en formato 12 horas con AM/PM ("10 AM", "6 PM"), nunca "10:00".

## La tienda

- Instagram: @spartan_fitness_spa · Metricool blogId **7278335** · zona horaria **America/Santiago**.
- Entregas: delivery en Caldera por $1.500 o retiro en domicilio. Entregas en Copiapó. Envíos a todo Chile por pagar, con la empresa que elija el cliente (Starken, Chilexpress, Blue Express); el plazo depende de la ciudad.
- Pago: transferencia, efectivo, tarjeta y Mercado Pago.
- Compra: por DM de Instagram. El dueño responde rápido.
- Productos originales y sellados. No hay devoluciones una vez abierto.
- Público: hombres y mujeres que entrenan, sin un nicho particular.
- El dueño puede salir en video, pero por defecto se muestran manos, brazos y producto, sin cara.

## Catálogo vigente (precios del dueño — no cambiarlos)

| Producto | Precio | Porciones / formato | Imagen recortada |
| --- | --- | --- | --- |
| Whey USN Premium Whey+ 5 lb chocolate (22 g proteína/porción) | $70.000 | 5 lb | kit/build/p_whey.png |
| Dymatize ISO 100 Hydrolyzed 5 lb Cocoa Pebbles (25 g proteína, 100% whey isolate) | $149.990 | 71 | kit/build/p_iso100.png |
| MuscleTech Nitro Tech 4 lb vainilla (30 g proteína + 3 g creatina por porción) | $99.990 | 4 lb | kit/build/p_nitro.png |
| Creatina USN 300 g sin sabor (5 g/porción) | $25.000 | 60 | kit/build/p_usn_crea.png |
| Creatina MuscleTech Platinum 400 g sin sabor (micronizada, 5 g) | $39.000 | 80 | kit/build/p_mt_sin.png |
| Creatina MuscleTech Platinum 392 g uva Grape Freeze (5 g) | $43.000 | 60 | kit/build/p_mt_uva.png |
| Creatina Finaflex 1 kg sin sabor (micronizada, 5 g, NSF Contents Certified) | $49.990 | 200 | kit/build/p_finaflex.png |
| Lipo 6 Black Ultra Concentrate, Nutrex, 60 cápsulas (222 mg cafeína/cápsula) | $30.000 | 60 | kit/build/p_lipo.png |
| Multivitamínico USN Super Daily Formula, 60 tabletas (2 por porción) | $30.000 | 30 | kit/build/p_multi.png |
| Omega 3 USN Fish Oil 1000 mg, 90 cápsulas blandas | $16.990 | 90 | kit/build/p_omega.png |
| Guaraná Shot OstroVit 80 ml sabor pera (200 mg cafeína) | $2.490 c/u | 1 shot | kit/build/p_guarana.png |
| Barra Space Protein XXL 80 g coco (36% proteína, 3 g azúcar) | $2.490 c/u | 1 barra | kit/build/p_barra.png |

Creatina OstroVit 21 g (sobre): no se vende; el dueño la usa como regalo para clientes frecuentes. No publicarla como promoción a menos que él lo pida.

Promoción real vigente: **por compra de proteína + creatina, shaker C4 de regalo** (kit/build/p_shaker.png).

Guaraná Shot: incluir siempre "Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas." No combinar en la misma recomendación con Lipo 6 (ambos tienen cafeína).

Productos nuevos que lleguen: no publicarlos hasta que el dueño mande imagen y precio.

## Reglas de confianza (obligatorias)

- Nunca inventar precios, stock, descuentos, testimonios, resultados ni escasez ("quedan pocas", "últimas unidades"). Urgencia solo si es real (fecha de una promoción que el dueño definió, llegada de stock real).
- Nada de promesas de cambios físicos ni curas. Lipo 6: presentarlo como termogénico con cafeína para energía al entrenar, nunca "baja X kilos"; incluir siempre la nota "Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas."
- Afirmaciones de suplementos solo las bien respaldadas (creatina 3–5 g/día, cualquier hora, todos los días, fase de carga opcional, retención de agua intramuscular, segura en personas sanas a dosis recomendadas). Ante enfermedad o medicamentos: "consulta a tu médico".
- Imágenes de producto: imágenes oficiales de la versión exacta que vende el dueño (kit/build/p_*.png; sus fotos originales quedan como p_*_real.png). Los textos siempre describen el producto que él vende (gramos y porciones del catálogo). No inventar envases ni modificar etiquetas. Fotos 4:5 listas en Fotos/; catálogo en Feed/catalogo/, serie de creatina en Historias/serie_creatina/.
- Marcar `isAiGenerated: false` (son fotos reales con diseño gráfico).

## Identidad visual

Fondo negro (#060504) con brasas naranjas, naranjo Spartans #F26A1B, blanco. Títulos en Bebas Neue, textos en Barlow Condensed (mayúsculas). Casco naranjo (kit/build/helmet.png) + "SPARTANS" arriba. Feed 1080×1350 (4:5); historias 1080×1920 con lo importante fuera de los 250 px superiores e inferiores. Historias **sin numeración** (nada de 1/5, 2/5: el orden lo controlamos nosotros al programar). **Historias y reels sin precios de productos** (decisión del dueño): en historias usar beneficios, datos (gramos, porciones, días que dura) y llamado al DM; los precios van solo en carruseles de catálogo del feed y la destacada Precios. El costo de delivery ($1.500) sí puede aparecer. No repetir el mismo formato en feed e historias; evitar que todo parezca catálogo.

## Cómo generar imágenes

Requisitos (ya presentes en el entorno): Python, Playwright con Chromium, Pillow.

- `kit/build/gen.py` — helpers: `FONTS`, `CSS` de feed, `FX` (brasas en canvas), `icon(nombre)` (íconos en `kit/npmw/node_modules/@tabler/icons/icons/outline`), `uri(ruta)`, `header()`, `bar_html()`, `product_slide(dict, seed)`, `render(pages)`.
- `kit/build/slides.py` — ejemplo de carrusel de producto (4:5). `python3 slides.py <carpeta_salida> [nombres]`.
- `kit/build/stories2.py` — ejemplo de serie de historias educativas 9:16 (gancho, mitos, costo por día, stack, objetivo). Úsalo como plantilla de estilo; escribe un script nuevo por serie.
- `kit/build/stock.py` — ejemplo de vitrina con repisas.
- `kit/build/recorte.py` — recorta imágenes oficiales de producto a PNG transparente sin sombra (`--hull` para frascos de etiqueta blanca).
- `kit/build/nuevos.py` — ejemplo de lanzamiento de productos nuevos: carrusel + historias.
- `kit/build/reel.py` — reel animado 9:16 de 15 s (animaciones CSS renderizadas cuadro a cuadro + ffmpeg). Salida en `Reels/`. Los reels se publican con `autoPublish: false` para que el dueño agregue música en Instagram.
- `kit/build/reel_proteina.py` — ejemplo de reel educativo (no centrado en productos) que reutiliza `reel.py` reemplazando `body()`. Ideas: cálculos, mitos, tips de entrenamiento, comparativas; remate breve con producto al final.
- `kit/build/destacadas.py` — portadas de destacadas (diseño centrado en un círculo de 500 px) e historias fijas "Cómo comprar" y "Cómo te llega". Salida en `Destacadas/`.

Ejecuta los scripts desde `kit/build` (rutas relativas). Revisa SIEMPRE el render (abrirlo con Read) antes de publicar: textos que se salen, solapes, recortes.

## Cómo publicar

1. Guarda los JPG (calidad 90) en `Historias/AAAA-MM-DD/` o `Feed/AAAA-MM-DD/`, haz commit y push a `main`.
2. URL para Metricool: `https://raw.githubusercontent.com/matiasndc98-design/spartans-media/main/<ruta>`.
3. `createScheduledPost` con `blogId 7278335`, `providers [{"network":"instagram"}]`, `publicationDate {dateTime, timezone:"America/Santiago"}`.
   - Historia: `instagramData {"type":"STORY","isAiGenerated":false}`, sin `text`. Una historia por post, espaciadas **2 minutos** en orden. Si hay que corregir una historia de una secuencia ya programada, no edites solo esa: pasa toda la secuencia a borrador y créala completa de nuevo (editar cambia el orden de publicación en Metricool).
   - Carrusel: `instagramData {"type":"POST","isAiGenerated":false}`, varias URLs en `media`, con `text` (caption).
4. Antes de crear, revisa con `getScheduledPosts` lo programado y con `getAnalyticsDataByMetrics` (IGST02, IGST05, IGST07; últimos 2 días) las historias ya publicadas, incluidas las que sube el dueño a mano, para no repetir tema ni producto. Metricool sincroniza las historias publicadas con algo de retraso.
5. Historias interactivas (encuesta, quiz, "esto o esto", preguntas): prográmalas con `autoPublish: false`. Metricool le manda un aviso a la app del dueño y él la publica a mano desde Instagram, agregando el sticker (encuesta, quiz o pregunta) y hashtags escondidos. Diseña esas pantallas dejando un espacio libre de unos 300 px de alto para el sticker. El resto de las historias va con `autoPublish: true`. En el resumen final, avisa qué historias quedaron en modo aviso y qué sticker poner.

## Robot propio (alternativa gratis a Metricool)

`Robot/` publica en Instagram desde GitHub Actions cada 15 minutos lo que esté en `Robot/cola.json` (ver `Robot/LEEME.md`). Cuando los secretos `IG_TOKEN` e `IG_USER_ID` estén configurados (el dueño avisa), programa ahí en vez de Metricool: agrega elementos `{"id","cuando" (ISO con -03:00),"tipo" HISTORIA|POST|CARRUSEL|REEL,"archivos":[rutas del repo],"texto","estado":"pendiente"}` y haz push. Revisa en la cola los elementos con `estado: error` y corrígelos. Piezas con stickers o música van igual a Metricool en modo aviso o se le mandan al dueño.

## Calendario (horarios óptimos según Metricool)

| Día | Feed | Historias | Hora |
| --- | --- | --- | --- |
| Lunes | Carrusel educativo | Encuesta / tema de la semana | 10:00 |
| Martes | Reel animado educativo | Pregunta frecuente | 18:00 |
| Miércoles | — | Producto de la semana con precio | 10:00 |
| Jueves | Reel animado (producto o comparativa) | Detrás de la tienda | 18:00 |
| Viernes | Carrusel de producto o comparativa | Combo / promoción real | 10:00 |
| Sábado | Reel animado educativo | Quiz o "esto o esto" | 10:00 |
| Domingo | — | Resumen y llamado al DM | 10:00 |

Temas: semana 11–17 oct creatina (incluye Finaflex 1 kg); 18–24 oct proteína (Whey USN, ISO 100, Nitro Tech, barra Space Protein); 25–31 oct energía para entrenar (Lipo 6, Guaraná Shot); 1–7 nov base y constancia (multivitamínico, Omega 3, stacks). El 11 oct se publicó el lanzamiento de los productos nuevos. Plan detallado: https://claude.ai/code/artifact/1d8386c5-c08a-4f94-b6d2-ec741c11f133

Reels: animados con `kit/build/reel.py` (base) siguiendo el formato de `reel_proteina.py`, que al dueño le encantó: gancho con pregunta → dato con fuente → ejemplo concreto → cómo aplicarlo → remate breve con producto y "Guárdalo y escríbenos". 15–18 s, sin música, `type: REEL` y `autoPublish: false` para que el dueño agregue música en Instagram. Cada reel nuevo debe mejorar algo respecto del anterior (ritmo, gancho, transición o dato). Si el dueño manda video real, se edita y se prioriza. Las historias interactivas van en modo aviso (`autoPublish: false`, ver Cómo publicar) para que el dueño agregue el sticker.

## Hashtags

Mezcla en cada caption (máximo 8): 2 grandes, 3 de nicho y 3 locales. Grandes: #gym #fitness #suplementos. Nicho: #suplementosdeportivos #suplementoschile #proteina #creatina #wheyprotein #hipertrofia. Locales: #caldera #copiapo #atacama #suplementoscaldera #gymcaldera #spartans. Agrega la marca del producto cuando corresponda (#dymatize #muscletech #usn #nutrex).

## Estructura del repositorio

- `Feed/` — publicaciones del feed: `Feed/AAAA-MM-DD/` por fecha y `Feed/catalogo/`.
- `Historias/` — historias: `Historias/AAAA-MM-DD/` por fecha, series reutilizables y `stock_disponible.jpg`.
- `Destacadas/` — portadas e historias fijas de las destacadas.
- `Fotos/` — fotos de producto 4:5 sobre negro.
- `Reels/` — reels animados (mp4).
- `Robot/` — robot de publicación gratis (cola.json, scripts) y `.github/workflows/`.
- `kit/` — scripts, fuentes, íconos e imágenes recortadas (`kit/build/p_*.png`).
Mantén este orden: nada suelto en la raíz, nombres de carpeta con mayúscula inicial, y borra versiones descartadas.

## Innovar siempre

Antes de diseñar una serie nueva, busca en internet (WebSearch) tendencias recientes de contenido de marcas de suplementos y fitness en Instagram (formatos de historias, ganchos, reels que funcionan) y aplica al menos una idea nueva, respetando las reglas de confianza. Si una imagen oficial de producto de mejor calidad está disponible, pídesela al dueño (el entorno no puede descargar imágenes de sitios externos).

## Registro de lo publicado

Agrega una línea por pieza en `registro.md` (fecha · formato · tema · archivos) para no repetir ideas.
