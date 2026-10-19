"""Lunes 19 oct 2026 · semana de la proteína.
Carrusel 4:5 PANORÁMICO CONTINUO "4 mitos de la proteína": se diseña como una sola tira de 6480 x 1350 y se corta
en 6 láminas; una línea naranja recorre todo el carrusel y el tarro y el shaker quedan "partidos" entre láminas para
invitar a deslizar (tendencia de carruseles seamless). Sin precios.
Historias 9:16: portada semana de la proteína, quiz "mito o verdad", respuesta, encuesta de sabores (4 opciones).
Uso (desde kit/build): python3 lunes_mitos_proteina.py <carpeta_feed> <carpeta_historias>
Respaldo: ISSN Position Stand protein and exercise (Jäger et al. 2017): el total diario es lo principal, la
"ventana" es amplia; Antonio et al. / revisiones: sin daño renal en personas sanas con ingestas altas.
"""
import sys, os
sys.path.insert(0, '.')
import gen
from stories_esto_o_esto import page, BRAND, I, OR, W, H
from playwright.sync_api import sync_playwright
from PIL import Image

FEED, STO = sys.argv[1], sys.argv[2]
ic = gen.icon
N = 6
PW = 1080 * N

PAN_FX = f"""<canvas id="fx" width="{PW}" height="1350"></canvas><script>
const c=document.getElementById('fx').getContext('2d');let s=4711;function r(){{s=(s*16807)%2147483647;return s/2147483647}}
for(let k=0;k<{N};k++){{let cx=k*1080+(k%2?300:780);let g=c.createRadialGradient(cx,1350,40,cx,1300,820);
 g.addColorStop(0,'rgba(200,70,10,.33)');g.addColorStop(1,'rgba(0,0,0,0)');c.fillStyle=g;c.fillRect(0,0,{PW},1350)}}
for(let i=0;i<70;i++){{let x=r()*{PW},y=400+r()*950,rad=150+r()*260;let gg=c.createRadialGradient(x,y,0,x,y,rad);
 gg.addColorStop(0,'rgba(120,60,30,.10)');gg.addColorStop(1,'rgba(0,0,0,0)');c.fillStyle=gg;c.fillRect(0,0,{PW},1350)}}
for(let i=0;i<1500;i++){{let x=r()*{PW},y=r()*1350,w=r();if(r()>0.25+0.75*(y/1350))continue;
 c.fillStyle=`rgba(255,${{120+r()*90|0}},${{30+r()*40|0}},${{0.25+w*0.7}})`;c.shadowColor='rgba(255,120,30,.9)';c.shadowBlur=6+w*10;
 c.beginPath();c.arc(x,y,0.6+w*2.4,0,7);c.fill()}}
</script>"""

FCSS = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{PW}px;height:1350px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.a{{position:absolute}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}.o{{color:{OR}}}
.brand{{position:absolute;top:58px;display:flex;align-items:center;gap:14px}}
.brand img{{height:56px}}.brand div{{font-family:Bebas;font-size:42px;letter-spacing:2px;line-height:.9}}
.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:18px;letter-spacing:5px;color:#bbb}}
.tag{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:50px;padding:8px 24px 0;border-radius:10px;letter-spacing:2px;transform:rotate(-2deg)}}
.tago{{display:inline-block;border:3px solid {OR};color:{OR};font-family:Bebas;font-size:46px;padding:8px 22px 0;border-radius:10px;letter-spacing:3px}}
.q{{font-family:Bebas;font-size:96px;line-height:.92;margin-top:26px;text-transform:uppercase}}
.q i{{font-style:normal;color:{OR}}}
.stamp{{display:inline-block;margin:26px 0 14px 4px;border:6px solid #ff3b2f;color:#ff3b2f;font-family:Bebas;font-size:104px;line-height:1;
 padding:10px 30px 0;border-radius:14px;transform:rotate(-7deg);box-shadow:0 0 30px rgba(255,59,47,.35), inset 0 0 20px rgba(255,59,47,.25)}}
