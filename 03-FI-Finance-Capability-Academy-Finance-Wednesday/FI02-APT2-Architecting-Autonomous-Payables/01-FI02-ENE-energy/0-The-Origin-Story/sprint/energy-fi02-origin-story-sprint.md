# The urgent supplier invoice that nearly got paid twice
## FI02 — Architecting Autonomous Payables

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-FI02-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published educational content, not an enrolled course or certification.

> **Your promise:** In two hours, design one payable-to-payment proposal that validates obligations and prevents duplicate release.

**One story · One Decision Card · Three tabletop tests**

## 1. The decision behind the numbers

A critical refinery maintenance supplier submits an invoice by portal and email. Operations wants immediate payment, but receipt or service-acceptance evidence is incomplete and a bank-detail change has just arrived.

**Workshop lead:** Aditi Sen — Group Financial Controller (OVE-FI-OS-P01, new fictional learning persona).  
**Counterpart:** Wei Zhang — Chief Supply Chain & Procurement Officer (OVE-P11).

Wei worries about maintenance continuity. Aditi asks whether there is one obligation or two, which acceptance check applies, and who independently verified the changed payment details.

The team links duplicate submissions to one business obligation, checks the applicable purchase/receipt or service evidence, and holds an exception for authorized resolution. Urgency does not silently remove the control.

**Pause:** Which fact would change your decision? Ask the counterpart one question before proposing a product.

OmniVerse is a fictional energy enterprise with 68,000 employees in 42 countries. Existing OVE-P identities come from the enterprise register. Aditi, Rohan and Amira are explicitly new fictional operational personas with OVE-FI-OS-P identifiers. All new dialogue and incidents are learning designs. Country, entity, accounting basis and approved policy must be established rather than assumed.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Before OmniVerse's fictional 1978 founding, examples describe the wider domain.

- **1970–1989:** Paper invoice registers connect bills to local approvals and physical evidence.
- **1990–1999:** Scanned documents and spreadsheets improve visibility but can duplicate obligations.
- **2000–2009:** ERP procurement/AP links support matching; exception handling still needs business owners.
- **2010–2019:** Shared services and electronic invoices standardize intake; changes to supplier information remain sensitive.
- **2020–2025:** Assisted capture and matching reduce re-entry; confidence scores cannot approve unsupported payment.

**Mindset:** faster processing is useful when the evidence and decision remain trustworthy. Who bears the cost of an incorrect result: a supplier, worker, customer, investor or community?

## 3. AI-driven horizon, 2026–2050

**2026 starting experiment:** let assistance prepare a low-risk draft, match suggestion or evidence summary. Test its limits before permitting consequential actions.

**2030 checkpoint:** compare the assisted process with a human-led baseline. Require source evidence, approved authority and a usable challenge route.

**2035–2050 scenario:** Imagine a 2050 supplier agent sending a structured invoice and evidence pack. Automation may validate fields quickly, but obligation ownership, verified payee changes and release authority remain necessary.

**Alternative:** If a supplier cannot use a digital portal, support assisted intake with the same obligation and duplicate controls.

These are possibilities and test questions, not forecasts, accounting interpretations or product commitments. Autonomy means bounded assistance under approved authority.

## 4. Smallest useful architecture

**Capability — OVE-FI02-OS-CAP01:** controlled supplier payable processing.

**Value stages — OVE-FI02-OS-VS01:** Receive → identify duplicate → validate obligation → resolve exception → approve proposal → hand off release.

**Objects:** supplier, invoice, business reference, acceptance evidence, exception, payment proposal and payee version.

**Application responsibility:** Procurement owns purchasing context; receiving/service owners confirm acceptance; AP owns supplier liabilities and payment proposals; master-data owners verify supplier changes; treasury/payment authorities own release.

**Boundary:** A scanned invoice, matching score or payment proposal is not bank settlement. FI02 does not override FI05 release controls.

The twelve FI themes are a curriculum axis, separate from the twelve architecture streams. SAP Finance is an optional demonstration context; edition, licensing and local requirements remain to validate. Live configuration, posting and payment execution are outside this paper sprint.

## 5. One Decision Card

Use synthetic case **OVE-FI02-OS-SYN001**. Keep the response to one card or screen.

