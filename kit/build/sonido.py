"""Banda sonora original para los reels (sin derechos de autor): efectos sincronizados con las animaciones + base rítmica.
Lo usa reel.py: sonido.pista(eventos, duracion, salida_wav).
eventos: lista de (segundos, nombre_animacion). Cada animación CSS conocida suena con su efecto.
"""
import numpy as np
import wave

SR = 44100
rng = np.random.default_rng(7)


def _t(d):
    return np.arange(int(SR * d)) / SR


def _lp(x, k):
    # pasa bajos simple (media móvil)
    if k <= 1:
        return x
    return np.convolve(x, np.ones(k) / k, mode='same')


def impacto(d=0.7):
    t = _t(d)
    f = 40 + 90 * np.exp(-t * 18)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 5)
    ruido = _lp(rng.standard_normal(len(t)), 6) * np.exp(-t * 30)
    return 0.9 * sub + 0.35 * ruido


def whoosh(d=0.45):
    t = _t(d)
    n = rng.standard_normal(len(t))
    env = np.sin(np.pi * t / d) ** 2
    a = _lp(n, 3) - _lp(n, 25)
    return 0.45 * a * env


def swish(d=0.22):
    return whoosh(d) * 0.6


def pop(d=0.12):
    t = _t(d)
    f = 520 + 700 * t / d
    return 0.5 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 28)


def tick(d=0.05):
    t = _t(d)
    return 0.45 * np.sin(2 * np.pi * 1800 * t) * np.exp(-t * 90)


def subida(d=0.9):
    t = _t(d)
    f = 250 + 900 * (t / d) ** 2
    s = np.sin(2 * np.pi * np.cumsum(f) / SR)
    n = _lp(rng.standard_normal(len(t)), 2) - _lp(rng.standard_normal(len(t)), 30)
    return (0.22 * s + 0.15 * n) * (t / d)


def sello(d=0.35):
    return impacto(d) * 0.8 + np.pad(tick(), (0, int(SR * d) - int(SR * 0.05))) * 0.6


EFECTOS = {'flash': [(0.0, impacto, 0.75), (-0.18, whoosh, 0.7)], 'slam': [(0.12, impacto, 0.55)],
           'pop': [(0.0, pop, 0.8)], 'inL': [(-0.02, swish, 0.55)], 'rise': [(0.0, swish, 0.35)],
           'stamp': [(0.15, sello, 0.9)], 'tick': [(0.1, tick, 0.9)], 'gx': [(0.0, subida, 0.8)]}


def base(dur, bpm=140, vol=0.32):
    """Base rítmica oscura tipo trap/phonk: bombo + 808, palmas, hi-hats."""
    out = np.zeros(int(SR * dur) + SR)
    beat = 60 / bpm
    t = _t(0.5)
    kick = np.sin(2 * np.pi * np.cumsum(45 + 110 * np.exp(-t * 35)) / SR) * np.exp(-t * 7)
    t8 = _t(0.9)
    b808 = np.tanh(2.2 * np.sin(2 * np.pi * 49 * t8)) * np.exp(-t8 * 3.2) * 0.55
    tc = _t(0.25)
    clap = (_lp(rng.standard_normal(len(tc)), 2) - _lp(rng.standard_normal(len(tc)), 20)) * np.exp(-tc * 22) * 0.7
    th = _t(0.05)
    hat = (rng.standard_normal(len(th)) - _lp(rng.standard_normal(len(th)), 4)) * np.exp(-th * 120) * 0.25

    def add(x, s):
        i = int(s * SR)
        if i < len(out):
            out[i:i + len(x)] += x[:len(out) - i]
    bar = beat * 4
    n = int(dur / bar) + 1
    for b in range(n):
        s0 = b * bar
        for k in (0, 1.5, 2.75):
            add(kick, s0 + k * beat); add(b808, s0 + k * beat)
        for k in (1, 3):
            add(clap, s0 + k * beat)
        for k in range(8):
            add(hat * (1.0 if k % 2 == 0 else 0.6), s0 + k * beat / 2)
    return out[:int(SR * dur)] * vol


def pista(eventos, dur, salida, con_base=False):
    out = np.zeros(int(SR * dur) + SR * 2)
    usados = []
    for s, nombre in sorted(eventos):
        for off, fn, g in EFECTOS.get(nombre, []):
            st = max(0.0, s + off)
            if any(abs(st - u) < 0.09 and nm == nombre for u, nm in usados):
                continue
            usados.append((st, nombre))
            x = fn() * g
            i = int(st * SR)
            out[i:i + len(x)] += x[:len(out) - i]
    out = out[:int(SR * dur)]
    if con_base:
        out = out * 0.9 + base(dur)
    fade = int(SR * 0.6)
    out[-fade:] *= np.linspace(1, 0, fade)
    out = np.tanh(out * 1.6) * 0.9  # limitador suave
    st = (np.stack([out, out], 1) * 32767).astype('<i2')
    with wave.open(salida, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
