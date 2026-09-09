#!/usr/bin/env python3
"""Compute a focal point per source image and store it in the manifest.

Magazine rule: a photograph must never be cropped through its subject. We find where the
"content" of the picture actually is — edges and colour, not flat sky, grass or studio white —
and hand that back as an object-position, so every crop keeps the house in frame.
"""
import json, pathlib, math
from PIL import Image, ImageFilter, ImageStat

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "assets/src"
MAN = ROOT / "assets/manifest.json"
N = 96  # analysis grid

def energy_map(p):
    im = Image.open(p).convert("RGB").resize((N, N), Image.BILINEAR)
    g = im.convert("L")
    edges = g.filter(ImageFilter.FIND_EDGES).load()
    px = im.load()
    m = [[0.0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            r, gg, b = px[x, y]
            mx, mn = max(r, gg, b), min(r, gg, b)
            sat = (mx - mn) / 255.0
            lum = (0.299 * r + 0.587 * gg + 0.114 * b) / 255.0
            e = edges[x, y] / 255.0
            # sky / flat-white penalty: bright, low-saturation or blue-dominant flat areas carry no subject
            sky = 1.0
            if lum > 0.70 and sat < 0.30: sky = 0.035          # bright overcast sky, studio white
            elif b > r + 14 and b > gg + 6 and lum > 0.45: sky = 0.07  # blue sky
            elif lum < 0.06: sky = 0.30                       # crushed shadow
            m[y][x] = (e * e * 6.0 + sat * 0.35 + 0.02) * sky
    return m

def focal(p):
    m = energy_map(p)
    tot = sum(sum(r) for r in m)
    if tot <= 0: return (50, 50)
    cy = sum((y + .5) * sum(m[y]) for y in range(N)) / tot / N
    cx = sum((x + .5) * sum(m[y][x] for y in range(N)) for x in range(N)) / tot / N
    # pull toward the centre a little so crops stay calm, then clamp
    cx = 0.5 + (cx - 0.5) * 0.92
    cy = 0.5 + (cy - 0.5) * 1.0
    f = lambda v: int(round(max(0.12, min(0.88, v)) * 100))
    return (f(cx), f(cy))

if __name__ == "__main__":
    man = json.loads(MAN.read_text())
    changed = 0
    for name, rec in man.items():
        if not isinstance(rec, dict): continue
        cands = [q for q in SRC.iterdir() if q.stem == name]
        if not cands: continue
        fx, fy = focal(cands[0])
        if rec.get("focal") != [fx, fy]:
            rec["focal"] = [fx, fy]; changed += 1
    MAN.write_text(json.dumps(man, indent=0))
    print(f"focal points written: {changed} of {len(man)}")
