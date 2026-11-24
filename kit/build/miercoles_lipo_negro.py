"""Miércoles 25 nov 2026 · producto de la semana (energía, estilo SOBRIO).
Idea nueva: NEGRO SOBRE NEGRO / LOW KEY CON LUZ DE CONTORNO (tendencia de still life "tone-on-tone" 2026:
set del mismo color que el envase, sin piso iluminado; el envase negro solo se dibuja por una luz de contorno
cálida en los bordes y un brillo vertical en el frasco).
Feed (4:5, Metricool 10 AM): Lipo 6 Black Ultra Concentrate "Energía. En negro." · 60 cápsulas · una al día.
Historias 9:16: 1 "Termogénico. Con cafeína." · 2 encuesta "¿Usas algo antes de entrenar?" (espacio libre ~760–1080).
Sin precios, sin numeración, nota de cafeína en todas. Uso (desde kit/build):
python3 miercoles_lipo_negro.py <feed_dir> <hist_dir>
"""
import sys
FEED_OUT = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST_OUT = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
IMG = 'p_lipo.png'
NOTA = 'Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas.'


def set_negro(cx, floor_y):
    """Set negro total: solo un halo muy tenue detrás del envase y un piso apenas insinuado."""
    return (
        '<div style="position:absolute;inset:0;background:#030202"></div>'
        f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 30% 26% at {cx}px {floor_y - 380}px,'
        'rgba(242,106,27,.10),transparent 70%)"></div>'
        f'<div style="position:absolute;left:0;right:0;top:{floor_y}px;bottom:0;'
        f'background:radial-gradient(ellipse 30% 30% at {cx}px 0,#161009 0%,#070504 55%,#030202 100%)"></div>'
    )


def producto(cx, base_y, height):
    src = P.I(IMG)
    pos = f'position:absolute;left:{cx}px;top:{base_y}px;height:{height}px;'
    # luz de contorno: halo naranja fino pegado al borde + resplandor amplio muy suave
    rim = (f'<img src="{src}" style="{pos}transform:translate(-50%,-100%);'
           'filter:drop-shadow(0 0 2px rgba(242,106,27,.85)) drop-shadow(0 0 22px rgba(242,106,27,.28));opacity:1">')
    rim2 = ''
    prod = (f'<img src="{src}" style="{pos}transform:translate(-50%,-100%);'
            'filter:contrast(1.08) brightness(.82)">')
    # brillo vertical tipo luz de tira (strip light) sobre el frasco
    brillo = (f'<div style="position:absolute;left:{cx - int(height * .22)}px;top:{base_y - int(height * .97)}px;'
              f'width:{int(height * .05)}px;height:{int(height * .9)}px;'
              'background:linear-gradient(to bottom,rgba(255,240,225,.0),rgba(255,240,225,.22) 30%,rgba(255,240,225,.10) 80%,transparent);'
              'filter:blur(6px);mix-blend-mode:screen"></div>')
    refl = (f'<img src="{src}" style="{pos}transform:translate(-50%,0) scaleY(-1);opacity:.10;'
            '-webkit-mask-image:linear-gradient(to bottom,rgba(0,0,0,.9),transparent 30%)">')
    return rim2 + rim + refl + prod + brillo


def feed():
    W, H = 1080, 1350
    b = (set_negro(700, 1160)
         + producto(700, 1160, 700)
         + P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Producto de la semana</div>'
         + '<div style="position:absolute;left:70px;top:150px"><div class="h" style="font-size:150px;line-height:.9">Energía.</div>'
           f'<div class="h" style="font-size:150px;line-height:.9;color:{OR}">En negro.</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;bottom:62px">'
           '<div style="display:flex;justify-content:space-between;align-items:flex-end">'
           '<div><div class="lab" style="color:#d8d3cb">Lipo 6 Black Ultra Concentrate · Nutrex</div>'
           '<div style="font-size:34px;color:#c9c4bc;margin-top:10px;font-weight:500">60 cápsulas. Una al día.</div></div>'
           f'<div style="width:90px;height:2px;background:{OR};margin-bottom:18px"></div></div>'
           f'<div style="font-size:20px;color:#7d786f;margin-top:16px;letter-spacing:1px">{NOTA}</div></div>')
    return P.page(W, H, b, 'rgba(0,0,0,0)')


def h_negro():
    SW, SH = 1080, 1920
    b = (set_negro(560, 1520)
         + producto(560, 1520, 900)
         + P.marca(70, 150)
         + '<div style="position:absolute;left:70px;top:290px"><div class="lab">Producto de la semana</div>'
           '<div class="h" style="font-size:150px;line-height:.9;margin-top:20px">Termogénico.</div>'
           f'<div class="h" style="font-size:150px;line-height:.9;color:{OR}">Con cafeína.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:330px">Lipo 6 Black · 60 cápsulas · Pídelo por DM</div>'
         + f'<div style="position:absolute;left:80px;right:80px;bottom:262px;text-align:center;font-size:21px;color:#7d786f">{NOTA}</div>')
    return P.page(SW, SH, b, 'rgba(0,0,0,0)')


def h_encuesta():
    SW, SH = 1080, 1920
    # producto abajo a la derecha; espacio libre al centro (~760–1080) para el sticker de encuesta
    b = (set_negro(840, 1600)
         + producto(840, 1600, 480)
         + P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Antes de entrenar</div>'
           '<div class="h" style="font-size:150px;line-height:.92;margin-top:22px">¿Usas algo</div>'
           f'<div class="h" style="font-size:150px;line-height:.92;color:{OR}">antes?</div></div>'
         + '<div class="foot" style="left:70px;bottom:330px">Lipo 6 Black · Pídelo por DM</div>'
         + f'<div style="position:absolute;left:70px;width:560px;bottom:262px;font-size:21px;color:#7d786f">{NOTA}</div>')
    return P.page(SW, SH, b, 'rgba(0,0,0,0)')


if __name__ == '__main__':
    P.render([('1_lipo6_energia_en_negro', feed())], FEED_OUT, 1080, 1350)
    P.render([('1_termogenico_con_cafeina', h_negro()), ('2_usas_algo_antes', h_encuesta())], HIST_OUT, 1080, 1920)
