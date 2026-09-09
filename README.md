# frest-web — Frest Homes website generator

Static site for **www.frest.lv** (LV) and **www.fresthomes.com** (EN), generated from one content model.

- `content/data.py` — every fact, model, price, project, FAQ (LV + EN). Edit here, never in HTML.
- `content/ui.py` — interface strings.
- `templates/` — Jinja2 page templates. `static/` — one CSS, one JS, logo, favicon.
- `assets/src/` — source images (renders, photos, plans). `images.py` turns them into WebP `srcset` sizes in `site/img/`.
- `build.py --base / --canonical https://www.frest.lv` — builds `site/`.
- `.github/workflows/pages.yml` — builds and deploys to GitHub Pages on every push to `main`.

Local: `pip install -r requirements.txt && python3 images.py && python3 build.py --base /frest-web/` then serve `site/`.
Checks: `python3 check.py` (Playwright: overflow, errors, screenshots).
