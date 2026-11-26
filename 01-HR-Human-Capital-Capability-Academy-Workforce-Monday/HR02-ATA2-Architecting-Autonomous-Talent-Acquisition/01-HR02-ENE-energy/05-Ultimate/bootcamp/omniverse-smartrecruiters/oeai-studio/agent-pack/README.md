# AIU-OVE-01 — Joule Studio implementation handoff

This is an independent OEAI Studio design pack for a single agent, not an importable SAP deployment bundle. No live model or tenant has been connected.

## Source baseline

The OmniVerse bootcamp registers AIU-OVE-01 as L1 Assist with OVE-R01 (Hiring Manager) accountable. Inputs: position data and workforce plan. Trigger: position approved. Output: a draft for human review. Publishing, position changes and budget setting are prohibited.

The original skill and PRM-OVE-181/182 prompts are included unchanged. Source scope and references are preserved. The linked requirements span different role families; validate their applicability during design review.

## Prototype additions

The local JavaScript engine implements deterministic guards and source-linked output. It is a prototype addition, not an SAP SDK implementation. Run `node verify-agent.cjs` to execute ten guard cases and the baseline check. `sample-input.json` is synthetic.

## Proposed real implementation sequence

1. Confirm tenant availability, Joule Studio entitlement, identity and development roles.
2. Create one agent project for AIU-OVE-01 in the supported tenant experience.
3. Review the source prompt and agent card with OVE-R01.
4. Map the proposed read-only contracts to supported tenant-specific position and workforce-plan APIs; no universal API path is assumed.
5. Configure credentials and model access only in tenant-owned secret/configuration mechanisms. Never put secrets in this static prototype.
6. Validate input/output schemas, source lineage, missing data, conflicts and prohibited-action handling.
7. Implement the human review handoff. Retain the prohibition on publishing, changing positions and setting budgets even after draft review.
8. Run real model, integration, access, failure, fairness and adverse-impact checks. Local deterministic passes do not substitute for these.
9. Record owner approval, release version, monitoring, pause authority and rollback.

## Resource links

- https://www.sap.com/products/artificial-intelligence/joule-studio.html
- https://learning.sap.com/learning-journeys/developing-with-joule-studio
- https://www.sap.com/products/artificial-intelligence/joule-studio/product-tour.html

SAP's marketing tour and availability are time-dependent; applications are described as coming soon on the product page inspected 26 November 2026. Verify actual tenant feature support. This prototype's supporting draft viewer is an original concept.
