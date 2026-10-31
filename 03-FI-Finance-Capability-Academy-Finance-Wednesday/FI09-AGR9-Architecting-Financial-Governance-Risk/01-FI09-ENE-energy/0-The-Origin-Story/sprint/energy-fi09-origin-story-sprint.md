# The emergency access expired only on the spreadsheet
## FI09 — Architecting Financial Governance Risk

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-FI09-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published educational content, not an enrolled course or certification.

> **Your promise:** In two hours, design one financial-control exception with independent approval, time limits and evidence of closure.

**One story · One Decision Card · Three tabletop tests**

## 1. The decision behind the numbers

An urgent refinery payment issue leads to emergency finance access. The user can amend supplier data and participate in payment processing. The exception register says expired, but the application role remains active.

**Workshop lead:** Hannah Fischer — Director of Enterprise Architecture (OVE-P12).  
**Counterpart:** Omar Haddad — Chief Information Security Officer (OVE-P13).

Omar asks who can exercise the access now. Hannah asks which control objective is at risk, who independently reviewed activity and what proves revocation occurred.

They define a bounded exception with approval, compensating review and a verifiable end condition. A document marked closed is not treated as removal of application access.

**Pause:** Which fact would change your decision? Ask the counterpart one question before proposing a product.

OmniVerse is a fictional energy enterprise with 68,000 employees in 42 countries. Existing OVE-P identities come from the enterprise register. Aditi, Rohan and Amira are explicitly new fictional operational personas with OVE-FI-OS-P identifiers. All new dialogue and incidents are learning designs. Country, entity, accounting basis and approved policy must be established rather than assumed.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Before OmniVerse's fictional 1978 founding, examples describe the wider domain.

- **1970–1989:** Manual approvals and audits rely on signatures and paper custody.
- **1990–1999:** Access registers and spreadsheets record controls; actual permissions can diverge.
- **2000–2009:** ERP roles and workflow enforce some boundaries; cross-system conflicts remain.
- **2010–2019:** GRC and monitoring connect access risks to owners; logs must be reviewed and acted on.
- **2020–2025:** Assisted risk detection prioritizes exceptions; independent assurance and closure evidence remain necessary.

**Mindset:** faster processing is useful when the evidence and decision remain trustworthy. Who bears the cost of an incorrect result: a supplier, worker, customer, investor or community?

## 3. AI-driven horizon, 2026–2050

**2026 starting experiment:** let assistance prepare a low-risk draft, match suggestion or evidence summary. Test its limits before permitting consequential actions.

**2030 checkpoint:** compare the assisted process with a human-led baseline. Require source evidence, approved authority and a usable challenge route.

**2035–2050 scenario:** Imagine a 2050 policy assistant proposing temporary access with narrow delegated limits. It still needs an accountable approver, enforceable expiry and independent review of what happened.

**Alternative:** If automated revocation fails, security/operations need an approved manual containment route and evidence of the final permission state.

These are possibilities and test questions, not forecasts, accounting interpretations or product commitments. Autonomy means bounded assistance under approved authority.

## 4. Smallest useful architecture

**Capability — OVE-FI09-OS-CAP01:** financial control and exception assurance.

**Value stages — OVE-FI09-OS-VS01:** Identify risk → evaluate access → approve bounded exception → monitor → revoke → verify → independently review.

**Objects:** control objective, role/permission, conflict, exception scope, approver, expiry and review evidence.

**Application responsibility:** Business control owners accept business risk; IAM/application owners enforce permissions; security monitors exposure; internal assurance reviews effectiveness. FI09 defines control evidence; FI12 transports events without replacing enforcement.

**Boundary:** A risk score, role label or exception spreadsheet is not proof of effective segregation or revoked access.

The twelve FI themes are a curriculum axis, separate from the twelve architecture streams. SAP Finance is an optional demonstration context; edition, licensing and local requirements remain to validate. Live configuration, posting and payment execution are outside this paper sprint.

## 5. One Decision Card

Use synthetic case **OVE-FI09-OS-SYN001**. Keep the response to one card or screen.

