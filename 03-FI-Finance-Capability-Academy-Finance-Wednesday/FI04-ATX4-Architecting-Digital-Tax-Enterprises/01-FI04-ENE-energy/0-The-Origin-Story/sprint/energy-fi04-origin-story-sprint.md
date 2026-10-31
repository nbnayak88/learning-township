# The tax file was sent; nobody knew whether it was accepted
## FI04 — Architecting Digital Tax Enterprises

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-FI04-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published educational content, not an enrolled course or certification.

> **Your promise:** In two hours, design one traceable tax-document flow that distinguishes determination, submission, acknowledgment and correction.

**One story · One Decision Card · Three tabletop tests**

## 1. The decision behind the numbers

An OmniVerse entity sends a synthetic tax document through a reporting service. The transport log says delivered, but the authority response rejects a field. A dashboard still calls the obligation complete.

**Workshop lead:** Amira Saleh — Group Tax Controls Lead (OVE-FI-OS-P03, new fictional learning persona).  
**Counterpart:** Aditi Sen — Group Financial Controller (OVE-FI-OS-P01, new fictional learning persona).

Amira asks which entity, jurisdiction, document type and rule version apply. Aditi asks whether the ledger, submission and acknowledgment can be traced without silently editing the original.

They record the applicable rule source, separate technical delivery from the required authority outcome, and design a versioned correction route. Country-specific requirements are questions for the accountable tax owner.

**Pause:** Which fact would change your decision? Ask the counterpart one question before proposing a product.

OmniVerse is a fictional energy enterprise with 68,000 employees in 42 countries. Existing OVE-P identities come from the enterprise register. Aditi, Rohan and Amira are explicitly new fictional operational personas with OVE-FI-OS-P identifiers. All new dialogue and incidents are learning designs. Country, entity, accounting basis and approved policy must be established rather than assumed.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Before OmniVerse's fictional 1978 founding, examples describe the wider domain.

- **1970–1989:** Paper tax books and forms require manual classification and reconciliations.
- **1990–1999:** Tax tables and spreadsheets automate calculations; rule versions and evidence can diverge.
- **2000–2009:** ERP tax determination links transactions; local obligations still vary.
- **2010–2019:** Digital reporting and e-document services connect businesses and authorities; rejection handling matters.
- **2020–2025:** Assisted validation spots anomalies; current rules and authority evidence still require accountable review.

**Mindset:** faster processing is useful when the evidence and decision remain trustworthy. Who bears the cost of an incorrect result: a supplier, worker, customer, investor or community?

## 3. AI-driven horizon, 2026–2050

**2026 starting experiment:** let assistance prepare a low-risk draft, match suggestion or evidence summary. Test its limits before permitting consequential actions.

**2030 checkpoint:** compare the assisted process with a human-led baseline. Require source evidence, approved authority and a usable challenge route.

**2035–2050 scenario:** Imagine a 2050 reporting assistant preparing evidence packages across jurisdictions. It must not invent legal interpretations or treat a technical receipt as compliance approval.

**Alternative:** If the authority endpoint is unavailable, an approved contingency procedure must preserve evidence and deadlines without falsely recording acceptance.

These are possibilities and test questions, not forecasts, accounting interpretations or product commitments. Autonomy means bounded assistance under approved authority.

## 4. Smallest useful architecture

**Capability — OVE-FI04-OS-CAP01:** auditable tax-document lifecycle.

**Value stages — OVE-FI04-OS-VS01:** Determine scope → validate data → approve → submit → interpret outcome → correct → reconcile.

**Objects:** entity, jurisdiction, document type/version, tax-rule source, submission ID, acknowledgment and correction link.

**Application responsibility:** Tax owners approve obligation/rule interpretations; source applications own transactions; reporting services manage submissions; authorities issue their defined responses; Finance reconciles resulting records.

**Boundary:** Not every jurisdiction uses clearance or the same statuses. Required completion criteria must come from that jurisdiction's official guidance and approved design.

The twelve FI themes are a curriculum axis, separate from the twelve architecture streams. SAP Finance is an optional demonstration context; edition, licensing and local requirements remain to validate. Live configuration, posting and payment execution are outside this paper sprint.

## 5. One Decision Card

Use synthetic case **OVE-FI04-OS-SYN001**. Keep the response to one card or screen.

