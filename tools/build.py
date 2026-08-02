#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка двух языковых версий из одного источника."""
import json, os, re, sys, base64, shutil, hashlib
sys.path.insert(0, os.path.dirname(__file__))
from content import RU, EN
import data as DAT
import geo as GEO

# ─── счётчики ───────────────────────────────────────────────────────────
# Пусто = аналитики нет вообще: ни скриптов, ни баннера согласия.
GA_ID      = 'G-9BLFSZP6X2'   # Google Analytics 4, вида G-XXXXXXXXXX
CLARITY_ID = ''          # Microsoft Clarity, вида abcdefghij

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def read(n):
    with open(os.path.join(HERE, n), encoding='utf-8') as f:
        return f.read()

TPL = read('tpl_head.html') + read('tpl_head2.html') + read('tpl_body.html') + read('tpl_js.html')

# шрифты (уже собранные в base64) — забираем из старой сборки, чтобы не тянуть сеть
def fonts_css():
    p = os.path.join(ROOT, 'tools', 'fonts_inline.css')
    if os.path.exists(p):
        return '<style>' + open(p, encoding='utf-8').read() + '</style>'
    return ('<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500'
            '&family=Manrope:wght@300..800&display=swap" rel="stylesheet">')

CREDIT = {'ru': 'иллюстрация создана ИИ для этого материала',
          'en': 'image generated with AI for this piece'}
STILL = {'ru': '© Universal Pictures / Syncopy · промоматериал, цитирование в целях критики',
         'en': '© Universal Pictures / Syncopy · promotional material, quoted for criticism'}
CLIP = {'ru': '© Universal Pictures / Syncopy · фрагмент трейлера, цитирование',
        'en': '© Universal Pictures / Syncopy · trailer excerpt, quoted for review'}


def sources_html(lang):
    T = RU if lang == 'ru' else EN
    out = []
    for gid, items in DAT.SOURCES:
        lis = ''.join(
            '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, (ru if lang == 'ru' else en))
            for u, ru, en in items)
        out.append('<div><h4>%s</h4><ul>%s</ul></div>' % (T['src_' + gid], lis))
    return ''.join(out)


def payload(lang):
    T = RU if lang == 'ru' else EN
    mp = []
    for m in DAT.MAP:
        d = m[lang]
        lab = GEO.LAB.get(m['id'], (0, -20))
        mp.append(dict(id=m['id'], x=m['x'], y=m['y'], lx=lab[0], ly=lab[1],
                       name=d['name'], role=d['role'], desc=d['desc'], place=d['place'], fact=d['fact'],
                       c1=d['c1'], c2=d['c2'], o1k=d['o1k'], o1=d['o1'], o2k=d['o2k'], o2=d['o2']))
    xen = [x[lang] for x in DAT.XENIA]
    tl = [dict(id=c['id'], cls=c['cls'], n=c[lang][0], d=c[lang][1]) for c in DAT.TL]
    tlL = {k: {i: list(v) for i, v in m.items()} for k, m in DAT.TL_LAYOUT.items()}
    tlN = {'chrono': T['tl_n1'], 'homer': T['tl_n2'], 'nolan': T['tl_n3']}
    bo = [dict(n=f['n'], y=f['y'], b=f['b'], g=f['g'], live=bool(f.get('live')), note=f[lang]) for f in DAT.BO]
    qz = [dict(q=q[lang][0], e=q[lang][1], a=q['a']) for q in DAT.QUIZ]
    keys = ['sound_on', 'sound_off', 'share', 'share_done', 'desc', 'choice_law_kept', 'choice_law_broken',
            'x_step', 'x_of', 'x_next', 'x_verdict', 'x_again', 'x_score',
            'bo_budget', 'bo_gross', 'bo_live', 'qz_stmt', 'qz_next', 'qz_result', 'qz_again',
            'name_after_sub', 'tl_m1', 'tl_m2', 'tl_m3', 'tl_read',
            'map_hint_touch', 'tl_hint_touch']
    return dict(root='' if lang == 'ru' else '../', ga=GA_ID, clarity=CLARITY_ID,
                t={k: T[k] for k in keys},
                map=mp, xenia=xen, xv=DAT.XVERDICT[lang], tl=tl, tlL=tlL, tlN=tlN,
                bo=bo, quiz=qz, qr=DAT.QZ_RESULT[lang])


