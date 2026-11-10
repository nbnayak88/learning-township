# OmniWorks Industrial Systems Ltd. — Enterprise Architecture, SAP Signavio, SAP LeanIX and Clean Core

## Demo 02 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 03 AI/GenAI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Energy version of this demo](../../../01-BTM11-ENE-energy/05-Ultimate/bootcamp/02-enterprise-architecture-signavio-leanix-clean-core.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is an **aspirational case study**. This file is an architecture design and teaching demonstration. It is **not** a record of a client implementation. No executed Signavio model, LeanIX inventory, sync run, Clean Core check or realized benefit is asserted. The case source contains little or no SAP landscape detail, so application names, fact sheets, process codes and requirements below are **synthetic placeholders** (prefix `IND-SYN`) and are labelled as new design. Product names are learning examples, not confirmed OmniWorks implementations.

---

## 1. The question this file answers

> *Enterprise architecture experience across SAP Signavio, SAP LeanIX and Clean Core.*

**What this file shows:** how the architect turns this sector's board-level case into (1) a capability and value-stream model, (2) a governed application and technology inventory, (3) a process model linked to that inventory, and (4) a Clean Core rule that decides how every requirement may extend SAP. It ends with a detailed action plan.

**What it does not show:** a delivered engagement. Real project experience is described separately by the presenter and should not be inferred from this file.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers |
| Business mix | Industrial automation 27%; aerospace and defence 23%; transport and mobility 19%; infrastructure 16%; aftermarket and lifecycle services 15% |
| Burning platform | Recurring transport asset failures cannot be consistently traced across configuration, telemetry, supplier batches and maintenance history |

**Decision under discussion (source):** Turn a USD 575M transformation envelope into credible customer, operational and financial value without disrupting safety-critical operations.

**Illustrative trigger (source):** Repeat customer asset failures expose fragmented engineering-to-service information, and the business wants to sell uptime rather than equipment (hero story).

**Sector constraint carried from the source:** Plant safety authority is explicit and standards are central with federated delivery (source M11).

**What the source gives for this demo (Theme C):**

| Source ID | Content (source) | Source deliverable |
|---|---|---|
| OW-M09 Business capability architecture | Product Engineering L2→L4; Manufacturing Operations L2→L4; Asset Lifecycle Services L2→L4; Supply Chain Resilience L2→L4; Sustainability Performance L1→L4. Maturity scales are illustrative and require rubric definitions. |  |
| OW-M10 Value streams and process architecture | Design→Source→Build→Commission→Operate→Maintain→Upgrade→Recycle; four transformation value streams: Engineer-to-Product, Plan-to-Operate, Asset-to-Outcome, Insight-to-Decision. |  |
| OW-M11 Target operating model | Move from siloed product functions to cross-functional value-stream accountability. Define centralized standards, federated delivery, plant safety authority, data stewards and benefits owners. |  |
| OW-M12 Enterprise architecture and digital enablement | Conceptual target: PLM/ERP/MES/EAM/FSM and customer portals linked through APIs/events; Product/Asset/Supplier/Customer/Service 360 data products; OPC UA/MQTT at OT edge; identity, cyber segmentation, cloud/edge services and governed AI. |  |

**Source aspirational stakeholder challenge (each M-section):** *What evidence is missing, which persona can authorize the decision, what constraints apply, and how will value be measured?*

**Resolution categories (series vocabulary, not from this case):** Configuration; Enhancement (BAdI / Key User Extensibility); Side-by-Side Extension (BTP); Custom Development (Private Edition only); Process Change; Third-Party Solution; Deferred. These seven categories come from the OmniVerse Energy source register (written in a SuccessFactors Employee Central gap-capture context). They were searched for in this case's source on 2026-11-10 and are **not present there**. This demo reuses them as a shared teaching vocabulary across the series and says so.

## 3. Source versus new design

| Element | Status |
|---|---|
| Capabilities, value-stream names, operating-model statements, M12 perspectives, personas | **Source** |
| Capability-to-owner register, process taxonomy codes, synthetic applications and fact sheets, LeanIX and Signavio data model, Clean Core admission rule, synthetic requirements, tests, action plan | **New design (illustrative)** |
| Any SAP product behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What minimum common architecture model and extension rule does OmniWorks need so that value-stream teams can deliver independently without creating disconnected pilots and brittle interfaces?

