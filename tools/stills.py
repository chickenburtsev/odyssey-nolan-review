#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Кадры, присланные пользователем: лёгкий грейд под палитру + кадрирование.
Обработка намеренно минимальная — это уже киноматериал, его не надо переделывать."""
import numpy as np
from PIL import Image, ImageFilter
import os

SRC = '/root/.claude/uploads/b403c9b0-9569-5772-adfc-27ab00fd906d'
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets')

JOBS = [
    # исходник, имя, соотношение (None — не резать), макс. ширина, сила грейда
    ('330d3dec-IMG_0288.jpeg', 'still-marble.jpg',  16/9,  1650, .55),
    ('724bf626-IMG_0291.WEBP', 'still-troy.jpg',    16/9,  1600, .5),
    ('d5b0a0a1-IMG_0290.JPG',  'still-voyage.jpg',  16/9,  780,  .5),
    ('95423489-IMG_0289.JPG',  'still-warrior.jpg', 16/9,  640,  .45),
    ('23271c13-IMG_0292.JPG',  'still-stacks.jpg',  1.0,   447,  .45),
]


def crop_to(im, ratio, anchor=.5):
    if ratio is None: return im
    w, h = im.size; cur = w/h
    if abs(cur-ratio) < .01: return im
    if cur > ratio:
        nw = int(round(h*ratio)); x = int((w-nw)*.5)
        return im.crop((x, 0, x+nw, h))
    nh = int(round(w/ratio)); y = int(round((h-nh)*anchor))
    return im.crop((0, y, w, y+nh))


def grade(a, k):
    f = a.astype(np.float32)/255.
    lum = f @ np.array([.2126,.7152,.0722], np.float32)
    sh = np.clip(1-lum*2.1, 0, 1)[...,None]
    hi = np.clip((lum-.58)*2.2, 0, 1)[...,None]
    f += sh*np.array([-.014,.003,.040], np.float32)*k     # тени в сине-чёрный
    f += hi*np.array([.022,.003,-.018], np.float32)*k     # света в терракоту
    g = f @ np.array([.2126,.7152,.0722], np.float32)
    f = g[...,None] + (f-g[...,None])*(1-.07*k)           # чуть приглушить цвет
    return np.clip(f,0,1)*255.


def vignette(a, s=.24):
    h,w = a.shape[:2]; yy,xx = np.mgrid[0:h,0:w]
    d = np.sqrt(((xx-w/2)/(w/2))**2 + ((yy-h/2)/(h/2))**2)/1.42
    return a*np.clip(1-s*d**1.8, 0, 1)[...,None]


def grain(a, amt, seed):
    h,w = a.shape[:2]; r = np.random.default_rng(seed)
    n = r.normal(0, amt, (h,w,1))
    lum = a.mean(axis=2, keepdims=True)/255
    return a + n*(.4+.8*(1-lum))


for i,(src,dst,ratio,maxw,k) in enumerate(JOBS):
    p = os.path.join(SRC, src)
    if not os.path.exists(p): print('нет:', src); continue
    im = Image.open(p).convert('RGB')
    im = crop_to(im, ratio)
    if im.size[0] > maxw:
        im = im.resize((maxw, int(round(maxw*im.size[1]/im.size[0]))), Image.LANCZOS)
    a = grade(np.array(im), k)
    a = vignette(a)
    a = grain(a, 3.4, 11+i)
    o = os.path.join(OUT, dst)
    Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save(o, quality=86, optimize=True, progressive=True)
    print('%-22s %s  %4d KB' % (dst, im.size, os.path.getsize(o)//1024))
