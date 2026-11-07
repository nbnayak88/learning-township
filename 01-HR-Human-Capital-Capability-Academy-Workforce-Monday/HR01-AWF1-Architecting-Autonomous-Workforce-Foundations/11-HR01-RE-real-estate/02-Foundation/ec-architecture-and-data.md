# OmniSpace HR01 — Architecture and data decisions
Edition: 2026-11-07 · Design baseline; tenant mapping unvalidated.
Read [controlled baseline](../01-Pre-Foundation/ec-case-baseline.md).

## Decisions
| ID | Adopted case decision | Alternative and trade-off |
|---|---|---|
| OSP-HR01-ADR02 | Property master belongs to property operations; EC stores or references only the primary-property key needed for HR | Copying full asset data into EC simplifies local reporting but creates competing masters |
| OSP-HR01-ADR03 | Legal employer, organization, position, location, property and accounting references are distinct concepts | One property per department is simpler but fails shared services and multi-property coverage |
| OSP-HR01-ADR04 | Permanent primary assignment is effective dated; temporary coverage uses a separately governed assignment register | Repeatedly changing the primary job obscures permanent ownership and creates payroll/access noise |
| OSP-HR01-ADR05 | HR commit, security confirmation and task authorization are separate states | One ready flag is easier to display but conceals incomplete handoffs |
| OSP-HR01-ADR06 | External supplier workers remain outside the direct-employee pilot | A total-workforce EC design may follow after source ownership and licensing review |

EC implementation choices are candidates until checked in the target release and tenant: Legal Entity, Business Unit, Division, Department, Location, Job Classification, Position and Job Information; primary-property reference may require an appropriate supported extension. Do not assume an arbitrary field or custom object is configured. Finance remains authoritative for cost-center reference data.

## Data contract
| Concept / key | Owner | Minimum attributes and control |
|---|---|---|
| Person / RE-P100 | HR steward | Synthetic immutable person key; duplicate check; correction route |
| Employment / RE-E100 | HR steward | Person key, employer, start/end; no new employment for this same-employer move |
| Job assignment / employment + effective date + sequence | HR | Position, manager, department, location, primary property, cost center; valid reference dates |
| Position / FAC-TECH-01 or 02 | HR organization owner | Job classification, reporting position, employer, location, vacancy/FTE policy |
| Property / PROPERTY-A or B | Property operations | Active code, service responsibility, reference version; no tenant details |
| Temporary coverage / coverage ID | Operations | Worker key, property, valid-from/to, authority; no automatic primary-job overwrite |
| Access request / request ID | Security | Worker identity reference, property, scope, valid interval, approval and acknowledgment |
| Task authorization / authorization ID | Property authority | Task scope, assessment reference, validity, approver; course completion alone insufficient |

Validate referential integrity, temporal overlaps, identifier uniqueness and required fields before publishing. Record source version, correction reason and accountable owner. Restrict pay, national identifiers and bank data to their declared purposes; never send them in building-access payloads.

## Twelve architecture views
| Stream | Unique deliverable / concern |
|---|---|
| Enterprise | Outcome, scope, roadmap and decision rights |
| Business | Workforce-change capability and value stream |
| Data | Identity, dating, ownership, quality and lineage |
| Application | EC versus payroll, property, learning and IAM responsibilities |
| Technology | Supported API/protocol and environment standards |
| AI | Optional evidence-completeness assistance with human review |
| Security | Target populations, least privilege and segregation |
| UI/UX | Employee/manager journeys, assisted and accessible channels |
| Infrastructure | Connectivity, recovery objectives and service dependencies |
| Integration | Message contracts, ordering, retries and reconciliation |
| Domain | Employment versus property coverage versus authorization rules |
| Industry | Property-service continuity and tenant-impact attribution |

TOGAF/ISO 42010 lens: identify stakeholder, concern, view, decision and evidence. BIZBOK lens: capability differs from process, organization and application. DAMA lens: accountable ownership and quality rules. These are alignment practices, not certifications.