**Scope of this demo:** two source value streams, chosen because the source trigger points at them: **Asset-to-Outcome** and **Engineer-to-Product**. The other streams reuse the same method.

**Accountable decision owner (proposed):** OW-P05 Priya Nair, with architecture assurance from OW-P11 Hannah Fischer. The sponsor (OW-P01 Dr. Maya Richter) will test every artefact against customer, employee or operational outcomes, not technology.

## 5. Personas and proposed decision rights

IDs, names and roles come from the case persona cards. Decision rights are **proposed** and need discovery validation.

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OW-P05 | Priya Nair, CIDO | Owns the minimum common platform decision; challenges disconnected pilots |
| OW-P11 | Hannah Fischer, Director, Enterprise Architecture | Owns standards, the Clean Core admission rule and architecture review |
| OW-P06 | Marcus Vogel, CISO | Security and trust-boundary approval for any extension or integration |
| OW-P15 | Dr. Leila Haddad, Head of Data Governance & AI | Owns data object definitions and stewardship in the inventory |
| OW-P09 | Isabel Torres, Chief Customer & Service Officer | Business owner for Asset-to-Outcome |
| OW-P10 | Ravi Deshpande, VP Manufacturing, Pune Operations | Business owner for Engineer-to-Product |
| OW-P12 | Daniel Okafor, Field Service Operations Manager | Operational or frontline authority; reality check on process models; veto where operations or safety are at risk |
| OW-P01 | Dr. Maya Richter, Group CEO | Sponsor; outcome test for every decision |
| OW-P04 | Dr. Lukas Weber, COO | Veto on anything that risks safety-critical operations |

Shared first names across cases do not establish shared identity. Source: [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md).

## 6. How the toolchain divides the work

Tool roles are described from SAP's public documentation (reviewed 2026-11-10).

| Tool | Role in this design | Source of truth for |
|---|---|---|
| SAP LeanIX | Enterprise architecture inventory: business capabilities, applications, IT components, data objects, organizations, lifecycle, ownership | Applications, business capabilities, organizations, data objects (SAP documentation recommends LeanIX as source of truth for these) |
| SAP Signavio | Process modelling and process navigation; value chains, process diagrams, dictionary/glossary | Process models and diagrams |
| SAP Cloud ALM | Implementation project, scope, requirements, tests, deployment tracking | Delivery records and requirement trace |
| Clean Core guardrail (this design) | Admission rule for every extension | The extension decision record |

**Documented LeanIX to Signavio integration behaviour (verify before relying on it):** processes sync from Signavio to LeanIX only (process diagrams, navigation maps and value chains become business-context fact sheets, with diagram links on the fact sheet). Applications, business capabilities and organizations sync **in both directions** against Signavio dictionary items, and you choose the source and target per mapping. The process hierarchy can be mapped top-down, bottom-up or by a list of Signavio directories. Fact sheets with matching names are linked; otherwise new ones are created. The setup needs a dedicated Signavio user with read and write permission (an API edition licence is recommended), the tenant ID, and a manual or scheduled sync run.

**Consequence for design:** agree one owner per object type **before** the first sync, otherwise two teams can rename the same capability in two tools (tabletop test T2).

## 7. Capability architecture

Capability names come from the source; owners and evidence needs are proposed. The evidence column is the work to do, not a finding.

| Capability (source) | Source maturity statement | Proposed business owner | Evidence needed before scoring | Stream touched |
|---|---|---|---|---|
| Product Engineering | L2 to L4 | OW-P10 Ravi Deshpande | Configuration baseline ownership | Engineer-to-Product |
| Manufacturing Operations | L2 to L4 | OW-P10 Ravi Deshpande | Plant data sample | Plan-to-Operate |
| Asset Lifecycle Services | L2 to L4 | OW-P09 Isabel Torres | Failure trace sample across configuration and telemetry | Asset-to-Outcome |
| Supply Chain Resilience | L2 to L4 | To be confirmed | Supplier data-sharing rules | Plan-to-Operate |
| Sustainability Performance | L1 to L4 | To be confirmed | Evidence lineage | Insight-to-Decision |

**Rule:** a maturity level is not scored until the scale is written down and an evidence sample exists.

## 8. Value streams and process taxonomy (new design)

Synthetic taxonomy for the two scoped streams. Codes are placeholders, not SAP Scope Item IDs, and must not be presented as such. The stream names are from the source; stages and processes are illustrative.

