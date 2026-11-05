"""Viernes 6 nov 2026 · semana "base y constancia" · estilo SOBRIO.
Carrusel 4:5 comparativa "Elige tu proteína." con idea nueva COMPARADOR DE MODELOS (estilo "compare models" de las
marcas grandes de tecnología: los 3 envases alineados en el mismo piso, un solo número grande bajo cada uno) +
2 historias del combo real (shaker de regalo, encuesta de 3 opciones).
Uso (desde kit/build): python3 viernes_elige_proteina.py <carpeta_feed> <carpeta_historias>
"""
import sys
FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P
from lunes_la_base import recorte

W, H = 1080, 1350
SW, SH = P.SW, P.SH


def num(n):
    return f'<div class="foot" style="right:70px;top:74px">{n:02d} / 06</div>'


def portada():
    row = (P.heroe('p_whey.png', 250, 1160, 470) + P.heroe('p_nitro.png', 830, 1160, 470)
           + P.heroe('p_iso100.png', 540, 1175, 560))
    b = (P.marca(70, 64) + num(1) + row
         + '<div style="position:absolute;left:70px;top:190px"><div class="lab">Comparativa</div>'
           '<div class="h" style="font-size:200px;margin-top:18px">Elige tu</div><div class="h o" style="font-size:200px">proteína.</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px">Desliza</div><div class="rule" style="position:absolute;left:200px;bottom:72px;width:120px"></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


def comparador():
    cols = [('p_whey.png', 200, 400, '22 g', 'Whey USN'), ('p_iso100.png', 540, 470, '25 g', 'ISO 100'),
            ('p_nitro.png', 880, 400, '30 g', 'Nitro Tech')]
    prods = ''.join(P.heroe(img, cx, 900, h) for img, cx, h, _, _ in cols)
    datos = ''.join(
        f'<div style="position:absolute;left:{cx - 160}px;width:320px;top:1010px;text-align:center">'
        f'<div class="h{" o" if i == 2 else ""}" style="font-size:120px">{g}</div>'
        f'<div class="foot" style="position:static;margin-top:14px;color:#bdb8b0">{n}</div></div>'
        for i, (_, cx, _, g, n) in enumerate(cols))
    b = (P.marca(70, 64) + num(5) + prods + datos
         + '<div style="position:absolute;left:0;right:0;top:170px;text-align:center"><div class="lab">Proteína por porción</div>'
           '<div class="h" style="font-size:120px;margin-top:16px">Una para cada uno.</div></div>'
         + '<div style="position:absolute;left:150px;right:150px;top:975px;height:1px;background:rgba(244,241,236,.18)"></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.08)')


def cierre():
    b = (P.marca(70, 64) + num(6)
         + P.heroe('p_whey.png', 330, 1080, 520) + P.heroe('p_shaker.png', 600, 1080, 470) + P.heroe('p_usn_crea.png', 820, 1080, 380)
         + '<div style="position:absolute;left:0;right:0;top:170px;text-align:center"><div class="lab">Spartans</div>'
           '<div class="h" style="font-size:150px;margin-top:16px">Pídela</div><div class="h o" style="font-size:150px">por DM.</div></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Proteína + creatina <span class="o">·</span> Shaker de regalo</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


def h_regalo():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Promoción vigente</div>'
           '<div class="h" style="font-size:190px;margin-top:26px">El regalo.</div></div>'
         + P.heroe('p_shaker.png', 540, 1340, 700)
         + '<div style="position:absolute;left:0;right:0;bottom:290px;text-align:center">'
           '<div class="h" style="font-size:72px">Proteína + creatina.</div><div class="h o" style="font-size:72px">Shaker C4 de regalo.</div>'
           '<div class="foot" style="position:static;margin-top:20px;color:#bdb8b0">Pídelo por DM · Delivery en Caldera $1.500</div></div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


def h_encuesta():
    # sticker de encuesta en 720–1060 (libre)
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Esta semana</div>'
           '<div class="h" style="font-size:150px;margin-top:26px">¿Cuál es</div><div class="h o" style="font-size:150px">la tuya?</div></div>'
         + P.heroe('p_whey.png', 260, 1580, 380) + P.heroe('p_iso100.png', 540, 1590, 430) + P.heroe('p_nitro.png', 820, 1580, 380)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">22 g · 25 g · 30 g de proteína por porción</div>')
    return P.page(SW, SH, b, 'rgba(60,110,170,.10)')


if __name__ == '__main__':
    P.render([
        ('1_elige_tu_proteina', portada()),
        ('2_whey_usn', recorte(2, 'p_whey.png', 'Whey USN · 5 lb chocolate', '22 g.', 'El clásico.', 'Premium Whey+ · por scoop', 'rgba(140,70,30,.16)', left=520)),
        ('3_iso100', recorte(3, 'p_iso100.png', 'Dymatize ISO 100 · 5 lb', '25 g.', '100% isolate.', '71 porciones · Cocoa Pebbles', 'rgba(60,110,170,.14)', left=540)),
        ('4_nitro_tech', recorte(4, 'p_nitro.png', 'MuscleTech Nitro Tech · 4 lb', '30 g.', '+ 3 g de creatina.', 'Por porción · Vainilla', 'rgba(200,30,30,.12)', left=540)),
        ('5_comparador', comparador()),
        ('6_pidela', cierre()),
    ], FEED, W, H)
    P.render([('1_el_regalo', h_regalo()), ('2_cual_es_la_tuya', h_encuesta())], HIST, SW, SH)