.stamp small{{font-size:52px;letter-spacing:1px}}
.card{{margin-top:34px;border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.9);border-radius:24px;padding:26px 32px}}
.card .k{{display:flex;align-items:center;gap:10px;font-weight:800;font-size:28px;letter-spacing:5px;color:{OR}}}
.card .t{{font-weight:600;font-size:37px;line-height:1.15;text-transform:uppercase;margin-top:8px}}
.card .t b{{color:{OR};font-weight:800}}
.fine{{font-weight:600;font-size:22px;letter-spacing:1px;color:#8d8d8d;text-transform:uppercase;margin-top:16px}}
.line{{position:absolute;left:0;width:{PW}px;top:1262px;height:5px;background:linear-gradient(90deg,{OR},#ff9a4d 50%,{OR});box-shadow:0 0 18px rgba(242,106,27,.8)}}
.chev{{position:absolute;top:1226px;width:76px;height:76px;margin-left:-38px;border-radius:50%;background:{OR};color:#0b0705;display:grid;place-items:center;box-shadow:0 0 0 8px #060504,0 0 30px rgba(242,106,27,.8)}}
.node{{position:absolute;top:1290px;font-weight:800;font-size:22px;letter-spacing:5px;color:#bbb}}
.prod{{text-align:center}}
.prod img{{filter:drop-shadow(0 20px 20px #000)}}
.prod .n{{font-family:Bebas;font-size:40px;line-height:.95;margin-top:10px}}
.prod .g{{font-family:Bebas;font-size:66px;line-height:.9;color:{OR}}}
.prod .s{{font-weight:700;font-size:21px;color:#bbb;text-transform:uppercase;line-height:1.1}}
.pill{{display:inline-flex;align-items:center;gap:10px;font-weight:800;font-size:23px;letter-spacing:2px;text-transform:uppercase;border:2px solid rgba(255,255,255,.25);border-radius:40px;padding:10px 22px;background:rgba(6,5,4,.7)}}
.pill svg{{stroke:{OR}}}
.chips{{display:flex;gap:18px;margin-top:30px}}
.chip{{flex:1;display:flex;flex-direction:column;align-items:center;gap:10px;padding:16px 10px;border-radius:22px;background:rgba(242,106,27,.08);border:2px solid rgba(242,106,27,.35);color:{OR}}}
.chip span{{font-weight:800;font-size:26px;letter-spacing:2px;color:#fff;text-transform:uppercase;text-align:center;line-height:1.05}}
"""


def chips(items):
    return '<div class="chips">' + ''.join(f'<div class="chip">{ic(i, 54)}<span>{t}</span></div>' for i, t in items) + '</div>'


def brand(x):
    return f'<div class="brand" style="left:{x}px"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>'


def mito(k, x, w, n, quote, sello, verdad, fine='', qs=96, extra=''):
    X = 1080 * k
    f = f'<div class="fine">{fine}</div>' if fine else ''
    return (f'{brand(X + 70)}<div class="a" style="left:{X + x}px;top:190px;width:{w}px"><span class="tago">MITO {n}</span>'
            f'<div class="q" style="font-size:{qs}px">{quote}</div><div class="stamp">{sello}</div>'
            f'<div class="card"><div class="k">{ic("check", 34)} LA VERDAD</div><div class="t">{verdad}</div></div>{f}{extra}</div>')


def carrusel():
    b = '<div class="line"></div>'
    b += ''.join(f'<div class="chev" style="left:{1080 * k}px">{ic("arrow-right", 46)}</div>' for k in range(1, N))
    # 1 portada (el tarro queda partido entre la lámina 1 y la 2)
    b += f'''{brand(70)}<div class="a" style="left:70px;top:250px;width:760px"><span class="tag">SEMANA DE LA PROTEÍNA</span>
<div class="big" style="font-size:250px;margin-top:40px">4 MITOS</div>
<div class="big" style="font-size:118px">DE LA <span class="o" style="text-shadow:0 0 40px rgba(242,106,27,.6)">PROTEÍNA</span></div>
<div class="big" style="font-size:118px">QUE TE FRENAN</div>
<div style="font-weight:700;font-size:34px;line-height:1.2;color:#ddd;text-transform:uppercase;margin-top:30px">¿Cuántos te creíste?<br>Guárdalo para no olvidarlo</div></div>
<div class="a" style="left:110px;top:1140px;font-family:Bebas;font-size:50px;letter-spacing:3px">DESLIZA <span class="o">{ic("arrow-right", 44)}</span></div>
<div class="a" style="left:820px;top:430px;width:520px;height:800px;background:radial-gradient(closest-side,rgba(242,106,27,.55),rgba(160,50,0,.2) 55%,transparent);filter:blur(12px)"></div>
<img class="a" src="{I("p_whey.png")}" style="left:860px;top:470px;height:740px;filter:drop-shadow(0 34px 30px #000)">'''
    # 2 a 5 mitos
    b += mito(1, 330, 690, 1, '“Si no te la tomas <i>apenas terminas</i> de entrenar, se pierde”', 'FALSO',
              'Lo que más importa es <b>cuánta proteína comes en el día</b>. Tómala cuando te acomode: después de entrenar, al desayuno o de colación.',
              'Fuente: Sociedad Internacional de Nutrición Deportiva (ISSN)')
    b += mito(2, 70, 940, 2, '“La proteína en polvo es solo para los que quieren <i>ponerse enormes</i>”', 'FALSO',
              'Es <b>proteína de leche en polvo</b>: comida práctica. Te ayuda a llegar a tu meta del día, entrenes por fuerza, salud o rendimiento.', qs=100,
              extra=chips([('barbell', 'Fuerza'), ('heart', 'Salud'), ('run', 'Rendimiento'), ('users', 'Hombres y<br>mujeres')]))
    b += mito(3, 70, 940, 3, '“La proteína <i>daña los riñones</i>”', 'FALSO <small>EN PERSONAS SANAS</small>',
              'En personas sanas y a las dosis recomendadas <b>no se ha visto daño</b>. Si tienes una enfermedad renal o tomas medicamentos, <b>consulta a tu médico</b>.',
              qs=130, extra=chips([('user', 'Personas<br>sanas'), ('scale', 'Dosis<br>recomendada'), ('shield-check', 'Ante dudas,<br>tu médico')]))
    b += mito(4, 70, 800, 4, '“Un batido <i>reemplaza</i> una comida”', 'FALSO',
              'Es un <b>complemento</b>. Primero comida real: huevos, carnes, legumbres, lácteos. El scoop completa <b>lo que te falta</b> para tu meta del día.', qs=120,
              extra=chips([('egg', 'Huevos'), ('meat', 'Carnes'), ('glass-full', 'Lácteos'), ('bowl', 'Legumbres')]))
    # shaker partido entre la lámina 5 y la 6
    b += f'''<div class="a" style="left:5180px;top:560px;width:440px;height:700px;background:radial-gradient(closest-side,rgba(242,106,27,.5),transparent);filter:blur(12px)"></div>
<img class="a" src="{I("p_shaker.png")}" style="left:5265px;top:620px;height:580px;transform:rotate(8deg);filter:drop-shadow(0 30px 26px #000)">'''
    # 6 cierre
    X = 5400
    P = [('p_whey.png', 300, 'WHEY USN 5 LB', '22 G', 'Chocolate'),
         ('p_iso100.png', 320, 'ISO 100 5 LB', '25 G', 'Isolate · Cocoa Pebbles'),
         ('p_nitro.png', 300, 'NITRO TECH 4 LB', '30 G', '+ 3 g creatina · vainilla')]
    prods = ''.join(f'<div class="prod" style="width:210px"><div style="height:320px;display:flex;align-items:flex-end;justify-content:center"><img src="{I(f)}" style="height:{h}px"></div>'
                    f'<div class="n">{n}</div><div class="g">{g}</div><div class="s">{s}</div></div>' for f, h, n, g, s in P)
    b += f'''{brand(X + 300)}<div class="a" style="left:{X + 250}px;top:170px;width:780px;text-align:center">
<div class="big" style="font-size:112px">LA VERDAD</div><div class="big o" style="font-size:74px;white-space:nowrap">1 SCOOP = 22 A 30 G DE PROTEÍNA</div>
<div style="font-weight:700;font-size:26px;color:#bbb;letter-spacing:2px;margin-top:8px">POR PORCIÓN, SEGÚN CUÁL ELIJAS</div></div>
<div class="a" style="left:{X + 270}px;top:450px;width:760px;display:flex;justify-content:space-between">{prods}</div>
<div class="a" style="left:{X + 250}px;top:960px;width:780px;text-align:center">
<span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:50px;padding:12px 26px 2px;border-radius:14px;box-shadow:0 0 40px rgba(242,106,27,.55)">CON CREATINA: SHAKER DE REGALO</span>
<div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:22px">
<span class="pill">{ic("message-circle", 30)} Pídela por DM</span><span class="pill">{ic("truck-delivery", 30)} Caldera $1.500</span><span class="pill">{ic("map-pin", 30)} Todo Chile</span></div></div>
<div class="a" style="left:{X + 250}px;top:1290px;width:780px;text-align:center;font-weight:800;font-size:22px;letter-spacing:4px;color:#bbb">COMENTA <span class="o">MITO</span> Y TE ORIENTAMOS POR DM</div>'''
    return f'<html><head><style>{FCSS}</style></head><body>{PAN_FX}{b}<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script></body></html>'


# ---------------- historias ----------------
SCSS = f"""
.tag{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:54px;padding:10px 26px 0;border-radius:12px;letter-spacing:3px}}
.tago{{display:inline-block;border:3px solid {OR};color:{OR};font-family:Bebas;font-size:50px;padding:10px 24px 2px;border-radius:12px;letter-spacing:3px}}
.qcard{{position:absolute;left:80px;right:80px;background:#f3ede6;color:#0b0705;border-radius:34px;padding:44px 50px;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(0,0,0,.6)}}
.qcard .big{{font-size:92px;line-height:.95}}
.stamp{{display:inline-block;border:9px solid #ff3b2f;color:#ff3b2f;font-family:Bebas;font-size:260px;line-height:1;padding:14px 50px 0;border-radius:24px;transform:rotate(-8deg);
 box-shadow:0 0 50px rgba(255,59,47,.4), inset 0 0 30px rgba(255,59,47,.3)}}
.card{{position:absolute;left:80px;right:80px;border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.9);border-radius:28px;padding:34px 40px}}
.card .t{{font-weight:600;font-size:42px;line-height:1.15;text-transform:uppercase}}
.card .t b{{color:{OR};font-weight:800}}
.tile{{position:absolute;width:440px;height:370px;border-radius:30px;overflow:hidden;border:2px solid rgba(255,255,255,.14);text-align:center}}
.tile img{{position:absolute;left:50%;transform:translateX(-50%);filter:drop-shadow(0 18px 18px #000)}}
.tile .f{{position:absolute;left:0;right:0;bottom:22px;font-family:Bebas;font-size:64px;line-height:.9}}
.tile .p{{position:absolute;left:0;right:0;bottom:0;transform:translateY(0);font-weight:700;font-size:20px;color:#ddd;letter-spacing:2px;text-transform:uppercase;display:none}}
.sticker{{position:absolute;left:170px;right:170px;height:300px}}
"""


def s_portada():
    body = f'''{BRAND}<div style="position:absolute;top:300px;left:0;right:0;text-align:center"><span class="tag">ARRANCA HOY</span>
<div class="big" style="font-size:140px;margin-top:30px">SEMANA DE LA</div>
<div class="big o" style="font-size:230px;text-shadow:0 0 60px rgba(242,106,27,.6)">PROTEÍNA</div></div>
<div style="position:absolute;top:720px;left:0;right:0;height:560px;background:radial-gradient(closest-side,rgba(242,106,27,.45),transparent);filter:blur(10px)"></div>
<div style="position:absolute;top:760px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:0">
 <img src="{I("p_whey.png")}" style="height:420px;transform:rotate(-6deg);margin-right:-20px;filter:drop-shadow(0 22px 22px #000)">
 <img src="{I("p_iso100.png")}" style="height:480px;position:relative;z-index:2;filter:drop-shadow(0 22px 22px #000)">
 <img src="{I("p_nitro.png")}" style="height:420px;transform:rotate(6deg);margin-left:-20px;filter:drop-shadow(0 22px 22px #000)"></div>
<img src="{I("p_barra.png")}" style="position:absolute;left:300px;top:1150px;width:480px;transform:rotate(-6deg);z-index:3;filter:drop-shadow(0 18px 18px #000)">
<div style="position:absolute;top:1340px;left:90px;right:90px;text-align:center;font-weight:700;font-size:36px;line-height:1.3;text-transform:uppercase;color:#eee">
Mitos que te frenan, cuál elegir según tu objetivo<br>y <span class="o">tus preguntas respondidas</span></div>
<div style="position:absolute;top:1560px;left:0;right:0;text-align:center;font-weight:800;font-size:30px;letter-spacing:5px;color:#bbb">PARTIMOS CON UN DESAFÍO {ic("arrow-right", 34)}</div>'''
    return page(body, SCSS, seed=1901)


def s_quiz():
    body = f'''{BRAND}<div style="position:absolute;top:290px;left:0;right:0;text-align:center"><span class="tago">MITO O VERDAD</span>
<div class="big" style="font-size:118px;margin-top:22px">¿QUÉ DICES TÚ?</div></div>
<div class="qcard" style="top:580px"><div style="font-weight:800;font-size:28px;letter-spacing:5px;color:{OR}">PROTEÍNA</div>
<div class="big" style="margin-top:12px">“Si no te tomas la proteína apenas terminas de entrenar, se pierde”</div></div>
<div class="sticker" style="top:1150px"></div>
<img src="{I("p_shaker.png")}" style="position:absolute;right:40px;top:1080px;height:330px;transform:rotate(12deg);opacity:.9;filter:drop-shadow(0 18px 18px #000)">
<div style="position:absolute;top:1500px;left:0;right:0;text-align:center;font-weight:800;font-size:32px;letter-spacing:4px">RESPONDE Y MIRA LA SIGUIENTE</div>'''
    return page(body, SCSS, seed=1902)


def s_respuesta():
    body = f'''{BRAND}<div style="position:absolute;top:300px;left:0;right:0;text-align:center"><div class="big" style="font-size:90px">LA RESPUESTA ES…</div>
<div style="margin-top:40px"><span class="stamp">MITO</span></div></div>
<div class="card" style="top:840px"><div class="t">Lo que más importa es <b>cuánta proteína comes en el día</b>.
Tómala cuando te acomode: después de entrenar, al desayuno o de colación.</div>
<div style="font-weight:600;font-size:24px;color:#8d8d8d;margin-top:16px;letter-spacing:1px">FUENTE: SOCIEDAD INTERNACIONAL DE NUTRICIÓN DEPORTIVA (ISSN)</div></div>
<div style="position:absolute;top:1270px;left:0;right:0;text-align:center"><div class="big" style="font-size:96px">HAY <span class="o">3 MITOS MÁS</span></div>
<div style="font-weight:800;font-size:34px;letter-spacing:3px;margin-top:10px;text-transform:uppercase">En el carrusel de hoy en nuestro feed</div>
<div style="font-weight:800;font-size:30px;letter-spacing:4px;color:#bbb;margin-top:30px">TOCA EL PERFIL {ic("arrow-right", 32)}</div></div>'''
    return page(body, SCSS, seed=1903)


def s_sabores():
    T = [('p_whey.png', 'CHOCOLATE', 'Whey USN', '#3a2216', 225, 24),
         ('p_iso100.png', 'COCOA PEBBLES', 'ISO 100', '#3b1a2e', 235, 18),
         ('p_nitro.png', 'VAINILLA', 'Nitro Tech', '#3a3020', 225, 24),
         ('p_barra.png', 'COCO', 'Barra Space Protein', '#173339', 0, 0)]
    tiles = ''
    for k, (f, fl, nm, bg, h, top) in enumerate(T):
        x, y = (80 if k % 2 == 0 else 560), (490 if k < 2 else 885)
        img = (f'<img src="{I(f)}" style="top:{top}px;height:{h}px">' if h else
               f'<img src="{I(f)}" style="top:95px;width:360px;transform:translateX(-50%) rotate(-8deg)">')
        tiles += (f'<div class="tile" style="left:{x}px;top:{y}px;background:radial-gradient(circle at 50% 40%,{bg},#0c0908 75%)">{img}'
                  f'<div class="f">{fl}<div style="font-family:Barlow;font-weight:700;font-size:21px;letter-spacing:3px;color:#ccc;margin-top:4px">{nm.upper()}</div></div></div>')
    body = f'''{BRAND}<div style="position:absolute;top:270px;left:0;right:0;text-align:center"><div class="big" style="font-size:120px">¿QUÉ SABOR</div>
<div class="big o" style="font-size:120px">TE TIENTA MÁS?</div></div>
{tiles}<div class="sticker" style="top:1285px"></div>
<div style="position:absolute;top:1600px;left:0;right:0;text-align:center;font-weight:800;font-size:30px;letter-spacing:3px">¿YA LO QUIERES? <span class="o">PÍDELO POR DM</span></div>'''
    return page(body, SCSS, seed=1904)


if __name__ == '__main__':
    os.makedirs(FEED, exist_ok=True); os.makedirs(STO, exist_ok=True)
    names = ['1_portada', '2_mito_hora', '3_mito_enormes', '4_mito_rinones', '5_mito_reemplazo', '6_la_verdad']
    stories = [('1_semana_proteina', s_portada()), ('2_quiz_mito_o_verdad', s_quiz()), ('3_respuesta_mito', s_respuesta()), ('4_encuesta_sabores', s_sabores())]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': PW, 'height': 1350})
        pg.set_content(gen.sin_emoji(carrusel()), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(400)
        tmp = os.path.join(FEED, '_pan.png'); pg.screenshot(path=tmp); pg.close()
        pan = Image.open(tmp).convert('RGB')
        for k, n in enumerate(names):
            pan.crop((1080 * k, 0, 1080 * (k + 1), 1350)).save(os.path.join(FEED, n + '.jpg'), quality=90); print(n)
        pan.resize((PW // 4, 1350 // 4)).save(os.path.join(FEED, '_vista_panoramica.jpg'), quality=85); os.remove(tmp)
        for n, h in stories:
            pg = b.new_page(viewport={'width': W, 'height': H})
            pg.set_content(gen.sin_emoji(h), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            png = os.path.join(STO, n + '.png'); pg.screenshot(path=png); pg.close()
            Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=90); os.remove(png); print(n)
        b.close()
