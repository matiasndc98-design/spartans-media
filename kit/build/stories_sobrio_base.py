"""Domingo 1 nov (reemplazo) · historias en estilo SOBRIO de marca grande (decisión del dueño del 1 nov:
sin chistes, casi sin texto, poco educativo). Producto héroe + titular corto + un dato del envase.
Uso (desde kit/build): python3 stories_sobrio_base.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

W, H = P.SW, P.SH


def ficha(img, lab, t1, t2, dato, glow, alto=980):
    b = (P.marca(70, 150)
         + f'<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">{lab}</div>'
           f'<div class="h" style="font-size:150px;margin-top:26px">{t1}</div><div class="h o" style="font-size:150px">{t2}</div></div>'
         + P.heroe(img, 540, 1440, alto - 330)
         + f'<div class="foot" style="left:0;right:0;text-align:center;bottom:280px">{dato}</div>')
    return P.page(W, H, b, glow)


def encuesta():
    # sticker en 760–1080
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:340px;text-align:center"><div class="lab">Noviembre</div>'
           '<div class="h" style="font-size:150px;margin-top:26px">¿Cuál es</div><div class="h o" style="font-size:150px">tu base?</div></div>'
         + P.heroe('p_omega.png', 380, 1440, 400) + P.heroe('p_multi.png', 700, 1440, 430)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:280px">Pídelo por DM · Delivery en Caldera $1.500</div>')
    return P.page(W, H, b, 'rgba(60,110,170,.10)')


if __name__ == '__main__':
    P.render([
        ('1_multivitaminico', ficha('p_multi.png', 'USN · Super Daily Formula', 'Lo básico.', 'Todos los días.', '30 porciones · Pídelo por DM', 'rgba(242,106,27,.10)')),
        ('2_omega3', ficha('p_omega.png', 'USN · Fish Oil 1000 mg', 'Omega 3.', 'Sin saltarte un día.', '90 cápsulas blandas · Pídelo por DM', 'rgba(60,110,170,.12)')),
        ('3_cual_es_tu_base', encuesta()),
    ], OUT, W, H)
