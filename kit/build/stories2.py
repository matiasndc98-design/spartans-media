import sys, os; sys.path.insert(0,'.')
import gen
from playwright.sync_api import sync_playwright
OUT=sys.argv[1]; OR='#F26A1B'
FX=gen.FX.replace('height="1350"','height="1920"').replace('1080,1350','1080,1920').replace('780,1350','540,1900').replace('780,1300','540,1700').replace('y=500+r()*850','y=200+r()*1720').replace('y=r()*1350','y=r()*1920').replace('(x-790)/320','(x-540)/500')
def I(n): return gen.uri(os.path.join(gen.B,n))
def ic(n,s=60): return gen.icon(n,s)
CSS=gen.FONTS+f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.brand{{position:absolute;top:190px;left:70px;display:flex;align-items:center;gap:16px}}
.brand img{{height:62px}}.brand div{{font-family:Bebas;font-size:46px;letter-spacing:2px;line-height:.9}}.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:20px;letter-spacing:5px;color:#bbb}}
.prog{{position:absolute;top:190px;right:70px;font-family:Bebas;font-size:44px;color:{OR}}}
.prog span{{color:#666}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}
.o{{color:{OR}}}
.kick{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:54px;padding:8px 26px 0;border-radius:10px;transform:rotate(-2deg)}}
.card{{border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.85);border-radius:26px;padding:40px 44px}}
.stamp{{position:absolute;font-family:Bebas;color:#ff3b1f;border:10px solid #ff3b1f;border-radius:18px;padding:14px 40px 0;transform:rotate(-14deg);opacity:.92;letter-spacing:6px;box-shadow:0 0 30px rgba(255,59,31,.35)}}
.real{{display:flex;gap:24px;align-items:flex-start}}
.real .ok{{flex:none;width:92px;height:92px;border-radius:50%;background:#1f9d55;display:grid;place-items:center;color:#fff}}
.lbl{{font-weight:800;font-size:34px;letter-spacing:4px;color:{OR}}}
.txt{{font-weight:600;font-size:46px;line-height:1.15}}
.fine{{font-weight:500;font-size:26px;color:#9a9a9a}}
.tap{{position:absolute;bottom:250px;left:0;right:0;text-align:center;font-family:Bebas;font-size:48px;letter-spacing:3px;color:#ddd}}
.tap b{{color:{OR};font-weight:400}}
"""
def page(body,seed,n=None,tot=7):
    pr=''  # sin numeración (decisión del dueño)
    b=f'<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>'
    return f'<html><head><style>{CSS}</style></head><body>{FX.replace("SEED",str(seed))}{b}{pr}{body}<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script></body></html>'

pages=[]
# 1 HOOK
pages.append(('s1_hook',page(f'''
<div style="position:absolute;top:470px;left:70px;right:70px">
 <div class="kick">ALERTA GYM ⚠️</div>
 <div class="big" style="font-size:260px;margin-top:40px">3 MITOS</div>
 <div class="big" style="font-size:118px">DE LA <span class="o">CREATINA</span></div>
 <div class="big" style="font-size:118px">QUE TE ESTÁN</div>
 <div class="big o" style="font-size:200px;text-shadow:0 0 40px rgba(242,106,27,.5)">FRENANDO</div>
</div>
<img src="{I('p_mt_sin.png')}" style="position:absolute;right:-60px;bottom:330px;height:620px;transform:rotate(12deg);filter:drop-shadow(0 30px 30px #000);opacity:.95">
<div class="tap" style="text-align:left;left:70px">TOCA PARA VER <b>→</b></div>''',11)))
MYTHS=[('LA CREATINA<br>ENGORDA','Puedes subir 1–2 kg, pero es <span class="o">agua dentro del músculo</span>, no grasa. Por eso te ves más lleno.'),
       ('HAY QUE HACER<br>FASE DE CARGA','No es obligatoria. Con <span class="o">3 a 5 g diarios</span> llegas al mismo nivel en 3–4 semanas, sin malestar.'),
       ('SOLO SE TOMA<br>LOS DÍAS DE GYM','Se toma <span class="o">todos los días</span>, también en descanso. Lo que funciona es la constancia, no la hora.')]
for k,(m,r) in enumerate(MYTHS):
    pages.append((f's{k+2}_mito{k+1}',page(f'''
<div style="position:absolute;top:400px;left:70px;right:70px">
 <div class="lbl">MITO #{k+1}</div>
 <div class="big" style="font-size:150px;margin-top:14px;color:#f1ece6">"{m}"</div>
</div>
<div class="stamp" style="top:760px;right:90px;font-size:150px">MITO</div>
<div class="card" style="position:absolute;top:1080px;left:60px;right:60px">
 <div class="real"><div class="ok">{ic('check',58)}</div><div><div class="lbl" style="color:#3ddc84">REALIDAD</div><div class="txt" style="margin-top:10px">{r}</div></div></div>
</div>
<img src="{I(['p_usn_crea.png','p_mt_uva.png','p_mt_sin.png'][k])}" style="position:absolute;right:40px;top:1390px;height:430px;transform:rotate({[-10,8,-6][k]}deg);filter:drop-shadow(0 30px 30px #000)"><div class="tap" style="text-align:left;left:70px">SIGUE <b>→</b></div>''',300+k*17,k+2)))
# 5 cost per day
rows=[('p_usn_crea.png','Creatina USN','300 g · 60 porciones','60'),('p_mt_sin.png','MuscleTech sin sabor','400 g · 80 porciones','80'),('p_finaflex.png','Finaflex','1 kg · 200 porciones','200')]
rh=''.join(f'''<div class="card" style="display:flex;align-items:center;gap:30px;padding:26px 34px;margin-bottom:26px">
 <img src="{I(i)}" style="height:190px;filter:drop-shadow(0 10px 10px #000)">
 <div style="flex:1"><div style="font-weight:800;font-size:40px;text-transform:uppercase">{a}</div><div class="fine">{b}</div></div>
 <div style="text-align:right"><div class="big o" style="font-size:110px">{c}</div><div class="fine" style="margin-top:-6px">DÍAS</div></div></div>''' for i,a,b,c in rows)
pages.append(('s5_cuanto_dura',page(f'''
<div style="position:absolute;top:400px;left:70px;right:70px">
 <div class="big" style="font-size:140px">¿CUÁNTO TE</div><div class="big" style="font-size:140px">DURA <span class="o">TU CREATINA?</span></div>
 <div class="fine" style="margin-top:18px;font-size:32px;color:#ccc">Tomando 5 g al día, todos los días</div>
</div>
<div style="position:absolute;top:800px;left:60px;right:60px">{rh}</div>
<div style="position:absolute;top:1650px;left:0;right:0;text-align:center"><div class="kick" style="font-size:60px">ESCRÍBENOS "CREATINA" 📩</div></div>''',555,5)))
# 6 stack
st=[('flame','VOLUMEN',['p_whey.png','p_mt_sin.png'],'Whey + Creatina MuscleTech','🎁'),
    ('bolt','DEFINICIÓN',['p_lipo.png','p_whey.png'],'Lipo 6 + Whey USN','📩'),
    ('heart','SALUD BASE',['p_multi.png','p_usn_crea.png'],'Multivitamínico + Creatina USN','🎁')]
sh=''.join(f'''<div class="card" style="display:flex;align-items:center;gap:22px;padding:22px 30px;margin-bottom:24px">
 <div style="display:flex;align-items:flex-end">{''.join(f'<img src="{I(x)}" style="height:{170 if j==0 else 140}px;margin-right:-26px;filter:drop-shadow(0 10px 10px #000)">' for j,x in enumerate(ims))}</div>
 <div style="flex:1;margin-left:36px"><div style="display:flex;align-items:center;gap:10px;color:{OR}">{ic(icn,40)}<span class="big" style="font-size:66px">{t}</span></div><div style="font-weight:600;font-size:30px;text-transform:uppercase">{d}</div></div>
 <div class="big" style="font-size:64px">{p}</div></div>''' for icn,t,ims,d,p in st)
pages.append(('s6_stack',page(f'''
<div style="position:absolute;top:400px;left:70px;right:70px">
 <div class="kick">ARMA TU</div>
 <div class="big o" style="font-size:230px;margin-top:20px;text-shadow:0 0 40px rgba(242,106,27,.45)">STACK</div>
 <div class="fine" style="font-size:32px;color:#ccc">Según tu objetivo</div>
</div>
<div style="position:absolute;top:900px;left:50px;right:50px">{sh}</div>''',666,6)))
# 7 CTA
opts=[('💪','GANAR MASA'),('🔥','DEFINIR'),('⚡','MÁS ENERGÍA')]
oh=''.join(f'<div class="card" style="display:flex;align-items:center;gap:30px;padding:26px 40px;margin-bottom:24px"><div style="font-size:84px">{e}</div><div class="big" style="font-size:96px">{t}</div></div>' for e,t in opts)
pages.append(('s7_objetivo',page(f'''
<div style="position:absolute;top:400px;left:70px;right:70px">
 <div class="big" style="font-size:150px">¿CUÁL ES TU</div><div class="big o" style="font-size:210px;text-shadow:0 0 40px rgba(242,106,27,.45)">OBJETIVO?</div>
</div>
<div style="position:absolute;top:830px;left:60px;right:60px">{oh}</div>
<div style="position:absolute;top:1480px;left:60px;right:60px;text-align:center">
 <div class="big" style="font-size:66px">RESPÓNDENOS CON EL EMOJI</div>
 <div class="big o" style="font-size:66px">Y TE ARMAMOS TU PACK 📩</div>
 <div class="fine" style="margin-top:14px">Entrega en Caldera · Envíos a todo Chile</div>
</div>''',777,7)))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,h in pages:
        pg.set_content(gen.sin_emoji(h),wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
        pg.screenshot(path=os.path.join(OUT,n+'.png')); print(n)
    b.close()
