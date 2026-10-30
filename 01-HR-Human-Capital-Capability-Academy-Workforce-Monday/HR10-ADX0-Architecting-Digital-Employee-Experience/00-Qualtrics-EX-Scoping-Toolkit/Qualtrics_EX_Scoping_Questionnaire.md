# Qualtrics Employee Experience: Scoping Questionnaire

**Client:** [Client name]  |  **Prepared by:** [Consultant / firm]  |  **Date:** 28 October 2026  |  **Version:** 1.0

**Context:** SAP SuccessFactors Employee Central and Performance & Goals (PMGM) are live. Other modules are upcoming. Qualtrics Employee Experience (EX) go-live is targeted in 3-4 months (late January to February 2027).

---

## How to use this document

1. Mark each use case **Wave 1**, **Phase 2** or **Out of scope** (see Use-case landscape).
2. Answer the 84 kick-off questions (marked ★) first. They unlock design decisions.
3. Work through the remaining sections. Write answers under each question, or in the companion Excel workbook.
4. Complete the module readiness, data inventory and stakeholder tables in the appendices.

**Totals:** 200 questions in 19 sections. 113 are P1 (must answer), 78 are P2 (should answer), 9 are P3 (nice to have).

| Priority | Meaning |
|---|---|
| P1 | Must answer; otherwise design or build is blocked |
| P2 | Should answer before build |
| P3 | Nice to have, or Phase 2 |

| Needed by | Meaning |
|---|---|
| Week 2 | Needed in discovery |
| Week 4 | Needed to finish design |
| Week 8 | Needed before build completes |
| Post go-live | Can follow launch |

> **Product caution.** SAP and Qualtrics product names, packaging and integration options change often. Treat any product option mentioned here as something to validate with SAP and Qualtrics, not a commitment.

## Contents

