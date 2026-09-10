/**
 * Frest lead pipeline — Google Apps Script web app.
 *
 * One script does four jobs:
 *   1. receives every form submission from frest.lv and fresthomes.com (doPost)
 *   2. writes it as a row in the Leads sheet, with full campaign attribution
 *   3. sends the person an auto-reply containing the catalogue code
 *   4. serves the lead list back to the CRM on lab.fresthomes.com (doGet, token-protected)
 *
 * Deploy: Extensions > Apps Script from the Leads spreadsheet, paste this file,
 * then Deploy > New deployment > Web app > Execute as: Me > Who has access: Anyone.
 * Copy the /exec URL into static/leads-config.js on both sites. See DEPLOY.md.
 *
 * Nothing here is secret except API_TOKEN, which only gates reading the lead list.
 */

// ======================= CONFIG =======================
var CONFIG = {
  SHEET_ID: '',                       // leave empty when the script is bound to the spreadsheet
  SHEET_LEADS: 'Leads',
  SHEET_LOG: 'Log',

  // Catalogue gate. Keep in step with frest-gates/catalogue/data/codes.json — the first code there
  // is the one the auto-reply hands out.
  CATALOGUE_URL: 'https://catalogue.fresthomes.com',
  CATALOGUE_CODE: 'ritausma-koks-862',
  CATALOGUE_CODE_VALID: '60 days',

  NOTIFY: 'info@frest.lv',            // internal notification of every new lead
  FROM_NAME: 'Frest Homes',
  REPLY_TO: 'info@frest.lv',

  // Read token for the CRM. CHANGE THIS before you use the CRM, and paste the same
  // value into the CRM page. It only protects reading; it cannot write anything.
  API_TOKEN: 'CHANGE-ME-frest-crm-2026',

  MAX_PER_EMAIL_PER_DAY: 5,           // simple abuse brake
  SEND_AUTOREPLY: true
};

var HEADERS = [
  'id', 'received_at', 'status', 'owner', 'next_action', 'next_action_at', 'notes',
  'name', 'email', 'phone', 'region', 'timing', 'stage_of_project',
  'lang', 'site', 'source', 'page', 'page_title',
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'click_id',
  'first_seen', 'first_landing', 'first_referrer', 'last_referrer',
  'catalogue_code', 'autoreply_sent', 'tz', 'user_agent', 'raw'
];

// ======================= ENTRY POINTS =======================
function doPost(e) {
  try {
    var data = parseBody(e);
    if (!data) return json({ ok: false, error: 'no body' });

    // honeypot: silently accept and drop
    if (data._company) return json({ ok: true, dropped: true });

    var email = String(data.email || '').trim().toLowerCase();
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(email)) return json({ ok: false, error: 'bad email' });

    var ss = book();
    var sheet = leadSheet(ss);

    if (countToday(sheet, email) >= CONFIG.MAX_PER_EMAIL_PER_DAY) {
      return json({ ok: true, throttled: true, code: CONFIG.CATALOGUE_CODE, url: CONFIG.CATALOGUE_URL });
    }

    var id = 'L' + Utilities.formatDate(new Date(), 'Europe/Riga', 'yyMMdd-HHmmss') +
             '-' + Math.random().toString(36).slice(2, 6);
    var row = {
      id: id,
      received_at: new Date(),
      status: 'New',
      owner: '',
      next_action: 'First contact',
      next_action_at: addDays(new Date(), 1),
      notes: '',
      name: clip(data.name, 120),
      email: email,
      phone: clip(data.phone, 40),
      region: clip(data.region, 60),
      timing: clip(data.timing, 40),
      stage_of_project: clip(data.stage, 80),
      lang: clip(data.lang, 8),
      site: clip(data.site, 80),
      source: clip(data.source, 60),
      page: clip(data.page, 200),
      page_title: clip(data.page_title, 200),
      utm_source: clip(data.utm_source, 60),
      utm_medium: clip(data.utm_medium, 60),
      utm_campaign: clip(data.utm_campaign, 80),
      utm_content: clip(data.utm_content, 80),
      utm_term: clip(data.utm_term, 80),
      click_id: clip(data.click_id, 200),
      first_seen: clip(data.first_seen, 40),
      first_landing: clip(data.first_landing, 200),
      first_referrer: clip(data.first_referrer, 200),
      last_referrer: clip(data.last_referrer, 200),
      catalogue_code: CONFIG.CATALOGUE_CODE,
      autoreply_sent: '',
      tz: clip(data.tz, 60),
      user_agent: clip(data.user_agent, 300),
      raw: JSON.stringify(data).slice(0, 4000)
    };

    var sent = '';
    if (CONFIG.SEND_AUTOREPLY) {
      try { sendAutoReply(row); sent = new Date(); } catch (err) { sent = 'ERROR: ' + err; }
    }
    row.autoreply_sent = sent;

    sheet.appendRow(HEADERS.map(function (h) { return row[h]; }));
    try { notifyTeam(row); } catch (err) {}

    return json({ ok: true, id: id, code: CONFIG.CATALOGUE_CODE, url: CONFIG.CATALOGUE_URL });
  } catch (err) {
    try { log('doPost', String(err)); } catch (e2) {}
    return json({ ok: false, error: String(err) });
  }
}

