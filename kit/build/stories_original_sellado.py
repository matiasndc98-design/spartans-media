"""Jueves 22 oct · "Detrás de la tienda" (estilo premium, semana de la proteína): "¿Original o pirata?".
Idea nueva: LUPA DE DETALLE (círculo con zoom sobre la parte real del envase: sello de la tapa, datos de la etiqueta),
estilo de fichas de marcas grandes, con chequeos que el cliente puede hacer al recibir (transparencia / confianza).
Secuencia: gancho -> chequeo sello -> chequeo etiqueta -> chequeo polvo -> cierre con espacio para encuesta.
Uso (desde kit/build): python3 stories_original_sellado.py <carpeta_salida>
"""
import sys
from PIL import Image
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
W, H = P.SW, P.SH
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Detrás de la tienda</div>'
SIZE = {n: Image.open(n).size for n in ['p_whey.png', 'p_iso100.png', 'p_nitro.png']}


def lupa(img, cx, base_y, height, fx, fy, lx, ly, d=380, zoom=2.4, texto=''):
    """Producto héroe + punto sobre el detalle (fx, fy en fracción de la imagen) + línea + lente circular con zoom."""
    iw, ih = SIZE[img]
    w = height * iw / ih
    px, py = cx - w / 2 + fx * w, base_y - height + fy * height
    zh = height * zoom
    zw = zh * iw / ih
    ix, iy = d / 2 - fx * zw, d / 2 - fy * zh
    dx, dy = lx - px, ly - py
    import math
    L = math.hypot(dx, dy) - d / 2
    ang = math.degrees(math.atan2(dy, dx))
    return (P.heroe(img, cx, base_y, height)
            + f'<div style="position:absolute;left:{px}px;top:{py}px;width:{L}px;height:2px;background:{OR};transform-origin:0 50%;transform:rotate({ang}deg)"></div>'
            + f'<div style="position:absolute;left:{px - 9}px;top:{py - 9}px;width:18px;height:18px;border-radius:50%;background:{OR};box-shadow:0 0 0 6px rgba(242,106,27,.25)"></div>'
            + f'<div style="position:absolute;left:{lx - d / 2}px;top:{ly - d / 2}px;width:{d}px;height:{d}px;border-radius:50%;overflow:hidden;'
              f'border:3px solid {OR};background:#1b1b1b;box-shadow:0 30px 60px rgba(0,0,0,.7)">'
              f'<img src="{P.I(img)}" style="position:absolute;left:{ix}px;top:{iy}px;height:{zh}px"></div>'
            + (f'<div class="lab" style="position:absolute;left:{lx - 220}px;width:440px;top:{ly + d / 2 + 22}px;text-align:center;color:#f4f1ec">{texto}</div>' if texto else ''))


def titulo(lab, l1, l2, top=330, size=170, apoyo=''):
    a = f'<div style="font-size:40px;line-height:1.28;font-weight:500;color:#d6d1c9;margin-top:34px;max-width:880px">{apoyo}</div>' if apoyo else ''
    return (f'<div style="position:absolute;left:80px;right:80px;top:{top}px"><div class="lab" style="color:{OR}">{lab}</div>'
            f'<div class="h" style="font-size:{size}px;margin-top:22px">{l1}</div><div class="h o" style="font-size:{size}px">{l2}</div>{a}</div>')


def gancho():
    b = (P.marca(70, 150) + TOP + P.heroe('p_whey.png', 540, 1640, 820)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Antes de abrir tu proteína</div>'
           '<div class="h" style="font-size:210px;margin-top:22px">¿Original</div><div class="h o" style="font-size:210px">o pirata?</div>'
           '<div style="font-size:40px;color:#d6d1c9;font-weight:500;margin-top:26px">3 cosas que revisar. Guárdala.</div></div>')
    return P.page(W, H, b, 'rgba(40,80,200,.14)')


def sello():
    b = (P.marca(70, 150) + TOP
         + titulo('Chequeo 1', 'Sello', 'intacto.', apoyo='Tapa sellada y sello de seguridad sin cortes. Si llega roto o despegado, no lo abras y escríbenos.')
         + lupa('p_whey.png', 680, 1660, 680, .30, .07, 270, 1060, texto='El sello de la tapa'))
    return P.page(W, H, b, 'rgba(40,80,200,.14)')


def etiqueta():
    b = (P.marca(70, 150) + TOP
         + titulo('Chequeo 2', 'La', 'etiqueta.', apoyo='Letras nítidas y los datos de siempre. Lote y vencimiento impresos en el envase, nunca con un papel pegado encima.')
         + lupa('p_iso100.png', 700, 1660, 640, .70, .24, 280, 1090, zoom=2.2, texto='Datos nítidos'))
    return P.page(W, H, b, 'rgba(60,110,170,.16)')


def polvo():
    b = (P.marca(70, 150) + TOP + P.heroe('p_nitro.png', 820, 1660, 640)
         + titulo('Chequeo 3', 'El', 'polvo.', apoyo='Al abrir: olor y color normales, suelto y sin bloques duros. Si algo se ve raro, escríbenos antes de usarlo.'))
    return P.page(W, H, b, 'rgba(200,30,30,.10)')


def cierre():
    row = (P.heroe('p_iso100.png', 300, 1640, 320) + P.heroe('p_whey.png', 540, 1650, 350) + P.heroe('p_nitro.png', 780, 1640, 320))
    b = (P.marca(70, 150) + TOP + row
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">En Spartans</div>'
           '<div class="h" style="font-size:180px;margin-top:22px">Original.</div><div class="h o" style="font-size:180px">Sellado.</div>'
           '<div style="font-size:38px;line-height:1.28;color:#d6d1c9;font-weight:500;margin:28px auto 0;max-width:820px">Revísalo al recibirlo: una vez abierto no hay devoluciones.</div></div>'
         + '<div style="position:absolute;left:0;right:0;top:1250px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div>')
    # espacio libre ~300 px (y 900–1220) para el sticker de encuesta
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render([('1_original_o_pirata', gancho()), ('2_chequeo_sello', sello()), ('3_chequeo_etiqueta', etiqueta()),
              ('4_chequeo_polvo', polvo()), ('5_encuesta_revisas_el_sello', cierre())], OUT, W, H)
