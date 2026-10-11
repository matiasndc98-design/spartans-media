"""Reel animado 9:16 (1080x1920, 30 fps) con animaciones CSS renderizadas cuadro a cuadro.
Uso (desde kit/build): python3 reel.py <salida.mp4>
Escenas: gancho "LLEGÓ ALGO NUEVO" -> un producto por escena con su dato clave (sin precio) -> cierre con todos y llamado al DM.
Sin música: el dueño la agrega en Instagram (publicar con autoPublish false).
"""
import sys, os, subprocess, tempfile, shutil
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright

OUT = sys.argv[1]
OR = '#F26A1B'
W, H, FPS = 1080, 1920, 30
I = lambda n: gen.uri(os.path.join(gen.B, n))

PRODS = [  # imagen, nombre, detalle, dato destacado (sin precios: decisión del dueño)
    ('p_iso100.png', 'ISO 100', 'Dymatize · 5 lb · Cocoa Pebbles', '25 G PROTEÍNA'),
    ('p_nitro.png', 'NITRO TECH', 'MuscleTech · 4 lb · vainilla', '30 G PROTEÍNA'),
    ('p_finaflex.png', 'CREATINA 1 KG', 'Finaflex · micronizada · NSF', '200 PORCIONES'),
    ('p_omega.png', 'OMEGA 3', 'USN · 90 cápsulas blandas', '1000 MG'),
    ('p_guarana.png', 'GUARANÁ SHOT', 'OstroVit · 80 ml · sabor pera', '200 MG CAFEÍNA'),
    ('p_barra.png', 'BARRA XXL', 'Space Protein · 80 g · coco', '36% PROTEÍNA'),
]
T0, STEP = 2.6, 2.5          # inicio de productos y duración de cada uno
TEND = T0 + STEP * len(PRODS)  # inicio del cierre
DUR = TEND + 3.6

FX = (gen.FX.replace('height="1350"', 'height="1920"').replace('1080,1350', '1080,1920').replace('780,1350', '540,1900')
      .replace('780,1300', '540,1500').replace('y=500+r()*850', 'y=200+r()*1720').replace('y=r()*1350', 'y=r()*1920').replace('(x-790)/320', '(x-540)/600'))


def scene_css():
    css = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.big{{font-family:Bebas;line-height:.9;text-transform:uppercase}}.o{{color:{OR}}}
