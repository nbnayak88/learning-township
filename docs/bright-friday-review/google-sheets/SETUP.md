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


## Single submission and duplicate checks
Use the latest Code.gs in the existing Apps Script project. Keep TAGMANGO_API_KEY private in Script Properties. The read APIs use Bearer authentication; if the integration key lacks read permission, set TAGMANGO_READ_API_KEY to the account's external API key. TAGMANGO_HOST defaults to hub.successlabsacademy.com.

Before creating any registration row or enrollment, the handler holds a script lock and checks normalized email OR international phone against Registrations, TagMango subscribers (all states), the selected free service, and free leads. Exact matches block the new registration. The same request ID can retrieve its existing result without appending or enrolling again. Lookup failures or incomplete pagination stop the request.

Coverage caveat: TagMango's subscriber API omits public products unless their IDs are explicit. Set TAGMANGO_PUBLIC_MANGO_IDS to a JSON array containing any additional public service IDs that must be covered, for example ["0123456789abcdef01234567"]. The selected Bright Friday service is always included. Other creators' customers are outside this host's visibility. Duplicate checks cannot be atomic with registrations made concurrently outside this Apps Script; TagMango must enforce its own identity uniqueness too.

Do not redeploy a second independent project for writes: retire old endpoints and use one Apps Script project, so its lock serializes submissions. Unconfirmed writes are marked Needs review and are not automatically retried. Existing saved registrations require administrator reconciliation, not repeated audience submission.

Redeploy: Deploy > Manage deployments > Edit > New version > Deploy. This repository update does not update the running Apps Script automatically. Validate read API permissions and one authorized real enrollment before announcing the integration as live. A successful enrollment is an API operation; no second checkout form is needed. Signing into the TagMango account can still require TagMango authentication.
