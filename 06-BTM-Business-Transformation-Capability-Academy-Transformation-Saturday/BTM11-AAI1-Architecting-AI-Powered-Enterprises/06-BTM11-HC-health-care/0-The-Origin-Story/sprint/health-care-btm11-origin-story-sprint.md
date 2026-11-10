# The clinical-admin assistant drafted a summary; two patient identifiers were mixed
## BTM11 — Architecting AI-Powered Enterprises

**SuccessLabs Academy · OmniHealth Systems Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-BTM11-HC-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one governed-assistance decision that keeps evidence, identity and human review accountable.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

An administrative assistant drafts a referral summary, but two patient records were combined.

**AI or data lead:** Dr. Diego Silva — Research and Responsible AI Lead (OHS-P14).  
**Counterpart:** Omar Haddad — CISO and Privacy Lead (OHS-P10).  
**Operations or customer voice:** Dr. Amina Okafor — Nursing and Care Coordination Director (OHS-P07).

Dr. Diego Silva asks what must be true before the team decides. Omar Haddad asks which evidence and owner support the decision. Dr. Amina Okafor asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic record, the identifiers were close and the retrieval merged them.

**Pause:** What evidence must the assistant cite? Which source version is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniHealth Systems Ltd. is an aspirational case study (USD 34B healthcare group; 126,000 staff; 19 countries). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniHealth Systems Ltd. history.

- **1970s–1980s:** Expert knowledge lives in manuals and people; answers depend on who is asked.
- **1980s–1990s:** Rule-based and expert systems encode procedures; maintenance of the rules becomes the hard part.
- **2000s–2010s:** Search, analytics and machine learning scale prediction; explanations and data quality lag.
- **2020s–2026:** Generative assistants draft fluent answers; grounding, identity and review decide whether they can be trusted.

**Mindset shift:** start with the decision, its evidence and its owner, then choose the model. A fluent answer built on a stale source can spread an error faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance on low-risk drafting with cited sources; retain the evidence gate, delegated authority and a human reviewer.

**2040 question:** if assistants act across systems, can each action carry the user's delegated authority and a reviewable trail?

**2050 scene:** Imagine assistants that coordinate routine work within clear limits. Providers may act faster, but people must own consequential decisions and the right to stop.

**Competing future:** A smaller rules-based service with trained people may beat an adaptive assistant on reliability, privacy and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OHS-BTM11-OS-CAP01:** governed AI-assisted decision. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OHS-BTM11-OS-VS01:** Frame the decision → ground the evidence → assist → human review → act → monitor.

**Objects to distinguish:** decision, evidence source, assistant output, confidence, reviewer and override.

**Proposed responsibility:** The business owner owns the decision; the data owner owns the source and its version; security owns identity and access; the reviewer owns the release. BTM11 owns the governed-assistance loop, not the model build.

**Protected boundary:** A fluent assistant answer is not evidence, and a successful pilot does not prove an approved enterprise capability.

Assistant and platform services are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole decision. Continue with the BTM11 bootcamp demos for this sector. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OHS-BTM11-OS-SYN001**. Synthetic assistant OHS-AST300, records OHS-PT300 and OHS-PT301, summary OHS-SUM300. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare releasing assistant answers directly with requiring cited sources, delegated authority and human review.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OHS-BTM11-OS-REQ01:** link one governed-assistance hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OHS-BTM11-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — The summary mixes two identifiers

**Expected:** Require identity checks and a human review before release.

### T02 — An agent reads records through a shared identity

**Expected:** Require delegated user authority, not a shared application identity, and log who acted.

### T03 — An output touches care decisions

**Expected:** Keep clinical decisions with accountable clinicians; the assistant only drafts.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OHS-BTM11-OS-T01/T02/T03, supporting OHS-BTM11-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OHS-BTM11-OS-KPI01:** Share of reviewed assistant outputs that carry a cited source version and a recorded reviewer decision, with a defined population and period; track overrides. Assign Dr. Diego Silva as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

**Acceptance:** the card identifies source and owner, preserves the protected boundary, handles all three tests after documented revisions and explains the decision in 60 seconds. Missing evidence remains visible. Record what is still unverified.

## 7. Use your 120 minutes

- **0–20:** read the origin timeline; explain what changed and what did not.
- **20–45:** role-play the story; ask the lead, counterpart and voice one useful question each.
- **45–65:** draw responsibilities and consult one resource selectively.
- **65–100:** complete the single Decision Card and compare the alternative.
- **100–115:** run the three tests; revise from observed paper behavior.
- **115–120:** explain the decision in 60 seconds and choose the next experiment.

All reading fits within these blocks. Do not complete an entire product course during the sprint.

## 8. Read with a question

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): which evidence, owner and monitoring would bound an assisted decision here?
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework): who owns permitted information use for this card?
- [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/): can everyone affected perceive, operate and understand the journey?

Official reference pages checked 10 November 2026; access and versions can vary. The historical periods and future stories are educational synthesis, not claims established by these pages.

## 9. Reflect and continue

Which answer would you still not release? Who reviewed it? What evidence would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable grounding hypothesis and the check that would test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniHealth Systems Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md): existing names, designations and OHS-P identifiers.
- **New material:** OHS-BTM11-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OHS-BTM11-OS-CAP01 → OHS-BTM11-OS-VS01 → OHS-BTM11-OS-REQ01 → OHS-BTM11-OS-ADR01 → OHS-BTM11-OS-EXP01 (this tabletop experiment) → OHS-BTM11-OS-T01/T02/T03 → OHS-BTM11-OS-KPI01. OHS-BTM11-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
