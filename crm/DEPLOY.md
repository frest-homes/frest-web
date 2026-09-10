# Lead pipeline — two-minute deploy

Everything below is already written. This is the one part that needs a human signed in as
**info@frest.lv**, because a Google Apps Script can only be deployed by the account that owns it.

Until it is done, nothing is broken: every form on both sites still emails info@frest.lv through
FormSubmit, exactly as before. What is missing until then is the lead row in the sheet, the
automatic catalogue-code reply, and the CRM having anything real to read.

---

## 1. Make the spreadsheet (30 seconds)

1. Signed in as **info@frest.lv**, go to <https://sheets.new>.
2. Rename it **Frest Leads**.

## 2. Paste the script (40 seconds)

3. In that sheet: **Extensions → Apps Script**.
4. Delete whatever is in `Code.gs` and paste the whole of `Code.gs` from this folder.
5. Near the top, change one line:

   ```js
   API_TOKEN: 'CHANGE-ME-frest-crm-2026',
   ```

   to any long random string. Keep a copy — the CRM asks for it once.

6. Save (⌘S / Ctrl-S).
7. Run the function `setup` once (choose it in the toolbar, press **Run**). Google will ask you to
   authorise the script: it needs the spreadsheet and the ability to send mail as info@frest.lv.
   The "Google hasn't verified this app" screen is expected for your own script — **Advanced →
   Go to Frest Leads (unsafe)** is the normal path for a script you wrote yourself.

## 3. Publish it (30 seconds)

8. **Deploy → New deployment → ⚙ → Web app**
   - Description: `frest leads v1`
   - **Execute as: Me (info@frest.lv)**
   - **Who has access: Anyone**
9. **Deploy**, then copy the **Web app URL**. It ends in `/exec`.

## 4. Switch the sites over (one commit)

10. In `frest-homes/frest-web`, edit `static/leads-config.js` and put the URL in:

    ```js
    window.FREST_LEADS = {
      endpoint: 'https://script.google.com/macros/s/AKfy…/exec',
      formsubmit: 'https://formsubmit.co/ajax/info@frest.lv'
    };
    ```

    Commit. Both sites pick it up on the next build — frest.lv builds from the same repo.

11. Open <https://www.frest.lv/modulu-majas/> and send yourself a test lead. Within a minute you
    should have: a row in the sheet, an auto-reply in that inbox, and a notification to info@frest.lv.

## 5. Turn on the CRM

12. Open <https://lab.fresthomes.com/crm/>, go to **Setup**, paste the same `/exec` URL and the
    API token. It stores them in that browser only.

## 6. Optional but worth it

13. In the Apps Script editor: **Triggers → Add trigger → `dailyDigest` → Time-driven → Day timer →
    7am–8am**. You get one mail each morning listing new leads and anything overdue.

---

## What to change later, and where

| Change | File | Line |
|---|---|---|
| The catalogue code the auto-reply sends | `Code.gs` | `CATALOGUE_CODE` |
| The wording of the Latvian auto-reply | `Code.gs` | `lvBody()` |
| The wording of the English auto-reply | `Code.gs` | `enBody()` |
| Who gets the internal notification | `Code.gs` | `NOTIFY` |
| Turning the auto-reply off | `Code.gs` | `SEND_AUTOREPLY: false` |
| Reply templates in the CRM | `crm.html` | `TEMPLATES` |

**Keep `CATALOGUE_CODE` in step with `frest-gates/catalogue/data/codes.json`.** The first code in
that file is the live one; when it rotates, change it here too or the auto-reply hands out a code
that no longer opens the catalogue.

## Limits worth knowing

- A consumer Gmail account sends about 500 mails a day; Workspace about 2,000. Each lead costs two
  (the auto-reply and the notification), so this handles roughly 250 leads a day before it stops.
  A campaign bigger than that needs a real ESB — Brevo and Resend both have free tiers and the
  script can post to them instead.
- `MAX_PER_EMAIL_PER_DAY` (default 5) stops one address flooding the sheet.
- The honeypot field `_company` catches most bots. If spam still gets through, add a
  timing check: reject anything submitted less than three seconds after page load.
