#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frest Homes static site generator.

One source tree, two published sites:

    www.frest.lv        --root-lang lv --sister https://www.fresthomes.com
    www.fresthomes.com  --root-lang en --sister https://www.frest.lv

The root language is the real site. The other language is emitted as small redirect stubs that
point at the sister domain, so the two domains never compete for the same query and every
language has exactly one canonical home. hreflang is written across the two domains.

Usage: python3 build.py [--base /] [--out site] [--root-lang lv|en]
                        [--canonical https://www.frest.lv] [--sister https://www.fresthomes.com]
                        [--cname www.frest.lv]
Reads content/*.py, images from assets/manifest.json (run images.py then focal.py first).
"""
import os, sys, json, shutil, argparse, datetime, html, re
from jinja2 import Environment, FileSystemLoader, select_autoescape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content.data import TIMING, SITE, MODELS, PACKAGES, FACADE_COLORS, ROOF_TYPES, ADDONS, ADDON_WHY, WORKS, CUSTOM_PROJECTS, PROCESS, FAQ, TEAM, VALUES, QUIZ
from content.ui import UI
from content.editorial import DESC as IMGDESC, AUDIENCES, SPREADS, KICKERS, POS as IMGPOS
from content.seo import PATHS, ALIASES, META, INTRO, GEO
from content.knowledge_lv import ARTICLES_LV
from content.knowledge_en import ARTICLES_EN

ap = argparse.ArgumentParser()
ap.add_argument('--base', default='/')
ap.add_argument('--out', default='site')
ap.add_argument('--root-lang', default='lv', choices=['lv', 'en'])
ap.add_argument('--cname', default='')
ap.add_argument('--canonical', default='')          # this site's own origin
ap.add_argument('--sister', default='')             # the other language's origin
args = ap.parse_args()
BASE = args.base if args.base.endswith('/') else args.base + '/'
OUT = args.out
MANIFEST = json.load(open('assets/manifest.json'))
LANGS = ['lv', 'en']
ROOT_LANG = args.root_lang
OTHER_LANG = 'en' if ROOT_LANG == 'lv' else 'lv'
CAN = args.canonical.rstrip('/')
SIS = args.sister.rstrip('/')
TODAY = datetime.date.today().isoformat()
ARTICLES = {'lv': ARTICLES_LV, 'en': ARTICLES_EN}

def seg(lang):
    """URL segment for a language: '' for the one at the root, 'xx/' for the other."""
    return '' if lang == ROOT_LANG else lang + '/'

def ppath(key, lang):
    return PATHS[key][lang]

def other_of(lang):
    return 'en' if lang == 'lv' else 'lv'

# Hero images preloaded per page — the LCP element on each.
PRELOAD = {'home': 'aura70-hero', 'landing': 'als110-day-dk', 'pricing': 'als110-evening-dk',
           'projects': 'als-kettingskov-aerial', 'knowledge': 'als110-photo-lv-exterior-forest'}

# ---------- routes ----------
PAGES = [
    ('index.html',    'home',      None),
    ('landing.html',  'landing',   None),
    ('compare.html',  'compare',   None),
    ('which.html',    'which',     None),
    ('pricing.html',  'pricing',   None),
    ('gallery.html',  'gallery',   None),
    ('projects.html', 'projects',  None),
    ('custom.html',   'custom',    None),
    ('knowledge.html','knowledge', None),
    ('resources.html','resources', None),
    ('team.html',     'team',      None),
    ('catalogue.html','catalogue', None),
    ('legal.html',    'privacy',   None),
    ('legal.html',    'terms',     None),
]
# pages that should not be indexed or listed in the sitemap
NOINDEX = {'privacy', 'terms'}

env = Environment(loader=FileSystemLoader('templates'), autoescape=select_autoescape(['html']), trim_blocks=True, lstrip_blocks=True)

# ---------- absolute URL of any page, on whichever domain owns that language ----------
def abs_url(key_or_path, lang, article=None):
    """Absolute URL for a page in `lang`, on the domain that owns `lang`.
    The root language lives on this site (CAN); the other language lives on the sister site (SIS)."""
    if article is not None:
        p = ppath('article_dir', lang) + article + '/'
    elif key_or_path in PATHS:
        p = ppath(key_or_path, lang)
    else:
        p = key_or_path.lstrip('/')
    if lang == ROOT_LANG:
        return f"{CAN}{BASE}{p}" if CAN else f"{BASE}{p}"
    return f"{SIS}/{p}" if SIS else f"{BASE}{seg(lang)}{p}"

def alternates(key, article=None):
    """hreflang set for a page, pointing across both domains. x-default follows English."""
    lv = abs_url(key, 'lv', article)
    en = abs_url(key, 'en', article)
    return [('lv', lv), ('en', en), ('x-default', en)]

# ---------- helpers ----------
def make_helpers(lang):
    other = 'en' if lang == 'lv' else 'lv'
    prefix = BASE + seg(lang)

    def t(x):
        if isinstance(x, dict) and lang in x:
            return x[lang]
        return x

    def url(path=''):
        """Internal link. Accepts a page key (preferred) or a raw path."""
        p = PATHS[path][lang] if path in PATHS else path.lstrip('/')
        return prefix + p

    def murl(slug):
        return prefix + ppath('model_dir', lang) + slug + '/'

    def aurl(slug):
        return prefix + ppath('article_dir', lang) + slug + '/'

    def url_other(key_or_path='', article=None):
        """The language switch always crosses to the sister domain."""
        return abs_url(key_or_path, other, article)

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
        s = f"{int(n):,}".replace(',', ' ')
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

    return dict(t=t, url=url, murl=murl, aurl=aurl, url_other=url_other, img=img, imgsrc=imgsrc, srcset=srcset,
                eur=eur, num=num, cnt=cnt, lang=lang, other=other, BASE=BASE)

def model_by_slug(slug):
    return next(m for m in MODELS if m['slug'] == slug)

# ---------- schema.org ----------
def org_schema(lang, h):
    areas = GEO[lang]['area']
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness",
        "@id": (CAN + BASE + "#org"), "name": "Frest Homes", "legalName": SITE['company'],
        "url": CAN + BASE, "email": SITE['email'], "telephone": SITE['phone'],
        "image": CAN + h['imgsrc']('als110-day-dk', 1600),
        "logo": CAN + BASE + "static/logo.png",
        "description": META['home'][lang][1],
        "address": {"@type": "PostalAddress", "streetAddress": SITE['street'],
                    "addressLocality": "Rīga", "postalCode": SITE['postcode'], "addressCountry": "LV"},
        "areaServed": [{"@type": "Country", "name": a} for a in areas],
        "priceRange": "€€€",
        "foundingDate": "2019",
        "sameAs": [SITE['facebook'], SITE['instagram']],
        "knowsLanguage": ["lv", "en", "da"],
    }

def breadcrumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(items)]}

def faq_schema(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}

def article_schema(art, lang, url, h):
    return {"@context": "https://schema.org", "@type": "Article",
            "headline": art['title'], "description": art['desc'],
            "datePublished": art['date'], "dateModified": art['date'],
            "inLanguage": GEO[lang]['lang'],
            "image": CAN + h['imgsrc'](art['hero'], 1600),
            "author": {"@type": "Organization", "name": "Frest Homes"},
            "publisher": {"@id": CAN + BASE + "#org"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url}}

# ---------- build ----------
def build_lang(lang):
    h = make_helpers(lang)
    t, url = h['t'], h['url']
    arts = ARTICLES[lang]
    ctx_base = dict(h, SITE=SITE, UI=UI, MODELS=MODELS, PACKAGES=PACKAGES, COLORS=FACADE_COLORS, ROOFS=ROOF_TYPES, ADDONS=ADDONS, ADDON_WHY=ADDON_WHY,
                    WORKS=WORKS, CUSTOM=CUSTOM_PROJECTS, PROCESS=PROCESS, TIMING=TIMING, FAQ=FAQ, TEAM=TEAM, VALUES=VALUES, QUIZ=QUIZ, year=datetime.date.today().year,
                    canonical=CAN, TITLES=None, IMGDESC=IMGDESC, IMGPOS=IMGPOS, AUDIENCES=AUDIENCES, SPREADS=SPREADS, KICKERS=KICKERS,
                    ARTICLES=arts, INTRO=INTRO, PATHS=PATHS, GEO=GEO[lang], sister=SIS)

    def pz_data(models):
        d = {'colors': [{'id': c['id'], 'name': t(c['name'])} for c in FACADE_COLORS], 'roofs': [{'id': r['id'], 'name': t(r['name'])} for r in ROOF_TYPES], 'models': {}}
        for m in models:
            d['models'][m['slug']] = {'name': m['name'], 'url': h['murl'](m['slug']),
                                      'facades': {r: {c: {'src': h['imgsrc'](n, 1600), 'srcset': h['srcset'](n)} for c, n in cols.items()} for r, cols in m['facades'].items()}}
        return json.dumps(d, ensure_ascii=False)
    quiz_models = {m['slug']: {'name': m['name'], 'why': t(UI['quiz_why'][m['slug']]), 'url': h['murl'](m['slug']),
                               'img': h['imgsrc'](m['hero'], 1600), 'srcset': h['srcset'](m['hero']),
                               'series': m['series'], 'tagline': t(m['tagline']),
                               'pills': [f"{h['num'](m['area'])} m²", h['cnt'](m['bedrooms'], 'bedrooms'), h['cnt'](m['bathrooms'], 'bathrooms')],
                               'facts': f"{h['num'](m['area'])} m² · {h['cnt'](m['bedrooms'], 'bedrooms')} · {h['cnt'](m['bathrooms'], 'bathrooms')}"} for m in MODELS}
    ctx_base['pz_data'] = pz_data
    ctx_base['aud_data'] = json.dumps({k: {'h': t(hh), 'p': t(p), 'href': url(href), 'link': t(link)} for k, lab, hh, p, href, link in AUDIENCES}, ensure_ascii=False)
    ctx_base['quiz_data'] = json.dumps(quiz_models, ensure_ascii=False)

    def gallery_items():
        """Every gallery frame, ordered so two shots of the same subject never sit next to each
        other. `als110-evening-dk` and `als110-evening2-dk` are the same house from nearly the
        same spot; side by side they read as a mistake. The key strips trailing digits from each
        name segment, so variants of one shot collapse to one family, and a greedy pass pulls the
        next frame from a different family forward."""
        items = []
        for w in WORKS:
            for im, cap in w['images']:
                items.append({'img': im, 'cap': f"{t(w['title'])} — {t(cap)}",
                              'full': f"{t(w['title'])} — {t(cap)} · {t(w['location'])} {w['year']}",
                              'tags': 'built ' + ' '.join(w['tags'])
                                      + (' als-70' if 'als70' in w['tags'] else '')
                                      + (' als-110' if 'als110' in w['tags'] else '')
                                      + (' aura-70 aura-110' if 'aura' in w['tags'] else '')})
        for m in MODELS:
            for g in m['gallery'][:4]:
                items.append({'img': g['img'], 'cap': f"{m['name']} — {t(g['cap'])}",
                              'full': f"{m['name']} — {t(g['cap'])}", 'tags': 'models ' + m['slug']})

        def family(name):
            return '-'.join(re.sub(r'\d+$', '', part) for part in name.split('-'))

        out, pool = [], list(items)
        while pool:
            i = 0
            if out:
                last = family(out[-1]['img'])
                nxt = next((k for k, it in enumerate(pool) if family(it['img']) != last), 0)
                i = nxt
            out.append(pool.pop(i))
        return out
    ctx_base['gallery_items'] = gallery_items


    def write(path, html_out):
        sub = seg(lang).rstrip('/')
        full = os.path.join(OUT, sub, path, 'index.html') if (path or sub) else os.path.join(OUT, 'index.html')
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, 'w', encoding='utf-8').write(html_out)
        return full

    written = []
    home_crumb = ('Frest', abs_url('home', lang))

    for tpl, key, _ in PAGES:
        path = ppath(key, lang)
        title, desc = META[key][lang]
        schemas = [org_schema(lang, h)] if key == 'home' else []
        if key != 'home':
            schemas.append(breadcrumbs([home_crumb, (title.split(' | ')[0], abs_url(key, lang))]))
        if key == 'resources':
            schemas.append(faq_schema([(t(q), t(a)) for q, a in FAQ]))
        ctx = dict(ctx_base, page=key, path=path, key=key, title=title, desc=desc,
                   alts=alternates(key), self_url=abs_url(key, lang),
                   schemas=[json.dumps(s, ensure_ascii=False) for s in schemas],
                   switch_url=abs_url(key, other_of(lang)), preload_img=PRELOAD.get(key),
                   og_image=PRELOAD.get(key, 'als110-day-dk'), noindex=(key in NOINDEX))
        written.append(write(path, env.get_template(tpl).render(**ctx)))

    # models
    for m in MODELS:
        title = f"{m['name']} — {t(m['tagline'])}, {h['num'](m['area'])} m², {h['cnt'](m['bedrooms'], 'bedrooms')} | Frest"
        path = ppath('model_dir', lang) + m['slug'] + '/'
        mlv = f"{abs_url('model_dir', 'lv')}{m['slug']}/"
        men = f"{abs_url('model_dir', 'en')}{m['slug']}/"
        self_u = mlv if lang == 'lv' else men
        prod = {"@context": "https://schema.org", "@type": "Product", "name": f"Frest {m['name']}",
                "description": t(m['lead']), "brand": {"@type": "Brand", "name": "Frest Homes"},
                "image": CAN + h['imgsrc'](m['hero'], 1600), "url": self_u,
                "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR",
                           "lowPrice": m['price_base'], "highPrice": m['price_complete'], "offerCount": 2,
                           "availability": "https://schema.org/PreOrder"}}
        ctx = dict(ctx_base, page='model', path=path, key='model', m=m, title=title, desc=t(m['lead']),
                   alts=[('lv', mlv), ('en', men), ('x-default', men)], self_url=self_u,
                   schemas=[json.dumps(prod, ensure_ascii=False),
                            json.dumps(breadcrumbs([home_crumb, (t(UI['nav_models']), abs_url('compare', lang)), (m['name'], self_u)]), ensure_ascii=False)],
                   noindex=False, switch_url=abs_url('model_dir', other_of(lang)) + m['slug'] + '/',
                   preload_img=m['hero'], og_image=m['hero'],
                   works=[w for w in WORKS if set(w['tags']) & set(m['works_tags'])], others=[x for x in MODELS if x is not m])
        written.append(write(path, env.get_template('model.html').render(**ctx)))

    # knowledge articles
    for a in arts:
        path = ppath('article_dir', lang) + a['slug'] + '/'
        self_u = abs_url(None, lang, article=a['slug'])
        schemas = [json.dumps(article_schema(a, lang, self_u, h), ensure_ascii=False),
                   json.dumps(breadcrumbs([home_crumb, (META['knowledge'][lang][0].split(' | ')[0], abs_url('knowledge', lang)), (a['title'], self_u)]), ensure_ascii=False)]
        fq = [b for b in a['body'] if b[0] == 'faq']
        if fq:
            schemas.append(json.dumps(faq_schema(fq[0][1]), ensure_ascii=False))
        ctx = dict(ctx_base, page='article', path=path, key='knowledge', a=a,
                   title=f"{a['title']} | Frest", desc=a['desc'],
                   alts=[],   # LV and EN articles are different pieces, not translations
                   self_url=self_u, schemas=schemas, noindex=False,
                   switch_url=abs_url('knowledge', other_of(lang)), preload_img=a['hero'], og_image=a['hero'],
                   more=[x for x in arts if x is not a][:3])
        written.append(write(path, env.get_template('article.html').render(**ctx)))

    # 404
    ctx = dict(ctx_base, page='404', path='404', key='home', title='404 | Frest', desc='', alts=[], self_url='',
               schemas=[], noindex=True, switch_url=abs_url('home', other_of(lang)), preload_img=None)
    out = env.get_template('404.html').render(**ctx)
    if lang == ROOT_LANG:
        open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8').write(out)
    return written

# ---------- redirect stubs for the language that lives on the sister domain ----------
STUB = """<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8">
<title>{title}</title><link rel="canonical" href="{target}">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0;url={target}">
<style>body{{font:15px/1.6 system-ui,sans-serif;margin:0;display:grid;place-items:center;min-height:100vh;background:#f2f7f8;color:#0c2429}}
a{{color:#0a7a88}}div{{text-align:center;max-width:34ch;padding:24px}}</style></head>
<body><div><p>{msg}</p><p><a href="{target}">{target}</a></p></div>
<script>location.replace({target_js});</script></body></html>"""

def write_stub(rel_path, target, lang):
    msg = {'lv': 'Šī lapa ir pārcelta uz frest.lv', 'en': 'This page has moved to fresthomes.com'}[lang]
    full = os.path.join(OUT, rel_path, 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(STUB.format(
        lang=lang, title='Frest', target=html.escape(target), msg=msg, target_js=json.dumps(target)))

def build_stubs():
    """Everything in the non-root language becomes a stub to the sister domain."""
    lang = OTHER_LANG
    pre = lang + '/'
    for _, key, _ in PAGES:
        write_stub(pre + ppath(key, lang), abs_url(key, lang), lang)
    for m in MODELS:
        write_stub(pre + ppath('model_dir', lang) + m['slug'] + '/',
                   abs_url('model_dir', lang) + m['slug'] + '/', lang)
    for a in ARTICLES[lang]:
        write_stub(pre + ppath('article_dir', lang) + a['slug'] + '/',
                   abs_url(None, lang, article=a['slug']), lang)

def build_aliases():
    """Old English-slug paths kept alive after the Latvian slugs were localised."""
    for lang, mapping in ALIASES.items():
        pre = '' if lang == ROOT_LANG else lang + '/'
        for old, new in mapping.items():
            if old == new:
                continue
            target = abs_url(new if new not in PATHS else new, lang) if False else (
                f"{CAN}{BASE}{new}" if lang == ROOT_LANG else abs_url_alias(new, lang))
            write_stub(pre + old, target, lang)
    # models used to live at /model/<slug>/ in both languages
    if ROOT_LANG == 'lv':
        for m in MODELS:
            write_stub('model/' + m['slug'] + '/', f"{CAN}{BASE}{ppath('model_dir','lv')}{m['slug']}/", 'lv')

def abs_url_alias(path, lang):
    return f"{SIS}/{path}" if SIS else f"{BASE}{seg(lang)}{path}"

# ---------- sitemap ----------
def build_sitemap():
    entries = []   # (loc, priority, changefreq, alts)
    lang = ROOT_LANG
    for _, key, _ in PAGES:
        if key in NOINDEX:
            continue
        pri = {'home': '1.0', 'landing': '0.9', 'pricing': '0.9', 'knowledge': '0.8'}.get(key, '0.7')
        entries.append((abs_url(key, lang), pri, 'weekly', alternates(key)))
    for m in MODELS:
        entries.append((abs_url('model_dir', lang) + m['slug'] + '/', '0.9', 'monthly',
                        [('lv', abs_url('model_dir', 'lv') + m['slug'] + '/'),
                         ('en', abs_url('model_dir', 'en') + m['slug'] + '/'),
                         ('x-default', abs_url('model_dir', 'en') + m['slug'] + '/')]))
    for a in ARTICLES[lang]:
        entries.append((abs_url(None, lang, article=a['slug']), '0.7', 'monthly', []))
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, pri, cf, alts in entries:
        alt = ''.join(f'<xhtml:link rel="alternate" hreflang="{k}" href="{html.escape(u)}"/>' for k, u in alts)
        out.append(f'<url><loc>{html.escape(loc)}</loc><lastmod>{TODAY}</lastmod>'
                   f'<changefreq>{cf}</changefreq><priority>{pri}</priority>{alt}</url>')
    out.append('</urlset>')
    open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(out))

def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, 'static'), exist_ok=True)
    for f in os.listdir('static'):
        shutil.copy(os.path.join('static', f), os.path.join(OUT, 'static', f))
    all_written = []
    all_written += build_lang(ROOT_LANG)
    build_stubs()
    build_aliases()
    build_sitemap()
    root = (CAN or '') + BASE.rstrip('/')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "# The /%s/ tree is redirect stubs to the sister domain. They must stay crawlable\n"
        "# so the canonical and the noindex on them can be read.\n"
        "\n"
        "User-agent: GPTBot\nAllow: /\n\n"
        "User-agent: ClaudeBot\nAllow: /\n\n"
        "User-agent: PerplexityBot\nAllow: /\n\n"
        f"Sitemap: {root}/sitemap.xml\n" % OTHER_LANG)
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    if args.cname:
        open(os.path.join(OUT, 'CNAME'), 'w').write(args.cname.strip() + '\n')
    print(f'built {len(all_written)} pages -> {OUT} (root lang {ROOT_LANG}, base {BASE}, canonical {CAN or "-"}, sister {SIS or "-"})')

if __name__ == '__main__':
    main()
