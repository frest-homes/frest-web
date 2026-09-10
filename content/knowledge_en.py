# -*- coding: utf-8 -*-
"""Knowledge base in English — fresthomes.com, aimed at Irish self-builders and contractors.

Frest's position in Ireland is deliberately narrow and is stated that way everywhere:
we manufacture the insulated timber frame kit and erect it on your prepared foundation.
Foundation, services, fit-out, certification, planning and warranty are arranged in Ireland.
Nothing in these articles claims an Irish office, an Irish certification, or a turnkey service there.

Block types: h2, h3, p, ul, ol, table, note, img, faq, cta.
"""

A = lambda **kw: kw

ARTICLES_EN = [

A(
 slug='timber-frame-kit-cost-ireland',
 title='What a Timber Frame Kit Actually Costs in Ireland in 2026',
 desc='What is in a timber frame kit price, what is not, and how the kit figure relates to the full cost '
      'of building a one-off house in Ireland. Real ranges, and the questions to ask any supplier.',
 topic='Cost', read=9, date='2026-09-09', hero='als110-day-dk',
 body=[
  ('p', 'A timber frame kit price and a house price are two different numbers, and most of the confusion in '
        'Irish self-build costing comes from treating them as one. This article separates them.'),
  ('h2', 'The short version'),
  ('p', 'A supplied-and-erected insulated timber frame kit for a one-off Irish house typically lands '
        'somewhere between €900 and €1,400 per square metre of floor area, depending on how much of the '
        'envelope the kit carries. That is roughly 30–40 % of what the finished house will cost you. The '
        'rest is site works, foundation, services, fit-out, professional fees and connections.'),
  ('p', 'For reference, the Frest kit for our 103.3 m² Als 110 is €128,000 including VAT — about €1,239 per '
        'square metre — and it covers factory-built insulated wall panels, the roof structure and covering, '
        'windows and external doors, the finished facade and erection on your prepared foundation. It does '
        'not cover the foundation itself or anything inside.'),
  ('h2', 'What the full house costs in Ireland'),
  ('p', 'Published 2026 figures for a one-off rural house in Ireland sit in these bands, excluding site:'),
  ('table', {'head': ['Route', 'Cost per m²', '200 m² house'],
             'rows': [
              ['Direct labour, self-managed', '€1,700–€2,200', '€340,000–€440,000'],
              ['Simple form, main contractor', '€1,800–€2,300', '€360,000–€460,000'],
              ['Typical one-off, main contractor', '€2,000–€2,800', '€400,000–€560,000'],
              ['Architect-designed and tendered', '€3,200–€3,800', '€640,000–€760,000'],
              ['Certified passive or high spec', '€3,800+', '€760,000+'],
             ]}),
  ('p', 'The usual split is about 60 % structure and shell, 40 % finishes and fit-out. A kit takes a large, '
        'well-defined bite out of the first 60 % and fixes its price before you break ground — which is the '
        'real argument for it, more than the headline rate.'),
  ('h2', 'What is never in a kit price'),
  ('ul', ['the site and everything to do with buying it',
          'site clearance, access, and groundworks — commonly €20,000–€50,000 on a rural site',
          'the foundation, whether raft, strip or piled',
          'ESB connection, water supply or well, and the wastewater treatment system',
          'all mechanical and electrical: ASHP, UFH, MVHR, plumbing, wiring — commonly €35,000–€60,000',
          'internal finishes, kitchen, bathrooms, stairs, flooring, painting',
          'professional fees: architect or technician, engineer, assigned certifier, PSDP, QS, BER assessor',
          'planning fees, development contributions, connection fees',
          'self-build insurance and any structural warranty product']),
  ('note', 'If a supplier quotes you a rate per square foot with no package named, the number is not '
           'information. Ask which of the items above are in it before you compare it with anything.'),
  ('h2', 'Where a kit changes your numbers'),
  ('ol', ['<b>Programme.</b> The frame goes up in days, not months, and the house is weather-tight far '
          'earlier. On an Irish site that is not a small thing — it takes the weather out of the critical path.',
          '<b>Certainty.</b> The largest single element of the shell is priced and fixed before the '
          'foundation is poured, which matters to both you and your lender.',
          '<b>Fabric performance.</b> Panels built indoors to a jig hold their insulation dry and their '
          'airtightness line continuous. That is what a good blower-door result is made of.',
          '<b>Finance.</b> Stage drawdowns move faster when the biggest stage completes in a week.']),
  ('h2', 'Where a kit does not help'),
  ('p', 'It does not reduce your groundworks, your services or your fit-out, and it does not shorten '
        'planning. If someone tells you a kit makes a house cheap, they are selling. It makes a large part '
        'of a house fast, predictable and thermally excellent.'),
  ('cta', 'en'),
  ('h2', 'Frequently asked questions'),
  ('faq', [
    ('How much does a timber frame kit cost in Ireland?',
     'Supplied and erected, typically €900–€1,400 per square metre of floor area depending on how complete '
     'the envelope is. The Frest Als 110 kit is €128,000 incl. VAT for 103.3 m², erected on your foundation.'),
    ('Does the kit price include the foundation?',
     'No. No timber frame supplier includes the foundation. You build it locally to the supplier’s '
     'setting-out drawing, to a tighter tolerance than a block build needs.'),
    ('What percentage of the build is the frame?',
     'Roughly 30–40 % of the total construction cost for a supplied-and-erected insulated kit, excluding '
     'site purchase and professional fees.'),
   ]),
 ]),

A(
 slug='cost-to-build-a-house-ireland-2026',
 title='Cost to Build a One-Off House in Ireland in 2026: Where the Money Goes',
 desc='A stage-by-stage breakdown of what a one-off house costs in Ireland in 2026 — groundworks, shell, '
      'services, finishes, fees and connections — and the items self-builders most often leave out.',
 topic='Cost', read=10, date='2026-09-09', hero='als-kettingskov-aerial',
 body=[
  ('p', 'Most self-build budgets fail in the same two places: the ground, and the last 15 %. This is a '
        'stage-by-stage look at where the money actually goes on an Irish one-off house in 2026.'),
  ('h2', 'The headline ranges'),
  ('table', {'head': ['Route', 'Cost per m² (ex site)'],
             'rows': [['Direct labour, self-managed', '€1,700–€2,200'],
                      ['Simple form, main contractor', '€1,800–€2,300'],
                      ['Typical one-off with a main contractor', '€2,000–€2,800'],
                      ['Architect-designed and tendered', '€3,200–€3,800'],
                      ['Certified passive or complex', '€3,800 and up']]}),
  ('p', 'Direct labour saves real money and costs real time. It also moves risk onto you: you become the '
        'coordinator, and every gap between trades is yours.'),
  ('h2', 'Stage by stage'),
  ('h3', 'Site and groundworks — €20,000 to €50,000, sometimes far more'),
  ('p', 'Access, clearance, dig, fill, rock breaking if you are unlucky, drainage, and the percolation area. '
        'This is the single most underestimated line on Irish rural sites, and it is decided by ground '
        'conditions you cannot see when you buy.'),
  ('h3', 'Foundation'),
  ('p', 'Raft, strip or piled depending on your site investigation. An insulated raft is common under timber '
        'frame because it removes the cold bridge at the perimeter and gives you the floor in one operation.'),
  ('h3', 'Structure and shell — around 60 % of the build'),
  ('p', 'Frame or blockwork, roof, windows, external doors, external finish. With a factory kit this is a '
        'fixed price and a short programme; with block it is weather-dependent and priced as it goes.'),
  ('h3', 'Mechanical and electrical — €35,000 to €60,000'),
  ('p', 'Heat pump, underfloor heating, mechanical ventilation with heat recovery, plumbing, first and '
        'second fix electrical. Part L pushes this line up, and there is no way around it.'),
  ('h3', 'Finishes and fit-out — around 40 % of the build'),
  ('table', {'head': ['Item', 'Typical Irish range 2026'],
             'rows': [['Kitchen', '€8,000–€60,000+'],
                      ['Each bathroom', '€3,000–€15,000+'],
                      ['Flooring, installed', '€40–€200+ per m²'],
                      ['Stairs', '€4,000–€25,000+']]}),
  ('h3', 'Professional fees and compliance'),
  ('ul', ['architect or building technician for design and planning',
          'structural engineer',
          'assigned certifier and design certifier under BCAR, for a dwelling that opts in',
          'PSDP — the project supervisor for the design process, a legal requirement',
          'BER assessor for the certificate at completion',
          'quantity surveyor, optional and usually worth it above €400,000']),
  ('h3', 'Connections and outside works'),
  ('p', 'ESB connection, water connection or well and pump, wastewater treatment system and percolation, '
        'driveway, entrance, boundary treatment, landscaping. Budget for these separately and early; they '
        'are the classic end-of-project shock.'),
  ('h2', 'The items people forget'),
  ('ol', ['<b>VAT.</b> Check whether every quote you are comparing is inclusive or exclusive. This alone '
          'can be a 13.5 % swing between two "similar" prices.',
          '<b>Development contributions</b> to the local authority, set as a condition of planning.',
          '<b>Self-build insurance</b> — contract works, public liability and employer’s liability. '
          'Not optional, and not the same as house insurance.',
          '<b>Finance during the build.</b> Interest on staged drawdowns while you may also be paying rent.',
          '<b>Contingency.</b> Ten per cent minimum on a greenfield rural site. Fifteen if the site '
          'investigation threw up anything at all.']),
  ('note', 'Two numbers make a budget safe: the site investigation report before you commit to a design, '
           'and a contingency you refuse to spend on upgrades.'),
  ('cta', 'en'),
  ('faq', [
    ('How much does it cost to build a 200 m² house in Ireland in 2026?',
     'Excluding the site, roughly €400,000–€560,000 with a main contractor at typical one-off rates, or '
     '€340,000–€440,000 if you self-manage with direct labour.'),
    ('Is timber frame cheaper than block in Ireland?',
     'Marginally more per square metre for the structure, and faster to weather-tight. Total build cost is '
     'usually close; the timber frame advantage is programme, airtightness and price certainty.'),
    ('What should my contingency be?',
     'Ten per cent of construction cost on a straightforward site, fifteen on a rural greenfield one.'),
   ]),
 ]),

A(
 slug='is-440-imported-timber-frame-ireland',
 title='IS 440 and Imported Timber Frame: What an Irish Self-Builder Must Check',
 desc='If your timber frame is manufactured outside Ireland, this is the documentation your engineer, '
      'assigned certifier and lender will look for — and the questions to put to the supplier in writing.',
 topic='Compliance', read=9, date='2026-09-09', hero='factory-kit-assembly',
 body=[
  ('p', 'Importing a frame into Ireland is completely normal — a large share of Irish timber frame has '
        'always come from Britain and the Nordics. What is not normal, and what causes real trouble at '
        'sign-off, is arriving on site with a frame and no paperwork. Sort the paperwork first.'),
  ('h2', 'What IS 440 is'),
  ('p', 'IS 440 is the Irish Standard for timber frame construction in dwellings and other buildings — '
        'IS 440:2009, with amendment 1 consolidated in 2014. It sets out design, manufacture, handling and '
        'site assembly requirements for timber frame in an Irish context, and it is the reference your '
        'engineer and certifier will work from. NSAI operates certification schemes for timber frame '
        'manufacture against it.'),
  ('p', 'It is a standard, not a law. Compliance with the Building Regulations is the legal requirement; '
        'IS 440 is the route almost everyone uses to demonstrate it for timber frame, which in practice '
        'makes it the thing you need.'),
  ('h2', 'Why it matters commercially, not just technically'),
  ('ul', ['<b>Your assigned certifier</b> has to be satisfied the structure complies before signing the '
          'certificate of compliance on completion.',
          '<b>Your lender</b> will usually not release the frame stage drawdown without the engineer '
          'confirming compliance.',
          '<b>Structural warranty providers</b> and some insurers have their own timber frame conditions '
          'on top of the standard.',
          '<b>Resale.</b> A future buyer’s solicitor will ask for the completion certificate. Anything '
          'unresolved becomes a price negotiation years later.']),
  ('h2', 'Ask the supplier for these, in writing, before you pay a deposit'),
  ('ol', ['Structural design calculations for your specific house, signed by an engineer, to Eurocode 5 '
          'with the Irish National Annex, including wind loading for your site.',
          'Full specification of the timber: strength class, grading standard, moisture content at '
          'manufacture, and preservative treatment where required.',
          'CE marking and Declaration of Performance for structural timber, engineered timber components '
          'and sheathing boards.',
          'The wall, roof and junction build-ups with U-values, and the condensation risk analysis.',
          'The airtightness strategy, drawn — not described. Where exactly is the continuous line?',
          'Fire performance of the wall and roof build-ups, including cavity barriers and the party wall '
          'condition if there is one.',
          'Durability and manufacturing quality control: what the factory checks and what it records.',
          'Setting-out and tolerance drawings for the foundation, and the erection method statement.',
          'Who erects, under whose insurance, and who is responsible for temporary bracing and weather '
          'protection during erection.']),
  ('note', 'Give this list to your engineer before you send it to a supplier. A supplier who can answer all '
           'nine quickly is a supplier who has done this before. One who answers "our system is fully '
           'certified" without documents is one to be careful with.'),
  ('h2', 'How Frest handles it'),
  ('p', 'We manufacture in Latvia and erect on your prepared foundation. We supply the structural '
        'calculations for your house, the timber and board specifications with their declarations of '
        'performance, the build-ups with U-values, the setting-out and tolerance drawings and the erection '
        'method statement. We do not certify compliance with the Irish Building Regulations — your '
        'engineer and assigned certifier do that, and we give them what they need to do it. We say this '
        'plainly because the alternative is a surprise on your site, and we would rather lose an enquiry '
        'than cause one.'),
  ('cta', 'en'),
  ('faq', [
    ('Can I use an imported timber frame in Ireland?',
     'Yes. It has to be designed and documented so your engineer and assigned certifier can demonstrate '
     'compliance with the Building Regulations, normally by reference to IS 440.'),
    ('Is IS 440 a legal requirement?',
     'No. The Building Regulations are the legal requirement. IS 440 is the standard used in practice to '
     'show a timber frame meets them, so lenders, certifiers and warranty providers expect it.'),
    ('Who signs off the frame on my site?',
     'Your structural engineer inspects and certifies the structure; the assigned certifier signs the '
     'certificate of compliance on completion. The frame supplier is not a substitute for either.'),
   ]),
 ]),

A(
 slug='part-l-nzeb-ber-ireland',
 title='Part L, NZEB and the New BER Scale: What Your House Has to Deliver',
 desc='What Part L and NZEB require of a new Irish dwelling, how the BER scale changed on 24 May 2026, '
      'and what the fabric has to do to reach the top of it.',
 topic='Compliance', read=8, date='2026-09-09', hero='als110-interior-living',
 body=[
  ('p', 'Three acronyms decide how your house is built and how it is graded at the end. They are related '
        'but not the same thing, and mixing them up is how people end up designing to the wrong target.'),
  ('h2', 'Part L is the rule'),
  ('p', 'Part L of the Building Regulations sets the conservation of fuel and energy requirements for a new '
        'dwelling. Compliance is demonstrated through DEAP, the calculation methodology, and it constrains '
        'fabric performance, airtightness, ventilation, the heating system and the renewable energy '
        'contribution together — not one at a time.'),
  ('h2', 'NZEB is the level'),
  ('p', 'Nearly Zero Energy Building is the performance level new dwellings have to reach. In practice it '
        'means a very good fabric, a heat pump rather than a fossil fuel boiler in most designs, controlled '
        'ventilation, and an airtightness result that has to be tested, not assumed.'),
  ('h2', 'BER is the label — and it changed in 2026'),
  ('p', 'On 24 May 2026 the Building Energy Rating scale was simplified. The fifteen old levels became '
        'eight bands: A0, A, B, C, D, E, F and G. The sub-categories such as A1, A2, A3, B1, B2 and B3 were '
        'removed. A0 is a new top band for buildings that are highly energy-efficient and use no fossil '
        'fuels. Certificates issued before the change stay valid for their ten years.'),
  ('note', 'The practical consequence for a self-builder: an A0 is now a meaningful thing to aim at, and it '
           'requires you to keep fossil fuel out of the design entirely. A gas hob is a conversation worth '
           'having with your BER assessor early rather than late.'),
  ('h2', 'What the fabric has to do'),
  ('table', {'head': ['Element', 'What matters', 'Frest Als build-up'],
             'rows': [
              ['Walls', 'U-value and no repeating cold bridge', '290–300 mm insulation in a 371 mm wall'],
              ['Roof', 'Depth of insulation, continuity at eaves', '250–300 mm'],
              ['Floor', 'Perimeter cold bridge is the weak point', '250 mm under the slab'],
              ['Windows', 'Whole-window U-value, not glass only', 'Triple glazed'],
              ['Airtightness', 'A continuous, drawn, buildable line', 'Vapour control layer detailed in the factory'],
              ['Ventilation', 'Heat recovery, commissioned and balanced', 'MVHR-ready, installed locally'],
             ]}),
  ('h2', 'Where factory manufacture helps and where it does not'),
  ('p', 'It helps with the fabric: panels are built indoors to a jig, the insulation never gets wet, and '
        'the airtightness layer is installed in controlled conditions rather than in February rain. It does '
        'nothing for your heat pump sizing, your ventilation commissioning or your DEAP assessment, all of '
        'which are done in Ireland by Irish professionals. A superb frame with an uncommissioned ventilation '
        'system is a bad house.'),
  ('cta', 'en'),
  ('faq', [
    ('What BER will a new house get in 2026?',
     'A new dwelling built to Part L and NZEB will normally land at A, and can reach A0 where the design '
     'uses no fossil fuel and the fabric and systems are strong. The actual result comes from the DEAP '
     'assessment of your specific house.'),
    ('Do the old A1, A2 and A3 ratings still exist?',
     'Not on new certificates. Since 24 May 2026 the scale is A0, A, B, C, D, E, F, G. Existing '
     'certificates remain valid for ten years from issue.'),
    ('Is an airtightness test mandatory?',
     'Yes, a test result is required for the DEAP calculation on a new dwelling. Design for it from the '
     'first drawing; it is very hard to fix afterwards.'),
   ]),
 ]),

A(
 slug='foundations-for-timber-frame-ireland',
 title='Foundations for a Timber Frame House in Ireland',
 desc='Insulated raft, strip foundation or piles — how the choice is made on an Irish site, what each '
      'costs, and why a factory frame needs a tighter foundation tolerance than blockwork.',
 topic='Construction', read=7, date='2026-09-09', hero='als-kettingskov-development',
 body=[
  ('p', 'The foundation is the part of the house your frame supplier will not build and your budget will '
        'not forgive. On an Irish rural site it is also the item most likely to move.'),
  ('h2', 'Start with the site investigation'),
  ('p', 'Before any foundation decision, you need to know what is under the topsoil: soil type, bearing '
        'capacity, water table, and whether there is rock or peat. A site investigation is a small cost '
        'against the risk it removes, and your engineer cannot design without one. On a rural greenfield '
        'site it is not optional.'),
  ('h2', 'The three options'),
  ('h3', 'Insulated raft'),
  ('p', 'A reinforced slab cast on a continuous layer of insulation. It is the natural partner for timber '
        'frame: no perimeter cold bridge, the floor and the foundation in one operation, and a flat, '
        'accurate surface to set the frame out on. Underfloor heating pipes go in before the pour.'),
  ('ul', ['Good for: level or gently sloping sites with reasonable bearing',
          'Watch: every service penetration has to be set out before the pour — there is no second chance',
          'Best for: Part L performance, because the floor perimeter is where heat quietly leaves']),
  ('h3', 'Strip foundation with a suspended or ground-bearing floor'),
  ('p', 'The traditional Irish approach. Works on slopes, tolerates variable ground, gives you a rising '
        'wall to level off. More operations, more cold bridge detail to resolve at the wall-floor junction.'),
  ('h3', 'Piles'),
  ('p', 'Where bearing is poor — peat, made ground, deep soft strata — piles with a ground beam or a piled '
        'raft are the answer. Expensive, definitive, and decided by the engineer rather than by preference.'),
  ('h2', 'Tolerance: the part people miss'),
  ('p', 'A factory-made panel is manufactured to the millimetre. It will not stretch to meet a foundation '
        'that is 30 mm out of square, and packing it out defeats the airtightness detail you paid for. '
        'Frame suppliers issue a setting-out drawing with a tolerance — typically far tighter than a '
        'blockwork build assumes — and the groundworks contractor has to be told about it before he prices, '
        'not after he pours.'),
  ('note', 'Put the frame supplier’s setting-out and tolerance drawing into the groundworks contractor’s '
           'tender documents. It is the single cheapest way to avoid the worst week of your build.'),
  ('h2', 'Sequence'),
  ('ol', ['Site investigation and engineer’s foundation design',
          'Frame supplier issues setting-out, loads and tolerances',
          'Groundworks, drainage and radon barrier',
          'Insulation, reinforcement, service ducts, UFH pipes',
          'Pour and cure',
          'Survey the finished slab and confirm it against the tolerance before the frame is delivered']),
  ('p', 'That last step takes an hour and is skipped constantly. Do it.'),
  ('cta', 'en'),
  ('faq', [
    ('Which foundation is best for timber frame?',
     'An insulated raft in most cases: it eliminates the perimeter cold bridge and gives the accurate, '
     'level base a factory frame needs. Ground conditions can override this.'),
    ('Does the frame supplier design the foundation?',
     'No. The supplier issues loads, setting-out and tolerances; your engineer designs the foundation for '
     'your ground conditions and a local contractor builds it.'),
   ]),
 ]),

A(
 slug='planning-permission-one-off-house-ireland',
 title='Planning Permission for a One-Off House in Ireland: The Sequence',
 desc='From site selection to commencement notice — the order things have to happen in, realistic '
      'timescales, and the conditions that most often catch rural applicants.',
 topic='Planning', read=9, date='2026-09-09', hero='als110-photo-lv-exterior-forest',
 body=[
  ('p', 'Planning is the longest pole in an Irish self-build and the one least affected by how you build. '
        'Understanding the sequence is what stops you paying for work in the wrong order.'),
  ('h2', 'Before you buy the site'),
  ('ul', ['<b>Rural housing policy.</b> Many county development plans restrict one-off rural housing to '
          'applicants with a demonstrated local need. Read the local plan for that county before you fall '
          'in love with a field.',
          '<b>Access and sightlines.</b> A site whose entrance cannot achieve the required sightlines is a '
          'refusal waiting to happen, and sightlines often need land you do not own.',
          '<b>Wastewater.</b> A site assessment and percolation test determine whether and what kind of '
          'treatment system is possible. On some sites the answer is no.',
          '<b>Services.</b> Distance to ESB and to a water main, and whether a well is viable.',
          '<b>Designations and flood risk.</b> Check before, not after.']),
  ('h2', 'The sequence'),
  ('ol', ['Pre-planning consultation with the local authority — free, and worth more than any other hour '
          'you will spend',
          'Site suitability assessment and percolation test',
          'Design, site layout and drawings',
          'Statutory notices: site notice and newspaper notice, both with strict timing rules',
          'Lodge the application',
          'Validation, then the assessment period; a request for further information is common and resets '
          'the clock',
          'Decision, then the third-party appeal window before it becomes final',
          'Discharge any pre-commencement conditions and pay development contributions',
          'Appoint the PSDP, submit the commencement notice and, where applicable, the BCAR certificates',
          'Start on site']),
  ('h2', 'Realistic timing'),
  ('table', {'head': ['Stage', 'Typical duration'],
             'rows': [['Pre-planning and site assessment', '4–10 weeks'],
                      ['Design and preparation of the application', '6–12 weeks'],
                      ['Assessment by the authority', '8 weeks minimum, longer with further information'],
                      ['Further information response', '4–12 weeks if requested'],
                      ['Appeal window', '4 weeks after decision'],
                      ['Conditions, commencement notice and mobilisation', '4–8 weeks'],
                      ['Total, best case to worst', '6 to 18 months']]}),
  ('note', 'Do not order a frame, or anything else with a lead time, before the decision is final and the '
           'pre-commencement conditions are discharged. Manufacturing slots can be held; deposits on a '
           'permission that is under appeal cannot be un-paid.'),
  ('h2', 'Where a factory frame fits'),
  ('p', 'Manufacturing runs in parallel with your foundation, not with your planning. Once permission is '
        'final and the foundation programme is set, the frame is booked to arrive when the slab has cured. '
        'That is the only part of the schedule a kit compresses — but it compresses it a lot.'),
  ('cta', 'en'),
  ('faq', [
    ('How long does planning permission take in Ireland?',
     'Eight weeks is the statutory minimum for a decision, but a one-off rural application realistically '
     'takes six to eighteen months from first site assessment to being able to start on site.'),
    ('Do I need to own the site before applying?',
     'No, but you need the landowner’s written consent to apply, and you need to be able to demonstrate '
     'control of any land needed for access and sightlines.'),
   ]),
 ]),

A(
 slug='self-build-finance-insurance-ireland',
 title='Self-Build Finance and Insurance in Ireland: Stage Payments Explained',
 desc='How a self-build mortgage releases money in stages, what the valuer looks for at each one, and the '
      'three insurances you must have in place before anyone sets foot on the site.',
 topic='Finance', read=7, date='2026-09-09', hero='aura110-hero',
 body=[
  ('p', 'A self-build mortgage does not arrive as a lump sum. It arrives in instalments, each one released '
        'after a valuer confirms the work is done — which means your cash flow, your contracts and your '
        'build sequence all have to be designed around it.'),
  ('h2', 'How stage drawdowns work'),
  ('p', 'The lender agrees a total and splits it into stages. After each stage you request a drawdown, the '
        'valuer inspects and certifies the value in place, and the money is released. You pay interest only '
        'on what has been drawn, which is why an efficient sequence is worth real money.'),
  ('table', {'head': ['Stage', 'Typical share'],
             'rows': [['Foundations and rising walls', '15–20 %'],
                      ['Structure wall plate to roofed and weather-tight', '30–40 %'],
                      ['Windows, external finish, first fix M&E', '20–25 %'],
                      ['Second fix, finishes and completion', '20–30 %']]}),
  ('p', 'Note what this does to a self-builder who is also paying rent: the longer the shell stage takes, '
        'the longer you carry both. A frame that reaches weather-tight in a week rather than three months '
        'is a finance argument as much as a construction one.'),
  ('h2', 'What the lender will want to see'),
  ('ul', ['final grant of planning permission and the approved drawings',
          'a detailed costed schedule of works, broken into sections rather than a single figure',
          'fixed-price contracts or quotations for the major elements',
          'confirmation of your own contribution, usually deployed first',
          'the professional appointments: engineer, assigned certifier, PSDP',
          'insurance certificates before any work starts']),
  ('h2', 'The three insurances'),
  ('ol', ['<b>Contract works.</b> Covers the partly built house and materials on site against fire, storm '
          'and theft. Standard house insurance does not cover a building site.',
          '<b>Public liability.</b> Covers injury or damage to third parties. Non-negotiable.',
          '<b>Employer’s liability.</b> Required the moment you engage labour directly, which is exactly '
          'what direct labour means.']),
  ('p', 'On top of these, consider a structural warranty product if you may sell within ten years, and '
        'check whether your lender requires one.'),
  ('note', 'Buy the insurance before the first machine arrives, not before the first invoice. Cover has to '
           'predate the work, and a site visit by an uninsured friend with a digger is a genuinely '
           'life-changing risk.'),
  ('cta', 'en'),
  ('faq', [
    ('Can I get a mortgage for a kit house in Ireland?',
     'Yes. Lenders finance the house, not the construction method. They will want the structural '
     'documentation for the frame and an engineer’s certification at the relevant stage.'),
    ('When is the frame stage paid?',
     'Usually within the structure drawdown, once the building is roofed and weather-tight and the valuer '
     'has inspected. Frame suppliers normally require payment before or on delivery, so this gap is the '
     'one to plan for with your lender in advance.'),
   ]),
 ]),

A(
 slug='timber-frame-vs-block-ireland',
 title='Timber Frame vs Cavity Block in Ireland: A Practical Comparison',
 desc='Programme, cost, thermal performance, acoustics, moisture, resale and lender attitude — how the two '
      'dominant Irish construction methods really compare in 2026.',
 topic='Technology', read=8, date='2026-09-09', hero='als70-front-dk',
 body=[
  ('p', 'Cavity block is still the default in rural Ireland and timber frame is the challenger. Both build '
        'good houses. They fail differently, cost differently and take different amounts of time, and the '
        'right answer depends more on your site and your schedule than on the method.'),
  ('h2', 'Head to head'),
  ('table', {'head': ['', 'Factory timber frame', 'Cavity block'],
             'rows': [
              ['Time to weather-tight', 'Days for the frame, 2–4 weeks to fully closed', '8–14 weeks'],
              ['Weather dependency', 'Low once erected; erection needs a dry window', 'High throughout'],
              ['Cost per m² of structure', 'Slight premium', 'Baseline'],
              ['Achieving Part L fabric', 'Straightforward — deep insulation in the stud zone', 'Achievable, needs careful detailing at every junction'],
              ['Airtightness', 'Strong, if the vapour layer is detailed and respected on site', 'Depends entirely on plaster continuity'],
              ['Thermal mass', 'Low — heats and cools quickly', 'High — slow to warm, slow to cool'],
              ['Acoustics between rooms', 'Needs deliberate detailing', 'Naturally good'],
              ['Cost certainty', 'Fixed at order', 'Priced as it proceeds'],
              ['Trades available locally', 'Fewer specialist erectors', 'Everywhere'],
              ['Lender and insurer attitude', 'Normal, with documentation', 'Normal'],
             ]}),
  ('h2', 'Where timber frame genuinely wins'),
  ('ul', ['A wet site and a schedule you cannot move — getting a roof on in week two changes everything.',
          'A fabric-first design where you want deep insulation without a 500 mm wall.',
          'Any project where price certainty for the shell matters more than the last few per cent of cost.',
          'Self-builders paying rent during construction.']),
  ('h2', 'Where block still makes sense'),
  ('ul', ['Very complex or heavily curved geometry that would fight a panelised system.',
          'Sites with no crane access at all.',
          'Where the local trade network is entirely blockwork and you are self-managing on price.',
          'Where you specifically want the thermal mass and the acoustic behaviour of masonry.']),
  ('h2', 'The myths worth retiring'),
  ('ol', ['<b>"Timber frame does not last."</b> Scandinavian timber houses stand for a century and more. '
          'What does not last is timber that gets wet and stays wet — which is a detailing and site '
          'protection question, not a material one.',
          '<b>"Timber frame is a fire risk."</b> Fire performance comes from the lining and the cavity '
          'barriers, both of which are designed and tested. During construction, before linings go on, the '
          'risk is real and is managed by site rules.',
          '<b>"You cannot hang anything on the walls."</b> You hang things on noggings, which are put where '
          'the drawings say. Mark your kitchen and your TV before the panels are made.',
          '<b>"It is much cheaper."</b> It is not. It is faster and more predictable.']),
  ('cta', 'en'),
  ('faq', [
    ('Is timber frame warm in an Irish climate?',
     'Yes. The insulation sits in the depth of the wall with no masonry ties bridging it, so a 371 mm wall '
     'can carry 290–300 mm of insulation. The Irish climate question is moisture management, and that is '
     'answered by detailing and by keeping the panels dry during erection.'),
    ('Do Irish banks lend on timber frame?',
     'Yes, routinely, provided the structural documentation is in order and the engineer certifies it.'),
    ('Which is better for resale?',
     'Neither, on the evidence. What affects resale is the BER, the finish quality and the completion '
     'certificate being in order.'),
   ]),
 ]),

]
