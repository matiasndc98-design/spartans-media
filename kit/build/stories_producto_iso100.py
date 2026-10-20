"""Miércoles 21 oct · "Producto de la semana" (estilo premium): Dymatize ISO 100 Cocoa Pebbles.
Idea nueva: "No solo en shaker" (3 formas de tomarla para guardar, tendencia de recetas rápidas con proteína)
+ ficha técnica con números grandes. Sin precios.
Secuencia: portada -> ficha -> 3 formas -> encuesta (espacio libre para sticker).
Uso (desde kit/build): python3 stories_producto_iso100.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
W, H = P.SW, P.SH
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Producto de la semana</div>'
GLOW = 'rgba(60,110,170,.18)'


def portada():
    b = (P.marca(70, 150) + TOP + P.heroe('p_iso100.png', 540, 1560, 860)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Dymatize ISO 100 · Cocoa Pebbles</div>'
           '<div class="h" style="font-size:132px;margin-top:24px">Sabor a cereal.</div>'
           '<div class="h o" style="font-size:132px">Proteína de adulto.</div></div>')
    return P.page(W, H, b, GLOW)


def ficha():
    def stat(num, lab, top):
        return (f'<div style="position:absolute;left:80px;top:{top}px"><div class="h" style="font-size:190px">{num}</div>'
                f'<div class="lab" style="margin-top:6px">{lab}</div></div>')
    b = (P.marca(70, 150) + TOP + P.heroe('p_iso100.png', 860, 1600, 640)
         + '<div style="position:absolute;left:80px;top:330px"><div class="lab o" style="color:#F26A1B">La ficha</div></div>'
         + stat('25 g', 'de proteína por scoop', 400)
         + stat('71', 'porciones por tarro', 680)
         + stat('100<span class="o">%</span>', 'whey isolate hidrolizada', 960)
         + '<div style="position:absolute;left:80px;width:560px;top:1290px"><div class="rule" style="margin-bottom:24px"></div>'
           '<div style="font-size:38px;line-height:1.28;font-weight:500;color:#e8e4dd">Isolate: proteína más filtrada, con menos lactosa y grasa que una whey normal. Hidrolizada: en partes más pequeñas.</div></div>')
    return P.page(W, H, b, GLOW)


def formas():
    items = [('Shaker', 'Con agua o leche bien fría. Sabe a la leche del cereal.'),
             ('Avena', 'Mézclala cuando la avena ya se entibió, no hirviendo.'),
             ('Yogur', 'Con yogur natural: postre alto en proteína.')]
    rows = ''
    for i, (t, d) in enumerate(items):
        top = 760 + i * 250
        rows += (f'<div style="position:absolute;left:80px;right:80px;top:{top}px;display:flex;gap:40px;align-items:flex-start">'
                 f'<div class="h o" style="font-size:120px;width:90px">{i + 1}</div>'
                 f'<div><div class="h" style="font-size:96px">{t}</div>'
                 f'<div style="font-size:36px;line-height:1.25;color:#bdb8b0;font-weight:500;margin-top:6px">{d}</div></div></div>')
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:340px"><div class="lab">Guárdala</div>'
           '<div class="h" style="font-size:170px;margin-top:20px">No solo</div><div class="h o" style="font-size:170px">en shaker.</div></div>'
         + rows
         + '<div style="position:absolute;left:0;right:0;bottom:270px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídela por DM <span class="o">·</span> Con creatina, shaker de regalo</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.07)')


def encuesta():
    b = (P.marca(70, 150) + TOP + P.heroe('p_iso100.png', 540, 1660, 420)
         + '<div style="position:absolute;left:0;right:0;top:340px;text-align:center"><div class="lab">Tu turno</div>'
           '<div class="h" style="font-size:170px;margin-top:24px">¿Cómo la</div><div class="h o" style="font-size:170px">tomarías?</div></div>')
    # espacio libre ~300 px (y 760–1160) para el sticker de encuesta
    return P.page(W, H, b, GLOW)


if __name__ == '__main__':
    P.render([('1_producto_semana_iso100', portada()), ('2_la_ficha', ficha()),
              ('3_no_solo_en_shaker', formas()), ('4_encuesta_como_la_tomarias', encuesta())], OUT, W, H)