function doGet(e) {
  var p = (e && e.parameter) || {};
  if (p.ping) return json({ ok: true, service: 'frest-leads', time: new Date().toISOString() });
  if (p.token !== CONFIG.API_TOKEN) return json({ ok: false, error: 'unauthorised' });

  if (p.action === 'update' && p.id && p.field) {
    return json(updateLead(p.id, p.field, p.value || ''));
  }
  // default: list
  var sheet = leadSheet(book());
  var values = sheet.getDataRange().getValues();
  var head = values.shift();
  var out = values.map(function (r) {
    var o = {};
    head.forEach(function (h, i) {
      var v = r[i];
      o[h] = (v instanceof Date) ? v.toISOString() : v;
    });
    return o;
  }).filter(function (o) { return o.id; });
  return json({ ok: true, count: out.length, leads: out });
}

// ======================= EMAIL =======================
function sendAutoReply(row) {
  var lv = (row.lang || 'lv').indexOf('lv') === 0;
  var subject = lv ? 'Frest katalogs ar cenām — jūsu piekļuves kods'
                   : 'Frest catalogue with prices — your access code';
  var body = lv ? lvBody(row) : enBody(row);
  MailApp.sendEmail({
    to: row.email,
    subject: subject,
    body: body.text,
    htmlBody: body.html,
    name: CONFIG.FROM_NAME,
    replyTo: CONFIG.REPLY_TO
  });
}

function lvBody(row) {
  var name = (row.name || '').split(' ')[0];
  var text =
    'Sveiki' + (name ? ', ' + name : '') + '!\n\n' +
    'Paldies par interesi par Frest mājām. Katalogs ar cenām ir šeit:\n\n' +
    CONFIG.CATALOGUE_URL + '\n' +
    'Jūsu kods: ' + CONFIG.CATALOGUE_CODE + '\n\n' +
    'Katalogā atradīsiet visus četrus modeļus — Als 70, Als 110, Aura 70 un Aura 110 — ar pilno ' +
    'komplektāciju, cenu katrai izvēlei un konfiguratoru, kas rēķina summu.\n\n' +
    'Divas lietas, ko der zināt jau tagad:\n' +
    '· Rūpnīcas komplekts ar montāžu sākas 92 000 € ar PVN. Tajā ir siltinātas sienas, jumts, logi, ' +
    'ārdurvis, fasāde un montāža objektā.\n' +
    '· Pamati, zeme, pieslēgumi un būvatļauja nav iekļauti nevienā paketē — tos rēķinām atsevišķi ' +
    'pēc jūsu zemesgabala.\n\n' +
    'Ja gribat konkrētu skaitli savai situācijai, atbildiet uz šo vēstuli un pastāstiet, kur būvēsiet ' +
    'un kad. Atbildam vienas darba dienas laikā.\n\n' +
    'Jānis Bērziņš\nFrest Homes · SIA Frest\ninfo@frest.lv · +371 2062 2020\nwww.frest.lv';
  return { text: text, html: html(text, 'lv') };
}

