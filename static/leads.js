/* Frest lead capture.
 *
 * Every form marked [data-lead] posts to two places:
 *   1. the lead endpoint (Google Apps Script web app) — writes the row, issues a catalogue
 *      passcode and sends the auto-reply. This is the pipeline.
 *   2. FormSubmit — still emails info@frest.lv, so a lead is never lost while the new pipe
 *      is unproven. If (1) fails for any reason, (2) is what saves the enquiry.
 *
 * Attribution is captured once per browser (first touch) and again on every visit (last touch)
 * so a campaign can be measured end to end without any tracking script.
 *
 * The endpoint lives in static/leads-config.js so it can be swapped without touching this file.
 */
(function () {
  'use strict';
  var CFG = window.FREST_LEADS || {};
  var ENDPOINT = CFG.endpoint || '';
  var FORMSUBMIT = CFG.formsubmit || 'https://formsubmit.co/ajax/info@frest.lv';

  // ---- attribution -------------------------------------------------------
  var UTM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term',
                  'gclid', 'fbclid', 'ttclid', 'msclkid'];

  function readParams() {
    var q = {}, sp;
    try { sp = new URLSearchParams(location.search); } catch (e) { return q; }
    UTM_KEYS.forEach(function (k) { var v = sp.get(k); if (v) q[k] = v; });
    return q;
  }

  function store(key, val) { try { localStorage.setItem(key, val); } catch (e) {} }
  function load(key) { try { return localStorage.getItem(key) || ''; } catch (e) { return ''; } }

  var now = readParams();
  var hasNow = Object.keys(now).length > 0;
  var landing = location.pathname + location.search;

  if (hasNow || !load('frest_first')) {
    var first = load('frest_first');
    if (!first) {
      store('frest_first', JSON.stringify({
        at: new Date().toISOString(), landing: landing,
        ref: document.referrer || '', params: now
      }));
    }
  }
  if (hasNow) {
    store('frest_last', JSON.stringify({
      at: new Date().toISOString(), landing: landing,
      ref: document.referrer || '', params: now
    }));
  }

  function attribution() {
    var f = {}, l = {};
    try { f = JSON.parse(load('frest_first') || '{}'); } catch (e) {}
    try { l = JSON.parse(load('frest_last') || '{}'); } catch (e) {}
    var p = (Object.keys(now).length ? now : (l.params || f.params || {}));
    return {
      utm_source: p.utm_source || '',
      utm_medium: p.utm_medium || '',
      utm_campaign: p.utm_campaign || '',
      utm_content: p.utm_content || '',
      utm_term: p.utm_term || '',
      click_id: p.gclid || p.fbclid || p.ttclid || p.msclkid || '',
      first_seen: f.at || '',
      first_landing: f.landing || landing,
      first_referrer: f.ref || document.referrer || '',
      last_referrer: (l.ref || document.referrer || '')
    };
  }

  // ---- submit ------------------------------------------------------------
  function payload(form) {
    var d = {};
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.type === 'submit') return;
      d[el.name] = (el.value || '').trim();
    });
    var a = attribution();
    for (var k in a) d[k] = a[k];
    d.source = form.getAttribute('data-source') || 'site';
    d.page = location.pathname;
    d.page_title = document.title;
    d.lang = document.documentElement.lang || '';
    d.site = location.hostname;
    d.submitted_at = new Date().toISOString();
    d.tz = (Intl.DateTimeFormat().resolvedOptions().timeZone) || '';
    d.user_agent = navigator.userAgent;
    return d;
  }

  function postEndpoint(data) {
    if (!ENDPOINT) return Promise.reject(new Error('no endpoint configured'));
    // text/plain avoids a CORS preflight; Apps Script reads e.postData.contents either way.
    return fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(data)
    }).then(function (r) {
      if (!r.ok) throw new Error('endpoint ' + r.status);
      return r.json().catch(function () { return { ok: true }; });
    });
  }

  function postFormSubmit(data) {
    var body = {
      _subject: 'Frest lead · ' + (data.name || '') + ' · ' + (data.source || ''),
      _template: 'table',
      _captcha: 'false'
    };
    for (var k in data) if (k.charAt(0) !== '_') body[k] = data[k];
    return fetch(FORMSUBMIT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(body)
    });
  }

  function done(form, res) {
    var ok = form.querySelector('.lf-done');
    Array.prototype.forEach.call(form.querySelectorAll('label, button, .lf-fine, .lf-head'), function (el) { el.hidden = true; });
    if (ok) {
      if (res && res.code) {
        var p = document.createElement('p');
        p.className = 'lf-code';
        p.innerHTML = (document.documentElement.lang === 'lv' ? 'Jūsu piekļuves kods: ' : 'Your access code: ') +
                      '<b>' + String(res.code).replace(/[<>&]/g, '') + '</b>';
        ok.appendChild(p);
      }
      ok.hidden = false;
      ok.setAttribute('tabindex', '-1');
      try { ok.focus(); } catch (e) {}
    }
    form.setAttribute('data-sent', '1');
    try {
      window.dispatchEvent(new CustomEvent('frest:lead', { detail: { source: form.getAttribute('data-source') } }));
      if (window.fbq) window.fbq('track', 'Lead');
      if (window.gtag) window.gtag('event', 'generate_lead');
    } catch (e) {}
  }

  function fail(form, msg) {
    var e = form.querySelector('.lf-err');
    if (e) {
      e.textContent = msg;
      e.hidden = false;
    }
  }

  function attach(form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (form.getAttribute('data-sent')) return;
      if ((form.elements['_company'] || {}).value) { done(form, null); return; }  // honeypot
      var btn = form.querySelector('button[type=submit]');
      if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = '…'; }
      var data = payload(form);
      var backup = postFormSubmit(data).catch(function () {});
      postEndpoint(data)
        .then(function (res) { done(form, res); })
        .catch(function () {
          // the endpoint is not live yet, or failed: the FormSubmit copy is the lead
          backup.then(function () { done(form, null); }).catch(function () {
            if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label || 'Send'; }
            fail(form, document.documentElement.lang === 'lv'
              ? 'Neizdevās nosūtīt. Rakstiet uz info@frest.lv vai zvaniet +371 2062 2020.'
              : 'Could not send. Please write to info@frest.lv or call +371 2062 2020.');
          });
        });
    });
  }

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll('form[data-lead]'), attach);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
