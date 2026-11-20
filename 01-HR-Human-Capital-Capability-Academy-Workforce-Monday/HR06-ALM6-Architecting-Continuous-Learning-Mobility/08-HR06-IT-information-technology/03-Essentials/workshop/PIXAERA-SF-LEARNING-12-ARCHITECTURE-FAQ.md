# Pixaera → SAP SuccessFactors Learning — 12 Architecture Streams FAQ

**SuccessLabs Academy · HR06 / ALM6 · Information Technology · Essentials · Workshop**  
**Version:** 1.0 · **Date:** 2026-11-20 · **Status:** reference design / tenant verification required

> **Case framing:** Pixaera conducts instructor-led/classroom modules and proposes a scheduled SFTP completion export into the SAP SuccessFactors Learning History Connector for EngroT. The vendor's two-page proposal is a design input, **not evidence of configuration already deployed**.

## Cross-stream architecture questions

**Q. What is the recommended phase-1 pattern?** Native SuccessFactors Learning History Connector, scheduled after an SFTP delivery, with deterministic upstream mapping and operational reconciliation. Add SAP Cloud Integration only where transformations or enterprise controls justify it.

**Q. Is `STUD_ID = learner email` supported?** Conditionally: `STUD_ID` identifies the **existing LMS User ID**, and an email-formatted value works only when that exact value is the LMS User ID (and meets allowed length/format constraints). Merely storing email in the separate email attribute does **not** establish a lookup.

**Q. What was wrong in the vendor example?** Verify the header `COMPL_DTE` rather than `CMPL_DTE`; do not approve the vendor's spelling or CSV settings without validating against the active tenant's Learning History Connector documentation.

**Q. What remains unconfirmed?** The actual EngroT identity model; tenant connector property defaults; exact file format, file name, header behavior and delimiter; revision and scheduled-offering policies; credit hours; and duplicate behavior. Close these as evidence-backed design decisions.

**Q. How are hours credited?** Prefer configured item credit hours for standardized module duration, and omit optional hours from the import where the tenant's standard behavior supports item-based credit. If actual learner hours vary, model them explicitly and validate the connector handling.

## FAQ by architecture stream

### 01. Enterprise Architecture

**Q1.1. What enterprise capability does the integration enable?**

It connects external immersive classroom learning with the authoritative enterprise learning record, supporting skill visibility, compliance evidence and workforce development.

**Q1.2. Who owns the end-to-end capability?**

The enterprise learning owner is accountable; Pixaera owns source completion capture, HRIS owns identity authority, the LMS owner owns learning records, and integration operations owns transport and reconciliation.

**Q1.3. Which architecture decisions must be formally recorded?**

ADR-001 identity mapping; ADR-002 item versus scheduled offering; ADR-003 transport and integration layer; ADR-004 hours and credit; ADR-005 event replay and duplicate policy; ADR-006 data retention.

### 02. Business Architecture

**Q2.1. What is the business event?**

A Pixaera classroom module is completed and accepted under an agreed attendance/completion policy; the event is subsequently credited in LMS.

**Q2.2. What is the target value stream?**

Register learner → deliver classroom → validate attendance → approve completion → export → import → reconcile → report and remediate.

**Q2.3. Who authorizes completion?**

The learning business owner defines eligibility, thresholds, instructor sign-off if needed and exceptions; Pixaera enforces the agreed rules before export.

### 03. Data Architecture

**Q3.1. Can STUD_ID hold an email address?**

Only when the email-formatted value exactly matches an existing SAP SuccessFactors Learning User ID and meets the field constraints. STUD_ID is not an automatic email lookup; otherwise translate the email to the canonical User ID.

**Q3.2. Which fields are in the proposed interface?**

STUD_ID, CPNT_TYP_ID, CPNT_ID, REV_DTE, CMPL_STAT_ID and COMPL_DTE. Verify required columns, exact spellings, format and revision handling against the tenant-specific connector specification.

**Q3.3. How are duplicate and changing identities managed?**

Use stable LMS User IDs and a separately retained immutable Pixaera completion-event ID; resolve email changes via the authoritative user directory, and define idempotency for repeated deliveries and permissible retakes.

### 04. Application Architecture

**Q4.1. Is an LMS online content object needed?**

No for the proposed item-based history-only approach: create mapped learning items and import completions. A content object is needed only if the LMS itself must launch or deliver content.

**Q4.2. Should we create scheduled offerings?**

Only if EngroT needs session-level administration, instructors, seats, locations or LMS attendance governance. A standalone item-based completion is simpler for phase 1.

**Q4.3. What if the connector cannot perform the required transformations?**

Perform validation and mapping upstream in Pixaera's export process or a governed middleware component; avoid unverified customizations to the standard connector.

### 05. Technology Architecture

**Q5.1. Why batch rather than real-time?**

The proposal specifies daily exports and a scheduled Learning History Connector; this is adequate if the business accepts a daily latency. Real-time is a separate requirement and architecture decision.

**Q5.2. Which environments are required?**

An EngroT test/UAT tenant and production, each with isolated SFTP credentials, input paths, item/status configurations, schedules and reconciliation.

**Q5.3. What should be verified before deployment?**

SFTP route, SSH host-key checking, authentication, file permissions, naming and encoding, batch timing, monitoring, retention and operator support access.

### 06. AI Architecture

**Q6.1. Is AI necessary for this integration?**

No. Deterministic identity mappings, schema validation and a native connector are preferred. AI should not decide whether a learner deserves training credit.

