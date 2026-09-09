# -*- coding: utf-8 -*-
"""Single source of truth for the Frest website content (LV + EN).
Every fact shown on the site comes from here. Numbers flagged with # CHECK need Janis's confirmation."""

def T(lv, en):
    return {'lv': lv, 'en': en}

SITE = {
    'name': 'Frest Homes',
    'company': 'SIA Frest',
    'email': 'info@frest.lv',
    'phone': '+371 20622020',
    'phone_display': '+371 2062 2020',
    'address': T('Rīga, Latvija', 'Riga, Latvia'),
    'facebook': 'https://www.facebook.com/frest.dk',
    'instagram': 'https://www.instagram.com/frest_homes',
    'tagline': T('Skandināvu mājas. Rūpnīcas precizitāte.', 'Scandinavian homes. Factory precision.'),
    'domains': {'lv': 'https://www.frest.lv', 'en': 'https://www.fresthomes.com'},
    'delivery_weeks': '16–20',
    'formsubmit': 'https://formsubmit.co/info@frest.lv',
}

FACADE_COLORS = [
    {'id': 'nordic-gray', 'name': T('Ziemeļu pelēks', 'Nordic Gray'), 'hex': '#9a9ea3'},
    {'id': 'charcoal-black', 'name': T('Ogļu melns', 'Charcoal Black'), 'hex': '#2b2d31'},
    {'id': 'warm-wood', 'name': T('Silts koks', 'Warm Wood'), 'hex': '#a4794e'},
    {'id': 'natural-pine', 'name': T('Dabīga priede', 'Natural Pine'), 'hex': '#d3b27c'},
]
ROOF_TYPES = [
    {'id': 'tile', 'name': T('Betona dakstiņš', 'Concrete tile')},
    {'id': 'metal', 'name': T('Metāla jumts', 'Metal roof')},
]

# Package contents (same for all models; wording from the pricing page)
PACKAGES = {
    'base': {
        'name': T('Pamata pakete', 'Base package'),
        'sub': T('Rūpnīcas komplekts', 'Factory kit'),
        'includes': [
            T('Rūpnīcā ražoti sienu paneļi ar siltinājumu', 'Factory-built insulated wall panels'),
            T('Jumta konstrukcija un segums', 'Roof structure and covering'),
            T('Logi un ārdurvis', 'Windows and exterior doors'),
            T('Pabeigta fasāde', 'Finished facade'),
            T('Montāža objektā', 'Assembly on site'),
            T('Montāžas dokumentācija un tehniskais atbalsts', 'Assembly documentation and technical support'),
        ],
        'excludes': [
            T('Iekšējā apdare', 'Interior finishing'),
            T('Elektroinstalācija un santehnika', 'Electrical and plumbing'),
            T('Virtuve un siltumsūknis', 'Kitchen and heat pump'),
        ],
    },
    'complete': {
        'name': T('Pilnā pakete', 'Complete package'),
        'sub': T('Atslēgas risinājums', 'Turnkey'),
        'popular': True,
        'includes': [
            T('Viss no Pamata paketes', 'Everything in the Base package'),
            T('Pilnīga iekšējā apdare — grīdas, sienas, griesti', 'Full interior finishing — floors, walls, ceilings'),
            T('Elektroinstalācija un santehnika', 'Electrical and plumbing'),
            T('Apkures sistēma un sanitārtehnika', 'Heating system and bathroom fittings'),
            T('Iekšdurvis un kājlīstes', 'Interior doors and skirting'),
        ],
        'excludes': [
            T('Virtuves mēbeles un iekārtas', 'Kitchen cabinets and appliances'),
            T('Siltumsūkņa iekārta', 'Heat pump unit'),
        ],
    },
    'not_in_any': [
        T('Pamatu darbi', 'Foundation works'),
        T('Zemes iegāde un pieslēgumi', 'Land and utility connections'),
        T('Būvatļauja un projekta saskaņošana', 'Building permit and approvals'),
        T('Labiekārtošana', 'Landscaping'),
    ],
    'note': T('Cenas norādītas ar PVN standarta komplektācijā. Galīgā cena tiek precizēta piedāvājumā pēc zemesgabala un komplektācijas izvēles.',
              'Prices include VAT in standard specification. The final price is confirmed in the offer after the plot and specification are chosen.'),  # CHECK
}

