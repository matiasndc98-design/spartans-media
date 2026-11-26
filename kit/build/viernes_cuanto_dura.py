"""Viernes 27 nov 2026 · cierre semana de la energía + panorámico semanal · estilo SOBRIO.
Carrusel 4:5 panorámico "De 30 a 200 días." con idea nueva ESCALERA DE DATOS (data-as-design):
la línea naranja del piso sube un escalón en cada lámina y el número crece en proporción a los días
que dura cada envase (a una porción al día, porciones del catálogo): Multivitamínico 30, Lipo 6 60,
Omega 3 90, Finaflex 200. Cierre con la promoción real (proteína + creatina = shaker C4 de regalo)
y el llamado a envíos "Mándaselo a quien entrena contigo. Guárdalo."
Historias 9:16 (viernes "combo / promoción real", Black Friday sin descuentos inventados):
"Sin letra chica." + encuesta "¿Qué se te acaba primero?".
Sin precios. Uso (desde kit/build): python3 viernes_cuanto_dura.py <carpeta_feed> <carpeta_historias>
"""
import sys, os
FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P
import gen
from playwright.sync_api import sync_playwright
from PIL import Image

OR = P.OR
W, H, N = 1080, 1350, 6
TW = W * N
# piso de cada lámina: sube un escalón por lámina (escalera)
PISO = [1200, 1200, 1160, 1120, 1080, 1080]
NOMBRES = ['1_de_30_a_200_dias', '2_multi_30_dias', '3_lipo_60_dias', '4_omega_90_dias',
           '5_finaflex_200_dias', '6_mandaselo']


def num(i):
    return f'<div class="foot" style="left:{i * W + W - 200}px;top:74px;width:130px;text-align:right">{i + 1:02d} / 0{N}</div>'


def marca(i):
    return P.marca(i * W + 70, 64)


def escalera():
    # tramos horizontales + subidas verticales en el borde de cada lámina
    s = ''
    for i in range(N):
        x0 = 70 if i == 0 else i * W
        x1 = (i + 1) * W if i < N - 1 else TW - 70
        s += f'<div style="position:absolute;left:{x0}px;width:{x1 - x0}px;top:{PISO[i]}px;height:2px;background:{OR}"></div>'
        if i < N - 1 and PISO[i + 1] != PISO[i]:
            y0, y1 = sorted([PISO[i], PISO[i + 1]])
            s += f'<div style="position:absolute;left:{(i + 1) * W - 1}px;width:2px;top:{y0}px;height:{y1 - y0 + 2}px;background:{OR}"></div>'
    return s


def dato(i, lab, n, size, sub, foot, foot2=''):
    f2 = (f'<div class="foot" style="left:{i * W + 70}px;bottom:{1350 - PISO[i] + 62}px;color:#b9b3aa;width:560px;'
          f'letter-spacing:3px;font-size:19px">{foot2}</div>') if foot2 else ''
    return (f'<div style="position:absolute;left:{i * W + 70}px;top:230px;width:560px"><div class="lab">{lab}</div>'
            f'<div class="h" style="font-size:{size}px;margin-top:18px">{n}</div>'
            f'<div class="h o" style="font-size:104px;margin-top:6px">{sub}</div></div>'
            f'<div class="foot" style="left:{i * W + 70}px;bottom:{1350 - PISO[i] + 24}px">{foot}</div>' + f2)


