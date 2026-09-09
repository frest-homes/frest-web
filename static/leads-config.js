/* Lead pipeline configuration.
 *
 * TO GO LIVE: paste the Apps Script web-app URL into `endpoint` below and commit this one file.
 * Nothing else has to change. Until then every lead still arrives by email through FormSubmit,
 * so no enquiry is lost — it just is not written to the Sheet and no auto-reply is sent.
 *
 * The deploy takes about two minutes and is described in crm/DEPLOY.md.
 */
window.FREST_LEADS = {
  endpoint: '',                                             // e.g. https://script.google.com/macros/s/AKfy.../exec
  formsubmit: 'https://formsubmit.co/ajax/info@frest.lv'     // backup copy, always on
};
