# OmniVerse Energy — Enterprise Architecture, SAP Signavio, SAP LeanIX and Clean Core

## Demo 02 of the BTM11 Energy Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Energy (ENE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniverse-case-baseline-sap-nextgen-architecture.md) · **Next in series (written for all 11 sectors):** [Demo 03 AI/GenAI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md)

> **Evidence boundary:** OmniVerse Energy Ltd. is an **aspirational case study**. This file is an architecture design and teaching demonstration. It is **not** a record of a client implementation. No executed Signavio model, LeanIX inventory, sync run, Clean Core check or realized benefit is asserted. The case source contains almost no SAP landscape detail, so application names, fact sheets, process codes and requirements below are **synthetic placeholders** (prefix `ENE-SYN`) and are labelled as new design. Product names are learning examples, not confirmed OmniVerse implementations.

---

## 1. The question this file answers

> *Enterprise architecture experience across SAP Signavio, SAP LeanIX and Clean Core.*

**What this file shows:** how an architect turns a board-level transformation case into (1) a capability and value-stream model, (2) a governed application and technology inventory, (3) a process model linked to that inventory, and (4) a Clean Core rule that decides how every requirement is allowed to extend SAP. It ends with a detailed action plan.

**What it does not show:** a delivered engagement. Real project experience is described separately by the presenter and should not be inferred from this file.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Enterprise | OmniVerse Energy Ltd., aspirational case study; USD 85B revenue; 68,000 employees; 42 countries |
| Business mix | Upstream 35%; refining and petrochemicals 28%; retail and marketing 18%; power 12%; renewables 7% |
| Assets | 8 refineries; 25,000 km pipelines; 12,500 retail sites; 15 GW generation; 5 GW operating renewables |
| Burning platform | Disconnected operational data, reactive maintenance, inconsistent customer journeys, fragmented ESG reporting, technology silos |
| Strategic options | Local pilots; central platform first; **federated value-stream delivery with shared standards** (provisional recommendation) |
| Budget | USD 900M over three years (illustrative, not validated) |

**What the source gives for this demo (Theme C):**

| Source ID | Content (source) | Source deliverable |
|---|---|---|
| OVE-M09 Business capability architecture | Maturity gaps: asset management L2 to L4; supply chain L2 to L4; customer engagement L1 to L4; trading and risk L2 to L4; ESG reporting L1 to L4. The scale definition is illustrative | Capability map, maturity heatmap, owner register |
| OVE-M10 Value streams and process architecture | Chain Explore, Extract, Refine, Transport, Distribute, Retail, Customer; power and renewables Generate, Dispatch, Serve; transformation streams Resource-to-Energy, Asset-to-Reliability, Customer-to-Service, Insight-to-Decision | Value-stream maps, stage-capability matrices, process taxonomy |
| OVE-M11 Target operating model | Cross-functional squads (customer experience, asset performance, energy trading, sustainability); central guardrails, federated delivery, explicit plant authority | TOM, decision rights, RACI, product ownership |
| OVE-M12 Enterprise architecture and digital enablement | TOGAF-aligned vision and data, application, technology views; Customer, Asset, Product, Supplier 360; stewardship; event/API integration; hybrid cloud; edge OT; zero trust; governed AI. Vendor names in source are examples, not selected products | Conceptual target architecture, information map, application portfolio, trust boundaries |

**Source aspirational stakeholder challenge (each M-section):** *What evidence is missing, which persona can authorize the decision, what constraints apply, and how will value be measured?*

**Source resolution categories** (from the enterprise source register, Cloud ALM gap-capture section): Configuration; Enhancement (BAdI / Key User Extensibility); Side-by-Side Extension (BTP); Custom Development (Private Edition only); Process Change; Third-Party Solution; Deferred. Note that the source table was written in a SuccessFactors Employee Central implementation context. This demo **extends** it to a broader architecture and says so.

## 3. Source versus new design

