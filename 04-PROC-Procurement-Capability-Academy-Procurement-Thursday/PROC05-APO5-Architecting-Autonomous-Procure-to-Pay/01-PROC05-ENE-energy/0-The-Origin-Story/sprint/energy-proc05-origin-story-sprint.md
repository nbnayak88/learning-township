# The purchase was urgent but the acceptance record was missing
## PROC05 — Architecting Autonomous Procure to Pay

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-PROC05-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published learning content, not an enrolled course or certification.

> **Your promise:** In two hours, design one requisition-to-invoice handoff with approved buying authority and verifiable receipt or service acceptance.

**One story · One Decision Card · Three tests**

## 1. The purchase behind the process

A turnaround team requests a maintenance service after work has started. The requisition, purchase order, service acceptance and invoice each use a different reference, and the supplier requests immediate payment.

**Lead:** Wei Zhang — Chief Supply Chain & Procurement Officer (OVE-P11).  
**Counterpart:** Michael Reed — Group Chief Financial Officer (OVE-P03).

Wei asks what was authorized and delivered. Michael asks which evidence supports the liability and which exception process applies to the retrospective request.

They link the business obligation, retain the exception history and identify the applicable goods/service acceptance gate. Payment approval and bank release stay with Finance.

**Pause:** What business need and evidence must be clear before the next commitment? Ask both people one useful question.

OmniVerse is a fictional integrated energy group with 68,000 employees in 42 countries. Existing OVE-P personas retain their source identities. Dialogue, incidents, supplier records and proposed outcomes here are new learning fiction. No real supplier, award, transaction or implementation result is represented.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Pre-1978 examples describe the wider domain rather than OmniVerse corporate history.

- **1970–1989:** Paper requisitions, orders and receipts move through manual approvals.
- **1990–1999:** Purchasing databases reduce re-entry but references remain disconnected.
- **2000–2009:** ERP procure-to-pay links commitments, receipts and invoices.
- **2010–2019:** Guided buying and networks coordinate user and supplier tasks.
- **2020–2025:** Assisted capture suggests matches; buying authority and acceptance remain necessary.

**Mindset:** optimize the business outcome and relationship, with evidence for each consequential decision. A faster purchase can still create a larger downstream problem.

**Social impact question:** whose safety, livelihood, access to opportunity or environment could this choice affect?

## 3. AI-driven horizon, 2026–2050

**2026 experiment:** use assistance for a narrow evidence summary, draft or exception suggestion. Test what it misses before delegating any action.

**2030 checkpoint:** compare assisted work with a human-led baseline, including contrary evidence and a challenge route.

**2035–2050 scenario:** Imagine a 2050 assistant preparing a purchase from an approved maintenance need. It must respect spending authority and evidence of service delivery before downstream payment decisions.

**Competing future:** If a supplier or frontline user is offline, an assisted process should retain the same approvals and traceable references.

These are design hypotheses, not forecasts, legal interpretations or vendor roadmaps. Autonomy remains bounded by approved authority.

## 4. Smallest useful architecture

**Capability — OVE-PROC05-OS-CAP01:** procure to pay.

**Value stages — OVE-PROC05-OS-VS01:** Request → approve → order → receive/accept → validate invoice → hand off payable outcome.

**Objects to distinguish:** requisition, approval, PO, receipt/service entry, invoice, exception and ERP acknowledgment.

**Application responsibility:** Procurement owns buying commitment; requesters/receiving owners confirm delivery; AP owns payable validation; treasury owns bank release. Contractor workforce and HSE decisions remain with their domain owners.

**Protected boundary:** A PO or timesheet does not universally prove acceptance. Choose the applicable evidence gate and controlled exception policy.

Start with the business need before choosing SAP Ariba, SAP Business Network, ERP or another platform. Product scope, editions, local obligations and licensing require validation. The twelve PROC themes and twelve architecture streams are separate axes.

## 5. One Decision Card

Use synthetic case **OVE-PROC05-OS-SYN001**. The Google workbook supplies editable fields; the deck supports discussion. Together they decode this same sprint rather than adding separate required deliverables.

1. **Need:** one decision, affected population and missing fact.
2. **Evidence:** source/business IDs, specification or scope, validity, unit/currency where relevant.
3. **Owner:** accountable business decision maker, source application and receiving owner.
4. **Gate:** prerequisite, allowed next state and exception condition.
5. **Alternative:** Compare fast document creation with a linked obligation and explicit retrospective-exception route.
6. **Recovery:** escalation owner and safe correction/assisted route.
7. **Proof:** three actual paper results, a measure and stop/revise/proceed decision.

