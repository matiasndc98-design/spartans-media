"""Historias 9:16 (estilo SOBRIO) · martes 10 nov 2026, "Pregunta espartana" de la semana de la creatina.
1: "¿Se toma sin entrenar?" (encuesta Sí / No en el espacio libre 700–1060; la respuesta no está a la vista).
2: "Sí. Todos los días." con Finaflex + caja de preguntas en el espacio libre 760–1080.
Sin precios, sin numeración. Uso (desde kit/build): python3 stories_pregunta_sin_entrenar.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

SW, SH = 1080, 1920


def h_pregunta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Pregunta espartana</div>'
           '<div class="h" style="font-size:170px;margin-top:26px">¿Los días que</div><div class="h o" style="font-size:170px">no entrenas?</div>'
           '<div style="font-size:38px;color:#c9c4bc;margin-top:26px;font-weight:500">¿La creatina se toma igual?</div></div>'
         + P.heroe('p_mt_sin.png', 540, 1580, 520)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Vota y mira la siguiente</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h_respuesta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">La respuesta</div>'
           '<div class="h o" style="font-size:230px;margin-top:22px">Sí.</div><div class="h" style="font-size:150px">Todos los días.</div>'
           '<div style="font-size:38px;color:#c9c4bc;margin-top:26px;font-weight:500">5 g al día, entrenes o no. Lo que cuenta es la constancia.</div></div>'
         + P.heroe('p_finaflex.png', 540, 1580, 500)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Finaflex 1 kg · 200 porciones · Pídela por DM</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.08)')


if __name__ == '__main__':
    P.render([('1_sin_entrenar', h_pregunta()), ('2_respuesta', h_respuesta())], OUT, SW, SH)