MODELS = [
    {
        'slug': 'aura-70', 'name': 'Aura 70', 'series': 'Aura', 'order': 1,
        'tagline': T('Kompakts un mūsdienīgs', 'Compact and contemporary'),
        'lead': T('Kompakta forma, moderna estētika un atvērts plānojums ar lieliem logiem. Ideāla pirmā māja pārim vai mazai ģimenei.',
                  'Compact form, modern aesthetics and an open plan with large windows. The ideal first home for a couple or a small family.'),
        'about': T('Aura 70 ir kompakts un efektīvs modelis mazām ģimenēm. Rūpnīcā ražota konstrukcija ar augstiem siltināšanas standartiem, atvērtu virtuves‑viesistabas zonu, divām guļamistabām un bēniņu stāvu, ko var izmantot kā darba vai viesu telpu.',
                   'Aura 70 is a compact, efficient model for small families. A factory-built structure with high insulation standards, an open kitchen–living area, two bedrooms and a loft that works as a study or guest space.'),
        'area': 72, 'total_area': 70, 'loft': 15, 'terrace': 17, 'width': 7, 'length': None,  # CHECK
        'rooms': 3, 'bedrooms': 2, 'bathrooms': 1, 'ceiling': 2.5,
        'price_base': 95000, 'price_complete': 135000, 'warranty': 2,  # CHECK warranty 2 vs 3
        'style': T('Mūsdienīgs', 'Contemporary'),
        'hero': 'aura70-hero', 'card': 'aura70-facade',
        'facades': {'tile': {'nordic-gray': 'aura70-facade', 'charcoal-black': 'aura70-tile-charcoal-black', 'warm-wood': 'aura70-tile-warm-wood', 'natural-pine': 'aura70-tile-natural-pine'},
                    'metal': {'nordic-gray': 'aura70-metal-nordic-gray', 'charcoal-black': 'aura70-metal-charcoal-black', 'warm-wood': 'aura70-metal-warm-wood', 'natural-pine': 'aura70-metal-natural-pine'}},
        'plans': [
            {'id': 'ground', 'name': T('1. stāvs', 'Ground floor'), 'img': 'aura70-plan-ground', 'view3d': 'aura70-3d-ground'},
            {'id': 'loft', 'name': T('Bēniņu stāvs', 'Loft'), 'img': 'aura70-loft-layout', 'view3d': 'aura70-3d-loft'},
        ],
        'rooms_list': [],
        'features': [T('2 guļamistabas', '2 bedrooms'), T('Atvērta virtuve‑viesistaba', 'Open kitchen–living'), T('1 vannasistaba', '1 bathroom'), T('Terase zem jumta', 'Covered terrace'), T('Lieli logi', 'Large windows'), T('Bēniņu stāvs', 'Loft floor')],
        'gallery': [
            {'img': 'aura70-hero', 'cap': T('Ārējais skats', 'Exterior view')},
            {'img': 'aura70-rendering', 'cap': T('Fasāde ar dakstiņu jumtu', 'Facade with tile roof')},
            {'img': 'aura70-facade-black', 'cap': T('Ogļu melna fasāde', 'Charcoal black facade')},
            {'img': 'aura70-urban', 'cap': T('Aura 70 Urban — dvīņu māju konfigurācija', 'Aura 70 Urban — twin-house configuration')},
            {'img': 'aura70-3d-ground', 'cap': T('1. stāva 3D skats', 'Ground floor 3D view')},
            {'img': 'aura70-3d-loft', 'cap': T('Bēniņu stāva 3D skats', 'Loft 3D view')},
        ],
        'works_tags': ['aura'],
        'variants': [
            {'name': 'Aura 70 Urban', 'img': 'aura70-urban',
             'text': T('Divas Aura 70 vienības uz kopīga zemesgabala ar centrālu autostāvvietu. Piemērots vairāku paaudžu ģimenēm, īres īpašumiem vai nelielai kopienai.',
                       'Two Aura 70 units on a shared plot with central parking. Suited to multi-generational families, rental property or a small community.'),
             'facts': [T('2 × 72 m² neatkarīgas vienības', '2 × 72 m² independent units'), T('Kopīga autostāvvieta', 'Shared parking'), T('Optimizēts pilsētas zemesgabaliem', 'Optimised for urban plots')]},
        ],
    },
    {
        'slug': 'aura-110', 'name': 'Aura 110', 'series': 'Aura', 'order': 2,
        'tagline': T('Paplašināts komforts', 'Extended comfort'),
        'lead': T('Par 40 % vairāk dzīvojamās telpas, trīs guļamistabas un divas vannasistabas. Augošai ģimenei, kas vērtē mūsdienu dizainu.',
                  '40% more living space, three bedrooms and two bathrooms. For a growing family that values contemporary design.'),
        'about': T('Aura 110 papildina Aura sēriju ar trešo guļamistabu, otru vannasistabu un plašāku kopīgo zonu. Tā pati rūpnīcas precizitāte, lielāki logi un vairāk vietas ikdienai.',
                   'Aura 110 extends the Aura series with a third bedroom, a second bathroom and a larger shared zone. The same factory precision, bigger windows and more room for everyday life.'),
        'area': 110, 'total_area': 112, 'loft': 17, 'terrace': 17, 'width': 8, 'length': None,  # CHECK
        'rooms': 4, 'bedrooms': 3, 'bathrooms': 2, 'ceiling': 2.5,
        'price_base': 125000, 'price_complete': 175000, 'warranty': 2,
        'style': T('Mūsdienīgs', 'Contemporary'),
        'hero': 'aura110-hero', 'card': 'aura110-facade',
        'facades': {'tile': {'nordic-gray': 'aura110-tile-nordic-gray', 'charcoal-black': 'aura110-facade', 'warm-wood': 'aura110-tile-warm-wood', 'natural-pine': 'aura110-tile-natural-pine'},
                    'metal': {'nordic-gray': 'aura110-metal-nordic-gray', 'charcoal-black': 'aura110-metal-charcoal-black', 'warm-wood': 'aura110-metal-warm-wood', 'natural-pine': 'aura110-metal-natural-pine'}},
        'plans': [
            {'id': 'ground', 'name': T('1. stāvs', 'Ground floor'), 'img': 'aura110-plan-ground', 'view3d': 'aura110-3d-ground'},
            {'id': 'loft', 'name': T('Bēniņu stāvs', 'Loft'), 'img': 'aura110-loft-layout', 'view3d': 'aura110-3d-loft'},
        ],
        'rooms_list': [],
        'features': [T('3 guļamistabas', '3 bedrooms'), T('Liela virtuve‑ēdamistaba', 'Large kitchen–dining'), T('2 vannasistabas', '2 bathrooms'), T('Terase zem jumta', 'Covered terrace'), T('Lieli logi', 'Large windows'), T('Bēniņu stāvs', 'Loft floor')],
        'gallery': [
            {'img': 'aura110-hero', 'cap': T('Ārējais skats', 'Exterior view')},
            {'img': 'aura110-facade-gray', 'cap': T('Ziemeļu pelēka fasāde', 'Nordic gray facade')},
            {'img': 'aura110-facade-wood', 'cap': T('Silta koka fasāde', 'Warm wood facade')},
            {'img': 'aura110-3d-ground', 'cap': T('1. stāva 3D skats', 'Ground floor 3D view')},
            {'img': 'aura110-3d-loft', 'cap': T('Bēniņu stāva 3D skats', 'Loft 3D view')},
        ],
        'works_tags': ['aura'],
        'variants': [],
    },
    {
        'slug': 'als-70', 'name': 'Als 70', 'series': 'Als', 'order': 3,
        'tagline': T('Ziemeļu minimālisms', 'Nordic minimalism'),
        'lead': T('Autentiska skandināvu estētika ar dabīgu koka apdari, augstu koru un vitrīnu logiem uz terasi. Pirmās mājas uzbūvētas Dānijā 2022. gadā.',
                  'Authentic Scandinavian aesthetics with natural wood cladding, a high ridge and full-height glazing onto the terrace. First homes built in Denmark in 2022.'),
        'about': T('Als 70 ir Frest klasika: viena stāva māja ar 25° jumtu, 2,7 m sienu augstumu un atvērtu virtuves‑viesistabu 37 m² platībā. Divas guļamistabas, sanmezgls, saimniecības telpa un 17 m² terase zem jumta. Energoklase A.',
                   'Als 70 is the Frest classic: a single-storey house with a 25° roof, 2.7 m wall height and an open 37 m² kitchen–living room. Two bedrooms, a bathroom, a utility room and a 17 m² covered terrace. Energy class A.'),
        'area': 68.4, 'total_area': 105.6, 'loft': None, 'terrace': 16.8, 'width': 8.5, 'length': 12.4,
        'rooms': 3, 'bedrooms': 2, 'bathrooms': 1, 'ceiling': 2.7,
        'price_base': 92000, 'price_complete': 129000, 'warranty': 3,
        'style': T('Skandināvu', 'Scandinavian'),
        'hero': 'als70-hero', 'card': 'als-facade',
        'facades': {'tile': {'nordic-gray': 'als-facade', 'charcoal-black': 'als-tile-charcoal-black', 'warm-wood': 'als-tile-warm-wood', 'natural-pine': 'als-tile-natural-pine'},
                    'metal': {'nordic-gray': 'als-metal-nordic-gray', 'charcoal-black': 'als-metal-charcoal-black', 'warm-wood': 'als-metal-warm-wood', 'natural-pine': 'als-metal-natural-pine'}},
        'plans': [
            {'id': 'ground', 'name': T('Plānojums', 'Floor plan'), 'img': 'als70-plan-ground', 'view3d': None},
        ],
        'rooms_list': [('01', T('Ieeja / vējtveris', 'Entrance / porch'), 3.46), ('02', T('Viesu guļamistaba', 'Guest bedroom'), 8.05), ('03', T('Guļamistaba', 'Bedroom'), 11.88), ('04', T('Sanmezgls', 'Bathroom'), 5.48), ('05', T('Virtuve / viesistaba', 'Kitchen / living'), 36.97), ('06', T('Saimniecības telpa', 'Utility room'), 2.50), ('07', T('Terase zem jumta', 'Covered terrace'), 16.81)],
        'params': [
            (T('Ārējie izmēri', 'External dimensions'), '12 430 × 8 494 mm'),
            (T('Jumta slīpums / kore', 'Roof pitch / ridge'), '25° / 4,79 m'),
            (T('Ārsiena', 'External wall'), T('396 mm · 300 mm minerālvate', '396 mm · 300 mm mineral wool')),
            (T('Jumts', 'Roof'), T('475 mm · 300 mm minerālvate', '475 mm · 300 mm mineral wool')),
            (T('Pamatu plātne', 'Foundation slab'), T('250 mm EPS + 150 mm dzelzsbetons', '250 mm EPS + 150 mm reinforced concrete')),
            (T('Energoklase', 'Energy class'), T('A · apkure 280–430 €/gadā', 'A · heating €280–430 per year')),
        ],
        'features': [T('2 guļamistabas', '2 bedrooms'), T('Atvērta virtuve‑viesistaba 37 m²', 'Open 37 m² kitchen–living'), T('1 vannasistaba', '1 bathroom'), T('Terase zem jumta 17 m²', '17 m² covered terrace'), T('Trīskārši logi', 'Triple-glazed windows'), T('Energoklase A', 'Energy class A')],
        'gallery': [
            {'img': 'als70-hero', 'cap': T('Ārējais skats', 'Exterior view')},
            {'img': 'als70-front-dk', 'cap': T('Kettingskov, Dānija, 2022', 'Kettingskov, Denmark, 2022')},
            {'img': 'als70-side-dk', 'cap': T('Sānu skats — Kettingskov, Dānija', 'Side view — Kettingskov, Denmark')},
            {'img': 'als70-black', 'cap': T('Ogļu melna fasāde', 'Charcoal black facade')},
            {'img': 'als70-photo-solar-front', 'cap': T('Uzbūvēta māja ar saules paneļiem', 'Built house with solar panels')},
            {'img': 'als70-photo-solar-terrace', 'cap': T('Terase zem jumta', 'Covered terrace')},
            {'img': 'als70-photo-solar-windows', 'cap': T('Vitrīnu logi', 'Full-height windows')},
            {'img': 'als70-photo-solar-entrance', 'cap': T('Ieeja', 'Entrance')},
        ],
        'works_tags': ['als70', 'kettingskov'],
        'variants': [],
        'catalogue_url': 'https://als70.fresthomes.com/',
    },
    {
        'slug': 'als-110', 'name': 'Als 110', 'series': 'Als', 'order': 4,
        'tagline': T('Plaša ziemeļu elegance', 'Spacious Nordic elegance'),
        'lead': T('Trīs guļamistabas, divi sanmezgli, 43 m² virtuve‑viesistaba un mezanīns. Uzbūvēta Dānijā un Latvijā.',
                  'Three bedrooms, two bathrooms, a 43 m² kitchen–living room and a mezzanine. Built in Denmark and Latvia.'),
        'about': T('Als 110 paplašina Als sērijas filozofiju: 16,7 m garš korpuss, 2,7 m sienas, 25° jumts un 17 m² mezanīna klājs virs guļamistabām. Ārsienās 290 mm siltinājums, jumtā 250 mm. Energoklase A.',
                   'Als 110 extends the Als philosophy: a 16.7 m long body, 2.7 m walls, a 25° roof and a 17 m² mezzanine deck above the bedrooms. 290 mm insulation in the walls, 250 mm in the roof. Energy class A.'),
        'area': 103.3, 'total_area': 143.6, 'loft': 17, 'terrace': 18.3, 'width': 8.6, 'length': 16.7,
        'rooms': 4, 'bedrooms': 3, 'bathrooms': 2, 'ceiling': 2.7,
        'price_base': 128000, 'price_complete': 179000, 'warranty': 3,
        'style': T('Skandināvu', 'Scandinavian'),
        'hero': 'als110-hero', 'card': 'als-tile-charcoal-black',
        'facades': {'tile': {'nordic-gray': 'als-facade', 'charcoal-black': 'als-tile-charcoal-black', 'warm-wood': 'als-tile-warm-wood', 'natural-pine': 'als-tile-natural-pine'},
                    'metal': {'nordic-gray': 'als-metal-nordic-gray', 'charcoal-black': 'als-metal-charcoal-black', 'warm-wood': 'als-metal-warm-wood', 'natural-pine': 'als-metal-natural-pine'}},
        'plans': [
            {'id': 'ground', 'name': T('1. stāvs', 'Ground floor'), 'img': 'als110-plan-ground', 'view3d': 'als110-interior-living'},
            {'id': 'loft', 'name': T('Mezanīns', 'Mezzanine'), 'img': 'als110-loft-layout', 'view3d': 'als110-interior-loft'},
        ],
        'rooms_list': [('01', T('Ieeja / vējtveris', 'Entrance / porch'), 10.0), ('02', T('Sanmezgls', 'Bathroom'), 3.5), ('03', T('Guļamistaba', 'Bedroom'), 9.7), ('04', T('Sanmezgls', 'Bathroom'), 4.0), ('05', T('Guļamistaba', 'Bedroom'), 15.6), ('06', T('Guļamistaba', 'Bedroom'), 8.3), ('07', T('Saimniecības telpa', 'Utility room'), 2.6), ('08', T('Gaitenis', 'Hallway'), 2.9), ('09', T('Virtuve / viesistaba', 'Kitchen / living'), 42.9), ('10', T('Terase zem jumta', 'Covered terrace'), 18.3), ('11', T('Mezanīns (17 m² klājs)', 'Mezzanine (17 m² deck)'), 3.6)],
        'params': [
            (T('Ārējie izmēri', 'External dimensions'), '16 700 × 8 600 mm'),
            (T('Sienas augstums', 'Wall height'), '2,70 m'),
            (T('Jumta slīpums / kore', 'Roof pitch / ridge'), '25° / 4,71 m'),
            (T('Logi un vitrīnas', 'Windows and glazing'), T('11 gab.', '11 units')),
            (T('Ārsienas biezums / siltinājums', 'Wall thickness / insulation'), '371 mm / 290 mm'),
            (T('Jumta siltinājums', 'Roof insulation'), '250 mm'),
            (T('Pamatu plātnes siltinājums', 'Slab insulation'), '250 mm'),
            (T('Energoklase', 'Energy class'), 'A'),
        ],
        'features': [T('3 guļamistabas', '3 bedrooms'), T('Virtuve‑viesistaba 43 m²', '43 m² kitchen–living'), T('2 sanmezgli', '2 bathrooms'), T('Terase zem jumta 18 m²', '18 m² covered terrace'), T('Mezanīns 17 m²', '17 m² mezzanine'), T('Energoklase A', 'Energy class A')],
        'gallery': [
            {'img': 'als110-hero', 'cap': T('Ārējais skats', 'Exterior view')},
            {'img': 'als110-day-dk', 'cap': T('Kettingskov, Dānija, 2022', 'Kettingskov, Denmark, 2022')},
            {'img': 'als110-evening-dk', 'cap': T('Vakara skats — Kettingskov', 'Evening view — Kettingskov')},
            {'img': 'als110-interior-living', 'cap': T('Virtuve‑viesistaba', 'Kitchen–living')},
            {'img': 'als110-interior-ground', 'cap': T('1. stāva interjers', 'Ground floor interior')},
            {'img': 'als110-interior-loft', 'cap': T('Mezanīns', 'Mezzanine')},
            {'img': 'als110-photo-lv-kitchen', 'cap': T('Virtuve — Latvija, 2024', 'Kitchen — Latvia, 2024')},
            {'img': 'als110-photo-lv-bedroom', 'cap': T('Guļamistaba — Latvija, 2024', 'Bedroom — Latvia, 2024')},
            {'img': 'als110-photo-lv-bathroom', 'cap': T('Vannasistaba — Latvija, 2024', 'Bathroom — Latvia, 2024')},
            {'img': 'als110-photo-lv-staircase', 'cap': T('Kāpnes uz mezanīnu', 'Stairs to the mezzanine')},
            {'img': 'als110-photo-lv-exterior-forest', 'cap': T('Māja mežā — Latvija, 2024', 'House in the forest — Latvia, 2024')},
            {'img': 'als110-photo-lv-metal-roof', 'cap': T('Metāla jumts', 'Metal roof')},
        ],
        'works_tags': ['als110', 'kettingskov'],
        'variants': [],
        'catalogue_url': 'https://als110.fresthomes.com/',
        'addons': [
            {'id': 'base', 'name': T('Bāze', 'Base'), 'area': 0, 'price': 0, 'img': 'als110-base-config', 'text': T('Standarta Als 110.', 'Standard Als 110.')},
            {'id': 'carport-left', 'name': T('Nojume kreisajā pusē', 'Carport left'), 'area': 18, 'price': 13500, 'img': 'als110-with-carport', 'text': T('Piebūvēta auto nojume ar papildu noliktavas vietu.', 'Attached carport with extra storage.')},
            {'id': 'carport-right', 'name': T('Nojume labajā pusē', 'Carport right'), 'area': 18, 'price': 13500, 'img': 'als110-carport-right', 'text': T('Tā pati nojume spoguļattēlā.', 'The same carport mirrored.')},
            {'id': 'annex', 'name': T('Dzīvojamā piebūve', 'Living annex'), 'area': 35, 'price': 55000, 'img': 'als110-with-annex', 'text': T('Modulāra piebūve viesiem, birojam vai īrei.', 'Modular annex for guests, an office or rental.')},
            {'id': 'annex-garden', 'name': T('Piebūve un dārzs', 'Annex and garden'), 'area': 35, 'price': 58000, 'img': 'als110-annex-garden', 'text': T('Piebūve ar paplašinātu dārza izkārtojumu.', 'Annex with an extended garden layout.')},
            {'id': 'dual', 'name': T('Dvīņu mājas', 'Dual homes'), 'area': 110, 'price': 179000, 'img': 'als110-dual', 'text': T('Divas Als 110 vairāku paaudžu ģimenei vai investīcijai.', 'Two Als 110 for a multi-generational family or investment.')},
        ],
    },
]

