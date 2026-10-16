"""Sábado quiz: "Examen final de la semana" con niveles tipo videojuego (Recluta -> Guerrero -> Espartano).
Cada historia revela arriba la respuesta de la anterior y deja espacio (~300 px) para el sticker de quiz.
Sin precios ni numeración de historias.
Uso (desde kit/build): python3 stories_examen_sabado.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from stories_esto_o_esto import page, BRAND, I, OR, W, H
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ic = gen.icon
GR = '#3ccf6e'
CSS = f"""
.tag{{display:inline-block;border:3px solid {OR};color:{OR};font-family:Bebas;font-size:52px;padding:10px 26px 2px;border-radius:12px;letter-spacing:3px}}
.lvl{{display:flex;align-items:center;gap:24px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.14);border-radius:22px;padding:18px 26px;margin-bottom:16px}}
.lvl .i{{width:92px;height:92px;border-radius:50%;display:grid;place-items:center;flex:none;border:4px solid {OR};background:rgba(242,106,27,.1)}}
.lvl .i svg{{stroke:{OR}}}
.lvl .n{{font-family:Bebas;font-size:70px;line-height:.9}}
.lvl .s{{font-weight:700;font-size:30px;color:#bbb;text-transform:uppercase}}
.lvl.top{{border-color:{OR};background:rgba(242,106,27,.14);box-shadow:0 0 40px rgba(242,106,27,.35)}}
.lvl.top .i{{background:#0b0705}}
.ans{{position:absolute;top:270px;left:60px;right:60px;background:rgba(60,207,110,.1);border:3px solid {GR};border-radius:24px;padding:22px 28px;display:flex;gap:22px;align-items:flex-start}}
.ans .ok{{width:70px;height:70px;border-radius:50%;background:{GR};display:grid;place-items:center;flex:none}}
.ans .ok svg{{stroke:#06240f}}
.ans .k{{font-weight:800;font-size:26px;letter-spacing:5px;color:{GR}}}
.ans .t{{font-family:Bebas;font-size:66px;line-height:.92;margin-top:4px}}
.ans .s{{font-weight:600;font-size:29px;line-height:1.15;color:#ddd;text-transform:uppercase;margin-top:6px}}
.q{{position:absolute;left:60px;right:60px;text-align:center}}
.hint{{font-weight:800;font-size:32px;letter-spacing:5px;color:#bbb}}
.sticker{{position:absolute;left:170px;right:170px;height:300px;border:3px dashed rgba(255,255,255,.0)}}
.opts{{display:flex;justify-content:center;gap:24px;margin-top:22px}}
.opts span{{font-family:Bebas;font-size:44px;padding:10px 26px 2px;border-radius:40px;border:2px solid rgba(255,255,255,.3);color:#ddd}}
"""


def ans(t, s):
    return f'<div class="ans"><div class="ok">{ic("check", 46)}</div><div><div class="k">RESPUESTA ANTERIOR</div><div class="t">{t}</div><div class="s">{s}</div></div></div>'


def niveles(destacar=False):
    L = [('HELMET', 'ESPARTANO', '3 correctas: sabes más que tu PT'),
         ('star', 'GUERRERO', '2 correctas: vas bien encaminado'),
         ('shield-check', 'RECLUTA', '0 a 1 correcta: repasa con nosotros')]
    return ''.join(f'<div class="lvl{" top" if destacar and k == 0 else ""}"><div class="i">{(f'<img src="{gen.HELMET}" style="height:58px">' if i == "HELMET" else ic(i, 54))}</div><div><div class="n">{n}</div><div class="s">{s}</div></div></div>'
                   for k, (i, n, s) in enumerate(L))


def portada():
    body = f'''{BRAND}<div style="position:absolute;top:280px;left:0;right:0;text-align:center"><span class="tag">EXAMEN FINAL</span>
<div class="big" style="font-size:150px;margin-top:30px">SEMANA DE LA</div><div class="big o" style="font-size:190px;text-shadow:0 0 50px rgba(242,106,27,.6)">CREATINA</div>
<div style="font-weight:700;font-size:38px;line-height:1.2;color:#ddd;text-transform:uppercase;margin-top:20px">3 preguntas rápidas.<br>Responde en el quiz y mira tu <span class="o">nivel</span> al final</div></div>
<div style="position:absolute;top:850px;left:110px;right:110px">{niveles(True)}</div>
<div style="position:absolute;top:1395px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:14px">
 <img src="{I("p_usn_crea.png")}" style="height:210px;transform:rotate(-8deg);filter:drop-shadow(0 22px 22px #000)">
 <img src="{I("p_finaflex.png")}" style="height:260px;filter:drop-shadow(0 22px 22px #000)">
 <img src="{I("p_mt_sin.png")}" style="height:225px;transform:rotate(8deg);filter:drop-shadow(0 22px 22px #000)"></div>'''
    return page(body, CSS, seed=1717)


def pregunta(top, label, l1, l2, opts, extra='', hint='RESPONDE EN EL QUIZ'):
    o = ''.join(f'<span>{x}</span>' for x in opts)
    return f'''{top}<div class="q" style="top:{label}px"><span class="tag">PREGUNTA</span>
<div class="big" style="font-size:120px;margin-top:22px">{l1}</div><div class="big o" style="font-size:120px;text-shadow:0 0 40px rgba(242,106,27,.5)">{l2}</div>
<div class="hint" style="margin-top:20px">{hint}</div></div>{extra}'''


def p1():
    body = BRAND + pregunta('', 330, '¿LA CREATINA ES', 'UN ESTEROIDE?', [], '''
<div class="sticker" style="top:900px"></div>''') + f'''
<div style="position:absolute;top:1290px;left:0;right:0;display:flex;justify-content:center"><img src="{I("p_mt_sin.png")}" style="height:330px;filter:drop-shadow(0 26px 24px #000)"></div>'''
    return page(body, CSS, seed=1818)


def p2():
    top = ans('NO, NO ES UN ESTEROIDE', 'Es un compuesto que tu cuerpo ya produce y que está en la carne y el pescado.')
    body = BRAND + top + pregunta('', 680, 'RETIENE AGUA...', '¿DÓNDE?', []) + f'''
<div class="sticker" style="top:1080px"></div><div style="position:absolute;top:1400px;left:0;right:0;display:flex;justify-content:center"><img src="{I("p_finaflex.png")}" style="height:260px;filter:drop-shadow(0 26px 24px #000)"></div>'''
    return page(body, CSS, seed=1919)


def p3():
    top = ans('DENTRO DEL MÚSCULO', 'Es agua intramuscular: va al músculo, no se acumula bajo la piel.')
    body = BRAND + top + pregunta('', 640, '¿HAY QUE DESCANSAR', 'DE LA CREATINA?', [], hint='DEJARLA CADA CIERTO TIEMPO ("CICLARLA")') + f'''
<div class="sticker" style="top:1080px"></div><div style="position:absolute;top:1400px;left:0;right:0;display:flex;justify-content:center"><img src="{I("p_usn_crea.png")}" style="height:250px;filter:drop-shadow(0 26px 24px #000)"></div>'''
    return page(body, CSS, seed=2020)


def final():
    top = ans('NO HACE FALTA', 'Se toma todos los días, 3 a 5 g, también en días de descanso. Segura en personas sanas a dosis recomendadas.')
    body = BRAND + top + f'''
<div style="position:absolute;top:610px;left:0;right:0;text-align:center"><div class="big" style="font-size:110px">¿CUÁNTAS <span class="o">ACERTASTE?</span></div></div>
<div style="position:absolute;top:730px;left:150px;right:150px;transform:scale(.86);transform-origin:top center">{niveles()}</div>
<div class="sticker" style="top:1080px"></div>
<div style="position:absolute;top:1400px;left:0;right:0;text-align:center"><span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:56px;padding:12px 30px 2px;border-radius:14px;box-shadow:0 0 40px rgba(242,106,27,.6)">PROTEÍNA + CREATINA: SHAKER DE REGALO</span>
<div style="font-weight:800;font-size:34px;letter-spacing:3px;margin-top:22px">¿DUDAS? ESCRÍBENOS POR DM</div>
<div style="font-weight:600;font-size:22px;color:#888;text-transform:uppercase;margin-top:16px">Fuente: ISSN. Si tienes una enfermedad o tomas medicamentos, consulta a tu médico.</div></div>'''
    return page(body, CSS, seed=2121)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [('1_examen_final', portada()), ('2_quiz_esteroide', p1()), ('3_quiz_agua', p2()), ('4_quiz_descanso', p3()), ('5_tu_nivel', final())]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, h in pages:
            pg = b.new_page(viewport={'width': W, 'height': H})
            pg.set_content(gen.sin_emoji(h), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            png = os.path.join(OUT, n + '.png'); pg.screenshot(path=png); pg.close()
            from PIL import Image
            Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=90); os.remove(png); print(n)
        b.close()
