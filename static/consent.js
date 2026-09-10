/* Consent — GDPR/ePrivacy gate for everything that is not strictly necessary.
 *
 * Two categories only, because we only have two:
 *
 *   necessary  the enquiry forms themselves, and the "remember what I typed" prefill. A person
 *              who submits a form asked for that; it needs no consent.
 *   analytics  Microsoft Clarity, AND the first-touch/last-touch campaign attribution that
 *              leads.js keeps in localStorage. Attribution is marketing, not a service the
 *              visitor asked for, so it needs consent just as much as the recording does.
 *
 * Rules this implements, all of which are requirements rather than niceties:
 *   · nothing is loaded or stored before an explicit yes — no pre-ticked anything
 *   · refusing is exactly as easy as accepting (two identical buttons, no dark pattern)
 *   · the choice can be withdrawn later, from the footer link on every page
 *   · Global Privacy Control and Do Not Track are honoured as a refusal, without nagging
 *   · the stored choice carries a version, so changing what we collect re-asks properly
 */
(function () {
  'use strict';
  var KEY = 'frest_consent', VERSION = 1;
  var CFG = (window.FREST_ANALYTICS || {});
  var LV = (document.documentElement.lang || 'lv') === 'lv';
  var T = function (lv, en) { return LV ? lv : en; };

  function read() {
    try { var v = JSON.parse(localStorage.getItem(KEY) || 'null'); return (v && v.v === VERSION) ? v : null; }
    catch (e) { return null; }
  }
  function write(granted) {
    try { localStorage.setItem(KEY, JSON.stringify({ v: VERSION, analytics: !!granted, at: new Date().toISOString() })); }
    catch (e) {}
  }
  function signalledRefusal() {
    return navigator.globalPrivacyControl === true || navigator.doNotTrack === '1' || window.doNotTrack === '1';
  }

  function clarityId() {
    var m = CFG.clarity;
    if (!m) return '';
    if (typeof m === 'string') return m;
    return m[location.hostname] || m[location.hostname.replace(/^www\./, '')] || '';
  }

  function startClarity() {
    var id = clarityId();
    if (!id || window.clarity) return;
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', id);
  }

  function grant() {
    document.documentElement.setAttribute('data-consent', 'analytics');
    startClarity();
  }
  function revoke() {
    document.documentElement.removeAttribute('data-consent');
    // Anything already stored under the analytics category goes now, not at some later cleanup.
    ['frest_first', 'frest_last'].forEach(function (k) { try { localStorage.removeItem(k); } catch (e) {} });
  }

  var el = null;
  function close() { if (el) { el.remove(); el = null; } }

  function banner(isChange) {
    close();
    el = document.createElement('div');
    el.className = 'consent';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', T('Sīkdatņu izvēle', 'Cookie choice'));
    el.innerHTML =
      '<p class="consent-t">' + T('Vai drīkstam skatīties, kā lietojat vietni?', 'May we look at how you use the site?') + '</p>' +
      '<p class="consent-b">' + T(
        'Mēs izmantotu Microsoft Clarity, lai redzētu, cik tālu lapas tiek ritinātas un kur cilvēki uzklikšķina, un atcerētos, no kuras reklāmas jūs atnācāt. Formās ievadītais — vārds, e-pasts, tālrunis — netiek ierakstīts. Bez piekrišanas vietne strādā tieši tāpat.',
        'We would use Microsoft Clarity to see how far pages are scrolled and where people click, and remember which campaign brought you here. What you type into a form — name, email, phone — is never recorded. Decline and the site works exactly the same.'
      ) + '</p>' +
      '<div class="consent-row">' +
        '<button type="button" data-consent-yes>' + T('Piekrītu', 'Accept') + '</button>' +
        '<button type="button" data-consent-no>' + T('Nepiekrītu', 'Decline') + '</button>' +
      '</div>' +
      '<p class="consent-f"><a href="' + (window.FREST_PRIVACY_URL || '/privatuma-politika/') + '">' +
        T('Privātuma politika', 'Privacy policy') + '</a></p>';
    document.body.appendChild(el);
    el.querySelector('[data-consent-yes]').addEventListener('click', function () { write(true); grant(); close(); });
    el.querySelector('[data-consent-no]').addEventListener('click', function () { write(false); revoke(); close(); });
    requestAnimationFrame(function () { el.classList.add('in'); });
    if (isChange) el.querySelector('[data-consent-yes]').focus();
  }

  function init() {
    var s = read();
    if (s) { if (s.analytics) grant(); return; }          // already decided
    if (signalledRefusal()) { write(false); return; }      // browser already said no; do not nag
    banner(false);
  }

  window.frestConsent = {
    analytics: function () { var s = read(); return !!(s && s.analytics); },
    open: function () { banner(true); },
    state: read
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