ADDONS = [
    {'name': T('Mājas birojs', 'Home office'), 'area': 20, 'price': 35000, 'text': T('Profesionāla darba telpa ar pilnu aprīkojumu', 'A professional workspace, fully serviced'), 'feats': [T('Siltinātas sienas', 'Insulated walls'), T('Elektroinstalācija', 'Electrical wiring'), T('Liels logs', 'Large window'), T('Ātra uzstādīšana', 'Quick installation')]},
    {'name': T('Viesu māja', 'Guest suite'), 'area': 15, 'price': 28000, 'text': T('Privāta telpa viesiem ar vannasistabu un virtuves nišu', 'Private guest space with a bathroom and kitchenette'), 'feats': [T('Panorāmas stiklojums', 'Panoramic glazing'), T('Sagatavota apkurei', 'Heating ready'), T('Iebūvēts apgaismojums', 'Integrated lighting'), T('Laikapstākļu izturīga', 'Weather-resistant')]},
    {'name': T('Dārza studija', 'Garden studio'), 'area': 25, 'price': 32000, 'text': T('Daudzfunkcionāla telpa hobijiem, mākslai vai atpūtai', 'A multi-purpose space for hobbies, art or rest'), 'feats': [T('Sekcijveida durvis', 'Sectional door'), T('Rozetes un apgaismojums', 'Power and lighting'), T('Noliktavas vieta', 'Storage space'), T('Izturīga konstrukcija', 'Durable construction')]},
]
ADDON_WHY = [
    (T('Ātra uzstādīšana', 'Fast installation'), T('Uzstādīts 1–2 dienās ar minimālu traucējumu', 'Installed in 1–2 days with minimal disruption')),
    (T('Bez pamatiem', 'No foundation'), T('Novietots uz regulējamām zemes skrūvēm', 'Placed on adjustable ground screws')),
    (T('Pārvietojams', 'Relocatable'), T('Var pārvietot, ja pārceļaties', 'Can move with you')),
    (T('Videi draudzīgs', 'Eco-friendly'), T('Ilgtspējīgi materiāli un siltinājums', 'Sustainable materials and insulation')),
]

