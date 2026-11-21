"""Sábado 21 nov 2026 · foto de feed automática (Metricool 10 AM) + historias "esto o esto" (estilo SOBRIO).
Puente a la semana de la energía. Idea nueva: PRODUCTO PEQUEÑO, MUCHO AIRE (minimalismo editorial: el envase chico
abajo, con sombra larga, y el titular gigante ocupando el negro) y, en historias, FORMATO CINE (franja panorámica
"skinny cinematic" de Reels 2026: el producto en una banda ancha y negro arriba y abajo).
Feed 4:5: Guaraná Shot OstroVit 80 ml pera "Un shot. Y a entrenar." + nota de cafeína.
Historias 9:16: 1 "Sábado. Se entrena." (banda de cine, Guaraná) · 2 encuesta "¿Shot o barra?" (espacio libre ~700–1050).
Sin precios, sin numeración. Uso (desde kit/build): python3 sabado_shot.py <feed_dir> <hist_dir>
"""
import sys
FEED_OUT = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST_OUT = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
NOTA = 'Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'


def negro(w, h, cx, floor_y):
    """Set negro con un charco de luz cálida chico bajo el producto y sombra larga."""
    return (
        '<div style="position:absolute;inset:0;background:#060504"></div>'
        f'<div style="position:absolute;left:0;right:0;top:{floor_y}px;bottom:0;'
        f'background:radial-gradient(ellipse 30% 40% at {cx}px 0,#2e2219 0%,#120d0a 55%,#060504 100%)"></div>'
        f'<div style="position:absolute;left:{cx - 260}px;top:{floor_y - 420}px;width:520px;height:520px;'
        'background:radial-gradient(closest-side,rgba(242,106,27,.10),transparent);filter:blur(10px)"></div>')


def shot(cx, base_y, height, sombra=True):
    src = P.I('p_guarana.png')
    s = ''
    if sombra:  # sombra larga hacia la derecha, como luz baja de costado
        s = (f'<div style="position:absolute;left:{cx}px;top:{base_y - height}px;height:{height}px;transform:translateX(-50%)">'
             f'<img src="{src}" style="height:{height}px;transform-origin:50% 100%;transform:skewX(-62deg) scaleY(.32);'
             'filter:brightness(0) blur(7px);opacity:.6"></div>')
    return (s + f'<img src="{src}" style="position:absolute;left:{cx}px;top:{base_y}px;height:{height}px;'
            'transform:translate(-50%,-100%);filter:drop-shadow(0 18px 18px rgba(0,0,0,.8))">'
            f'<img src="{src}" style="position:absolute;left:{cx}px;top:{base_y}px;height:{height}px;'
            'transform:translate(-50%,0) scaleY(-1);opacity:.12;'
            '-webkit-mask-image:linear-gradient(to bottom,rgba(0,0,0,.9),transparent 30%)">')


def feed():
    W, H = 1080, 1350
    b = (negro(W, H, 540, 1080)
         + shot(540, 1080, 450)
         + P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Sábado</div>'
         + '<div style="position:absolute;left:0;right:0;top:170px;text-align:center">'
           '<div class="h" style="font-size:230px;line-height:.86">Un shot.</div>'
           f'<div class="h" style="font-size:150px;line-height:.9;color:{OR}">Y a entrenar.</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;bottom:62px;text-align:center">'
           '<div class="lab" style="color:#d8d3cb">Guaraná Shot OstroVit · 80 ml · Pera</div>'
           f'<div style="font-size:21px;color:#8d8880;margin-top:14px;font-weight:500">{NOTA}</div></div>')
    return P.page(W, H, b, 'rgba(0,0,0,0)')


def banda(top, alto, contenido):
    """Franja panorámica de cine: estudio con foco dentro, negro puro afuera, filos finos."""
    return (f'<div style="position:absolute;left:0;right:0;top:{top}px;height:{alto}px;overflow:hidden;'
            'background:radial-gradient(ellipse 45% 70% at 50% 55%,#2c2622 0%,#15110e 55%,#0a0807 100%)">'
            f'<div style="position:absolute;left:0;right:0;bottom:0;height:{int(alto * .3)}px;'
            'background:linear-gradient(180deg,rgba(255,255,255,0),rgba(255,255,255,.03) 40%,rgba(0,0,0,.55))"></div>'
            f'{contenido}</div>'
            f'<div style="position:absolute;left:0;right:0;top:{top}px;height:1px;background:rgba(255,230,210,.10)"></div>'
            f'<div style="position:absolute;left:0;right:0;top:{top + alto}px;height:1px;background:rgba(255,230,210,.10)"></div>')


def h_cine():
    SW, SH = 1080, 1920
    alto = 760
    top = 640
    b = ('<div style="position:absolute;inset:0;background:#060504"></div>'
         + banda(top, alto, P.heroe('p_guarana.png', 540, 650, 540))
         + P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Sábado</div>'
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center">'
           '<div class="h" style="font-size:150px">Sábado.</div>'
           f'<div class="h o" style="font-size:150px">Se entrena.</div></div>'
         + f'<div style="position:absolute;left:0;right:0;top:{top + alto + 60}px;text-align:center">'
           '<div class="lab" style="color:#d8d3cb">Guaraná Shot · 80 ml · Pera</div>'
           f'<div style="width:80px;height:2px;background:{OR};margin:28px auto"></div>'
           '<div style="font-weight:600;font-size:26px;letter-spacing:5px;text-transform:uppercase;color:#c9c4bd">Pídelo por DM</div></div>'
         + f'<div style="position:absolute;left:90px;right:90px;bottom:262px;text-align:center;font-size:22px;color:#8d8880;font-weight:500">{NOTA}</div>')
    return P.page(SW, SH, b, 'rgba(0,0,0,0)')


def h_encuesta():
    SW, SH = 1080, 1920
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Esto o esto</div>'
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Al bolso</div>'
           '<div class="h" style="font-size:190px;margin-top:22px">¿Shot</div><div class="h o" style="font-size:190px">o barra?</div></div>'
         + P.heroe('p_guarana.png', 270, 1450, 400)
         + f'<img class="prod" src="{P.I("p_barra.png")}" style="left:540px;top:1240px;width:450px;transform:rotate(-12deg)">'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">Guaraná Shot pera · Barra Space Protein XXL coco</div>'
         + f'<div style="position:absolute;left:90px;right:90px;bottom:256px;text-align:center;font-size:20px;color:#8d8880;font-weight:500">{NOTA}</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.08)')


if __name__ == '__main__':
    P.render([('1_guarana_un_shot', feed())], FEED_OUT, 1080, 1350)
    P.render([('1_sabado_se_entrena', h_cine()), ('2_shot_o_barra', h_encuesta())], HIST_OUT, 1080, 1920)
