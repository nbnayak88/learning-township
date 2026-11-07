# OmniSpace HR01 — Employee Central source of truth
Edition: 2026-11-07 · GICS11 Real Estate · Fictional educational implementation case.

This folder is canonical for HR01 Employee Central. Notion mirrors this edition. Other repositories provide enterprise context and links; they must not override HR01 decisions. Record proposed mirror edits here before republishing. Automated synchronization is not established by this declaration.

## Gap resolution and folder map
| Gap | Resolution | Canonical document |
|---|---|---|
| Conflicting enterprise profiles | Bounded 120-employee India pilot; historical global variants excluded from sizing | [Pre-Foundation baseline](01-Pre-Foundation/ec-case-baseline.md) |
| Employer/transfer ambiguity | Same-employer pilot; cross-employer/international variants separately gated | [Baseline](01-Pre-Foundation/ec-case-baseline.md) |
| Property/org/position relationships | Distinct identities and ownership; primary versus temporary assignments | [Foundation architecture](02-Foundation/ec-architecture-and-data.md) |
| Lifecycle/configuration/security | Requirements, approval policy, permission populations and implementation journal | [Essentials controls](03-Essentials/ec-process-configuration-and-controls.md) |
| Interface/recovery/test gaps | Five logical contracts, ordering/replay rules and 12 extended tests | [Advanced verification](04-Advanced/ec-integration-and-test-catalogue.md) |
| Migration/cutover/value gaps | Sequence, reconciliation/release gates, six KPI definitions and cost model | [Ultimate assurance](05-Ultimate/ec-migration-cutover-and-value.md) |

Documentation gaps are resolved at design level for this pilot. Tenant configuration, release-specific validation, statutory localization, observed tests, production access and measured benefits remain unexecuted or require discovery. This edition does not claim global implementation readiness.

[Origin Story](0-The-Origin-Story/sprint/real-estate-workforce-foundations-evolution-sprint.md) retains its three tabletop tests and stable IDs.
[Notion mirror](https://app.notion.com/p/bd7f2d24c966478a92c7c06ec73a029a).
[Enterprise context](https://github.com/nbnayak88/successlabs-case-studies/tree/main/11-real-estate/omnispace-real-estate-ltd).
