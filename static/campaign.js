/* =====================================================================================
   Kampaņas lapas saturs — patērētāja puse.

   Kampaņas lapa ir uzbūvēta ar savu tekstu, un tas ir pareizs bez šī faila. Šeit notiek
   tikai viens: ja adresē ir `?v=<variants>` vai `utm_campaign`, kam Lab ir sagatavojis
   variantu, lapas virsraksts, ievads, čipi un formas nosaukums tiek nomainīti uz to.

   Trīs lietas, kas padara to drošu:
     · nekas netiek dzēsts. Ja variantā lauka nav, paliek tas, kas uzbūvēts;
     · ja galapunkts klusē, ir bloķēts vai variants nav atrasts, lapa paliek tāda, kāda
       ir. Reklāma nekad nenoved uz tukšu lapu;
     · variants tiek ierakstīts formā (`variant` lauks), tāpēc CRM redz, kurš teksts
       atnesa līdu — citādi A/B tests neko nepasaka.

   Iestati window.FREST_CAMPAIGN = { endpoint: '…/exec', lang: 'lv' } pirms šī faila —
   to dara static/campaign-config.js.
   ===================================================================================== */
(function () {
  'use strict';

  var CFG = window.FREST_CAMPAIGN || {};
  var LANG = CFG.lang || document.documentElement.lang || 'en';
  LANG = LANG.indexOf('lv') === 0 ? 'lv' : 'en';
  var CACHE_KEY = 'frest_campaign_' + LANG;
  var CACHE_MS = 5 * 60 * 1000;

  /* ---------------------------------------------------- kurš variants ------------ */
  /* Secība ir apzināta: `?v=` ir tiešs rīkojums (to lieto priekšskatījums Lab), un
     `utm_campaign` ir tas, kas atnāk no reklāmas. Ja ir abi, uzvar `?v=`. */
  function wanted() {
    var q = new URLSearchParams(location.search);
    var v = q.get('v') || q.get('variant') || q.get('utm_campaign');
    if (!v) {
      try { v = sessionStorage.getItem('frest_variant'); } catch (e) {}
    } else {
      try { sessionStorage.setItem('frest_variant', v); } catch (e) {}
    }
    return v ? String(v).trim().toLowerCase() : null;
  }

  /* ---------------------------------------------------- uzlikšana ---------------- */
  /* data-cv="lauks" uz elementa. Vērtība ir teksts; ar data-cv-html="1" tiek atļauts
     <br> un <b> — tikai tur, kur lapa pati to jau lieto (virsraksts). */
  function paint(v) {
    if (!v || typeof v !== 'object') return 0;
    var n = 0, nodes = document.querySelectorAll('[data-cv]');
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i], key = el.getAttribute('data-cv');
      var val = v[key];
      if (val == null || val === '') continue;          /* tukšs lauks nedzēš neko */
      if (el.hasAttribute('data-cv-html')) {
        var safe = String(val)
          .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
          .replace(/&lt;br\s*\/?&gt;/gi, '<br>')
          .replace(/&lt;(\/?)b&gt;/gi, '<$1b>');
        if (el.innerHTML !== safe) { el.innerHTML = safe; n++; }
      } else if (el.textContent !== String(val)) {
        el.textContent = String(val); n++;
      }
    }
    /* Čipi zem virsraksta: masīvs no {v, t}. Ja to nav, paliek uzbūvētie. */
    var chips = document.querySelector('[data-cv-chips]');
    if (chips && Object.prototype.toString.call(v.chips) === '[object Array]' && v.chips.length) {
      var html = '';
      for (var c = 0; c < v.chips.length; c++) {
        var ch = v.chips[c] || {};
        html += '<li><b></b> <span></span></li>';
      }
      chips.innerHTML = html;
      var lis = chips.children;
      for (var k = 0; k < lis.length && k < v.chips.length; k++) {
        lis[k].querySelector('b').textContent = String(v.chips[k].v || '');
        lis[k].querySelector('span').textContent = String(v.chips[k].t || '');
      }
      n++;
    }
    if (n) document.documentElement.setAttribute('data-campaign', v.id || 'on');
    return n;
  }

  /* Variants brauc līdzi formā, lai CRM zina, kurš teksts pārdeva. */
  function tag(id) {
    var forms = document.querySelectorAll('form[data-lead]');
    for (var i = 0; i < forms.length; i++) {
      var f = forms[i];
      if (f.querySelector('input[name="variant"]')) continue;
      var inp = document.createElement('input');
      inp.type = 'hidden'; inp.name = 'variant'; inp.value = id;
      f.appendChild(inp);
    }
  }

  /* ---------------------------------------------------- ievākšana ---------------- */
  function cached() {
    try {
      var raw = localStorage.getItem(CACHE_KEY);
      if (!raw) return null;
      var o = JSON.parse(raw);
      return (Date.now() - o.t < CACHE_MS) ? o.d : null;
    } catch (e) { return null; }
  }
  function remember(d) {
    try { localStorage.setItem(CACHE_KEY, JSON.stringify({ t: Date.now(), d: d })); } catch (e) {}
  }

  function apply(all, id) {
    if (!all) return false;
    var v = all[id];
    if (!v) return false;
    var body = v[LANG] || v;
    body.id = id;
    if (paint(body)) { tag(id); return true; }
    return false;
  }

  function go() {
    var id = wanted();
    if (!id) return;

    /* Lab priekšskatījums padod variantu tieši, bez tīkla — tā redaktorā redz izmaiņas
       uzreiz, arī tad, ja galapunkts vēl nav publicēts.

       Klausāmies tikai tad, kad lapa jau ir rāmī (`window !== top`) un tikai uz Frest
       izcelsmi. Ziņojums var tikai nomainīt tekstu; neko citu tas darīt nevar. */
    if (window !== window.top) {
      window.addEventListener('message', function (e) {
        if (!/^https:\/\/lab\.fresthomes\.com$/.test(e.origin || '')) return;
        var d = e.data;
        if (!d || typeof d !== 'object' || !d.frestCampaignPreview) return;
        var one = {}; one[d.id || id] = { lv: d.frestCampaignPreview, en: d.frestCampaignPreview };
        apply(one, d.id || id);
      });
      try { window.top.postMessage({ frestCampaignReady: true }, '*'); } catch (e) {}
    }

    if (window.FREST_CAMPAIGN_PREVIEW) {
      var p = {}; p[id] = window.FREST_CAMPAIGN_PREVIEW;
      apply(p, id);
      return;
    }

    var warm = cached();
    if (warm) apply(warm, id);
    if (!CFG.endpoint) return;

    var url = CFG.endpoint + (CFG.endpoint.indexOf('?') < 0 ? '?' : '&') + 'action=campaigns';
    var done = false, timer = setTimeout(function () { done = true; }, 6000);

    fetch(url, { method: 'GET', mode: 'cors', credentials: 'omit' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (j) {
        clearTimeout(timer);
        if (done || !j || !j.ok || !j.campaigns) return;
        remember(j.campaigns);
        apply(j.campaigns, id);
      })
      .catch(function () { /* uzbūvētais teksts paliek */ });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go);
  else go();

  window.frestCampaign = { paint: paint, wanted: wanted };
})();
