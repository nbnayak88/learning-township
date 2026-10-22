# SuccessLabs Academy — Learning Township

Independent repository for the SuccessLabs learning ecosystem. Academy folders, AI architecture content, community resources, and catalogs live at this repository’s root.

**31,680 HUB catalog pathways** = 792 learning units × 5 curriculum tiers × 8 learning formats.

Explore **7 academy folders (6 populated from HUB, 1 planned LIT academy) → 12 series → 11 GICS sectors → 6 curriculum tiers (0–5); sprint only at Level 0; eight formats at Levels 1–5**.

This township is separate from the **2,640 vendor-neutral Architecture Learning Journeys** in [Architecture Center Atlas](https://github.com/nbnayak88/architecture-center-atlas/tree/main/learning-journeys).

The source of truth is the uploaded HUB CSV. The published catalog excludes allocated-member names. Available/Occupied describes township allocation, **not** live-course status.

See [catalog.csv](catalog.csv) for a searchable catalog index.

Origin Story contains **924 sprint pathways** across seven academies, twelve series each and eleven sectors: 792 HUB-derived units plus 132 LIT units. Other Origin Story learning formats have been removed. [Free HUB Origin sprint catalog](hub-origin-free-pathways.csv).

## Repository separation

Moved from `nbnayak88/architecture-center-atlas` on 22 October 2026. Original source snapshot: `520b89a2b`. The original file history remains available in Atlas.

The HUB source CSV is in `township-source/`. The generator is in `scripts/generate_learning_township.py` and now targets this repository’s root. The previous publishing workflow is retained as a reference in `migration-reference/`; it is not enabled because its delete-and-regenerate step would remove manually authored learning content.
