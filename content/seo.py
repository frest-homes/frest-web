# -*- coding: utf-8 -*-
"""SEO layer: one title + one meta description per page per language, written against a keyword.

Two domains, two languages, one canonical home for each language:
  www.frest.lv        -> Latvian at /,  English pages are redirect stubs to fresthomes.com
  www.fresthomes.com  -> English at /,  Latvian pages are redirect stubs to frest.lv
so nothing competes with itself in search. hreflang points across the two domains.

Latvian intent: people in Latvia searching for moduļu mājas / koka karkasa mājas / cik maksā uzbūvēt māju.
English intent: Irish self-builders and contractors searching for timber frame house kits and build costs.
Frest in Ireland supplies the kit and erects it — foundation, services, interior and certification are local.
"""

# Path per page key per language. A tuple means the two languages use different slugs.
PATHS = {
    'home':      {'lv': '',                  'en': ''},
    'compare':   {'lv': 'salidzinat/',       'en': 'compare/'},
    'which':     {'lv': 'konfigurators/',    'en': 'configure/'},
    'pricing':   {'lv': 'cenas/',            'en': 'pricing/'},
    'gallery':   {'lv': 'galerija/',         'en': 'gallery/'},
    'projects':  {'lv': 'projekti/',         'en': 'projects/'},
    'custom':    {'lv': 'individuali-projekti/', 'en': 'custom-design/'},
    'resources': {'lv': 'jautajumi/',        'en': 'faq/'},
    'team':      {'lv': 'par-mums/',         'en': 'about/'},
    'catalogue': {'lv': 'katalogs/',         'en': 'catalogue/'},
    'privacy':   {'lv': 'privatuma-politika/', 'en': 'privacy/'},
    'terms':     {'lv': 'noteikumi/',        'en': 'terms/'},
    # new
    'landing':   {'lv': 'modulu-majas/',     'en': 'ireland/'},
    'knowledge': {'lv': 'zinasana/',         'en': 'knowledge/'},
    'model_dir': {'lv': 'majas/',            'en': 'model/'},
    'article_dir': {'lv': 'zinasana/',       'en': 'knowledge/'},
}

# Old paths that must keep working (the site was already published with these).
ALIASES = {
    'lv': {'compare/': 'salidzinat/', 'configure/': 'konfigurators/', 'pricing/': 'cenas/',
           'gallery/': 'galerija/', 'projects/': 'projekti/', 'custom-design/': 'individuali-projekti/',
           'resources/': 'jautajumi/', 'team/': 'par-mums/', 'catalogue/': 'katalogs/',
           'privacy/': 'privatuma-politika/', 'terms/': 'noteikumi/'},
    'en': {'resources/': 'faq/', 'team/': 'about/'},
}