# Completed works (from the current gallery; captions rewritten, facts unchanged)
WORKS = [
    {'id': 'kettingskov', 'title': T('Als ciemats Kettingskovā', 'Als village in Kettingskov'), 'location': T('Kettingskov, Dānija', 'Kettingskov, Denmark'), 'year': 2022, 'tags': ['als70', 'als110', 'kettingskov'],
     'text': T('Pirmās astoņas Als mājas vienā apbūvē: Als 70 un Als 110 ar melnu, pelēku un koka fasādi.', 'The first eight Als homes in one development: Als 70 and Als 110 with black, gray and wood facades.'),
     'images': [('als-kettingskov-aerial', T('Skats no gaisa', 'Aerial view')), ('als70-front-dk', T('Als 70 ar terasi', 'Als 70 with terrace')), ('als70-side-dk', T('Als 70 sānu skats', 'Als 70 side view')), ('als110-day-dk', T('Als 110 dienā', 'Als 110 by day')), ('als110-evening-dk', T('Als 110 vakarā', 'Als 110 at dusk')), ('als110-evening2-dk', T('Als 110 vakarā', 'Als 110 at dusk')), ('als70-black', T('Als 70 melna fasāde', 'Als 70 black facade')), ('als-kettingskov-development', T('Būvlaukums', 'Development site')), ('als-kettingskov-framing', T('Koka karkass', 'Timber framing')), ('als-kettingskov-modular-assembly', T('Paneļu montāža', 'Panel assembly'))]},
    {'id': 'als110-latvia', 'title': T('Als 110 Latvijā', 'Als 110 in Latvia'), 'location': T('Latvija', 'Latvia'), 'year': 2024, 'tags': ['als110'],
     'text': T('Standarta Als 110 ar metāla jumtu mežā: virtuve, guļamistabas, vannasistaba un kāpnes uz mezanīnu.', 'A standard Als 110 with a metal roof in the forest: kitchen, bedrooms, bathroom and stairs to the mezzanine.'),
     'images': [('als110-photo-lv-exterior-forest', T('Māja mežā', 'House in the forest')), ('als110-photo-lv-metal-roof', T('Metāla jumts', 'Metal roof')), ('als110-photo-lv-kitchen', T('Virtuve', 'Kitchen')), ('als110-photo-lv-bedroom', T('Guļamistaba', 'Bedroom')), ('als110-photo-lv-bathroom', T('Vannasistaba', 'Bathroom')), ('als110-photo-lv-staircase', T('Kāpnes', 'Staircase')), ('als110-latvia-hallway', T('Gaitenis', 'Hallway'))]},
    {'id': 'als110-plus', 'title': T('Als 110+ individuāls projekts', 'Als 110+ custom project'), 'location': T('Latvija', 'Latvia'), 'year': 2024, 'tags': ['als110', 'custom'],
     'text': T('Als 110 pamatne ar individuālu plānojumu, augstiem griestiem un ķieģeļu rakstā liktu parketu.', 'An Als 110 base with a custom layout, high ceilings and herringbone parquet.'),
     'images': [('als110-plus-latvia-exterior', T('Fasāde', 'Facade')), ('als110-plus-latvia-terrace', T('Terase', 'Terrace')), ('als110-plus-latvia-interior', T('Interjers', 'Interior')), ('als110-plus-latvia-kitchen', T('Virtuve', 'Kitchen')), ('als110-plus-latvia-facade-detail', T('Fasādes detaļa', 'Facade detail')), ('als110-plus-latvia-construction', T('Būvniecība', 'Construction'))]},
    {'id': 'als70-solar', 'title': T('Als 70 ar saules paneļiem', 'Als 70 with solar panels'), 'location': T('Dānija', 'Denmark'), 'year': 2023, 'tags': ['als70'],  # CHECK location/year
     'text': T('Als 70 ar melnu fasādi, saules paneļiem uz jumta un terasi zem jumta.', 'Als 70 with a black facade, roof-mounted solar panels and a covered terrace.'),
     'images': [('als70-photo-solar-front', T('Priekšskats', 'Front')), ('als70-photo-solar-terrace', T('Terase', 'Terrace')), ('als70-photo-solar-windows', T('Logi', 'Windows')), ('als70-photo-solar-detail', T('Detaļa', 'Detail')), ('als70-photo-solar-entrance', T('Ieeja', 'Entrance'))]},
    {'id': 'aura-latvia', 'title': T('Aura individuālā izmērā', 'Aura in a custom size'), 'location': T('Latvija', 'Latvia'), 'year': 2023, 'tags': ['aura', 'custom'],
     'text': T('Aura sērijas māja pagarinātā korpusā ar pelēku vertikālu dēļu fasādi.', 'An Aura series house with an extended body and a gray vertical board facade.'),
     'images': [('aura-latvia-exterior', T('Fasāde', 'Facade')), ('aura-latvia-detail-1', T('Detaļa', 'Detail')), ('aura-latvia-detail-2', T('Detaļa', 'Detail'))]},
    {'id': 'energy-house', 'title': T('Energy+ māja', 'Energy+ house'), 'location': T('Stiklingen, Dānija', 'Stiklingen, Denmark'), 'year': 2021, 'tags': ['custom'],
     'text': T('Plakana jumta māja ar koka fasādi un saules paneļiem, kas saražo vairāk enerģijas, nekā patērē.', 'A flat-roof house with a wood facade and solar panels that produces more energy than it uses.'),
     'images': [('energy-house-front-deck', T('Priekšējā terase', 'Front deck')), ('energy-house-exterior', T('Fasāde', 'Facade')), ('energy-house-side-view', T('Sānu skats', 'Side view')), ('energy-house-solar-panels', T('Saules paneļi', 'Solar panels')), ('energy-house-terrace', T('Terase', 'Terrace')), ('energy-house-detail', T('Fasādes detaļa', 'Facade detail'))]},
    {'id': 'aurora', 'title': T('Aurora individuālais projekts', 'Aurora custom design'), 'location': T('Stiklingen, Dānija', 'Stiklingen, Denmark'), 'year': 2019, 'tags': ['custom'],
     'text': T('Individuāls projekts ar plakanu jumtu, koka fasādi un panorāmas logiem.', 'A custom design with a flat roof, wood facade and panoramic windows.'),
     'images': [('aurora-stiklingen-exterior', T('Fasāde', 'Facade')), ('aurora-stiklingen-interior', T('Interjers', 'Interior')), ('aurora-stiklingen-bathroom', T('Vannasistaba', 'Bathroom')), ('aurora-flat-roof-winter-2', T('Ziemā', 'In winter'))]},
    {'id': 'custom-build-2024', 'title': T('Individuāla māja ar auto nojumi', 'Custom house with carport'), 'location': T('Latvija', 'Latvia'), 'year': 2024, 'tags': ['custom'],
     'text': T('Vienstāva māja ar pagarinātu paviljona tipa nojumi, apmestu fasādi un koka akcentiem.', 'A single-storey house with an extended pavilion-style carport, rendered facade and wood accents.'),
     'images': [('custom-build-exterior-sunset', T('Saulrietā', 'At sunset')), ('custom-build-carport-view', T('Auto nojume', 'Carport')), ('custom-build-corner-view', T('Stūra skats', 'Corner view')), ('custom-build-entrance-detail', T('Ieeja', 'Entrance')), ('custom-build-living-room', T('Viesistaba', 'Living room')), ('custom-build-insulation-walls', T('Siltināšana', 'Insulation'))]},
    {'id': 'factory', 'title': T('Rūpnīca un montāža', 'Factory and assembly'), 'location': T('Ražošana', 'Production'), 'year': 2024, 'tags': ['factory'],
     'text': T('Sienu un jumta paneļi tiek ražoti rūpnīcā un objektā uzstādīti ar celtni dažu dienu laikā.', 'Wall and roof panels are produced in the factory and craned into place on site within days.'),
     'images': [('factory-kit-assembly', T('Paneļu montāža ar celtni', 'Crane assembly')), ('factory-wall-construction', T('Sienu montāža', 'Wall assembly')), ('factory-roof-installation', T('Jumta paneļi', 'Roof panels')), ('factory-construction', T('Ražošana', 'Production'))]},
]

