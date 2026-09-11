/* =====================================================================================
   Frest published prices — the consumer side.

   Every euro figure on the public sites and inside both catalogue gates is printed at
   build time AND tagged with `data-p`. This file asks the parameter store what those
   figures are now, and rewrites the tagged ones.

   The order matters: the page is correct before this file runs. If the endpoint is slow,
   blocked, or has never been published to, the visitor sees the build-time number rather
   than a spinner or a blank. Nothing here can empty a price.

   Set window.FREST_PRICES = { endpoint: '…/exec', market: 'IE', lang: 'en' } before
   loading this file — static/prices-config.js does that.
   ===================================================================================== */
(function () {
  'use strict';

  var CFG = window.FREST_PRICES || {};
  if (!CFG.endpoint || !CFG.market) return;

  var LANG = CFG.lang || document.documentElement.lang || 'en';
  var CACHE_KEY = 'frest_prices_' + CFG.market;
  var CACHE_MS = 10 * 60 * 1000;

  /* ------------------------------------------------------ formatting ------------- */
  /* Must match build.py's eur(): "128 000 €" in Latvian, "€128,000" in English. */
  function eur(n) {
    var v = Math.round(Number(n) || 0);
    /* The gates format money the same way in both languages ("143 700 €"); the public
       sites follow the language. CFG.format lets the caller say which, so a live update
       never reformats a number the page already printed. */
    var suffix = CFG.format ? CFG.format === 'suffix' : LANG.indexOf('lv') === 0;
    if (suffix) return String(v).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' €';
    return '€' + String(v).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }

  /* ------------------------------------------------------ lookup ----------------- */
  /* data-p syntax:  model:<slug>:<base|complete|per_m2|difference>
                     addon:<id>   ·   module:<id>
                     min:<base|complete>   — the lowest of the four, for "from" figures  */
  function valueOf(table, key) {
    var bits = String(key).split(':');
    if (bits[0] === 'model') {
      var m = table.models && table.models[bits[1]];
      return m ? m[bits[2] || 'base'] : null;
    }
    if (bits[0] === 'addon')  return table.addons ? table.addons[bits[1]] : null;
    if (bits[0] === 'module') return table.modules ? table.modules[bits[1]] : null;
    if (bits[0] === 'min') {
      var f = bits[1] || 'base', lo = null;
      for (var s in table.models) {
        var v = table.models[s][f];
        if (v != null && (lo === null || v < lo)) lo = v;
      }
      return lo;
    }
    return null;
  }

  function paint(table) {
    if (!table) return 0;
    var n = 0;
    var nodes = document.querySelectorAll('[data-p]');
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i], v = valueOf(table, el.getAttribute('data-p'));
      if (v == null) continue;
      var next = el.hasAttribute('data-p-raw') ? String(Math.round(v)) : eur(v);
      if (el.textContent !== next) { el.textContent = next; n++; }
    }
    /* JSON-LD offers, so structured data agrees with what the page shows. */
    var ld = document.querySelector('script[type="application/ld+json"][data-p-offer]');
    if (ld) {
      try {
        var obj = JSON.parse(ld.textContent), slug = ld.getAttribute('data-p-offer');
        var m = table.models && table.models[slug];
        if (m && obj.offers) {
          obj.offers.lowPrice = String(m.base);
          obj.offers.highPrice = String(m.complete);
          ld.textContent = JSON.stringify(obj);
        }
      } catch (e) {}
    }
    if (n) document.documentElement.setAttribute('data-prices', 'live');
    return n;
  }

  /* ------------------------------------------------------ fetch ------------------ */
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

  function go() {
    var warm = cached();
    if (warm) paint(warm);

    var url = CFG.endpoint + (CFG.endpoint.indexOf('?') < 0 ? '?' : '&')
            + 'action=prices&market=' + encodeURIComponent(CFG.market);
    var done = false;
    var timer = setTimeout(function () { done = true; }, 6000);

    fetch(url, { method: 'GET', mode: 'cors', credentials: 'omit' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (j) {
        clearTimeout(timer);
        if (done || !j || !j.ok) return;
        var t = j.markets && j.markets[CFG.market];
        if (!t) return;
        remember(t);
        paint(t);
        window.FREST_PRICES.version = j.version;
        window.FREST_PRICES.updated_at = j.updated_at;
      })
      .catch(function () { /* the build-time figures stand */ });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go);
  else go();

  window.frestPrices = { paint: paint, eur: eur };
})();
