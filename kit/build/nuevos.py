"""Lanzamiento de productos nuevos: carrusel 4:5 + historias 9:16 con reveal.
Uso (desde kit/build): python3 nuevos.py <carpeta_feed> <carpeta_historias>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright

FEED, HIST = sys.argv[1], sys.argv[2]
OR = '#F26A1B'
I = lambda n: gen.uri(os.path.join(gen.B, n))

# ---------- Carrusel (usa product_slide del kit) ----------
P = [
    dict(name='02_iso100', img='p_iso100.png', h=760, a='Nivel', b='PREMIUM.', c='Dymatize ISO 100 Hydrolyzed<br>5 lb · Cocoa Pebbles', price='$149.990',
         ben=[('barbell', '25 g de proteína', 'por porción'), ('droplet', '100% whey isolate', 'hidrolizada'), ('clock', '71 porciones', '5 lb (2,3 kg)')]),
    dict(name='03_nitro', img='p_nitro.png', h=700, a='Proteína +', b='CREATINA.', c='MuscleTech Nitro Tech<br>4 lb · vainilla', price='$99.990',
         ben=[('barbell', '30 g de proteína', 'por porción'), ('bolt', '3 g de creatina', 'en cada porción'), ('award', '4 lb (1,81 kg)', 'sabor vainilla')]),
    dict(name='04_finaflex', img='p_finaflex.png', h=740, a='1 kilo de', b='CREATINA.', c='Finaflex Creatine<br>1 kg · sin sabor', price='$49.990',
         ben=[('bolt', '5 g de creatina', 'micronizada'), ('clock', '200 porciones', '$250 al día'), ('shield-check', 'Certificada NSF', 'contenido verificado')]),
    dict(name='05_omega', img='p_omega.png', h=740, a='Tu esencial', b='DIARIO.', c='USN Omega 3 Fish Oil<br>1000 mg', price='$16.990',
         ben=[('droplet', '1000 mg', 'por cápsula'), ('pill', '90 cápsulas', 'blandas'), ('leaf', 'Ácidos grasos', 'esenciales')]),
    dict(name='06_guarana', img='p_guarana.png', h=760, a='Energía en', b='UN SHOT.', c='OstroVit Guaraná Shot<br>80 ml · sabor pera', price='$2.490',
         note='Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.',
         ben=[('bolt', '200 mg de cafeína', 'por shot'), ('bottle', '80 ml', 'listo para tomar'), ('flame', 'Sabor pera', 'antes de entrenar')]),
    dict(name='07_barra', img='p_barra.png', h=300, a='Proteína', b='AL PASO.', c='Space Protein XXL<br>80 g · coco', price='$2.490',
         ben=[('barbell', '36% proteína', 'barra de 80 g'), ('heart', '3 g de azúcar', 'por barra'), ('star', 'Sabor coco', 'tamaño XXL')]),
]
NEW = ['p_iso100.png', 'p_nitro.png', 'p_finaflex.png', 'p_omega.png', 'p_guarana.png', 'p_barra.png']


def cover():
    hs = [330, 320, 330, 290, 300, 120]
    row = ''.join(f'<img src="{I(i)}" style="height:{h}px;margin:0 -12px;filter:drop-shadow(0 20px 20px rgba(0,0,0,.85))">' for i, h in zip(NEW[:5], hs))
    css = gen.CSS + f"""
