import sys; sys.path.insert(0,'.')
import gen
P=[
 dict(name='02_whey',img='p_whey.png',h=760,a='Proteína que',b='TE CONSTRUYE.',c='USN Premium Whey+ 5 lb<br>sabor chocolate',
  ben=[('barbell','22 g de proteína','por porción'),('stretching','Recuperación','después de entrenar'),('award','5 lb (2,27 kg)','rinde semanas de entreno')]),
 dict(name='03_creatina_usn',img='p_usn_crea.png',h=700,a='Fuerza que',b='TE IMPULSA.',c='Creatina monohidratada<br>USN 300 g',
  ben=[('bolt','5 g de creatina','por porción'),('clock','60 porciones','2 meses de uso diario'),('droplet','Sin sabor','mézclala con lo que quieras')]),
 dict(name='04_muscletech_sin_sabor',img='p_mt_sin.png',h=720,a='Platinum',b='100% PURA.',c='Creatina MuscleTech<br>400 g sin sabor',
  ben=[('award','Micronizada','y ultra pura'),('bolt','5 g por porción','80 porciones'),('droplet','Sin sabor','se disuelve fácil en agua')]),
 dict(name='05_muscletech_uva',img='p_mt_uva.png',h=720,a='Sabor que',b='MOTIVA.',c='Creatina MuscleTech<br>392 g sabor uva',
  ben=[('award','Micronizada','y ultra pura'),('bolt','5 g por porción','60 porciones'),('heart','Sabor uva','Grape Freeze')]),
 dict(name='06_lipo6',img='p_lipo.png',h=720,a='Enciende tu',b='FUEGO INTERNO.',c='Termogénico Nutrex<br>Lipo 6 Black · 60 cápsulas',
  note='Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas.',
  ben=[('flame','Energía intensa','y enfoque mental'),('pill','Una cápsula','por porción'),('shield-check','Sello original','verificable de Nutrex')]),
 dict(name='07_multivitaminico',img='p_multi.png',h=700,a='Tu base de',b='CADA DÍA.',c='Multivitamínico USN<br>Super Daily Formula',
  ben=[('pill','20+ ingredientes','activos'),('heart','Vitaminas y minerales','esenciales'),('clock','60 tabletas','1 mes de uso')]),

    dict(name='08_iso100', img='p_iso100.png', h=760, a='Nivel', b='PREMIUM.', c='Dymatize ISO 100 Hydrolyzed<br>5 lb · Cocoa Pebbles',
         ben=[('barbell', '25 g de proteína', 'por porción'), ('droplet', '100% whey isolate', 'hidrolizada'), ('clock', '71 porciones', '5 lb (2,3 kg)')]),
    dict(name='09_nitro', img='p_nitro.png', h=700, a='Proteína +', b='CREATINA.', c='MuscleTech Nitro Tech<br>4 lb · vainilla',
         ben=[('barbell', '30 g de proteína', 'por porción'), ('bolt', '3 g de creatina', 'en cada porción'), ('award', '4 lb (1,81 kg)', 'sabor vainilla')]),
    dict(name='10_finaflex', img='p_finaflex.png', h=740, a='1 kilo de', b='CREATINA.', c='Finaflex Creatine<br>1 kg · sin sabor',
         ben=[('bolt', '5 g de creatina', 'micronizada'), ('clock', '200 porciones', '200 días de uso diario'), ('shield-check', 'Certificada NSF', 'contenido verificado')]),
    dict(name='11_omega', img='p_omega.png', h=740, a='Tu esencial', b='DIARIO.', c='USN Omega 3 Fish Oil<br>1000 mg',
         ben=[('droplet', '1000 mg', 'por cápsula'), ('pill', '90 cápsulas', 'blandas'), ('leaf', 'Ácidos grasos', 'esenciales')]),
    dict(name='12_guarana', img='p_guarana.png', h=760, a='Energía en', b='UN SHOT.', c='OstroVit Guaraná Shot<br>80 ml · sabor pera',
         note='Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.',
         ben=[('bolt', '200 mg de cafeína', 'por shot'), ('bottle', '80 ml', 'listo para tomar'), ('flame', 'Sabor pera', 'antes de entrenar')]),
    dict(name='13_barra', img='p_barra.png', h=760, align='center', imgstyle='max-width:none;max-height:none;width:760px;transform:rotate(-68deg)', a='Proteína', b='AL PASO.', c='Space Protein XXL<br>80 g · coco',
         ben=[('barbell', '36% proteína', 'barra de 80 g'), ('heart', '3 g de azúcar', 'por barra'), ('star', 'Sabor coco', 'tamaño XXL')]),
]
import os
out=sys.argv[1]; gen.OUT=out
only=sys.argv[2:] 
pages=[(d['name'],gen.product_slide(d,i*7919+13)) for i,d in enumerate(P) if not only or d['name'] in only]
gen.render(pages)

