"""Viernes 16 oct 2026 · cierre de la semana de la creatina.
Carrusel 4:5 comparativa "¿Micronizada o normal?" (qué cambia y qué no) + historias 9:16 "Arma tu combo"
estilo tótem de autoservicio (idea nueva): eliges proteína -> eliges creatina -> el shaker se suma solo,
con una bandeja "TU COMBO" abajo que se va llenando. Cierra con encuesta. Sin precios ni numeración.
Uso (desde kit/build): python3 viernes_combo.py <carpeta_feed> <carpeta_historias> [nombres]
Respaldo: micronizada = monohidrato con partícula más fina -> mejor solubilidad; no hay evidencia de mayor efecto
(ISSN, Kreider et al. 2017: el monohidrato es la forma de referencia; 3-5 g/día).
"""
import sys, os
sys.path.insert(0, '.')
import gen
from stories_esto_o_esto import page, BRAND, I, OR, W, H
from playwright.sync_api import sync_playwright
from PIL import Image

FEED, STO = sys.argv[1], sys.argv[2]
only = sys.argv[3:]
ic = gen.icon
GREEN = '#3ccf6e'

COMMON = f"""
.kick{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:54px;padding:8px 26px 0;border-radius:10px;transform:rotate(-2deg)}}
.card{{border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.9);border-radius:26px;padding:30px 36px}}
.txt{{font-weight:600;font-size:38px;line-height:1.16;text-transform:uppercase}}
.fine{{font-weight:500;font-size:24px;color:#9a9a9a;text-transform:uppercase}}
.glow{{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(242,106,27,.55),rgba(160,50,0,.2) 55%,transparent);filter:blur(10px)}}
.row{{display:flex;gap:22px;align-items:center;margin-bottom:24px}}
.row .ck{{flex:none;width:64px;height:64px;border-radius:50%;display:grid;place-items:center}}
.swipe{{position:absolute;right:70px;bottom:60px;font-family:Bebas;font-size:44px;letter-spacing:2px;color:#ddd}}
.swipe b{{color:{OR};font-weight:400}}
"""

