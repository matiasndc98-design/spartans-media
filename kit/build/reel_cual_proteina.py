"""Reel 9:16 (15 s, estilo premium) · jueves 22 oct, semana de la proteína: "¿Qué proteína es para ti?".
Tipo: comparativa de producto en formato SELECTOR ("si buscas X -> esta"), distinto al humor del martes.
Mejora respecto del anterior: barra-selector fija abajo con las 4 opciones que se van encendiendo (el espectador
sabe cuántas faltan) y remate que pide comentar el número. Gancho completo desde el cuadro 0. Sin precios.
Uso (desde kit/build): python3 reel_cual_proteina.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
HOOK, STEP = 2.4, 2.5
OPC = [  # imagen, si buscas..., nombre, dato
    ('p_whey.png', 'Si quieres<br>lo clásico.', 'Whey USN · chocolate', '22 g de proteína por scoop'),
    ('p_iso100.png', 'Si buscas<br>menos lactosa.', 'ISO 100 · Dymatize', '25 g · whey isolate hidrolizada'),
    ('p_nitro.png', 'Si quieres<br>2 en 1.', 'Nitro Tech · MuscleTech', '30 g de proteína + 3 g de creatina'),
    ('p_barra.png', 'Si la quieres<br>al paso.', 'Barra Space Protein XXL', '36% proteína · 3 g de azúcar'),
]
TEND = HOOK + STEP * len(OPC)
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
@keyframes slam{{0%{{transform:scale(1.4);opacity:0}}40%{{transform:scale(.97);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(140px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes pop{{0%{{transform:scale(.6);opacity:0}}60%{{transform:scale(1.05);opacity:1}}100%{{transform:scale(1);opacity:1}}}}
@keyframes on{{0%{{opacity:.28}}8%,92%{{opacity:1}}100%{{opacity:.28}}}}
@keyframes ul{{0%{{width:0}}8%,92%{{width:100%}}100%{{width:0}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.sel{{position:absolute;left:110px;right:110px;top:1530px;display:flex;justify-content:space-between;z-index:8}}
.sel .it{{width:170px;text-align:center;opacity:.28}}
.sel .im{{height:96px;display:flex;align-items:flex-end;justify-content:center}}
.sel .im img{{max-height:96px;max-width:150px;filter:drop-shadow(0 10px 10px rgba(0,0,0,.7))}}
.sel .n{{font-family:Bebas;font-size:34px;margin-top:8px}}
.sel .u{{height:3px;background:{OR};width:0;margin:4px auto 0}}
"""


def fondo():
    return ('<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 35% at 50% 52%,rgba(242,106,27,.09),transparent 70%)"></div>'
            f'<div class="floor" style="height:{int(R.H * .32)}px"></div>')


def selector():
    its = ''
    for k, (img, *_rest) in enumerate(OPC):
        t = HOOK + k * STEP
        its += (f'<div class="it" style="animation:on {STEP}s linear {t}s both"><div class="im"><img src="{P.I(img)}"></div>'
                f'<div class="n">{k + 1}</div><div class="u" style="animation:ul {STEP}s linear {t}s both"></div></div>')
    return f'<div class="sel" style="animation:hold {TEND + .3}s linear 0s both">{its}</div>'


def opcion(k, img, si, nombre, dato):
    t = HOOK + k * STEP
    prod = (P.heroe(img, 540, 1360, 250) if img == 'p_barra.png' else P.heroe(img, 540, 1370, 680))
    return f'''<div class="sc" style="animation:show {STEP}s linear {t}s both">
<div style="position:absolute;left:80px;right:80px;top:380px">
 <div class="lab" style="color:{OR};animation:inL .3s ease-out {t}s both">Opción {k + 1}</div>
 <div class="big" style="font-size:150px;margin-top:20px;transform-origin:left center;animation:slam .45s ease-out {t + .05}s both">{si}</div>
</div>
<div style="position:absolute;inset:0;animation:rise .5s ease-out {t + .25}s both">{prod}</div>
<div style="position:absolute;left:0;right:0;top:1395px;text-align:center;animation:pop .4s ease-out {t + .6}s both">
 <div class="big o" style="font-size:66px">{nombre}</div>
 <div class="lab" style="color:#e8e4dd;margin-top:10px;letter-spacing:4px">{dato}</div>
</div></div>'''


def body():
    b = fondo() + P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px;color:#F26A1B">Semana de la proteína</div><div class="prog"><i></i></div>'
    # Gancho: visible completo desde el cuadro 0 (sin animación de entrada)
    fila = (P.heroe('p_iso100.png', 280, 1380, 330) + P.heroe('p_whey.png', 540, 1400, 370) + P.heroe('p_nitro.png', 800, 1380, 330))
    b += f'''<div class="sc" style="animation:hold {HOOK}s linear 0s both">
<div style="position:absolute;left:0;right:0;top:400px;text-align:center">
 <div class="lab">4 opciones · elige la tuya</div>
 <div class="big" style="font-size:190px;margin-top:26px">¿Qué proteína</div>
 <div class="big o" style="font-size:190px">es para ti?</div>
</div>{fila}</div>'''
    for k, o in enumerate(OPC):
        b += opcion(k, *o)
    t = TEND
    fila2 = (P.heroe('p_iso100.png', 250, 1330, 300) + P.heroe('p_whey.png', 450, 1350, 340) + P.heroe('p_nitro.png', 650, 1330, 300))
    b += f'''<div class="sc" style="animation:showEnd {R.DUR - t}s linear {t}s both">
<div style="position:absolute;left:0;right:0;top:390px;text-align:center">
 <div class="lab" style="animation:showEnd .3s linear {t}s both">Tu turno</div>
 <div class="big" style="font-size:170px;margin-top:24px;animation:slam .45s ease-out {t}s both">¿Cuál eres?</div>
 <div class="big o" style="font-size:130px;margin-top:10px;animation:slam .45s ease-out {t + .35}s both">Comenta 1, 2, 3 o 4</div>
</div>
<div style="position:absolute;inset:0;animation:rise .6s ease-out {t + .3}s both">{fila2}
 <img class="prod" src="{P.I('p_barra.png')}" style="left:640px;top:1180px;width:330px;transform:rotate(-14deg)"></div>
<div style="position:absolute;left:0;right:0;top:1440px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase;animation:pop .45s ease-out {t + 1}s both">Pídela por DM <span class="o">·</span> Con creatina, shaker de regalo</div>
</div>'''
    return b + selector() + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
