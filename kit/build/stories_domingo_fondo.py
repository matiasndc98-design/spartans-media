"""Historias 9:16 (estilo SOBRIO) · domingo 22 nov 2026: resumen y llamado al DM, abre la semana de la energía.
Idea nueva: FONDO DE PANTALLA PARA GUARDAR (tendencia de marcas grandes: wallpapers de marca que la gente
descarga y usa; optimiza capturas y envíos). Casco grande en set oscuro + "Se entrena." abajo, zona del reloj libre.
1: "Tu fondo de la semana." (wallpaper, haz captura).
2: "Esta semana: Energía." Lipo 6 Black como héroe + nota de cafeína; espacio libre ~680–1040 para la caja de preguntas.
Sin precios, sin numeración. Uso (desde kit/build): python3 stories_domingo_fondo.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P
import gen

SW, SH = 1080, 1920
NOTA_LIPO = 'Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas.'


def h_fondo():
    b = ('<div style="position:absolute;left:0;right:0;top:640px;height:900px;'
         'background:radial-gradient(ellipse 42% 45% at 50% 50%,rgba(242,106,27,.16),transparent 70%)"></div>'
         f'<img src="{gen.HELMET}" style="position:absolute;left:50%;top:700px;width:560px;transform:translateX(-50%);'
         'filter:drop-shadow(0 30px 60px rgba(0,0,0,.8))">'
         '<div style="position:absolute;left:0;right:0;top:1330px;text-align:center">'
         '<div class="h" style="font-size:170px">Se <span class="o">entrena.</span></div>'
         '<div class="lab" style="margin-top:24px;color:#8d8880">Lunes a domingo</div></div>'
         '<div class="foot" style="left:0;right:0;bottom:285px;text-align:center;color:#c9c4bd">'
         'Tu fondo de la semana · Haz captura</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.04)')


def h_energia():
    b = (P.marca(70, 280)
         + '<div style="position:absolute;left:70px;top:380px"><div class="lab">Esta semana</div>'
           '<div class="h o" style="font-size:200px;margin-top:20px">Energía.</div>'
           '<div style="font-weight:500;font-size:34px;color:#c9c4bd;margin-top:18px;letter-spacing:1px">'
           'Pregunta lo que quieras. Te respondemos.</div></div>'
         + P.heroe('p_lipo.png', 760, 1600, 560)
         + '<div style="position:absolute;left:70px;top:1180px;width:360px">'
           '<div style="font-family:Bebas;font-size:110px;line-height:.9">60</div>'
           '<div class="lab" style="margin-top:10px;color:#c9c4bd">Cápsulas</div>'
           '<div class="foot" style="position:static;margin-top:40px;color:#f4f1ec">Lipo 6 Black<br>Pídelo por DM</div>'
           f'<div style="margin-top:40px;font-weight:500;font-size:26px;line-height:1.3;color:#8d8880;letter-spacing:1px">{NOTA_LIPO}</div></div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.08)')


if __name__ == '__main__':
    P.render([('1_tu_fondo_de_la_semana', h_fondo()), ('2_esta_semana_energia', h_energia())], OUT, SW, SH)
