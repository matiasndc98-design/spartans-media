"""Reel 9:16 (15 s, estilo premium) · sábado 24 oct, cierre de la semana de la proteína: "Checklist del bolso del gym".
Tipo nuevo: CHECKLIST para guardar (distinto del selector del jueves). La lista se va marcando con un check que suena;
los dos últimos ítems traen el producto (shaker con el scoop listo y la barra para la vuelta).
Mejora respecto del anterior: gancho que es una pregunta personal ("¿tienes todo?"), legible desde el cuadro 0,
y la lista completa queda en pantalla al final para que la gente pause o guarde. Sin precios.
Uso (desde kit/build): python3 reel_bolso_gym.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P
import gen

OR = R.OR
HOOK = 2.4
ITEMS = [  # texto, detalle, duración
    ('Agua', '', 1.2),
    ('Toalla', '', 1.2),
    ('Audífonos cargados', '', 1.2),
    ('Candado', '', 1.2),
    ('Shaker listo', 'Con tu scoop de Whey USN · 22 g de proteína', 2.2),
    ('Algo para la vuelta', 'Barra Space Protein XXL · 36% proteína', 2.2),
]
T = []
t = HOOK
for it in ITEMS:
    T.append(t); t += it[2]
TEND = t  # 11,6
R.DUR = TEND + 3.4  # 15,0 s


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}
@keyframes hold{{0%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes show{{0%{{opacity:0}}6%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}10%{{opacity:1}}100%{{opacity:1}}}}
@keyframes inL{{0%{{transform:translateX(-60px);opacity:0}}100%{{transform:translateX(0);opacity:1}}}}
@keyframes tick{{0%{{transform:scale(.3);opacity:0}}60%{{transform:scale(1.15);opacity:1}}100%{{transform:scale(1);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(140px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.4);opacity:0}}40%{{transform:scale(.97);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes pop{{0%{{transform:scale(.6);opacity:0}}60%{{transform:scale(1.05);opacity:1}}100%{{transform:scale(1);opacity:1}}}}
@keyframes dim{{0%{{opacity:1}}100%{{opacity:.35}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.row{{display:flex;align-items:center;gap:28px;min-height:132px}}
.ck{{width:62px;height:62px;border-radius:50%;border:2px solid rgba(244,241,236,.25);flex:none;position:relative}}
.ck i{{position:absolute;inset:-2px;border-radius:50%;background:{OR};display:flex;align-items:center;justify-content:center;color:#0a0a0a}}
.ck svg{{width:40px;height:40px}}
"""


def fondo():
    return ('<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 35% at 50% 52%,rgba(242,106,27,.09),transparent 70%)"></div>'
            f'<div class="floor" style="height:{int(R.H * .32)}px"></div>')


def lista():
    rows = ''
    for k, (txt, det, _d) in enumerate(ITEMS):
        t0 = T[k]
        sub = f'<div class="lab" style="font-size:20px;letter-spacing:4px;color:#bdb8b0;margin-top:6px">{det}</div>' if det else ''
        rows += (f'<div class="row" style="opacity:0;animation:inL .3s ease-out {t0}s both">'
                 f'<div class="ck"><i style="animation:tick .35s ease-out {t0 + .15}s both">{gen.icon("check", 40)}</i></div>'
                 f'<div><div class="big" style="font-size:92px">{txt}</div>{sub}</div></div>')
    return (f'<div style="position:absolute;left:80px;top:440px;width:920px;animation:showEnd .2s linear {HOOK}s both">'
            f'<div class="lab o" style="color:{OR};margin-bottom:24px">Checklist del bolso</div>{rows}</div>')


def body():
    b = fondo() + P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px;color:#F26A1B">Guárdalo</div><div class="prog"><i></i></div>'
    # Gancho: completo desde el cuadro 0 (sin animación de entrada)
    b += f'''<div class="sc" style="animation:hold {HOOK}s linear 0s both">
<div style="position:absolute;left:0;right:0;top:420px;text-align:center">
 <div class="lab">Antes de salir al gym</div>
 <div class="big" style="font-size:230px;margin-top:26px">¿Tienes</div>
 <div class="big o" style="font-size:230px">todo?</div>
</div>{P.heroe('p_shaker.png', 400, 1560, 430, -6)}{P.heroe('p_whey.png', 700, 1570, 480)}</div>'''
    b += lista()
    # Producto de los 2 últimos ítems, a la derecha
    t5, t6 = T[4], T[5]
    b += f'<div class="sc" style="animation:show {ITEMS[4][2]}s linear {t5}s both"><div style="position:absolute;inset:0;animation:rise .5s ease-out {t5 + .1}s both">{P.heroe("p_shaker.png", 640, 1640, 330, -6)}{P.heroe("p_whey.png", 880, 1650, 400)}</div></div>'
    b += (f'<div class="sc" style="animation:show {ITEMS[5][2]}s linear {t6}s both"><div style="position:absolute;inset:0;animation:rise .5s ease-out {t6 + .1}s both">'
          f'<img class="prod" src="{P.I("p_barra.png")}" style="left:470px;top:1380px;width:520px;transform:rotate(-14deg)"></div></div>')
    # Remate: la lista queda arriba atenuada, pregunta abajo
    t = TEND
    b += f'''<div class="sc" style="animation:showEnd {R.DUR - t}s linear {t}s both">
<div style="position:absolute;left:0;right:0;top:1300px;text-align:center">
 <div class="big" style="font-size:130px;animation:slam .45s ease-out {t}s both">¿Qué se te<br><span class="o">olvida siempre?</span></div>
 <div class="lab" style="color:#e8e4dd;margin-top:22px;animation:pop .4s ease-out {t + .6}s both">Coméntalo <span class="o">·</span> Guárdalo antes de salir</div>
 <div style="margin-top:26px;font-weight:600;font-size:24px;letter-spacing:5px;text-transform:uppercase;color:#9a958e;animation:pop .4s ease-out {t + 1}s both">Pídelo por DM · Con creatina, shaker de regalo</div>
</div></div>'''
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
