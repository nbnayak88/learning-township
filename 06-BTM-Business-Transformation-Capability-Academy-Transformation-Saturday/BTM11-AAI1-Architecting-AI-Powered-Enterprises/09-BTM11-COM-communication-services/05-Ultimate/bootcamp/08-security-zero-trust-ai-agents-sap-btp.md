# OmniConnect — Security and Zero Trust for AI Assistants and Agents on SAP BTP

## Demo 08 of the BTM11 Communication Services Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Communication Services (COM) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniconnect-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniConnect is a **fictional educational case**. The case sources describe security perspectives; the agent permissions, threats and checks below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `COM-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Security architecture for AI and autonomous operations: what can an assistant or agent do, as whom, and what stops it doing more?*

**What this file shows:** an identity and permission model for OmniConnect's assistant and agents, four threat scenarios with a control and a check, and the sector boundary that no agent may cross.

**What it does not show:** a configured identity tenant, a penetration test result or a certified control.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 37B communications group; 62,000 employees; 28 countries; 210M subscriptions |
| Business mix | Mobile 34%; fixed and fiber 25%; media 19%; enterprise 14%; advertising and data 8% |
| Source problem | Separate network, customer, billing and content stacks; manual activation and assurance; identity and consent silos |

**Decision under discussion (source):** Fund a bounded converged-activation pilot with privacy, service-state, recovery and economic evidence before expansion.

**Illustrative trigger (source):** A converged bundle shows billing active while connectivity and content entitlement remain incomplete; care and network teams cannot reconcile status (invented, not an actual outage).

**Pilot from Demo 03:** Care-agent bundle-status explainer (consent-aware, no network changes)

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Agent identity model, permission matrix, threat scenarios, tests | **New design (illustrative)** |
| SAP identity and BTP security behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Under what identity and permissions may OmniConnect's assistant and agents run, and who can widen them?

**Accountable owner (proposed):** OCN-P10 Omar Haddad, with OCN-P12 Daniel Weber for the pattern and OCN-P09 Mei Lin for AI governance.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCN-P06 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes |
| OCN-P12 | Daniel Weber, Director Enterprise Architecture | Owns standards and review |
| OCN-P10 | Omar Haddad, CISO and Resilience Lead | Security and boundary approval |
| OCN-P09 | Mei Lin, Subscriber Data and Consent Lead | Data and AI governance |
| OCN-P13 | Priya Shah, Service Catalog and Fulfillment Lead | Business owner (first scope) |
| OCN-P08 | Marcus Okoro, Service Assurance and NOC Director | Business owner (second scope) |
| OCN-P04 | Arjun Mehta, Chief Network Officer | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. What SAP describes (public documentation, verify)

| Capability | What the documentation or SAP community describes | Use in this design |
|---|---|---|
| SAP Cloud Identity Services (Identity Authentication, Identity Provisioning) | Sign-in, tokens and user provisioning across SAP and non-SAP systems | Identity for people and applications |
| App-to-app OAuth2 client credentials | In an SAP community example the token identifies the application, not the end user; the agent checks signature, issuer, audience, expiry and a scope claim | Agent identity; user-level access needs principal propagation, so verify |
| Agent-to-agent protocol and BTP Destinations | An SAP community example secures an agent with a middleware and calls it through a destination using OAuth2 client credentials | Pattern for agent calls; verify for current versions |
| Role collections and authorizations on BTP | Roles are grouped into role collections and assigned to users | Human roles for approvals |

## 7. Identity and permission model (new design)

| Principle | Design |
|---|---|
| Two identities | The user's identity decides what data is visible; the agent's own identity decides which tools it may call |
| Least privilege | Each tool has its own scope; no wildcard scopes |
| Read before write | Agents start read-only; write tools are drafts that a person confirms |
| Approvals | Bound to one action, expire quickly, recorded with approver |
| Data minimization | Role filter applied before retrieval; identifiers masked |
| Untrusted text | Retrieved text is data and cannot trigger a tool call |
| Audit | Every tool call logged with user, agent, input class and result |

**Tool permission matrix from the Demo 03 pilot**

| Tool | Mode | Approval | Note |
|---|---|---|---|
| search_catalog | Read | None | Returns catalog version |
| get_service_state | Read (consent-filtered) | None | Returns nothing outside consented purposes |
| draft_care_note | Draft only | Care agent approves | No promise of resolution time |
| raise_fulfilment_task | Creates a task | Fulfilment owns the outcome | Assistant cannot change service state |
| Any network or OSS configuration change | Not exposed | Not available to the agent | No autonomous production-control validation |

**Sector boundary:** Network element control stays outside IT and AI tooling; assistants read subscriber data under consent only.

**Never available:** Data beyond the subscriber's consented purposes; Network topology and credentials; Another subscriber's data; Instructions found inside retrieved notices

## 8. Threat scenarios

| Threat | Control | Check |
|---|---|---|
| Injection in a care note | Text is data | Seed a note with an instruction |
| Agent changing network configuration | No such tool | Ask for a change |
| Use of data outside consent | Purpose filter | Query for a withdrawn purpose |
| Leak of subscriber records | Role filters | Query without role |

## 9. Hands-on exercise (synthetic data)

1. List every tool the assistant can call and mark its scope and approval.
2. Run the four threat checks on paper and record the expected result.
3. Draw the two identities (user and agent) on the first tool call.
4. Decide who may widen a scope and how the change is approved.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Network change request | An agent is asked to change a network element | Refused |
| T2 Withdrawn consent | A query uses a withdrawn purpose | Blocked; logged |
| T3 Role leak | A user without the role asks for records | Filter blocks |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Tools with an explicit scope and approval rule | Count against the tool list | Not measured |
| Threat checks with a recorded expected result | Count of four | Not measured |
| Tool calls with audit fields defined | Review | Not measured |
| Scope changes with a named approver | Policy review | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why agents change the threat model | Shared problem statement |
| 0:20 to 1:00 | Identity and permission model | Matrix with scopes |
| 1:00 to 1:45 | Threat scenarios | Four checks |
| 1:45 to 2:15 | Tabletop tests | Three findings |
| 2:15 to 2:30 | Decisions | Open items with owners |

## Evidence status and run log

| Item | Status |
|---|---|
| Design in this file | Written |
| Walk-through with a live audience | Not yet run |
| Hands-on run on a vendor-provided system | Not yet run |
| Customer-confirmed requirements | Not applicable (fictional case) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Cloud Identity Services](https://www.sap.com/products/technology-platform/cloud-identity-services.html)
- [SAP community: secure code-based agents with IAS](https://community.sap.com/t5/technology-blog-posts-by-sap/joule-a2a-secure-code-based-agents-with-ias/ba-p/14367792)

- [OmniConnect case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/09-communication-services/omniconnect-media-networks-ltd)
- [OmniConnect persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/personas/persona-cards.md)

