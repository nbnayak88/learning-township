# The purchase order arrived but the supplier never accepted it
## PROC12 — Architecting Connected Procurement Enterprises

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-PROC12-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published learning content, not an enrolled course or certification.

> **Your promise:** In two hours, design one procurement exchange with business acknowledgment, safe replay and reconciled outcomes.

**One story · One Decision Card · Three tests**

## 1. The purchase behind the process

A procurement network delivers a PO, but the supplier rejects a unit of measure. The interface is green; an old replay later overwrites the buyer's amended quantity.

**Lead:** Rajiv Kapoor — Chief Digital and Information Officer (OVE-P05).  
**Counterpart:** Wei Zhang — Chief Supply Chain & Procurement Officer (OVE-P11).

Rajiv asks whether transport success proves business acceptance. Wei asks which PO version and business key the supplier actually agreed to.

The team defines delivery, validation and business acceptance separately. It preserves amendment sequence, routes rejects to owners and tests idempotent replay before claiming completion.

**Pause:** What business need and evidence must be clear before the next commitment? Ask both people one useful question.

OmniVerse is a fictional integrated energy group with 68,000 employees in 42 countries. Existing OVE-P personas retain their source identities. Dialogue, incidents, supplier records and proposed outcomes here are new learning fiction. No real supplier, award, transaction or implementation result is represented.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Pre-1978 examples describe the wider domain rather than OmniVerse corporate history.

- **1970–1989:** Paper orders and re-entry depend on manual confirmation.
- **1990–1999:** Batch files/EDI automate exchange but hide rejects.
- **2000–2009:** ERP and network integration connect orders and invoices.
- **2010–2019:** APIs/events improve timeliness while versions and units remain important.
- **2020–2025:** Assisted monitoring suggests repair; business reconciliation and controlled replay remain necessary.

**Mindset:** optimize the business outcome and relationship, with evidence for each consequential decision. A faster purchase can still create a larger downstream problem.

**Social impact question:** whose safety, livelihood, access to opportunity or environment could this choice affect?

## 3. AI-driven horizon, 2026–2050

**2026 experiment:** use assistance for a narrow evidence summary, draft or exception suggestion. Test what it misses before delegating any action.

**2030 checkpoint:** compare assisted work with a human-led baseline, including contrary evidence and a challenge route.

**2035–2050 scenario:** Imagine a 2050 supplier ecosystem exchanging commitments through agents. Participants must still agree identity, schemas, meanings and accepted business outcomes.

**Competing future:** During connectivity loss, durable pending states and a reconciled manual route remain essential.

These are design hypotheses, not forecasts, legal interpretations or vendor roadmaps. Autonomy remains bounded by approved authority.

## 4. Smallest useful architecture

**Capability — OVE-PROC12-OS-CAP01:** connected procurement enterprises.

**Value stages — OVE-PROC12-OS-VS01:** Authorize → send → validate → accept/reject → reconcile → repair → replay safely.

**Objects to distinguish:** supplier/business key, PO version, event ID, unit, effective time, acknowledgment and exception.

**Application responsibility:** Procurement owns PO meaning and approval; suppliers own their acknowledgments; integration owns delivery/recovery; receiving/Finance own later outcomes. PROC12 does not redefine contracts or payment policy.

**Protected boundary:** Technical receipt is not supplier acceptance, delivery, invoice approval or payment settlement.

Start with the business need before choosing SAP Ariba, SAP Business Network, ERP or another platform. Product scope, editions, local obligations and licensing require validation. The twelve PROC themes and twelve architecture streams are separate axes.

## 5. One Decision Card

Use synthetic case **OVE-PROC12-OS-SYN001**. The Google workbook supplies editable fields; the deck supports discussion. Together they decode this same sprint rather than adding separate required deliverables.

1. **Need:** one decision, affected population and missing fact.
2. **Evidence:** source/business IDs, specification or scope, validity, unit/currency where relevant.
3. **Owner:** accountable business decision maker, source application and receiving owner.
4. **Gate:** prerequisite, allowed next state and exception condition.
5. **Alternative:** Compare delivery-only monitoring with versioned business acknowledgments and safe recovery.
6. **Recovery:** escalation owner and safe correction/assisted route.
7. **Proof:** three actual paper results, a measure and stop/revise/proceed decision.

**Requirement — OVE-PROC12-OS-REQ01:** trace one authorized document version to its business outcome and reconcile duplicates, rejects and amendments.

**Decision — OVE-PROC12-OS-ADR01:** record the chosen option, alternative, trade-off and evidence that would change your choice.

## 6. Three tabletop tests

### T01 — Supplier rejects an otherwise delivered PO

**Expected:** Keep acceptance incomplete and route the reason to an accountable buyer.

### T02 — Old amendment arrives after a newer one

**Expected:** Prevent stale overwrite under the agreed version/order rule.

### T03 — Accepted message is replayed

**Expected:** Apply the business effect once and reconcile final quantities/status.

Record **input → expected → actual paper result → evidence → reviewer decision → revision/retest**. Sprint-local tests OVE-PROC12-OS-T01/T02/T03 support REQ01. Publishing expected results does not prove execution.

**Measure — OVE-PROC12-OS-KPI01:** in-scope documents with confirmed business outcomes / documents due, with unresolved aging. Confirm the owner, baseline, period and exclusions before setting targets.

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

**Next Pre-Foundation experiment:** write one PO event contract and test duplicate and reordered processing.

**Mission:** Architecting Experiences for a Better World.

## Sources and traceability

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Procurement blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/04-procurement.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Current academy mapping](https://app.notion.com/p/54da2cdc13204086bb4f7fb2387b591a).

Inherited anchors: OVE-M03, OVE-M09, OVE-M10, OVE-M17. New OVE-PROC12-OS IDs belong to this proposed learning expansion.

**Trace:** source → OVE-PROC12-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 → T01/T02/T03 → KPI01. Shortened IDs retain the OVE-PROC12-OS prefix. EV01 stays empty until observed evidence is recorded.

**Source reconciliation:** legacy Drive prompt filenames use PROC01 for Ariba Sourcing. They remain preserved. This edition follows the current catalog: PROC01 strategy, PROC02 sourcing, and unchanged APR1–AIG2 course-code sequence.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA data quality; COBIT accountability; ISO/IEC 27001 information protection; ISO 20400 sustainability guidance. No compliance certification is claimed.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/04-PROC-Procurement-Capability-Academy-Procurement-Thursday/PROC12-AIG2-Architecting-Connected-Procurement-Enterprises/01-PROC12-ENE-energy/0-The-Origin-Story/sprint/energy-proc12-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1qA0e-sXaAuCHNG2M3S0FSHSBdCCWejbFDxlBF-fPfDY/edit?usp=drivesdk)


[Google Slides](https://docs.google.com/presentation/d/1EQylmZv8alVVFIApw-y97uy0wEDXzNuqJefxZbNCHbc/edit?usp=drivesdk) · [Google Sheets Decision Card](https://docs.google.com/spreadsheets/d/1_QxWB4k6KpVtfw3QFhfL_ceRmcBo6UgP9sVmnEj5gBU/edit?usp=drivesdk) · [Notion](https://app.notion.com/p/40ace6de608981159458ec200ba40378?pvs=204) · [All twelve Energy Procurement stories](https://github.com/nbnayak88/learning-township/blob/main/04-PROC-Procurement-Capability-Academy-Procurement-Thursday/energy-origin-stories.md)