function enBody(row) {
  var name = (row.name || '').split(' ')[0];
  var text =
    'Hello' + (name ? ' ' + name : '') + ',\n\n' +
    'Thank you for your interest in Frest. The catalogue with prices is here:\n\n' +
    CONFIG.CATALOGUE_URL + '\n' +
    'Your code: ' + CONFIG.CATALOGUE_CODE + '\n\n' +
    'A note before you open it: the catalogue is written for the Latvian market and its prices are ' +
    'Latvian, including 21% VAT. The model specifications, drawings and the configurator all apply ' +
    'to an Irish project; the delivered price for Ireland differs because of transport and because ' +
    'we supply and erect the kit only.\n\n' +
    'What that means in practice:\n' +
    '· We manufacture the insulated timber frame in Latvia and erect it on your prepared foundation.\n' +
    '· Foundation, services, internal fit-out, BER assessment and certification stay with your ' +
    'Irish team. We supply the structural calculations, U-values, setting-out and tolerances they need.\n' +
    '· The Als 110 kit, supplied and erected, is EUR 128,000 including VAT for 103.3 m2.\n\n' +
    'If you tell me the county, the site status and roughly when you want to build, I will come back ' +
    'with a delivered figure for your project within one working day.\n\n' +
    'Janis Berzins\nFrest Homes · SIA Frest, Riga, Latvia\ninfo@frest.lv · +371 2062 2020\n' +
    'www.fresthomes.com';
  return { text: text, html: html(text, 'en') };
}

function html(text, lang) {
  var esc = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  var body = esc.split('\n\n').map(function (p) {
    return '<p style="margin:0 0 16px">' + p.replace(/\n/g, '<br>') + '</p>';
  }).join('');
  body = body.replace(CONFIG.CATALOGUE_URL,
    '<a href="' + CONFIG.CATALOGUE_URL + '" style="color:#0a7a88;font-weight:600">' + CONFIG.CATALOGUE_URL + '</a>');
  body = body.replace(CONFIG.CATALOGUE_CODE,
    '<b style="background:#fdf7e7;padding:2px 8px;border-radius:6px;border:1px dashed #50d1e0">' + CONFIG.CATALOGUE_CODE + '</b>');
  return '<div style="font:15px/1.65 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#0c2429;max-width:620px">' +
         body +
         '<hr style="border:0;border-top:1px solid #e3ecee;margin:26px 0 14px">' +
         '<p style="font-size:12px;color:#6b8085;margin:0">' +
         (lang === 'lv'
           ? 'Jūs saņemat šo vēstuli, jo pieprasījāt Frest katalogu. Datus izmantojam tikai, lai atbildētu uz jūsu pieprasījumu.'
           : 'You are receiving this because you requested the Frest catalogue. We use your details only to answer your enquiry.') +
         '</p></div>';
}

function notifyTeam(row) {
  if (!CONFIG.NOTIFY) return;
  var lines = ['New lead: ' + row.name + ' <' + row.email + '>', ''];
  ['phone', 'region', 'timing', 'stage_of_project', 'lang', 'site', 'source',
   'utm_source', 'utm_medium', 'utm_campaign', 'first_landing', 'first_referrer'].forEach(function (k) {
    if (row[k]) lines.push(k + ': ' + row[k]);
  });
  lines.push('', 'id: ' + row.id);
  MailApp.sendEmail({
    to: CONFIG.NOTIFY,
    subject: '🏠 Frest lead · ' + (row.name || row.email) + ' · ' + (row.utm_campaign || row.source || ''),
    body: lines.join('\n'),
    name: CONFIG.FROM_NAME,
    replyTo: row.email
  });
}

// ======================= SHEET =======================
function book() {
  return CONFIG.SHEET_ID ? SpreadsheetApp.openById(CONFIG.SHEET_ID) : SpreadsheetApp.getActiveSpreadsheet();
}

function leadSheet(ss) {
  var sheet = ss.getSheetByName(CONFIG.SHEET_LEADS);
  if (!sheet) {
    sheet = ss.insertSheet(CONFIG.SHEET_LEADS);
  }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold').setBackground('#e8f1f3');
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(1, 130);
  }
  return sheet;
}

function countToday(sheet, email) {
  var last = sheet.getLastRow();
  if (last < 2) return 0;
  var n = Math.min(300, last - 1);
  var rows = sheet.getRange(last - n + 1, 1, n, HEADERS.length).getValues();
  var ei = HEADERS.indexOf('email'), ti = HEADERS.indexOf('received_at');
  var since = new Date().getTime() - 24 * 3600 * 1000;
  var c = 0;
  rows.forEach(function (r) {
    if (String(r[ei]).toLowerCase() === email && new Date(r[ti]).getTime() > since) c++;
  });
  return c;
}