def lienzo():
    glows = ['rgba(242,106,27,.10)', 'rgba(242,106,27,.10)', 'rgba(242,106,27,.12)', 'rgba(60,110,170,.12)',
             'rgba(242,106,27,.10)', 'rgba(242,106,27,.12)']
    b = ''.join(f'<div style="position:absolute;left:{i * W}px;top:0;width:{W}px;height:{H}px;'
                f'background:radial-gradient(ellipse 60% 45% at 70% 55%,{g},transparent 70%)"></div>'
                for i, g in enumerate(glows))
    b += escalera()
    # 1 portada: el multivitamínico asoma desde el borde derecho
    b += (marca(0) + num(0)
          + '<div style="position:absolute;left:70px;top:250px"><div class="lab">Lo que dura cada envase</div>'
            '<div class="h" style="font-size:250px;margin-top:44px">De 30</div>'
            '<div class="h o" style="font-size:250px">a 200 días.</div></div>'
          + f'<div class="foot" style="left:70px;bottom:{1350 - PISO[0] + 24}px">A una porción al día · Desliza</div>')
    # 2 Multivitamínico USN (centrado en el borde para asomar en la portada)
    b += marca(1) + num(1) + P.heroe('p_multi.png', W + 90, PISO[1], 600)
    b += (f'<div style="position:absolute;left:{W + 440}px;top:230px;width:600px"><div class="lab">Multivitamínico USN</div>'
          f'<div class="h" style="font-size:230px;margin-top:18px">30</div><div class="h o" style="font-size:104px;margin-top:6px">días.</div></div>'
          f'<div class="foot" style="left:{W + 440}px;bottom:{1350 - PISO[1] + 24}px">60 tabletas · 2 al día</div>')
    # 3 Lipo 6 Black
    b += marca(2) + num(2) + P.heroe('p_lipo.png', 2 * W + 800, PISO[2], 640)
    b += dato(2, 'Lipo 6 Black · Nutrex', '60', 300, 'días.', '60 cápsulas · 1 al día',
              'Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas.')
    # 4 Omega 3 USN
    b += marca(3) + num(3) + P.heroe('p_omega.png', 3 * W + 800, PISO[3], 640)
    b += dato(3, 'Omega 3 USN · 1000 mg', '90', 370, 'días.', '90 cápsulas blandas')
    # 5 Finaflex 1 kg: el número más grande
    b += marca(4) + num(4) + P.heroe('p_finaflex.png', 4 * W + 810, PISO[4], 700)
    b += (f'<div style="position:absolute;left:{4 * W + 70}px;top:200px;width:700px"><div class="lab">Creatina Finaflex · 1 kg</div>'
          f'<div class="h" style="font-size:440px;margin-top:10px">200</div><div class="h o" style="font-size:104px;margin-top:0">días.</div></div>'
          f'<div class="foot" style="left:{4 * W + 70}px;bottom:{1350 - PISO[4] + 24}px">5 g al día · 200 porciones</div>')
    # 6 cierre: promo real + llamado a envíos
    x = 5 * W
    b += (marca(5) + num(5)
          + P.heroe('p_iso100.png', x + 300, PISO[5], 480) + P.heroe('p_finaflex.png', x + 610, PISO[5], 420)
          + P.heroe('p_shaker.png', x + 840, PISO[5], 380)
          + f'<div style="position:absolute;left:{x}px;width:{W}px;top:170px;text-align:center"><div class="lab">Proteína + creatina · Shaker de regalo</div>'
            '<div class="h" style="font-size:120px;margin-top:22px">Mándaselo a quien</div>'
            '<div class="h o" style="font-size:120px">entrena contigo.</div></div>'
          + f'<div style="position:absolute;left:{x}px;width:{W}px;bottom:90px;text-align:center;font-weight:600;font-size:26px;'
            'letter-spacing:6px;text-transform:uppercase">Guárdalo <span class="o">·</span> Pídelo por DM</div>')
    return P.page(TW, H, b, 'rgba(0,0,0,0)')


def render_panorama(html, out):
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': TW, 'height': H})
        pg.set_content(gen.sin_emoji(html), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
        full = os.path.join(out, '_full.png'); pg.screenshot(path=full); br.close()
    im = Image.open(full).convert('RGB')
    for i, n in enumerate(NOMBRES):
        im.crop((i * W, 0, (i + 1) * W, H)).save(os.path.join(out, n + '.jpg'), quality=90); print(n)
    im.resize((TW // 4, H // 4)).save(os.path.join(out, '_panorama.jpg'), quality=85)
    os.remove(full)


SW, SH = P.SW, P.SH


def h_sin_letra_chica():
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:161px">Viernes</div>'
         + '<div style="position:absolute;left:70px;top:300px"><div class="lab">Promoción real</div>'
           '<div class="h" style="font-size:210px;line-height:.9;margin-top:20px">Sin letra</div>'
           f'<div class="h" style="font-size:210px;line-height:.9;color:{OR}">chica.</div>'
           '<div style="margin-top:34px;font-weight:600;font-size:40px;letter-spacing:3px;text-transform:uppercase;color:#cfcac2">'
           'Proteína + creatina.<br>El shaker va de regalo.</div></div>'
         + P.heroe('p_iso100.png', 250, 1430, 560) + P.heroe('p_finaflex.png', 580, 1430, 470)
         + P.heroe('p_shaker.png', 860, 1430, 440)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px;color:#d8d3cb">Pídelo por DM</div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Delivery Caldera $1.500 <span class="o">·</span> Copiapó <span class="o">·</span> Todo Chile</div>')
    return P.page(SW, SH, b, 'rgba(150,80,30,.14)')


def h_encuesta():
    # espacio libre ~720–1060 para el sticker de encuesta
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Fin de mes</div>'
           '<div class="h" style="font-size:150px;margin-top:26px">¿Qué se te</div><div class="h o" style="font-size:150px">acaba primero?</div></div>'
         + P.heroe('p_whey.png', 380, 1480, 400) + P.heroe('p_usn_crea.png', 710, 1480, 320)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Te lo reponemos por DM</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.07)')


if __name__ == '__main__':
    render_panorama(lienzo(), FEED)
    P.render([('1_sin_letra_chica', h_sin_letra_chica()), ('2_que_se_te_acaba', h_encuesta())], HIST, SW, SH)