def cover():
    imgs=['p_whey.png','p_iso100.png','p_nitro.png','p_finaflex.png','p_mt_sin.png','p_lipo.png','p_omega.png']
    hs=[300,300,290,290,250,250,240]
    row=''.join(f'<img src="{gen.uri(gen.os.path.join(gen.B,i))}" style="height:{h}px;margin:0 -14px;filter:drop-shadow(0 20px 20px rgba(0,0,0,.85))">' for i,h in zip(imgs,hs))
    css=gen.CSS+"""
.hdr{left:0;right:0;width:auto}.hdr .ln{width:460px}
.big{position:absolute;left:0;right:0;top:355px;text-align:center}
.big .a{font-family:Bebas;font-size:190px;line-height:.85;color:#f1ece6}
.big .b{font-family:Bebas;font-size:150px;line-height:.9;color:#F26A1B;text-shadow:0 0 40px rgba(242,106,27,.4)}
.big .c{font-weight:700;font-size:34px;letter-spacing:3px;margin-top:10px;text-transform:uppercase}
.row6{position:absolute;left:0;right:0;top:770px;height:340px;display:flex;align-items:flex-end;justify-content:center;z-index:3}
.glow{left:90px;top:640px;width:900px;height:560px}
.ped{left:110px;width:860px;top:1085px;height:70px}
.sw{position:absolute;right:56px;top:1135px;font-family:Bebas;font-size:40px;color:#F26A1B;letter-spacing:2px;z-index:4}
"""
    return f'<html><head><style>{css}</style></head><body>{gen.FX.replace("SEED","4242")}<div class="stripes"></div><div class="glow"></div><div class="ped"></div>{gen.header()}<div class="big"><div class="a">CATÁLOGO</div><div class="b">SPARTANS</div><div class="c">12 productos 100% originales · pide por DM</div></div><div class="row6">{row}</div><div class="sw">DESLIZA →</div>{gen.bar_html()}{gen.FIT}</body></html>'

def final():
    steps=[('1','Escríbenos al DM','Dinos qué producto quieres'),('2','Elige tu entrega','Delivery o retiro en Caldera, o envío a todo Chile'),('3','Coordina y recibe','Te confirmamos stock, pago y entrega')]
    st=''.join(f'<div class="st"><div class="n">{n}</div><div><div class="t1">{a}</div><div class="t2">{b}</div></div></div>' for n,a,b in steps)
    css=gen.CSS+"""
.hdr{left:0;right:0;width:auto}.hdr .ln{width:460px}
.q{position:absolute;left:70px;top:350px;font-family:Bebas;font-size:150px;line-height:.88}
.q span{color:#F26A1B}
.steps{position:absolute;left:70px;top:640px;width:560px}
.st{display:flex;gap:26px;align-items:center;padding:18px 0;border-bottom:1px solid rgba(242,106,27,.35)}
.st:last-child{border:none}
.st .n{width:84px;height:84px;flex:none;border:3px solid #F26A1B;border-radius:50%;display:grid;place-items:center;font-family:Bebas;font-size:56px;color:#F26A1B;background:rgba(242,106,27,.08)}
.st .t1{font-weight:800;font-size:38px;text-transform:uppercase;line-height:1}
.st .t2{font-weight:500;font-size:26px;color:#cfcfcf;margin-top:6px;text-transform:uppercase;line-height:1.1}
.bdg{position:absolute;right:40px;top:560px;width:400px;border-radius:24px;overflow:hidden;box-shadow:0 0 60px rgba(242,106,27,.35);border:2px solid rgba(242,106,27,.6)}
.bdg img{width:100%;display:block}
.bdg2{position:absolute;right:50px;top:600px;width:380px;height:380px;border-radius:50%;border:3px solid rgba(242,106,27,.7);background:radial-gradient(circle,#2a1406,#0b0806 70%);box-shadow:0 0 70px rgba(242,106,27,.35);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.bdg2 img{width:220px}
.bdg2 .t{text-align:center;font-weight:800;font-size:20px;letter-spacing:6px;color:#ddd}.bdg2 .t b{display:block;font-family:Bebas;font-weight:400;font-size:58px;letter-spacing:3px;color:#fff;line-height:.9}
.dm{position:absolute;left:70px;top:1062px;background:#F26A1B;color:#0b0705;font-family:Bebas;font-size:58px;padding:14px 30px 6px;border-radius:14px;box-shadow:0 0 40px rgba(242,106,27,.45)}
"""
    return f'<html><head><style>{css}</style></head><body>{gen.FX.replace("SEED","777")}<div class="stripes"></div>{gen.header()}<div class="q">¿CÓMO<br><span>COMPRAR?</span></div><div class="steps">{st}</div><div class="bdg2"><img src="{gen.HELMET}"><div class="t">SUPLEMENTOS<b>SPARTANS</b></div></div><div class="dm">ESCRÍBENOS AL DM →</div>{gen.bar_html()}{gen.FIT}</body></html>'

if not only or '01_portada' in only: gen.render([('01_portada',cover())])
if not only or '14_como_comprar' in only: gen.render([('14_como_comprar',final())])
