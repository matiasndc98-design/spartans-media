"""Reel de humor 9:16 (15 s, estilo premium): "Diccionario del gym: lo que dice vs lo que significa".
Tipo nuevo: humor identificable (después de la lista de errores). Gancho legible completo desde el cuadro 0 (sin animación de entrada).
Remate con producto: "Mi batido" -> "Mi personalidad" + Whey USN (22 g por scoop).
Uso (desde kit/build): python3 reel_diccionario_gym.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P
import gen

OR = R.OR
HOOK, STEP = 2.4, 2.5
FRASES = [
    ('“Una serie más.”', 'Cuatro series más.'),
    ('“Solo voy a calentar.”', 'Me quedé dos horas.'),
    ('“Hoy entreno liviano.”', 'Hoy converso harto.'),
    ('“Mañana empiezo la dieta.”', 'Pasé por un completo.'),
]
TEND = HOOK + STEP * len(FRASES)
R.DUR = TEND + 2.6  # 15,0 s


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}
@keyframes show{{0%{{opacity:0}}5%{{opacity:1}}95%{{opacity:1}}100%{{opacity:0}}}}
@keyframes hold{{0%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}10%{{opacity:1}}100%{{opacity:1}}}}
@keyframes inL{{0%{{transform:translateX(-60px);opacity:0}}100%{{transform:translateX(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.5);opacity:0}}40%{{transform:scale(.97);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(120px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes pop{{0%{{transform:scale(.6);opacity:0}}60%{{transform:scale(1.05);opacity:1}}100%{{transform:scale(1);opacity:1}}}}
@keyframes ln{{0%{{width:0}}100%{{width:120px}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
"""


def fondo():
    return ('<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 35% at 50% 55%,rgba(242,106,27,.09),transparent 70%)"></div>'
            f'<div class="floor" style="height:{int(R.H * .3)}px"></div>')


def entrada(t, dice, sig):
    return f'''<div class="sc" style="animation:show {STEP}s linear {t}s both">
<div style="position:absolute;left:80px;right:80px;top:470px">
 <div class="lab" style="animation:inL .35s ease-out {t}s both">Lo que dice</div>
 <div class="big" style="font-size:150px;margin-top:26px;animation:inL .4s ease-out {t + .05}s both">{dice}</div>
 <div style="height:3px;background:{OR};margin:60px 0 40px;animation:ln .4s ease-out {t + .8}s both"></div>
 <div class="lab" style="color:{OR};animation:showEnd .3s linear {t + .85}s both">Lo que significa</div>
 <div class="big o" style="font-size:190px;margin-top:26px;transform-origin:left center;animation:slam .5s ease-out {t + .9}s both">{sig}</div>
</div></div>'''


def body():
    b = fondo() + P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px;color:#F26A1B">Diccionario del gym</div><div class="prog"><i></i></div>'
    # Gancho: visible completo desde el cuadro 0
    b += f'''<div class="sc" style="animation:hold {HOOK}s linear 0s both">
<div style="position:absolute;left:80px;right:80px;top:470px">
 <div class="lab">Diccionario del gym</div>
 <div class="big" style="font-size:220px;margin-top:30px">Lo que dice</div>
 <div class="big" style="font-size:110px;color:#8d8880;margin:14px 0">vs</div>
 <div class="big o" style="font-size:220px">lo que significa.</div>
 <div style="font-size:44px;color:#bdb8b0;margin-top:50px;font-weight:500">¿Cuál eres tú?</div>
</div></div>'''
    for k, (d, s) in enumerate(FRASES):
        b += entrada(HOOK + k * STEP, d, s)
    t = TEND
    b += f'''<div class="sc" style="animation:showEnd {R.DUR - t}s linear {t}s both">
<div style="position:absolute;left:80px;right:80px;top:400px">
 <div class="lab" style="animation:inL .35s ease-out {t}s both">Lo que dice</div>
 <div class="big" style="font-size:150px;margin-top:22px;animation:inL .4s ease-out {t + .05}s both">“Mi batido.”</div>
 <div style="height:3px;background:{OR};margin:46px 0 34px;animation:ln .4s ease-out {t + .6}s both"></div>
 <div class="lab" style="color:{OR};animation:showEnd .3s linear {t + .65}s both">Lo que significa</div>
 <div class="big o" style="font-size:170px;margin-top:22px;transform-origin:left center;animation:slam .5s ease-out {t + .7}s both">Mi personalidad.</div>
</div>
<div style="position:absolute;inset:0;animation:rise .6s ease-out {t + .2}s both">{P.heroe('p_whey.png', 790, 1530, 470)}</div>
<div style="position:absolute;left:80px;top:1260px;width:360px;animation:showEnd .4s linear {t + 1.1}s both"><div class="big" style="font-size:96px">22 g</div><div class="lab" style="margin-top:8px;line-height:1.5">de proteína por scoop · Whey USN</div></div>
<div style="position:absolute;left:0;right:0;top:1560px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase;animation:pop .45s ease-out {t + 1.4}s both">Comenta la tuya <span class="o">·</span> Pídela por DM</div>
</div>'''
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