def build(lang):
    T = dict(RU if lang == 'ru' else EN)
    T['root'] = '' if lang == 'ru' else '../'
    T['fonts'] = fonts_css()
    T['sources'] = sources_html(lang)
    T['img_credit'] = CREDIT[lang]
    T['clip_credit'] = CLIP[lang]
    T['still_credit'] = STILL[lang]
    closed = [d for d in GEO.LAND if d.endswith('Z')]
    opened = [d for d in GEO.LAND if not d.endswith('Z')]
    T['land'] = ('<g id="land" stroke="rgba(184,145,47,.30)" stroke-width=".8" stroke-linejoin="round">'
                 + '<g fill="#152032">' + ''.join('<path d="%s"/>' % d for d in closed) + '</g>'
                 + '<g fill="none">' + ''.join('<path d="%s"/>' % d for d in opened) + '</g></g>')
    T['route_d'] = GEO.ROUTE
    T['sealabels'] = ''.join(
        '<text x="%d" y="%d" text-anchor="middle" fill="rgba(240,235,226,.17)" '
        'font-family="Cormorant Garamond, serif" font-style="italic" font-size="%d" '
        'letter-spacing="3">%s</text>' % (x, y, 20 if i == 3 else 17, (ru if lang == 'ru' else en))
        for i, (ru, en, x, y) in enumerate(GEO.SEAS))
    # сборка одна на все устройства: подсказку под указатель выбирает JS во время выполнения
    T['map_hint'] = T['map_hint_desktop']
    T['manifest'] = 'manifest.webmanifest'
    T['analytics'] = '' if not (GA_ID or CLARITY_ID) else ' data-an="1"'
    T['alt_ru'] = './' if lang == 'ru' else '../'
    T['alt_en'] = './en/' if lang == 'ru' else './'
    html = TPL
    html = html.replace('{{DATA}}', json.dumps(payload(lang), ensure_ascii=False))
    for k, v in T.items():
        html = html.replace('{{%s}}' % k, str(v))
    left = set(re.findall(r'\{\{(\w+)\}\}', html))
    if left:
        raise SystemExit('НЕ ЗАПОЛНЕНО: ' + ', '.join(sorted(left)))
    return html


def main():
    ru = build('ru')
    en = build('en')
    with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(ru)
    os.makedirs(os.path.join(ROOT, 'en'), exist_ok=True)
    with open(os.path.join(ROOT, 'en', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(en)

    # PWA: у каждой языковой версии свой манифест, иначе установка из /en/ открывала русскую страницу
    def manifest(lang, icons):
        T = RU if lang == 'ru' else EN
        return {
            "name": T['title'], "short_name": "ΞΕΝΙΑ", "lang": lang, "dir": "ltr",
            "start_url": "./", "scope": "./", "display": "standalone",
            "background_color": "#0a0f18", "theme_color": "#0a0f18",
            "description": T['desc'],
            "icons": [{"src": icons + "assets/icon-192.png", "sizes": "192x192",
                       "type": "image/png", "purpose": "any maskable"},
                      {"src": icons + "assets/icon-512.png", "sizes": "512x512",
                       "type": "image/png", "purpose": "any maskable"}]
        }
    with open(os.path.join(ROOT, 'manifest.webmanifest'), 'w', encoding='utf-8') as f:
        json.dump(manifest('ru', ''), f, ensure_ascii=False, indent=1)
    with open(os.path.join(ROOT, 'en', 'manifest.webmanifest'), 'w', encoding='utf-8') as f:
        json.dump(manifest('en', '../'), f, ensure_ascii=False, indent=1)

    ver = hashlib.sha1((ru + en).encode()).hexdigest()[:8]
    sw = """const C='xenia-%s';""" % ver + """
const CORE=['./','./en/','./manifest.webmanifest','./en/manifest.webmanifest',
 './assets/still-threshold.jpg','./assets/still-cyclops.jpg','./assets/still-stacks.jpg',
 './assets/still-drag.jpg','./assets/still-horse.jpg'];
self.addEventListener('install',e=>{self.skipWaiting();
  e.waitUntil(caches.open(C).then(c=>Promise.allSettled(CORE.map(u=>c.add(u)))));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>
  Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const r=e.request; if(r.method!=='GET') return;
  if(r.headers.get('range')) return;           // видео отдаём сети
  // страницы берём из сети и только при её отсутствии из кэша:
  // иначе после публикации правок вернувшийся читатель видит старую версию
  if(r.mode==='navigate'){
    e.respondWith(fetch(r).then(res=>{
      const cp=res.clone(); caches.open(C).then(c=>c.put(r,cp)); return res;
    }).catch(()=>caches.match(r).then(hit=>hit||caches.match(/\\/en\\//.test(new URL(r.url).pathname)?'./en/':'./'))));
    return;
  }
  e.respondWith(caches.match(r).then(hit=>hit||fetch(r).then(res=>{
    if(res.ok && res.type==='basic' && !/\\.(mp4|webm|mp3)$/i.test(new URL(r.url).pathname)){
      const cp=res.clone(); caches.open(C).then(c=>c.put(r,cp));
    } return res;
  }).catch(()=>caches.match(/\\/en\\//.test(new URL(r.url).pathname)?'./en/':'./'))));});
"""
    with open(os.path.join(ROOT, 'sw.js'), 'w', encoding='utf-8') as f:
        f.write(sw)

    print('index.html      %6.0f KB' % (len(ru.encode()) / 1024))
    print('en/index.html   %6.0f KB' % (len(en.encode()) / 1024))


if __name__ == '__main__':
    main()