1. **Need:** one business decision, affected population and missing fact.
2. **Evidence:** source IDs, entity, period/effective date, currency or other relevant unit, and approved policy owner.
3. **Ownership:** source application, accountable decision maker and receiving owner.
4. **Gate:** prerequisite, authorized next state and failure/hold condition.
5. **Alternative:** Compare pay-on-urgency with an exception route that preserves supplier continuity and independent authorization.
6. **Recovery:** exception owner, escalation and safe correction/retry.
7. **Proof:** the three actual paper results, measure and stop/revise/proceed decision.

**Requirement — OVE-FI02-OS-REQ01:** link each proposed payment to one validated liability, verified payee data and approved exception handling.

**Decision — OVE-FI02-OS-ADR01:** record your choice, trade-off and the evidence that would make you change it.

## 6. Three tabletop tests

### T01 — Same invoice arrives twice

**Expected:** Identify the duplicate business obligation and prevent a second payable/payment proposal.

### T02 — Required acceptance evidence is missing

**Expected:** Hold the applicable gate, identify the business owner and use only an authorized exception process.

### T03 — Bank details change before release

**Expected:** Require independent verification and access/approval controls; do not trust an invoice email alone.

Record **input → expected → actual paper result → evidence note → revision → retest**. Tests OVE-FI02-OS-T01/T02/T03 support REQ01; expected results are not observed tenant evidence.

**Measure — OVE-FI02-OS-KPI01:** proposals with complete obligation/payee evidence / proposals reviewed; track duplicate and unresolved exceptions separately. Name the accountable operational owner, baseline, exclusions and as-of date before setting a target.

**Acceptance:** your card preserves the boundary, names accountable owners, handles all three tests after revisions and supports a 60-second explanation. Unresolved facts remain visible; no achieved financial benefit is claimed.

## 7. Your 120 minutes

- **0–20:** explore the history and explain the enduring problem.
- **20–45:** role-play the lead and counterpart; ask for evidence.
- **45–65:** map responsibilities and consult one resource selectively.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise.
- **115–120:** explain the decision and choose the next experiment.

## 8. Resources and reflection

[SAP Discovering Finance](https://learning.sap.com/learning-journeys/discovering-finance) and [Financial Accounting Overview](https://learning.sap.com/learning-journeys/outlining-the-financial-accounting-overview): select the part relevant to payables, procurement handoffs and payment control. Ask which application owns the fact and which person approves its interpretation. Read selectively within the sprint.

Official resource pages checked 31 October 2026. Resources orient learning; current local authority guidance and qualified policy interpretation are still needed before production design, particularly for tax and reporting.

**Reflect:** What became clearer? Who could your design disadvantage? What evidence would overturn your choice?

**Next Pre-Foundation experiment:** define one invoice exception gate and a duplicate-detection acceptance test.

**Mission:** Architecting Experiences for a Better World.

## Traceability and scope

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Finance blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/03-finance.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Finance academy source](https://app.notion.com/p/0c0a85eaefe145d3bed6c2ea143b6009).

Inherited blueprint anchors: OVE-M02, OVE-M08, OVE-M14, OVE-M20. New namespace OVE-FI02-OS denotes this learning expansion, not previously approved enterprise requirements.

**Trace:** source → OVE-FI02-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 (this experiment) → T01/T02/T03 → KPI01. All shortened IDs carry the same OVE-FI02-OS prefix. EV01 remains an empty evidence slot until a learner records results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA ownership/quality; COBIT control accountability; ISO/IEC 27001 information protection. This is not a compliance certification.

**Publication:** matching manually published learning editions. Original enterprise research and financial hypotheses remain preserved. No unattended synchronization is asserted.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/03-FI-Finance-Capability-Academy-Finance-Wednesday/FI02-APT2-Architecting-Autonomous-Payables/01-FI02-ENE-energy/0-The-Origin-Story/sprint/energy-fi02-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1vYLYsT70mNJM7U0QfLM0zZA5clEf45dtf11WtFk2yGc/edit?usp=drivesdk)

[Notion edition](https://app.notion.com/p/40ace6de608981998be9da1c279a8d5b?pvs=204)
