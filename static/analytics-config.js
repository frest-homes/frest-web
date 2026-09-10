/* Analytics configuration — one file to edit per site.
 *
 * Nothing here loads until the visitor accepts analytics in the consent banner. Leave a value
 * empty and that tool is simply never loaded, which is the correct state until a project exists.
 *
 * Microsoft Clarity project IDs come from clarity.microsoft.com → Settings → Overview.
 * They are per-site, so frest.lv and fresthomes.com each need their own; the host decides which
 * one is used, so this same file is correct on both domains and in local preview.
 */
window.FREST_ANALYTICS = {
  clarity: {
    'www.frest.lv':       'yg26q2fm03',
    'frest.lv':           'yg26q2fm03',
    'www.fresthomes.com': 'yg273tmhke',
    'fresthomes.com':     'yg273tmhke'
  }
};