| Element | Status |
|---|---|
| Capability gaps, value streams, TOM statements, M12 perspectives, resolution categories, personas | **Source** |
| Capability-to-owner register, process taxonomy codes, synthetic applications and fact sheets, LeanIX and Signavio data model, Clean Core admission rule, synthetic requirements, tests, action plan | **New design (illustrative)** |
| Any SAP product behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What minimum common architecture model and extension rule does OmniVerse need so that federated value-stream teams can deliver independently without creating disconnected pilots and brittle interfaces?

**Scope of this demo:** two of the four source transformation streams, chosen because the source hero story and burning platform point at them: **Asset-to-Reliability** (reactive maintenance, a refinery reliability alert) and **Customer-to-Service** (inconsistent customer journeys). The other streams reuse the same method.

**Accountable decision owner (proposed):** the CDIO (OVE-P05) with architecture assurance from the Director of Enterprise Architecture (OVE-P12). The CEO (OVE-P02) will not approve a technology-first transformation, so every artefact below must tie to a customer, employee or asset outcome.

## 5. Personas and proposed decision rights

IDs, names and roles come from the case persona cards. Decision rights are **proposed** and need discovery validation.

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVE-P05 | Rajiv Kapoor, CDIO | Owns the minimum common platform decision; challenges disconnected pilots and brittle interfaces |
| OVE-P12 | Hannah Fischer, Director of Enterprise Architecture | Owns standards, the Clean Core admission rule and architecture review |
| OVE-P13 | Omar Haddad, CISO | Security and trust-boundary approval for any extension or integration |
| OVE-P16 | Dr. Leila Haddad, Head of Data Governance and AI | Owns data object definitions and stewardship in the inventory |
| OVE-P09 | Carlos Mendes, VP Asset Reliability and Maintenance | Business owner for the Asset-to-Reliability capability and process models |
| OVE-P10 | Grace Okafor, Chief Customer and Retail Officer | Business owner for Customer-to-Service |
| OVE-P04 | Farah Al-Hassan, COO | Veto on anything that risks plant operations during integration |
| OVE-P14 | Meera Iyer, Refinery Operations Manager, Mumbai | Frontline reality check on process models |
| OVE-P02 | Dr. Asha Menon, CEO | Sponsor; outcome test for every decision |

Shared first names across cases do not establish shared identity. Source: [OmniVerse persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md).

## 6. How the toolchain divides the work

This is the method the demo teaches. Tool roles are described from SAP's public documentation (reviewed 2026-11-10).

| Tool | Role in this design | Source of truth for |
|---|---|---|
| SAP LeanIX | Enterprise architecture inventory: business capabilities, applications, IT components, data objects, organizations, lifecycle, ownership | Applications, business capabilities, organizations, data objects (SAP documentation recommends LeanIX as source of truth for these) |
| SAP Signavio | Process modelling and process navigation; value chains, process diagrams, dictionary/glossary | Process models and diagrams |
| SAP Cloud ALM | Implementation project, scope, requirements, tests, deployment tracking | Delivery records and requirement trace |
| Clean Core guardrail (this design) | Admission rule for every extension | The extension decision record |

**Documented LeanIX to Signavio integration behaviour (verify before relying on it):** processes sync from Signavio to LeanIX only (process diagrams, navigation maps and value chains become business-context fact sheets, with diagram links on the fact sheet). Applications, business capabilities and organizations sync **in both directions** against Signavio dictionary items, and you choose the source and target per mapping. The process hierarchy can be mapped top-down, bottom-up or by a list of Signavio directories. Fact sheets with matching names are linked; otherwise new ones are created. The setup needs a dedicated Signavio user with read and write permission (an API edition licence is recommended), the tenant ID, and a manual or scheduled sync run.

**Consequence for design:** agree one owner per object type **before** the first sync, otherwise two teams can rename the same capability in two tools (tabletop test T2).

## 7. Capability architecture (OVE-M09 extended)

The five source gaps become a register. The owner column is proposed; the evidence column is empty on purpose, because the source gives no baseline.

