"""Jueves "Detrás de la tienda" (historias 9:16, sin precios de productos ni numeración).
Idea nueva: "Seguimiento del pedido" estilo app de delivery: una barra de progreso con 4 etapas
(escribes -> pagas -> preparamos -> te llega) que avanza en cada historia. Cierra con encuesta.
Uso (desde kit/build): python3 stories_detras_tienda.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from stories_esto_o_esto import page, BRAND, I, OR, W, H
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ic = gen.icon
STEPS = [('message-circle', 'ESCRIBES'), ('credit-card', 'PAGAS'), ('package', 'PREPARAMOS'), ('truck-delivery', 'TE LLEGA')]
CSS = f"""
.trk{{position:absolute;left:60px;right:60px;background:rgba(20,14,10,.9);border:2px solid rgba(242,106,27,.45);border-radius:26px;padding:24px 30px 20px;box-shadow:0 14px 40px rgba(0,0,0,.6);z-index:5}}
.trk .hd{{display:flex;justify-content:space-between;font-weight:800;font-size:24px;letter-spacing:3px;color:#999;margin-bottom:18px}}
.trk .hd b{{color:{OR}}}
.line{{position:relative;display:flex;justify-content:space-between}}
.line .rail{{position:absolute;left:50px;right:50px;top:38px;height:8px;border-radius:4px;background:#2c2420}}
.line .fill{{position:absolute;left:50px;top:38px;height:8px;border-radius:4px;background:{OR};box-shadow:0 0 18px {OR}}}
.st{{position:relative;width:100px;text-align:center}}
.st .c{{width:84px;height:84px;margin:0 auto;border-radius:50%;display:grid;place-items:center;background:#2c2420;border:4px solid #2c2420}}
.st .c svg{{stroke:#777}}
.st.done .c{{background:{OR};border-color:{OR}}}.st.done .c svg{{stroke:#0b0705}}
.st.now .c{{background:#060504;border-color:{OR};box-shadow:0 0 0 8px rgba(242,106,27,.25),0 0 30px {OR}}}.st.now .c svg{{stroke:{OR}}}
.st .l{{font-family:Bebas;font-size:34px;margin-top:10px;color:#777;white-space:nowrap;margin-left:-30px;margin-right:-30px}}
.st.done .l,.st.now .l{{color:#fff}}
.tag{{position:absolute;top:262px;left:0;right:0;text-align:center;z-index:6}}
.tag span{{display:inline-block;border:3px solid {OR};color:{OR};font-family:Bebas;font-size:50px;padding:10px 26px 2px;border-radius:12px;letter-spacing:3px}}
.bub{{max-width:700px;font-weight:700;font-size:40px;line-height:1.15;padding:22px 30px;border-radius:34px;text-transform:none}}
.chip{{display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.16);border-radius:20px;padding:18px 22px}}
.chip svg{{stroke:{OR};flex:none}}
.chip span{{font-family:Bebas;font-size:50px;line-height:.9;padding-top:6px}}
.ok{{display:flex;align-items:center;gap:22px;margin-bottom:26px}}
.ok i{{width:74px;height:74px;border-radius:50%;background:#3ccf6e;display:grid;place-items:center;flex:none}}
.ok i svg{{stroke:#06240f}}
.ok div{{font-family:Bebas;font-size:58px;line-height:.92}}
.ok small{{display:block;font-family:Barlow;font-weight:700;font-size:26px;color:#bbb;text-transform:uppercase;letter-spacing:1px;margin-top:6px}}
.dest{{display:flex;align-items:center;gap:26px;background:rgba(20,14,10,.88);border:2px solid rgba(242,106,27,.45);border-radius:24px;padding:24px 28px;margin-bottom:24px}}
.dest .ico{{width:104px;height:104px;border-radius:22px;background:rgba(242,106,27,.14);display:grid;place-items:center;flex:none}}
.dest .ico svg{{stroke:{OR}}}
.dest .t{{font-family:Bebas;font-size:72px;line-height:.9}}
.dest .s{{font-weight:700;font-size:30px;color:#ddd;text-transform:uppercase;line-height:1.12;margin-top:4px}}
.box{{position:absolute;left:50%;transform:translateX(-50%);width:760px;height:330px;background:linear-gradient(180deg,#b07a45,#8a5a2e);border-radius:10px 10px 18px 18px;box-shadow:0 40px 60px rgba(0,0,0,.7),inset 0 -20px 40px rgba(0,0,0,.25);z-index:3}}
.box:before{{content:'';position:absolute;left:0;right:0;top:0;height:46px;background:linear-gradient(180deg,#c48b52,#a06c3a);border-radius:10px 10px 0 0}}
.box .tape{{position:absolute;left:50%;top:0;bottom:0;width:120px;transform:translateX(-50%);background:rgba(242,106,27,.85)}}
.box .lab{{position:absolute;right:40px;bottom:40px;background:#f3eee6;color:#111;border-radius:8px;padding:10px 18px 4px;font-family:Bebas;font-size:40px;letter-spacing:2px;display:flex;align-items:center;gap:10px}}
.box .lab img{{height:44px;margin-bottom:6px}}
"""


def tracker(now, top, title='TU PEDIDO'):
    n = len(STEPS)
    pct = min(now / (n - 1), 1)
    st = ''
    for i, (icn, lab) in enumerate(STEPS):
        cls = 'done' if i < now else ('now' if i == now else '')
        st += f'<div class="st {cls}"><div class="c">{ic("check" if i < now else icn, 44)}</div><div class="l">{lab}</div></div>'
    estado = 'ENTREGADO' if now >= n else STEPS[now][1]
    return f'''<div class="trk" style="top:{top}px"><div class="hd"><span>{title}</span><span>ESTADO: <b>{estado}</b></span></div>
<div class="line"><div class="rail"></div><div class="fill" style="width:calc((100% - 100px) * {pct:.3f})"></div>{st}</div></div>'''


def gancho():
    body = f'''{BRAND}<div class="tag"><span>DETRÁS DE LA TIENDA</span></div>
<div style="position:absolute;top:370px;left:0;right:0;text-align:center"><div class="big" style="font-size:150px">ASÍ VIAJA</div>
<div class="big o" style="font-size:150px;text-shadow:0 0 50px rgba(242,106,27,.6)">TU PEDIDO</div>
<div style="font-weight:700;font-size:34px;letter-spacing:4px;color:#ccc;margin-top:16px">DESDE QUE NOS ESCRIBES HASTA QUE LO TIENES</div></div>
<div style="position:absolute;left:50%;top:1290px;width:900px;height:300px;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(ellipse,rgba(242,106,27,.45),transparent 70%)"></div>
<img src="{I("p_whey.png")}" style="position:absolute;left:200px;top:760px;height:520px;transform:rotate(-8deg);filter:drop-shadow(0 30px 30px #000);z-index:2">
<img src="{I("p_usn_crea.png")}" style="position:absolute;left:520px;top:860px;height:400px;transform:rotate(6deg);clip-path:inset(0 7.1% 4% 7.1%);filter:drop-shadow(0 30px 30px #000);z-index:2">
<img src="{I("p_shaker.png")}" style="position:absolute;left:740px;top:880px;height:380px;transform:rotate(12deg);filter:drop-shadow(0 30px 30px #000);z-index:2">
<div class="box" style="top:1180px"><div class="tape"></div><div class="lab"><img src="{gen.HELMET}">SPARTANS</div></div>
<div style="position:absolute;top:1560px;left:0;right:0;text-align:center;font-weight:800;font-size:30px;letter-spacing:5px;color:{OR}">SIGUE LAS HISTORIAS</div>'''
    return page(body, CSS, seed=1501)


def escribes():
    pagos = [('refresh', 'TRANSFERENCIA'), ('cash', 'EFECTIVO'), ('credit-card', 'TARJETA'), ('shopping-cart', 'MERCADO PAGO')]
    ch = ''.join(f'<div class="chip">{ic(a, 54)}<span>{b}</span></div>' for a, b in pagos)
    body = f'''{BRAND}{tracker(1, 270)}
<div style="position:absolute;top:560px;left:70px;right:70px">
 <div class="big" style="font-size:110px">1. NOS ESCRIBES</div><div class="big o" style="font-size:110px">POR DM</div>
 <div style="margin-top:34px;display:flex;flex-direction:column;gap:20px">
  <div class="bub" style="align-self:flex-end;background:{OR};color:#0b0705;border-bottom-right-radius:8px">Hola, quiero empezar con creatina. ¿Cuál me recomiendan?</div>
  <div class="bub" style="align-self:flex-start;background:#2a2421;color:#fff;border-bottom-left-radius:8px">¡Hola! Te ayudo a elegir según tu objetivo y cuánto quieres que te dure.</div>
 </div>
 <div style="font-weight:600;font-size:24px;color:#888;margin-top:12px;text-transform:uppercase">Ejemplo de conversación</div>
 <div class="big" style="font-size:96px;margin-top:56px">2. PAGAS COMO</div><div class="big o" style="font-size:96px">PREFIERAS</div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:26px">{ch}</div>
</div>'''
    return page(body, CSS, seed=1502)


def preparamos():
    items = [('ORIGINALES Y SELLADOS', 'Tal como salen de la marca'),
             ('TE AYUDAMOS A ELEGIR', 'Según tu objetivo, sin vender de más'),
             ('PROTEÍNA + CREATINA', 'Va el shaker C4 de regalo en la caja')]
    ih = ''.join(f'<div class="ok"><i>{ic("check", 46)}</i><div>{a}<small>{b}</small></div></div>' for a, b in items)
    body = f'''{BRAND}{tracker(2, 270)}
<div style="position:absolute;top:560px;left:70px;right:70px"><div class="big" style="font-size:110px">3. PREPARAMOS</div><div class="big o" style="font-size:110px">TU PEDIDO</div></div>
<div style="position:absolute;top:840px;left:70px;right:70px">{ih}</div>
<div style="position:absolute;left:50%;top:1500px;width:900px;height:260px;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(ellipse,rgba(242,106,27,.4),transparent 70%)"></div>
<img src="{I("p_nitro.png")}" style="position:absolute;left:250px;top:1180px;height:360px;transform:rotate(-7deg);filter:drop-shadow(0 26px 26px #000);z-index:2">
<img src="{I("p_mt_sin.png")}" style="position:absolute;left:500px;top:1240px;height:300px;transform:rotate(5deg);filter:drop-shadow(0 26px 26px #000);z-index:2">
<img src="{I("p_shaker.png")}" style="position:absolute;left:690px;top:1240px;height:300px;transform:rotate(12deg);filter:drop-shadow(0 26px 26px #000);z-index:2">
<div class="box" style="top:1440px;height:230px"><div class="tape"></div><div class="lab"><img src="{gen.HELMET}">SPARTANS</div></div>'''
    return page(body, CSS, seed=1503)


def llega():
    d = [('map-pin', 'CALDERA', 'Delivery por $1.500 o retiro en domicilio'),
         ('building-store', 'COPIAPÓ', 'Hacemos entregas'),
         ('truck-delivery', 'TODO CHILE', 'Envío por pagar con Starken, Chilexpress o Blue Express')]
    dh = ''.join(f'<div class="dest"><div class="ico">{ic(a, 64)}</div><div><div class="t">{b}</div><div class="s">{c}</div></div></div>' for a, b, c in d)
    body = f'''{BRAND}{tracker(3, 270)}
<div style="position:absolute;top:560px;left:70px;right:70px"><div class="big" style="font-size:110px">4. TE LLEGA</div><div class="big o" style="font-size:110px">DONDE ESTÉS</div></div>
<div style="position:absolute;top:840px;left:70px;right:70px">{dh}
<div style="font-weight:600;font-size:26px;color:#999;text-transform:uppercase;margin-top:6px">Envíos: tú eliges la empresa. El plazo depende de tu ciudad.</div></div>'''
    return page(body, CSS, seed=1504)


def encuesta():
    body = f'''{BRAND}<div style="position:absolute;top:290px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:36px;letter-spacing:5px;color:#bbb">CUÉNTANOS</div>
<div class="big" style="font-size:140px;margin-top:10px">¿CÓMO PREFIERES</div><div class="big o" style="font-size:140px;text-shadow:0 0 50px rgba(242,106,27,.6)">RECIBIRLO?</div></div>
<div class="sticker" style="top:720px"></div>
{tracker(4, 1110, 'TU PRÓXIMO PEDIDO')}
<div style="position:absolute;top:1400px;left:0;right:0;display:flex;justify-content:center">
 <div style="display:flex;align-items:center;gap:12px;background:{OR};color:#0b0705;border-radius:14px;padding:12px 26px 4px"><span style="margin-bottom:8px">{ic("message-circle", 50).replace("currentColor", "#0b0705")}</span><span class="big" style="font-size:60px">PÍDELO POR DM</span></div></div>'''
    return page(body, CSS, seed=1505)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [('1_asi_viaja', gancho()), ('2_escribes_pagas', escribes()), ('3_preparamos', preparamos()),
             ('4_te_llega', llega()), ('5_encuesta', encuesta())]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, h in pages:
            pg = b.new_page(viewport={'width': W, 'height': H})
            pg.set_content(gen.sin_emoji(h), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, n + '.png')); pg.close(); print(n)
        b.close()