function updateLead(id, field, value) {
  var i = HEADERS.indexOf(field);
  if (i < 0) return { ok: false, error: 'unknown field' };
  if (['id', 'received_at', 'email', 'raw'].indexOf(field) >= 0) return { ok: false, error: 'read-only field' };
  var sheet = leadSheet(book());
  var ids = sheet.getRange(1, 1, sheet.getLastRow(), 1).getValues();
  for (var r = 1; r < ids.length; r++) {
    if (String(ids[r][0]) === String(id)) {
      sheet.getRange(r + 1, i + 1).setValue(value);
      return { ok: true, id: id, field: field, value: value };
    }
  }
  return { ok: false, error: 'not found' };
}

function log(what, detail) {
  var ss = book();
  var s = ss.getSheetByName(CONFIG.SHEET_LOG) || ss.insertSheet(CONFIG.SHEET_LOG);
  s.appendRow([new Date(), what, detail]);
}

// ======================= UTIL =======================
function parseBody(e) {
  if (!e) return null;
  if (e.postData && e.postData.contents) {
    try { return JSON.parse(e.postData.contents); } catch (err) {}
  }
  if (e.parameter && Object.keys(e.parameter).length) return e.parameter;
  return null;
}
function clip(v, n) { return String(v == null ? '' : v).slice(0, n); }
function addDays(d, n) { var x = new Date(d); x.setDate(x.getDate() + n); return x; }
function json(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

// ======================= ONE-OFF SETUP =======================
/** Run once from the editor: creates the Leads sheet with headers and a sample row. */
function setup() {
  var sheet = leadSheet(book());
  Logger.log('Leads sheet ready with ' + HEADERS.length + ' columns.');
  Logger.log('Now: Deploy > New deployment > Web app > Execute as Me > Anyone.');
  return sheet.getName();
}

/** Run once to check the auto-reply renders correctly. Sends to CONFIG.NOTIFY. */
function testAutoReply() {
  sendAutoReply({ name: 'Test Person', email: CONFIG.NOTIFY, lang: 'lv' });
  sendAutoReply({ name: 'Test Person', email: CONFIG.NOTIFY, lang: 'en' });
}

/**
 * Daily digest of leads that need action. Add a time-driven trigger for this
 * (Triggers > Add trigger > dailyDigest > Time-driven > Day timer > 7am-8am).
 */
function dailyDigest() {
  var sheet = leadSheet(book());
  if (sheet.getLastRow() < 2) return;
  var rows = sheet.getRange(2, 1, sheet.getLastRow() - 1, HEADERS.length).getValues();
  var si = HEADERS.indexOf('status'), ni = HEADERS.indexOf('name'), ei = HEADERS.indexOf('email');
  var ai = HEADERS.indexOf('next_action_at'), ci = HEADERS.indexOf('utm_campaign'), ri = HEADERS.indexOf('received_at');
  var today = new Date(); today.setHours(23, 59, 59);
  var due = [], fresh = [];
  rows.forEach(function (r) {
    if (['Won', 'Lost'].indexOf(String(r[si])) >= 0) return;
    if (r[ai] && new Date(r[ai]) <= today) due.push(r);
    if (new Date(r[ri]).getTime() > new Date().getTime() - 24 * 3600 * 1000) fresh.push(r);
  });
  if (!due.length && !fresh.length) return;
  var line = function (r) { return '· ' + r[ni] + ' <' + r[ei] + '> — ' + r[si] + (r[ci] ? ' — ' + r[ci] : ''); };
  var body = '';
  if (fresh.length) body += 'New in the last 24 hours (' + fresh.length + '):\n' + fresh.map(line).join('\n') + '\n\n';
  if (due.length) body += 'Due or overdue (' + due.length + '):\n' + due.map(line).join('\n') + '\n\n';
  body += 'CRM: https://lab.fresthomes.com/crm/';
  MailApp.sendEmail({ to: CONFIG.NOTIFY, subject: 'Frest leads — ' + due.length + ' due, ' + fresh.length + ' new', body: body, name: CONFIG.FROM_NAME });
}
