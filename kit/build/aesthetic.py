"""Pieza AESTHETIC tipo editorial (fondo papel beige, tipografía negra, acento naranjo): frases espartanas con contexto.
Uso (desde kit/build): python3 aesthetic.py <salida.jpg>
"""
import sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else 'aesthetic.jpg'
sys.argv = [sys.argv[0]]
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright

OR = '#E2601A'
LOGO_SVG = open(os.path.join(gen.B, '..', '..', 'Logo', 'logo_spartans.svg')).read()
logo_negro = 'data:image/svg+xml;base64,' + __import__('base64').b64encode(LOGO_SVG.replace('#F26A1B', '#151311').encode()).decode()

CSS = gen.FONTS + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#e9e2d6;color:#151311;font-family:Barlow;overflow:hidden;position:relative}
.paper{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(255,255,255,.55),rgba(0,0,0,.08) 85%)}
.grain{position:absolute;inset:0;opacity:.16;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter><rect width='240' height='240' filter='url(%23n)'/></svg>")}
.h{font-family:Bebas;line-height:.86;text-transform:uppercase}
.lab{font-weight:700;font-size:22px;letter-spacing:8px;text-transform:uppercase;color:#6d665c}
"""


def molon_labe():
    return f'''<html><head><style>{CSS}</style></head><body><div class="paper"></div>
<div style="position:absolute;left:0;right:0;top:80px;display:flex;justify-content:space-between;padding:0 80px" class="lab"><span>Spartans</span><span>Termópilas · 480 a.C.</span></div>
<div style="position:absolute;left:0;right:0;top:210px;display:flex;justify-content:center"><img src="{logo_negro}" style="width:250px;opacity:.92"></div>
<div style="position:absolute;left:0;right:0;top:500px;text-align:center">
 <div style="font-family:serif;font-size:58px;letter-spacing:14px;color:#6d665c">ΜΟΛΩΝ ΛΑΒΕ</div>
 <div class="h" style="font-size:230px;margin-top:14px">Molon labe.</div>
 <div class="h" style="font-size:86px;color:{OR};margin-top:6px">"Ven a buscarlas."</div></div>
<div style="position:absolute;left:90px;right:90px;top:960px;text-align:center;font-size:36px;line-height:1.35;font-weight:500;color:#2a2622">
 Lo respondió Leónidas cuando le exigieron entregar las armas.<br><b style="color:#151311">Tú lo respondes cada vez que no te saltas el gym.</b></div>
<div style="position:absolute;left:80px;right:80px;bottom:80px;display:flex;justify-content:space-between;align-items:center" class="lab">
 <span>Disciplina</span><span style="flex:1;height:2px;background:#151311;margin:0 30px;opacity:.6"></span><span>Caldera · Chile</span></div>
<div class="grain"></div><script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script></body></html>'''


if __name__ == '__main__':
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        pg.set_content(gen.sin_emoji(molon_labe()), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
        png = OUT[:-4] + '.png'; pg.screenshot(path=png); b.close()
    from PIL import Image
    Image.open(png).convert('RGB').save(OUT, quality=92); os.remove(png); print(OUT)
