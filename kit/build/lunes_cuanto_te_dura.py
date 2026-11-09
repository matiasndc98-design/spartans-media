"""Lunes 9 nov 2026 · semana de la creatina (2ª vuelta) · estilo SOBRIO.
Carrusel 4:5 "¿Cuánto te dura?" con idea nueva CARRUSEL PANORÁMICO CONTINUO: un solo lienzo de 6 láminas
(6480×1350) con piso, foco y una línea naranja que corren de lámina en lámina; el primer tarro asoma por el borde
de la portada para invitar a deslizar. Un dato por envase (porciones a 5 g = días).
Historias 9:16: tema de la semana + encuesta "¿Ya tomas creatina?".
Sin precios. Uso (desde kit/build): python3 lunes_cuanto_te_dura.py <carpeta_feed> <carpeta_historias>
"""
import sys, os
FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P
import gen
from playwright.sync_api import sync_playwright
from PIL import Image

W, H, N = 1080, 1350, 6
TW = W * N
FLOOR = 1170  # línea de piso común


def num(i):
    return f'<div class="foot" style="left:{i * W + W - 200}px;top:74px;width:130px;text-align:right">{i + 1:02d} / 0{N}</div>'


def marca(i):
    return P.marca(i * W + 70, 64)


def producto(i, img, alto, dx=0):
    # producto a la derecha de su lámina, parado en el piso común
    return P.heroe(img, i * W + 760 + dx, FLOOR, alto)


def texto(i, lab, t1, t2, dato):
    return (f'<div style="position:absolute;left:{i * W + 70}px;top:300px;width:480px"><div class="lab">{lab}</div>'
            f'<div class="h" style="font-size:210px;margin-top:20px">{t1}</div>'
            f'<div class="h o" style="font-size:96px;margin-top:8px">{t2}</div></div>'
            f'<div class="foot" style="left:{i * W + 70}px;bottom:70px">{dato}</div>')


def lienzo():
    # foco de estudio por lámina sobre un fondo continuo
    focos = ''.join(f'<div style="position:absolute;left:{i * W}px;top:0;width:{W}px;height:{H}px;'
                    f'background:radial-gradient(ellipse 60% 45% at 68% 52%,{g},transparent 70%)"></div>'
                    for i, g in enumerate(['rgba(242,106,27,.10)', 'rgba(242,106,27,.10)', 'rgba(150,150,150,.10)',
                                           'rgba(130,60,170,.16)', 'rgba(60,110,170,.12)', 'rgba(242,106,27,.10)']))
    linea = f'<div style="position:absolute;left:70px;width:{TW - 140}px;top:{FLOOR + 2}px;height:2px;background:linear-gradient(90deg,{P.OR},{P.OR} 92%,transparent)"></div>'
    b = focos + linea
    # 1 portada (el tarro USN asoma desde la lámina 2: centrado en el borde)
    b += (marca(0) + num(0)
          + '<div style="position:absolute;left:70px;top:250px"><div class="lab">Semana de la creatina</div>'
            '<div class="h" style="font-size:230px;margin-top:48px">¿Cuánto</div><div class="h o" style="font-size:230px">te dura?</div></div>'
          + '<div class="foot" style="left:70px;bottom:70px">5 g al día · Desliza</div>')
    # 2 USN 300 g (centrado cerca del borde izquierdo para que asome en la portada)
    b += marca(1) + num(1) + P.heroe('p_usn_crea.png', W + 70, FLOOR, 560)
    b += (f'<div style="position:absolute;left:{W + 430}px;top:300px;width:600px"><div class="lab">Creatina USN · 300 g</div>'
          f'<div class="h" style="font-size:300px;margin-top:20px">60</div><div class="h o" style="font-size:110px;margin-top:4px">días.</div></div>'
          f'<div class="foot" style="left:{W + 430}px;bottom:70px">Sin sabor · 60 porciones</div>')
    # 3 MuscleTech Platinum sin sabor
    b += marca(2) + num(2) + producto(2, 'p_mt_sin.png', 640)
    b += texto(2, 'MuscleTech Platinum · 400 g', '80', 'días.', 'Sin sabor · Micronizada')
    # 4 MuscleTech Platinum uva
    b += marca(3) + num(3) + producto(3, 'p_mt_uva.png', 660)
    b += texto(3, 'MuscleTech Platinum · 392 g', '60', 'días.', 'Sabor uva · Grape Freeze')
    # 5 Finaflex 1 kg
    b += marca(4) + num(4) + producto(4, 'p_finaflex.png', 700)
    b += texto(4, 'Finaflex · 1 kg', '200', 'días.', 'Sin sabor · NSF Contents Certified')
    # 6 cierre
    b += (marca(5) + num(5)
          + P.heroe('p_finaflex.png', 5 * W + 330, FLOOR, 420) + P.heroe('p_whey.png', 5 * W + 580, FLOOR, 500)
          + P.heroe('p_shaker.png', 5 * W + 820, FLOOR, 400)
          + f'<div style="position:absolute;left:{5 * W}px;width:{W}px;top:180px;text-align:center"><div class="lab">Spartans</div>'
            '<div class="h" style="font-size:150px;margin-top:16px">Elige tu</div><div class="h o" style="font-size:150px">ritmo.</div></div>'
          + f'<div style="position:absolute;left:{5 * W}px;width:{W}px;bottom:70px;text-align:center;font-weight:600;font-size:26px;'
            'letter-spacing:6px;text-transform:uppercase">Pídela por DM <span class="o">·</span> Con proteína, shaker de regalo</div>')
    return P.page(TW, H, b, 'rgba(0,0,0,0)')


def render_panorama(html, out):
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': TW, 'height': H})
        pg.set_content(gen.sin_emoji(html), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
        full = os.path.join(out, '_full.png'); pg.screenshot(path=full); br.close()
    im = Image.open(full).convert('RGB')
    nombres = ['1_cuanto_te_dura', '2_usn_60_dias', '3_platinum_80_dias', '4_uva_60_dias', '5_finaflex_200_dias', '6_elige_tu_ritmo']
    for i, n in enumerate(nombres):
        im.crop((i * W, 0, (i + 1) * W, H)).save(os.path.join(out, n + '.jpg'), quality=90); print(n)
    os.remove(full)


SW, SH = P.SW, P.SH


def h_semana():
    row = (P.heroe('p_usn_crea.png', 200, 1500, 330) + P.heroe('p_mt_sin.png', 420, 1500, 380)
           + P.heroe('p_finaflex.png', 660, 1500, 430) + P.heroe('p_mt_uva.png', 890, 1500, 380))
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Esta semana</div>'
           '<div class="h o" style="font-size:240px;margin-top:26px">Creatina.</div>'
           '<div class="h" style="font-size:96px;color:#cfcac2;margin-top:14px">Cuatro formas. Una regla.</div></div>'
         + row
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:280px">5 g al día · Pídela por DM</div>')
    return P.page(SW, SH, b)


def h_encuesta():
    # espacio libre ~720–1060 para el sticker de encuesta
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Lunes</div>'
           '<div class="h" style="font-size:160px;margin-top:26px">¿Ya tomas</div><div class="h o" style="font-size:160px">creatina?</div></div>'
         + P.heroe('p_mt_sin.png', 540, 1560, 400)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Te respondemos por DM</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.07)')


if __name__ == '__main__':
    render_panorama(lienzo(), FEED)
    P.render([('1_semana_creatina', h_semana()), ('2_ya_tomas_creatina', h_encuesta())], HIST, SW, SH)
