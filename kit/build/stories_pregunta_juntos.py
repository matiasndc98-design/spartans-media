"""Historias 9:16 (estilo SOBRIO) · martes 24 nov 2026, "Pregunta espartana" de la semana de la energía.
1: "¿Lipo 6 y Guaraná juntos?" (encuesta Sí / No en el espacio libre ~760–1080; la respuesta no está a la vista).
2: "No. Elige uno." Juntos suman 422 mg de cafeína (222 + 200) + caja de preguntas en el espacio libre ~760–1080.
Sin precios, sin numeración. Notas de cafeína obligatorias.
Uso (desde kit/build): python3 stories_pregunta_juntos.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

SW, SH = 1080, 1920
NOTA = ('Contiene cafeína: Lipo 6 Black 222 mg por cápsula · Guaraná Shot 200 mg por shot. '
        'No apto para menores ni embarazadas.')


def nota():
    return (f'<div style="position:absolute;left:90px;right:90px;bottom:262px;text-align:center;font-size:24px;'
            f'line-height:1.45;color:#9b958d;letter-spacing:1px">{NOTA}</div>')


def h_pregunta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Pregunta espartana</div>'
           '<div class="h" style="font-size:180px;margin-top:26px">¿Se pueden</div><div class="h o" style="font-size:180px">tomar juntos?</div>'
           '<div style="font-size:40px;color:#c9c4bc;margin-top:26px;font-weight:500">Lipo 6 Black y Guaraná Shot.</div></div>'
         + P.heroe('p_lipo.png', 360, 1500, 400) + P.heroe('p_guarana.png', 730, 1500, 430)
         + nota())
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h_respuesta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">La respuesta</div>'
           '<div class="h" style="font-size:180px;margin-top:22px">No.</div><div class="h o" style="font-size:180px">Elige uno.</div>'
           '<div style="font-size:40px;color:#c9c4bc;margin-top:26px;font-weight:500">Los dos tienen cafeína: juntos suman 422 mg.</div>'
           '<div class="lab" style="margin-top:34px">¿Otra duda? Déjala aquí</div></div>'
         + P.heroe('p_lipo.png', 360, 1500, 400) + P.heroe('p_guarana.png', 730, 1500, 430)
         + nota())
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


if __name__ == '__main__':
    P.render([('1_se_pueden_tomar_juntos', h_pregunta()), ('2_no_elige_uno', h_respuesta())], OUT, SW, SH)
