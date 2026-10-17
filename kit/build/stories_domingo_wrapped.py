"""Domingo "Resumen y llamado al DM": SPARTANS WRAPPED, la semana de la creatina en números (estilo resumen anual
de apps de música: números gigantes en tarjetas), elige tu creatina por cuántos días te dura + llamado al DM,
y adelanto de la semana de la proteína con caja de preguntas (~300 px libres para el sticker).
Sin precios ni numeración. Uso (desde kit/build): python3 stories_domingo_wrapped.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from stories_esto_o_esto import page, BRAND, I, OR, W, H
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ic = gen.icon
CSS = f"""
.tag{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:54px;padding:10px 26px 0;border-radius:12px;letter-spacing:3px}}
.tago{{display:inline-block;border:3px solid {OR};color:{OR};font-family:Bebas;font-size:50px;padding:10px 24px 2px;border-radius:12px;letter-spacing:3px}}
.card{{position:absolute;left:70px;right:70px;border-radius:30px;padding:26px 36px;display:flex;align-items:center;gap:30px;overflow:hidden}}
.card .n{{font-family:Bebas;font-size:190px;line-height:.82;flex:none;min-width:250px;text-align:center}}
.card .t{{font-family:Bebas;font-size:58px;line-height:.92}}
.card .s{{font-weight:700;font-size:28px;line-height:1.15;text-transform:uppercase;margin-top:6px;opacity:.85}}
.c1{{background:{OR};color:#0b0705;transform:rotate(-2deg)}}
.c2{{background:#f3ede6;color:#0b0705;transform:rotate(1.5deg)}}
.c3{{background:#1a1310;border:3px solid {OR};color:#fff;transform:rotate(-1deg)}}
.c3 .n{{color:{OR}}}
.c4{{background:#2a160b;border:3px solid rgba(255,255,255,.18);color:#fff;transform:rotate(2deg)}}
.c4 .n{{color:{OR}}}
.prod{{display:flex;align-items:center;gap:26px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.14);border-radius:24px;padding:14px 26px;margin-bottom:16px}}
.prod img{{height:150px;width:120px;object-fit:contain;flex:none;filter:drop-shadow(0 12px 12px #000)}}
.prod .nm{{font-family:Bebas;font-size:50px;line-height:.92}}
.prod .sb{{font-weight:700;font-size:25px;color:#bbb;text-transform:uppercase}}
.prod .d{{margin-left:auto;text-align:center;flex:none}}
.prod .d b{{display:block;font-family:Bebas;font-size:96px;line-height:.85;color:{OR}}}
.prod .d span{{font-weight:800;font-size:22px;letter-spacing:3px;color:#ddd}}
.bar{{height:12px;border-radius:6px;background:{OR};margin-top:10px}}
.pill{{display:inline-flex;align-items:center;gap:10px;font-weight:800;font-size:28px;letter-spacing:2px;text-transform:uppercase;border:2px solid rgba(255,255,255,.25);border-radius:40px;padding:10px 22px}}
.pill svg{{stroke:{OR}}}
.sticker{{position:absolute;left:170px;right:170px;height:300px}}
"""


def portada():
    body = f'''{BRAND}<div style="position:absolute;top:300px;left:0;right:0;text-align:center"><span class="tag">SPARTANS WRAPPED</span>
<div class="big" style="font-size:130px;margin-top:34px">TU SEMANA DE LA</div>
<div class="big o" style="font-size:210px;text-shadow:0 0 60px rgba(242,106,27,.6)">CREATINA</div>
<div class="big" style="font-size:130px">EN NÚMEROS</div>
<div style="font-weight:700;font-size:36px;line-height:1.2;color:#ddd;text-transform:uppercase;margin-top:26px">Lo que tienes que recordar,<br>en 30 segundos</div></div>
<div style="position:absolute;top:1180px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:6px">
 <img src="{I("p_usn_crea.png")}" style="height:250px;transform:rotate(-10deg);filter:drop-shadow(0 22px 22px #000)">
 <img src="{I("p_mt_sin.png")}" style="height:290px;transform:rotate(-3deg);filter:drop-shadow(0 22px 22px #000)">
 <img src="{I("p_finaflex.png")}" style="height:350px;filter:drop-shadow(0 22px 22px #000)">
 <img src="{I("p_mt_uva.png")}" style="height:290px;transform:rotate(6deg);filter:drop-shadow(0 22px 22px #000)"></div>
<div style="position:absolute;top:1560px;left:0;right:0;text-align:center;font-weight:800;font-size:30px;letter-spacing:5px;color:#bbb">TOCA PARA VER TU RESUMEN {ic("arrow-right", 34)}</div>'''
    return page(body, CSS, seed=2201)


def numeros():
    cards = [('c1', 420, '5 G', 'AL DÍA ES TODO', 'Con 3 a 5 g diarios basta. Más no rinde más.'),
             ('c2', 700, '0', 'DÍAS DE DESCANSO', 'Se toma todos los días, también los que no entrenas.'),
             ('c3', 980, '3–4', 'SEMANAS', 'Para llenar tus reservas sin fase de carga. Constancia.'),
             ('c4', 1260, '24 H', 'CUALQUIER HORA', 'Antes o después de entrenar: lo que importa es no saltártela.')]
    c = ''.join(f'<div class="card {k}" style="top:{t}px"><div class="n">{n}</div><div><div class="t">{tt}</div><div class="s">{s}</div></div></div>'
                for k, t, n, tt, s in cards)
    body = f'''{BRAND}<div style="position:absolute;top:255px;left:0;right:0;text-align:center"><div class="big" style="font-size:96px">TUS <span class="o">NÚMEROS</span> CLAVE</div></div>
{c}
<div style="position:absolute;top:1560px;left:80px;right:80px;text-align:center;font-weight:700;font-size:25px;line-height:1.25;color:#999;text-transform:uppercase">
Retiene agua dentro del músculo, no bajo la piel. Fuente: ISSN.<br>Si tienes una enfermedad o tomas medicamentos, consulta a tu médico.</div>'''
    return page(body, CSS, seed=2202)


def elige():
    P = [('p_usn_crea.png', 'USN 300 G', 'Sin sabor · ideal para empezar', 60),
         ('p_mt_uva.png', 'MUSCLETECH 392 G', 'Sabor uva · micronizada', 60),
         ('p_mt_sin.png', 'MUSCLETECH 400 G', 'Sin sabor · micronizada', 80),
         ('p_finaflex.png', 'FINAFLEX 1 KG', 'Sin sabor · micronizada · NSF', 200)]
    rows = ''.join(f'<div class="prod"><img src="{I(f)}"><div style="flex:1"><div class="nm">{n}</div><div class="sb">{s}</div><div class="bar" style="width:{int(d / 200 * 100)}%"></div></div>'
                   f'<div class="d"><b>{d}</b><span>DÍAS</span></div></div>' for f, n, s, d in P)
    body = f'''{BRAND}<div style="position:absolute;top:260px;left:0;right:0;text-align:center"><div class="big" style="font-size:104px">¿TE QUEDASTE SIN?</div>
<div class="big o" style="font-size:104px">ELIGE POR CUÁNTO TE DURA</div>
<div style="font-weight:700;font-size:28px;color:#bbb;letter-spacing:3px;margin-top:10px">TOMANDO 5 G AL DÍA</div></div>
<div style="position:absolute;top:560px;left:70px;right:70px">{rows}</div>
<div style="position:absolute;top:1340px;left:0;right:0;text-align:center"><span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:52px;padding:12px 28px 2px;border-radius:14px;box-shadow:0 0 40px rgba(242,106,27,.55)">CON PROTEÍNA: SHAKER DE REGALO</span>
<div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin:24px 60px 0">
<span class="pill">{ic("message-circle", 32)} Pídela por DM</span><span class="pill">{ic("truck-delivery", 32)} Caldera $1.500</span><span class="pill">{ic("map-pin", 32)} Copiapó y todo Chile</span></div></div>'''
    return page(body, CSS, seed=2203)


def se_viene():
    body = f'''{BRAND}<div style="position:absolute;top:265px;left:0;right:0;text-align:center"><span class="tago">DESDE MAÑANA</span>
<div class="big" style="font-size:120px;margin-top:22px">SEMANA DE LA</div>
<div class="big o" style="font-size:190px;text-shadow:0 0 60px rgba(242,106,27,.6)">PROTEÍNA</div></div>
<div style="position:absolute;top:740px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:4px">
 <img src="{I("p_barra.png")}" style="height:78px;margin-right:-30px;margin-bottom:20px;transform:rotate(-12deg);filter:drop-shadow(0 18px 18px #000)">
 <img src="{I("p_whey.png")}" style="height:250px;filter:drop-shadow(0 18px 18px #000)">
 <img src="{I("p_iso100.png")}" style="height:270px;filter:drop-shadow(0 18px 18px #000)">
 <img src="{I("p_nitro.png")}" style="height:250px;filter:drop-shadow(0 18px 18px #000)"></div>
<div style="position:absolute;top:1060px;left:0;right:0;text-align:center"><div class="big" style="font-size:78px">¿QUÉ QUIERES SABER?</div>
<div style="font-weight:700;font-size:28px;color:#bbb;letter-spacing:2px;text-transform:uppercase;margin-top:6px">Las mejores dudas las respondemos esta semana</div></div>
<div class="sticker" style="top:1190px"></div>
<div style="position:absolute;top:1520px;left:0;right:0;text-align:center;font-weight:800;font-size:30px;letter-spacing:3px">¿YA SABES CUÁL QUIERES? <span class="o">ESCRÍBENOS POR DM</span></div>'''
    return page(body, CSS, seed=2204)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [('1_wrapped_portada', portada()), ('2_numeros_clave', numeros()), ('3_elige_tu_creatina', elige()), ('4_se_viene_proteina', se_viene())]
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, h in pages:
            pg = b.new_page(viewport={'width': W, 'height': H})
            pg.set_content(gen.sin_emoji(h), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            png = os.path.join(OUT, n + '.png'); pg.screenshot(path=png); pg.close()
            Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=90); os.remove(png); print(n)
        b.close()