| Level | Asset-to-Outcome (`IND-SYN-A2O`) | Engineer-to-Product (`IND-SYN-E2P`) |
|---|---|---|
| L1 value stream | Asset-to-Outcome | Engineer-to-Product |
| L2 stages | Configure asset, Commission, Operate, Maintain, Report outcome | Design, Release, Manufacture, Verify, Change |
| L3 processes (examples) | Record as-built configuration; Ingest telemetry event; Triage failure; Issue service work order; Link supplier batch to asset | Release engineering change; Update bill of materials; Notify service of change; Record deviation; Close change |
| Control points | Human sign-off on safety-critical steps; supplier data shared only under partner permission | Engineering IP protected by role; change approval before release |
| Systems of record | PLM, FSM and asset sources (to be mapped) | PLM, ERP and MES sources (to be mapped) |
| Business owner (proposed) | OW-P09 Isabel Torres | OW-P10 Ravi Deshpande |

**Deliverable pattern:** one Signavio value chain per stream; process diagrams to L3 for the first two or three processes only; each diagram linked to a capability and an owner.

## 9. Application and technology portfolio (synthetic)

Rows are **roles**, not products, so nobody mistakes them for a real inventory.

| Fact sheet (synthetic) | Type | Supports capability | Owner (proposed) | Lifecycle | Disposition (proposed) | Evidence needed |
|---|---|---|---|---|---|---|
| IND-SYN-APP-01 Product lifecycle management application | Application | Product Engineering | OW-P10 Ravi Deshpande | Unknown | To be decided | Configuration objects and interfaces |
| IND-SYN-APP-02 Enterprise resource planning application | Application | Manufacturing Operations; Supply Chain Resilience | OW-P10 Ravi Deshpande | Unknown | To be decided | Version and extensions inventory |
| IND-SYN-APP-03 Manufacturing execution application | Application | Manufacturing Operations | OW-P10 Ravi Deshpande | Unknown | To be decided | OT boundary and criticality |
| IND-SYN-APP-04 Enterprise asset and field-service applications | Application | Asset Lifecycle Services | OW-P09 Isabel Torres | Unknown | To be decided | Work-order and telemetry links |
| IND-SYN-APP-05 Customer service portal | Application | Asset Lifecycle Services | OW-P09 Isabel Torres | Unknown | To be decided | Access model and data classes |
| IND-SYN-APP-06 OT edge gateway and integration layer | IT component | All | OW-P05 Priya Nair | Unknown | To be decided | OPC UA and MQTT boundary, segmentation |

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
| D | Not recommended: modifications, writes to SAP tables, implicit enhancements; highest risk and technical debt | Rejected by default; needs an architecture exception at decision-owner level |

**Applicability warning:** the level concept is described in the context of SAP S/4HANA. Confirm which levels, tooling and wording apply to the actual product and edition before using it with a real client. This case does not state that OmniWorks runs S/4HANA.

**Mapping the series resolution categories to levels (proposed):**

| Resolution category (series vocabulary) | Typical Clean Core level | Admission question |
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

All requirements are synthetic. Participants fill the three blank columns without looking at the key. The key is a teaching answer to be debated, not an SAP certification of any item.

| ID | Synthetic requirement | Participant: category | Participant: level | Participant: decision | Proposed answer (teaching key) |
|---|---|---|---|---|---|
| IND-SYN-RQ-01 | Add a configuration-baseline field to the service work-order screen |  |  |  | Enhancement; Level A if a released key-user mechanism covers it; else side-by-side |
| IND-SYN-RQ-02 | Combine telemetry events and maintenance history into a failure-trace view for technicians |  |  |  | Side-by-side on BTP; Level A only if released APIs and events suffice; OT data stays at the edge |
| IND-SYN-RQ-03 | Read an SAP internal table directly to reconcile supplier batches |  |  |  | Level C; reject unless no released alternative exists; exception with expiry |
| IND-SYN-RQ-04 | Modify standard SAP code to skip an engineering-change approval step |  |  |  | Level D; reject; control equivalence needed; explore process change |
| IND-SYN-RQ-05 | Integrate field-service orders through a documented classic interface |  |  |  | Level B; allowed with owner approval; plan migration to a released API |
| IND-SYN-RQ-06 | Route service requests by asset class with a new rule |  |  |  | Configuration first; extension only if configuration cannot do it |
| IND-SYN-RQ-07 | Replace supplier sustainability tracking with an external tool |  |  |  | Third-party; assess partner data-sharing, privacy, integration, exit |
| IND-SYN-RQ-08 | Digital twin visualization not needed this year |  |  |  | Deferred with consequence, review date and owner |

