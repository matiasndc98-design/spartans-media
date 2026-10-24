"""Historias 9:16 (estilo premium) · domingo 25 oct: resumen de la semana de la proteína + llamado al DM
+ adelanto de la semana de la energía.
Idea nueva: formato SERIE DE STREAMING ("Fin de temporada" → "Próxima temporada" con guía de episodios L–S),
para que el cambio de tema semanal se sienta como una serie que se sigue.
Última historia con encuesta (~300 px libres para el sticker, 1000–1330).
Uso (desde kit/build): python3 stories_domingo_temporada.py <carpeta_salida>
"""
import sys
import premium as P

OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
SW, SH = P.SW, P.SH
OR = P.OR
CAF = ('<div class="foot" style="left:80px;right:80px;bottom:270px;font-size:19px;letter-spacing:2px;line-height:1.5;text-align:center">'
       'Lipo 6: contiene cafeína (222 mg por cápsula). Guaraná Shot: contiene cafeína (200 mg por shot).<br>'
       'No aptos para menores ni embarazadas. No los combines.</div>')


def h1():  # fin de temporada: lo que nos dejó la semana
    filas = [('01', 'Proteína los 7 días,', 'no solo cuando entrenas.'),
             ('02', 'No se pierde', 'si no la tomas al tiro.'),
             ('03', '1 scoop = 22 a 30 g.', 'La comida primero.')]
    lista = ''.join(
        f'<div style="display:flex;gap:34px;align-items:flex-start;margin-bottom:46px">'
        f'<div class="h o" style="font-size:90px;width:110px">{n}</div>'
        f'<div><div class="h" style="font-size:72px">{a}</div><div style="font-size:40px;color:#bdb8b0;font-weight:500;margin-top:6px">{b}</div></div></div>'
        for n, a, b in filas)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Semana de la proteína</div>'
         + '<div style="position:absolute;left:80px;top:330px"><div class="lab o" style="color:#F26A1B">Fin de temporada</div>'
           '<div class="h" style="font-size:150px;margin-top:20px">Lo que nos</div><div class="h o" style="font-size:150px">dejó la semana.</div></div>'
         + f'<div style="position:absolute;left:80px;right:60px;top:760px">{lista}</div>'
         + '<div class="rule" style="position:absolute;left:80px;bottom:300px;width:120px"></div>')
    return P.page(SW, SH, b, 'rgba(60,110,170,.12)')


def h2():  # llamado al DM con las 3 proteínas
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">¿Te quedaste sin?</div>'
           '<div class="h" style="font-size:190px;margin-top:44px">Pídela</div><div class="h o" style="font-size:190px">por DM.</div></div>'
         + P.heroe('p_iso100.png', 270, 1330, 470) + P.heroe('p_whey.png', 540, 1360, 540) + P.heroe('p_nitro.png', 815, 1330, 470)
         + '<div style="position:absolute;left:0;right:0;top:1420px;text-align:center">'
           '<div class="lab" style="color:#f4f1ec">Whey USN · ISO 100 · Nitro Tech</div>'
           '<div style="font-size:36px;color:#bdb8b0;font-weight:500;margin-top:22px;line-height:1.4">Delivery en Caldera $1.500 · Entregas en Copiapó<br>Envíos a todo Chile</div>'
           '<div class="foot" style="position:static;margin-top:26px;color:#F26A1B">Con creatina, shaker de regalo</div></div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h3():  # próxima temporada: guía de episodios
    eps = [('Lun', 'Cafeína: lo que sí y lo que no'), ('Mar', 'Pregunta espartana'), ('Mié', 'Producto de la semana'),
           ('Jue', 'Detrás de la tienda'), ('Sáb', 'Cero ganas de entrenar')]
    lista = ''.join(
        f'<div style="display:flex;align-items:baseline;gap:30px;padding:20px 0;border-bottom:1px solid rgba(244,241,236,.12)">'
        f'<div class="lab o" style="color:#F26A1B;width:90px">{d}</div><div style="font-size:42px;font-weight:600;text-transform:uppercase;letter-spacing:1px">{t}</div></div>'
        for d, t in eps)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px;color:#F26A1B">Desde mañana</div>'
         + '<div style="position:absolute;left:80px;top:310px"><div class="lab">Próxima temporada</div>'
           '<div class="h" style="font-size:250px;margin-top:14px">Energía</div><div class="h o" style="font-size:120px">para entrenar.</div></div>'
         + P.heroe('p_lipo.png', 860, 1060, 380, 6)
         + f'<div style="position:absolute;left:80px;right:80px;top:1090px">{lista}</div>'
         + CAF)
    return P.page(SW, SH, b, 'rgba(200,40,30,.12)')


def h4():  # encuesta: ¿a qué hora entrenas? (sticker en 920–1240)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Semana de la energía</div>'
         + '<div style="position:absolute;left:0;right:0;top:340px;text-align:center"><div class="lab o" style="color:#F26A1B">Encuesta</div>'
           '<div class="h" style="font-size:200px;margin-top:44px">¿A qué hora</div><div class="h o" style="font-size:200px">entrenas?</div>'
           '<div style="font-size:38px;line-height:1.3;font-weight:500;color:#cfcac2;margin:34px auto 0;width:800px">Con tu respuesta armamos la semana: cuándo conviene la cafeína y cuándo no.</div></div>'
         + P.heroe('p_guarana.png', 540, 1540, 290)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:270px;font-size:19px;letter-spacing:2px">Guaraná Shot: contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


if __name__ == '__main__':
    P.render([('1_fin_de_temporada', h1()), ('2_pidela_por_dm', h2()), ('3_proxima_temporada', h3()), ('4_a_que_hora_entrenas', h4())], OUT, SW, SH)
