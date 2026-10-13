"""Serie semanal "Pregunta espartana" (martes, pregunta frecuente). Historias 9:16 sin precios ni numeración.
Secuencia: quiz con barra de búsqueda -> respuesta -> con qué mezclarla (promo shaker) -> caja de preguntas para la próxima semana.
Uso (desde kit/build): python3 stories_pregunta_martes.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from stories_esto_o_esto import page, BRAND, I, OR, W, H
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ic = gen.icon
LUPA = '<svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#777" stroke-width="2.4" stroke-linecap="round"><circle cx="10" cy="10" r="7"/><path d="M15 15l6 6"/></svg>'
TAG = f'''<div style="position:absolute;top:270px;left:0;right:0;text-align:center"><span class="big" style="display:inline-block;border:3px solid {OR};color:{OR};font-size:52px;padding:10px 26px 2px;border-radius:12px;letter-spacing:3px">PREGUNTA ESPARTANA</span></div>'''
CSS = f"""
.bar{{position:absolute;left:70px;right:70px;height:130px;background:#fff;border-radius:65px;display:flex;align-items:center;gap:22px;padding:0 40px;box-shadow:0 20px 60px rgba(0,0,0,.7),0 0 0 6px rgba(242,106,27,.35)}}
.bar span{{font-family:Barlow;font-weight:600;font-size:44px;color:#222;white-space:nowrap}}
.cur{{display:inline-block;width:4px;height:52px;background:{OR};margin-left:4px;vertical-align:middle;animation:none}}
.chip{{display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 26px;font-family:Bebas;font-size:62px;line-height:.9}}
.chip .ok{{width:62px;height:62px;border-radius:50%;background:#3ccf6e;display:grid;place-items:center;flex:none}}
.chip .ok svg{{stroke:#06240f}}
.rule{{display:flex;align-items:center;gap:26px;margin-bottom:30px}}
.rule .i{{width:96px;height:96px;border-radius:24px;background:{OR};display:grid;place-items:center;flex:none}}
.rule .i svg{{stroke:#0b0705}}
.rule .t{{font-family:Bebas;font-size:66px;line-height:.9}}
.rule .s{{font-weight:600;font-size:32px;color:#ccc;text-transform:uppercase;line-height:1.1;margin-top:4px}}
.sticker{{position:absolute;left:190px;right:190px;height:300px}}
"""


def quiz():
    body = f'''{BRAND}{TAG}
<div class="bar" style="top:420px">{LUPA}<span>¿a qué hora se toma la creatina<i class="cur"></i></span></div>
<div style="position:absolute;top:620px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:36px;letter-spacing:5px;color:#bbb">LA DUDA DE SIEMPRE</div>
<div class="big" style="font-size:150px;margin-top:14px">¿CUÁNDO SE</div><div class="big o" style="font-size:150px">TOMA?</div></div>
<div style="position:absolute;top:1000px;left:0;right:0;display:flex;justify-content:center;gap:10px">
 <img src="{I("p_usn_crea.png")}" style="height:300px;transform:rotate(-8deg);filter:drop-shadow(0 26px 24px #000)">
 <img src="{I("p_mt_sin.png")}" style="height:330px;transform:rotate(6deg);filter:drop-shadow(0 26px 24px #000)"></div>
<div class="sticker" style="top:1360px"></div>'''
    return page(body, CSS, seed=1313)


def respuesta():
    chips = ''.join(f'<div class="chip"><div class="ok">{ic("check", 44)}</div>{t}</div>' for t in ['EN LA MAÑANA', 'ANTES DE ENTRENAR', 'DESPUÉS DE ENTRENAR', 'EN LA NOCHE'])
    rules = [('calendar', 'TODOS LOS DÍAS', 'También en los días de descanso'),
             ('scale', '3 A 5 G AL DÍA', 'Más no sirve más'),
             ('clock', 'JUNTO A UN HÁBITO', 'Con el desayuno o tu batido: así no se te olvida')]
    rh = ''.join(f'<div class="rule"><div class="i">{ic(i, 58)}</div><div><div class="t">{t}</div><div class="s">{s}</div></div></div>' for i, t, s in rules)
    body = f'''{BRAND}<div style="position:absolute;top:270px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:40px;letter-spacing:6px;color:#3ccf6e">RESPUESTA</div>
<div class="big o" style="font-size:180px;margin-top:10px;text-shadow:0 0 50px rgba(242,106,27,.6)">A CUALQUIER</div><div class="big" style="font-size:180px">HORA</div></div>
<div style="position:absolute;top:720px;left:70px;right:70px;display:grid;grid-template-columns:1fr 1fr;gap:18px">{chips}</div>
<div style="position:absolute;top:1010px;left:70px;right:70px"><div style="font-weight:800;font-size:34px;letter-spacing:5px;color:{OR};margin-bottom:26px">LO QUE SÍ IMPORTA</div>{rh}</div>
<div style="position:absolute;top:1590px;left:70px;right:70px;font-weight:600;font-size:26px;color:#999;text-transform:uppercase">Fuente: Sociedad Internacional de Nutrición Deportiva (ISSN). Si tienes una enfermedad o tomas medicamentos, consulta a tu médico.</div>'''
    css = CSS + '.chip{font-size:46px;padding:16px 20px;gap:14px}.chip .ok{width:52px;height:52px}'
    return page(body, css, seed=1414)


def mezcla():
    opts = [('droplet', 'AGUA'), ('glass-full', 'JUGO'), ('cup', 'TU BATIDO')]
    oh = ''.join(f'<div style="text-align:center"><div style="width:170px;height:170px;margin:0 auto;border-radius:50%;border:4px solid {OR};display:grid;place-items:center;background:rgba(242,106,27,.08)">{ic(i, 90).replace("currentColor", OR)}</div><div class="big" style="font-size:66px;margin-top:16px">{t}</div></div>' for i, t in opts)
    body = f'''{BRAND}<div style="position:absolute;top:270px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:36px;letter-spacing:5px;color:#bbb">Y LA QUE SIGUE</div>
<div class="big" style="font-size:150px;margin-top:14px">¿CON QUÉ</div><div class="big o" style="font-size:150px">LA MEZCLO?</div></div>
<div style="position:absolute;top:690px;left:60px;right:60px;display:flex;justify-content:space-around">{oh}</div>
<div style="position:absolute;top:1010px;left:70px;right:70px;text-align:center;font-weight:700;font-size:34px;line-height:1.2;text-transform:uppercase;color:#ddd">La sin sabor va con lo que quieras.<br>Juntarla con tu proteína es lo más cómodo:<br><span class="o">un solo batido</span></div>
<div style="position:absolute;top:1200px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:0">
 <img src="{I("p_whey.png")}" style="height:330px;margin-right:-30px;filter:drop-shadow(0 26px 24px #000)">
 <div class="big o" style="font-size:120px;margin:0 6px 110px;position:relative;z-index:2">+</div>
 <img src="{I("p_usn_crea.png")}" style="height:250px;margin-left:-10px;filter:drop-shadow(0 26px 24px #000)">
 <div class="big o" style="font-size:120px;margin:0 10px 110px">=</div>
 <img src="{I("p_shaker.png")}" style="height:320px;filter:drop-shadow(0 26px 24px #000)"></div>
<div style="position:absolute;top:1560px;left:0;right:0;text-align:center"><span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:62px;padding:12px 30px 2px;border-radius:14px;box-shadow:0 0 40px rgba(242,106,27,.6)">PROTEÍNA + CREATINA: SHAKER DE REGALO</span></div>'''
    return page(body, CSS, seed=1515)


def pregunta():
    body = f'''{BRAND}{TAG}
<div style="position:absolute;top:400px;left:0;right:0;text-align:center"><div class="big" style="font-size:140px">¿Y TÚ QUÉ</div><div class="big o" style="font-size:140px;text-shadow:0 0 50px rgba(242,106,27,.6)">DUDA TIENES?</div>
<div style="font-weight:700;font-size:36px;line-height:1.2;color:#ddd;text-transform:uppercase;margin-top:24px">Creatina, proteína, energía...<br>Elegimos una y la respondemos<br><span class="o">el próximo martes</span></div></div>
<div class="sticker" style="top:1000px"></div>
<div style="position:absolute;top:1370px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:20px;opacity:.95">
 <img src="{I("p_finaflex.png")}" style="height:260px;transform:rotate(-8deg);filter:drop-shadow(0 20px 20px #000)">
 <img src="{I("p_nitro.png")}" style="height:300px;filter:drop-shadow(0 20px 20px #000)">
 <img src="{I("p_whey.png")}" style="height:280px;transform:rotate(8deg);filter:drop-shadow(0 20px 20px #000)"></div>'''
    return page(body, CSS, seed=1616)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [('1_quiz_cuando', quiz()), ('2_respuesta', respuesta()), ('3_con_que_mezclo', mezcla()), ('4_tu_pregunta', pregunta())]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, h in pages:
            pg = b.new_page(viewport={'width': W, 'height': H})  # página nueva: el script de brasas usa const globales
            pg.set_content(gen.sin_emoji(h), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, n + '.png')); pg.close(); print(n)
        b.close()
