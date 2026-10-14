"""Miércoles "Producto de la semana" (historias 9:16, sin precios ni numeración).
Idea nueva: "Lee la etiqueta conmigo" (decodificador de etiqueta con flechas a lo que dice el envase real).
Secuencia: revelación -> lee la etiqueta -> ¿es para ti? (+ alternativas y promo) -> encuesta con espacio para sticker.
Uso (desde kit/build): python3 stories_producto_semana.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from stories_esto_o_esto import page, BRAND, I, OR, W, H
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ic = gen.icon
TAG = f'''<div style="position:absolute;top:270px;left:0;right:0;text-align:center;z-index:6"><span class="big" style="display:inline-block;border:3px solid {OR};color:{OR};font-size:52px;padding:10px 26px 2px;border-radius:12px;letter-spacing:3px">PRODUCTO DE LA SEMANA</span></div>'''
CSS = f"""
.usn{{clip-path:inset(0 7.1% 4% 7.1% round 0 0 50% 50% / 0 0 5% 5%)}}
.card{{position:absolute;left:650px;right:40px;background:rgba(20,14,10,.88);border:2px solid rgba(242,106,27,.55);border-radius:22px;padding:20px 22px 18px;box-shadow:0 14px 40px rgba(0,0,0,.6)}}
.card .k{{font-weight:800;font-size:24px;letter-spacing:3px;color:#999}}
.card .t{{font-family:Bebas;font-size:66px;line-height:.9;color:{OR};margin-top:4px}}
.card .s{{font-weight:700;font-size:28px;line-height:1.1;text-transform:uppercase;color:#eee;margin-top:6px}}
.chk{{display:flex;align-items:center;gap:24px;margin-bottom:30px}}
.chk .ok{{width:80px;height:80px;border-radius:50%;background:#3ccf6e;display:grid;place-items:center;flex:none}}
.chk .ok svg{{stroke:#06240f}}
.chk .t{{font-family:Bebas;font-size:64px;line-height:.92}}
.alt{{flex:1;display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.14);border-radius:20px;padding:14px 18px}}
.alt img{{height:150px;filter:drop-shadow(0 12px 12px #000)}}
.alt .t{{font-family:Bebas;font-size:50px;line-height:.9}}
.alt .s{{font-weight:700;font-size:24px;color:#bbb;text-transform:uppercase;line-height:1.1}}
"""


def revelacion():
    body = f'''{BRAND}{TAG}
<div style="position:absolute;left:50%;top:930px;width:820px;height:820px;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,rgba(242,106,27,.45),rgba(242,106,27,.08) 55%,transparent 70%)"></div>
<div style="position:absolute;left:50%;top:930px;width:700px;height:700px;transform:translate(-50%,-50%);border-radius:50%;border:4px dashed rgba(242,106,27,.55)"></div>
<img class="usn" src="{I("p_usn_crea.png")}" style="position:absolute;left:50%;top:480px;height:880px;transform:translateX(-50%) rotate(-4deg);filter:drop-shadow(0 40px 36px #000)">
<div style="position:absolute;top:1400px;left:0;right:0;text-align:center">
 <div class="big" style="font-size:130px">CREATINA USN</div>
 <div class="big o" style="font-size:96px;text-shadow:0 0 40px rgba(242,106,27,.6)">LA IDEAL PARA EMPEZAR</div>
 <div style="font-weight:700;font-size:32px;letter-spacing:4px;color:#ccc;margin-top:18px">300 G · MONOHIDRATO · SIN SABOR</div></div>'''
    return page(body, CSS, seed=2141)


def etiqueta():
    # Producto: imagen 758x1278; recuadros sobre lo que dice el envase real y tarjetas con la traducción
    X0, Y0, PH = 110, 470, 800
    PW = PH * 758 / 1278
    bx = lambda x1, y1, x2, y2: (X0 + x1 * PW, Y0 + y1 * PH, X0 + x2 * PW, Y0 + y2 * PH)
    svg = ''
    def box(b):
        x1, y1, x2, y2 = b
        return f'<rect x="{x1:.0f}" y="{y1:.0f}" width="{x2-x1:.0f}" height="{y2-y1:.0f}" rx="10" fill="none" stroke="{OR}" stroke-width="5"/>'
    # Arriba: CREATINE MONOHYDRATE POWDER -> tarjeta a la derecha
    b = bx(.09, .58, .91, .73); svg += box(b)
    svg += f'<line x1="{b[2]:.0f}" y1="{(b[1]+b[3])/2:.0f}" x2="640" y2="{(b[1]+b[3])/2:.0f}" stroke="{OR}" stroke-width="5"/>'
    top_card = f'<div class="card" style="left:640px;top:{(b[1]+b[3])/2-120:.0f}px"><div class="k">DICE "CREATINE MONOHYDRATE"</div><div class="t">MONOHIDRATO</div><div class="s">La forma más estudiada de creatina</div></div>'
    # Abajo: 5g / 60 servings / unflavored -> tres tarjetas bajo el tarro
    lows = [((.08, .848, .33, .895), 'DICE "5G CREATINE"', '5 G POR PORCIÓN', 'La dosis diaria: 3 a 5 g'),
            ((.34, .848, .63, .895), 'DICE "60 SERVINGS"', '60 PORCIONES', 'Te dura 2 meses diarios'),
            ((.70, .848, .92, .895), 'DICE "UNFLAVORED"', 'SIN SABOR', 'Con agua, jugo o tu batido')]
    CT, CW, GAP = 1400, 316, 22
    low = ''
    for i, (r, k, t, sub) in enumerate(lows):
        b = bx(*r); svg += box(b)
        cx = 40 + i * (CW + GAP) + CW / 2
        svg += f'<line x1="{(b[0]+b[2])/2:.0f}" y1="{b[3]:.0f}" x2="{cx:.0f}" y2="{CT}" stroke="{OR}" stroke-width="5"/><circle cx="{cx:.0f}" cy="{CT}" r="9" fill="{OR}"/>'
        low += f'<div class="card sm" style="left:{40 + i * (CW + GAP)}px;width:{CW}px;top:{CT}px"><div class="k">{k}</div><div class="t">{t}</div><div class="s">{sub}</div></div>'
    body = f'''{BRAND}<div style="position:absolute;top:262px;left:0;right:0;text-align:center"><div class="big" style="font-size:112px">LEE LA ETIQUETA</div><div class="big o" style="font-size:112px;margin-top:-6px">CONMIGO</div></div>
<img class="usn" src="{I("p_usn_crea.png")}" style="position:absolute;left:{X0}px;top:{Y0}px;height:{PH}px;filter:drop-shadow(0 30px 30px #000)">
<svg width="{W}" height="{H}" style="position:absolute;inset:0;filter:drop-shadow(0 0 8px rgba(242,106,27,.8))">{svg}</svg>
{top_card}{low}'''
    css = CSS + '.card.sm{right:auto;padding:16px 16px 14px}.card.sm .k{font-size:19px;letter-spacing:2px}.card.sm .t{font-size:50px}.card.sm .s{font-size:24px}'
    return page(body, css, seed=2142)


def para_ti():
    items = ['VAS A PROBAR CREATINA POR PRIMERA VEZ', 'QUIERES UN TARRO QUE TE DURE 2 MESES', 'LA QUIERES MEZCLAR CON LO QUE YA TOMAS']
    ih = ''.join(f'<div class="chk"><div class="ok">{ic("check", 52)}</div><div class="t">{t}</div></div>' for t in items)
    body = f'''{BRAND}<div style="position:absolute;top:270px;left:0;right:0;text-align:center"><div class="big" style="font-size:150px">¿ES PARA TI?</div>
<div style="font-weight:800;font-size:34px;letter-spacing:5px;color:#bbb;margin-top:8px">LA USN 300 G ES TU CREATINA SI...</div></div>
<div style="position:absolute;top:560px;left:70px;right:70px">{ih}</div>
<div style="position:absolute;top:1000px;left:70px;right:70px"><div style="font-weight:800;font-size:32px;letter-spacing:5px;color:{OR};margin-bottom:20px">¿QUIERES QUE TE DURE MÁS?</div>
<div style="display:flex;gap:20px">
 <div class="alt"><img src="{I("p_mt_sin.png")}"><div><div class="t">MUSCLETECH<br>400 G</div><div class="s">80 días</div></div></div>
 <div class="alt"><img src="{I("p_finaflex.png")}"><div><div class="t">FINAFLEX<br>1 KG</div><div class="s">200 días</div></div></div></div>
<div style="font-weight:600;font-size:24px;color:#999;text-transform:uppercase;margin-top:14px">Tomando 5 g al día. Las tres son creatina monohidrato.</div></div>
<div style="position:absolute;top:1430px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:26px">
 <img src="{I("p_shaker.png")}" style="height:210px;filter:drop-shadow(0 20px 20px #000)">
 <div><div class="big" style="font-size:66px">PROTEÍNA + CREATINA</div><div class="big o" style="font-size:66px">SHAKER DE REGALO</div></div></div>'''
    return page(body, CSS, seed=2143)


def encuesta():
    body = f'''{BRAND}<div style="position:absolute;top:290px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:36px;letter-spacing:5px;color:#bbb">CUÉNTANOS</div>
<div class="big" style="font-size:160px;margin-top:10px">¿YA TOMAS</div><div class="big o" style="font-size:160px;text-shadow:0 0 50px rgba(242,106,27,.6)">CREATINA?</div></div>
<div class="sticker" style="top:760px"></div>
<div style="position:absolute;top:1100px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:30px">
 <img class="usn" src="{I("p_usn_crea.png")}" style="height:380px;transform:rotate(-6deg);filter:drop-shadow(0 26px 24px #000)">
 <div style="text-align:left"><div style="font-weight:700;font-size:34px;line-height:1.15;color:#ddd;text-transform:uppercase">¿Primera vez?<br>Te explicamos<br>cómo tomarla</div>
 <div style="display:flex;align-items:center;gap:12px;margin-top:22px;background:{OR};color:#0b0705;border-radius:14px;padding:12px 22px 4px"><span style="margin-bottom:8px">{ic("message-circle", 50).replace("currentColor", "#0b0705")}</span><span class="big" style="font-size:58px">PÍDELA POR DM</span></div></div></div>'''
    return page(body, CSS, seed=2144)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [('1_producto_semana', revelacion()), ('2_lee_la_etiqueta', etiqueta()), ('3_es_para_ti', para_ti()), ('4_encuesta', encuesta())]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, h in pages:
            pg = b.new_page(viewport={'width': W, 'height': H})
            pg.set_content(gen.sin_emoji(h), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, n + '.png')); pg.close(); print(n)
        b.close()
