"""Miércoles 28 oct · "Producto de la semana" (estilo premium, semana de la energía): Lipo 6 Black Ultra Concentrate.
Paquete liviano (ajuste del 26 oct): 3 historias, la última con encuesta (espacio libre ~300 px).
Idea nueva: "NO ES PARA TI SI…" (transparencia: decir para quién no es el producto genera confianza).
Lipo 6 se presenta como termogénico con cafeína para energía al entrenar; nunca como "baja kilos".
Cafeína 30-60 min antes (ISSN). Uso (desde kit/build): python3 stories_producto_lipo.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

W, H = P.SW, P.SH
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Producto de la semana</div>'
LIPO = 'Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas.'
NOTA = f'<div class="foot" style="left:80px;right:80px;bottom:270px;font-size:18px;letter-spacing:2px;line-height:1.5">{LIPO}</div>'


def heroe_lipo():
    b = (P.marca(70, 150) + TOP + P.heroe('p_lipo.png', 780, 1600, 780, 5)
         + '<div style="position:absolute;left:80px;top:330px;width:560px"><div class="lab">Lipo 6 Black · Nutrex</div>'
           '<div class="h" style="font-size:150px;margin-top:22px">Energía</div><div class="h" style="font-size:150px">en una</div>'
           '<div class="h o" style="font-size:150px">cápsula.</div></div>'
         + '<div style="position:absolute;left:80px;width:380px;top:960px"><div class="rule" style="margin-bottom:26px"></div>'
           '<div style="font-size:40px;line-height:1.28;font-weight:500;color:#e8e4dd">Termogénico con cafeína para llegar con todo al entreno.</div>'
           '<div class="foot" style="position:static;margin-top:30px;font-size:20px;letter-spacing:3px">60 cápsulas · 1 antes de entrenar</div></div>'
         + NOTA)
    return P.page(W, H, b, 'rgba(200,150,40,.13)')


def no_es_para_ti():
    filas = [
        ('Eres menor de edad', 'o estás embarazada.'),
        ('Ya tomaste café', 'o un shot ese día.'),
        ('Entrenas de noche', 'y te cuesta dormir.'),
        ('Tomas medicamentos', 'o tienes una enfermedad: consulta a tu médico.'),
    ]
    rows = ''.join(
        f'<div style="padding:34px 0;border-top:1px solid rgba(244,241,236,.14)">'
        f'<div class="h" style="font-size:84px">{a}</div>'
        f'<div style="font-size:36px;color:#bdb8b0;font-weight:500;margin-top:8px">{c}</div></div>' for a, c in filas)
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:330px"><div class="lab">Siendo honestos</div>'
           '<div class="h" style="font-size:150px;margin-top:22px">No es para ti</div><div class="h o" style="font-size:150px">si…</div>'
           f'<div style="margin-top:46px">{rows}</div>'
           '<div style="font-size:36px;color:#e8e4dd;font-weight:500;margin-top:30px">¿Dudas? Pregúntanos por DM antes de comprar.</div></div>'
         + NOTA)
    return P.page(W, H, b, 'rgba(242,106,27,.07)')


def encuesta():
    # espacio libre 1150-1480 para el sticker de encuesta
    b = (P.marca(70, 150) + TOP + P.heroe('p_lipo.png', 910, 1060, 440, -6)
         + '<div style="position:absolute;left:80px;top:360px;width:640px"><div class="lab">Tu turno</div>'
           '<div class="h" style="font-size:130px;margin-top:22px">¿Has probado</div><div class="h" style="font-size:130px">un</div>'
           '<div class="h o" style="font-size:130px">termogénico?</div>'
           '<div style="font-size:38px;color:#bdb8b0;margin-top:30px;font-weight:500;width:520px">Si tienes dudas, escríbenos por DM y te contamos cómo usarlo.</div></div>'
         + NOTA)
    return P.page(W, H, b, 'rgba(200,150,40,.11)')


if __name__ == '__main__':
    P.render([('1_lipo6_energia_en_una_capsula', heroe_lipo()), ('2_no_es_para_ti_si', no_es_para_ti()),
              ('3_encuesta_termogenico', encuesta())], OUT, W, H)
