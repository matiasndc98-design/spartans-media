"""Jueves 26 nov 2026 · historias "Detrás de la tienda" (estilo SOBRIO), acompañan el reel "¿Es original?".
1 "Llega sellado. Lo abres tú." ISO 100 en recorte grande (productos originales y sellados, DM, delivery).
2 Encuesta "¿Revisas el sello?" (Siempre / A veces) con Nitro Tech y Finaflex abajo; espacio libre ~720–1080 px para el sticker.
Sin precios de productos, sin numeración, sin emojis.
Uso (desde kit/build): python3 stories_jueves_sellado.py <hist_dir>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
SW, SH = 1080, 1920


def h_sellado():
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:161px">Detrás de la tienda</div>'
         + '<div style="position:absolute;left:70px;top:300px"><div class="lab">Original y sellado</div>'
           '<div class="h" style="font-size:180px;line-height:.9;margin-top:20px">Llega sellado.</div>'
           f'<div class="h" style="font-size:180px;line-height:.9;color:{OR}">Lo abres tú.</div></div>'
         + P.heroe('p_iso100.png', 560, 1560, 820)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px;color:#d8d3cb">Pídelo por DM</div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">'
           'Delivery en Caldera $1.500 <span class="o">·</span> Copiapó <span class="o">·</span> Todo Chile</div>')
    return P.page(SW, SH, b, 'rgba(60,110,170,.16)')


def h_encuesta():
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:161px">Detrás de la tienda</div>'
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Cuando compras</div>'
           f'<div class="h" style="font-size:210px;line-height:.92;margin-top:22px">¿Revisas</div>'
           f'<div class="h" style="font-size:210px;line-height:.92;color:{OR}">el sello?</div></div>'
         + P.heroe('p_nitro.png', 380, 1600, 440) + P.heroe('p_finaflex.png', 700, 1600, 400)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Original y sellado <span class="o">·</span> Siempre</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render([('1_llega_sellado', h_sellado()), ('2_revisas_el_sello', h_encuesta())], OUT, SW, SH)
