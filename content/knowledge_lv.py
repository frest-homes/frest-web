# -*- coding: utf-8 -*-
"""Zināšanu bāze latviešu valodā — frest.lv.

Katrs raksts ir rakstīts uz konkrētu meklēšanas nolūku. Skaitļi, kas nāk no Frest tāmēm, ir atzīmēti;
tirgus diapazoni ir norādīti kā diapazoni, nevis kā precīzas cenas, jo tie mainās.
Bloku veidi: h2, h3, p, ul, ol, table, note, img, faq, cta.
"""

A = lambda **kw: kw

ARTICLES_LV = [

A(
 slug='cik-maksa-uzbuvet-maju-latvija',
 title='Cik maksā uzbūvēt privātmāju Latvijā 2026. gadā',
 desc='Kur aiziet nauda, būvējot privātmāju: zeme, projekts, pamati, konstrukcija, inženierkomunikācijas, '
      'apdare un labiekārtošana. Reāli diapazoni un tas, ko cilvēki visbiežāk aizmirst ieplānot.',
 topic='Izmaksas', read=9, date='2026-09-09', hero='als110-photo-lv-exterior-forest',
 body=[
  ('p', 'Uz jautājumu “cik maksā uzbūvēt māju” nav vienas atbildes, un jebkurš, kas jums to iedod vienā '
        'skaitlī, kaut ko noklusē. Ir tikai saraksts ar posmiem, un katram no tiem ir sava cena. Šis raksts '
        'ir tas saraksts.'),
  ('h2', 'Īsā atbilde'),
  ('p', 'Vienstāva koka karkasa privātmāja ar apdari Latvijā 2026. gadā izmaksā aptuveni 1 400–2 000 € par '
        'kvadrātmetru telpu platības, neskaitot zemi un neskaitot pamatus. Ar pamatiem, pieslēgumiem un '
        'labiekārtošanu reāls kopbudžets 100 m² mājai sākas ap 190 000 € un viegli aiziet līdz 260 000 €, '
        'ja izvēles ir dārgākas vai zemesgabals ir sarežģīts.'),
  ('p', 'Zemākā robeža nav sasniedzama, ja jūs vēlaties parketu, koka/alumīnija logus un akmens virsmas. '
        'Augstākā robeža nav vajadzīga, ja jūs mierīgi dzīvojat ar 33. klases laminātu un PVC logiem. '
        'Tieši šī izvēļu josla ir tā, kur klients reāli kontrolē tāmi.'),
  ('h2', 'Posmi un to īpatsvars'),
  ('table', {'head': ['Posms', 'Aptuveni % no kopbudžeta', 'Ko tas ietver'],
             'rows': [
              ['Zeme', 'atsevišķi', 'Zemesgabala cena Pierīgā svārstās no 15 000 € līdz 90 000 € un vairāk'],
              ['Projektēšana un saskaņošana', '4–8 %', 'Arhitektūra, konstrukcijas, inženiertīkli, topogrāfija, ģeotehnika, būvatļauja'],
              ['Pamati', '8–14 %', 'Sagatavošana, plātne vai lentveida pamati, siltinājums, hidroizolācija'],
              ['Konstrukcija un norobežojošās konstrukcijas', '35–45 %', 'Sienas, jumts, logi, ārdurvis, fasāde, montāža'],
              ['Inženierkomunikācijas', '10–15 %', 'Elektrība, ūdens, kanalizācija, ventilācija, apkure'],
              ['Iekšējā apdare', '18–25 %', 'Grīdas, sienas, griesti, vannasistabas, iekšdurvis, kājlīstes'],
              ['Pieslēgumi un labiekārtošana', '5–12 %', 'Elektrības pieslēgums, urbums vai ūdensvads, septiķis, piebraucamais ceļš, terase, žogs'],
             ]}),
  ('note', 'Šie procenti ir no pieredzes ar reāliem objektiem, nevis no normatīva. Konkrētā mājā tie '
           'pārbīdās: sarežģīts zemesgabals uzpūš pamatus un pieslēgumus, dārga virtuve uzpūš apdari.'),
  ('h2', 'Kas nekad nav “mājas cenā”'),
  ('p', 'Šis ir biežākais pārpratums, un tas maksā cilvēkiem desmitiem tūkstošu. Kad ražotājs vai būvnieks '
        'nosauc mājas cenu, gandrīz nekad tajā nav:'),
  ('ul', ['zemesgabals un tā iegādes izmaksas',
          'pamatu darbi — pat tad, ja pamatu plātne ir “standarta risinājums”',
          'elektrības pieslēgums no sadales tīkla un ūdens ieguve vai pieslēgums',
          'notekūdeņu risinājums — septiķis vai bioloģiskās attīrīšanas iekārta',
          'būvatļauja, nodevas un ekspluatācijā pieņemšana',
          'piebraucamais ceļš, žogs, terase ārpus projekta, apzaļumošana',
          'virtuves mēbeles un iekārtas, mēbeles kopumā',
          'siltumsūkņa iekārta, ja tā nav atsevišķi nosaukta']),
  ('p', 'Pirms salīdzināt divus piedāvājumus, izdrukājiet šo sarakstu un atzīmējiet, kurš no punktiem ir '
        'katrā no tiem. Bieži izrādās, ka lētākais piedāvājums vienkārši ir tas, kurā ir vismazāk.'),
  ('h2', 'Kur reāli var ietaupīt'),
  ('ol', ['<b>Vienkārša forma.</b> Taisnstūris ar divslīpju jumtu ir lētākais m² jebkurā konstrukcijā. '
          'Katrs izlīkums, erkers un jumta ielaidums maksā gan materiālos, gan darbā.',
          '<b>Mazāk kvadrātmetru, vairāk kvalitātes.</b> 95 m² ar labu apdari maksā mazāk un dzīvo labāk '
          'nekā 130 m² ar taupītu apdari.',
          '<b>Grīdas un sienu apdare.</b> Pāreja no parketa uz kvalitatīvu 33. klases laminātu un no '
          'špaktelētas sienas uz laminētu paneļu sistēmu var mainīt tāmi par 8 000–15 000 € 100 m² mājā.',
          '<b>Logu materiāls.</b> Koka/alumīnija logi izskatās un kalpo lieliski, bet PVC ar trīskāršu '
          'stiklojumu dod to pašu siltuma rādītāju par ievērojami mazāku naudu.',
          '<b>Vannasistabu komplektācija.</b> Divas vannasistabas ar vidēju komplektāciju maksā tik, cik '
          'viena ar premium.']),
  ('h2', 'Kur ietaupīt nedrīkst'),
  ('ul', ['<b>Siltinājums un hermētiskums.</b> To vairs nevar mainīt pēc tam, un tas nosaka apkures rēķinu '
          'nākamos trīsdesmit gadus.',
          '<b>Pamati un hidroizolācija.</b> Kļūda šeit ir vienīgā, kas praktiski nav labojama.',
          '<b>Ventilācija.</b> Hermētiska māja bez rekuperācijas ir mitruma problēma, kas tikai gaida.',
          '<b>Projekts.</b> Ietaupīt uz projektēšanu nozīmē maksāt būvniecībā — parasti vairāk.']),
  ('h2', 'Rūpnīcā ražotas mājas ietekme uz budžetu'),
  ('p', 'Rūpnīcā ražota koka karkasa māja nemaina to, cik maksā pamati vai pieslēgumi. Tā maina divas '
        'lietas: konstrukcijas cena ir zināma jau līguma brīdī, nevis pēc būvniecības, un objektā pavadītais '
        'laiks samazinās no mēnešiem uz dienām. Frest rūpnīcas komplekts ar montāžu sākas 92 000 € ar PVN — '
        'tajā ir siltinātas sienas, jumts, logi, ārdurvis, fasāde un montāža objektā, bet nav pamatu un '
        'iekšējās apdares.'),
  ('cta', 'lv'),
  ('h2', 'Biežākie jautājumi'),
  ('faq', [
    ('Cik maksā 100 m² māja Latvijā?',
     'Ar apdari, bez zemes un bez pamatiem — aptuveni 140 000–200 000 €. Ar pamatiem, pieslēgumiem un '
     'labiekārtošanu reāls kopbudžets ir 190 000–260 000 €.'),
    ('Vai koka karkasa māja ir lētāka par mūra māju?',
     'Konstrukcijas posmā parasti jā, un tā ir ievērojami ātrāka. Kopējā budžetā starpība ir mazāka, jo '
     'pamati, inženierkomunikācijas un apdare maksā tikpat.'),
    ('Cik maksā pamati privātmājai?',
     'Siltināta pamatu plātne 100 m² mājai Latvijā parasti izmaksā 18 000–30 000 € atkarībā no grunts, '
     'reljefa un piekļuves.'),
   ]),
 ]),

A(
 slug='modulu-maja-vai-koka-karkasa-maja',
 title='Moduļu māja vai koka karkasa māja — kāda ir atšķirība',
 desc='Moduļu, paneļu un uz vietas būvēta koka karkasa māja: kā tās tiešām atšķiras pēc ražošanas, '
      'transporta, plānojuma brīvības, cenas un kvalitātes kontroles.',
 topic='Tehnoloģija', read=7, date='2026-09-09', hero='factory-kit-assembly',
 body=[
  ('p', 'Latvijā šos trīs vārdus lieto kā sinonīmus, un tas rada pārpratumus jau sarunas pirmajā minūtē. '
        'Atšķirība ir vienkārša: tā ir par to, cik daudz mājas ir gatavs, kad tas atstāj rūpnīcu.'),
  ('h2', 'Trīs tehnoloģijas'),
  ('h3', 'Moduļu māja'),
  ('p', 'Rūpnīcā tiek pabeigta vesela telpu vienība — ar grīdu, griestiem, sienām, bieži arī ar apdari, '
        'elektrību un santehniku. Objektā moduļus noliek uz pamatiem un savieno. Uzstādīšana ir viena diena. '
        'Ierobežojums ir transports: modulis nedrīkst būt platāks par to, ko var pārvest pa ceļu, tāpēc '
        'telpu proporcijas ir sašaurinātas un lielas atvērtas zonas ir grūti panākamas.'),
  ('h3', 'Paneļu (karkasa) māja'),
  ('p', 'Rūpnīcā tiek ražoti sienu un jumta paneļi — karkass, siltinājums, tvaika barjera, apšuvums, bieži '
        'arī jau iemontēti logi. Objektā tos saceļ ar celtni un savieno. Montāža aizņem dienas, nevis mēnešus. '
        'Plānojuma brīvība ir gandrīz tāda pati kā būvējot uz vietas, jo panelis var būt jebkura izmēra '
        'sienas gabals. Frest strādā tieši šajā tehnoloģijā.'),
  ('h3', 'Uz vietas būvēts koka karkass'),
  ('p', 'Viss top objektā: brigāde zāģē, saliek karkasu, liek vati, apšuj. Maksimāla brīvība, minimāla '
        'kvalitātes kontrole. Kokmateriāls un siltinājums stāv laikapstākļos, un mitrs siltinājums nekad '
        'vairs nesasniedz projektēto rādītāju.'),
  ('h2', 'Salīdzinājums'),
  ('table', {'head': ['', 'Moduļu', 'Paneļu', 'Uz vietas'],
             'rows': [
              ['Gatavība, atstājot rūpnīcu', '80–95 %', '50–70 %', '0 %'],
              ['Montāža objektā', '1–2 dienas', '3–10 dienas', '6–14 nedēļas'],
              ['Plānojuma brīvība', 'Ierobežota ar moduļa platumu', 'Praktiski neierobežota', 'Neierobežota'],
              ['Kvalitātes kontrole', 'Ļoti augsta', 'Augsta', 'Atkarīga no brigādes'],
              ['Siltinājuma mitrums', 'Kontrolēts', 'Kontrolēts', 'Risks'],
              ['Transports', 'Dārgs, negabarīta', 'Standarta kravas', 'Nav'],
              ['Pārvietojamība vēlāk', 'Iespējama', 'Nē', 'Nē'],
             ]}),
  ('h2', 'Kā izvēlēties'),
  ('ul', ['Ja jums vajag mazu ēku, ko var aizvest projam — moduļu.',
          'Ja jums vajag pilnvērtīgu ģimenes māju ar atvērtu virtuvi-viesistabu un lielu stiklojumu — paneļu.',
          'Ja jums ir ļoti netipisks projekts, sarežģīta piekļuve un laiks nav svarīgs — uz vietas.']),
  ('note', 'Vārds “moduļu māja” Latvijas sludinājumos bieži nozīmē vienkārši “rūpnīcā ražota māja”. '
           'Pirms salīdzināt cenas, pajautājiet, kas tieši atbrauc uz objektu — gatavas telpas vai paneļi.'),
  ('cta', 'lv'),
  ('faq', [
    ('Vai paneļu māja ir siltāka par mūra māju?',
     'Pie vienāda siltinājuma biezuma — jā, jo koka karkasa sienā nav aukstuma tiltu no mūra saitēm, un '
     'siltinājums aizņem gandrīz visu sienas biezumu. Frest ārsienā ir 290–300 mm siltinājuma.'),
    ('Cik ilgi kalpo koka karkasa māja?',
     'Tikpat ilgi, cik mūra — ja hidroizolācija, tvaika barjera un ventilējamā fasāde ir izdarītas pareizi. '
     'Skandināvijā koka karkasa mājas stāv simt gadus.'),
    ('Vai bankas dod kredītu koka karkasa mājai?',
     'Jā. Bankai svarīgs ir būvprojekts, tāme un tas, ka ēka tiek reģistrēta un nodota ekspluatācijā, '
     'nevis sienas materiāls.'),
   ]),
 ]),

A(
 slug='ka-salidzinat-maju-piedavajumus',
 title='Kā salīdzināt māju piedāvājumus: €/m² gandrīz vienmēr melo',
 desc='Kāpēc divi piedāvājumi ar vienādu cenu par kvadrātmetru nav salīdzināmi, un septiņi jautājumi, '
      'kas jāuzdod katram ražotājam, pirms izvēlaties.',
 topic='Cenas', read=8, date='2026-09-09', hero='als110-day-dk',
 body=[
  ('p', 'Cena par kvadrātmetru ir vienīgais skaitlis, ko cilvēki salīdzina, un tas ir vienīgais skaitlis, '
        'ko ir visvieglāk uzlabot, neko nemainot mājā. Pietiek mainīt to, ko sauc par kvadrātmetru.'),
  ('h2', 'Pirmā slazds: kura platība'),
  ('p', 'Vienai un tai pašai mājai ir vismaz trīs dažādas platības:'),
  ('ul', ['<b>Telpu platība</b> — tas, pa ko jūs staigājat. Als 110 tā ir 103,3 m².',
          '<b>Bruto apbūves laukums</b> — ar sienām. Als 110 tas ir 116,13 m².',
          '<b>Kopējā platība ar terasi un mezanīnu</b> — vēl lielāka.']),
  ('p', 'Ja viens ražotājs dala cenu ar telpu platību, bet otrs ar kopējo platību, otrā €/m² būs par 15–25 % '
        'zemāks, kaut arī māja ir tā pati un cena ir tā pati. Vienmēr prasiet, ar kuru skaitli dalīts.'),
  ('h2', 'Otrā slazds: kura pakete'),
  ('p', 'Rūpnīcas komplekts, komplekts ar montāžu, komplekts ar apdari un atslēgas risinājums ir četras '
        'dažādas cenas vienai mājai, un starp pirmo un pēdējo ir vairāk nekā 50 %. Piedāvājumā, kurā nav '
        'nosaukta pakete, cena nenozīmē neko.'),
  ('h2', 'Septiņi jautājumi'),
  ('ol', ['Ar kuru platību ir rēķināts €/m² — telpu, bruto vai kopējo?',
          'Vai cenā ir montāža objektā, vai tikai komplekta piegāde?',
          'Vai cenā ir pamati? (Gandrīz vienmēr nav — bet to reti pasaka skaidri.)',
          'Cik biezs ir siltinājums sienā, jumtā un pamatu plātnē, un kāds materiāls?',
          'Kādi logi — profils, stiklu skaits, U vērtība, kas ražotājs?',
          'Kas notiek ar inženierkomunikācijām: elektrība, ventilācija, apkure — iekļauts vai nav?',
          'Vai piedāvājumā ir tāme pa sadaļām, vai viena summa?']),
  ('note', 'Ja uz septīto jautājumu atbilde ir “viena summa”, palūdziet tāmi pa sadaļām. Ražotājs, kuram '
           'nav ko slēpt, to iedod. Frest tāme ir sadalīta pa sadaļām, un katrai izvēlei ir sava rinda.'),
  ('h2', 'Kā salīdzināt pēc būtības'),
  ('p', 'Uztaisiet vienkāršu tabulu ar rindām no saraksta augstāk un aizpildiet to katram piedāvājumam. '
        'Tas aizņem stundu un parasti maina lēmumu. Divas lietas, kas gandrīz vienmēr atklājas: lētākais '
        'piedāvājums nav lētākais, kad tam pieskaita trūkstošo, un dārgākais piedāvājums bieži ir vienīgais, '
        'kurā viss ir uzrakstīts.'),
  ('cta', 'lv'),
  ('faq', [
    ('Kāda ir normāla cena par kvadrātmetru Latvijā 2026. gadā?',
     'Ar pilnu apdari, bez pamatiem un zemes — aptuveni 1 400–2 000 €/m² telpu platības. Rūpnīcas '
     'komplektam ar montāžu — aptuveni 1 100–1 400 €/m².'),
    ('Kāpēc viens ražotājs ir par 30 % lētāks?',
     'Trīs biežākie iemesli: cita platība saucējā, cita pakete, vai plānākas norobežojošās konstrukcijas. '
     'Ceturtais, retākais: viņi tiešām ir efektīvāki.'),
   ]),
 ]),

A(
 slug='pamati-privatmajai',
 title='Pamati privātmājai: plātne, lentveida vai skrūvpāļi',
 desc='Kā izvēlēties pamatu tipu koka karkasa mājai Latvijā, ko nosaka ģeotehniskā izpēte, un cik katrs '
      'risinājums reāli maksā.',
 topic='Būvniecība', read=7, date='2026-09-09', hero='als-kettingskov-development',
 body=[
  ('p', 'Pamati ir vienīgā mājas daļa, kuru pēc tam nevar pārtaisīt. Tā ir arī tā daļa, kas visbiežāk '
        'nav iekļauta mājas cenā, un tā, kur zemesgabals var pārsteigt.'),
  ('h2', 'Vispirms ģeotehniskā izpēte'),
  ('p', 'Pirms jebkuras pamatu izvēles vajag zināt, kas ir zem zemes: grunts tips, nestspēja, gruntsūdens '
        'līmenis un sasalšanas dziļums. Izpēte Latvijā maksā aptuveni 400–900 € un ir lētākā apdrošināšana, '
        'ko var nopirkt. Bez tās jebkurš pamatu piedāvājums ir minējums.'),
  ('h2', 'Trīs risinājumi'),
  ('h3', 'Siltināta pamatu plātne'),
  ('p', 'Betona plātne uz siltinājuma slāņa, parasti 200–300 mm EPS zem plātnes. Latvijā tas ir standarta '
        'risinājums koka karkasa mājai un tas, ar kuru Frest strādā. Plātne vienlaikus ir pamats, grīda un '
        'siltuma akumulators, un tajā ērti iebūvēt siltās grīdas caurules.'),
  ('ul', ['Aptuvenā cena: 180–280 €/m² apbūves laukuma',
          'Labi: nav aukstuma tiltu, gatava grīda, ātri',
          'Slikti: prasa līdzenu zemesgabalu un labu grunti, komunikācijas jāplāno precīzi pirms liešanas']),
  ('h3', 'Lentveida pamati ar pagrabu vai ventilējamu pagrīdi'),
  ('p', 'Klasika, kas der slīpam reljefam un tur, kur vajag pagrabu vai tehnisko telpu. Dārgāk, ilgāk, '
        'bet dod telpu zem mājas.'),
  ('ul', ['Aptuvenā cena: 220–400 €/m², ar pagrabu ievērojami vairāk',
          'Labi: reljefs, pagrabs, vēlāka piekļuve komunikācijām',
          'Slikti: vairāk darba, vairāk aukstuma tiltu, ilgāks termiņš']),
  ('h3', 'Skrūvpāļi'),
  ('p', 'Metāla pāļi, ko ieskrūvē gruntī. Ātri, lēti, bez betona darbiem, der mīkstai gruntij un vietām, kur '
        'nedrīkst rakt. Praksē Latvijā tos lieto vasarnīcām, terasēm un vieglām ēkām, retāk pastāvīgai '
        'ģimenes mājai, jo grīdu tad vajag siltināt atsevišķi un pagrīde ir jāventilē.'),
  ('ul', ['Aptuvenā cena: 90–160 €/m²',
          'Labi: ātrums, cena, mitra vai mīksta grunts, minimāls zemes darbs',
          'Slikti: siltināta grīda jārisina atsevišķi, mazāka termiskā masa, ne visas bankas to mīl']),
  ('h2', 'Ko nozīmē “pamati nav iekļauti”'),
  ('p', 'Kad ražotājs saka, ka pamati nav iekļauti, tas nozīmē, ka jūs tos pasūtāt atsevišķi — parasti '
        'vietējam būvniekam pēc ražotāja rasējuma. Ražotājs iedod precīzu pamatu plānu ar enkurojuma '
        'punktiem un pielaidēm; būvnieks to izpilda. Frest gadījumā tieši tā tas notiek, un pielaide ir '
        'stingrāka nekā parastai mūra mājai, jo paneļi ir ražoti līdz milimetram.'),
  ('cta', 'lv'),
  ('faq', [
    ('Cik maksā pamati 100 m² mājai?',
     'Siltināta plātne — aptuveni 18 000–28 000 € ar sagatavošanas darbiem. Sarežģīta grunts vai slīpums '
     'to var palielināt par 30–50 %.'),
    ('Cik ilgi jāgaida, kamēr pamati ir gatavi montāžai?',
     'Parasti 3–6 nedēļas no zemes darbu sākuma, plus betona nabriešanas laiks. Frest ražo paneļus tajā '
     'pašā laikā, tāpēc gaidīšanas nav.'),
   ]),
 ]),

A(
 slug='buvatlauja-privatmajai',
 title='Būvatļauja privātmājai Latvijā: soļi, termiņi un dokumenti',
 desc='No zemesgabala līdz būvatļaujai un no būvatļaujas līdz ekspluatācijai — kas jāizdara, kādā secībā, '
      'cik tas aizņem laiku un kas to var darīt jūsu vietā.',
 topic='Dokumenti', read=8, date='2026-09-09', hero='als110-evening-dk',
 body=[
  ('p', 'Dokumentu ceļš izbiedē vairāk cilvēku nekā būvniecība pati. Patiesībā tas ir paredzams process ar '
        'zināmiem soļiem — tikai garš. Plānojiet no pusgada līdz gadam no lēmuma līdz pirmajam ekskavatoram.'),
  ('h2', 'Secība'),
  ('ol', ['<b>Zemesgabals un tā pārbaude.</b> Zemes lietošanas mērķis, apbūves noteikumi teritorijas '
          'plānojumā, apgrūtinājumi, pieejamie pieslēgumi.',
          '<b>Topogrāfiskais plāns.</b> Sertificēts mērnieks, derīgs parasti divus gadus.',
          '<b>Ģeotehniskā izpēte.</b> Nosaka pamatu risinājumu.',
          '<b>Būvniecības ieceres dokumentācija.</b> Arhitektūras daļa, novietne, fasādes, ainaviskais '
          'risinājums, ja to prasa būvvalde.',
          '<b>Tehniskie noteikumi.</b> Elektrība, ūdens, kanalizācija, gāze, ceļš — no katra turētāja.',
          '<b>Iesniegšana BIS sistēmā.</b> Būvniecības informācijas sistēma; būvvaldei ir normatīvs termiņš '
          'atbildei.',
          '<b>Būvatļauja ar nosacījumiem.</b> Pēc tam jāizstrādā būvprojekts un jāizpilda projektēšanas '
          'nosacījumi.',
          '<b>Atzīme par projektēšanas nosacījumu izpildi.</b> Tikai pēc tās drīkst sākt būvdarbus.',
          '<b>Būvdarbi ar būvuzraudzību un autoruzraudzību.</b>',
          '<b>Apliecinājums par ēkas gatavību un nodošana ekspluatācijā.</b> Kadastrālā uzmērīšana, '
          'izpildmērījumi, ēkas reģistrācija.']),
  ('h2', 'Cik tas aizņem'),
  ('table', {'head': ['Posms', 'Reāls termiņš'],
             'rows': [
              ['Topogrāfija un ģeotehnika', '2–5 nedēļas'],
              ['Ieceres dokumentācija', '3–8 nedēļas'],
              ['Tehniskie noteikumi', '2–8 nedēļas, paralēli'],
              ['Būvvaldes izskatīšana', 'līdz mēnesim, praksē ar precizējumiem ilgāk'],
              ['Būvprojekts un nosacījumu izpilde', '6–16 nedēļas'],
              ['Kopā līdz būvdarbu sākumam', '3–9 mēneši'],
             ]}),
  ('note', 'Termiņi ir orientējoši un atšķiras pa pašvaldībām. Pierīgā, kur slodze ir lielāka, plānojiet '
           'garāko galu.'),
  ('h2', 'Kas to var izdarīt jūsu vietā'),
  ('p', 'Visu no topogrāfijas līdz atzīmei par nosacījumu izpildi var nokārtot projektētājs vai '
        'projektēšanas un būvniecības uzņēmums ar pilnvaru. Tas ir tieši tas, ko nozīmē “projektējam un '
        'uzbūvējam” — jūs parakstāt, mēs kārtojam. Frest projektēšanas un saskaņošanas posms parasti aizņem '
        'no 12 nedēļām līdz pusgadam no projektēšanas līguma.'),
  ('cta', 'lv'),
  ('faq', [
    ('Vai mājai līdz 60 m² vajag būvatļauju?',
     'Vienstāva ēkai ar apbūves laukumu līdz 60 m² procedūra var būt vienkāršota — atkarībā no zonējuma un '
     'ēkas lietošanas veida. Precīzo prasību pasaka konkrētā būvvalde; nekad neplānojiet, balstoties uz '
     'kaimiņa pieredzi citā pašvaldībā.'),
    ('Vai var sākt būvēt uzreiz pēc būvatļaujas saņemšanas?',
     'Nē. Būvatļauja tiek izsniegta ar projektēšanas nosacījumiem; būvdarbus drīkst sākt tikai pēc atzīmes '
     'par to izpildi.'),
   ]),
 ]),

A(
 slug='energoklase-un-apkures-izmaksas',
 title='Energoklase A un apkures izmaksas koka karkasa mājā',
 desc='Ko nozīmē energoklase A praksē, cik biezs siltinājums tam vajadzīgs, un kāds ir reāls apkures '
      'rēķins 70 un 110 kvadrātmetru mājā Latvijā.',
 topic='Energoefektivitāte', read=7, date='2026-09-09', hero='als110-interior-living',
 body=[
  ('p', 'Energoklase ir vienīgais mājas parametrs, kas jums maksās naudu katru mēnesi nākamos trīsdesmit '
        'gadus. Tā arī ir vienīgais parametrs, ko pēc būvniecības praktiski nevar uzlabot.'),
  ('h2', 'Ko nozīmē burti'),
  ('p', 'Ēkas energosertifikātā klasi nosaka aprēķinātais apkurei nepieciešamais enerģijas patēriņš uz '
        'kvadrātmetru gadā. Jaunbūvēm Latvijā prasība ir gandrīz nulles enerģijas ēkas līmenī; klase A '
        'nozīmē būtiski zemāku patēriņu nekā vecai mājai un praksē ir tas, ko jaunai koka karkasa mājai '
        'sasniegt ir dabiski.'),
  ('h2', 'Kas dod klasi A'),
  ('table', {'head': ['Elements', 'Frest Als sērijā', 'Kāpēc tas svarīgi'],
             'rows': [
              ['Ārsienas siltinājums', '290–300 mm', 'Koka karkasā siltinājums aizņem gandrīz visu sienas biezumu'],
              ['Jumta siltinājums', '250–300 mm', 'Siltums iet uz augšu; te ietaupīt ir dārgākā kļūda'],
              ['Pamatu plātnes siltinājums', '250 mm', 'Bez tā plātne ir liels aukstuma tilts'],
              ['Logi', 'Trīskāršs stiklojums', 'Logi ir vājākā vieta jebkurā norobežojošajā konstrukcijā'],
              ['Hermētiskums', 'Tvaika barjera nepārtraukta', 'Caurvējš caur konstrukciju atceļ siltinājumu'],
              ['Ventilācija', 'Rekuperācija', 'Hermētiskā mājā gaiss jāmaina kontrolēti, ar siltuma atgūšanu'],
             ]}),
  ('h2', 'Reāls apkures rēķins'),
  ('p', 'Als 70 aprēķinātās apkures izmaksas ir 280–430 € gadā. Tas ir rēķins par visu apkures sezonu, '
        'nevis mēnesī. Lielākai mājai skaitlis aug aptuveni proporcionāli platībai, nevis lēcienveidā, jo '
        'norobežojošo konstrukciju kvalitāte ir tā pati.'),
  ('note', 'Diapazons ir plats, jo tajā ietilpst gan siltumsūkņa efektivitāte, gan tas, cik silti jums '
           'patīk dzīvot. Divdesmit divi grādi maksā jūtami vairāk nekā divdesmit.'),
  ('h2', 'Siltumsūknis, malka vai gāze'),
  ('ul', ['<b>Gaiss–ūdens siltumsūknis</b> ar siltajām grīdām ir pašreizējais standarts jaunai mājai '
          'Latvijā. Iekārta ar uzstādīšanu — aptuveni 8 000–14 000 €.',
          '<b>Zeme–ūdens</b> ir efektīvāks un dārgāks; atmaksājas lielākā mājā ar lielu patēriņu.',
          '<b>Malkas katls vai kamīns ar ūdens kontūru</b> labi strādā kā papildu avots, ne kā vienīgais.',
          '<b>Gāze</b> jaunbūvē vairs reti ir loģiskā izvēle, ja vien pieslēgums nav jau pie robežas.']),
  ('cta', 'lv'),
  ('faq', [
    ('Vai koka karkasa māja tur siltumu tikpat labi kā mūra?',
     'Pie vienāda siltinājuma biezuma — labāk, jo nav aukstuma tiltu no mūra saitēm. Mūra mājai ir lielāka '
     'termiskā masa, kas nozīmē lēnāku uzsilšanu un lēnāku atdzišanu, nevis mazāku patēriņu.'),
    ('Cik maksā energosertifikāts?',
     'Jaunbūvei aptuveni 150–350 €. To gatavo neatkarīgs sertificēts eksperts un tas ir nepieciešams '
     'nodošanai ekspluatācijā.'),
   ]),
 ]),

A(
 slug='majas-buvniecibas-kredits',
 title='Mājas būvniecības kredīts: kā banka izmaksā naudu pa posmiem',
 desc='Ar ko būvniecības kredīts atšķiras no hipotekārā, kādus dokumentus banka prasa, kā notiek izmaksa '
      'pa posmiem un kāpēc tāme pa sadaļām ir tik svarīga.',
 topic='Finanses', read=7, date='2026-09-09', hero='aura110-hero',
 body=[
  ('p', 'Būvniecības kredīts nav viens pārskaitījums. Banka izmaksā naudu pa daļām, pēc katra posma '
        'pārbaudot, ka tas tiešām ir izdarīts. Tas maina to, kā jāplāno gan naudas plūsma, gan līgums ar '
        'būvnieku.'),
  ('h2', 'Ko banka prasa'),
  ('ul', ['zemesgabals īpašumā vai vienlaicīgi pērkams ar to pašu kredītu',
          'būvatļauja un būvprojekts',
          'būvdarbu tāme pa sadaļām — nevis viena summa',
          'būvniecības līgums ar termiņiem un maksājumu grafiku',
          'apdrošināšana būvniecības laikā',
          'jūsu pašu līdzdalība, parasti 15–30 % no projekta vērtības']),
  ('h2', 'Kā notiek izmaksa'),
  ('p', 'Banka sadala summu posmos un pēc katra posma sūta vērtētāju, kas fiksē paveikto. Tipisks grafiks '
        'jaunai mājai:'),
  ('table', {'head': ['Posms', 'Aptuvenā daļa'],
             'rows': [['Pamati', '15–20 %'], ['Konstrukcija zem jumta', '30–40 %'],
                      ['Logi, fasāde, inženierkomunikācijas', '20–25 %'],
                      ['Apdare un nodošana', '20–30 %']]}),
  ('h2', 'Kāpēc rūpnīcā ražota māja bankai patīk'),
  ('p', 'Divi iemesli. Pirmkārt, konstrukcijas cena ir fiksēta līgumā pirms būvniecības, tāpēc bankas '
        'lielākais risks — sadārdzinājums pa vidu — ir mazāks. Otrkārt, posms “konstrukcija zem jumta” '
        'aizņem dienas, nevis mēnešus, tāpēc procentu maksājumi būvniecības laikā ir mazāki.'),
  ('note', 'Prasiet tāmi pa sadaļām jau pirmajā sarunā ar būvnieku, nevis tad, kad banka to pieprasa. '
           'Uzņēmums, kas to nevar iedot, jums sagādās problēmas arī vēlāk.'),
  ('cta', 'lv'),
  ('faq', [
    ('Cik liela pašu līdzdalība vajadzīga?',
     'Parasti 15–30 %. Ja zemesgabals jau pieder jums un ir bez apgrūtinājumiem, tas bieži tiek ieskaitīts '
     'kā daļa no līdzdalības.'),
    ('Vai var ņemt kredītu tikai mājas komplektam?',
     'Var, bet banka gribēs redzēt visu projektu līdz nodošanai ekspluatācijā, jo nepabeigta māja nav '
     'pilnvērtīgs nodrošinājums.'),
   ]),
 ]),

A(
 slug='cik-ilgi-buve-maju',
 title='Cik ilgi būvē māju: reāls grafiks no lēmuma līdz atslēgām',
 desc='Reāls laika grafiks privātmājas būvniecībai Latvijā — projektēšana, saskaņošana, pamati, '
      'konstrukcija, apdare un nodošana, ar to, kas visbiežāk kavējas.',
 topic='Process', read=6, date='2026-09-09', hero='als-kettingskov-modular-assembly',
 body=[
  ('p', 'Reklāmās mājas top sešpadsmit nedēļās. Tas ir taisnība par konstrukciju un nepatiesība par māju. '
        'Šeit ir viss grafiks, ieskaitot to daļu, kas notiek pirms kāds ko uzbūvē.'),
  ('h2', 'Pilns grafiks'),
  ('table', {'head': ['Posms', 'Ilgums', 'Kas notiek paralēli'],
             'rows': [
              ['Zemesgabala izvēle un pārbaude', '1–6 mēneši', '—'],
              ['Projektēšana un saskaņošana', '12 nedēļas – 6 mēneši', 'Tehniskie noteikumi'],
              ['Pamatu darbi', '3–6 nedēļas', 'Ražošana rūpnīcā jau notiek'],
              ['Komplekta ražošana un montāža', '16–20 nedēļas', 'No tām montāža objektā — dienas'],
              ['Inženierkomunikācijas un apdare', '8–20 nedēļas', 'Labiekārtošana'],
              ['Nodošana ekspluatācijā', '3–8 nedēļas', '—'],
             ]}),
  ('p', 'Kopā no projektēšanas līguma līdz atslēgām reāli sanāk no 24 nedēļām līdz gadam. Katrs projekts ir '
        'mazliet unikāls: zemesgabals, būvvalde un jūsu izvēles maina grafiku.'),
  ('h2', 'Kas kavē visbiežāk'),
  ('ol', ['<b>Lēmumu gaidīšana.</b> Ne būvvaldes, bet jūsu. Flīžu izvēle var apturēt būvlaukumu uz nedēļu.',
          '<b>Tehniskie noteikumi.</b> Elektrības pieslēgums ar jaunu pieslēguma jaudu var aizņemt mēnešus.',
          '<b>Precizējumi būvvaldē.</b> Katrs precizējuma pieprasījums restartē termiņu.',
          '<b>Ziema pamatu darbos.</b> Betonēšana zem nulles ir iespējama, bet dārgāka un lēnāka.',
          '<b>Apdares materiālu piegādes.</b> Netipiskas flīzes vai īpaši logi — seši līdz desmit nedēļas.']),
  ('note', 'Vienīgais posms, kur rūpnīcā ražota māja tiešām lauž grafiku, ir konstrukcija: sienas un jumts '
           'tiek uzcelti dienās, un māja ir zem jumta pirms rudens lietiem. Viss pārējais aizņem tikpat, '
           'cik jebkurai citai mājai.'),
  ('cta', 'lv'),
  ('faq', [
    ('Vai ziemā var būvēt?',
     'Komplektu var montēt visu gadu. Pamatu darbi ziemā ir dārgāki, un apdares darbi prasa apsildītu māju. '
     'Optimāli ir pamati rudenī, montāža ziemā, apdare pavasarī.'),
    ('Cik ilgi aizņem montāža objektā?',
     'Frest paneļu sistēmai — parasti trīs līdz desmit dienas līdz slēgtai ēkai, atkarībā no mājas izmēra.'),
   ]),
 ]),

]