**Time:** 25 minutes. **Output:** eight Extension Decision Records, at least two argued as exceptions.

## 12. Three tabletop tests

A tabletop test is a paper walk-through. It is not a technical test of a running tenant.

| Test | Scenario | Expected result | Actual paper result | Correction | Pass or revise |
|---|---|---|---|---|---|
| T1 Level D request on an engineering change | A planner asks for a code modification to skip an approval step before a customer deadline | Admission rule rejects level D; control equivalence required; engineering and safety owners informed |  |  |  |
| T2 Two tools, two names | A product family is renamed in the process tool while the architecture tool keeps the old name before sync | Owner rule decides direction; conflict reported; owner register updated |  |  |  |
| T3 Supplier data crosses a boundary | An impact view shows supplier-restricted batch data to a customer user | Permission flag blocks display; freshness and ownership stated; incident logged |  |  |  |

## 13. Detailed action plan

This is a **proposed** plan. Durations are working-day estimates for a first bounded pass on two value streams, not commitments. Owners are proposed personas. Every action has an artefact and an acceptance check so it can be inspected.

### Phase 0: Frame the decision

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-01 | Confirm the decision statement in Section 4 and the two scoped streams | OW-P05 | Case Theme C; sponsor view | One-page decision brief | OW-P05 and OW-P11 sign it; sponsor outcome question answered | 1 |
| A-02 | Name one owner per object type: capability, process, application, data object, organization | OW-P11 | Section 6 | Object ownership rule | No object type has two owners | 1 |
| A-03 | Write the evidence-gap list: what is missing, who can authorize, constraints, how value is measured (source challenge) | OW-P11 | Section 2 | Evidence-gap register | Every gap has an owner and a due date | 2 |
| A-04 | Agree the standing rule: nothing is scored or targeted without a baseline | OW-P05 | Source rule | Governance note | Rule appears in the review checklist | 0.5 |

### Phase 1: Capability and value-stream model

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-05 | Write the capability maturity scale (what each level means, observably) | OW-P11 with business owners | Source capability statements | Scale definition page | Each level has an observable test | 2 |
| A-06 | Build the capability map and owner register (Section 7) | OW-P11 | A-02, A-05 | Capability map; owner register | Source capabilities present; owners confirmed or marked TBC | 3 |
| A-07 | Collect evidence samples for the capabilities touched by the two streams only | OW-P09, OW-P10, OW-P15 | A-05 | Evidence samples | Sample method documented; no invented scores | 5 |
| A-08 | Draw the two value streams and stage-capability matrices (Section 8) | OW-P09, OW-P10 | Source stream names | Value-stream maps | Each stage maps to a capability and an owner | 3 |
| A-09 | Walk the maps with the operational authority to find what the diagram misses | OW-P12 | A-08 | Findings log | At least one change or an explicit "no change" recorded | 1 |

### Phase 2: Process model (Signavio)

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-10 | Set the process taxonomy and naming rules (Section 8) | OW-P11 | A-08 | Naming and level standard | Two reviewers apply it to the same process and get the same code | 1 |
| A-11 | Model two or three L3 processes per stream with owners and control points | Process owners | A-10 | Process diagrams | Owner has read back and accepted each diagram | 5 |
| A-12 | Record glossary or dictionary entries for capabilities, applications, organizations | OW-P15 | A-06 | Dictionary entries | No duplicates; names match the owner register | 2 |
| A-13 | Mark every process step that touches operational authority, consent or a regulated control | OW-P12 and OW-P09 | A-11 | Control-point overlay | Each marked step names its approver | 1 |

### Phase 3: Inventory (LeanIX) and integration

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-14 | Define the fact sheet attributes and data-quality rules (Section 9) | OW-P11 and OW-P15 | A-02 | Inventory standard | Rules testable by a script or a checklist | 2 |
| A-15 | Load the scoped applications as fact sheets with owners, lifecycle and interfaces | Technical owners | A-14 | Inventory for scoped streams | Every fact sheet has an owner and a review date | 5 |
| A-16 | Decide sync direction per object type, mapping and schedule | OW-P11 | A-02, A-12 | Sync design note | Matches the owner rule; one source of truth per type | 1 |
| A-17 | Obtain the dedicated integration user and confirm permissions and licensing | OW-P06 and OW-P11 | A-16 | Access record | Least privilege; credentials held in a managed secret store | 2 |
| A-18 | Run a first sync in a non-production or sandbox setting and review conflicts | OW-P11 | A-16, A-17 | Sync report | Every conflict has a resolution; unexpected changes explained | 2 |
| A-19 | Produce one dependency view: process, application, data, interface | OW-P11 | A-15, A-18 | Impact view | Freshness statement included; one known dependency verified by hand | 2 |

