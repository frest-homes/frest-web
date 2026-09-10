/* Lead pipeline configuration.
 *
 * The endpoint is live as of 10 Sep 2026: a Google Apps Script web app owned by info@frest.lv,
 * bound to the "CRM Frest" Leads spreadsheet. It writes the lead row, sends the catalogue
 * auto-reply and notifies info@frest.lv. The CRM at lab.fresthomes.com/crm/ reads back through
 * the same URL with the API token.
 *
 * FormSubmit stays on as a second copy of every lead. That matters more than it looks: some
 * networks cannot resolve formsubmit.co at all, and some cannot reach Google — with both paths
 * a lead has to lose twice to be lost.
 *
 * To repoint at a new deployment, replace the URL below and commit this one file; both sites
 * pick it up on their next build. The deploy steps are in crm/DEPLOY.md.
 */
window.FREST_LEADS = {
  endpoint: 'https://script.google.com/macros/s/AKfycbzkzsSMHIJ5-1A4Cwuu8TAdlTlY41oobzQc6SJIBY-31TfmLczUQRHDVdgr6aWKwZWL/exec',
  formsubmit: 'https://formsubmit.co/ajax/info@frest.lv'     // backup copy, always on
};