| Capability (source) | Source gap | Proposed business owner | Proposed data steward | Evidence needed before scoring | Stream touched |
|---|---|---|---|---|---|
| Asset management | L2 to L4 | OVE-P09 Carlos Mendes | OVE-P16 Dr. Leila Haddad | Definition of L2 and L4 on one page; current asset-data quality sample | Asset-to-Reliability |
| Supply chain | L2 to L4 | OVE-P11 Wei Zhang | OVE-P16 | Supplier master ownership; material genealogy gaps | Resource-to-Energy |
| Customer engagement | L1 to L4 | OVE-P10 Grace Okafor | OVE-P16 | Customer journey inventory; consent and identity ownership | Customer-to-Service |
| Trading and risk | L2 to L4 | To be confirmed (no matching persona in source) | To be confirmed | Decision-rights discovery | Insight-to-Decision |
| ESG reporting | L1 to L4 | OVE-P06 Leena Fernandes | OVE-P16 | Emissions data lineage; audit requirements | Insight-to-Decision |

**Rule:** a maturity level is not scored until the scale is written down and an evidence sample exists. The scale in the source is illustrative.

## 8. Value streams and process taxonomy (OVE-M10 extended, new design)

Synthetic taxonomy for the two scoped streams. Codes are placeholders, not SAP Scope Item IDs, and must not be presented as such.

| Level | Asset-to-Reliability (`ENE-SYN-A2R`) | Customer-to-Service (`ENE-SYN-C2S`) |
|---|---|---|
| L1 value stream | Asset-to-Reliability | Customer-to-Service |
| L2 stages | Detect condition, Assess risk, Plan work, Execute work, Verify and learn | Identify customer, Capture request, Resolve, Communicate, Learn |
| L3 processes (examples) | Raise a condition alert; Review alert with operations; Plan shutdown window; Issue and close work order; Record failure cause | Verify identity and consent; Log a service request; Route to owner; Send status update; Close and confirm |
| Control points | Plant authority approves any change to a live asset; safety review before shutdown plan | Consent respected; one status shown across channels |
| Systems of record (to be mapped) | Asset, work-order, condition-monitoring sources | Customer, order, service sources |

**Deliverable pattern:** one Signavio value chain per stream; process diagrams to L3 for the first two or three processes only; each diagram linked to a capability and an owner.

## 9. Application and technology portfolio (OVE-M12 extended, synthetic)

The source names no applications. The rows below are **roles**, not products, so nobody mistakes them for a real inventory.

| Fact sheet (synthetic) | Type | Supports capability | Owner (proposed) | Lifecycle | Disposition (proposed, TIME-style) | Evidence needed |
|---|---|---|---|---|---|---|
| ENE-SYN-APP-01 Enterprise asset and work-order application | Application | Asset management | OVE-P09 | Unknown | To be decided | Contract, version, interface list |
| ENE-SYN-APP-02 Condition-monitoring and alert service | Application | Asset management | OVE-P09 with OVE-P14 | Unknown | To be decided | OT boundary and data flow |
| ENE-SYN-APP-03 Customer service case application | Application | Customer engagement | OVE-P10 | Unknown | To be decided | Channel coverage, consent handling |
| ENE-SYN-APP-04 Customer identity and consent store | Application | Customer engagement | OVE-P16 | Unknown | To be decided | Master data ownership |
| ENE-SYN-APP-05 Integration and event layer | IT component | All | OVE-P05 | Unknown | To be decided | Existing integration catalogue |
| ENE-SYN-APP-06 Emissions data collection | Application | ESG reporting | OVE-P06 | Unknown | To be decided | Lineage and audit trail |

**Disposition values stay "to be decided"** until lifecycle, cost and fit evidence exists. Do not present a disposition as a finding.

**Fact sheet minimum attributes (new design):** name; type; description; business owner; technical owner; lifecycle phase and dates; data classification; hosting; interfaces in and out; supported capabilities; supported processes; criticality; last review date; source of record. A fact sheet without an owner and a review date is not counted as governed.

