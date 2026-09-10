# -*- coding: utf-8 -*-
from content.data import T

UI = {
    # navigation
    'nav_models': T('Modeļi', 'Models'), 'nav_als': 'ALS', 'nav_aura': 'AURA',
    'nav_compare': T('Salīdzināt', 'Compare'), 'nav_which': T('Atrodiet savu māju', 'Find your house'),
    'nav_pricing': T('Cenas', 'Pricing'), 'nav_gallery': T('Galerija', 'Gallery'), 'nav_projects': T('Realizētie projekti', 'Completed projects'),
    'nav_custom': T('Individuāli projekti', 'Custom design'), 'nav_resources': T('Resursi', 'Resources'), 'nav_faq': T('BUJ', 'FAQ'),
    'nav_team': T('Par mums', 'About us'), 'nav_contact': T('Kontakti', 'Contact'), 'nav_catalogue': T('Katalogs ar cenām', 'Catalogue with prices'),
    'nav_addons': T('Moduļi un piebūves', 'Modules and annexes'), 'nav_process': T('Kā tas notiek', 'How it works'),
    'menu': T('Izvēlne', 'Menu'), 'close': T('Aizvērt', 'Close'),
    'lang_switch': T('EN', 'LV'), 'lang_switch_title': T('English version', 'Latviešu versija'),

    # generic
    'from': T('no', 'from'), 'starting_from': T('Sākot no', 'Starting from'), 'weeks': T('nedēļas', 'weeks'), 'weeks_delivery': T('nedēļas līdz atslēgām', 'weeks to keys'),
    'view_model': T('Apskatīt', 'View model'), 'view_all': T('Visi modeļi', 'All models'), 'compare_models': T('Salīdzināt modeļus', 'Compare models'),
    'request': T('Pieprasīt piedāvājumu', 'Request an offer'), 'request_short': T('Pieprasīt', 'Enquire'), 'register': T('Reģistrēties un skatīt cenas', 'Register and see prices'),
    'living_area': T('Telpu platība', 'Living area'), 'total_area': T('Apbūves laukums', 'Building footprint'), 'rooms': T('Istabas', 'Rooms'), 'bedrooms': T('Guļamistabas', 'Bedrooms'),
    'bathrooms': T('Vannasistabas', 'Bathrooms'), 'terrace': T('Terase', 'Terrace'), 'loft': T('Bēniņi / mezanīns', 'Loft / mezzanine'), 'width': T('Platums', 'Width'), 'length': T('Garums', 'Length'),
    'ceiling': T('Griestu augstums', 'Ceiling height'), 'style': T('Stils', 'Style'), 'delivery': T('Piegāde', 'Delivery'), 'warranty_terms': T('Pēc līguma', 'Per contract'), 'warranty': T('Garantija', 'Warranty'), 'years': T('gadi', 'years'),
    'base_price': T('Pamata pakete', 'Base package'), 'complete_price': T('Pilnā pakete', 'Complete package'),
    'm2': 'm²', 'with_vat': T('ar PVN', 'incl. VAT'),
    # Every price on the site must say WHICH package it is. price_base = the factory kit
    # (panels, roof, windows, facade, assembly) — no foundation, no interior.
    'kit_price': T('Rūpnīcas komplekts ar montāžu', 'Factory kit with assembly'),
    'kit_excl': T('Bez pamatiem un iekšējās apdares', 'Excl. foundation and interior finishing'),
    'see_packages': T('Kas ir katrā paketē →', 'What is in each package →'),

    # home
    'hero_eyebrow': T('Projektējam un uzbūvējam', 'We design and we build'),
    'why_title': T('Kāpēc Frest', 'Why Frest'),
    'why': [
        (T('Rūpnīcas precizitāte', 'Factory precision'), T('Sienu un jumta paneļi tiek ražoti sausos apstākļos un montēti objektā dažās dienās.', 'Wall and roof panels are built indoors and assembled on site in days.')),
        (T('Viens līgums, viena atbildība', 'One contract, one responsibility'), T('Projektēšana, saskaņošana, ražošana un būvniecība — viens partneris un viena tāme visam ceļam.', 'Design, permitting, production and construction — one partner and one estimate for the whole way.')),
        (T('Energoklase A', 'Energy class A'), T('300 mm siltinājums sienās, trīskārši logi un zemas apkures izmaksas.', '300 mm wall insulation, triple glazing and low heating costs.')),
        (T('Uzbūvētas Dānijā un Latvijā', 'Built in Denmark and Latvia'), T('Als un Aura mājas dzīvo Kettingskovā, Stiklingenā un Latvijā kopš 2019. gada.', 'Als and Aura homes stand in Kettingskov, Stiklingen and Latvia since 2019.')),
    ],
    'models_title': T('Četri modeļi. Divas sērijas.', 'Four models. Two series.'),
    'models_lead': T('Aura — mūsdienīga, ar zemu siluetu. Als — skandināvu, ar augstu kori un koka fasādi. Katra pieejama kā rūpnīcas komplekts vai atslēgas risinājums.', 'Aura — contemporary with a low silhouette. Als — Scandinavian with a high ridge and wood facade. Each available as a factory kit or turnkey.'),
    'quiz_title': T('Atrodiet savu māju 3 atbildēs', 'Find your house in 3 answers'), 'quiz_lead': T('Trīs jautājumi — un mēs ieteiksim modeli.', 'Three questions and we recommend a model.'),
    'quiz_result': T('Mūsu ieteikums', 'Our recommendation'), 'quiz_restart': T('Sākt no jauna', 'Start over'), 'quiz_next': T('Tālāk', 'Next'),
    'quiz_why': {
        'aura-70': T('Kompakta, mūsdienīga un ekonomiska — vislabākā pirmā māja.', 'Compact, contemporary and economical — the best first home.'),
        'aura-110': T('Trīs guļamistabas un divas vannasistabas mūsdienīgā formā.', 'Three bedrooms and two bathrooms in a contemporary form.'),
        'als-70': T('Skandināvu klasika ar augstu kori un 37 m² viesistabu.', 'Scandinavian classic with a high ridge and a 37 m² living room.'),
        'als-110': T('Plašākā māja: 43 m² viesistaba, trīs guļamistabas un mezanīns.', 'The most spacious: a 43 m² living room, three bedrooms and a mezzanine.'),
    },
    'personalise_title': T('Personalizē fasādi', 'Personalise the facade'), 'personalise_lead': T('Četras fasādes krāsas un divi jumta tipi katram modelim. Izvēlies un redzi uzreiz.', 'Four facade colours and two roof types for every model. Choose and see it instantly.'),
    'colour': T('Fasādes krāsa', 'Facade colour'), 'roof': T('Jumta tips', 'Roof type'), 'current_config': T('Izvēlētā konfigurācija', 'Selected configuration'),
    'process_title': T('Kā tas notiek', 'How it works'), 'process_lead': T('Pieci soļi no pirmās sarunas līdz atslēgām.', 'Five steps from the first conversation to the keys.'),
    'works_title': T('Realizētie projekti', 'Completed projects'), 'works_lead': T('Reālas mājas Dānijā un Latvijā — ne renderi.', 'Real houses in Denmark and Latvia — not renders.'), 'all_works': T('Visi projekti', 'All projects'),
    'addons_title': T('Moduļi un piebūves', 'Modules and annexes'), 'addons_lead': T('Rūpnīcā ražoti moduļi birojam, viesiem vai studijai. Uz zemes skrūvēm, bez pamatiem, 1–2 dienās.', 'Factory-built modules for an office, guests or a studio. On ground screws, no foundations, in 1–2 days.'),
    'addons_why': T('Kāpēc moduļi', 'Why modules'),
    'faq_title': T('Biežāk uzdotie jautājumi', 'Frequently asked questions'), 'all_faq': T('Visi jautājumi', 'All questions'),
    'cta_title': T('Katalogs ar cenām', 'Catalogue with prices'),
    'cta_lead': T('Reģistrējieties un saņemiet piekļuvi pilnajam katalogam: katra komplektācijas izvēle ar cenu, konfigurators ar kopsummu un piedāvājums 30 dienu laikā.', 'Register for access to the full catalogue: every specification option with its price, a configurator with a running total and an offer within 30 days.'),
    'cta_soon': T('Reģistrācija tiek atvērta drīzumā. Līdz tam — pieprasiet piedāvājumu.', 'Registration opens shortly. Until then, request an offer.'),
    'contact_title': T('Sazināties', 'Get in touch'),

    # model page
    'about_model': T('Par modeli', 'About the model'), 'facts': T('Fakti', 'Facts'), 'params': T('Ēkas parametri', 'Building parameters'),
    'floor_plans': T('Plānojums', 'Floor plan'), 'room_legend': T('Telpu eksplikācija', 'Room schedule'), 'view_3d': T('3D skats', '3D view'), 'view_plan': T('Plāns', 'Plan'),
    'key_features': T('Galvenās īpašības', 'Key features'), 'packages': T('Komplektācijas paketes', 'Packages'), 'includes': T('Iekļauts', 'Included'), 'excludes': T('Nav iekļauts', 'Not included'),
    'not_in_any': T('Nevienā paketē nav iekļauts', 'Not included in any package'), 'popular': T('Populārākā', 'Most popular'),
    'model_gallery': T('Galerija', 'Gallery'), 'built_examples': T('Uzbūvētās mājas', 'Built examples'), 'variants': T('Konfigurācijas', 'Configurations'),
    'addons_model': T('Piebūves un moduļi', 'Annexes and modules'), 'addon_total': T('Kopā', 'Total'), 'addon_extra': T('Papildu platība', 'Extra area'),
    'other_models': T('Citi modeļi', 'Other models'), 'open_catalogue': T('Atvērt katalogu ar cenām', 'Open the catalogue with prices'),
    'catalogue_gate': T('Pilnā komplektācija ar cenām reģistrētiem lietotājiem', 'Full specification with prices for registered users'),

    # compare
    'compare_title': T('Salīdzināt modeļus', 'Compare models'), 'compare_lead': T('Visi četri modeļi blakus. Ieslēdziet “tikai atšķirības”, lai redzētu, ar ko tie atšķiras.', 'All four models side by side. Switch on “differences only” to see what sets them apart.'),
    'diff_only': T('Rādīt tikai atšķirības', 'Show differences only'), 'feature': T('Rādītājs', 'Feature'),

    # pricing
    'pricing_title': T('Paketes un cenas', 'Packages and prices'),
    'pricing_lead': T('Divas paketes katram modelim. Pilnā komplektācija ar cenu katrai izvēlei — katalogā pēc reģistrācijas.', 'Two packages for every model. The full specification with a price for every option is in the catalogue after registration.'),
    'whats_included': T('Kas ir iekļauts', 'What is included'), 'delivery_title': T('Piegādes laiks', 'Delivery time'),

    # gallery
    'gallery_title': T('Galerija', 'Gallery'), 'gallery_lead': T('Modeļi, fasādes un uzbūvētās mājas. Filtrējiet pēc modeļa vai projekta.', 'Models, facades and built houses. Filter by model or project.'),
    'filter_all': T('Visi', 'All'), 'filter_models': T('Modeļi', 'Models'), 'filter_works': T('Uzbūvētās mājas', 'Built houses'), 'filter_factory': T('Rūpnīca', 'Factory'),
    'projects_title': T('Realizētie projekti', 'Completed projects'), 'projects_lead': T('Mājas, ko esam uzbūvējuši Dānijā un Latvijā kopš 2019. gada.', 'Houses we have built in Denmark and Latvia since 2019.'),

    # custom
    'custom_title': T('Individuāli projekti', 'Custom design'), 'custom_eyebrow': T('Ārpus standarta modeļiem', 'Beyond the standard models'),
    'custom_lead': T('Mūsu arhitekti projektē unikālas mājas — no koncepta līdz būvniecībai. Tā pati rūpnīcas precizitāte, jūsu plānojums.', 'Our architects design unique homes — from concept to construction. The same factory precision, your layout.'),
    'custom_cta': T('Apspriest savu projektu', 'Discuss your project'), 'size': T('Platība', 'Size'), 'task': T('Uzdevums', 'Scope'),
    'custom_services': [
        (T('Arhitektūras projekts', 'Architectural design'), T('Pilna projekta dokumentācija un saskaņošana', 'Full design documentation and approvals')),
        (T('Projekts + būvniecība', 'Design + build'), T('Pilns pakalpojums no koncepta līdz atslēgām', 'Full service from concept to keys')),
        (T('Modeļa pielāgošana', 'Model adaptation'), T('Als vai Aura pamatne ar jūsu plānojumu', 'An Als or Aura base with your layout')),
    ],

    # resources
    'resources_title': T('Resursi', 'Resources'), 'resources_lead': T('Atbildes uz biežākajiem jautājumiem par rūpnīcā ražotu māju būvniecību.', 'Answers to the most common questions about factory-built homes.'),

    # team
    'team_title': T('Par mums', 'About us'),
    'team_lead': T('Frest apvieno skandināvu dizaina principus ar rūpnīcas ražošanu, lai kvalitatīva māja būtu pieejama vairāk ģimenēm. Komanda strādā Latvijā, Dānijā un Spānijā.', 'Frest combines Scandinavian design principles with factory production so that a quality home is accessible to more families. The team works in Latvia, Denmark and Spain.'),
    'values_title': T('Vērtības', 'Values'), 'leadership': T('Komanda', 'Team'),

    # contact / form
    'form_title': T('Pieprasīt piedāvājumu', 'Request an offer'), 'form_lead': T('Atbildēsim vienas darba dienas laikā.', 'We reply within one working day.'),
    'f_name': T('Vārds', 'Name'), 'f_email': T('E‑pasts', 'E-mail'), 'f_phone': T('Tālrunis', 'Phone'), 'f_model': T('Interesējošais modelis', 'Model of interest'),
    'f_plot': T('Vai jums jau ir zemesgabals?', 'Do you already have a plot?'), 'f_plot_yes': T('Jā', 'Yes'), 'f_plot_no': T('Vēl nē', 'Not yet'),
    'f_message': T('Ziņa', 'Message'), 'f_message_ph': T('Pastāstiet par savu ieceri — vieta, laiks, budžets…', 'Tell us about your plans — location, timing, budget…'),
    'f_consent': T('Piekrītu, ka SIA Frest sazinās ar mani par šo pieprasījumu.', 'I agree that SIA Frest contacts me about this enquiry.'),
    'f_send': T('Nosūtīt', 'Send'), 'f_or': T('vai', 'or'), 'f_call': T('zvaniet', 'call'),
    'f_undecided': T('Vēl nezinu', 'Not decided yet'), 'f_custom': T('Individuāls projekts', 'Custom design'),
    'thanks_title': T('Paldies!', 'Thank you!'), 'thanks_text': T('Jūsu pieprasījums ir saņemts. Sazināsimies vienas darba dienas laikā.', 'Your enquiry has been received. We will be in touch within one working day.'),

    # footer
    'footer_models': T('Modeļi', 'Models'), 'footer_company': T('Uzņēmums', 'Company'), 'footer_help': T('Palīdzība', 'Help'), 'footer_legal': T('Juridiskā informācija', 'Legal'),
    'privacy': T('Privātuma politika', 'Privacy policy'), 'terms': T('Noteikumi', 'Terms'), 'rights': T('Visas tiesības aizsargātas.', 'All rights reserved.'),
    'reg_no': T('Reģ. nr.', 'Reg. no.'),

    # legal pages (drafts)
    'privacy_body': T(
        'SIA Frest (info@frest.lv) apstrādā jūsu vārdu, e‑pastu un tālruņa numuru tikai, lai atbildētu uz jūsu pieprasījumu un sagatavotu piedāvājumu. Dati netiek nodoti trešajām personām, izņemot pakalpojumu sniedzējus, kas nodrošina e‑pasta nosūtīšanu. Datus glabājam ne ilgāk kā 24 mēnešus pēc pēdējās saziņas. Jums ir tiesības pieprasīt datu labošanu vai dzēšanu, rakstot uz info@frest.lv. Sīkdatnes un statistika: vietnes darbībai nepieciešamā informācija tiek glabāta jūsu pārlūkā bez piekrišanas. Ja jūs piekrītat, mēs izmantojam Microsoft Clarity (Microsoft Ireland Operations Limited), lai redzētu, cik tālu lapas tiek ritinātas un kur cilvēki klikšķina, un saglabājam, no kuras reklāmas kampaņas jūs atnācāt. Formās ievadītie dati Clarity ierakstos tiek maskēti. Šos datus Microsoft glabā 90 dienas. Piekrišanu var atsaukt jebkurā brīdī, izmantojot saiti \u201cSīkdatņu izvēle\u201d lapas kājenē; pēc atsaukšanas kampaņas dati tiek izdzēsti no jūsu pārlūka. Bez piekrišanas vietne strādā tieši tāpat.',
        'SIA Frest (info@frest.lv) processes your name, e-mail and phone number only to answer your enquiry and prepare an offer. Data is not shared with third parties except the providers that deliver e-mail. We keep data for no longer than 24 months after the last contact. You may request correction or deletion by writing to info@frest.lv. Cookies and analytics: information needed for the site to work is stored in your browser without consent. If you agree, we use Microsoft Clarity (Microsoft Ireland Operations Limited) to see how far pages are scrolled and where people click, and we store which advertising campaign brought you here. What you type into a form is masked in Clarity recordings. Microsoft keeps this data for 90 days. You can withdraw consent at any time using the \u201cCookie choice\u201d link in the footer; campaign data is deleted from your browser when you do. Decline and the site works exactly the same.'),
    'terms_body': T(
        'Vietnē norādītās cenas ir orientējošas, ar PVN, standarta komplektācijā un neietver pamatu darbus, zemi, pieslēgumus un būvatļauju. Saistošs ir tikai rakstisks SIA Frest piedāvājums, kas derīgs 30 dienas. Attēli ir renderi vai uzbūvēto māju fotogrāfijas; faktiskā apdare var atšķirties atkarībā no izvēlētās komplektācijas.',
        'Prices on this site are indicative, include VAT, apply to the standard specification and exclude foundation works, land, utility connections and the building permit. Only a written offer from SIA Frest, valid for 30 days, is binding. Images are renders or photographs of built houses; the actual finish may differ depending on the chosen specification.'),
}
