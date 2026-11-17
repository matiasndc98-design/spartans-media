"""Historias 9:16 (estilo SOBRIO) · martes 17 nov 2026, "Pregunta espartana" de la semana de la proteína.
1: "¿Whey o isolate? ¿Qué cambia?" Whey USN + ISO 100 (encuesta Sí / No en el espacio libre 760–1080; la respuesta no está a la vista).
2: "Se filtra más." ISO 100 + caja de preguntas en el espacio libre 780–1100.
Sin precios, sin numeración. Uso (desde kit/build): python3 stories_pregunta_isolate.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

SW, SH = 1080, 1920


def h_pregunta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Pregunta espartana</div>'
           '<div class="h" style="font-size:190px;margin-top:26px">¿Whey o</div><div class="h o" style="font-size:190px">isolate?</div>'
           '<div style="font-size:40px;color:#c9c4bc;margin-top:26px;font-weight:500">¿Sabes qué cambia?</div></div>'
         + P.heroe('p_whey.png', 330, 1600, 440) + P.heroe('p_iso100.png', 760, 1600, 470)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Vota y mira la siguiente</div>')
    return P.page(SW, SH, b, 'rgba(60,110,170,.12)')


def h_respuesta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">La respuesta</div>'
           '<div class="h" style="font-size:170px;margin-top:22px">El isolate</div><div class="h o" style="font-size:170px">se filtra más.</div>'
           '<div style="font-size:40px;color:#c9c4bc;margin-top:26px;font-weight:500">Queda más pura: menos lactosa y menos grasa.</div></div>'
         + P.heroe('p_iso100.png', 540, 1600, 500)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Dymatize ISO 100 · 25 g por scoop · 71 porciones · Pídela por DM</div>')
    return P.page(SW, SH, b, 'rgba(60,110,170,.14)')


if __name__ == '__main__':
    P.render([('1_whey_o_isolate', h_pregunta()), ('2_se_filtra_mas', h_respuesta())], OUT, SW, SH)