**Relations to model:** capability to application; application to process (via Signavio link); application to data object; application to IT component; application to interface; organization to capability.

## 10. Clean Core admission rule (new design on a verified SAP concept)

**Verified concept (SAP News, August 2025; reviewed 2026-11-10):** SAP describes a Clean Core level concept that sorts extensions into four levels by architectural integrity and upgrade safety.

| Level | SAP description (summarised) | Design use |
|---|---|---|
| A | Fully compliant: only publicly released, stable SAP interfaces, backed by stability contracts. Side-by-side on SAP BTP; on-stack through the ABAP Cloud model with released APIs | Default admission |
| B | Compliant: may use classic APIs that are documented and generally upgrade-stable | Allowed with owner approval |
| C | Partially compliant: accesses SAP internal objects; higher upgrade risk | Exception only, with expiry and named owner |
| D | Not recommended: modifications, writes to SAP tables, implicit enhancements; highest risk and technical debt | Rejected by default; needs an architecture exception at CDIO level |

**Applicability warning:** the level concept is described in the context of SAP S/4HANA; confirm which levels, tooling and wording apply to the actual product and edition before using it with a real client. This case does not state that OmniVerse runs S/4HANA.

**Mapping the source resolution categories to levels (proposed):**

| Resolution category (source) | Typical Clean Core level | Admission question |
|---|---|---|
| Configuration | Not an extension | Is the outcome achievable and documented in standard settings? |
| Enhancement (key-user or released extension point) | Level A if only released mechanisms are used | Is the extension mechanism released for the actual product? |
| Side-by-Side Extension (BTP) | Level A if only released APIs and events are used | Are APIs and events released, security and lifecycle owned, cost compared? |
| Custom Development (Private Edition only) | A, B, C or D depending on what it touches | Which objects does it touch, and is a stricter alternative possible? |
| Process Change | Not an extension | Has the business owner approved adoption and control equivalence? |
| Third-Party Solution | Assessed separately | Support, privacy, integration, commercial and exit implications |
| Deferred | Not applicable | Consequence, review trigger and owner recorded? |

**Admission order (decision tree):** (1) configuration, (2) process change, (3) released in-app extension, (4) side-by-side on released APIs, (5) third-party, (6) classic API use with approval, (7) exception for internal object access, (8) deferred. Anything needing level D is returned to the requester with alternatives.

**Extension Decision Record (one page per requirement):** requirement ID; process and capability; source reference; resolution category; proposed Clean Core level and why; objects and APIs touched; alternatives considered; owner; decision authority and date; exception expiry (levels C and D); test links; evidence status.

## 11. Hands-on exercise: classify eight synthetic requirements

All requirements are synthetic. Participants fill the last three columns without looking at the key. The "proposed answer" column is a teaching key to be debated, not an SAP certification of any item.

| ID | Synthetic requirement | Participant: category | Participant: level | Participant: decision | Proposed answer (teaching key) |
|---|---|---|---|---|---|
| ENE-SYN-RQ-01 | Add a shutdown-reason field to the work-order screen | | | | Enhancement; Level A if a released key-user mechanism covers it; else side-by-side |
| ENE-SYN-RQ-02 | Compute a reliability indicator from condition events and maintenance history and show it to planners | | | | Side-by-side on BTP; Level A only if released APIs and events are enough; OT data stays within plant boundaries |
| ENE-SYN-RQ-03 | Read an SAP internal table directly for a legacy report | | | | Level C; reject unless no released alternative exists; exception with expiry |
| ENE-SYN-RQ-04 | Write directly to an SAP table to change a stock value | | | | Level D; reject; ask for the business outcome and offer a released API or process change |
| ENE-SYN-RQ-05 | Integrate retail-site sales data through a documented classic interface | | | | Level B; allowed with owner approval; plan migration to a released API |
| ENE-SYN-RQ-06 | Route customer service cases by site type with a new rule | | | | Configuration first; extension only if configuration cannot do it |
| ENE-SYN-RQ-07 | Replace emissions reporting with an external tool | | | | Third-party; assess support, privacy, lineage, integration, exit |
| ENE-SYN-RQ-08 | Advanced trading analytics not needed this year | | | | Deferred with consequence, review date and owner |

