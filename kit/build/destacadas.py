"""Portadas de historias destacadas + historias informativas fijas.
Uso (desde kit/build): python3 destacadas.py <carpeta_salida>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright

OUT = sys.argv[1]
OR = '#F26A1B'
W, H = 1080, 1920
FX = (gen.FX.replace('height="1350"', 'height="1920"').replace('1080,1350', '1080,1920')
      .replace('780,1350', '540,1900').replace('780,1300', '540,1500')
      .replace('y=500+r()*850', 'y=200+r()*1720').replace('y=r()*1350', 'y=r()*1920')
      .replace('(x-790)/320', '(x-540)/600'))

BASE = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.big{{font-family:Bebas;line-height:.9;text-transform:uppercase}}
.o{{color:{OR}}}
.card{{border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.85);border-radius:26px}}
.brand{{position:absolute;top:190px;left:70px;display:flex;align-items:center;gap:16px}}
.brand img{{height:62px}}.brand div{{font-family:Bebas;font-size:46px;letter-spacing:2px;line-height:.9}}
.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:20px;letter-spacing:5px;color:#bbb}}
"""
DONE = "<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"


def page(css, body, seed=7):
    return f'<html><head><style>{BASE}{css}</style></head><body>{FX.replace("SEED", str(seed))}{body}{DONE}</body></html>'


def cover(icon_name=None, img=None):
    # Instagram recorta un círculo centrado: todo el diseño vive en el centro.
    inner = (f'<img src="{img}" style="width:300px">' if img else gen.icon(icon_name, 300))
    css = f"""
.glow{{position:absolute;left:140px;top:560px;width:800px;height:800px;border-radius:50%;
 background:radial-gradient(closest-side,rgba(242,106,27,.45),rgba(242,106,27,.08) 70%,transparent)}}
.ring{{position:absolute;left:290px;top:710px;width:500px;height:500px;border-radius:50%;
 border:6px solid {OR};box-shadow:0 0 40px rgba(242,106,27,.6), inset 0 0 40px rgba(242,106,27,.25);
 display:grid;place-items:center;color:{OR};background:rgba(8,6,5,.75)}}
.ring svg{{filter:drop-shadow(0 0 14px rgba(242,106,27,.7))}}
.ring svg *{{stroke-width:1.4}}
"""
    return page(css, f'<div class="glow"></div><div class="ring">{inner}</div>', 11)


COVERS = [('precios', 'tag'), ('comprar', 'shopping-cart'), ('envios', 'truck-delivery'),
          ('aprende', 'brain'), ('stacks', 'barbell'), ('spartans', None)]


def info_comprar():
    steps = [('message-circle', 'ESCRÍBENOS AL DM', 'Dinos qué producto buscas o tu objetivo'),
             ('check', 'TE ASESORAMOS', 'Te confirmamos stock y te ayudamos a elegir'),
             ('credit-card', 'PAGA COMO QUIERAS', 'Transferencia, efectivo, tarjeta o Mercado Pago'),
             ('package', 'RECIBE TU PEDIDO', 'Delivery en Caldera o envío a todo Chile')]
    rows = ''.join(f'''<div class="card" style="display:flex;align-items:center;gap:30px;padding:28px 36px;margin-bottom:24px">
      <div style="flex:none;width:96px;height:96px;border-radius:50%;background:{OR};color:#0b0705;display:grid;place-items:center">{gen.icon(ic, 54)}</div>
      <div><div class="big" style="font-size:62px">{a}</div><div style="font-weight:600;font-size:30px;color:#cfcfcf;text-transform:uppercase">{b}</div></div></div>'''
                   for ic, a, b in steps)
    body = f'''<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>
<div style="position:absolute;top:380px;left:70px;right:70px"><div class="big" style="font-size:150px">¿CÓMO</div><div class="big o" style="font-size:190px;text-shadow:0 0 40px rgba(242,106,27,.45)">COMPRAR?</div></div>
<div style="position:absolute;top:800px;left:60px;right:60px">{rows}</div>
<div style="position:absolute;top:1610px;left:0;right:0;text-align:center;font-family:Bebas;font-size:54px;letter-spacing:2px">PRODUCTOS 100% ORIGINALES Y SELLADOS</div>'''
    return page('', body, 21)


def info_envios():
    opts = [('home', 'DELIVERY EN CALDERA', '$1.500', 'Te lo llevamos a tu casa'),
            ('map-pin', 'RETIRO EN CALDERA', 'GRATIS', 'Coordinamos punto y hora por DM'),
            ('truck-delivery', 'ENVÍOS A TODO CHILE', 'POR PAGAR', 'Starken, Chilexpress o Blue Express: tú eliges')]
    rows = ''.join(f'''<div class="card" style="padding:30px 36px;margin-bottom:26px">
      <div style="display:flex;align-items:center;gap:22px;color:{OR}">{gen.icon(ic, 56)}<span class="big" style="font-size:64px;color:#fff;flex:1">{a}</span><span class="big o" style="font-size:64px">{p}</span></div>
      <div style="font-weight:600;font-size:30px;color:#cfcfcf;text-transform:uppercase;margin-top:6px;padding-left:78px">{d}</div></div>'''
                   for ic, a, p, d in opts)
    body = f'''<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>
<div style="position:absolute;top:380px;left:70px;right:70px"><div class="big" style="font-size:150px">¿CÓMO TE</div><div class="big o" style="font-size:190px;text-shadow:0 0 40px rgba(242,106,27,.45)">LLEGA?</div></div>
<div style="position:absolute;top:800px;left:60px;right:60px">{rows}</div>
<div style="position:absolute;top:1400px;left:60px;right:60px;text-align:center;font-weight:600;font-size:30px;color:#bbb;text-transform:uppercase">El plazo de envío depende de tu ciudad.<br>Escríbenos y te cotizamos.</div>'''
    return page('', body, 33)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [(f'portada_{n}', cover(i, None if i else gen.HELMET)) for n, i in COVERS]
    pages += [('info_comprar', info_comprar()), ('info_envios', info_envios())]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
        for n, h in pages:
            pg.set_content(h, wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, n + '.png')); print(n)
        b.close()