CUSTOM_PROJECTS = [
    {'name': 'Ģimnastikas 41', 'size': 195, 'task': T('Tikai projekts', 'Design only'), 'img': 'custom-gimnastikas-41', 'text': T('Mūsdienīgs fasādes dizains ar vertikālām koka lameļu detaļām', 'Contemporary facade design with vertical timber slat details')},
    {'name': 'Avotkalna 12, Engure', 'size': 115, 'task': T('Projekts + būvniecība', 'Design + build'), 'img': 'custom-avotkalna-12', 'text': T('Moderna vienstāva māja ar pagarinātu paviljona tipa auto nojumi', 'A modern single-storey house with an extended pavilion-style carport')},
    {'name': 'Juglasciema bulvāris, Rīga', 'size': 115, 'task': T('Projekts + būvniecība', 'Design + build'), 'img': 'juglas-bulvaris-completed', 'text': T('Uzbūvēta individuāla māja ar 115 m² dzīvojamo platību un koka fasādi', 'A completed custom home with 115 m² of living space and a wood facade')},
]

PROCESS = [
    (T('Konsultācija', 'Consultation'), T('Pārrunājam zemesgabalu, ģimenes vajadzības un budžetu. Iesakām modeli un komplektāciju.', 'We discuss the plot, your family’s needs and the budget, and recommend a model and specification.')),
    (T('Piedāvājums un konfigurācija', 'Offer and configuration'), T('Reģistrētie klienti katalogā konfigurē māju ar cenām un saņem precizētu piedāvājumu.', 'Registered clients configure the house with prices in the catalogue and receive a detailed offer.')),
    (T('Projekts un atļauja', 'Design and permit'), T('Novietojuma projekts, topogrāfija, ģeotehniskā izpēte un būvatļauja.', 'Site plan, topography, geotechnical survey and building permit.')),
    (T('Ražošana rūpnīcā', 'Factory production'), T('Sienu un jumta paneļi tiek ražoti sausos apstākļos ar milimetru precizitāti.', 'Wall and roof panels are produced indoors with millimetre precision.')),
    (T('Montāža un atslēgas', 'Assembly and keys'), T('Montāža objektā dažās dienās, apdare un nodošana 16–20 nedēļās no pasūtījuma.', 'Assembly on site in days, finishing and handover within 16–20 weeks of the order.')),
]