**Time:** 25 minutes. **Output:** eight Extension Decision Records, at least two argued as exceptions.

## 12. Three tabletop tests

A tabletop test is a paper walk-through. It is not a technical test of a running tenant.

| Test | Scenario | Expected result | Actual paper result | Correction | Pass or revise |
|---|---|---|---|---|---|
| T1 Level D request on a critical asset process | A planner asks for direct table writes to speed up work-order closure after a refinery alert | Admission rule rejects level D; alternatives listed; plant authority (OVE-P04) informed; decision record kept | | | |
| T2 Two tools, two names | The business renames a capability in the process tool while the architecture tool still holds the old name and sync is scheduled | Object owner rule decides the direction before sync; conflict reported, not silently overwritten; owner register updated | | | |
| T3 Stale inventory misleads impact analysis | An application is decommissioned in reality but remains linked to three processes; a change impact report omits a real dependency | Review-date rule flags the fact sheet; impact report states data freshness; owner re-certifies | | | |

## 13. Detailed action plan

This is a **proposed** plan. Durations are working-day estimates for a first bounded pass on two value streams, not commitments. Owners are proposed personas. Every action has an artefact and an acceptance check so it can be inspected.

### Phase 0: Frame the decision

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-01 | Confirm the decision statement in Section 4 and the two scoped streams | OVE-P05 | Case Theme C; sponsor view | One-page decision brief | CDIO and EA Director sign it; CEO outcome question answered | 1 |
| A-02 | Name one owner per object type: capability, process, application, data object, organization | OVE-P12 | Section 6 | Object ownership rule | No object type has two owners | 1 |
| A-03 | Write the evidence-gap list: what is missing, who can authorize, constraints, how value is measured (source challenge) | OVE-P12 | Section 2 | Evidence-gap register | Every gap has an owner and a due date | 2 |
| A-04 | Agree the standing rule: nothing is scored or targeted without a baseline | OVE-P05 | Source rule | Governance note | Rule appears in the review checklist | 0.5 |

### Phase 1: Capability and value-stream model

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-05 | Write the capability maturity scale (what L1, L2, L4 mean) | OVE-P12 with business owners | Source gaps | Scale definition page | Each level has an observable test | 2 |
| A-06 | Build the capability map and owner register (Section 7) | OVE-P12 | A-02, A-05 | Capability map; owner register | Five source capabilities present; owners confirmed or marked TBC | 3 |
| A-07 | Collect evidence samples for asset management and customer engagement only | OVE-P09, OVE-P10, OVE-P16 | A-05 | Evidence samples | Sample method documented; no invented scores | 5 |
| A-08 | Draw the two value streams and stage-capability matrices (Section 8) | OVE-P09, OVE-P10 | Source stream chain | Value-stream maps | Each stage maps to a capability and an owner | 3 |
| A-09 | Walk the maps with frontline operations to find what the diagram misses | OVE-P14 | A-08 | Findings log | At least one change or an explicit "no change" recorded | 1 |

### Phase 2: Process model (Signavio)

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-10 | Set the process taxonomy and naming rules (Section 8) | OVE-P12 | A-08 | Naming and level standard | Two reviewers apply it to the same process and get the same code | 1 |
| A-11 | Model two or three L3 processes per stream with owners and control points | Process owners | A-10 | Process diagrams | Owner has read back and accepted each diagram | 5 |
| A-12 | Record glossary or dictionary entries for capabilities, applications, organizations | OVE-P16 | A-06 | Dictionary entries | No duplicates; names match the owner register | 2 |
| A-13 | Mark every process step that touches plant authority or consent | OVE-P04 and OVE-P10 | A-11 | Control-point overlay | Each marked step names its approver | 1 |

