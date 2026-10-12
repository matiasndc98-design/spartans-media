"""Historias interactivas 9:16 más visuales: "esto o esto" en pantalla dividida, adivinanza con producto gigante,
revelación con número enorme y adelanto con cuenta regresiva. Sin precios ni numeración.
Uso (desde kit/build): python3 stories_esto_o_esto.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
OR = '#F26A1B'
W, H = 1080, 1920
I = lambda n: gen.uri(os.path.join(gen.B, n))
FX = (gen.FX.replace('height="1350"', 'height="1920"').replace('1080,1350', '1080,1920').replace('780,1350', '540,1900')
      .replace('780,1300', '540,1500').replace('y=500+r()*850', 'y=200+r()*1720').replace('y=r()*1350', 'y=r()*1920').replace('(x-790)/320', '(x-540)/600'))
BASE = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}.o{{color:{OR}}}
.brand{{position:absolute;top:150px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:14px;z-index:9}}
.brand img{{height:56px}}.brand div{{font-family:Bebas;font-size:42px;letter-spacing:2px;line-height:.9}}
.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:18px;letter-spacing:5px;color:#bbb}}
.sticker{{position:absolute;left:190px;right:190px;height:300px}}
"""
DONE = "<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"
BRAND = f'<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>'


def page(body, css='', seed=5, fx=True):
    return f'<html><head><style>{BASE}{css}</style></head><body>{FX.replace("SEED", str(seed)) if fx else ""}{body}{DONE}</body></html>'


def esto_o_esto():
    css = """
.half{position:absolute;top:0;bottom:0;width:540px;overflow:hidden}
.l{left:0;background:radial-gradient(circle at 50% 52%,#3a3a3a,#111 55%,#060504)}
.r{right:0;background:radial-gradient(circle at 50% 52%,#6b2fa6,#2a0f44 55%,#0b0510)}
.half img{position:absolute;left:50%;top:640px;height:640px;transform:translateX(-50%);filter:drop-shadow(0 40px 34px #000)}
.lab{position:absolute;top:1300px;left:0;right:0;text-align:center}
.vs{position:absolute;left:50%;top:860px;transform:translate(-50%,-50%) rotate(-8deg);width:190px;height:190px;border-radius:50%;
 background:#F26A1B;color:#0b0705;display:grid;place-items:center;font-family:Bebas;font-size:110px;box-shadow:0 0 0 12px #060504,0 0 60px rgba(242,106,27,.8);z-index:5}
"""
    body = f'''<div class="half l"><img src="{I("p_mt_sin.png")}"><div class="lab"><div class="big" style="font-size:120px">SIN SABOR</div><div style="font-weight:700;font-size:30px;color:#ccc">LA MEZCLAS CON LO QUE QUIERAS</div></div></div>
<div class="half r"><img src="{I("p_mt_uva.png")}"><div class="lab"><div class="big" style="font-size:120px;color:#d9b3ff">SABOR UVA</div><div style="font-weight:700;font-size:30px;color:#ccc">SOLO CON AGUA Y LISTO</div></div></div>
{BRAND}<div style="position:absolute;top:270px;left:0;right:0;text-align:center;z-index:6"><div class="big" style="font-size:150px;text-shadow:0 6px 30px #000">¿CUÁL ERES?</div>
<div style="font-weight:800;font-size:34px;letter-spacing:4px;color:#fff;margin-top:6px">CREATINA MUSCLETECH PLATINUM</div></div>
<div class="vs">VS</div><div class="sticker" style="top:1500px"></div>'''
    return page(body, css, fx=False)


def adivina():
    body = f'''{BRAND}<div style="position:absolute;top:260px;left:70px;right:70px"><span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:56px;padding:8px 22px 0;border-radius:10px;transform:rotate(-3deg)">ADIVINA 🤔</span>
<div class="big" style="font-size:118px;margin-top:22px">¿CUÁNTAS PORCIONES</div><div class="big o" style="font-size:118px">TRAE ESTE TARRO?</div></div>
<div style="position:absolute;left:-40px;right:-40px;top:560px;height:820px;display:flex;justify-content:center;align-items:center">
 <div style="position:absolute;width:820px;height:820px;border-radius:50%;background:radial-gradient(closest-side,rgba(242,106,27,.6),transparent)"></div>
 <img src="{I("p_finaflex.png")}" style="height:780px;position:relative;transform:rotate(-6deg);filter:drop-shadow(0 40px 40px #000)">
 <div class="big" style="position:absolute;right:120px;top:40px;background:#fff;color:#0b0705;font-size:90px;padding:10px 26px 0;border-radius:16px;transform:rotate(8deg)">1 KG</div></div>
<div class="sticker" style="top:1400px"></div>'''
    return page(body, seed=811)


def respuesta():
    body = f'''{BRAND}<div style="position:absolute;top:300px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:40px;letter-spacing:6px;color:#3ccf6e">RESPUESTA</div></div>
<div style="position:absolute;top:360px;left:0;right:0;text-align:center"><div class="big o" style="font-size:520px;line-height:.8;text-shadow:0 0 80px rgba(242,106,27,.7)">200</div>
<div class="big" style="font-size:140px;margin-top:-10px">PORCIONES</div></div>
<div style="position:absolute;top:1000px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:30px">
 <img src="{I("p_finaflex.png")}" style="height:420px;filter:drop-shadow(0 30px 26px #000)">
 <div><div class="big" style="font-size:96px">+6 MESES</div><div style="font-weight:700;font-size:34px;color:#ddd;text-transform:uppercase;line-height:1.15">tomando 5 g<br>todos los días</div>
 <div style="font-weight:700;font-size:28px;color:#aaa;text-transform:uppercase;margin-top:14px">Micronizada · certificada NSF</div></div></div>
<div style="position:absolute;top:1520px;left:0;right:0;text-align:center"><span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:70px;padding:12px 34px 0;border-radius:16px;box-shadow:0 0 40px rgba(242,106,27,.6)">PÍDELA POR DM 📩</span></div>'''
    return page(body, seed=919)


def adelanto():
    sil = ''.join(f'<img src="{I(p)}" style="height:{h}px;margin:0 -10px;filter:brightness(0) drop-shadow(0 0 3px {OR}) drop-shadow(0 0 26px rgba(242,106,27,.9))">'
                  for p, h in [('p_usn_crea.png', 360), ('p_mt_sin.png', 400), ('p_finaflex.png', 440)])
    body = f'''{BRAND}<div style="position:absolute;top:290px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:40px;letter-spacing:6px;color:#bbb">ESTE JUEVES · 6 PM</div>
<div class="big" style="font-size:150px;margin-top:16px">¿QUÉ CREATINA</div><div class="big o" style="font-size:190px;text-shadow:0 0 40px rgba(242,106,27,.6)">TE CONVIENE?</div></div>
<div style="position:absolute;top:800px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;height:460px">{sil}</div>
<div style="position:absolute;top:1290px;left:0;right:0;text-align:center;font-weight:800;font-size:36px;letter-spacing:3px">LAS COMPARAMOS EN UN REEL 🎬</div>
<div class="sticker" style="top:1380px;height:260px"></div>'''
    return page(body, seed=303)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [('1_esto_o_esto', esto_o_esto()), ('2_adivina', adivina()), ('3_respuesta', respuesta()), ('4_adelanto_jueves', adelanto())]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
        for n, h in pages:
            pg.set_content(h, wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, n + '.png')); print(n)
        b.close()
