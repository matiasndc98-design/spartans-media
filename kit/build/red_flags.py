"""Carrusel de humor identificable: "Red flags en el gym" (estilo premium). Contenido para compartir, con remate de marca.
Uso (desde kit/build): python3 red_flags.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

RED = '#E0302A'
FLAG = (f'<svg width="{{s}}" height="{{s}}" viewBox="0 0 100 100"><rect x="18" y="8" width="7" height="88" rx="3" fill="#cfcac2"/>'
        f'<path d="M25 12 C45 4 60 22 88 12 L88 52 C60 62 45 44 25 52 Z" fill="{RED}"/></svg>')
flag = lambda s: FLAG.replace('{s}', str(s))

FLAGS = [
    ('Ocupa 3 máquinas<br>al mismo tiempo.', 'Y te dice "me quedan 4 series".', None),
    ('No devuelve<br>los discos.', 'El gimnasio no es su casa. O sí, pero igual.', None),
    ('Toma creatina solo los días que entrena.', 'Spoiler: se toma todos los días, también los de descanso.', 'p_mt_sin.png'),
    ('Su shaker huele a algo que murió en 2019.', 'Lávalo apenas lo uses. Tu bolso te lo agradece.', 'p_shaker.png'),
    ('"Mañana empiezo."<br>Desde marzo.', 'El mejor día para partir fue ayer. El segundo mejor, hoy.', None),
]


def portada():
    b = (P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Spartans · Humor</div>'
         + f'<div style="position:absolute;left:0;right:0;top:300px;display:flex;justify-content:center">{flag(260)}</div>'
         + '<div style="position:absolute;left:0;right:0;top:620px;text-align:center">'
           f'<div class="h" style="font-size:200px;color:{RED}">Red flags</div><div class="h" style="font-size:150px">en el gym.</div>'
           '<div class="lab" style="margin-top:30px">¿Cuántas tienes tú? Sé honesto</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px">Desliza</div><div class="rule" style="position:absolute;left:200px;bottom:72px;width:120px"></div>')
    return P.page(P.W, P.H, b, 'rgba(224,48,42,.12)')


def lamina(i, frase, remate, img):
    prod = ''
    if img == 'p_shaker.png':
        prod = P.heroe(img, 860, 1210, 520, rot=-8)
    elif img:
        prod = P.heroe(img, 870, 1210, 470)
    b = (P.marca(70, 64) + f'<div class="foot" style="right:70px;top:74px">Red flag {i:02d} / 05</div>'
         + f'<div style="position:absolute;left:70px;top:{230 if img else 330}px">{flag(120)}</div>'
         + prod
         + f'<div style="position:absolute;left:70px;top:{420 if img else 520}px;width:{600 if img else 940}px">'
           f'<div class="h" style="font-size:{104 if img else 160}px">{frase}</div>'
           f'<div class="rule" style="margin:44px 0 26px;background:{RED}"></div>'
           f'<div style="font-size:38px;line-height:1.3;color:#bdb8b0;font-weight:500">{remate}</div></div>')
    return P.page(P.W, P.H, b, 'rgba(224,48,42,.08)' if not img else 'rgba(242,106,27,.10)')


def cierre():
    b = (P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">La green flag</div>'
         + P.heroe('p_finaflex.png', 420, 1150, 520) + P.heroe('p_shaker.png', 720, 1150, 430, rot=6)
         + '<div style="position:absolute;left:0;right:0;top:170px;text-align:center"><div class="lab">Green flag de verdad</div>'
           '<div class="h" style="font-size:150px;margin-top:16px">Constancia.</div>'
           '<div style="font-size:34px;color:#bdb8b0;margin-top:18px;font-weight:500">Creatina todos los días y el shaker limpio.</div></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Comenta tu red flag <span class="o">·</span> Pídela por DM</div>')
    return P.page(P.W, P.H, b, 'rgba(60,200,110,.10)')


if __name__ == '__main__':
    pages = [('1_portada', portada())] + [(f'{i + 2}_red_flag{i + 1}', lamina(i + 1, *f)) for i, f in enumerate(FLAGS)] + [('7_green_flag', cierre())]
    P.render(pages, OUT, P.W, P.H)