### Phase 3: Inventory (LeanIX) and integration

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-14 | Define the fact sheet attributes and data-quality rules (Section 9) | OVE-P12 and OVE-P16 | A-02 | Inventory standard | Rules testable by a script or a checklist | 2 |
| A-15 | Load the scoped applications as fact sheets with owners, lifecycle and interfaces | Technical owners | A-14 | Inventory for scoped streams | Every fact sheet has an owner and a review date | 5 |
| A-16 | Decide sync direction per object type, mapping and schedule | OVE-P12 | A-02, A-12 | Sync design note | Matches the owner rule; one source of truth per type | 1 |
| A-17 | Obtain the dedicated integration user and confirm permissions and licensing | OVE-P13 and OVE-P12 | A-16 | Access record | Least privilege; credentials held in a managed secret store | 2 |
| A-18 | Run a first sync in a non-production or sandbox setting and review conflicts | OVE-P12 | A-16, A-17 | Sync report | Every conflict has a resolution; unexpected changes explained | 2 |
| A-19 | Produce one dependency view: process, application, data, interface | OVE-P12 | A-15, A-18 | Impact view | Freshness statement included; one known dependency verified by hand | 2 |

### Phase 4: Clean Core guardrail and delivery tracking

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-20 | Confirm which Clean Core levels, tools and terms apply to the actual SAP products and editions in scope | OVE-P12 | Current SAP documentation | Applicability note | Wording checked against SAP sources on a stated date | 1 |
| A-21 | Approve the admission rule and exception policy (Section 10) | OVE-P05, OVE-P12, OVE-P13 | A-20 | Admission rule v1 | Level D default rejection and exception expiry written | 1 |
| A-22 | Create the Extension Decision Record template and the decision log | OVE-P12 | A-21 | Template and log | Template fits on one page; log fields match source attributes | 1 |
| A-23 | Run the eight-requirement exercise with real reviewers and refine the rule | OVE-P12 | Section 11 | Revised rule and key | Reviewers agree on at least the A and D cases; disagreements logged | 1 |
| A-24 | Link requirements to processes and resolution categories in the delivery tool (validate tenant features first) | Delivery lead | A-21 | Traceable requirement set | Every approved requirement has category, level, owner, tests | 2 |

### Phase 5: Prove it on paper, then decide

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-25 | Run tabletop tests T1 to T3 and revise | OVE-P12 with OVE-P13 | Section 12 | Test sheet | Each test has actual result and pass or revise | 1 |
| A-26 | Define review cadence: monthly architecture review; quarterly inventory re-certification | OVE-P12 | A-14 | Review calendar | Dates set; owners named | 0.5 |
| A-27 | Select the measures and capture baselines before any target | OVE-P05 | Section 14 | Baseline sheet | Targets blank until baselines exist | 2 |
| A-28 | Present the decision pack to the CEO and CFO: what was built, what is evidence, what is not | OVE-P05 | All | Decision pack | Open questions and evidence gaps are visible, not hidden | 1 |

**Critical path (proposed):** A-02, A-05, A-08, A-10, A-14, A-16, A-18, A-21. Phases 2 and 3 can overlap once A-10 and A-14 are done.

### Presenter action items for the technical discussion

These are for the trainer preparing to show this demo to a corporate audience. They do not appear in the case.

| ID | Action | Why | Done when |
|---|---|---|---|
| P-01 | Decide which parts you will show live and which on paper; label each as sandbox, vendor-provided or paper | Honesty about what was actually exercised | Slide or note states the status of every screen |
| P-02 | Confirm access to a Signavio and a LeanIX environment, or prepare static screenshots from your own training sandbox | The vendor is expected to provide demo systems | Access confirmed in writing, or fallback ready |
| P-03 | Load the synthetic fact sheets from Section 9 and one synthetic process | Gives a concrete walkthrough | Records carry the `ENE-SYN` prefix |
| P-04 | Rehearse the 25-minute classification exercise with a colleague | Timing and disagreements | Timing and key adjusted |
| P-05 | Prepare the one-page answer to "have you done this for a client?" using your real engagements, kept separate from this file | Do not imply that case-study work is client work | Answer reviewed by you; no client names without permission |
| P-06 | Re-check the SAP sources listed in Section 17 for changes the day before delivery | Product guidance changes | Review date updated |
| P-07 | Record the session run log (Section 16) | Evidence trail | Log completed with what was actually run |