- [Use-case landscape](#use-case-landscape)
- [1. Project Context & Objectives](#1-project-context--objectives)
- [2. Use-Case Selection & Prioritisation](#2-use-case-selection--prioritisation)
- [3. Licensing, Commercials & Contracting](#3-licensing-commercials--contracting)
- [4. Employee Engagement Survey](#4-employee-engagement-survey)
- [5. Pulse & Ad Hoc Listening](#5-pulse--ad-hoc-listening)
- [6. Lifecycle Moments: Onboarding, Exit & Candidate](#6-lifecycle-moments-onboarding-exit--candidate)
- [7. 360 / Multi-Rater Feedback](#7-360--multi-rater-feedback)
- [8. Manager Effectiveness & Action Planning](#8-manager-effectiveness--action-planning)
- [9. Employee Technology Experience](#9-employee-technology-experience)
- [10. Survey Content, Scales & Languages](#10-survey-content-scales--languages)
- [11. SuccessFactors Integration & Architecture](#11-successfactors-integration--architecture)
- [12. Employee Data, Hierarchy & Attributes](#12-employee-data-hierarchy--attributes)
- [13. Reporting, Dashboards & Analytics (incl. AI)](#13-reporting-dashboards--analytics-incl-ai)
- [14. Security, Privacy & Compliance](#14-security-privacy--compliance)
- [15. Roles, Access & Governance](#15-roles-access--governance)
- [16. Communications, Change & Adoption](#16-communications-change--adoption)
- [17. Upcoming SuccessFactors Modules & Sequencing](#17-upcoming-successfactors-modules--sequencing)
- [18. Delivery, Timeline, Testing & Support](#18-delivery-timeline-testing--support)
- [19. Success Measures & Operating Model](#19-success-measures--operating-model)
- [Appendices](#appendices)

---

## Use-case landscape

Our starting hypothesis for fit within a 3-4 month window. Challenge it in discovery.

| Use case | What it covers | Depends on | Fit | Why | Scope decision |
|---|---|---|---|---|---|
| **Annual Engagement** | Census survey of engagement, drivers and manager effectiveness with hierarchy-based reporting. | EC only (live) | High | Needs EC data only; the biggest effort is content, anonymity design and reporting roles. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Pulse & Ad Hoc** | Short recurring or event-driven surveys, including a SuccessFactors adoption pulse. | EC only (live) | High | Reuses the engagement foundation; quickest visible value. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Onboarding** | Surveys at set days after hire for new hire, manager and buddy. | EC hire events; richer if SF Onboarding is live | Medium-High | Trigger works from EC; check hiring volumes, event reasons and email availability before day one. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Exit** | Leaver feedback and attrition drivers, before or after the last day. | EC termination events; offboarding process | Medium-High | Needs reliable termination data and a personal-contact policy; legal sensitivity is high. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Candidate Experience** | Feedback from applicants across hiring stages. | SF Recruiting (planned) | Low-Medium | Depends on Recruiting being live and on applicant-privacy rules; usually a Phase 2 candidate. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **360 / Multi-Rater** | Subjects receive feedback from self and evaluators; workflows can be predefined, nominated or open. | EC; PMGM overlap decision | Medium | Needs competency content, rater workflow and a decision against PMGM multi-rater; plan waves. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Manager Effectiveness & Action Planning** | Manager dashboards, upward feedback and tracked action plans. | Engagement or pulse results | Medium-High | Builds on engagement; the key risks are small-team anonymity and manager capability. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Employee Technology Experience** | Feedback on tools and services, including SuccessFactors itself. | Optional ITSM integration | Medium | SF-adoption pulse is a quick win; ITSM integration is Phase 2. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Internal Moves & Return from Leave** | Surveys after promotion, transfer, leave return or manager change. | EC events; data quality | Low-Medium | Same mechanics as onboarding; usually follows once triggers are proven. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Well-Being & Inclusion** | Targeted surveys on well-being, belonging and inclusion. | Legal approval for sensitive data | Medium | Content and legal review dominate; the platform work is light. | ☐ Wave 1  ☐ Phase 2  ☐ Out |
| **Change & Project Pulses** | Rapid feedback on restructuring, policy change or return-to-office. | EC only (live) | High | Easy once the foundation exists; needs governance to avoid fatigue. | ☐ Wave 1  ☐ Phase 2  ☐ Out |

**Starting hypothesis.** Wave 1: foundation (integration, directory, roles, anonymity rules) plus Engagement or Pulse, Onboarding and Exit. Phase 2: 360, Candidate Experience, Technology Experience integrations, internal moves.

**Qualtrics 360 terms** (from the Qualtrics Support guide you referenced):

- **Subject:** A person receiving feedback; usually also completes a self-evaluation.
- **Evaluator:** A person giving feedback on a subject; external evaluators only give feedback.
- **Brand Administrator:** Full platform access including directory and permissions.
- **Employee Insights Administrator:** Can build and run EX projects but has no directory or Admin page access.
- **Directory:** Central list of all EX participants for the organisation, current and previous.

---

## 1. Project Context & Objectives

*Why the client is investing, who decides, and what the listening landscape looks like today.*

### CTX-01 ★  What are the top three business outcomes you expect from Qualtrics EX (for example lower regretted attrition, higher engagement, better onboarding, stronger managers, SuccessFactors adoption)? Please rank them.

- **Why we ask:** Outcomes decide which use cases go first and how success is judged.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-02 ★  Who is the executive sponsor, and what decision rights do they hold over scope, budget and the go-live date?

- **Why we ask:** Avoids stalled decisions in a 3-4 month window.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-03 ★  Which employee listening tools, vendors and programmes run today (engagement, pulse, onboarding, exit, 360)? Please share the last 24 months of results, response rates and survey instruments.

- **Why we ask:** Gives baselines and reusable content. Qualtrics itself advises gathering previous reports as a reference point.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-04  Which existing survey programmes must be replaced, kept, or run in parallel at go-live?

- **Why we ask:** Drives migration, trend continuity and communication.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-05 ★  Workforce profile: headcount, countries, legal entities, worker types (employees, contingent, interns), share of shift or deskless staff, and languages spoken.

- **Why we ask:** Sizes licences, languages, delivery channels and test scope.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-06 ★  Is the go-live date fixed? What drives it (contract start, board commitment, business event) and what is the cost of moving it by four weeks?

- **Why we ask:** Tells us whether to cut scope or move the date when trade-offs appear.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-07  Which other programmes compete for the same HR, HRIS, IT and communications people over the next four months (other SF module go-lives, payroll cycles, M&A, restructuring)?

- **Why we ask:** Capacity clashes are a leading cause of slippage.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-08  Who will own EX after go-live (HR, People Analytics, IT, Internal Comms) and how large is the run team?

- **Why we ask:** The design must match the team that will operate it.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-09  Is there an EX framework, employee value proposition or people strategy that survey content and dashboards should align to?

- **Why we ask:** Keeps content and reporting consistent with strategy.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-10  What has worked or failed in past listening efforts (low participation, survey fatigue, no visible action, trust issues)?

- **Why we ask:** Prevents repeating known failures.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CTX-11 ★  Is Qualtrics already used elsewhere in the organisation (CX, brand, research)? If so, share tenant details, data centre and existing administrators.

- **Why we ask:** Lets us reuse existing tenant, SSO and security approvals.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## 2. Use-Case Selection & Prioritisation

*Which Employee Experience use cases go live first, for whom, how often, and who owns each.*

### USE-01 ★  For each use case on the Use Case Map tab, mark Wave 1 (go-live), Phase 2, or Out of scope.

- **Why we ask:** The core scoping decision; everything else follows from it.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### USE-02  For each in-scope use case, who is the business owner, who is the audience, and what decision will the data drive?

- **Why we ask:** A use case without an owner and a decision becomes shelfware.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### USE-03 ★  If only one or two use cases could be live in 3-4 months, which would they be and why?

- **Why we ask:** Forces a realistic minimum viable launch.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### USE-04 ★  Which use cases depend on SuccessFactors modules that are not yet live, and could they start with a file-based or manual trigger?

- **Why we ask:** Lets lifecycle use cases launch without waiting for every module.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ONB, EXT, CAN
- **Response:**

  > _[Type answer here]_

### USE-05  Beyond the standard list, are there other use cases (M&A integration, return-to-office, restructuring, safety culture, well-being, inclusion, SuccessFactors adoption)?

- **Why we ask:** Surfaces ad hoc needs early so the design stays flexible.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Multi-select  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### USE-06  Which populations are in scope for each use case (all employees, countries, entities, job families, new joiners, leavers, contingent workers)?

- **Why we ask:** Determines the participant file, licences and legal review.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### USE-07 ★  How often must each use case run (annual, quarterly, event-triggered, always-on), and what are the blackout periods (year-end, payroll, appraisal cycles, local holidays)?

- **Why we ask:** Builds the listening calendar and avoids fatigue and clashes.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### USE-08  Will one listening calendar govern engagement, pulse and lifecycle surveys, and who owns it?

- **Why we ask:** Caps total surveys per employee and avoids overlap.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### USE-09  Which surveys should be tied to the SF PMGM cycle (for example 360 feedback inside the performance cycle, or a post-review pulse)?

- **Why we ask:** Aligns timing and avoids stacking requests on managers.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** 360, ENG, PLS
- **Response:**

  > _[Type answer here]_

---

## 3. Licensing, Commercials & Contracting

*Contract route, licensed products, tenant, data centre and procurement readiness.*

### COM-01 ★  How is Qualtrics EX contracted: SAP Endorsed Apps agreement, directly with Qualtrics, or via a reseller? Which products or SKUs (Engagement, Pulse, Onboarding, Exit, 360, Lifecycle, Employee Technology Experience)?

- **Why we ask:** Licensed products set what can be configured and when. SAP and Qualtrics announced an Endorsed Apps route in January 2025.
- **Priority:** P1 - Must answer  |  **Owner:** Finance / Procurement  |  **Needed by:** Week 2  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### COM-02  What are the licensed participant counts per product, and the contract start date and term? Does the licence start before the build begins?

- **Why we ask:** A late licence start blocks tenant access and build.
- **Priority:** P1 - Must answer  |  **Owner:** Finance / Procurement  |  **Needed by:** Week 2  |  **Type:** Number  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### COM-03 ★  Is the Qualtrics tenant (brand) already provisioned, and in which data centre region?

- **Why we ask:** Region drives data residency and is hard to change later.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 2  |  **Type:** Yes / No  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### COM-04 ★  Are AI features (Qualtrics Assist, text analytics, conversational feedback) licensed, and permitted under your internal AI policy?

- **Why we ask:** AI features may need separate approval.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 4  |  **Type:** Yes / No  |  **Use case:** RPT
- **Response:**

  > _[Type answer here]_

### COM-05  What budget is approved for implementation, change management, translation and run costs (admin effort, partner support)?

- **Why we ask:** Sets realistic scope.
- **Priority:** P2 - Should answer  |  **Owner:** Finance / Procurement  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### COM-06 ★  Who is the implementation partner, and which SAP and Qualtrics contacts (account executives, solution architects) are engaged?

- **Why we ask:** Shows who can unblock licence, tenant and integration questions.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### COM-07 ★  What is the status of procurement, vendor risk assessment and data processing agreements for Qualtrics, and how long do these normally take?

- **Why we ask:** Security and legal reviews can exceed eight weeks.
- **Priority:** P1 - Must answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### COM-08  Are there other costs to plan for: integration middleware (SAP BTP / Integration Suite), SSO, premium support, benchmarks?

- **Why we ask:** Avoids late surprises.
- **Priority:** P2 - Should answer  |  **Owner:** Finance / Procurement  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** INT
- **Response:**

  > _[Type answer here]_

---

## 4. Employee Engagement Survey

*Annual or biannual census engagement programme, models, anonymity, reporting cuts and benchmarks.*

### ENG-01 ★  Is there an existing engagement model or index (composite index, eNPS, drivers)? Must trend continuity with historical results be preserved?

- **Why we ask:** Changing items breaks year-on-year comparison.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-02  Will you use the Qualtrics best-practice engagement library, a custom model, or a hybrid? Who approves final content?

- **Why we ask:** Decides build effort, translation scope and approval path.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-03  Census or sample? What participation target do you set, and what was achieved last time?

- **Why we ask:** Sets licence volume, reminder strategy and success KPI.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-04 ★  Which results cuts are required (org unit, location, job level, tenure, age band, gender, manager)? What is the minimum group size for reporting?

- **Why we ask:** Drives data attributes needed from EC and the anonymity threshold.
- **Priority:** P1 - Must answer  |  **Owner:** People Analytics  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-05 ★  Will the survey be anonymous or confidential? Will SF attributes be attached to responses, and how will employees be told?

- **Why we ask:** The promise made to employees must match the technical design.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-06  Is benchmarking required (internal, industry, external)? Against which peer groups?

- **Why we ask:** Determines licensed benchmark content and comparisons.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-07  Who sees results (executives, HRBPs, all people managers), and when? What is the cascade process?

- **Why we ask:** Defines roles, dashboard design and release gates.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** List / table  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-08 ★  How will open-text comments be handled: languages, redaction of names, and escalation of sensitive content (harassment, safety)?

- **Why we ask:** Duty-of-care and anonymity obligations.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-09 ★  What are managers expected to do with results (action plans, deadlines, tracking)? Should plans link to SF goals or development plans?

- **Why we ask:** Closing the loop is what makes engagement credible.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ENG, MGR
- **Response:**

  > _[Type answer here]_

### ENG-10  What survey window and reminder pattern are planned, and how will frontline or deskless staff take part (mobile, kiosk, QR code, personal links)?

- **Why we ask:** Participation fails when access is not designed in.
- **Priority:** P2 - Should answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### ENG-11 ★  Do you expect to link engagement to attrition, performance (PMGM ratings) or other HR outcomes, and is that permitted by policy and employee representatives?

- **Why we ask:** Joining survey and HR data is valuable but needs legal and trust safeguards.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

---

## 5. Pulse & Ad Hoc Listening

*Always-on, quarterly, topic-based and event-driven pulses, governance and fatigue control.*

### PLS-01 ★  Which pulse programmes do you need (always-on, quarterly, topic-based, post-event, manager pulse)?

- **Why we ask:** Defines templates, licences and cadence.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** PLS
- **Response:**

  > _[Type answer here]_

### PLS-02 ★  Who may launch a pulse (central HR only, or delegated to HRBPs and managers)? What caps prevent fatigue (maximum surveys per employee per quarter)?

- **Why we ask:** Governance prevents survey overload.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** PLS
- **Response:**

  > _[Type answer here]_

### PLS-03  How will respondents be sampled (full population, random sample, rotating cohorts)?

- **Why we ask:** Affects participant lists and statistical validity.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** PLS
- **Response:**

  > _[Type answer here]_

### PLS-04  Who curates the standard pulse question bank, and what is the target length (items and minutes)?

- **Why we ask:** Keeps pulses short and comparable.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** PLS
- **Response:**

  > _[Type answer here]_

### PLS-05 ★  Which delivery channels are needed: email, SF home page or Engagement card, MS Teams, Slack, SMS, mobile, QR codes?

- **Why we ask:** Channels determine integration effort and response rates.
- **Priority:** P1 - Must answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 4  |  **Type:** Multi-select  |  **Use case:** PLS
- **Response:**

  > _[Type answer here]_

### PLS-06  For ad hoc, event-driven pulses (restructuring, policy change, SuccessFactors go-live), what approval workflow and turnaround time are expected?

- **Why we ask:** Speed versus control trade-off.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** PLS, ETX
- **Response:**

  > _[Type answer here]_

### PLS-07 ★  Should low scores trigger real-time alerts or cases to HRBPs or managers? Which case or ticketing system would receive them?

- **Why we ask:** Defines workflow and integration scope.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** PLS
- **Response:**

  > _[Type answer here]_

### PLS-08  Who sees pulse results, at what minimum group size, and how quickly after close?

- **Why we ask:** Sets expectations and dashboard design.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** PLS
- **Response:**

  > _[Type answer here]_

---

## 6. Lifecycle Moments: Onboarding, Exit & Candidate

*Event-triggered surveys driven by Employee Central events (hire, transfer, leave, termination).*

### LCE-01 ★  Which lifecycle moments are in scope: candidate, pre-boarding, Day 1 / 30 / 90 / 180, probation end, promotion, transfer, return from leave, manager change, exit (voluntary or involuntary), alumni?

- **Why we ask:** Each moment needs a trigger, template and owner.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 2  |  **Type:** Multi-select  |  **Use case:** ONB, EXT, CAN
- **Response:**

  > _[Type answer here]_

### LCE-02 ★  For each moment, what is the EC trigger (hire date, position start, event reason, employment status, termination date)? Which event reasons apply?

- **Why we ask:** Triggers must be reliable and mapped to configured event reasons.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ONB, EXT
- **Response:**

  > _[Type answer here]_

### LCE-03  Is SAP SuccessFactors Onboarding (or another tool) live at go-live? If not, what is the system of record for new-hire tasks and data?

- **Why we ask:** Determines whether onboarding surveys can use task or milestone data.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Single choice  |  **Use case:** ONB
- **Response:**

  > _[Type answer here]_

### LCE-04 ★  What are the monthly hiring volumes by country, and what survey cadence is wanted (days since hire) for new hire, manager and buddy?

- **Why we ask:** Sizes the programme and tells us if results will reach reportable group sizes.
- **Priority:** P1 - Must answer  |  **Owner:** Talent Acquisition  |  **Needed by:** Week 4  |  **Type:** Number  |  **Use case:** ONB
- **Response:**

  > _[Type answer here]_

### LCE-05 ★  How should exit surveys work: which exit types are included (resignation, retirement, dismissal, contract end), and should they be sent before or after the last day?

- **Why we ask:** Exit timing and exclusions are sensitive and legal-critical.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** EXT
- **Response:**

  > _[Type answer here]_

### LCE-06  After offboarding, how will leavers be reached (personal email) and what are the policy and legal limits on holding that data and on alumni contact?

- **Why we ask:** Corporate email is often disabled at exit.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** EXT
- **Response:**

  > _[Type answer here]_

### LCE-07  Will a self-service survey complement or replace HR-led exit interviews? Is manager input about the leaver required?

- **Why we ask:** Defines the exit experience and data model.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** EXT
- **Response:**

  > _[Type answer here]_

### LCE-08  Is Recruiting Management in scope and live? At which stages should candidate surveys trigger (applied, interviewed, offered, declined, hired), and what applicant-privacy limits apply?

- **Why we ask:** Candidate data often sits in a different system with different privacy rules.
- **Priority:** P2 - Should answer  |  **Owner:** Talent Acquisition  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** CAN
- **Response:**

  > _[Type answer here]_

### LCE-09  Are surveys needed for internal moves, promotions, return from leave or manager change?

- **Why we ask:** Candidate Phase 2 moments.
- **Priority:** P3 - Nice to have  |  **Owner:** HR / People Leadership  |  **Needed by:** Post go-live  |  **Type:** Multi-select  |  **Use case:** LCE
- **Response:**

  > _[Type answer here]_

### LCE-10 ★  When a new hire or leaver raises a serious issue (harassment, safety, discrimination), who is notified, how fast, and what happens to anonymity?

- **Why we ask:** Duty-of-care protocol must exist before launch.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ONB, EXT
- **Response:**

  > _[Type answer here]_

### LCE-11  Do managers see onboarding and exit results for their teams, and under what anonymity rules?

- **Why we ask:** Balances insight and confidentiality.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ONB, EXT, MGR
- **Response:**

  > _[Type answer here]_

### LCE-12  How reliable are hire and termination dates, business email and manager assignment in EC today? Are back-dated, future-dated or mass-uploaded records common?

- **Why we ask:** Lifecycle triggers fire on this data; poor quality means missed or wrong surveys.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ONB, EXT
- **Response:**

  > _[Type answer here]_

### LCE-13  What annual volumes do you expect for each lifecycle type?

- **Why we ask:** Sizes testing and licences.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Number  |  **Use case:** ONB, EXT
- **Response:**

  > _[Type answer here]_

### LCE-14  Which countries have specific rules for onboarding or exit surveys (consultation, consent, restricted data)?

- **Why we ask:** Avoids country-level blocks on go-live.
- **Priority:** P2 - Should answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ONB, EXT
- **Response:**

  > _[Type answer here]_

---

## 7. 360 / Multi-Rater Feedback

*Subjects, evaluators, workflow, competencies, reports and the Qualtrics 360 vs PMGM decision.*

### 360-01 ★  Is 360 in scope for go-live? What is its purpose: development only, leadership assessment, talent-review input, or performance input?

- **Why we ask:** Purpose sets confidentiality, report design and legal review.
- **Priority:** P1 - Must answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 2  |  **Type:** Single choice  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-02 ★  SF PMGM is already live. Does it already run multi-rater or 360 feedback? Which tool will be the system of record for 360 (Qualtrics 360 or PMGM), and what drives the choice?

- **Why we ask:** Avoids two competing 360 processes and duplicated rater fatigue.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Single choice  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-03  Who are the subjects (all managers, senior leaders, high potentials)? How many, and how often (annual, cycle-aligned)?

- **Why we ask:** Sizes licences and workload.
- **Priority:** P1 - Must answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-04 ★  Which workflow model applies: predefined subject-evaluator pairs, subject nominates from a predefined list, or open nomination? Is manager approval of raters required?

- **Why we ask:** These are the standard Qualtrics 360 workflows and each needs different data.
- **Priority:** P1 - Must answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-05  Which rater categories (manager, peers, direct reports, skip-level, customers, external) and what minimum raters per category before results show?

- **Why we ask:** Anonymity depends on minimums.
- **Priority:** P1 - Must answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-06  Should the project run in waves (nominations, evaluations, report release), and how long should each wave last?

- **Why we ask:** Qualtrics recommends waves for 360 projects; durations drive the calendar.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-07 ★  Is there a leadership competency model? How many competencies and items, which rating scale, which open-ended questions, which scoring categories, and which translations?

- **Why we ask:** Question set and scoring categories must be final before build.
- **Priority:** P1 - Must answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-08  How will subject and evaluator data be derived from EC: reporting lines, dotted-line or matrix managers, project teams?

- **Why we ask:** Rater lists are the main data dependency of 360.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-09  What should subject reports contain, and who sees them (subject, manager, HRBP, coach)? Are norm groups or benchmarks needed?

- **Why we ask:** Drives report design and access rules.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 8  |  **Type:** List / table  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-10  How do 360 results flow to development plans (SF Succession & Development, Learning) or stay outside SF?

- **Why we ask:** Defines integration and confidentiality.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-11  Who writes invitation and reminder messages, in which languages, and who coaches subjects on results?

- **Why we ask:** Messaging and coaching drive trust and quality.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-12  Are external evaluators (customers, vendors) or contingent workers included, and how is their data handled?

- **Why we ask:** External participants have different data and access needs.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-13  May 360 results be used in talent, promotion or pay decisions? What do the legal team and employee representatives say?

- **Why we ask:** Use of results changes legal and consultation requirements.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

### 360-14  Which subjects will pilot, and when? What success criteria would let you scale?

- **Why we ask:** A small pilot lowers launch risk.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** 360
- **Response:**

  > _[Type answer here]_

---

## 8. Manager Effectiveness & Action Planning

*Manager dashboards, expectations after results, and closing the loop with action plans.*

### MGR-01  Is manager effectiveness a named use case (upward feedback, manager pulse, manager scorecard)?

- **Why we ask:** Decides content and reporting scope.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Yes / No  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-02 ★  What must managers do after results arrive: required action plans, deadlines, tracking and nudges?

- **Why we ask:** Defines the action-planning module scope.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-03  Do you have manager development content (internal or from Qualtrics) to recommend alongside results? Should it link to SF Learning?

- **Why we ask:** Turns insight into help.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-04 ★  How is a manager defined for reporting (direct reports, full hierarchy roll-up, matrix)? What happens when a manager has fewer reports than the minimum group size?

- **Why we ask:** Small teams are the most common anonymity problem.
- **Priority:** P1 - Must answer  |  **Owner:** People Analytics  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-05 ★  What follow-up applies to low-scoring teams (HRBP involvement, targeted support)?

- **Why we ask:** Defines escalation rules.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-06  Who tracks action-plan completion, and how is it reported to executives?

- **Why we ask:** Accountability for outcomes.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-07  Should action plans link to SF goals, PMGM or development plans?

- **Why we ask:** Decides the return integration to SF.
- **Priority:** P2 - Should answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-08 ★  How many managers need access, and will they use dashboards (SSO) or receive PDFs or emails?

- **Why we ask:** Drives licence, role and SSO design.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 4  |  **Type:** Number  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

### MGR-09  Who will train managers to read results and run team discussions? Are conversation guides needed?

- **Why we ask:** Manager capability decides whether action happens.
- **Priority:** P2 - Should answer  |  **Owner:** Talent & L&D  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** MGR
- **Response:**

  > _[Type answer here]_

---

## 9. Employee Technology Experience

*Measuring the experience of tools and services, including SuccessFactors adoption itself.*

### ETX-01 ★  Is Employee Technology Experience in scope? Which tools and services (laptops, VPN, collaboration, service desk, SuccessFactors itself)?

- **Why we ask:** Decides if IT-side stakeholders join discovery.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 4  |  **Type:** Yes / No  |  **Use case:** ETX
- **Response:**

  > _[Type answer here]_

### ETX-02 ★  Who owns it (CIO, service desk, digital workplace) and is there sponsor and budget?

- **Why we ask:** Needs an owner outside HR.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ETX
- **Response:**

  > _[Type answer here]_

### ETX-03 ★  Which ITSM or ticketing tool is in use (ServiceNow, Jira, other)? Should low scores create tickets?

- **Why we ask:** Closing the loop on IT issues needs integration.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 8  |  **Type:** Single choice  |  **Use case:** ETX
- **Response:**

  > _[Type answer here]_

### ETX-04  What triggers these surveys: ticket closure, device refresh, a new SF release, or a periodic cycle?

- **Why we ask:** Defines event sources.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ETX
- **Response:**

  > _[Type answer here]_

### ETX-05 ★  Do you want to measure employee and manager experience of SuccessFactors itself (EC self-service, PMGM, new modules) right after go-live?

- **Why we ask:** Fast win that also supports adoption.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** Yes / No  |  **Use case:** ETX, PLS
- **Response:**

  > _[Type answer here]_

### ETX-06  Is device, location or application data beyond EC needed for segmentation?

- **Why we ask:** Adds data sources.
- **Priority:** P3 - Nice to have  |  **Owner:** IT / Architecture  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ETX
- **Response:**

  > _[Type answer here]_

### ETX-07  Which technology KPIs are targeted (satisfaction, effort, time-to-resolve)?

- **Why we ask:** Aligns metrics.
- **Priority:** P3 - Nice to have  |  **Owner:** IT / Architecture  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ETX
- **Response:**

  > _[Type answer here]_

---

## 10. Survey Content, Scales & Languages

*Question libraries, rating scales, translations, branding, accessibility and consent text.*

### SUR-01 ★  Which languages are required per use case? What is the source language, translation method (human, machine plus review) and who validates?

- **Why we ask:** Translation lead time can decide the go-live date.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-02 ★  Which rating scales and wording standards must be used (5, 7 or 10 point, agree/disagree, eNPS) to stay comparable with history?

- **Why we ask:** Standardising early avoids rework.
- **Priority:** P1 - Must answer  |  **Owner:** People Analytics  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-03  Which demographic attributes come from SF (hidden metadata) and which are asked? Are any categories restricted in certain countries (gender, ethnicity, age, disability)?

- **Why we ask:** Legal and privacy constraints vary by country.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-04 ★  What privacy notice, consent text and mandatory statements must appear on each survey?

- **Why we ask:** Must be reviewed before build.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-05  What branding is required (logo, colours, tone) and which accessibility standard (for example WCAG) must surveys meet?

- **Why we ask:** Quick to define now and costly later.
- **Priority:** P2 - Should answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-06  What accessibility needs exist (screen readers, low bandwidth, shift workers, kiosks)?

- **Why we ask:** Ensures every employee can respond.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-07  What survey length targets apply, and who signs off on content?

- **Why we ask:** Controls fatigue and approval time.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-08 ★  Will you use Qualtrics best-practice libraries (engagement, onboarding, exit, 360, well-being, candidate) as the baseline, and how much customisation is allowed?

- **Why we ask:** Libraries speed delivery; customisation adds testing and translation.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-09  Which scoring conventions apply (favourable %, mean, top-box)?

- **Why we ask:** Keeps analytics consistent.
- **Priority:** P3 - Nice to have  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUR-10  Would you accept AI-assisted follow-up questions on vague comments (conversational feedback)?

- **Why we ask:** Needs policy approval.
- **Priority:** P3 - Nice to have  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** PLS, ENG
- **Response:**

  > _[Type answer here]_

---

## 11. SuccessFactors Integration & Architecture

*How Employee Central data and events reach Qualtrics, authentication, environments and monitoring.*

### INT-01 ★  Describe the SuccessFactors landscape: instances (test, preview, production), data centre, EC release status, identity provider and SSO.

- **Why we ask:** Foundation for integration and authentication design.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-02 ★  What is the preferred method for sending EC employee data to Qualtrics: pre-packaged SF extension, SFTP file, API or Integration Center, or SAP BTP Integration Suite? Any constraints?

- **Why we ask:** Selects the integration pattern and drives effort.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 2  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-03  Do you have SAP BTP / Integration Suite today? Who has the skills and capacity to build and run the integration?

- **Why we ask:** Capacity is the main schedule risk for integration.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-04 ★  How often must data sync (daily full, daily delta, near real time)? Which fields need near-real-time updates (hire for onboarding, termination for exit)?

- **Why we ask:** Sync frequency decides architecture.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-05  How will EC events (hire, transfer, termination) trigger surveys: SF Intelligent Services events, Integration Center, or scheduled delta files? Is Intelligent Services enabled?

- **Why we ask:** Event triggers are the heart of lifecycle surveys.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ONB, EXT
- **Response:**

  > _[Type answer here]_

### INT-06 ★  Do surveys need to appear inside SF (home page tile, Engagement card, mobile app)? On which SF home page version?

- **Why we ask:** Embedded delivery improves response and adoption.
- **Priority:** P2 - Should answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 8  |  **Type:** Yes / No  |  **Use case:** PLS, ETX
- **Response:**

  > _[Type answer here]_

### INT-07  Should results or action plans flow back to SF (development plans, goals, talent profile) or to a data warehouse (SAC, Datasphere, BW)?

- **Why we ask:** Return flows add scope and security review.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** MGR, RPT
- **Response:**

  > _[Type answer here]_

### INT-08  Which identity standard will be used for employee access (SAML or OIDC, which IdP)? What is the fallback for employees without SSO?

- **Why we ask:** Access design affects frontline reach and security approval.
- **Priority:** P1 - Must answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 2  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-09  How many Qualtrics sandbox and production environments are needed, how often is SF preview refreshed, and what is the policy on test data (anonymised or real)?

- **Why we ask:** Environments and test data decide test quality and compliance.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-10  What API user, OAuth, IP allow-list and permission roles will the integration need, and who approves them?

- **Why we ask:** Integration security approvals take time.
- **Priority:** P1 - Must answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-11  Who monitors failed syncs, how will alerts be raised, and what SLA is expected?

- **Why we ask:** Operational readiness for run.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-12 ★  What architecture-board approvals and change-freeze windows apply in the next four months?

- **Why we ask:** Freeze windows can block deployment.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-13  Is data needed from outside EC (Employee Central Payroll, time tracking, ITSM, other HR systems)?

- **Why we ask:** Extra sources lengthen the build.
- **Priority:** P2 - Should answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-14  Do firewalls or mail filters need allow-listing for Qualtrics survey links? How is email deliverability handled (sender domain, SPF, DKIM)?

- **Why we ask:** Invitations landing in spam is a frequent launch problem.
- **Priority:** P1 - Must answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### INT-15  Do People Analytics or Workforce Analytics pipelines need to consume EX data?

- **Why we ask:** Plans downstream data flows.
- **Priority:** P3 - Nice to have  |  **Owner:** People Analytics  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** RPT
- **Response:**

  > _[Type answer here]_

---

## 12. Employee Data, Hierarchy & Attributes

*Which Employee Central fields drive reporting hierarchies, segmentation, triggers and eligibility.*

### DAT-01 ★  Which EC fields are needed in Qualtrics (person, employment, job, organisation: legal entity, business unit, division, department, location, cost centre, job family, level, manager, position)? Please complete the Data Inventory tab.

- **Why we ask:** The field list is the backbone of hierarchy, triggers and segmentation.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-02 ★  How complete and trusted is EC data (manager, email, location, job level)? Which known gaps exist?

- **Why we ask:** Data quality problems surface as wrong survey populations.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-03 ★  Which organisational structure drives reporting (reporting line or organisation units)? How many levels and units exist?

- **Why we ask:** Determines hierarchy build and dashboard roll-ups.
- **Priority:** P1 - Must answer  |  **Owner:** People Analytics  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-04  How are matrix, dotted-line, concurrent employment, global assignments and secondments handled? Which manager and organisation does each person report under?

- **Why we ask:** These cases create duplicates and wrong roll-ups.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-05  Which demographic attributes exist in EC and are approved for survey analysis (gender, age band, tenure, nationality, and so on)?

- **Why we ask:** Needs privacy and legal approval.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-06 ★  Who is eligible to be surveyed: active, on leave, notice period, contingent, part-time, future hires? What are the exclusion rules?

- **Why we ask:** Eligibility rules define the participant file.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-07  What contact data is available: business email coverage, personal email, mobile number for deskless staff, preferred language?

- **Why we ask:** Without contact data people cannot be invited.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-08  Where should derived attributes (tenure band, age band, span of control) be calculated: EC, middleware or Qualtrics?

- **Why we ask:** Avoids inconsistent definitions.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-09  Is there historical survey data or historical organisation snapshots to load for trend reporting? Format, volume and quality?

- **Why we ask:** Historical loads need mapping effort.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ENG, PLS
- **Response:**

  > _[Type answer here]_

### DAT-10  What retention periods apply per use case? How are leavers' data deletion and erasure requests handled?

- **Why we ask:** Retention rules shape configuration.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-11  Are reorganisations planned between now and go-live, and how will hierarchy changes during a survey window be handled (snapshot or live)?

- **Why we ask:** Mid-survey changes corrupt results.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-12  Which unique identifier will be the key between EC and Qualtrics (person ID, user ID), and how will pseudonymisation be handled?

- **Why we ask:** Key design is hard to change after build.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DAT-13  Are there entities or populations not on EC (acquisitions, joint ventures, contractors)? Should they be included and from which source?

- **Why we ask:** Scope and data source gap.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## 13. Reporting, Dashboards & Analytics (incl. AI)

*Audiences, dashboards, distribution, text analytics, and joining survey data with SF outcomes.*

### RPT-01 ★  Which reporting audiences exist (executives, HRBPs, managers, employees, People Analytics) and what does each need to see?

- **Why we ask:** Defines roles and dashboard scope.
- **Priority:** P1 - Must answer  |  **Owner:** People Analytics  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-02  Which dashboard types are must-have: executive overview, manager dashboard, heat map, driver analysis, comparison, trend?

- **Why we ask:** Controls build effort.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Multi-select  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-03  How will reports be distributed: dashboard login, scheduled email, PDF, embedded in SF?

- **Why we ask:** Affects access model and SSO.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Multi-select  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-04  Who needs live response-rate tracking and at what granularity (without identifying respondents)?

- **Why we ask:** Supports participation management.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-05 ★  Which text analytics and AI summaries (Qualtrics Assist) are in scope, in which languages, and do Legal and employee representatives approve them?

- **Why we ask:** AI on employee comments needs explicit approval.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-06 ★  Will survey data be combined with SF data (turnover, PMGM performance rating, promotion, tenure) for analysis? What safeguards apply?

- **Why we ask:** Joined data is powerful and sensitive.
- **Priority:** P1 - Must answer  |  **Owner:** People Analytics  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ENG, PLS, 360
- **Response:**

  > _[Type answer here]_

### RPT-07  Which internal targets and external benchmarks apply?

- **Why we ask:** Defines reporting comparisons.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ENG
- **Response:**

  > _[Type answer here]_

### RPT-08  Do reports need local-language labels or corporate templates?

- **Why we ask:** Template effort.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-09  Will raw data go to a data warehouse or People Analytics, how often, and who holds access?

- **Why we ask:** Extra export flows.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-10  What accessibility and mobile support is needed for dashboards?

- **Why we ask:** Usability for all managers.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### RPT-11 ★  Which custom metrics (eNPS, engagement index composition, attrition-risk index) need agreed definitions and owners?

- **Why we ask:** Metric definitions must be fixed before dashboards.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## 14. Security, Privacy & Compliance

*Residency, anonymity, consultation, consent, retention, AI governance and vendor security review.*

### SEC-01 ★  Where must employee data be stored and processed? Are there restrictions on cross-border transfer (EU, India, China, Middle East, other)?

- **Why we ask:** Residency drives data-centre choice and legal basis.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-02  Has a DPIA or privacy impact assessment been done or required? Who is the DPO and when must they be consulted?

- **Why we ask:** Often a critical-path item.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-03 ★  Which countries require works council, union or employee representative consultation, and what are the lead times?

- **Why we ask:** Consultation can delay go-live by weeks or months.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-04 ★  What anonymity commitments apply: minimum group size, suppression of small groups, comment redaction, and who approves exceptions?

- **Why we ask:** Anonymity breaches destroy trust.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-05  What is the legal basis (legitimate interest or consent) and the required privacy notice wording for each country?

- **Why we ask:** Needed before the first invitation.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-06  Which EC attributes are classified sensitive or restricted? Are any prohibited from leaving EC?

- **Why we ask:** Sets the data mapping scope.
- **Priority:** P1 - Must answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-07  What SSO, MFA, session, admin-access and IP-restriction policies apply?

- **Why we ask:** Security configuration to design up front.
- **Priority:** P1 - Must answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-08 ★  What security evidence is required from the vendor (certifications, pen-test reports, sub-processor list)? Where does the review stand?

- **Why we ask:** Vendor review can gate access to real data.
- **Priority:** P1 - Must answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-09  How are data subject access requests involving survey data handled?

- **Why we ask:** Needs a process before go-live.
- **Priority:** P2 - Should answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-10  What is your protocol for sensitive disclosures in comments (harassment, safety, wellbeing risk): duty of care, escalation path, limits of anonymity?

- **Why we ask:** Legal duty may override anonymity.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-11  What audit logging is required (who accessed which results) and how will logs be exported?

- **Why we ask:** Compliance evidence.
- **Priority:** P2 - Should answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SEC-12  Has Legal assessed AI-based analysis of employee data (sentiment, attrition prediction) under internal AI policy and applicable regulation, including EU AI Act treatment of employment-related AI?

- **Why we ask:** AI governance rules for employee data are evolving.
- **Priority:** P1 - Must answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** RPT
- **Response:**

  > _[Type answer here]_

---

## 15. Roles, Access & Governance

*Administrator model, role design by hierarchy, approvals, segregation of duties and support.*

### ROL-01 ★  Who will be Brand Administrators and who will be EX project administrators? Brand Administrators have full platform access including the directory; Employee Insights Administrators can build projects but cannot access the directory or admin page.

- **Why we ask:** Admin separation is a core design choice in Qualtrics EX.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### ROL-02 ★  Define viewer roles (executives, HRBPs, managers, regional HR, employee representatives) and map each to hierarchy-based access.

- **Why we ask:** Hierarchy-based access is the basis of dashboards.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### ROL-03 ★  Who can create and launch surveys, approve content and release results? What approval chain and SLA apply?

- **Why we ask:** Prevents bottlenecks and rogue surveys.
- **Priority:** P1 - Must answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### ROL-04  Who may see raw comments or respondent-level data? What segregation of duties applies between administrators, HRBPs and IT?

- **Why we ask:** Protects confidentiality.
- **Priority:** P1 - Must answer  |  **Owner:** Security & Privacy  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### ROL-05  Will joiner-mover-leaver access be automated from SF roles or managed manually?

- **Why we ask:** Access hygiene at scale.
- **Priority:** P2 - Should answer  |  **Owner:** IT / Architecture  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### ROL-06 ★  Which governance body oversees EX (steering committee, content council, privacy officer)? How often does it meet?

- **Why we ask:** Someone must own decisions after go-live.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### ROL-07  What support model is expected (employee help, administrators, vendor) and in which languages and hours?

- **Why we ask:** Prepares for go-live volume.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### ROL-08  How will changes to surveys and participant data after launch be documented and audited?

- **Why we ask:** Change control.
- **Priority:** P2 - Should answer  |  **Owner:** Security & Privacy  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## 16. Communications, Change & Adoption

*Invitations, sender, trust messaging, manager toolkits, training and closing the loop.*

### CMM-01 ★  Who sends invitations (executive, HR, manager), from which sender name and email domain, over which channels?

- **Why we ask:** Sender trust drives response rates.
- **Priority:** P1 - Must answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-02 ★  Is Internal Communications engaged, and which channels exist (intranet, Teams, town halls, posters for frontline staff)?

- **Why we ask:** Comms lead times are long.
- **Priority:** P1 - Must answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-03  What employee-facing FAQ and privacy message will explain what happens to results?

- **Why we ask:** Trust drives honest answers.
- **Priority:** P1 - Must answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-04  What reminder cadence and tone are planned, and will managers receive response-rate nudges?

- **Why we ask:** Participation levers.
- **Priority:** P2 - Should answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-05  What toolkit will managers receive to explain the survey and discuss results?

- **Why we ask:** Manager confidence affects outcomes.
- **Priority:** P2 - Should answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ENG, MGR
- **Response:**

  > _[Type answer here]_

### CMM-06 ★  How and when will you communicate what changed as a result (you said, we did), and who owns it?

- **Why we ask:** Without visible action, response rates decay.
- **Priority:** P1 - Must answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-07  What changes for HR, managers and employees, who might resist, and what training is needed?

- **Why we ask:** Shapes the change plan.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-08  What training is planned for administrators, HRBPs and managers (formats, lead times)?

- **Why we ask:** Training must complete before launch.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-09 ★  Which other surveys, campaigns or SuccessFactors go-live communications run in the same period, and how will they be coordinated?

- **Why we ask:** Clashing campaigns reduce participation.
- **Priority:** P1 - Must answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### CMM-10  What local-language adaptation is needed for communications by country?

- **Why we ask:** Communication scope.
- **Priority:** P2 - Should answer  |  **Owner:** Internal Communications  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## 17. Upcoming SuccessFactors Modules & Sequencing

*How other modules going live in the same window affect triggers, data, testing and calendars.*

### UPC-01 ★  Which SuccessFactors modules go live in the next 3-4 months (for example Recruiting, Onboarding, Learning, Succession & Development, Compensation, Time, Payroll) and what are their dates? Please complete the SF Module Readiness tab.

- **Why we ask:** Module dates drive trigger availability and test windows.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### UPC-02  For each module, does an EX use case need its data (onboarding task completion, course completion, requisition stages)? Is a manual or file-based interim acceptable?

- **Why we ask:** Separates hard dependencies from nice-to-haves.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### UPC-03 ★  Can EX requirements be fed into the design workshops of those other modules now (fields, event reasons, status codes)?

- **Why we ask:** Cheap now, expensive later.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### UPC-04 ★  Which EC configuration changes are planned (new fields, org restructure, position management, event reasons) that would affect the EX data feed?

- **Why we ask:** Mid-build data model changes break integrations.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### UPC-05  How will SuccessFactors half-yearly releases be handled, and what test windows apply?

- **Why we ask:** Release regression is a known risk.
- **Priority:** P2 - Should answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### UPC-06  Is the same partner implementing the other modules and Qualtrics? Where does resource overlap?

- **Why we ask:** Shared people cause conflicts.
- **Priority:** P2 - Should answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### UPC-07  When do other modules cut over and hold hypercare, and how does that collide with EX testing and pilot?

- **Why we ask:** Avoids testing during SF cutovers.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### UPC-08  Is Workforce Analytics or SAC planned and should it consume EX data?

- **Why we ask:** Plans downstream use.
- **Priority:** P3 - Nice to have  |  **Owner:** People Analytics  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** RPT
- **Response:**

  > _[Type answer here]_

### UPC-09 ★  What is the PMGM cycle calendar (goals, reviews, calibration)? Which PMGM data (ratings, goals) may be used with survey data?

- **Why we ask:** Avoids collisions and clarifies permitted data use.
- **Priority:** P1 - Must answer  |  **Owner:** HRIS / SuccessFactors Lead  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** 360, ENG, PLS
- **Response:**

  > _[Type answer here]_

### UPC-10  Are further EC rollout waves planned (new countries or entities) that will expand the EX population?

- **Why we ask:** Scalability planning.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## 18. Delivery, Timeline, Testing & Support

*Phases, team, environments, pilot, go-live approach, hypercare and acceptance.*

### DEL-01 ★  What phases and milestones are expected (design, build, test, pilot, go-live, hypercare)? Review the proposed 16-week plan on the Timeline & Risks tab.

- **Why we ask:** Aligns on the critical path.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-02 ★  Who is on the project team (business, HRIS, IT, security, comms) with what percentage allocation, and who is the day-to-day decision maker?

- **Why we ask:** Named capacity beats intentions.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-03  What testing approach applies: UAT participants, test cases, test data and sign-off criteria?

- **Why we ask:** Defines quality gates.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-04 ★  Which population and use case will pilot, at what size, and what success criteria would trigger full launch?

- **Why we ask:** A pilot lowers launch risk.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-05  Is go-live big-bang or phased (by use case or country)? What are the rollback criteria?

- **Why we ask:** Phasing is the best lever in a short window.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 4  |  **Type:** Single choice  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-06 ★  How long is hypercare, and how will knowledge transfer to the run team work?

- **Why we ask:** Support continuity.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-07  Which blackout dates and holidays (year-end, festivals, fiscal close) will remove key people over the next four months?

- **Why we ask:** Holiday periods can remove one to two weeks of capacity.
- **Priority:** P1 - Must answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-08  Which assumptions and dependencies does the client already see (licences, access, security review)?

- **Why we ask:** Surfaces risks early.
- **Priority:** P2 - Should answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-09  What are the top risks the client perceives and what mitigation is already considered?

- **Why we ask:** Seeds the risk register.
- **Priority:** P2 - Should answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-10  What project governance applies (weekly cadence, steering committee, escalation path, RAID log tool)?

- **Why we ask:** Operating rhythm.
- **Priority:** P2 - Should answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-11  Which deliverables are expected (design document, integration specification, test results, admin guide, training)?

- **Why we ask:** Scope of documentation.
- **Priority:** P2 - Should answer  |  **Owner:** Project / PMO  |  **Needed by:** Week 4  |  **Type:** Multi-select  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### DEL-12  What are the acceptance criteria for go-live?

- **Why we ask:** Prevents scope disputes.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## 19. Success Measures & Operating Model

*KPIs, baselines, business case, run model and the roadmap after go-live.*

### SUC-01 ★  Which three to five KPIs define success at 6 and 12 months (participation, eNPS, onboarding satisfaction, regretted attrition, action-plan completion)?

- **Why we ask:** Success definition guides trade-offs.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUC-02 ★  What baselines exist today for those KPIs?

- **Why we ask:** Without baselines benefits cannot be shown.
- **Priority:** P2 - Should answer  |  **Owner:** People Analytics  |  **Needed by:** Week 4  |  **Type:** List / table  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUC-03 ★  What business case or ROI has been promised internally, and who owns benefits tracking?

- **Why we ask:** Defines accountability.
- **Priority:** P1 - Must answer  |  **Owner:** Executive Sponsor  |  **Needed by:** Week 2  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUC-04 ★  What will the operating model look like after go-live: run-team size, skills, annual programme calendar, centre of excellence?

- **Why we ask:** Sustainable operation.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Week 8  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUC-05  How will content and adoption be reviewed quarterly, and who approves new use cases?

- **Why we ask:** Continuous improvement.
- **Priority:** P2 - Should answer  |  **Owner:** HR / People Leadership  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUC-06  What scale-up is expected in 12-24 months (countries, subsidiaries, populations)?

- **Why we ask:** Informs design headroom.
- **Priority:** P3 - Nice to have  |  **Owner:** HR / People Leadership  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUC-07  What executive reporting cadence on EX outcomes is expected?

- **Why we ask:** Governance rhythm.
- **Priority:** P3 - Nice to have  |  **Owner:** Executive Sponsor  |  **Needed by:** Post go-live  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

### SUC-08 ★  What policy governs use of results in performance, promotion or pay decisions?

- **Why we ask:** Prevents misuse and mistrust.
- **Priority:** P2 - Should answer  |  **Owner:** Legal / DPO / Employee Relations  |  **Needed by:** Week 4  |  **Type:** Free text  |  **Use case:** ALL
- **Response:**

  > _[Type answer here]_

---

## Appendices

### A. SuccessFactors module readiness

| Module | Status | EX relevance | Qualtrics touchpoint | Data / trigger | Question to confirm | Planned go-live |
|---|---|---|---|---|---|---|
| Employee Central (core HR) | Live | Primary data source for every EX use case | Employee directory, hierarchy, lifecycle triggers | Person, employment, job, organisation, manager, events | Which EC changes are planned before go-live? |  |
| Performance & Goals (PMGM) | Live | 360 overlap; post-review pulse; link to ratings | 360 decision, review-cycle calendar, optional rating joins | Cycle dates, form templates, multi-rater use, ratings | Does PMGM already run multi-rater feedback, and which tool will own 360? |  |
| Continuous Performance Management | To confirm | Check-in and feedback pulses | Manager conversation pulses | Activity events | Is CPM in use or planned? |  |
| Recruiting Management | Planned - confirm date | Candidate experience | Stage-triggered candidate surveys | Requisition, application stage, applicant contact | Go-live date and applicant-privacy constraints? |  |
| Recruiting Marketing / CRM | To confirm | Employer brand and candidate funnel | Candidate pulse (optional) | Career site events | In scope? |  |
| Onboarding | Planned - confirm date | Onboarding experience | Day-1 / 30 / 90 surveys, task-based triggers | Hire event, tasks, buddy, manager | Go-live date; is a manual trigger acceptable at launch? |  |
| Offboarding (EC) | To confirm | Exit experience | Pre-exit and exit surveys | Termination event, last day, reason code | Is offboarding configured and reliable? |  |
| Learning | Planned - confirm date | Learning experience; manager development follow-up | Course-completion pulse; link from action plans | Course completions | Go-live date; integration expectations? |  |
| Succession & Development | Planned - confirm date | 360 results into development plans | Development plan linkage | Talent profile, development goals | Should 360 results flow here or stay confidential? |  |
| Compensation | Planned - confirm date | Pay perception (survey content only) | None required | None | Any rule against linking pay data to survey data? |  |
| Employee Central Payroll | To confirm | Pay-cycle blackout dates | Calendar only | Payroll calendar | Avoid surveys in payroll-close windows? |  |
| Time Management / Time Tracking | To confirm | Work-pattern segmentation (optional) | Optional attributes | Work schedule | Needed for segmentation? |  |
| Employee Central Service Center | To confirm | Case closure survey | Post-case satisfaction survey | Case closure event | In scope? |  |
| Workforce Analytics / People Analytics | To confirm | Joint analysis of survey and HR data | Data export or SAC integration | Turnover, headcount metrics | Who consumes EX data? |  |
| Home page / mobile app | To confirm | Embedded survey delivery | Engagement card or tile | Home page version | Which home page version and mobile app? |  |
| SF Intelligent Services / Integration Center | To confirm | Event-driven triggers | Lifecycle event feed | Hire, transfer and termination events | Are these enabled and who maintains them? |  |

### B. Employee Central data inventory

Typical EC data areas are indicative. Confirm real field names with your HRIS lead. Do not send government ID or bank details.

| Attribute | EC area | Purpose | Sensitivity | Needed for | Available? | Quality 1-5 | Approved? |
|---|---|---|---|---|---|---|---|
| Person ID / User ID | Person information | Key / identifier | Medium | All |  |  |  |
| First and last name | Personal information | Contact / display | Medium | All |  |  |  |
| Business email | Email information | Contact | Medium | All |  |  |  |
| Personal email | Email information | Contact (leavers, deskless) | High | Exit, Onboarding, Candidate |  |  |  |
| Mobile number | Phone information | Contact (SMS) | High | Pulse, Deskless |  |  |  |
| Preferred language | Personal information | Survey language | Low | All |  |  |  |
| Hire date / original start date | Employment information | Lifecycle trigger | Low | Onboarding, Engagement tenure |  |  |  |
| Termination date | Employment information | Lifecycle trigger | Medium | Exit |  |  |  |
| Event / event reason | Job information | Trigger and eligibility filter | Low | Onboarding, Exit, Moves |  |  |  |
| Employment status | Job information | Eligibility | Low | All |  |  |  |
| Employee class / worker type | Job information | Eligibility and segmentation | Low | All |  |  |  |
| Full-time / part-time, FTE | Job information | Segmentation | Low | Engagement |  |  |  |
| Legal entity / company | Job information | Hierarchy | Low | All |  |  |  |
| Business unit / division / department | Job information | Hierarchy | Low | All |  |  |  |
| Cost centre | Job information | Hierarchy (optional) | Low | Engagement |  |  |  |
| Location / country | Job information | Hierarchy and legal rules | Low | All |  |  |  |
| Job code / title | Job information | Segmentation | Low | Engagement |  |  |  |
| Job family / function | Job information | Segmentation | Low | Engagement |  |  |  |
| Job level / grade | Job information | Segmentation | Low | Engagement, 360 |  |  |  |
| Position ID | Position management | Hierarchy | Low | All |  |  |  |
| Manager ID | Job information | Reporting hierarchy | Low | All |  |  |  |
| Dotted-line / matrix manager | Job relationships | 360 raters, matrix reporting | Low | 360, Engagement |  |  |  |
| HR business partner | Job relationships | Access roles | Low | All |  |  |  |
| Date of birth (age band only) | Personal information | Demographic segmentation | High | Engagement (if permitted) |  |  |  |
| Gender | Personal information | Demographic segmentation | High | Engagement, Inclusion (if permitted) |  |  |  |
| Nationality | Personal information | Demographic segmentation | High | Inclusion (if permitted) |  |  |  |
| Work arrangement (remote / hybrid / on-site) | Job or custom field | Segmentation | Low | Engagement, Pulse |  |  |  |
| Last promotion / transfer date | Job history | Segmentation, moves trigger | Low | Moves, Engagement |  |  |  |
| Performance rating (PMGM) | Performance form | Analysis only (restricted) | High | Engagement analysis |  |  |  |
| Leave start / return date | Time off or employment | Return-from-leave trigger | Medium | Moves |  |  |  |

### C. Illustrative 16-week plan

Assumes project start Monday 2 November 2026 and go-live in weeks 14-15. Year-end holidays often remove one to two weeks of capacity.

| Phase | Weeks | Key activities |
|---|---|---|
| Mobilise & discover | 1-2 | Kick-off, questionnaire issued and walked through, stakeholder interviews, licence and tenant confirmed, security and legal review started |
| Design | 3-5 | Use-case scope confirmed, hierarchy and data mapping, integration design, roles and anonymity rules, survey content and translations started |
| Build & integrate | 5-10 | Directory and integration build, project configuration, dashboards, roles, messages, translations loaded |
| Test & pilot | 10-13 | Integration test, UAT, privacy and accessibility checks, pilot with a small population |
| Go-live preparation | 12-14 | Communications, manager toolkit, training, support model, cutover plan |
| Go-live | 14-15 | Launch Wave 1 use cases; monitor syncs and participation |
| Hypercare & handover | 15-16 | Daily monitoring, fixes, knowledge transfer, Wave 2 planning |

### D. Risk register (starting estimates)

| Risk | Likelihood | Impact | Score | Mitigation | Owner |
|---|---|---|---|---|---|
| Vendor security, privacy or DPIA review runs past the build start | 4 | 5 | 20 | Start reviews in week 1; share Qualtrics security pack early; build on test data in the meantime | Security & Privacy |
| Works council or union consultation required in one or more countries | 3 | 5 | 15 | Identify countries in week 2; launch in unaffected countries first; prepare consultation pack | Legal / Employee Relations |
| Other SF modules go live in the same window and consume the same people | 4 | 4 | 16 | Agree a single resource plan and change calendar; avoid EX testing during cutovers | PMO |
| EC data quality (manager, email, location) creates wrong survey populations | 4 | 4 | 16 | Run a data-quality profile in weeks 2-3; fix at source; add exception reports | HRIS |
| Integration capacity (BTP or API skills) is not available | 3 | 4 | 12 | Confirm the build owner in week 2; fall back to SFTP file feed for Wave 1 | IT |
| Lifecycle triggers depend on modules that are not yet live | 4 | 3 | 12 | Use EC hire and termination events; manual or file triggers for the rest; defer candidate use case | HRIS |
| Translation and legal text approval delays survey content | 3 | 4 | 12 | Freeze source content by week 5; start translation by week 6; limit launch languages | HR |
| Anonymity thresholds not met for small teams | 4 | 3 | 12 | Agree minimum group size and roll-up rules in design; test with real hierarchy | People Analytics |
| Holiday and year-end periods remove key people for one to two weeks | 4 | 3 | 12 | Plan around regional calendars; book UAT and pilot slots early | PMO |
| 360 overlaps with PMGM multi-rater and creates two processes | 3 | 3 | 9 | Decide the system of record in week 2; start with one population | Talent & L&D |
| Employee trust is low and participation falls short | 3 | 4 | 12 | Early comms, clear anonymity message, visible leader sponsorship, you-said-we-did plan | Internal Communications |
| Invitation emails blocked or filtered | 3 | 3 | 9 | Allow-list sender and domain; test deliverability in UAT; use multiple channels | IT |
| Scope grows beyond the minimum viable launch | 4 | 3 | 12 | Hold a Wave 1 / Phase 2 line; change control through the steering committee | Executive Sponsor |
| AI features not approved by Legal or employee representatives | 2 | 3 | 6 | Raise in week 2; go live without AI summaries if needed | Legal |

### E. Stakeholders and respondents

| Role | Why needed | Involvement | Name | Email |
|---|---|---|---|---|
| Executive Sponsor | Owns scope, budget and date decisions | Weeks 1-16 |  |  |
| CHRO / Head of People | Business owner of EX outcomes | Weeks 1-16 |  |  |
| HRIS / SuccessFactors Lead | EC data, triggers, module calendar | Weeks 1-16 |  |  |
| People Analytics Lead | Hierarchy, anonymity, reporting design | Weeks 2-16 |  |  |
| Talent & L&D Lead | 360, manager development, competencies | Weeks 2-14 |  |  |
| Talent Acquisition Lead | Onboarding and candidate experience | Weeks 2-12 |  |  |
| IT / Integration Architect | Integration, SSO, environments | Weeks 1-16 |  |  |
| Information Security Lead | Vendor review, access, API security | Weeks 1-12 |  |  |
| Data Protection Officer / Legal | DPIA, consent, retention, AI policy | Weeks 1-12 |  |  |
| Employee Relations / Works Council liaison | Consultation and country rules | Weeks 1-10 |  |  |
| Internal Communications Lead | Invitations, trust messaging, FAQ | Weeks 4-16 |  |  |
| Procurement / Finance | Contract, licences, budget | Weeks 1-6 |  |  |
| SF Implementation Partner PM | Cross-module sequencing | Weeks 1-16 |  |  |
| SAP / Qualtrics Solution Architect | Product and integration guidance | Weeks 1-12 |  |  |
| HRBP Representatives | Dashboard users, pilot | Weeks 8-16 |  |  |
| Pilot Managers | Pilot, feedback on toolkit | Weeks 10-14 |  |  |

### F. Sources

- [Qualtrics Support: Step 1, Getting Ready to Launch Your 360 Project](https://www.qualtrics.com/support/employee-experience/getting-started-employee-experience/360-onboarding/form-building/)
- [Qualtrics and SAP announce new partnership (SAP Endorsed Apps), Jan 2025](https://www.qualtrics.com/articles/news/qualtrics-and-sap-announce-new-partnership-to-help-organizations-deliver-great-employee-experiences/)
- [SAP Store: Qualtrics XM for Employee Experience](https://www.sap.com/uk/products/hcm/partners/qualtrics-llc-qualtrics-employee-experience.html)
- [SAP User Groups: Qualtrics / SuccessFactors integration roadmap (archived deck)](https://assets.dm.ux.sap.com/webinars/sap-user-groups-k4u/pdfs/191212_qualtrics_successfactors_roadmap.pdf)
- [TechTarget: What capabilities does Qualtrics EmployeeXM offer?](https://www.techtarget.com/enterprise-software/answer/What-capabilities-does-Qualtrics-EmployeeXM-offer)

*Use-case fit, plan and risk ratings are our own judgement, not vendor statements.*