### Phase 4: Clean Core guardrail and delivery tracking

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-20 | Confirm which Clean Core levels, tools and terms apply to the actual SAP products and editions in scope | OW-P11 | Current SAP documentation | Applicability note | Wording checked against SAP sources on a stated date | 1 |
| A-21 | Approve the admission rule and exception policy (Section 10) | OW-P05, OW-P11, OW-P06 | A-20 | Admission rule v1 | Level D default rejection and exception expiry written | 1 |
| A-22 | Create the Extension Decision Record template and the decision log | OW-P11 | A-21 | Template and log | Template fits on one page; log fields match source attributes | 1 |
| A-23 | Run the eight-requirement exercise with real reviewers and refine the rule | OW-P11 | Section 11 | Revised rule and key | Reviewers agree on at least the A and D cases; disagreements logged | 1 |
| A-24 | Link requirements to processes and resolution categories in the delivery tool (validate tenant features first) | Delivery lead | A-21 | Traceable requirement set | Every approved requirement has category, level, owner, tests | 2 |

### Phase 5: Prove it on paper, then decide

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-25 | Run tabletop tests T1 to T3 and revise | OW-P11 with OW-P06 | Section 12 | Test sheet | Each test has actual result and pass or revise | 1 |
| A-26 | Define review cadence: monthly architecture review; quarterly inventory re-certification | OW-P11 | A-14 | Review calendar | Dates set; owners named | 0.5 |
| A-27 | Select the measures and capture baselines before any target | OW-P05 | Section 14 | Baseline sheet | Targets blank until baselines exist | 2 |
| A-28 | Present the decision pack to the sponsor and finance: what was built, what is evidence, what is not | OW-P05 | All | Decision pack | Open questions and evidence gaps are visible, not hidden | 1 |

**Critical path (proposed):** A-02, A-05, A-08, A-10, A-14, A-16, A-18, A-21. Phases 2 and 3 can overlap once A-10 and A-14 are done.

### Presenter action items for the technical discussion

These are for the trainer preparing to show this demo to a corporate audience. They do not appear in the case.

| ID | Action | Why | Done when |
|---|---|---|---|
| P-01 | Decide which parts you will show live and which on paper; label each as sandbox, vendor-provided or paper | Honesty about what was actually exercised | Slide or note states the status of every screen |
| P-02 | Confirm access to a Signavio and a LeanIX environment, or prepare static screenshots from your own training sandbox | The vendor is expected to provide demo systems | Access confirmed in writing, or fallback ready |
| P-03 | Load the synthetic fact sheets from Section 9 and one synthetic process for Asset-to-Outcome | Gives a concrete walkthrough | Records carry the `IND-SYN` prefix |
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
|  |  |  |  |  |

## 17. Resources and sources

- SAP News, [Extend SAP S/4HANA Cloud the right way: clean and clear](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/) (Clean Core level concept; reviewed 2026-11-10)
- SAP LeanIX documentation, [SAP Signavio integration](https://docs-eam.leanix.net/docs/technical-signavio) (reviewed 2026-11-10)
- SAP Learning, [Integrating SAP LeanIX and SAP Signavio](https://learning.sap.com/courses/sap-signavio-process-management/integrating-sap-leanix-and-sap-signavio-3)
- Case: [OmniWorks Industrial Systems Ltd.](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems) · [Theme C architecture (OW-M09 to M12)](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/master/theme-c-architecture.md) · [source and assumptions](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/references/source-and-assumptions.md) · [persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)
- Series baseline: [Demo 01](01-omniworks-case-baseline-sap-nextgen-architecture.md)

**Educational alignment:** TOGAF for architecture views and decisions; BIZBOK for capability and value-stream distinctions; BABOK for needs and acceptance; DAMA for data ownership and quality; COBIT for accountable control. These mappings are educational and are not compliance certification or reproduction of proprietary standards.

**Publication note:** this is a demonstration file in the bootcamp folder. It is not proof that a course is live, purchasable or delivered.