**Requirement — OVE-PROC05-OS-REQ01:** trace one authorized purchase through applicable receipt/service evidence and acknowledged invoice handoff.

**Decision — OVE-PROC05-OS-ADR01:** record the chosen option, alternative, trade-off and evidence that would change your choice.

## 6. Three tabletop tests

### T01 — Service acceptance is missing

**Expected:** Hold unsupported acceptance and identify the authorized service owner.

### T02 — Invoice exceeds approved scope

**Expected:** Expose variance, seek authorized change/exception and prevent silent acceptance.

### T03 — Duplicate invoice or PO resend

**Expected:** Link the existing business reference and prevent duplicate obligations.

Record **input → expected → actual paper result → evidence → reviewer decision → revision/retest**. Sprint-local tests OVE-PROC05-OS-T01/T02/T03 support REQ01. Publishing expected results does not prove execution.

**Measure — OVE-PROC05-OS-KPI01:** reviewed purchase/invoice handoffs with complete applicable evidence / handoffs reviewed. Confirm the owner, baseline, period and exclusions before setting targets.

**Acceptance:** the card names owners and sources, preserves the protected boundary, handles all three tests after documented revisions and explains the decision in 60 seconds. Keep unverified facts visible.

## 7. Your 120 minutes

- **0–20:** read the evolution; explain the problem that persists.
- **20–45:** role-play the lead and counterpart; request evidence.
- **45–65:** map application responsibilities and inspect one resource.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise from observed paper behavior.
- **115–120:** explain your decision and choose the next experiment.

## 8. Resources and reflection

[SAP Procurement Process Overview](https://learning.sap.com/courses/procurement-process-overview) and [Sourcing and Contract Management learning journey](https://learning.sap.com/learning-journeys/discovering-procurement-sourcing-and-contract-management-in-sap-ariba-and-sap-cloud-erp): read the relevant portion selectively. Which product owns the record, and what must the receiving application acknowledge?

[ISO 20400 sustainable procurement guidance](https://www.iso.org/standard/63026.html): consider stakeholder impact and accountable sustainable purchasing. This educational mapping does not claim certification.

Official reference pages checked 31 October 2026. Historical periodization and future scenarios are teaching synthesis, not facts established by these product pages.

**Reflect:** What changed for the buyer and supplier? Who could be excluded? Which evidence would overturn your preferred option?

**Next Pre-Foundation experiment:** define one service-entry acceptance rule and its ERP handoff.

**Mission:** Architecting Experiences for a Better World.

## Sources and traceability

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Procurement blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/04-procurement.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Current academy mapping](https://app.notion.com/p/54da2cdc13204086bb4f7fb2387b591a).

Inherited anchors: OVE-M03, OVE-M09, OVE-M10, OVE-M17. New OVE-PROC05-OS IDs belong to this proposed learning expansion.

**Trace:** source → OVE-PROC05-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 → T01/T02/T03 → KPI01. Shortened IDs retain the OVE-PROC05-OS prefix. EV01 stays empty until observed evidence is recorded.

**Source reconciliation:** legacy Drive prompt filenames use PROC01 for Ariba Sourcing. They remain preserved. This edition follows the current catalog: PROC01 strategy, PROC02 sourcing, and unchanged APR1–AIG2 course-code sequence.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA data quality; COBIT accountability; ISO/IEC 27001 information protection; ISO 20400 sustainability guidance. No compliance certification is claimed.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/04-PROC-Procurement-Capability-Academy-Procurement-Thursday/PROC05-APO5-Architecting-Autonomous-Procure-to-Pay/01-PROC05-ENE-energy/0-The-Origin-Story/sprint/energy-proc05-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1GTZF0fYEokD1C_nXLfet0BxOJ3CgB4qOhO_wRSzE1pA/edit?usp=drivesdk)


[Google Slides](https://docs.google.com/presentation/d/1XPXhyXSjDIEo_Yk2HOZR4nTEGdDDoKUyQDyzCZ_n63I/edit?usp=drivesdk) · [Google Sheets Decision Card](https://docs.google.com/spreadsheets/d/1CpIQQsodzESs0zGPZCoALU7tcmIpZk4a-MobcBpP-zY/edit?usp=drivesdk) · [Notion](https://app.notion.com/p/40ace6de608981d19e7feab9aa035973?pvs=204) · [All twelve Energy Procurement stories](https://github.com/nbnayak88/learning-township/blob/main/04-PROC-Procurement-Capability-Academy-Procurement-Thursday/energy-origin-stories.md)