# ---------------- CARRUSEL 4:5 ----------------
FX_FEED = gen.FX
FBASE = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}.o{{color:{OR}}}
.brand{{position:absolute;top:58px;left:70px;display:flex;align-items:center;gap:16px}}
.brand img{{height:62px}}.brand div{{font-family:Bebas;font-size:46px;letter-spacing:2px;line-height:.9}}
.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:20px;letter-spacing:5px;color:#bbb}}
"""
READY = "<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"


def feed(body, seed):
    b = f'<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>'
    return f'<html><head><style>{FBASE}{COMMON}</style></head><body>{FX_FEED.replace("SEED", str(seed))}{b}{body}{READY}</body></html>'


def grains(n, rmin, rmax, seed, w=380, h=300, col='#f2ece4'):
    import random
    r = random.Random(seed)
    dots = ''
    for _ in range(n):
        s = r.uniform(rmin, rmax)
        x, y = r.uniform(0, w - s), r.uniform(0, h - s)
        rad = f'{r.randint(20, 45)}% {r.randint(30, 60)}% {r.randint(25, 50)}% {r.randint(35, 60)}%'
        dots += f'<i style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{s:.0f}px;height:{s * r.uniform(.7, 1):.0f}px;border-radius:{rad};background:{col};opacity:{r.uniform(.75, 1):.2f};box-shadow:0 2px 4px rgba(0,0,0,.6)"></i>'
    return f'<div style="position:relative;width:{w}px;height:{h}px">{dots}</div>'


F = []
F.append(('1_portada', feed(f'''
<div class="glow" style="left:380px;top:460px;width:800px;height:880px"></div>
<img src="{I('p_finaflex.png')}" style="position:absolute;right:20px;bottom:110px;height:600px;transform:rotate(7deg);filter:drop-shadow(0 30px 30px #000)">
<img src="{I('p_mt_sin.png')}" style="position:absolute;right:330px;bottom:130px;height:440px;transform:rotate(-6deg);filter:drop-shadow(0 30px 30px #000)">
<div style="position:absolute;top:230px;left:70px;right:70px">
 <div class="kick">GUÁRDALO</div>
 <div class="big" style="font-size:118px;margin-top:30px">CREATINA</div>
 <div class="big o" style="font-size:176px;text-shadow:0 0 40px rgba(242,106,27,.5)">MICRONIZADA</div>
 <div style="font-weight:700;font-size:40px;text-transform:uppercase;color:#ddd;margin-top:20px;line-height:1.1">¿Qué significa<br>y qué cambia?</div>
</div>
<div class="swipe" style="left:70px;right:auto">DESLIZA <b>→</b></div>''', 1601)))

F.append(('2_que_es', feed(f'''
<div style="position:absolute;top:180px;left:70px;right:70px">
 <div class="big" style="font-size:112px">ES LA MISMA</div>
 <div class="big o" style="font-size:112px">CREATINA, MÁS FINA</div>
 <div class="txt" style="margin-top:22px;color:#ddd">Creatina monohidrato molida en partículas más pequeñas. Nada más.</div>
</div>
<div style="position:absolute;top:620px;left:50px;right:50px;display:flex;gap:30px">
 <div class="card" style="flex:1;padding:26px;text-align:center;border-color:rgba(255,255,255,.25)">
  <div class="big" style="font-size:60px">MONOHIDRATO</div><div class="fine" style="margin-bottom:18px">Partícula normal</div>
  <div style="display:flex;justify-content:center">{grains(34, 34, 58, 3, 380, 290)}</div></div>
 <div class="card" style="flex:1;padding:26px;text-align:center">
  <div class="big o" style="font-size:60px">MICRONIZADA</div><div class="fine" style="margin-bottom:18px">Partícula más fina</div>
  <div style="display:flex;justify-content:center">{grains(700, 6, 13, 4, 380, 290)}</div></div>
</div>
<div class="fine" style="position:absolute;top:1090px;left:70px;right:70px;text-align:center">Ilustración, no a escala</div>
<div class="swipe">SIGUE <b>→</b></div>''', 1602)))


def lista(items, color, icon):
    return ''.join(f'<div class="row"><div class="ck" style="background:{color}22;border:2px solid {color}">{ic(icon, 36).replace("currentColor", color)}</div><div class="txt">{t}</div></div>' for t in items)


F.append(('3_que_cambia', feed(f'''
<div style="position:absolute;top:170px;left:70px;right:70px">
 <div class="big" style="font-size:104px">LO QUE <span class="o">CAMBIA</span></div>
</div>
<div style="position:absolute;top:290px;left:70px;right:70px">{lista([
    'Se disuelve <span class="o">más fácil</span>',
    'Menos arenilla en el fondo del vaso',
    'Se integra mejor en tu batido'], GREEN, 'check')}</div>
<div style="position:absolute;top:640px;left:70px;right:70px;height:3px;background:linear-gradient(90deg,transparent,{OR},transparent)"></div>
<div style="position:absolute;top:690px;left:70px;right:70px">
 <div class="big" style="font-size:104px">LO QUE <span class="o">NO CAMBIA</span></div>
</div>
<div style="position:absolute;top:810px;left:70px;right:70px">{lista([
    'La dosis: <span class="o">3 a 5 g al día</span>',
    'Que la tomes todos los días',
    'Su efecto: sigue siendo monohidrato'], '#bbbbbb', 'shield-check')}</div>
<div class="swipe">SIGUE <b>→</b></div>''', 1603)))

CREAS = [('p_mt_sin.png', 'MuscleTech Platinum', '400 g · sin sabor', '80', 'MICRONIZADA', 330),
         ('p_finaflex.png', 'Finaflex', '1 kg · sin sabor · NSF', '200', 'MICRONIZADA', 360),
         ('p_usn_crea.png', 'USN', '300 g · sin sabor', '60', 'IDEAL PARA EMPEZAR', 320)]
ch = ''.join(f'''<div style="flex:1;display:flex;flex-direction:column;align-items:center">
 <div style="height:380px;display:flex;align-items:flex-end"><img src="{I(p)}" style="height:{h}px;max-width:290px;object-fit:contain;filter:drop-shadow(0 16px 14px #000)"></div>
 <div style="margin-top:18px;background:{OR if t == 'MICRONIZADA' else '#2a2421'};color:{'#0b0705' if t == 'MICRONIZADA' else '#fff'};font-family:Bebas;font-size:32px;padding:6px 14px 0;border-radius:8px;letter-spacing:1px">{t}</div>
 <div style="font-weight:800;font-size:30px;text-transform:uppercase;margin-top:14px;text-align:center;line-height:1">{n}</div>
 <div class="fine" style="margin-top:6px;font-size:22px">{g}</div>
 <div class="big o" style="font-size:78px;margin-top:8px">{d}</div><div class="fine" style="margin-top:-4px">PORCIONES</div></div>''' for p, n, g, d, t, h in CREAS)
F.append(('4_en_spartans', feed(f'''
<div style="position:absolute;top:170px;left:70px;right:70px">
 <div class="big" style="font-size:104px">¿CUÁL ES CUÁL</div>
 <div class="big o" style="font-size:104px">EN SPARTANS?</div>
</div>
<div class="glow" style="left:90px;top:470px;width:900px;height:560px"></div>
<div style="position:absolute;top:420px;left:30px;right:30px;display:flex;gap:10px">{ch}</div>
<div class="txt" style="position:absolute;top:1150px;left:70px;right:70px;text-align:center;font-size:32px;color:#ddd">Las tres son creatina monohidrato. Elige por textura y cuánto te dura.</div>
<div class="swipe">SIGUE <b>→</b></div>''', 1604)))

PASOS = [('glass-full', 'Primero el líquido', 'Agua, jugo o tu batido'), ('scale', 'Después el scoop', '5 g, al nivel'),
         ('refresh', 'Agita 10 segundos', 'En el shaker queda lista'), ('bolt', 'Tómala al tiro', 'Sin dejarla reposar horas')]
ph = ''.join(f'<div class="row" style="margin-bottom:20px"><div class="ck" style="background:rgba(242,106,27,.12);border:2px solid {OR};color:{OR}">{ic(a, 36)}</div><div><div class="big" style="font-size:54px">{b}</div><div class="fine" style="font-size:24px">{c}</div></div></div>' for a, b, c in PASOS)
F.append(('5_sin_grumos', feed(f'''
<div style="position:absolute;top:170px;left:70px;right:70px">
 <div class="big" style="font-size:104px">TIP: <span class="o">SIN GRUMOS</span></div>
 <div style="font-weight:600;font-size:30px;color:#ccc;text-transform:uppercase;margin-top:10px">Sirve para cualquier creatina</div>
</div>
<div style="position:absolute;top:400px;left:70px;width:640px">{ph}</div>
<div class="glow" style="left:650px;top:430px;width:480px;height:600px"></div>
<img src="{I('p_shaker.png')}" style="position:absolute;right:50px;top:470px;height:500px;transform:rotate(8deg);filter:drop-shadow(0 20px 20px #000)">
<div class="card" style="position:absolute;top:1010px;left:60px;right:60px;display:flex;align-items:center;justify-content:space-between;padding:24px 34px">
 <div style="font-weight:700;font-size:32px;text-transform:uppercase;line-height:1.1">Proteína + creatina =<br><span class="o">shaker C4 de regalo</span></div>
 <span class="kick" style="font-size:46px;transform:rotate(-2deg)">PÍDELA POR DM</span>
</div>
<div style="position:absolute;bottom:22px;left:0;right:0;text-align:center;font-size:19px;color:#888">Si tienes alguna enfermedad o tomas medicamentos, consulta a tu médico.</div>''', 1605)))

# ---------------- HISTORIAS 9:16: ARMA TU COMBO ----------------
SCSS = COMMON + f"""
.kiosk{{position:absolute;left:50px;right:50px;top:250px;display:flex;gap:12px;z-index:5}}
.kiosk div{{flex:1;text-align:center;font-family:Bebas;font-size:38px;letter-spacing:2px;padding:14px 0 6px;border-radius:14px;background:#1c1613;color:#6d625b;border:2px solid #2c2420}}
.kiosk div.on{{background:{OR};color:#0b0705;border-color:{OR};box-shadow:0 0 30px rgba(242,106,27,.6)}}
.kiosk div.ok{{background:#2a1708;color:{OR};border-color:rgba(242,106,27,.6)}}
.opt{{background:rgba(20,14,10,.92);border:2px solid rgba(255,255,255,.14);border-radius:26px;display:flex;align-items:center;gap:26px;padding:18px 28px;margin-bottom:20px}}
.opt .im{{width:170px;height:190px;display:flex;align-items:center;justify-content:center;flex:none}}
.opt .im img{{max-height:190px;max-width:170px;filter:drop-shadow(0 10px 10px #000)}}
.opt .n{{font-family:Bebas;font-size:62px;line-height:.9}}
.opt .d{{font-weight:700;font-size:28px;color:#ccc;text-transform:uppercase;line-height:1.15;margin-top:6px}}
.opt .d b{{color:{OR}}}
.tray{{position:absolute;left:50px;right:50px;top:1390px;background:#f3eee6;color:#111;border-radius:26px;padding:16px 30px 20px;z-index:5;box-shadow:0 20px 50px rgba(0,0,0,.7)}}
.tray .h{{font-family:Bebas;font-size:36px;letter-spacing:3px;color:#7a6f68;display:flex;justify-content:space-between}}
.tray .h b{{color:{OR};font-weight:400}}
.tray .s{{display:flex;align-items:center;justify-content:space-between;margin-top:6px}}
.slot{{width:230px;height:150px;border-radius:18px;display:flex;align-items:center;justify-content:center;background:#e4ddd3}}
.slot img{{max-height:136px;max-width:210px}}
.slot.q{{border:4px dashed #b9aea5;background:none;font-family:Bebas;font-size:90px;color:#b9aea5}}
.tray .p{{font-family:Bebas;font-size:80px;color:{OR}}}
"""
STEPS = ['PROTEÍNA', 'CREATINA', 'TU REGALO']


def kiosk(cur):
    return '<div class="kiosk">' + ''.join(
        f'<div class="{"on" if k == cur else ("ok" if k < cur else "")}">{"✓ " if k < cur else ""}{s}</div>' for k, s in enumerate(STEPS)) + '</div>'


def tray(a=None, b=None, c=None, label='TU COMBO'):
    def sl(x):
        return f'<div class="slot"><img src="{I(x)}"></div>' if x else '<div class="slot q">?</div>'
    return f'''<div class="tray"><div class="h"><span>{label}</span><b>PÍDELO POR DM</b></div>
<div class="s">{sl(a)}<span class="p">+</span>{sl(b)}<span class="p">+</span>{sl(c)}</div></div>'''


def sp(body, seed):
    return page(BRAND.replace('top:150px', '') + body, SCSS, seed=seed)


S = []
S.append(('1_arma_tu_combo', sp(f'''
<div style="position:absolute;top:290px;left:0;right:0;text-align:center"><span class="kick" style="font-size:50px">PROMO REAL DE LA TIENDA</span></div>
<div style="position:absolute;top:400px;left:0;right:0;text-align:center">
 <div class="big" style="font-size:170px">ARMA TU</div>
 <div class="big o" style="font-size:190px;text-shadow:0 0 50px rgba(242,106,27,.6)">COMBO</div>
 <div style="font-weight:700;font-size:36px;letter-spacing:3px;color:#ddd;margin-top:16px;text-transform:uppercase">Proteína + creatina = shaker de regalo</div>
</div>
<div class="glow" style="left:90px;top:860px;width:900px;height:560px"></div>
<img src="{I('p_whey.png')}" style="position:absolute;left:90px;top:870px;height:470px;transform:rotate(-7deg);filter:drop-shadow(0 30px 30px #000);z-index:2">
<div class="big o" style="position:absolute;left:420px;top:1040px;font-size:140px;z-index:3">+</div>
<img src="{I('p_finaflex.png')}" style="position:absolute;left:500px;top:900px;height:430px;transform:rotate(5deg);filter:drop-shadow(0 30px 30px #000);z-index:2">
<img src="{I('p_shaker.png')}" style="position:absolute;left:780px;top:960px;height:360px;transform:rotate(12deg);filter:drop-shadow(0 30px 30px #000);z-index:2">
<div style="position:absolute;top:1440px;left:0;right:0;text-align:center;font-family:Bebas;font-size:60px;letter-spacing:3px">ELIGE EN <span class="o">3 PASOS</span> {ic('arrow-right', 54).replace('currentColor', OR)}</div>''', 1611)))

PROT = [('p_whey.png', 'WHEY USN 5 LB', '<b>22 g</b> de proteína · chocolate', 'Para el día a día'),
        ('p_iso100.png', 'ISO 100 DYMATIZE', '<b>25 g</b> · 100% whey isolate', 'Cocoa Pebbles · 5 lb'),
        ('p_nitro.png', 'NITRO TECH', '<b>30 g</b> + 3 g de creatina', 'Vainilla · 4 lb')]
ph = ''.join(f'<div class="opt"><div class="im"><img src="{I(p)}"></div><div><div class="n">{n}</div><div class="d">{d}<br>{e}</div></div></div>' for p, n, d, e in PROT)
S.append(('2_elige_proteina', sp(f'''{kiosk(0)}
<div style="position:absolute;top:370px;left:70px;right:70px"><div class="big" style="font-size:120px">ELIGE TU <span class="o">PROTEÍNA</span></div>
<div class="fine" style="font-size:26px;margin-top:6px">Proteína por porción</div></div>
<div style="position:absolute;top:540px;left:60px;right:60px">{ph}</div>
{tray()}''', 1612)))

CRE = [('p_usn_crea.png', 'USN 300 G', '<b>60</b> porciones · sin sabor'),
       ('p_mt_sin.png', 'MUSCLETECH 400 G', '<b>80</b> porciones · micronizada'),
       ('p_mt_uva.png', 'MUSCLETECH UVA', '<b>60</b> porciones · sabor uva'),
       ('p_finaflex.png', 'FINAFLEX 1 KG', '<b>200</b> porciones · NSF')]
chh = ''.join(f'<div class="opt" style="flex-direction:column;gap:6px;padding:16px 10px;margin:0;text-align:center"><div class="im" style="height:200px"><img src="{I(p)}" style="max-height:200px"></div><div class="n" style="font-size:48px">{n}</div><div class="d" style="font-size:24px">{d}</div></div>' for p, n, d in CRE)
S.append(('3_elige_creatina', sp(f'''{kiosk(1)}
<div style="position:absolute;top:370px;left:70px;right:70px"><div class="big" style="font-size:120px">ELIGE TU <span class="o">CREATINA</span></div>
<div class="fine" style="font-size:26px;margin-top:6px">5 g por porción · todas monohidrato</div></div>
<div style="position:absolute;top:540px;left:60px;right:60px;display:grid;grid-template-columns:1fr 1fr;gap:18px">{chh}</div>
{tray('p_whey.png')}''', 1613)))

S.append(('4_tu_regalo', sp(f'''{kiosk(2)}
<div style="position:absolute;top:380px;left:0;right:0;text-align:center"><div class="big" style="font-size:120px">EL SHAKER</div>
<div class="big o" style="font-size:150px;text-shadow:0 0 50px rgba(242,106,27,.6)">VA DE REGALO</div></div>
<div class="glow" style="left:190px;top:700px;width:700px;height:640px"></div>
<img src="{I('p_shaker.png')}" style="position:absolute;left:50%;top:700px;height:560px;transform:translateX(-50%) rotate(6deg);filter:drop-shadow(0 30px 30px #000);z-index:2">
<div style="position:absolute;top:1290px;left:60px;right:60px;text-align:center;font-weight:700;font-size:30px;color:#ddd;text-transform:uppercase;z-index:3">Shaker C4 por compra de proteína + creatina</div>
{tray('p_whey.png', 'p_finaflex.png', 'p_shaker.png', 'TU COMBO ESTÁ LISTO')}''', 1614)))

S.append(('5_encuesta', sp(f'''
<div style="position:absolute;top:290px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:36px;letter-spacing:5px;color:#bbb">ARMA EL TUYO</div>
<div class="big" style="font-size:140px;margin-top:10px">¿CON QUÉ PROTEÍNA</div><div class="big o" style="font-size:140px;text-shadow:0 0 50px rgba(242,106,27,.6)">PARTE TU COMBO?</div></div>
<div class="sticker" style="top:720px;height:340px"></div>
<div style="position:absolute;top:1120px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:40px">
 <img src="{I('p_whey.png')}" style="height:230px;filter:drop-shadow(0 14px 14px #000)">
 <img src="{I('p_iso100.png')}" style="height:250px;filter:drop-shadow(0 14px 14px #000)">
 <img src="{I('p_nitro.png')}" style="height:230px;filter:drop-shadow(0 14px 14px #000)"></div>
<div style="position:absolute;top:1450px;left:0;right:0;display:flex;justify-content:center">
 <div style="display:flex;align-items:center;gap:12px;background:{OR};color:#0b0705;border-radius:14px;padding:12px 26px 4px"><span style="margin-bottom:8px">{ic("message-circle", 50).replace("currentColor", "#0b0705")}</span><span class="big" style="font-size:60px">PIDE TU COMBO POR DM</span></div></div>''', 1615)))


def run(pages, out, h):
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, html in pages:
            pg = b.new_page(viewport={'width': 1080, 'height': h})
            pg.set_content(gen.sin_emoji(html), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            png = os.path.join(out, n + '.png'); pg.screenshot(path=png); pg.close()
            Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=90); os.remove(png); print(n)
        b.close()


run([x for x in F if not only or x[0] in only], FEED, 1350)
run([x for x in S if not only or x[0] in only], STO, 1920)
