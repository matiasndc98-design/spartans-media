"""Reel listicle 9:16: 3 errores con la creatina (formato para guardar).
Uso (desde kit/build): python3 reel_errores_creatina.py <salida.mp4>
Respaldo: ISSN (Kreider et al. 2017): 3-5 g/día bastan para mantener; sin carga, saturación en ~3-4 semanas;
la creatina mejora la capacidad de entrenar, no reemplaza el entrenamiento.
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import gen

OR = R.OR
I = R.I
RED = '#e5372c'
STEP = 4.2
T0 = 2.6
ERR = [('TOMAR MÁS DE LA CUENTA', 'Con 3 a 5 g al día basta. Más no es mejor: el exceso se elimina.', 'scale'),
       ('ESPERAR RESULTADOS EN 3 DÍAS', 'Sin fase de carga, tus reservas se llenan en 3 a 4 semanas. La clave es la constancia.', 'calendar'),
       ('TOMARLA Y NO ENTRENAR', 'La creatina te ayuda a rendir más en el gym. No reemplaza el entrenamiento.', 'barbell')]
TEND = T0 + STEP * len(ERR)
R.DUR = TEND + 3.4
EXTRA = ('<style>@keyframes strike{0%{transform:scaleX(0)}100%{transform:scaleX(1)}}'
         '@keyframes stamp{0%{transform:scale(3) rotate(-14deg);opacity:0}40%{transform:scale(.9) rotate(-8deg);opacity:1}60%,100%{transform:scale(1) rotate(-8deg);opacity:1}}</style>')


def body():
    b = EXTRA + f'{R.FX.replace("SEED", "9191")}<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div><div class="prog"><i></i></div>'
    # gancho
    b += f'''<div class="sc" style="animation:show {T0}s linear 0s both"><div class="glow"></div>
<div style="position:absolute;top:470px;left:0;right:0;text-align:center;animation:slam .8s ease-out .05s both"><div class="big o" style="font-size:420px;line-height:.8;text-shadow:0 0 60px rgba(242,106,27,.6)">3</div></div>
<div style="position:absolute;top:830px;left:0;right:0;text-align:center;animation:slam .8s ease-out .4s both"><div class="big" style="font-size:150px">ERRORES</div><div class="big" style="font-size:110px">CON LA CREATINA</div></div>
<div class="big" style="position:absolute;top:1260px;left:0;right:0;text-align:center;font-size:66px;color:#ddd;animation:pulse 1s ease-in-out 1.3s 1 both">¿COMETES ALGUNO? 👀</div></div>'''
    for k, (err, fix, ic) in enumerate(ERR):
        t = T0 + k * STEP
        b += f'''<div class="flash" style="animation:flash .35s ease-out {t}s forwards"></div>
<div class="sc" style="animation:show {STEP}s linear {t}s both"><div class="glow" style="top:760px"></div>
<div class="big" style="position:absolute;top:360px;left:70px;font-size:64px;color:{RED};animation:inL .4s ease-out {t + .05}s both">ERROR #{k + 1}</div>
<div style="position:absolute;top:450px;left:70px;right:70px;animation:inL .5s ease-out {t + .15}s both"><div class="big" style="font-size:118px;position:relative;display:inline">{err}</div></div>
<div style="position:absolute;top:700px;left:70px;color:{RED};animation:stamp .5s ease-out {t + .9}s both;z-index:3">
 <span class="big" style="display:inline-block;border:8px solid {RED};border-radius:14px;padding:10px 26px 0;font-size:96px;background:rgba(6,5,4,.55)">✕ ERROR</span></div>
<div style="position:absolute;top:880px;left:60px;right:60px;border:2px solid rgba(242,106,27,.7);background:rgba(16,11,8,.92);border-radius:26px;padding:40px 44px;animation:rise .6s ease-out {t + 1.5}s both">
 <div style="display:flex;align-items:center;gap:18px;color:#3ccf6e">{gen.icon("check", 64)}<span class="big" style="font-size:66px;color:#3ccf6e">HAZ ESTO</span></div>
 <div style="font-weight:700;font-size:50px;line-height:1.18;text-transform:uppercase;color:#f2f2f2;margin-top:14px">{fix}</div></div>
<div style="position:absolute;top:1330px;left:0;right:0;display:flex;justify-content:center;color:{OR};opacity:.9;animation:pop .5s ease-out {t + 2.1}s both">{gen.icon(ic, 150)}</div></div>'''
    # cierre
    row = ''.join(f'<img src="{I(p)}" style="height:{h}px;margin:0 4px;filter:drop-shadow(0 20px 16px #000)">'
                  for p, h in zip(['p_usn_crea.png', 'p_mt_sin.png', 'p_finaflex.png'], [280, 300, 320]))
    b += f'''<div class="flash" style="animation:flash .35s ease-out {TEND}s forwards"></div>
<div class="sc" style="animation:showEnd {R.DUR - TEND}s linear {TEND}s both"><div class="glow"></div>
<div style="position:absolute;top:400px;left:70px;right:70px;animation:inL .5s ease-out {TEND + .05}s both"><div class="big" style="font-size:110px">GUÁRDALO 📌</div><div class="big o" style="font-size:96px">Y MÁNDASELO A TU</div><div class="big o" style="font-size:96px">YUNTA DEL GYM</div></div>
<div style="position:absolute;top:870px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;animation:rise .7s ease-out {TEND + .5}s both">{row}</div>
<div style="position:absolute;top:1260px;left:0;right:0;text-align:center;animation:pop .6s ease-out {TEND + 1.1}s both">
 <span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:80px;padding:14px 40px 0;border-radius:18px;box-shadow:0 0 50px rgba(242,106,27,.6)">¿DUDAS? ESCRÍBENOS 📩</span></div>
<div style="position:absolute;top:1420px;left:0;right:0;text-align:center;font-size:24px;color:#999">Referencia: Sociedad Internacional de Nutrición Deportiva (ISSN)</div></div>'''
    return b


R.body = body
if __name__ == '__main__':
    R.main()
