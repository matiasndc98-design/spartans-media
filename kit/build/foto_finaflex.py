"""Publicidad con foto real del dueño (Finaflex 1 kg en la mano): historia 9:16 y post 4:5. Sin precios ni emojis.
Uso (desde kit/build): python3 foto_finaflex.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
OR = '#F26A1B'
FOTO = gen.uri(os.path.join(gen.B, '..', 'fotos_dueno', 'finaflex_mano.jpg'))
BASE = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
.big{{font-family:Bebas;line-height:.86;text-transform:uppercase}}.o{{color:{OR}}}
.brand{{display:flex;align-items:center;gap:14px}}.brand img{{height:64px}}
.brand div{{font-family:Bebas;font-size:44px;letter-spacing:2px;line-height:.9}}.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:18px;letter-spacing:5px;color:#ddd}}
.pill{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;border-radius:14px;box-shadow:0 0 40px rgba(242,106,27,.6)}}
.chip{{display:inline-flex;align-items:center;gap:12px;background:rgba(6,5,4,.78);border:2px solid rgba(242,106,27,.75);border-radius:16px;padding:12px 22px 10px;font-weight:800;font-size:30px;letter-spacing:1px;text-transform:uppercase;color:#fff}}
.chip svg{{color:{OR}}}
"""
DONE = "<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"
BR = f'<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>'


def historia():
    return f'''<html><head><style>{BASE}body{{width:1080px;height:1920px}}</style></head><body>
<img src="{FOTO}" style="position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,5,4,.92) 0%,rgba(6,5,4,.55) 17%,rgba(6,5,4,0) 30%,rgba(6,5,4,0) 62%,rgba(6,5,4,.75) 76%,rgba(6,5,4,.96) 88%)"></div>
<div style="position:absolute;top:150px;left:70px">{BR}</div>
<div style="position:absolute;top:260px;left:70px;right:70px"><div class="big" style="font-size:96px;color:#ddd">¿ES GIGANTE?</div>
<div class="big o" style="font-size:190px;text-shadow:0 6px 40px rgba(0,0,0,.6)">SÍ, 1 KILO.</div></div>
<div style="position:absolute;top:1080px;right:60px;transform:rotate(6deg)"><span class="pill" style="font-size:66px;padding:12px 28px 4px">+6 MESES</span></div>
<div style="position:absolute;top:1470px;left:70px;right:70px;display:flex;flex-wrap:wrap;gap:14px">
 <span class="chip">{gen.icon("clock",34)} 200 porciones de 5 g</span><span class="chip">{gen.icon("award",34)} Micronizada</span><span class="chip">{gen.icon("shield-check",34)} Certificada NSF</span></div>
<div style="position:absolute;top:1620px;left:70px"><span class="pill" style="font-size:76px;padding:14px 36px 4px">PÍDELA POR DM {gen.icon("message-circle",56)}</span></div>
{DONE}</body></html>'''


def post():
    # recorte 4:5 centrado en el tarro: la foto mide 1125x2000; usamos y≈330..1736
    return f'''<html><head><style>{BASE}body{{width:1080px;height:1350px}}</style></head><body>
<div style="position:absolute;inset:0;overflow:hidden"><img src="{FOTO}" style="position:absolute;left:0;top:-170px;width:1080px;height:1920px"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,5,4,.92) 0%,rgba(6,5,4,.6) 18%,rgba(6,5,4,0) 30%,rgba(6,5,4,0) 70%,rgba(6,5,4,.85) 86%,rgba(6,5,4,.97) 100%)"></div>
<div style="position:absolute;top:44px;left:60px">{BR}</div>
<div style="position:absolute;top:140px;left:60px"><div class="big" style="font-size:66px;color:#ddd">¿ES GIGANTE?</div><div class="big o" style="font-size:118px">SÍ, 1 KILO.</div></div>
<div style="position:absolute;top:760px;right:40px;transform:rotate(6deg)"><span class="pill" style="font-size:58px;padding:10px 24px 2px">+6 MESES</span></div>
<div style="position:absolute;bottom:150px;left:60px;right:60px;display:flex;flex-wrap:wrap;gap:12px">
 <span class="chip" style="font-size:26px">{gen.icon("clock",30)} 200 porciones de 5 g</span><span class="chip" style="font-size:26px">{gen.icon("award",30)} Micronizada</span><span class="chip" style="font-size:26px">{gen.icon("shield-check",30)} NSF</span></div>
<div style="position:absolute;bottom:50px;left:60px"><span class="pill" style="font-size:60px;padding:10px 30px 2px">PÍDELA POR DM {gen.icon("message-circle",44)}</span></div>
{DONE}</body></html>'''


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n, h, w, hh in [('historia_finaflex', historia(), 1080, 1920), ('post_finaflex', post(), 1080, 1350)]:
            pg = b.new_page(viewport={'width': w, 'height': hh})
            pg.set_content(gen.sin_emoji(h), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, n + '.png')); print(n); pg.close()
        b.close()
