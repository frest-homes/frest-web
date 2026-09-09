#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frest Homes static site generator.
Usage: python3 build.py [--base /frest-web/] [--out site]
Reads content/data.py + content/ui.py, images from assets/manifest.json (run images.py first)."""
import os, sys, json, shutil, argparse, datetime, html
from jinja2 import Environment, FileSystemLoader, select_autoescape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content.data import TIMING, SITE, MODELS, PACKAGES, FACADE_COLORS, ROOF_TYPES, ADDONS, ADDON_WHY, WORKS, CUSTOM_PROJECTS, PROCESS, FAQ, TEAM, VALUES, QUIZ
from content.ui import UI
from content.editorial import DESC as IMGDESC, AUDIENCES, SPREADS, KICKERS, POS as IMGPOS

ap = argparse.ArgumentParser()
ap.add_argument('--base', default='/')
ap.add_argument('--out', default='site')
ap.add_argument('--root-lang', default='lv', choices=['lv', 'en'])  # which language lives at /
ap.add_argument('--cname', default='')      # custom domain -> writes site/CNAME for GitHub Pages
ap.add_argument('--canonical', default='')  # e.g. https://frest-homes.github.io/frest-web
args = ap.parse_args()
BASE = args.base if args.base.endswith('/') else args.base + '/'
OUT = args.out
MANIFEST = json.load(open('assets/manifest.json'))
LANGS = ['lv', 'en']
ROOT_LANG = None  # set in main() from --root-lang
def seg(lang):
    """URL segment for a language: '' for the one at the root, 'xx/' for the other."""
    return '' if lang == ROOT_LANG else lang + '/'

# ---------- routes ----------
PAGES = [
    # (template, slug-path, key)
    ('index.html', '', 'home'),
    ('compare.html', 'compare/', 'compare'),
    ('which.html', 'configure/', 'which'),
    ('pricing.html', 'pricing/', 'pricing'),
    ('gallery.html', 'gallery/', 'gallery'),
    ('projects.html', 'projects/', 'projects'),
    ('custom.html', 'custom-design/', 'custom'),
    ('resources.html', 'resources/', 'resources'),
    ('team.html', 'team/', 'team'),
    ('catalogue.html', 'catalogue/', 'catalogue'),
    ('legal.html', 'privacy/', 'privacy'),
    ('legal.html', 'terms/', 'terms'),
]
TITLES = {
    'home': {'lv': 'Skandināvu dizaina mājas — projektējam un uzbūvējam | Frest Homes', 'en': 'Scandinavian-design homes — we design and build | Frest Homes'},
    'compare': {'lv': 'Salīdzināt modeļus — Aura 70, Aura 110, Als 70, Als 110 | Frest', 'en': 'Compare models — Aura 70, Aura 110, Als 70, Als 110 | Frest'},
    'which': {'lv': 'Kura māja man? | Frest', 'en': 'Which house is mine? | Frest'},
    'pricing': {'lv': 'Paketes un cenas | Frest', 'en': 'Packages and prices | Frest'},
    'gallery': {'lv': 'Galerija | Frest', 'en': 'Gallery | Frest'},
    'projects': {'lv': 'Realizētie projekti Dānijā un Latvijā | Frest', 'en': 'Completed projects in Denmark and Latvia | Frest'},
    'custom': {'lv': 'Individuāli projekti | Frest', 'en': 'Custom design | Frest'},
    'resources': {'lv': 'Biežāk uzdotie jautājumi | Frest', 'en': 'Frequently asked questions | Frest'},
    'team': {'lv': 'Par mums | Frest', 'en': 'About us | Frest'},
    'catalogue': {'lv': 'Katalogs ar cenām | Frest', 'en': 'Catalogue with prices | Frest'},
    'privacy': {'lv': 'Privātuma politika | Frest', 'en': 'Privacy policy | Frest'},
    'terms': {'lv': 'Noteikumi | Frest', 'en': 'Terms | Frest'},
}
DESC = {
    'home': {'lv': 'Aura un Als sērijas mājas: projektēšana, saskaņošana, ražošana un būvniecība ar vienu atbildīgo. Energoklase A. Uzbūvētas Dānijā un Latvijā. Rūpnīcas komplekts ar montāžu no 92 000 € ar PVN, bez pamatiem un apdares.',
             'en': 'Aura and Als series homes: design, permitting, manufacturing and construction with one responsible partner. Energy class A. Built in Denmark and Latvia. Factory kit with assembly from €92,000 incl. VAT, excl. foundation and interior.'},
}

env = Environment(loader=FileSystemLoader('templates'), autoescape=select_autoescape(['html']), trim_blocks=True, lstrip_blocks=True)

# ---------- helpers ----------
def make_helpers(lang):
    other = 'en' if lang == 'lv' else 'lv'
    prefix = BASE + seg(lang)

    def t(x):
        if isinstance(x, dict) and lang in x:
            return x[lang]
        return x

    def url(path=''):
        return prefix + path.lstrip('/')

    def url_other(path=''):
        return BASE + seg(other) + path.lstrip('/')

    def imgsrc(name, w=None):
        m = MANIFEST[name]
        w = w or max(m['sizes'])
        return f"{BASE}img/{name}-{w}.webp"

    def srcset(name):
        m = MANIFEST[name]
        return ', '.join(f"{BASE}img/{name}-{w}.webp {w}w" for w in m['sizes'])

    def img(name, alt='', sizes='100vw', cls='', loading='lazy', fetchpriority=None, width=None, extra=''):
        m = MANIFEST[name]
        fb = f"{BASE}img/{m['fallback']}"
        ratio_w, ratio_h = m['w'], m['h']
        attrs = f'alt="{html.escape(str(alt))}" width="{ratio_w}" height="{ratio_h}" loading="{loading}" decoding="async"'
        # magazine crop: never cut through the subject — the focal point comes from focal.py
        fp = m.get('focal')
        if fp and IMGPOS.get(name) not in ('c',):
            attrs += f' style="object-position:{fp[0]}% {fp[1]}%"'
        if fetchpriority:
            attrs += f' fetchpriority="{fetchpriority}"'
        if cls:
            attrs += f' class="{cls}"'
        return (f'<picture><source type="image/webp" srcset="{srcset(name)}" sizes="{sizes}">'
                f'<img src="{fb}" {attrs} {extra}></picture>')

    def eur(n):
        s = f"{int(n):,}".replace(',', ' ')
        return f"{s} €" if lang == 'lv' else f"€{int(n):,}"

    def num(n):
        if n is None:
            return '—'
        if isinstance(n, float):
            s = f"{n:.1f}".rstrip('0').rstrip('.')
            return s.replace('.', ',') if lang == 'lv' else s
        return str(n)

    SING = {'bedrooms': {'lv': 'guļamistaba', 'en': 'bedroom'}, 'bathrooms': {'lv': 'vannasistaba', 'en': 'bathroom'},
            'rooms': {'lv': 'istaba', 'en': 'room'}}

    def cnt(n, key):
        """'1 bathroom' / '2 bathrooms' — UI holds the plural, the singular is derived here."""
        w = SING[key][lang] if n == 1 and key in SING else t(UI[key]).lower()
        return f"{n} {w}"

    return dict(t=t, url=url, url_other=url_other, img=img, imgsrc=imgsrc, srcset=srcset, eur=eur, num=num, cnt=cnt, lang=lang, other=other, BASE=BASE)

def model_by_slug(slug):
    return next(m for m in MODELS if m['slug'] == slug)

def build_lang(lang):
    h = make_helpers(lang)
    t, url = h['t'], h['url']
    ctx_base = dict(h, SITE=SITE, UI=UI, MODELS=MODELS, PACKAGES=PACKAGES, COLORS=FACADE_COLORS, ROOFS=ROOF_TYPES, ADDONS=ADDONS, ADDON_WHY=ADDON_WHY,
                    WORKS=WORKS, CUSTOM=CUSTOM_PROJECTS, PROCESS=PROCESS, TIMING=TIMING, FAQ=FAQ, TEAM=TEAM, VALUES=VALUES, QUIZ=QUIZ, year=datetime.date.today().year,
                    canonical=args.canonical, TITLES=TITLES, IMGDESC=IMGDESC, IMGPOS=IMGPOS, AUDIENCES=AUDIENCES, SPREADS=SPREADS, KICKERS=KICKERS)
    # personaliser data (JSON for JS)
    def pz_data(models):
        d = {'colors': [{'id': c['id'], 'name': t(c['name'])} for c in FACADE_COLORS], 'roofs': [{'id': r['id'], 'name': t(r['name'])} for r in ROOF_TYPES], 'models': {}}
        for m in models:
            d['models'][m['slug']] = {'name': m['name'], 'url': url(f"model/{m['slug']}/"),
                                      'facades': {r: {c: {'src': h['imgsrc'](n, 1600), 'srcset': h['srcset'](n)} for c, n in cols.items()} for r, cols in m['facades'].items()}}
        return json.dumps(d, ensure_ascii=False)
    quiz_models = {m['slug']: {'name': m['name'], 'why': t(UI['quiz_why'][m['slug']]), 'url': url(f"model/{m['slug']}/"), 'img': h['imgsrc'](m['card'], 960), 'srcset': h['srcset'](m['card']),
                               'facts': f"{h['num'](m['area'])} m² · {h['cnt'](m['bedrooms'], 'bedrooms')} · {h['cnt'](m['bathrooms'], 'bathrooms')}"} for m in MODELS}
    ctx_base['pz_data'] = pz_data
    ctx_base['aud_data'] = json.dumps({k: {'h': t(h), 'p': t(p), 'href': url(href), 'link': t(link)} for k, lab, h, p, href, link in AUDIENCES}, ensure_ascii=False)
    ctx_base['quiz_data'] = json.dumps(quiz_models, ensure_ascii=False)

    def write(path, html_out):
        sub = seg(lang).rstrip('/')
        full = os.path.join(OUT, sub, path, 'index.html') if (path or sub) else os.path.join(OUT, 'index.html')
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, 'w', encoding='utf-8').write(html_out)
        return full

    written = []
    for tpl, path, key in PAGES:
        ctx = dict(ctx_base, page=key, path=path, title=TITLES[key][lang], desc=DESC.get(key, DESC['home'])[lang])
        out = env.get_template(tpl).render(**ctx)
        written.append(write(path, out))
    for m in MODELS:
        title = f"{m['name']} — {t(m['tagline'])}, {h['num'](m['area'])} m², {h['cnt'](m['bedrooms'], 'bedrooms')} | Frest"
        ctx = dict(ctx_base, page='model', path=f"model/{m['slug']}/", m=m, title=title, desc=t(m['lead']),
                   works=[w for w in WORKS if set(w['tags']) & set(m['works_tags'])], others=[x for x in MODELS if x is not m])
        written.append(write(f"model/{m['slug']}/", env.get_template('model.html').render(**ctx)))
    # 404
    ctx = dict(ctx_base, page='404', path='404', title='404 | Frest', desc='')
    out = env.get_template('404.html').render(**ctx)
    if lang == ROOT_LANG:
        open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8').write(out)
    return written

def main():
    global ROOT_LANG
    ROOT_LANG = args.root_lang
    os.makedirs(OUT, exist_ok=True)
    # static
    os.makedirs(os.path.join(OUT, 'static'), exist_ok=True)
    for f in os.listdir('static'):
        shutil.copy(os.path.join('static', f), os.path.join(OUT, 'static', f))
    all_written = []
    for lang in LANGS:
        all_written += build_lang(lang)
    # sitemap + robots
    can = args.canonical.rstrip('/') if args.canonical else ''
    urls = []
    for lang in LANGS:
        pre = ('/' + seg(lang).rstrip('/')) if seg(lang) else ''
        for _, path, key in PAGES:
            if key in ('privacy', 'terms'):
                continue
            urls.append(f"{pre}/{path}")
        for m in MODELS:
            urls.append(f"{pre}/model/{m['slug']}/")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.w3.org/1999/xhtml" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u in urls:
        loc = (can or '') + BASE.rstrip('/') + u
        oth = 'en' if ROOT_LANG == 'lv' else 'lv'
        op = '/' + oth
        bare = u[len(op):] if u.startswith(op + '/') else u
        alt_root = (can or '') + BASE.rstrip('/') + bare
        alt_oth = (can or '') + BASE.rstrip('/') + op + bare
        alt_lv, alt_en = (alt_root, alt_oth) if ROOT_LANG == 'lv' else (alt_oth, alt_root)
        sm.append(f'<url><loc>{loc}</loc><xhtml:link rel="alternate" hreflang="lv" href="{alt_lv}"/><xhtml:link rel="alternate" hreflang="en" href="{alt_en}"/></url>')
    sm.append('</urlset>')
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('\n'.join(sm))
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f"User-agent: *\nAllow: /\nSitemap: {(can or '') + BASE.rstrip('/')}/sitemap.xml\n")
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    if args.cname:
        open(os.path.join(OUT, 'CNAME'), 'w').write(args.cname.strip() + '\n')
    print(f'built {len(all_written)} pages -> {OUT} (base {BASE})')

if __name__ == '__main__':
    main()
