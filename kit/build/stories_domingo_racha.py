"""Domingo 1 nov · "Resumen y llamado al DM" (estilo premium, paquete liviano: 3 historias).
Cierra la semana de la energía y abre la de base y constancia (1–7 nov).
Idea nueva: CALENDARIO DE RACHA PARA SACARLE CAPTURA (noviembre = 30 días = 30 porciones del multivitamínico USN):
el seguidor guarda la historia y marca sus días. Última historia con encuesta (espacio libre 900–1230).
Uso (desde kit/build): python3 stories_domingo_racha.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

W, H = P.SW, P.SH
CAF2 = ('<div class="foot" style="left:80px;right:80px;bottom:270px;font-size:18px;letter-spacing:2px;line-height:1.5">'
        'Guaraná Shot: contiene cafeína (200 mg por shot). Lipo 6: contiene cafeína (222 mg por cápsula).<br>'
        'No aptos para menores ni embarazadas.</div>')


def resumen():
    filas = [('01', '30 a 60 min antes.', 'Ahí conviene la cafeína (ISSN).'),
             ('02', 'Dura más de lo que crees.', 'Cerca de 5 h después queda la mitad.'),
             ('03', 'Elige uno.', 'Shot o cápsula. Nunca los dos.')]
    lista = ''.join(
        f'<div style="display:flex;gap:34px;align-items:flex-start;margin-bottom:46px">'
        f'<div class="h o" style="font-size:90px;width:110px">{n}</div>'
        f'<div><div class="h" style="font-size:70px">{a}</div><div style="font-size:38px;color:#bdb8b0;font-weight:500;margin-top:6px">{b}</div></div></div>'
        for n, a, b in filas)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:162px">Semana de la energía</div>'
         + '<div style="position:absolute;left:80px;top:330px"><div class="lab o" style="color:#F26A1B">Fin de temporada</div>'
           '<div class="h" style="font-size:150px;margin-top:20px">Lo que nos</div><div class="h o" style="font-size:150px">dejó la semana.</div></div>'
         + f'<div style="position:absolute;left:80px;right:60px;top:760px">{lista}</div>'
         + '<div style="position:absolute;left:80px;top:1390px"><div class="rule" style="width:120px"></div>'
           '<div class="h" style="font-size:64px;margin-top:30px">¿Te quedaste sin? <span class="o">Pídelo por DM.</span></div></div>'
         + CAF2)
    return P.page(W, H, b, 'rgba(200,40,30,.10)')


def racha():
    celdas = ''
    for d in range(1, 31):
        hoy = d == 1
        st = ('background:#F26A1B;color:#060504;border-color:#F26A1B' if hoy else '')
        celdas += (f'<div class="h" style="height:96px;border:2px solid rgba(244,241,236,.22);border-radius:14px;display:flex;'
                   f'align-items:center;justify-content:center;font-size:54px;padding-top:6px;{st}">{d}</div>')
    dias = ''.join(f'<div class="lab" style="text-align:center;font-size:22px">{x}</div>' for x in 'DLMMJVS')
    # noviembre 2026 parte en domingo: el 1 cae en la primera columna
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Sácale captura</div>'
         + '<div style="position:absolute;left:80px;top:310px"><div class="lab">Base y constancia</div>'
           '<div class="h" style="font-size:180px;margin-top:16px">Noviembre.</div>'
           '<div class="h o" style="font-size:96px">30 días. Tu racha.</div></div>'
         + '<div style="position:absolute;left:80px;width:640px;top:720px">'
           f'<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:12px;margin-bottom:14px">{dias}</div>'
           f'<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:12px">{celdas}</div></div>'
         + P.heroe('p_multi.png', 880, 1330, 420)
         + '<div style="position:absolute;left:80px;right:80px;top:1440px">'
           '<div style="font-size:40px;color:#cfcac2;font-weight:500;line-height:1.35">Marca cada día que cumples. El multivitamínico USN trae 30 porciones: una al día, justo el mes.</div>'
           '<div class="foot" style="position:static;margin-top:22px;color:#F26A1B">Pídelo por DM</div></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


def encuesta():
    # sticker de encuesta en 900–1230 (libre)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:162px">Desde hoy</div>'
         + '<div style="position:absolute;left:0;right:0;top:340px;text-align:center"><div class="lab o" style="color:#F26A1B">Encuesta</div>'
           '<div class="h" style="font-size:170px;margin-top:40px">¿Te sumas a</div><div class="h o" style="font-size:170px">la racha?</div>'
           '<div style="font-size:38px;line-height:1.3;font-weight:500;color:#cfcac2;margin:30px auto 0;width:820px">30 días sin fallarle al gym ni a lo básico.</div></div>'
         + P.heroe('p_omega.png', 400, 1500, 320, -4) + P.heroe('p_multi.png', 680, 1500, 340, 4)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:270px">Multivitamínico USN · Omega 3 USN · Pídelos por DM</div>')
    return P.page(W, H, b, 'rgba(60,110,170,.12)')


if __name__ == '__main__':
    P.render([('1_lo_que_nos_dejo', resumen()), ('2_noviembre_tu_racha', racha()), ('3_te_sumas_encuesta', encuesta())], OUT, W, H)
