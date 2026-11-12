"""Jueves 12 nov 2026 · historias "Detrás de la tienda" (estilo SOBRIO, semana de la creatina).
1 "De aquí a tu casa." Finaflex 1 kg como héroe + formas de entrega reales (delivery Caldera $1.500, Copiapó, todo Chile).
2 Encuesta "¿Cómo lo prefieres?" Delivery / Retiro, con espacio libre ~760–1100 px para el sticker.
Sin precios de productos, sin numeración. Uso (desde kit/build): python3 stories_jueves_entrega.py <hist_dir>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
SW, SH = 1080, 1920


def h_casa():
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:161px">Detrás de la tienda</div>'
         + P.heroe('p_finaflex.png', 640, 1560, 860)
         + '<div style="position:absolute;left:70px;top:300px"><div class="lab">Cómo te llega</div>'
           '<div class="h" style="font-size:180px;line-height:.9;margin-top:20px">De aquí</div>'
           f'<div class="h" style="font-size:180px;line-height:.9;color:{OR}">a tu casa.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px;color:#d8d3cb">'
           'Delivery en Caldera $1.500 <span class="o">·</span> Copiapó <span class="o">·</span> Todo Chile</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


def h_encuesta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Tu pedido</div>'
           '<div class="h" style="font-size:180px;line-height:.92;margin-top:22px">¿Cómo lo</div>'
           f'<div class="h" style="font-size:180px;line-height:.92;color:{OR}">prefieres?</div></div>'
         + P.heroe('p_usn_crea.png', 400, 1580, 400) + P.heroe('p_shaker.png', 680, 1580, 420)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Delivery $1.500 o retiro en Caldera · Pídelo por DM</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.08)')


if __name__ == '__main__':
    P.render([('1_de_aqui_a_tu_casa', h_casa()), ('2_como_lo_prefieres', h_encuesta())], OUT, SW, SH)