.brand{{position:absolute;top:190px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;z-index:9}}
.brand img{{height:62px}}.brand div{{font-family:Bebas;font-size:46px;letter-spacing:2px;line-height:.9}}
.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:20px;letter-spacing:5px;color:#bbb}}
.sc{{position:absolute;inset:0;opacity:0}}
.glow{{position:absolute;left:90px;top:620px;width:900px;height:900px;border-radius:50%;background:radial-gradient(closest-side,rgba(242,106,27,.65),rgba(160,50,0,.2) 55%,transparent);filter:blur(10px)}}
.flash{{position:absolute;inset:0;background:{OR};opacity:0;pointer-events:none;z-index:20}}
@keyframes show{{0%{{opacity:0}}6%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}12%{{opacity:1}}100%{{opacity:1}}}}
@keyframes slam{{0%{{transform:scale(2.4);opacity:0}}35%{{transform:scale(.95);opacity:1}}50%{{transform:scale(1.03)}}65%,100%{{transform:scale(1)}}}}
@keyframes rise{{0%{{transform:translateY(260px) scale(.85);opacity:0}}30%{{transform:translateY(-14px) scale(1.02);opacity:1}}45%,100%{{transform:translateY(0) scale(1);opacity:1}}}}
@keyframes drift{{0%{{transform:translateY(0) scale(1)}}100%{{transform:translateY(-18px) scale(1.04)}}}}
@keyframes inL{{0%{{transform:translateX(-120%)}}40%,100%{{transform:translateX(0)}}}}
@keyframes pop{{0%{{transform:scale(0) rotate(-8deg)}}55%{{transform:scale(1.15) rotate(-3deg)}}75%,100%{{transform:scale(1) rotate(-3deg)}}}}
@keyframes flash{{0%{{opacity:.55}}100%{{opacity:0}}}}
@keyframes pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.06)}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:290px;height:6px;background:rgba(255,255,255,.12);border-radius:3px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};border-radius:3px;box-shadow:0 0 12px {OR};animation:bar {DUR}s linear both}}
"""
    return css


def body():
    b = f'{FX.replace("SEED", "3131")}<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div><div class="prog"><i></i></div>'
    # Escena 0: gancho
    sil = ''.join(f'<img src="{I(p[0])}" style="height:{h}px;margin:0 -14px;filter:brightness(0) drop-shadow(0 0 3px {OR}) drop-shadow(0 0 24px rgba(242,106,27,.9))">'
                  for p, h in zip(PRODS[:5], [330, 350, 340, 310, 320]))
    b += f'''<div class="sc" style="animation:show {T0}s linear 0s both"><div class="glow"></div>
<div style="position:absolute;top:470px;left:0;right:0;text-align:center;animation:slam .9s ease-out .1s both"><div class="big" style="font-size:200px">LLEGÓ</div></div>
<div style="position:absolute;top:660px;left:0;right:0;text-align:center;animation:slam .9s ease-out .55s both"><div class="big o" style="font-size:190px;text-shadow:0 0 40px rgba(242,106,27,.6)">ALGO NUEVO</div></div>
<div style="position:absolute;top:1000px;left:0;right:0;height:380px;display:flex;align-items:flex-end;justify-content:center;animation:rise 1.2s ease-out 1s both">{sil}</div>
<div class="big" style="position:absolute;top:1470px;left:0;right:0;text-align:center;font-size:64px;animation:pulse 1s ease-in-out 1.4s 2 both">👀 MIRA</div></div>'''
    # Escenas de producto
    for k, (img, name, det, tag) in enumerate(PRODS):
        t = T0 + k * STEP
        wide = img == 'p_barra.png'
        ims = 'width:940px' if wide else 'height:760px'
        note = ('<div style="position:absolute;top:1620px;left:70px;right:70px;text-align:center;font-size:24px;color:#aaa">Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.</div>' if img == 'p_guarana.png' else '')
        b += f'''<div class="flash" style="animation:flash .35s ease-out {t}s forwards"></div>
<div class="sc" style="animation:show {STEP}s linear {t}s both"><div class="glow"></div>
<div class="big" style="position:absolute;top:360px;left:70px;font-size:54px;color:#888">{k + 1:02d}/{len(PRODS):02d} · NUEVO</div>
<div style="position:absolute;top:440px;left:70px;right:70px;overflow:hidden"><div class="big" style="font-size:150px;animation:inL .5s cubic-bezier(.2,.8,.2,1) {t + .05}s both">{name}</div></div>
<div style="position:absolute;top:590px;left:70px;font-weight:700;font-size:36px;text-transform:uppercase;color:#ddd;animation:inL .5s ease-out {t + .15}s both">{det}</div>
<div style="position:absolute;top:700px;left:0;right:0;height:820px;display:flex;align-items:center;justify-content:center;animation:rise .8s ease-out {t + .1}s both">
 <img src="{I(img)}" style="{ims};filter:drop-shadow(0 34px 30px #000);animation:drift {STEP}s ease-in-out {t}s both"></div>
<div style="position:absolute;top:1430px;left:0;right:0;text-align:center;animation:pop .55s ease-out {t + .45}s both">
 <span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:110px;padding:14px 46px 0;border-radius:18px;box-shadow:0 0 50px rgba(242,106,27,.6)">{tag}</span></div>{note}</div>'''
    # Cierre
    grid = ''.join(f'<div style="display:flex;align-items:flex-end;justify-content:center;height:300px;animation:rise .7s ease-out {TEND + .1 + k * .08}s both">'
                   f'<img src="{I(p[0])}" style="{"width:290px;transform:rotate(-10deg)" if p[0] == "p_barra.png" else "max-height:290px;max-width:280px"};filter:drop-shadow(0 18px 14px #000)"></div>'
                   for k, p in enumerate(PRODS))
    b += f'''<div class="flash" style="animation:flash .35s ease-out {TEND}s forwards"></div>
<div class="sc" style="animation:showEnd {DUR - TEND}s linear {TEND}s both"><div class="glow" style="top:560px"></div>
<div class="big" style="position:absolute;top:360px;left:0;right:0;text-align:center;font-size:120px;animation:slam .8s ease-out {TEND}s both">6 NUEVOS EN <span class="o">SPARTANS</span></div>
<div style="position:absolute;top:560px;left:60px;right:60px;display:grid;grid-template-columns:repeat(3,1fr);gap:30px 10px">{grid}</div>
<div style="position:absolute;top:1300px;left:0;right:0;text-align:center;animation:pop .6s ease-out {TEND + .9}s both">
 <span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:96px;padding:14px 44px 0;border-radius:18px;box-shadow:0 0 50px rgba(242,106,27,.6)">PÍDELO POR DM 📩</span></div>
<div style="position:absolute;top:1480px;left:0;right:0;text-align:center;font-weight:700;font-size:34px;letter-spacing:1px;color:#ddd;animation:showEnd 1s linear {TEND + 1.3}s both">DELIVERY EN CALDERA $1.500 · ENVÍOS A TODO CHILE</div>
<div style="position:absolute;top:1540px;left:70px;right:70px;text-align:center;font-size:22px;color:#999;animation:showEnd 1s linear {TEND + 1.3}s both">Guaraná Shot contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.</div></div>'''
    return b


def main():
    html = f'<html><head><style>{scene_css()}</style></head><body>{body()}<script>document.fonts.ready.then(()=>{{document.getAnimations().forEach(a=>a.pause());document.body.dataset.ok=1}})</script></body></html>'
    tmp = tempfile.mkdtemp()
    n = int(DUR * FPS)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
        pg.set_content(html, wait_until='load'); pg.wait_for_selector('body[data-ok]')
        for f in range(n):
            pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={f * 1000 / FPS}}})')
            pg.screenshot(path=os.path.join(tmp, f'{f:05d}.jpg'), type='jpeg', quality=92)
        b.close()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(tmp, '%05d.jpg'),
                    '-f', 'lavfi', '-t', str(DUR), '-i', 'anullsrc=r=44100:cl=stereo',
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '19', '-preset', 'medium',
                    '-c:a', 'aac', '-shortest', '-movflags', '+faststart', OUT], check=True)
    shutil.rmtree(tmp)
    print(OUT, round(DUR, 1), 's')


if __name__ == '__main__':
    main()
