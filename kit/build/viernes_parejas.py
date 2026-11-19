"""Viernes 20 nov 2026 · cierre semana de la proteína · estilo SOBRIO · carrusel panorámico semanal.
Carrusel 4:5 "Un scoop. + 5 g." con idea nueva PAREJAS EN UN LIENZO CONTINUO: la línea naranja del piso corre
por las 6 láminas y entre cada proteína y su creatina se levanta un "+" naranja; el Whey USN queda partido entre la
portada y la lámina 2 (invita a deslizar). Combo real: proteína + creatina = shaker C4 de regalo.
Historias 9:16: "El shaker va incluido." + encuesta "¿Ya tienes shaker?".
Sin precios. Uso (desde kit/build): python3 viernes_parejas.py <carpeta_feed> <carpeta_historias>
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
FLOOR = 1170
OR = P.OR


def num(i):
    return f'<div class="foot" style="left:{i * W + W - 200}px;top:74px;width:130px;text-align:right">{i + 1:02d} / 0{N}</div>'


def mas(x, size=150):
    # "+" naranja que nace de la línea del piso
    return (f'<div style="position:absolute;left:{x - size // 2}px;top:{FLOOR - 300 - size // 2}px;width:{size}px;height:{size}px">'
            f'<div style="position:absolute;left:{size // 2 - 3}px;top:0;width:6px;height:{size}px;background:{OR}"></div>'
            f'<div style="position:absolute;top:{size // 2 - 3}px;left:0;height:6px;width:{size}px;background:{OR}"></div></div>'
            f'<div style="position:absolute;left:{x - 1}px;top:{FLOOR - 300 + size // 2}px;width:2px;height:{300 - size // 2}px;'
            f'background:linear-gradient(180deg,transparent,{OR})"></div>')


def titulo(i, lab, t1, t2, dato, left=70, top=200):
    return (f'<div style="position:absolute;left:{i * W + left}px;top:{top}px;width:{W - 140}px"><div class="lab">{lab}</div>'
            f'<div class="h" style="font-size:170px;margin-top:18px">{t1}</div>'
            + (f'<div class="h o" style="font-size:170px">{t2}</div>' if t2 else '') + '</div>'
            f'<div class="foot" style="left:{i * W + 70}px;bottom:70px">{dato}</div>')


def lienzo():
    focos = ''.join(f'<div style="position:absolute;left:{i * W}px;top:0;width:{W}px;height:{H}px;'
                    f'background:radial-gradient(ellipse 60% 45% at 55% 62%,{g},transparent 70%)"></div>'
                    for i, g in enumerate(['rgba(242,106,27,.08)', 'rgba(150,80,30,.14)', 'rgba(60,110,170,.13)',
                                           'rgba(160,140,90,.12)', 'rgba(242,106,27,.12)', 'rgba(242,106,27,.08)']))
    linea = (f'<div style="position:absolute;left:70px;width:{TW - 140}px;top:{FLOOR + 2}px;height:2px;'
             f'background:linear-gradient(90deg,{OR},{OR} 94%,transparent)"></div>')
    b = focos + linea
    # 1 portada: el Whey USN asoma por el borde derecho (centrado en el corte 1|2)
    b += (P.marca(70, 64) + num(0)
          + '<div style="position:absolute;left:70px;top:250px"><div class="lab">Proteína + creatina</div>'
            '<div class="h" style="font-size:230px;margin-top:44px">Un scoop.</div>'
            '<div class="h o" style="font-size:230px">+ 5 g.</div></div>'
          + '<div style="position:absolute;left:70px;top:820px;width:760px;font-size:38px;color:#c9c4bc;font-weight:500">'
            'Así se arma el combo. El shaker va de regalo.</div>'
          + '<div class="foot" style="left:70px;bottom:70px">Guárdalo · Desliza</div>')
    # 2 Whey USN + Creatina USN (el whey cruza el corte)
    x = W
    b += (P.marca(x + 70, 64) + num(1) + P.heroe('p_whey.png', x + 130, FLOOR, 640)
          + mas(x + 500) + P.heroe('p_usn_crea.png', x + 800, FLOOR, 470)
          + f'<div style="position:absolute;left:{x + 430}px;top:200px;width:600px;text-align:right"><div class="lab">Whey USN + Creatina USN</div>'
            '<div class="h" style="font-size:170px;margin-top:18px">El</div><div class="h o" style="font-size:170px">clásico.</div></div>'
          + f'<div class="foot" style="left:{x + 430}px;width:580px;text-align:right;bottom:70px">22 g de proteína + 5 g de creatina</div>')
    # 3 ISO 100 + Finaflex
    x = 2 * W
    b += (P.marca(x + 70, 64) + num(2) + P.heroe('p_iso100.png', x + 290, FLOOR, 600)
          + mas(x + 590) + P.heroe('p_finaflex.png', x + 840, FLOOR, 520)
          + titulo(2, 'ISO 100 + Finaflex 1 kg', 'El que', 'dura.', '71 porciones + 200 porciones', top=170))
    # 4 Nitro Tech (ya viene junto)
    x = 3 * W
    b += (P.marca(x + 70, 64) + num(3) + P.heroe('p_nitro.png', x + 740, FLOOR, 720)
          + f'<div style="position:absolute;left:{x + 70}px;top:300px;width:520px"><div class="lab">MuscleTech Nitro Tech · 4 lb</div>'
            '<div class="h" style="font-size:170px;margin-top:18px">Ya viene</div><div class="h o" style="font-size:170px">junto.</div></div>'
          + f'<div class="foot" style="left:{x + 70}px;bottom:70px">30 g de proteína + 3 g de creatina</div>')
    # 5 Shaker C4 de regalo
    x = 4 * W
    b += (P.marca(x + 70, 64) + num(4) + P.heroe('p_shaker.png', x + 540, FLOOR, 640)
          + f'<div style="position:absolute;left:{x}px;width:{W}px;top:170px;text-align:center"><div class="lab">Shaker C4</div>'
            '<div class="h o" style="font-size:190px;margin-top:18px">De regalo.</div></div>'
          + f'<div class="foot" style="left:{x}px;width:{W}px;text-align:center;bottom:70px">Por compra de proteína + creatina</div>')
    # 6 cierre con pregunta A o B
    x = 5 * W
    b += (P.marca(x + 70, 64) + num(5)
          + P.heroe('p_whey.png', x + 330, FLOOR, 500) + P.heroe('p_iso100.png', x + 750, FLOOR, 500)
          + f'<div style="position:absolute;left:{x}px;width:{W}px;top:170px;text-align:center"><div class="lab">Responde con una palabra</div>'
            '<div class="h" style="font-size:150px;margin-top:16px">¿Clásico</div><div class="h o" style="font-size:150px">o isolate?</div></div>'
          + f'<div style="position:absolute;left:{x}px;width:{W}px;bottom:70px;text-align:center;font-weight:600;font-size:26px;'
            'letter-spacing:6px;text-transform:uppercase">Pídelo por DM <span class="o">·</span> Delivery Caldera $1.500</div>')
    return P.page(TW, H, b, 'rgba(0,0,0,0)')


NOMBRES = ['1_un_scoop_mas_5g', '2_el_clasico', '3_el_que_dura', '4_ya_viene_junto', '5_shaker_de_regalo', '6_clasico_o_isolate']


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


def h_incluido():
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:161px">Viernes</div>'
         + '<div style="position:absolute;left:70px;top:300px"><div class="lab">Proteína + creatina</div>'
           '<div class="h" style="font-size:200px;line-height:.9;margin-top:20px">El shaker</div>'
           f'<div class="h" style="font-size:200px;line-height:.9;color:{OR}">va incluido.</div></div>'
         + P.heroe('p_usn_crea.png', 220, 1420, 400) + P.heroe('p_whey.png', 545, 1420, 600)
         + P.heroe('p_shaker.png', 870, 1420, 470)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px;color:#d8d3cb">Pídelo por DM</div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Delivery Caldera $1.500 <span class="o">·</span> Copiapó <span class="o">·</span> Todo Chile</div>')
    return P.page(SW, SH, b, 'rgba(150,80,30,.14)')


def h_encuesta():
    # espacio libre ~720–1080 para el sticker de encuesta
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Viernes</div>'
           '<div class="h" style="font-size:170px;margin-top:26px">¿Ya tienes</div><div class="h o" style="font-size:170px">shaker?</div></div>'
         + P.heroe('p_shaker.png', 540, 1580, 440)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Con tu combo va de regalo</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.07)')


if __name__ == '__main__':
    render_panorama(lienzo(), FEED)
    P.render([('1_el_shaker_va_incluido', h_incluido()), ('2_ya_tienes_shaker', h_encuesta())], HIST, SW, SH)
