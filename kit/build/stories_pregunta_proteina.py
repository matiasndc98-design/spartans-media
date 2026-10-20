"""Martes 20 oct · "Pregunta espartana" (estilo premium): ¿proteína los días que no entrenas?
Idea nueva: semana visual L-M-M-J-V-S-D (entrenas 4 días, la proteína va los 7).
Secuencia: quiz (espacio para sticker) -> respuesta con la semana -> día de descanso con Whey USN -> caja de preguntas.
Uso (desde kit/build): python3 stories_pregunta_proteina.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
W, H = P.SW, P.SH
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Pregunta espartana</div>'


def h1():
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:390px"><div class="lab">Responde</div>'
           '<div class="h" style="font-size:170px;margin-top:24px">¿Proteína los días</div><div class="h o" style="font-size:170px">que no entrenas?</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">La respuesta en la siguiente</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.08)')


def semana():
    dias = ['L', 'M', 'M', 'J', 'V', 'S', 'D']
    gym = [1, 0, 1, 0, 1, 1, 0]
    cols = ''
    for d, g in zip(dias, gym):
        bar = (f'<div style="height:8px;width:56px;margin:0 auto;background:{"#f4f1ec" if g else "rgba(244,241,236,.12)"};border-radius:4px"></div>')
        dot = f'<div style="height:56px;width:56px;margin:26px auto 0;border-radius:50%;background:{OR};box-shadow:0 0 30px rgba(242,106,27,.45)"></div>'
        cols += (f'<div style="flex:1;text-align:center"><div class="h" style="font-size:80px;color:{"#f4f1ec" if g else "#6f6a63"}">{d}</div>'
                 f'<div style="margin-top:22px">{bar}</div>{dot}</div>')
    leyenda = ('<div style="display:flex;gap:60px;justify-content:center;margin-top:46px" class="lab">'
               '<span><span style="display:inline-block;width:40px;height:8px;background:#f4f1ec;border-radius:4px;vertical-align:middle;margin-right:14px"></span>Entrenas</span>'
               f'<span><span style="display:inline-block;width:26px;height:26px;background:{OR};border-radius:50%;vertical-align:middle;margin-right:14px"></span>Proteína</span></div>')
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:360px"><div class="lab">La respuesta</div>'
           '<div class="h o" style="font-size:300px;margin-top:70px">Sí.</div><div class="h" style="font-size:130px">Los 7 días.</div></div>'
         + f'<div style="position:absolute;left:60px;right:60px;top:960px"><div style="display:flex">{cols}</div>{leyenda}</div>'
         + '<div style="position:absolute;left:80px;right:80px;top:1340px"><div class="rule" style="margin-bottom:26px"></div>'
           '<div style="font-size:42px;line-height:1.25;font-weight:500;color:#e8e4dd">El músculo se recupera cuando descansas. Lo que cuenta es la proteína total del día, entrenes o no.</div></div>'
         + '<div class="foot" style="left:80px;bottom:270px;font-size:18px">Referencia: Sociedad Internacional de Nutrición Deportiva (ISSN)</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.07)')


def descanso():
    b = (P.marca(70, 150) + TOP + P.heroe('p_whey.png', 700, 1560, 700)
         + '<div style="position:absolute;left:80px;top:360px;width:600px"><div class="lab">Día de descanso</div>'
           '<div class="h" style="font-size:150px;margin-top:20px">Comida</div><div class="h" style="font-size:150px">primero.</div>'
           '<div class="h o" style="font-size:110px;margin-top:20px">El scoop, si no llegas.</div></div>'
         + '<div style="position:absolute;left:80px;top:1000px;width:330px"><div class="rule" style="margin-bottom:22px"></div>'
           '<div class="h" style="font-size:110px">22 g</div><div class="lab" style="margin-top:8px;line-height:1.5">de proteína por scoop · Whey USN</div></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:270px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídela por DM <span class="o">·</span> Con creatina, shaker de regalo</div>')
    return P.page(W, H, b, 'rgba(120,70,30,.16)')


def caja():
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:400px;text-align:center"><div class="lab">Tu turno</div>'
           '<div class="h" style="font-size:190px;margin-top:24px">¿Qué duda</div><div class="h o" style="font-size:190px">tienes?</div>'
           '<div style="font-size:40px;color:#bdb8b0;margin-top:30px;font-weight:500">La respondemos el próximo martes.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">Proteína, creatina, lo que sea</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.09)')


if __name__ == '__main__':
    P.render([('1_quiz_proteina_descanso', h1()), ('2_respuesta_7_dias', semana()), ('3_dia_de_descanso', descanso()), ('4_caja_de_preguntas', caja())], OUT, W, H)
