# OmniSpace HR01 — Migration, cutover and value assurance
Edition: 2026-11-07 · Proposed pilot gates; results unavailable.

## Migration scope and sequence
HR owns person/employment/job history; finance owns cost centers; property operations owns property keys; HR organization owner owns positions; security owns identity mappings. Load only synthetic data in the lab.
Sequence: reference validity → organization/job/position structure → person/employment → dated job/pay records → identity/property mappings → reconciliation.
History policy: load approved hire records and dated changes needed to reconstruct the pilot history; preserve any excluded history in a controlled read-only archive with a documented retrieval route. Country retention and production history scope require a separate decision.
Check duplicate persons, missing employers/managers, orphan references, overlapping or invalid dates, inactive properties and inconsistent position assignments.

## Gates
| Gate | Proposed acceptance | Owner |
|---|---|---|
| Design | Baseline and exceptions documented; no conflicting scale used for pilot | HR sponsor |
| Mock migration | All 120 employees reconciled; 20 supplier workers excluded and accounted for; zero unexplained duplicate/orphan critical records | HR data steward |
| Payroll/security rehearsal | All required destination outcomes reconciled or explicitly contained with approved owner | Payroll/security owners |
| Release | Critical tests pass with observed evidence; no unresolved critical access/privacy defect; rehearsal and support ready | Release authority |
| Cutover | Controlled source freeze, delta captured, load totals and histories checked, approvals recorded | Cutover lead |
| Hypercare exit | Exception ownership stable; agreed observation period reviewed; service process demonstrated | HR and operations |

Synthetic rehearsal: freeze approved source at T0, snapshot control totals, load baseline and deltas, reconcile before release. Before release, failed gates restore the prior approved dataset/checkpoint and replay verified deltas. After downstream processing, use controlled correction/compensation with payroll and security agreement; do not blindly erase history. Preserve audit and evidence.

## KPI dictionary
| ID | Definition | Owner / baseline |
|---|---|---|
| OSP-HR01-K01 | Correct dated sampled assignments / sampled assignments ×100 | HR steward; baseline to be observed |
| OSP-HR01-K02 | Median elapsed time from complete approved request to HR commit | HR operations; baseline to be observed |
| OSP-HR01-K03 | Transfers with all required downstream confirmations / transfers due for completion ×100 | Integration owner; baseline to be observed |
| OSP-HR01-K04 | Overdue unresolved access/task confirmations, count and age | Security/property authorities; baseline to be observed |
| OSP-HR01-K05 | Users completing the task correctly without intervention / assessed users ×100 | Change lead; baseline to be observed |
| OSP-HR01-K06 | Avoidable staffing-handoff service disruptions per 100 transfers | Property operations; causal attribution reviewed |

Measure over the same defined population and period before/after; exclude or explain incomplete cases, policy changes and seasonality. No numerical business improvement or ROI is claimed.
Cost model: implementation + migration + integration + licenses + training/backfill + support + control maintenance. Benefit hypothesis: evidenced rework hours avoided × agreed loaded cost, less added operating cost. Avoid double-counting saved time and headcount reduction. Financial and tenant/ESG benefits require separate causal evidence.

## Learning and governance
Use the same RE-P100 story through the levels. Learners may challenge the proposed model, run a reversible alternative and recommend scale, redesign or stop. Rubric: correctness 30%, ownership/security 25%, exception recovery 20%, evidence/traceability 15%, accessible explanation 10%. Proposed lab pass: 80% and no unauthorized consequential action; not professional certification.
Maintain requirement → decision → configuration → test → release → KPI links. TOGAF supports roadmap/decisions; DAMA quality/lineage; BABOK acceptance; COBIT decision rights; ISO/IEC principles controlled change/security. No compliance certification is implied.
