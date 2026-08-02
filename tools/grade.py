#!/usr/bin/env python3
"""Единый грейд под палитру лендинга + кадрирование под слоты.

Сдержанно: холодим тени, оставляем тёплые света, лёгкая деконтрастность,
плёночное зерно и виньетка — чтобы кадры жили в одной среде со страницей.
"""
import numpy as np
from PIL import Image, ImageFilter
import sys, os

SRC = '/root/.claude/uploads/b403c9b0-9569-5772-adfc-27ab00fd906d'
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets')

JOBS = [
    # (исходник, имя на выходе, целевое соотношение, вертикальный якорь кадрирования 0..1)
    ('a428dba0-Gemini_Generated_Image_g8rxbwg8rxbwg8rx.png', 'still-scylla.jpg',    16/9,   0.50),
    ('5b5fe257-Gemini_Generated_Image_8g2v9g8g2v9g8g2v.png', 'still-cyclops.jpg',   16/9,   0.50),
    ('cf88e723-Gemini_Generated_Image_5edff35edff35edf.png', 'still-penelope.jpg',  2.2,    0.46),
    ('99a65c3d-Gemini_Generated_Image_bjoaqybjoaqybjoa.png', 'still-threshold.jpg', 16/9,   0.50),
]
MAXW = 2000


def crop_to(im, ratio, anchor=0.5):
    w, h = im.size
    cur = w / h
    if abs(cur - ratio) < 0.01:
        return im
    if cur > ratio:                     # шире нужного — режем по бокам от центра
        nw = int(round(h * ratio))
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = int(round(w / ratio))          # выше нужного — режем по вертикали от якоря
    y = int(round((h - nh) * anchor))
    return im.crop((0, y, w, y + nh))


def grade(img):
    f = img.astype(np.float32) / 255.0
    lum = f @ np.array([0.2126, 0.7152, 0.0722], np.float32)

    # маски теней и светов
    sh = np.clip(1.0 - lum * 2.1, 0, 1)[..., None]
    hi = np.clip((lum - 0.55) * 2.2, 0, 1)[..., None]

    # тени уводим в сине-чёрный (палитра #0c1522), света оставляем терракотовыми
    f += sh * np.array([-0.020, 0.004, 0.052], np.float32)
    f += hi * np.array([0.030, 0.004, -0.024], np.float32)

    # лёгкая деконтрастность в тенях: «плёночный» подъём чёрного
    f = f * (1.0 - 0.045) + 0.045 * np.clip(f * 1.25, 0, 1) ** 1.05
    f += 0.014 * sh[..., 0][..., None]

    # приглушаем насыщенность
    g = f @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    f = g[..., None] + (f - g[..., None]) * 0.90

    # мягкий S-контраст
    f = np.clip(f, 0, 1)
    f = f * f * (3 - 2 * f) * 0.34 + f * 0.66
    return np.clip(f, 0, 1) * 255.0


def halation(img, thresh=168, blur=20, gain=0.30):
    pil = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    l = np.array(pil.convert('L'), np.float32)
    m = np.clip((l - thresh) / (255 - thresh), 0, 1)
    m = np.array(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur)), np.float32)[..., None] / 255
    return img + m * np.array([255, 176, 118], np.float32)[None, None, :] * gain


def vignette(img, strength=0.34, power=1.8):
    h, w = img.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) / 1.42
    return img * np.clip(1 - strength * d ** power, 0, 1)[..., None]


def grain(img, amount=5.2, seed=3):
    h, w = img.shape[:2]
    r = np.random.default_rng(seed)
    n = r.normal(0, amount, (h, w, 1))
    lum = img.mean(axis=2, keepdims=True) / 255
    return img + n * (0.45 + 0.85 * (1 - lum))


for i, (src, dst, ratio, anchor) in enumerate(JOBS):
    p = os.path.join(SRC, src)
    if not os.path.exists(p):
        print('НЕТ ИСХОДНИКА:', src); continue
    im = Image.open(p).convert('RGB')
    im = crop_to(im, ratio, anchor)
    if im.size[0] > MAXW:
        im = im.resize((MAXW, int(round(MAXW / ratio))), Image.LANCZOS)
    a = grade(np.array(im, np.float32))
    a = halation(a)
    a = vignette(a)
    a = grain(a, seed=7 + i)
    out = os.path.join(OUT, dst)
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(out, quality=84, optimize=True, progressive=True)
    print(f'{dst:22s} {im.size[0]}x{im.size[1]}  {round(os.path.getsize(out)/1024)} KB')