1. **Need:** one business decision, affected population and missing fact.
2. **Evidence:** source IDs, entity, period/effective date, currency or other relevant unit, and approved policy owner.
3. **Ownership:** source application, accountable decision maker and receiving owner.
4. **Gate:** prerequisite, authorized next state and failure/hold condition.
5. **Alternative:** Compare broad emergency access with a time-bound least-privilege exception and independent compensating review.
6. **Recovery:** exception owner, escalation and safe correction/retry.
7. **Proof:** the three actual paper results, measure and stop/revise/proceed decision.

**Requirement — OVE-FI09-OS-REQ01:** retain independent approval, bounded scope/expiry, activity review and verified permission closure.

**Decision — OVE-FI09-OS-ADR01:** record your choice, trade-off and the evidence that would make you change it.

## 6. Three tabletop tests

### T01 — User can alter payee and complete incompatible payment steps

**Expected:** Identify the conflict and enforce approved separation or a documented compensating control.

### T02 — Expiry passes but application role stays active

**Expected:** Escalate, contain and verify actual permission removal before closing.

### T03 — Logs are missing for the exception window

**Expected:** Record an evidence gap, investigate and do not assert control effectiveness.

Record **input → expected → actual paper result → evidence note → revision → retest**. Tests OVE-FI09-OS-T01/T02/T03 support REQ01; expected results are not observed tenant evidence.

**Measure — OVE-FI09-OS-KPI01:** closed exceptions with verified enforcement and review evidence / exceptions reported closed. Name the accountable operational owner, baseline, exclusions and as-of date before setting a target.

**Acceptance:** your card preserves the boundary, names accountable owners, handles all three tests after revisions and supports a 60-second explanation. Unresolved facts remain visible; no achieved financial benefit is claimed.

## 7. Your 120 minutes

- **0–20:** explore the history and explain the enduring problem.
- **20–45:** role-play the lead and counterpart; ask for evidence.
- **45–65:** map responsibilities and consult one resource selectively.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise.
- **115–120:** explain the decision and choose the next experiment.

## 8. Resources and reflection

[SAP Discovering Finance](https://learning.sap.com/learning-journeys/discovering-finance) and [Financial Accounting Overview](https://learning.sap.com/learning-journeys/outlining-the-financial-accounting-overview): select the part relevant to finance controls and auditability. Ask which application owns the fact and which person approves its interpretation. Read selectively within the sprint.

Official resource pages checked 31 October 2026. Resources orient learning; current local authority guidance and qualified policy interpretation are still needed before production design, particularly for tax and reporting.

**Reflect:** What became clearer? Who could your design disadvantage? What evidence would overturn your choice?

**Next Pre-Foundation experiment:** write one control objective and distinguish design evidence from operating-effectiveness evidence.

**Mission:** Architecting Experiences for a Better World.

## Traceability and scope

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Finance blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/03-finance.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Finance academy source](https://app.notion.com/p/0c0a85eaefe145d3bed6c2ea143b6009).

Inherited blueprint anchors: OVE-M02, OVE-M08, OVE-M14, OVE-M20. New namespace OVE-FI09-OS denotes this learning expansion, not previously approved enterprise requirements.

**Trace:** source → OVE-FI09-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 (this experiment) → T01/T02/T03 → KPI01. All shortened IDs carry the same OVE-FI09-OS prefix. EV01 remains an empty evidence slot until a learner records results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA ownership/quality; COBIT control accountability; ISO/IEC 27001 information protection. This is not a compliance certification.

**Publication:** matching manually published learning editions. Original enterprise research and financial hypotheses remain preserved. No unattended synchronization is asserted.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/03-FI-Finance-Capability-Academy-Finance-Wednesday/FI09-AGR9-Architecting-Financial-Governance-Risk/01-FI09-ENE-energy/0-The-Origin-Story/sprint/energy-fi09-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1LtDR3Hb41PKMwi7UsOvIrRoNUjijmRGHyBy63CL4cgA/edit?usp=drivesdk)

[Notion edition](https://app.notion.com/p/40ace6de608981bc82b4c3cc746523c3?pvs=204)
