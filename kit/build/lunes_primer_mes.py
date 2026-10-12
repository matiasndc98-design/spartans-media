"""Lunes 12 oct 2026 · semana de la creatina.
Carrusel 4:5 "Tu primer mes con creatina" (línea de tiempo que avanza en cada lámina) + historias 9:16
(agenda de la semana con slider de emoji, encuesta, quiz, respuesta).
Uso (desde kit/build): python3 lunes_primer_mes.py <carpeta_feed> <carpeta_historias>
Respaldo: ISSN (Kreider et al. 2017): 3-5 g/día; carga opcional ~20 g/día 5-7 días; sin carga saturación en ~3-4 semanas;
retención de agua intramuscular; al dejarla, las reservas vuelven a lo normal en ~4-6 semanas.
"""
import sys, os
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright

FEED, STO = sys.argv[1], sys.argv[2]
OR = '#F26A1B'
GREEN = '#3ccf6e'
def I(n): return gen.uri(os.path.join(gen.B, n))
def ic(n, s=60): return gen.icon(n, s)

BASE = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.brand{{position:absolute;left:70px;display:flex;align-items:center;gap:16px}}
.brand img{{height:62px}}.brand div{{font-family:Bebas;font-size:46px;letter-spacing:2px;line-height:.9}}
.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:20px;letter-spacing:5px;color:#bbb}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}
.o{{color:{OR}}}
.kick{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:54px;padding:8px 26px 0;border-radius:10px;transform:rotate(-2deg)}}
.card{{border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.88);border-radius:26px;padding:34px 40px}}
.txt{{font-weight:600;font-size:40px;line-height:1.16;text-transform:uppercase}}
.fine{{font-weight:500;font-size:24px;color:#9a9a9a}}
.glow{{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(242,106,27,.55),rgba(160,50,0,.2) 55%,transparent);filter:blur(10px)}}
.tl{{position:absolute;left:70px;right:70px;top:170px;display:flex;align-items:center}}
.tl .st{{display:flex;flex-direction:column;align-items:center;width:150px;flex:none}}
.tl .dot{{width:34px;height:34px;border-radius:50%;border:3px solid #555;background:#111}}
.tl .dot.on{{border-color:{OR};background:{OR};box-shadow:0 0 24px rgba(242,106,27,.8)}}
.tl .dot.done{{border-color:{OR};background:#3a1a08}}
.tl .lb{{font-family:Bebas;font-size:30px;color:#777;margin-top:8px;letter-spacing:1px}}
.tl .lb.on{{color:#fff}}
.tl .ln{{flex:1;height:4px;background:#333;margin-bottom:38px}}
.tl .ln.done{{background:{OR}}}
.swipe{{position:absolute;right:70px;bottom:60px;font-family:Bebas;font-size:44px;letter-spacing:2px;color:#ddd}}
.swipe b{{color:{OR};font-weight:400}}
.row{{display:flex;gap:22px;align-items:flex-start;margin-bottom:22px}}
.row .ck{{flex:none;width:64px;height:64px;border-radius:50%;background:rgba(242,106,27,.12);border:2px solid {OR};display:grid;place-items:center;color:{OR}}}
"""

FX_FEED = gen.FX
FX_STO = (gen.FX.replace('height="1350"', 'height="1920"').replace('1080,1350', '1080,1920').replace('780,1350', '540,1900')
          .replace('780,1300', '540,1700').replace('y=500+r()*850', 'y=200+r()*1720').replace('y=r()*1350', 'y=r()*1920')
          .replace('(x-790)/320', '(x-540)/500'))
READY = "<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"


def feed(body, seed):
    b = f'<div class="brand" style="top:58px"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>'
    return f'<html><head><style>{BASE}body{{height:1350px}}</style></head><body>{FX_FEED.replace("SEED", str(seed))}{b}{body}{READY}</body></html>'


def story(body, seed):
    b = f'<div class="brand" style="top:270px"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>'
    return f'<html><head><style>{BASE}body{{height:1920px}}</style></head><body>{FX_STO.replace("SEED", str(seed))}{b}{body}{READY}</body></html>'


STEPS = ['DÍA 1', 'SEMANA 1–2', 'SEMANA 3–4', 'MES 2+']


def timeline(cur):
    h = ''
    for k, s in enumerate(STEPS):
        st = 'on' if k == cur else ('done' if k < cur else '')
        h += f'<div class="st"><div class="dot {st}"></div><div class="lb {"on" if k == cur else ""}">{s}</div></div>'
        if k < len(STEPS) - 1:
            h += f'<div class="ln {"done" if k < cur else ""}"></div>'
    return f'<div class="tl">{h}</div>'


def rows(items):
    return ''.join(f'<div class="row"><div class="ck">{ic(i, 36)}</div><div class="txt">{t}</div></div>' for i, t in items)


# ---------------- CARRUSEL ----------------
F = []
F.append(('1_portada', feed(f'''
<div class="glow" style="left:430px;top:420px;width:760px;height:900px"></div>
<img src="{I('p_finaflex.png')}" style="position:absolute;right:0px;bottom:120px;height:720px;transform:rotate(6deg);filter:drop-shadow(0 30px 30px #000)">
<div style="position:absolute;top:250px;left:70px;width:640px">
 <div class="kick">GUÁRDALO 📌</div>
 <div class="big" style="font-size:150px;margin-top:34px">TU PRIMER</div>
 <div class="big" style="font-size:150px">MES CON</div>
 <div class="big o" style="font-size:168px;text-shadow:0 0 40px rgba(242,106,27,.5)">CREATINA</div>
 <div style="font-weight:700;font-size:40px;text-transform:uppercase;color:#ddd;margin-top:24px;line-height:1.1">Qué pasa<br>semana a semana</div>
</div>
<div class="swipe" style="left:70px;right:auto">DESLIZA <b>→</b></div>''', 1201)))

F.append(('2_dia1', feed(f'''{timeline(0)}
<div style="position:absolute;top:330px;left:70px;right:70px">
 <div class="big" style="font-size:120px">EMPIEZA <span class="o">SIMPLE</span></div>
</div>
<div style="position:absolute;top:500px;left:70px;width:640px">{rows([
    ('scale', '<span class="o">3 a 5 g al día</span> (1 scoop). No necesitas más.'),
    ('glass-full', 'Con agua, jugo o en tu batido de proteína.'),
    ('clock', 'A la hora que te acomode. Lo importante es no saltártela.'),
    ('bolt', 'Fase de carga: <span class="o">opcional</span>. Acelera, pero no es necesaria.')])}
</div>
<div class="glow" style="left:620px;top:640px;width:560px;height:700px"></div>
<img src="{I('p_usn_crea.png')}" style="position:absolute;right:30px;bottom:150px;height:440px;transform:rotate(-6deg);filter:drop-shadow(0 20px 20px #000)">
<div class="swipe">SIGUE <b>→</b></div>''', 1202)))

F.append(('3_semana1_2', feed(f'''{timeline(1)}
<div style="position:absolute;top:330px;left:70px;right:70px">
 <div class="big" style="font-size:120px">TUS MÚSCULOS</div>
 <div class="big o" style="font-size:120px">SE VAN CARGANDO</div>
</div>
<div class="card" style="position:absolute;top:620px;left:60px;right:60px">
 <div class="txt">La creatina se acumula de a poco en el músculo. Por eso la constancia importa más que la hora.</div>
</div>
<div class="card" style="position:absolute;top:900px;left:60px;right:60px;border-color:rgba(60,207,110,.6)">
 <div style="display:flex;align-items:center;gap:14px;color:{GREEN}">{ic('droplet', 48)}<span class="big" style="font-size:56px;color:{GREEN}">¿SUBE LA BALANZA?</span></div>
 <div class="txt" style="margin-top:10px;font-size:36px">Puede ser 1 a 2 kg: es <span style="color:{GREEN}">agua dentro del músculo</span>, no grasa. Es normal.</div>
</div>
<div class="swipe">SIGUE <b>→</b></div>''', 1203)))

F.append(('4_semana3_4', feed(f'''{timeline(2)}
<div style="position:absolute;top:330px;left:70px;right:70px">
 <div class="big" style="font-size:120px">RESERVAS <span class="o">LLENAS</span></div>
 <div style="font-weight:600;font-size:32px;color:#ccc;text-transform:uppercase;margin-top:12px">Sin fase de carga, llegas aquí en 3 a 4 semanas</div>
</div>
<div style="position:absolute;top:580px;left:70px;width:620px">{rows([
    ('barbell', 'Puedes rendir un poco más en series <span class="o">cortas e intensas</span>.'),
    ('trending-up', 'Esa rep extra suma: más trabajo de calidad en cada sesión.'),
    ('run', 'La creatina te ayuda a entrenar mejor. <span class="o">El resultado lo pone tu entrenamiento.</span>')])}
</div>
<div class="glow" style="left:640px;top:660px;width:540px;height:680px"></div>
<img src="{I('p_mt_sin.png')}" style="position:absolute;right:30px;bottom:150px;height:440px;transform:rotate(7deg);filter:drop-shadow(0 20px 20px #000)">
<div class="swipe">SIGUE <b>→</b></div>''', 1204)))

F.append(('5_mes2', feed(f'''{timeline(3)}
<div style="position:absolute;top:330px;left:70px;right:70px">
 <div class="big" style="font-size:120px">AHORA <span class="o">MANTÉN</span></div>
</div>
<div style="position:absolute;top:500px;left:70px;right:70px">{rows([
    ('calendar', '<span class="o">Todos los días</span>, también los de descanso.'),
    ('scale', 'La misma dosis: 3 a 5 g. No hay que subirla.'),
    ('alert-triangle', 'Si la dejas, tus reservas vuelven a lo normal en unas semanas.')])}
</div>
<div class="card" style="position:absolute;top:1000px;left:60px;right:60px;text-align:center;padding:28px 30px">
 <div class="big" style="font-size:76px">CONSTANCIA <span class="o">&gt;</span> HORA</div>
</div>
<div class="swipe">SIGUE <b>→</b></div>''', 1205)))

CREAS = [('p_usn_crea.png', 'USN', '300 g', '60', 300), ('p_mt_sin.png', 'MuscleTech', '400 g', '80', 300),
         ('p_mt_uva.png', 'MuscleTech uva', '392 g', '60', 320), ('p_finaflex.png', 'Finaflex', '1 kg', '200', 330)]
ch = ''.join(f'''<div style="flex:1;display:flex;flex-direction:column;align-items:center">
 <div style="height:340px;display:flex;align-items:flex-end"><img src="{I(p)}" style="height:{h}px;max-width:225px;object-fit:contain;filter:drop-shadow(0 16px 14px #000)"></div>
 <div style="font-weight:800;font-size:28px;text-transform:uppercase;margin-top:14px;text-align:center;line-height:1">{n}</div>
 <div class="fine" style="margin-top:4px">{g}</div>
 <div class="big o" style="font-size:72px;margin-top:6px">{d}</div><div class="fine" style="margin-top:-4px">DÍAS</div></div>''' for p, n, g, d, h in CREAS)
F.append(('6_elige', feed(f'''
<div style="position:absolute;top:170px;left:70px;right:70px">
 <div class="big" style="font-size:110px">¿CON CUÁL HACES</div>
 <div class="big o" style="font-size:110px">TU PRIMER MES?</div>
 <div style="font-weight:600;font-size:28px;color:#ccc;text-transform:uppercase;margin-top:10px">Días que te dura tomando 5 g diarios</div>
</div>
<div class="glow" style="left:90px;top:520px;width:900px;height:620px"></div>
<div style="position:absolute;top:470px;left:40px;right:40px;display:flex">{ch}</div>
<div style="position:absolute;top:1060px;left:60px;right:60px;display:flex;align-items:center;gap:20px" class="card">
 <img src="{I('p_shaker.png')}" style="height:110px">
 <div style="font-weight:700;font-size:32px;text-transform:uppercase;line-height:1.1">Proteína + creatina = <span class="o">shaker C4 de regalo</span></div>
</div>
<div style="position:absolute;top:1228px;left:0;right:0;text-align:center"><span class="kick" style="font-size:52px">PÍDELA POR DM 📩</span></div>
<div style="position:absolute;bottom:20px;left:0;right:0;text-align:center;font-size:19px;color:#888">Si tienes alguna enfermedad o tomas medicamentos, consulta a tu médico.</div>''', 1206)))

# ---------------- HISTORIAS ----------------
S = []
SLOT = 'border:3px dashed rgba(255,255,255,.28);border-radius:28px;height:300px;display:grid;place-items:center;font-family:Bebas;font-size:40px;color:rgba(255,255,255,.35);letter-spacing:3px'
AG = [('LUNES', 'Tu primer mes con creatina', 'en el feed'), ('JUEVES', '¿Qué creatina te conviene?', 'comparativa en reel'),
      ('SÁBADO', '3 errores con la creatina', 'reel para guardar')]
agh = ''.join(f'''<div class="card" style="display:flex;align-items:center;gap:26px;padding:24px 34px;margin-bottom:22px">
 <div class="big o" style="font-size:64px;width:210px">{d}</div>
 <div><div style="font-weight:800;font-size:38px;text-transform:uppercase;line-height:1.05">{t}</div><div class="fine" style="text-transform:uppercase">{s}</div></div></div>''' for d, t, s in AG)
S.append(('1_semana_creatina', story(f'''
<div class="glow" style="left:240px;top:380px;width:900px;height:700px"></div>
<img src="{I('p_finaflex.png')}" style="position:absolute;right:50px;top:400px;height:470px;transform:rotate(8deg);filter:drop-shadow(0 30px 30px #000)">
<div style="position:absolute;top:420px;left:70px;width:640px">
 <div class="kick">ESTA SEMANA</div>
 <div class="big" style="font-size:150px;margin-top:30px">TODO SOBRE</div>
 <div class="big o" style="font-size:170px;text-shadow:0 0 40px rgba(242,106,27,.5)">CREATINA</div>
</div>
<div style="position:absolute;top:930px;left:60px;right:60px">{agh}</div>
<div style="position:absolute;top:1340px;left:60px;right:60px;{SLOT}">DESLIZA EL 🔥 AQUÍ</div>''', 2201)))

S.append(('2_encuesta', story(f'''
<div style="position:absolute;top:470px;left:70px;right:70px;text-align:center">
 <div class="big" style="font-size:120px">PREGUNTA</div>
 <div class="big" style="font-size:120px">RÁPIDA 👇</div>
 <div class="big o" style="font-size:200px;margin-top:40px;text-shadow:0 0 40px rgba(242,106,27,.5)">¿TOMAS</div>
 <div class="big o" style="font-size:200px;text-shadow:0 0 40px rgba(242,106,27,.5)">CREATINA?</div>
</div>
<div style="position:absolute;top:1130px;left:90px;right:90px;{SLOT}">ENCUESTA AQUÍ</div>
<div style="position:absolute;top:1480px;left:0;right:0;text-align:center;display:flex;justify-content:center;gap:30px">
 <img src="{I('p_usn_crea.png')}" style="height:170px;transform:rotate(-8deg);filter:drop-shadow(0 12px 12px #000)">
 <img src="{I('p_mt_uva.png')}" style="height:170px;filter:drop-shadow(0 12px 12px #000)">
 <img src="{I('p_mt_sin.png')}" style="height:170px;transform:rotate(8deg);filter:drop-shadow(0 12px 12px #000)"></div>''', 2202)))

S.append(('3_quiz', story(f'''
<div style="position:absolute;top:430px;left:70px;right:70px">
 <div class="kick">QUIZ ⏱️</div>
 <div class="big" style="font-size:112px;margin-top:34px">SIN FASE DE CARGA,</div>
 <div class="big" style="font-size:112px">¿CUÁNTO TARDA LA</div>
 <div class="big o" style="font-size:112px">CREATINA EN LLENAR</div>
 <div class="big o" style="font-size:112px">TUS MÚSCULOS?</div>
</div>
<div style="position:absolute;top:1060px;left:90px;right:90px;{SLOT}">QUIZ AQUÍ</div>
<div style="position:absolute;top:1400px;left:70px;right:70px;text-align:center;font-family:Bebas;font-size:48px;letter-spacing:2px;color:#ddd">LA RESPUESTA EN LA <span class="o">SIGUIENTE</span> 👉</div>
<div style="position:absolute;top:1480px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:20px"><img src="{I('p_mt_sin.png')}" style="height:160px;filter:drop-shadow(0 12px 12px #000)"><img src="{I('p_finaflex.png')}" style="height:180px;filter:drop-shadow(0 12px 12px #000)"></div>''', 2203)))

S.append(('4_respuesta', story(f'''
<div style="position:absolute;top:430px;left:70px;right:70px">
 <div class="lbl" style="font-weight:800;font-size:34px;letter-spacing:4px;color:{GREEN}">RESPUESTA CORRECTA</div>
 <div class="big o" style="font-size:250px;margin-top:10px;text-shadow:0 0 50px rgba(242,106,27,.5)">3 A 4</div>
 <div class="big" style="font-size:170px">SEMANAS</div>
</div>
<div class="card" style="position:absolute;top:1000px;left:60px;right:60px">
 <div class="txt">Tomando 3 a 5 g todos los días. Con fase de carga se acorta a <span class="o">5 a 7 días</span>, pero no es obligatoria.</div>
</div>
<div style="position:absolute;top:1330px;left:60px;right:60px;text-align:center">
 <div class="big" style="font-size:62px">SEMANA A SEMANA, EN EL</div>
 <div class="big o" style="font-size:62px">POST DE HOY 📌</div>
 <div style="margin-top:26px"><span class="kick" style="font-size:52px">¿DUDAS? ESCRÍBENOS 📩</span></div>
</div>''', 2204)))


def run(pages, out, h):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': h})
        for n, html in pages:
            pg.set_content(html, wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            png = os.path.join(out, n + '.png'); pg.screenshot(path=png)
            from PIL import Image
            Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=90); os.remove(png); print(n)
        b.close()


os.makedirs(FEED, exist_ok=True); os.makedirs(STO, exist_ok=True)
only = sys.argv[3:]
run([x for x in F if not only or x[0] in only], FEED, 1350)
run([x for x in S if not only or x[0] in only], STO, 1920)
