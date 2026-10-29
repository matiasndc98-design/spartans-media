"""Jueves 29 oct · "Detrás de la tienda" (estilo premium, semana de la energía, paquete liviano: 3 historias).
Idea nueva "DETRÁS DEL DM": mostrar cómo ayudamos a elegir energía por DM (las 3 cosas que conviene contarnos
antes de elegir shot o cápsula). Transparencia y servicio, sin testimonios ni DMs inventados.
Última historia con slider "¿cuántos cafés tomas al día?" (espacio libre ~300 px). Notas de cafeína en todas.
Uso (desde kit/build): python3 stories_detras_dm.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

W, H = P.SW, P.SH
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Detrás del DM</div>'
NOTAS = ('Guaraná Shot: contiene cafeína (200 mg por shot). Lipo 6: contiene cafeína (222 mg por cápsula). '
         'No aptos para menores ni embarazadas.')
NOTA = f'<div class="foot" style="left:80px;right:80px;bottom:270px;font-size:18px;letter-spacing:2px;line-height:1.5">{NOTAS}</div>'


def portada():
    b = (P.marca(70, 150) + TOP + P.heroe('p_guarana.png', 400, 1560, 560, -4) + P.heroe('p_lipo.png', 760, 1560, 440, 5)
         + '<div style="position:absolute;left:80px;right:80px;top:330px"><div class="lab">Detrás de la tienda</div>'
           '<div class="h" style="font-size:150px;margin-top:22px">Tu energía</div><div class="h" style="font-size:150px">no se elige</div>'
           '<div class="h o" style="font-size:150px">al azar.</div>'
           '<div class="rule" style="margin:40px 0 26px"></div>'
           '<div style="font-size:40px;line-height:1.28;font-weight:500;color:#e8e4dd;width:760px">Por DM te ayudamos a elegir entre shot o cápsula. Solo cuéntanos 3 cosas.</div></div>'
         + NOTA)
    return P.page(W, H, b, 'rgba(200,150,40,.12)')


def tres_cosas():
    filas = [
        ('1', '¿A qué hora entrenas?', 'Si es de noche, ojo con el sueño.'),
        ('2', '¿Cuánto café tomas?', 'Todo suma: el tope del día son 400 mg.'),
        ('3', '¿Tomas algún medicamento?', 'Si es así, primero consulta a tu médico.'),
    ]
    rows = ''.join(
        f'<div style="display:flex;gap:36px;padding:40px 0;border-top:1px solid rgba(244,241,236,.14)">'
        f'<div class="h o" style="font-size:120px;width:70px">{n}</div><div>'
        f'<div class="h" style="font-size:80px">{a}</div>'
        f'<div style="font-size:36px;color:#bdb8b0;font-weight:500;margin-top:10px">{c}</div></div></div>' for n, a, c in filas)
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:330px"><div class="lab">Antes de elegir</div>'
           '<div class="h" style="font-size:140px;margin-top:22px">Cuéntanos</div><div class="h o" style="font-size:140px">3 cosas</div>'
           f'<div style="margin-top:46px">{rows}</div>'
           '<div style="font-size:36px;color:#e8e4dd;font-weight:500;margin-top:24px">Con eso te decimos cuál te conviene. Escríbenos por DM.</div></div>'
         + '<div class="foot" style="left:80px;bottom:330px;font-size:18px;letter-spacing:3px">Tope 400 mg al día en adultos sanos · EFSA</div>'
         + NOTA)
    return P.page(W, H, b, 'rgba(242,106,27,.07)')


def slider():
    # espacio libre 1130-1460 para el sticker slider
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:360px"><div class="lab">Tu turno</div>'
           '<div class="h" style="font-size:140px;margin-top:22px">¿Cuántos cafés</div><div class="h" style="font-size:140px">tomas</div>'
           '<div class="h o" style="font-size:140px">al día?</div>'
           '<div style="font-size:38px;color:#bdb8b0;margin-top:30px;font-weight:500;width:820px">Muévelo con honestidad. Te leemos por DM.</div></div>'
         + NOTA)
    return P.page(W, H, b, 'rgba(200,150,40,.10)')


if __name__ == '__main__':
    P.render([('1_tu_energia_no_al_azar', portada()), ('2_cuentanos_3_cosas', tres_cosas()),
              ('3_slider_cafes', slider())], OUT, W, H)
