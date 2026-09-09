"""Image pipeline: assets/src/* -> site/img/<name>-<w>.webp (+ jpg fallback at 1600) + manifest.
Idempotent: skips outputs that already exist and are newer than the source."""
import os, json, sys
from PIL import Image, ImageOps

SRC = 'assets/src'
OUT = 'site/img'
WIDTHS = [480, 960, 1600, 2400]
MANIFEST = 'assets/manifest.json'

def process(name, path, out_dir, manifest):
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    has_alpha = im.mode in ('RGBA', 'LA') and im.getextrema()[-1][0] < 255
    if not has_alpha:
        im = im.convert('RGB')
    w, h = im.size
    entry = {'w': w, 'h': h, 'sizes': [], 'alpha': has_alpha}
    for tw in WIDTHS:
        if tw > w and tw != WIDTHS[0]:
            continue
        tw2 = min(tw, w)
        th = round(h * tw2 / w)
        outp = f'{out_dir}/{name}-{tw2}.webp'
        entry['sizes'].append(tw2)
        if os.path.exists(outp) and os.path.getmtime(outp) >= os.path.getmtime(path):
            continue
        r = im.resize((tw2, th), Image.LANCZOS)
        r.save(outp, 'WEBP', quality=80 if tw2 < 2000 else 74, method=4)
    # jpeg/png fallback at up to 1600
    fw = min(1600, w); fh = round(h * fw / w)
    if has_alpha:
        outp = f'{out_dir}/{name}-{fw}.png'
        if not os.path.exists(outp):
            im.resize((fw, fh), Image.LANCZOS).save(outp, 'PNG', optimize=True)
        entry['fallback'] = f'{name}-{fw}.png'
    else:
        outp = f'{out_dir}/{name}-{fw}.jpg'
        if not os.path.exists(outp):
            im.resize((fw, fh), Image.LANCZOS).save(outp, 'JPEG', quality=82, optimize=True, progressive=True)
        entry['fallback'] = f'{name}-{fw}.jpg'
    entry['sizes'] = sorted(set(entry['sizes']))
    manifest[name] = entry

def run(only=None):
    os.makedirs(OUT, exist_ok=True)
    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    for f in sorted(os.listdir(SRC)):
        name, ext = os.path.splitext(f)
        if ext.lower() not in ('.png', '.jpg', '.jpeg'):
            continue
        if only and name not in only:
            continue
        process(name, f'{SRC}/{f}', OUT, manifest)
        json.dump(manifest, open(MANIFEST, 'w'), indent=1)
        print('ok', name, manifest[name]['sizes'], flush=True)
    return manifest

if __name__ == '__main__':
    run(sys.argv[1:] or None)
