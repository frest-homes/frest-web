import sys, asyncio, json
from playwright.async_api import async_playwright
BASE='http://localhost:8765/frest-web/'
PAGES=sys.argv[1:] or ['', 'model/als-110/', 'compare/', 'configure/', 'pricing/', 'gallery/', 'projects/', 'custom-design/', 'resources/', 'team/', 'catalogue/', 'en/', 'en/model/aura-70/']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw,label in [(1280,'d'),(390,'m')]:
            ctx=await b.new_context(viewport={'width':vw,'height':900 if vw>400 else 844}, device_scale_factor=1)
            pg=await ctx.new_page()
            errs=[]; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
            for path in PAGES:
                await pg.goto(BASE+path, wait_until='networkidle'); await pg.evaluate("document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))"); await pg.evaluate("(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}window.scrollTo(0,0);})()"); await pg.wait_for_timeout(800)
                sw=await pg.evaluate('document.documentElement.scrollWidth'); h=await pg.evaluate('document.body.scrollHeight')
                broken=await pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.currentSrc||i.src).slice(0,5)")
                name=(path.strip('/').replace('/','_') or 'home')+'-'+label
                await pg.screenshot(path=f'shots/{name}.png', full_page=True)
                print(f'{label} {path or "/"}: scrollWidth={sw} (vw {vw}) height={h} broken={broken} errs={[e for e in errs if "fonts.g" not in e][:3]}')
                errs.clear()
            await ctx.close()
        await b.close()
asyncio.run(main())