FAQ = [
    (T('Cik ilgā laikā tiek uzbūvēta Frest māja?', 'How long does a Frest home take?'),
     T('No pasūtījuma apstiprinājuma līdz nodošanai parasti paiet 16–20 nedēļas. Rūpnīcā paneļi tiek ražoti paralēli pamatu darbiem, tāpēc montāža objektā aizņem tikai dažas dienas.',
       'From order confirmation to handover usually takes 16–20 weeks. Panels are produced in the factory while the foundations are built, so on-site assembly takes only days.')),
    (T('Kas ir iekļauts Pamata un Pilnajā paketē?', 'What is in the Base and Complete packages?'),
     T('Pamata pakete ir rūpnīcas komplekts ar montāžu: siltināti sienu paneļi, jumts, logi, ārdurvis un pabeigta fasāde. Pilnā pakete pievieno iekšējo apdari, elektroinstalāciju, santehniku un apkuri. Neviena pakete neietver pamatu darbus, zemi un būvatļauju.',
       'The Base package is the factory kit with assembly: insulated wall panels, roof, windows, exterior doors and a finished facade. The Complete package adds interior finishing, electrical, plumbing and heating. Neither package includes foundation works, land or the building permit.')),
    (T('Vai plānojumu var mainīt?', 'Can the layout be changed?'),
     T('Jā. Standarta modeļiem var izvēlēties apdari, fasādes krāsu un jumta tipu, kā arī veikt izmaiņas plānojumā — pārvietot sienas vai pievienot moduļus. Pilnīgi unikālam projektam piedāvājam individuālo projektēšanu.',
       'Yes. Standard models let you choose finishes, facade colour and roof type, and make layout changes — moving walls or adding modules. For a fully unique home we offer custom design.')),
    (T('Kāda ir mājas energoefektivitāte?', 'How energy-efficient are the houses?'),
     T('Als sērijai ir energoklase A: ārsienās 290–300 mm siltinājuma, jumtā 250–300 mm, pamatu plātnē 250 mm, trīskārši logi. Als 70 aprēķinātās apkures izmaksas ir 280–430 € gadā.',
       'The Als series has energy class A: 290–300 mm of wall insulation, 250–300 mm in the roof, 250 mm under the slab and triple glazing. Als 70 has calculated heating costs of €280–430 per year.')),
    (T('Kā redzēt cenas un konfigurēt māju?', 'How do I see prices and configure a house?'),
     T('Reģistrējieties katalogā — tur ir pilna komplektācija ar cenām katrai izvēlei, konfigurators ar kopsummu un iespēja nosūtīt savu izvēli Frest komandai.',
       'Register for the catalogue — it holds the full specification with a price for every option, a configurator with a running total, and a way to send your choice to the Frest team.')),
    (T('Vai Frest būvē ārpus Latvijas?', 'Does Frest build outside Latvia?'),
     T('Jā. Mājas uzbūvētas Dānijā (Kettingskov, Stiklingen) un Latvijā; Als sērija radīta Dānijas tirgum un pielāgota Baltijas klimatam.',
       'Yes. Homes have been built in Denmark (Kettingskov, Stiklingen) and Latvia; the Als series was created for the Danish market and adapted to the Baltic climate.')),
]

