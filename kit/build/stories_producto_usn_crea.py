"""Miércoles 4 nov 2026 · Producto de la semana (sin precio) · semana base y constancia · estilo SOBRIO.
Idea nueva: TEASER EN MACRO → REVELADO (como los lanzamientos de marcas grandes): la primera historia muestra
solo un detalle del envase en primerísimo plano; la segunda revela el producto completo, con espacio para
la caja de preguntas.
Uso (desde kit/build): python3 stories_producto_usn_crea.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

W, H = P.SW, P.SH
IMG = 'p_usn_crea.png'


def macro():
    # producto enorme: solo se ve un tramo de la etiqueta
    prod = f'<img class="prod" src="{P.I(IMG)}" style="left:50%;top:-170px;height:2100px;transform:translateX(-50%) rotate(-5deg)">'
    velo = ('<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,8,8,.92) 0%,rgba(8,8,8,.35) 22%,'
            'rgba(8,8,8,.1) 45%,rgba(8,8,8,.8) 63%,rgba(8,8,8,1) 68.5%)"></div>')
    b = (prod + velo + P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:1300px;text-align:center"><div class="lab">Producto de la semana</div>'
           '<div class="h" style="font-size:170px;margin-top:26px">Lo básico</div><div class="h o" style="font-size:170px">tiene nombre.</div>'
           '<div class="rule" style="margin:34px auto 0"></div></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.08)')


def revelado():
    # caja de preguntas en 610–890 (zona libre)
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">USN · Creatina 300 g</div>'
           '<div class="h" style="font-size:150px;margin-top:22px">Creatina.</div><div class="h o" style="font-size:150px">60 días.</div></div>'
         + P.heroe(IMG, 540, 1420, 520)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:280px">Sin sabor · 5 g al día · Pídela por DM</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render([('1_producto_semana', macro()), ('2_creatina_usn', revelado())], OUT, W, H)