1. **Need:** one business decision, affected population and missing fact.
2. **Evidence:** source IDs, entity, period/effective date, currency or other relevant unit, and approved policy owner.
3. **Ownership:** source application, accountable decision maker and receiving owner.
4. **Gate:** prerequisite, authorized next state and failure/hold condition.
5. **Alternative:** Compare sent-equals-complete with obligation-specific outcome tracking and linked corrections.
6. **Recovery:** exception owner, escalation and safe correction/retry.
7. **Proof:** the three actual paper results, measure and stop/revise/proceed decision.

**Requirement — OVE-FI04-OS-REQ01:** retain the applicable rule source and distinguish submitted, rejected and accepted/otherwise-completed states as defined for the obligation.

**Decision — OVE-FI04-OS-ADR01:** record your choice, trade-off and the evidence that would make you change it.

## 6. Three tabletop tests

### T01 — Transport succeeds but required authority validation rejects

**Expected:** Keep the obligation incomplete, capture rejection evidence and assign a correction owner.

### T02 — Rule version or jurisdiction is unclear

**Expected:** Hold unsupported determination and obtain the official rule and accountable interpretation.

### T03 — Correction request retries

**Expected:** Preserve the original/correction link and prevent unintended duplicate submissions.

Record **input → expected → actual paper result → evidence note → revision → retest**. Tests OVE-FI04-OS-T01/T02/T03 support REQ01; expected results are not observed tenant evidence.

**Measure — OVE-FI04-OS-KPI01:** documents with the required verified outcome / in-scope documents due; report rejected/pending aging and exclusions. Name the accountable operational owner, baseline, exclusions and as-of date before setting a target.

**Acceptance:** your card preserves the boundary, names accountable owners, handles all three tests after revisions and supports a 60-second explanation. Unresolved facts remain visible; no achieved financial benefit is claimed.

## 7. Your 120 minutes

- **0–20:** explore the history and explain the enduring problem.
- **20–45:** role-play the lead and counterpart; ask for evidence.
- **45–65:** map responsibilities and consult one resource selectively.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise.
- **115–120:** explain the decision and choose the next experiment.

## 8. Resources and reflection

[SAP Discovering Finance](https://learning.sap.com/learning-journeys/discovering-finance) and [Financial Accounting Overview](https://learning.sap.com/learning-journeys/outlining-the-financial-accounting-overview): select the part relevant to tax control and document/reporting responsibilities. Ask which application owns the fact and which person approves its interpretation. Read selectively within the sprint.

Official resource pages checked 31 October 2026. Resources orient learning; current local authority guidance and qualified policy interpretation are still needed before production design, particularly for tax and reporting.

**Reflect:** What became clearer? Who could your design disadvantage? What evidence would overturn your choice?

**Next Pre-Foundation experiment:** select one hypothetical jurisdiction/document type and identify the official rule evidence needed before build.

**Mission:** Architecting Experiences for a Better World.

## Traceability and scope

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Finance blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/03-finance.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Finance academy source](https://app.notion.com/p/0c0a85eaefe145d3bed6c2ea143b6009).

Inherited blueprint anchors: OVE-M02, OVE-M08, OVE-M14, OVE-M20. New namespace OVE-FI04-OS denotes this learning expansion, not previously approved enterprise requirements.

**Trace:** source → OVE-FI04-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 (this experiment) → T01/T02/T03 → KPI01. All shortened IDs carry the same OVE-FI04-OS prefix. EV01 remains an empty evidence slot until a learner records results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA ownership/quality; COBIT control accountability; ISO/IEC 27001 information protection. This is not a compliance certification.

**Publication:** matching manually published learning editions. Original enterprise research and financial hypotheses remain preserved. No unattended synchronization is asserted.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/03-FI-Finance-Capability-Academy-Finance-Wednesday/FI04-ATX4-Architecting-Digital-Tax-Enterprises/01-FI04-ENE-energy/0-The-Origin-Story/sprint/energy-fi04-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1lmUvLKHvOS56RDm4JR09HcbDVE2_oYRRDLqLPMLQx3Q/edit?usp=drivesdk)

[Notion edition](https://app.notion.com/p/40ace6de608981fd8e75c27a5935ad49?pvs=204)