.hdr{{left:0;right:0;width:auto}}.hdr .ln{{width:460px}}
.big{{position:absolute;left:0;right:0;top:355px;text-align:center}}
.big .k{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:56px;padding:8px 26px 0;border-radius:10px;transform:rotate(-2deg);margin-bottom:18px}}
.big .a{{font-family:Bebas;font-size:200px;line-height:.85;color:#f1ece6}}
.big .b{{font-family:Bebas;font-size:120px;line-height:.9;color:{OR};text-shadow:0 0 40px rgba(242,106,27,.4)}}
.row6{{position:absolute;left:0;right:0;top:760px;height:340px;display:flex;align-items:flex-end;justify-content:center;z-index:3}}
.glow{{left:90px;top:640px;width:900px;height:560px}}
.ped{{left:110px;width:860px;top:1085px;height:70px}}
.bar6{{position:absolute;left:560px;top:1010px;width:330px;transform:rotate(-8deg);z-index:4;filter:drop-shadow(0 14px 14px rgba(0,0,0,.85))}}
.sw{{position:absolute;right:56px;top:1135px;font-family:Bebas;font-size:40px;color:{OR};letter-spacing:2px;z-index:4}}
"""
    return (f'<html><head><style>{css}</style></head><body>{gen.FX.replace("SEED", "6161")}<div class="stripes"></div><div class="glow"></div><div class="ped"></div>'
            f'{gen.header()}<div class="big"><div class="k">RECIÉN LLEGADOS</div><div class="a">NUEVO STOCK</div><div class="b">6 PRODUCTOS NUEVOS</div></div>'
            f'<div class="row6">{row}</div><img class="bar6" src="{I(NEW[5])}"><div class="sw">DESLIZA →</div>{gen.bar_html()}{gen.FIT}</body></html>')


# ---------- Historias ----------
W, H = 1080, 1920
FX = (gen.FX.replace('height="1350"', 'height="1920"').replace('1080,1350', '1080,1920').replace('780,1350', '540,1900')
      .replace('780,1300', '540,1500').replace('y=500+r()*850', 'y=200+r()*1720').replace('y=r()*1350', 'y=r()*1920').replace('(x-790)/320', '(x-540)/600'))
SCSS = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.big{{font-family:Bebas;line-height:.9;text-transform:uppercase}}.o{{color:{OR}}}
.card{{border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.85);border-radius:26px}}
.brand{{position:absolute;top:190px;left:70px;display:flex;align-items:center;gap:16px}}
.brand img{{height:62px}}.brand div{{font-family:Bebas;font-size:46px;letter-spacing:2px;line-height:.9}}
.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:20px;letter-spacing:5px;color:#bbb}}
.prog{{position:absolute;top:190px;right:70px;font-family:Bebas;font-size:44px;color:{OR}}}.prog span{{color:#666}}
.kick{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:54px;padding:8px 26px 0;border-radius:10px;transform:rotate(-2deg)}}
.glow{{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(242,106,27,.6),rgba(160,50,0,.22) 55%,transparent);filter:blur(10px)}}
.note{{font-size:24px;color:#aaa;font-weight:500}}
.sil{{filter:brightness(0) drop-shadow(0 0 3px {OR}) drop-shadow(0 0 3px {OR}) drop-shadow(0 0 24px rgba(242,106,27,.9))}}
"""
DONE = "<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"


def sp(body, seed, n, tot=5):
    b = f'<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div><div class="prog">{n}<span>/{tot}</span></div>'
    return f'<html><head><style>{SCSS}</style></head><body>{FX.replace("SEED", str(seed))}{b}{body}{DONE}</body></html>'


def fan(cls, top):
    pos = [(60, 320, -8), (250, 380, -3), (470, 360, 3), (660, 330, 7), (830, 340, 10)]
    out = ''
    for (x, h, r), img in zip(pos, NEW[:5]):
        out += f'<img class="{cls}" src="{I(img)}" style="position:absolute;left:{x}px;bottom:{1920 - top}px;height:{h}px;transform:rotate({r}deg)">'
    return out


def stories():
    s = []
    # 1 teaser: siluetas
    s.append(('h1_teaser', sp(f'''<div class="glow" style="left:90px;top:800px;width:900px;height:900px"></div>
<div style="position:absolute;top:430px;left:70px;right:70px"><div class="kick">ATENCIÓN SPARTANS</div>
<div class="big" style="font-size:190px;margin-top:30px">LLEGÓ</div><div class="big o" style="font-size:190px;text-shadow:0 0 40px rgba(242,106,27,.5)">ALGO NUEVO</div>
<div class="big" style="font-size:80px;margin-top:10px;color:#ddd">¿ADIVINAS QUÉ ES? 👀</div></div>
{fan("sil", 1560)}<div style="position:absolute;bottom:250px;left:0;right:0;text-align:center" class="big"><span style="font-size:52px;letter-spacing:3px">TOCA PARA DESCUBRIRLO <span class="o">→</span></span></div>''', 71, 1)))
    # 2 reveal
    s.append(('h2_reveal', sp(f'''<div class="glow" style="left:90px;top:800px;width:900px;height:900px"></div>
<div style="position:absolute;top:400px;left:70px;right:70px"><div class="big" style="font-size:300px;color:{OR};text-shadow:0 0 50px rgba(242,106,27,.5)">6</div>
<div class="big" style="font-size:130px;margin-top:-20px">PRODUCTOS</div><div class="big" style="font-size:130px">NUEVOS</div></div>
{fan("", 1530)}<img src="{I(NEW[5])}" style="position:absolute;left:560px;top:560px;width:460px;transform:rotate(-14deg);filter:drop-shadow(0 14px 14px rgba(0,0,0,.85))">
<div style="position:absolute;bottom:230px;left:0;right:0;text-align:center"><div class="big" style="font-size:52px">ISO 100 · NITRO TECH · FINAFLEX · OMEGA 3 · GUARANÁ · BARRAS</div></div>''', 72, 2)))
    # 3 esto o esto: proteínas
    def col(img, name, rows, price):
        r = ''.join(f'<div style="display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.12)"><span style="color:#bbb;font-weight:600;font-size:28px;text-transform:uppercase">{a}</span><span class="big" style="font-size:44px">{b}</span></div>' for a, b in rows)
        return f'''<div class="card" style="flex:1;padding:24px 26px;text-align:center"><img src="{I(img)}" style="height:380px;filter:drop-shadow(0 18px 14px #000)">
<div class="big" style="font-size:58px;margin:10px 0 6px">{name}</div><div style="text-align:left">{r}</div><div class="big o" style="font-size:74px;margin-top:16px">{price}</div></div>'''
    s.append(('h3_proteinas', sp(f'''<div style="position:absolute;top:390px;left:70px;right:70px"><div class="big" style="font-size:120px">¿CUÁL ES</div><div class="big o" style="font-size:150px">TU PROTEÍNA?</div></div>
<div style="position:absolute;top:740px;left:50px;right:50px;display:flex;gap:26px">
{col("p_iso100.png", "ISO 100", [("Proteína", "25 g"), ("Tipo", "ISOLATE"), ("Porciones", "71")], "$149.990")}
{col("p_nitro.png", "NITRO TECH", [("Proteína", "30 g"), ("Extra", "+3 G CREATINA"), ("Tamaño", "4 LB")], "$99.990")}</div>
<div style="position:absolute;bottom:250px;left:0;right:0;text-align:center" class="big"><span style="font-size:48px">RESPONDE <span class="o">ISO</span> O <span class="o">NITRO</span> POR DM</span></div>''', 73, 3)))
    # 4 finaflex
    s.append(('h4_finaflex', sp(f'''<div class="glow" style="left:240px;top:760px;width:800px;height:900px"></div>
<div style="position:absolute;top:400px;left:70px;right:70px"><div class="kick">EL MÁS RENDIDOR</div>
<div class="big" style="font-size:260px;margin-top:24px">1 KG</div><div class="big o" style="font-size:120px">200 PORCIONES</div></div>
<img src="{I("p_finaflex.png")}" style="position:absolute;right:40px;top:830px;height:700px;transform:rotate(5deg);filter:drop-shadow(0 30px 30px #000)">
<div style="position:absolute;left:70px;top:900px;width:430px">
 <div class="card" style="padding:30px 32px;margin-bottom:24px"><div style="font-weight:700;font-size:30px;color:#bbb">TE SALE A</div><div class="big o" style="font-size:120px">$250</div><div style="font-weight:700;font-size:30px;color:#bbb">AL DÍA</div></div>
 <div class="card" style="padding:26px 32px"><div class="big" style="font-size:96px">$49.990</div><div style="font-weight:600;font-size:26px;color:#bbb;text-transform:uppercase">Finaflex · micronizada · NSF</div></div></div>
<div style="position:absolute;bottom:250px;left:0;right:0;text-align:center" class="big"><span style="font-size:50px">ESCRÍBENOS <span class="o">"CREATINA"</span> POR DM</span></div>''', 74, 4)))
    # 5 al paso
    s.append(('h5_al_paso', sp(f'''<div style="position:absolute;top:400px;left:70px;right:70px"><div class="big" style="font-size:150px">PARA ANTES</div><div class="big o" style="font-size:150px;text-shadow:0 0 40px rgba(242,106,27,.45)">Y DESPUÉS</div></div>
<div class="glow" style="left:90px;top:800px;width:900px;height:800px"></div>
<div style="position:absolute;top:760px;left:50px;right:50px;display:flex;gap:26px">
 <div class="card" style="flex:1;padding:28px;text-align:center"><div class="big o" style="font-size:44px">ANTES DE ENTRENAR</div><img src="{I("p_guarana.png")}" style="height:440px;margin:16px 0;filter:drop-shadow(0 18px 14px #000)"><div class="big" style="font-size:52px">GUARANÁ SHOT</div><div class="big o" style="font-size:84px">$2.490</div></div>
 <div class="card" style="flex:1;padding:28px;text-align:center;display:flex;flex-direction:column;align-items:center"><div class="big o" style="font-size:44px">DESPUÉS O DE COLACIÓN</div><div style="flex:1;display:flex;align-items:center"><img src="{I("p_barra.png")}" style="width:400px;transform:rotate(-12deg);filter:drop-shadow(0 18px 14px #000)"></div><div class="big" style="font-size:52px">BARRA XXL COCO</div><div class="big o" style="font-size:84px">$2.490</div></div></div>
<div style="position:absolute;top:1450px;left:70px;right:70px;text-align:center" class="note">Guaraná Shot contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.</div>
<div style="position:absolute;bottom:230px;left:0;right:0;text-align:center"><div class="kick" style="font-size:62px">PÍDELOS POR DM 📩</div><div style="font-weight:700;font-size:28px;margin-top:18px;color:#ddd">DELIVERY EN CALDERA $1.500 · ENVÍOS A TODO CHILE</div></div>''', 75, 5)))
    return s


def render(pages, out, w, h):
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': w, 'height': h})
        for n, html in pages:
            pg.set_content(html, wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(out, n + '.png')); print(n)
        b.close()


if __name__ == '__main__':
    feed = [('01_portada', cover())] + [(d['name'], gen.product_slide(d, 900 + i * 37)) for i, d in enumerate(P)]
    render(feed, FEED, 1080, 1350)
    render(stories(), HIST, W, H)