# (title, meta description). Titles aim at ~60 characters plus the brand; descriptions at 150–165.
META = {
    'home': {
        'lv': ('Moduļu mājas un koka karkasa mājas Latvijā | Frest Homes',
               'Rūpnīcā ražotas koka karkasa mājas ar montāžu no 92 000 € ar PVN (bez pamatiem un apdares). '
               'Energoklase A, četri modeļi 68–110 m². Projektējam, saskaņojam un uzbūvējam.'),
        'en': ('Scandinavian Timber Frame House Kits for Irish Self Builds | Frest',
               'Factory-built insulated timber frame kits erected on your site. Four models 68–110 m², '
               'A-rated fabric, fixed kit price from €92,000 incl. VAT. Foundation and fit-out stay local.'),
    },
    'landing': {
        'lv': ('Moduļu mājas ar cenām — Aura un Als sērija | Frest Homes',
               'Četri moduļu māju modeļi ar skaidrām cenām pa paketēm: rūpnīcas komplekts ar montāžu no '
               '92 000 € ar PVN. Saņemiet pilno katalogu ar cenām savā e-pastā.'),
        'en': ('Timber Frame House Kits in Ireland — Prices and Catalogue | Frest',
               'Scandinavian timber frame kits shipped and erected in Ireland. Four models, fixed kit price '
               'from €92,000 incl. VAT, A-rated fabric. Get the full catalogue with prices by email.'),
    },
    'compare': {
        'lv': ('Salīdzināt moduļu māju modeļus un cenas | Frest',
               'Aura 70, Aura 110, Als 70 un Als 110 blakus: platība, guļamistabas, siltinājums un cena pa '
               'paketēm. Atrodiet, kura koka karkasa māja der jūsu zemesgabalam.'),
        'en': ('Compare Timber Frame House Kits — Size, Spec and Price | Frest',
               'Aura 70, Aura 110, Als 70 and Als 110 side by side: floor area, bedrooms, insulation and the '
               'price of each package. Find the kit that suits your site.'),
    },
    'which': {
        'lv': ('Kura māja jums der? Moduļu mājas konfigurators | Frest',
               'Atbildiet uz pieciem jautājumiem par ģimeni, zemesgabalu un budžetu, un mēs pasakām, kurš '
               'Frest modelis jums der vislabāk — ar platību, plānojumu un cenu paketēm.'),
        'en': ('Which House Kit Suits You? Self-Build Configurator | Frest',
               'Five questions about your family, your site and your budget, and we tell you which Frest '
               'model fits — with floor area, layout and what each package costs.'),
    },
    'pricing': {
        'lv': ('Moduļu māju cenas 2026 — kas ir katrā paketē | Frest',
               'Divas paketes katram modelim: rūpnīcas komplekts ar montāžu un pilnā pakete ar apdari. '
               'Skaidri norādīts, kas cenā nav — pamati, zeme, pieslēgumi un būvatļauja.'),
        'en': ('Timber Frame Kit Prices 2026 — What Each Package Includes | Frest',
               'Two packages per model: the factory kit with assembly, and the complete package with '
               'finishes. Clearly stated what is not in the price — foundation, site, services, permit.'),
    },
    'gallery': {
        'lv': ('Uzbūvēto māju galerija — Latvija un Dānija | Frest',
               'Fotogrāfijas no uzbūvētajām Aura un Als mājām Latvijā un Dānijā: fasādes, interjeri, '
               'terases un montāža objektā.'),
        'en': ('Gallery of Built Timber Frame Homes — Denmark and Latvia | Frest',
               'Photographs of completed Aura and Als houses in Denmark and Latvia: facades, interiors, '
               'terraces and the frame going up on site.'),
    },
    'projects': {
        'lv': ('Realizētie projekti Dānijā un Latvijā | Frest',
               'Kettingskovas ciemats ar astoņām Als mājām vienā sezonā, privātmājas Latvijā un Dānijā — '
               'ar plāniem, fotogrāfijām un stāstu par katru objektu.'),
        'en': ('Completed Timber Frame Projects in Denmark and Latvia | Frest',
               'Eight Als homes built at Kettingskov in a single season, plus private houses in Latvia and '
               'Denmark — with plans, photographs and the story of each site.'),
    },
    'custom': {
        'lv': ('Individuāls mājas projekts uz Als vai Aura bāzes | Frest',
               'Pagarināta māja, pilnvērtīgs otrais stāvs, dvīņu mājas vai vairāku māju apbūve — '
               'projektējam individuāli uz pārbaudītas rūpnīcas konstrukcijas bāzes.'),
        'en': ('Custom Timber Frame Design on an Als or Aura Base | Frest',
               'A longer house, a full first floor, twin homes or a multi-house development — designed to '
               'order on a proven factory-built structure.'),
    },
    'resources': {
        'lv': ('Biežāk uzdotie jautājumi par moduļu mājām | Frest',
               'Cik maksā, cik ilgi būvē, kādi pamati, kāda garantija, vai der kredītam — godīgas atbildes '
               'uz jautājumiem, ko klienti uzdod pirms mājas pasūtīšanas.'),
        'en': ('Timber Frame House Kit FAQ — Cost, Time, Foundations | Frest',
               'What it costs, how long it takes, which foundation, what the warranty covers and what an '
               'Irish self-builder has to arrange locally. Honest answers, no sales talk.'),
    },
    'team': {
        'lv': ('Par SIA Frest — kas mēs esam | Frest Homes',
               'Frest projektē, ražo un uzbūvē skandināvu dizaina mājas Latvijā un Dānijā kopš 2019. gada. '
               'Viens līgums, viena tāme, viens atbildīgais.'),
        'en': ('About Frest Homes — Who Builds Your Kit | Frest',
               'Frest has designed, manufactured and built Scandinavian-design homes in Latvia and Denmark '
               'since 2019. One contract, one estimate, one person responsible.'),
    },
    'catalogue': {
        'lv': ('Katalogs ar cenām — reģistrējieties piekļuvei | Frest',
               'Pilnā komplektācija ar cenu katrai izvēlei — jumts, apdare, grīdas, logi, vannasistabas — '
               'un konfigurators ar summu. Piekļuve pēc reģistrācijas.'),
        'en': ('Catalogue with Prices — Register for Access | Frest',
               'The full specification with a price for every option — roof, finishes, floors, windows, '
               'bathrooms — and a configurator with a running total. Access after registration.'),
    },
    'knowledge': {
        'lv': ('Zināšanu bāze: mājas būvniecība Latvijā | Frest',
               'Izmaksas, pamati, būvatļauja, energoklase, kredīts un grafiks — praktiski raksti par to, kas '
               'tiešām notiek, kad būvē privātmāju Latvijā.'),
        'en': ('Self-Build Knowledge Base for Ireland | Frest Homes',
               'Costs, foundations, planning, Part L and BER, insurance and programme — practical articles '
               'on what actually happens when you build a one-off house in Ireland.'),
    },
    'privacy': {
        'lv': ('Privātuma politika | Frest', 'Kā SIA Frest apstrādā jūsu datus.'),
        'en': ('Privacy policy | Frest', 'How SIA Frest processes your data.'),
    },
    'terms': {
        'lv': ('Noteikumi | Frest', 'Vietnes un piedāvājumu noteikumi.'),
        'en': ('Terms | Frest', 'Website and offer terms.'),
    },
}

# Extra keyword-bearing copy blocks rendered on the pages that need ranking text.
INTRO = {
    'pricing': {
        'lv': 'Moduļu māju cenas nav salīdzināmas, kamēr nav skaidrs, kas ir iekļauts. Šajā lapā katrai '
              'cenai ir nosaukta pakete, un tabulā redzams arī tas, kas nav iekļauts nevienā no tām.',
        'en': 'Timber frame kit prices are not comparable until you know what is in them. On this page every '
              'figure names its package, and the table also shows what is in neither of them.',
    },
}

# Country / region targeting used in schema and in the landing pages.
GEO = {
    'lv': {'area': ['Latvija'], 'lang': 'lv-LV'},
    'en': {'area': ['Ireland', 'Denmark', 'Latvia'], 'lang': 'en-IE'},
}
