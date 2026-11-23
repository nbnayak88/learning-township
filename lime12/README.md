# Lime 12 — 12 Streams of Architecture and 7 Enterprise Domains (GitHub Pages)

Single-file web app: `index.html` (no build, no dependencies). Each lab page keeps its lab-website link.

## Structure
- Home → 12 architecture streams and 7 enterprise business domains (HR, Customer Experience, Finance,
  Procurement, Supply Chain, Business Transformation, Leadership and Inner Transformation)
- Each entry → Dashboard · Product Roadmap · Status Updates · 20 Labs
- Each lab → its own colour theme, lab-specific mission, rule and five sprint tasks

## World of Work (WoW)
The right-hand panel lists the 11 GICS sectors. Each sector page shows a 12 streams × 20 labs grid; every cell
links to that stream's lab. Stream dashboards and lab pages link back to the sectors.

## Editing (admin only)
Viewers see everything read-only. The lock icon in the header (or the Edit button / `E`) asks for the admin
password; once unlocked you can rename items, add (+), delete (✕), move roadmap items, cycle status colours
and tick lab tasks. Edits save in the admin's browser; use Download / Copy / Import JSON to move them.

The page holds only a salted password hash, never the password. This lock is a front-end gate for a static
site: it stops casual edits, but it is not server-side security, and edits are not shared between visitors.
For shared, enforced editing put the data behind a small authenticated service.

## Publish
Settings → Pages → Deploy from branch → `main` / root.
Deep links: `#finance`, `#finance-roadmap`, `#finance-validate`, `#enterprise-discover`.