## 14. Acceptance and measures

**The design is acceptable for a bounded first pass only if:** one owner exists per object type; the two scoped streams have capability and process models read back by their owners; scoped applications have owners and review dates; the admission rule and exception policy are approved; tabletop tests are walked through; and the evidence status below is honest.

**Candidate measures (no baseline, no target supplied):**

| Measure | Definition | Baseline status |
|---|---|---|
| Governed fact sheet share | Scoped fact sheets with owner, lifecycle and review date divided by scoped fact sheets | Not measured |
| Requirement traceability | Approved requirements with category, level, owner and tests divided by approved requirements | Not measured |
| Exception count and age | Open level C and D exceptions, with age against expiry | Not measured |
| Sync conflicts | Conflicts found per sync run and time to resolve | Not measured |
| Inventory freshness | Fact sheets reviewed within the review period | Not measured |

**Do not invent a baseline, benefit or target.** Set a target only after measuring a baseline with the accountable owner.

## 15. Fit in a 2 to 3 hour session

| Minutes | Activity | Output |
|---|---|---|
| 0 to 20 | Case briefing; decision and personas (Sections 2 to 5) | Decision statement and owner |
| 20 to 50 | Toolchain roles and ownership rule (Section 6); capability and value-stream view (Sections 7 and 8) | Ownership rule; map sketch |
| 50 to 80 | Portfolio and fact sheet standard (Section 9) | Fact sheet template filled for two rows |
| 80 to 125 | Clean Core levels, admission rule and the eight-requirement exercise (Sections 10 and 11) | Eight decision records |
| 125 to 150 | Three tabletop tests (Section 12) | Pass or revise decisions |
| 150 to 180 | Action plan walk-through (Section 13); recall check; assessment; attendance | Assessment record |

This is a proposed teaching pattern, not a committed schedule.

## 16. Evidence status and limits

| Item | Status |
|---|---|
| Capability, value-stream and portfolio design | Designed, not executed |
| Fact sheets and requirements | Synthetic placeholders |
| Signavio and LeanIX sync | Described from public documentation; not run here |
| Clean Core classification of the eight requirements | Teaching key; not an SAP classification |
| Tabletop tests | Template; paper results filled in session |
| Real client delivery | Not represented by this file |

**Run log (fill only with what was actually run):**

| Date | Environment | Items run | Result | Notes |
|---|---|---|---|---|
| | | | | |

## 17. Resources and sources

- SAP News, [Extend SAP S/4HANA Cloud the right way: clean and clear](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/) (Clean Core level concept; reviewed 2026-11-10)
- SAP LeanIX documentation, [SAP Signavio integration](https://docs-eam.leanix.net/docs/technical-signavio) (reviewed 2026-11-10)
- SAP Learning, [Integrating SAP LeanIX and SAP Signavio](https://learning.sap.com/courses/sap-signavio-process-management/integrating-sap-leanix-and-sap-signavio-3)
- Case: [OmniVerse case](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd) · [Theme C architecture (OVE-M09 to M12)](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/master/theme-c-architecture.md) · [source and assumptions](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/references/source-and-assumptions.md) · [persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md)
- Series baseline: [Demo 01](01-omniverse-case-baseline-sap-nextgen-architecture.md)

**Educational alignment:** TOGAF for architecture views and decisions; BIZBOK for capability and value-stream distinctions; BABOK for needs and acceptance; DAMA for data ownership and quality; COBIT for accountable control. These mappings are educational and are not compliance certification or reproduction of proprietary standards.

**Publication note:** this is a demonstration file in the bootcamp folder. It is not proof that a course is live, purchasable or delivered.