**Q6.2. Where could AI be useful without becoming authoritative?**

Optional anomaly triage, explaining rejected records to support agents and identifying trends in failed imports, with human review.

**Q6.3. What AI controls are appropriate?**

No autonomous alteration of credits, no unrestricted exposure of learner data, human approval for remediation, logging, explainability and quality evaluation.

### 07. Security Architecture

**Q7.1. What are the principal security controls?**

SFTP transport security, verified server host key, managed credentials or keys, least-privilege accounts, restricted inbound directory, file retention controls and auditable access.

**Q7.2. Is learner email personal data?**

Yes; treat it as employee personal information and minimize it where possible. Use internal LMS IDs in destination files if those fulfill the purpose.

**Q7.3. How should authentication secrets be handled?**

Keep private keys and credentials in an approved secrets manager; exchange public keys only and rotate/revoke credentials on change or incident.

### 08. UI–UX Architecture

**Q8.1. What should a learner experience?**

The learner sees an accurate completion, date, training item and credited hours in SuccessFactors learning history without duplicate effort.

**Q8.2. What should an administrator experience?**

A clear exception queue/reconciliation report with reason codes for unknown user, missing item, date error, duplicate, access failure or failed import.

**Q8.3. How are user expectations managed?**

Explain the daily batch latency, potential delays after attendance, and a support channel for missing completions; avoid presenting imported history as an LMS-delivered course.

### 09. Infrastructure Architecture

**Q9.1. Who provisions the file endpoint?**

Confirm the exact SAP-managed SFTP service and directory for each tenant with the responsible SAP/LMS administration and platform teams; do not assume the vendor can create or change SAP hosting.

**Q9.2. How should files be retained?**

Agree encryption, minimum operational retention, archive location, access privileges and deletion schedule in line with EngroT policy.

**Q9.3. What happens when the file service is unavailable?**

Queue source files safely, alert owners, retry within a bounded window and reconcile after recovery without blind duplicate postings.

### 10. Integration Architecture

**Q10.1. What is the canonical sequence?**

Pixaera approved completion → extract → identity and item mapping → schema/format validation → secure SFTP delivery → scheduled Learning History Connector → posted/rejected reconciliation.

**Q10.2. Which header correction is essential?**

The proposal showed CMPL_DTE in one sample; SAP's Learning History field is COMPL_DTE. Also validate whether the tenant accepts a header row and how CSV mode is enabled.

**Q10.3. How is success reconciled?**

For each batch, reconcile source-approved events with successfully posted, rejected and pending records, using source event IDs and connector logs.

### 11. Domain Architecture

**Q11.1. Which HR learning domain entities are relevant?**

Learner, identity, module, item type, item ID, revision, completion, credit hours, status, learning history, assignment and optionally scheduled offering.

**Q11.2. How do competencies and mobility relate?**

History credit becomes evidence for learning and mobility workflows, but skill inference, competency attainment and eligibility for roles require distinct governed rules.

**Q11.3. Does a successful import satisfy mandatory training?**

Only if the relevant assignment, curriculum, compliance and retraining rules in the tenant recognize the imported item/status/hours as satisfying the requirement. Test end to end.

### 12. Industry Architecture

**Q12.1. How does this relate to an IT-sector workshop?**

Use the integration as an applied HR06 learning-and-mobility technology case for an IT-sector enterprise while keeping the same core architecture portable to other industries.

**Q12.2. What sector-specific overlays may apply?**

Information-security training, technical skill certification, contractor access, audit trails and regulatory/customer requirements may change the controls, not the base connector semantics.

**Q12.3. Can the pattern be reused across the 11 GICS sectors?**

Yes as a reference pattern; each sector must validate identity sources, compliance rules, training duration, residency, security and reporting before reuse.

## Workshop review questions

1. Draw an L1 system context and an L2 integration flow, separating Pixaera, identity master, SFTP, connector and LMS.
2. Trace one classroom completion from QR attendance through learning-history credit and management reporting.
3. Compare Pixaera email against `STUD_ID` in three tenant user profiles; record evidence, no real email addresses.
4. Describe failed/duplicate event handling without claiming SAP automatically deduplicates every reimport.
5. Explain how the same pattern changes if LMS scheduled offerings are mandatory.
6. For each architecture stream, record a design decision, risk, owner, test and evidence.

## Evidence register

| Topic | Evidence required | Sign-off |
|---|---|---|
| Learner ID | Redacted LMS User ID versus Email field comparison | HRIS/LMS |
| Course mapping | Item type, item ID, item revision, active status | Learning Admin |
| Credits | Item credit values and posting result | Learning Business |
| SFTP | Endpoint, account, access and SSH controls (no secrets in repo) | Security/Basis |
| Parsing | Actual connector properties and sample processed file | LMS Technical |
| Audit | Source event ID, import totals, rejected-record queue | Integration Ops |
| Acceptance | SIT/UAT records and CAB approval | Business/Change |

## References

- SAP Help: [Learning History Connector technical documentation](https://help.sap.com/doc/f04490ba96cc4de3a59cf34f3a9d0c46/2405/en-US/SF_LRN_Learning_History_Connector.pdf) — verify applicable release and current tenant configuration.
- Vendor input: Pixaera's *Sending Pixaera completions to SAP SuccessFactors* (Engro, November 2026), supplied as screenshots in the architecture workshop.

**Boundary:** These answers are design guidance. Never treat tenant-specific assumptions as confirmed implementation facts.