TEAM = [
    {'name': 'Jānis Bērziņš', 'role': T('Vadītājs', 'Managing director'), 'unit': 'Frest Homes', 'img': None,
     'bio': T('Vairāk nekā 15 gadu pieredze ilgtspējīgā mājokļu būvniecībā un modulārajā ražošanā. Frest misija — kvalitatīvas mājas par pieejamu cenu.', 'Over 15 years in sustainable housing and modular construction. The Frest mission: quality homes at accessible prices.')},
    {'name': 'Māris Veitners', 'role': T('Būvniecības vadītājs', 'Head of construction'), 'unit': T('Baltija', 'Baltics'), 'img': 'team-maris',
     'bio': T('Nodrošina, ka katra Frest māja atbilst Ziemeļeiropas klimata un Baltijas būvnormatīvu prasībām.', 'Makes sure every Frest home meets Northern European climate and Baltic building standards.')},
    {'name': 'Ivars Buts', 'role': T('Būvniecības vadītājs', 'Head of construction'), 'unit': T('Spānija', 'Spain'), 'img': 'team-ivars',
     'bio': T('Pielāgo skandināvu dizaina principus Vidusjūras klimatam.', 'Adapts Scandinavian design principles to the Mediterranean climate.')},
    {'name': 'Anna Rancāne', 'role': T('Vadošā arhitekte', 'Senior architect'), 'unit': T('Projektēšana', 'Design'), 'img': 'team-anna',
     'bio': T('Minimālisms un funkcionāls dizains, kas veido visu Frest modeļu estētiku.', 'Minimalism and functional design that shape the aesthetic of every Frest model.')},
    {'name': 'Uldis Trokšs', 'role': T('Ražošanas partneris', 'Factory production partner'), 'unit': T('Ražošana', 'Manufacturing'), 'img': None,
     'bio': T('Vada rūpnīcas darbību un kvalitātes kontroli.', 'Runs factory operations and quality control.')},
    {'name': 'Patryk Borkowski', 'role': T('Pārdošanas vadītājs', 'Head of sales'), 'unit': T('Dienvideiropa', 'Southern Europe'), 'img': None,
     'bio': T('Vada Frest izaugsmi Vidusjūras tirgos.', 'Leads Frest’s growth in Mediterranean markets.')},
]
VALUES = [
    (T('Kvalitāte', 'Quality'), T('Katra detaļa — mājai, kas kalpo desmitgadēm', 'Every detail, for a home that lasts decades')),
    (T('Ilgtspēja', 'Sustainability'), T('Energoefektīvi risinājumi un koka konstrukcijas', 'Energy-efficient solutions and timber structures')),
    (T('Caurskatāmība', 'Transparency'), T('Skaidras cenas un godīga komunikācija katrā solī', 'Clear prices and honest communication at every step')),
    (T('Attīstība', 'Innovation'), T('Nepārtraukti uzlabojam mūsdienu dzīvei', 'Continuously improving for modern living')),
]

# "Which house is mine?" recommender
QUIZ = {
    'q': [
        {'id': 'who', 'label': T('Kas dzīvos mājā?', 'Who will live in the house?'), 'opts': [('couple', T('Pāris vai viens cilvēks', 'A couple or one person')), ('family-small', T('Ģimene ar 1–2 bērniem', 'Family with 1–2 children')), ('family-big', T('Ģimene ar 3+ bērniem vai vairākas paaudzes', 'Family with 3+ children or several generations'))]},
        {'id': 'style', 'label': T('Kāds stils jums tuvāks?', 'Which style is closer to you?'), 'opts': [('aura', T('Mūsdienīgs — vienkāršas līnijas, plakans siluets', 'Contemporary — simple lines, low silhouette')), ('als', T('Skandināvu — augsta kore, koka fasāde, vitrīnu logi', 'Scandinavian — high ridge, wood facade, full-height glazing'))]},
        {'id': 'budget', 'label': T('Kāds ir budžets mājai bez zemes?', 'What is the budget for the house, excluding land?'), 'opts': [('lt140', T('Līdz 140 000 €', 'Up to €140,000')), ('gt140', T('Virs 140 000 €', 'Over €140,000'))]},
    ],
}
