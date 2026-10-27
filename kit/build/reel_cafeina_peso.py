"""Reel 9:16 (~15,5 s, estilo premium) · martes 27 oct, semana de la energía: "¿Cuánta cafeína según tu peso?"
Tipo: educativo con cálculo (el que más le gustó al dueño), distinto del anterior (checklist del bolso).
Idea nueva: TABLA "BUSCA TU PESO" para guardar (50 a 90 kg → mg a 3 mg/kg) que queda completa en pantalla
para pausar; remate "comenta tu peso". Gancho legible desde el cuadro 0, sin animación de entrada.
Respaldo: ISSN Position Stand caffeine (Guest et al. 2021): 3–6 mg/kg, 30–60 min antes; EFSA 2015: hasta 400 mg/día
en adultos sanos (no embarazadas). Sin precios.
Uso (desde kit/build): python3 reel_cafeina_peso.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
HOOK, DATO, TABLA, CUENTA = 2.6, 2.8, 4.4, 2.8
T1 = HOOK
T2 = T1 + DATO
T3 = T2 + TABLA
TEND = T3 + CUENTA  # 12,6
R.DUR = TEND + 3.0  # 15,6 s
GUA = 'Guaraná Shot: contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'
FILAS = [(50, 150), (60, 180), (70, 210), (80, 240), (90, 270)]


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}
@keyframes hold{{0%{{opacity:1}}95%{{opacity:1}}100%{{opacity:0}}}}
@keyframes show{{0%{{opacity:0}}5%{{opacity:1}}95%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}10%{{opacity:1}}100%{{opacity:1}}}}
@keyframes inL{{0%{{transform:translateX(-60px);opacity:0}}100%{{transform:translateX(0);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(140px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.4);opacity:0}}40%{{transform:scale(.97);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes pop{{0%{{transform:scale(.6);opacity:0}}60%{{transform:scale(1.05);opacity:1}}100%{{transform:scale(1);opacity:1}}}}
@keyframes gx{{0%{{width:0}}100%{{width:var(--w)}}}}
@keyframes hi{{0%{{background:transparent}}100%{{background:rgba(242,106,27,.16)}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.fila{{display:flex;align-items:center;height:118px;padding:0 26px;border-radius:14px;border-bottom:1px solid rgba(244,241,236,.08)}}
.nota{{position:absolute;left:80px;right:80px;font-weight:600;font-size:19px;letter-spacing:2px;text-transform:uppercase;color:#8d8880;line-height:1.5}}
"""


def fondo():
    return ('<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 35% at 50% 52%,rgba(242,106,27,.09),transparent 70%)"></div>'
            f'<div class="floor" style="height:{int(R.H * .32)}px"></div>')


def body():
    b = fondo() + P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px;color:#F26A1B">Guárdalo</div><div class="prog"><i></i></div>'
    # 1 · Gancho completo desde el cuadro 0
    b += f'''<div class="sc" style="animation:hold {HOOK}s linear 0s both">
<div style="position:absolute;left:80px;right:80px;top:400px">
 <div class="lab">Antes de entrenar</div>
 <div class="big" style="font-size:170px;margin-top:26px">¿Cuánta cafeína</div>
 <div class="big o" style="font-size:170px">según tu peso?</div>
</div>{P.heroe('p_guarana.png', 540, 1600, 560)}</div>'''
    # 2 · El dato con fuente
    t = T1
    b += f'''<div class="sc" style="animation:show {DATO}s linear {t}s both">
<div style="position:absolute;left:80px;right:80px;top:430px">
 <div class="lab" style="animation:inL .3s ease-out {t}s both">Lo que dice la ciencia</div>
 <div class="big o" style="font-size:330px;margin-top:20px;animation:slam .45s ease-out {t + .1}s both">3 mg</div>
 <div class="big" style="font-size:150px;animation:inL .35s ease-out {t + .45}s both">por kilo</div>
 <div class="rule" style="margin:46px 0 30px;width:120px"></div>
 <div style="font-size:46px;line-height:1.25;font-weight:500;color:#e8e4dd;animation:pop .35s ease-out {t + .9}s both">Para partir. Tómala 30 a 60 minutos antes de entrenar.</div>
</div>
<div class="nota" style="bottom:300px">Rango estudiado: 3 a 6 mg por kilo · ISSN, 2021</div></div>'''
    # 3 · Tabla "busca tu peso"
    t = T2
    rows = ''
    for k, (kg, mg) in enumerate(FILAS):
        tk = t + .35 + k * .32
        hl = f';animation:inL .25s ease-out {tk}s both' + (f',hi .3s ease-out {t + 2.6}s both' if kg == 70 else '')
        w = int(mg / 270 * 300)
        rows += (f'<div class="fila" style="opacity:0{hl}">'
                 f'<div class="big" style="font-size:84px;width:260px">{kg} kg</div>'
                 f'<div style="flex:1;height:10px;margin-right:34px"><div style="height:10px;border-radius:5px;background:{OR};--w:{w}px;animation:gx .3s ease-out {tk + .1}s both"></div></div>'
                 f'<div class="big {"o" if kg == 70 else ""}" style="font-size:84px;width:240px;text-align:right">{mg} mg</div></div>')
    b += f'''<div class="sc" style="animation:showEnd .2s linear {t}s both">
<div style="position:absolute;left:70px;right:70px;top:400px">
 <div class="lab" style="color:{OR}">Busca tu peso</div>
 <div class="big" style="font-size:120px;margin:16px 0 30px">Tu dosis para partir</div>
 {rows}
</div></div>'''
    # 4 · La cuenta: 70 kg ≈ 1 shot (debajo de la tabla, que queda en pantalla)
    t = T3
    b += f'''<div class="sc" style="animation:show {CUENTA}s linear {t}s both">
<div style="position:absolute;left:80px;right:80px;top:1250px">
 <div class="big" style="font-size:96px;animation:slam .4s ease-out {t}s both">70 kg ≈ <span class="o">1 Guaraná Shot</span></div>
 <div style="font-size:38px;line-height:1.3;font-weight:500;color:#e8e4dd;margin-top:18px;animation:pop .35s ease-out {t + .6}s both">200 mg por shot. Más no es mejor: tope del día 400 mg, sumando el café.</div>
 <div class="nota" style="position:static;margin-top:18px;animation:pop .35s ease-out {t + .9}s both">EFSA, 2015 · adultos sanos</div>
</div></div>'''
    # 5 · Remate
    t = TEND
    b += f'''<div class="sc" style="animation:showEnd {R.DUR - t}s linear {t}s both">
<div style="position:absolute;left:80px;right:80px;top:1240px">
 <div class="big" style="font-size:130px;animation:slam .45s ease-out {t}s both">¿Cuánto <span class="o">pesas tú?</span></div>
 <div class="lab" style="color:#e8e4dd;margin-top:20px;animation:pop .4s ease-out {t + .5}s both">Coméntalo <span class="o">·</span> Guárdalo para tu próximo entreno</div>
 <div style="margin-top:18px;font-weight:600;font-size:24px;letter-spacing:5px;text-transform:uppercase;color:#9a958e;animation:pop .4s ease-out {t + .8}s both">Guaraná Shot · Pídelo por DM</div>
</div>
<div class="nota" style="bottom:300px;animation:pop .4s ease-out {t + .8}s both">{GUA}</div></div>'''
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
