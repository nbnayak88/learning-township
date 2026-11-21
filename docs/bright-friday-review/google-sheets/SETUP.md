# Activate Bright Friday registration

1. Open the registration Google Sheet: https://docs.google.com/spreadsheets/d/18ljeRvypL0xDHYTleFeegiogrSUKL-XU4mOTW54-dcw/edit
2. Choose Extensions → Apps Script.
3. Replace Code.gs with the complete Code.gs in this folder and save.
4. Deploy → New deployment → Web app.
5. Execute as: Me. Who has access: Anyone (if permitted by your account).
6. Deploy and authorize with the account that owns the sheet.
7. Copy the deployment URL ending in /exec and send it to ChatGPT. No passwords or tokens needed.
8. ChatGPT will set registration-config.json and verify an authorized test submission.

The website form stays disabled until the endpoint is configured. The spreadsheet stays private. Submissions log preferences for review, not seat reservations or membership grants. The sector is saved separately from the original seat reference.

Reference: https://developers.google.com/apps-script/guides/web
