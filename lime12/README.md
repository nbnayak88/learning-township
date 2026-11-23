# 🚀 LIME 12 — Architect Your Learning. Transform Your Future.

**What if learning enterprise architecture was not limited to courses, certifications and static content?**
**What if every learner could explore, experiment, architect, build and demonstrate real capabilities?**

Welcome to **LIME 12**, a connected Enterprise Architecture & Learning Workspace from **SuccessLabs Academy**.

## 🌱 LIME = Learning · Innovation · Mastery · Enterprise

| Letter | Stands for | What it means in the workspace |
|---|---|---|
| **L** | **Learning** | Structured pathways across 12 architecture streams and 7 enterprise domains |
| **I** | **Innovation** | Explore and experiment in 20 SuperLabs: discovery, design, experimentation, implementation, transformation |
| **M** | **Mastery** | Build evidence of mastery, not just course completions |
| **E** | **Enterprise** | Apply it to real enterprise challenges across 11 industry sectors |

## The ecosystem

- ✅ **12 Architecture Streams** — from Enterprise and Business Architecture to AI, Security, Integration and Industry Architecture.
- ✅ **7 Enterprise Domains** — Workforce, Customer Experience, Finance, Procurement, Supply Chain, Business Transformation and Leadership.
- ✅ **20 SuperLabs** — connecting discovery, design, experimentation, implementation and transformation.
- ✅ **11 Industry Sectors** — contextual learning through enterprise scenarios (World of Work, WoW).

## Our philosophy

- Don't just consume knowledge. **Apply it.**
- Don't just learn technology. **Architect solutions.**
- Don't just complete courses. **Build evidence of mastery.**

LIME 12 connects learning with real-world enterprise challenges.

**12 Streams. 7 Domains. One Architecture.**
🌍 *Architecting Experiences for a Better World.*

`#LIME12 #SuccessLabsAcademy #EnterpriseArchitecture #LearningInnovation #BusinessTransformation #FutureOfLearning #ArchitectureThinking`

---

## About this web app

Single-file web app: `index.html` (no build, no dependencies). Each lab page keeps its lab-website link.

### Structure
- Home → 12 architecture streams and 7 enterprise business domains (HR, Customer Experience, Finance,
  Procurement, Supply Chain, Business Transformation, Leadership and Inner Transformation)
- Each entry → Dashboard · Product Roadmap · Status Updates · 20 Labs
- Each lab → its own colour theme, lab-specific mission, rule and five sprint tasks

### World of Work (WoW)
The right-hand panel lists the 11 GICS sectors. Each sector page shows a 12 streams × 20 labs grid; every cell
links to that stream's lab. Stream dashboards and lab pages link back to the sectors.

### Editing (admin only)
Viewers see everything read-only. The lock icon in the header (or the Edit button / `E`) asks for the admin
password; once unlocked you can rename items, add (+), delete (✕), move roadmap items, cycle status colours
and tick lab tasks. Edits save in the admin's browser; use Download / Copy / Import JSON to move them.

The page holds only a salted password hash, never the password. This lock is a front-end gate for a static
site: it stops casual edits, but it is not server-side security, and edits are not shared between visitors.

### Publish
Settings → Pages → Deploy from branch → `main` / root. Live at `/learning-township/lime12/`.
Deep links: `#finance`, `#finance-roadmap`, `#finance-validate`, `#enterprise-discover`.

Comments are handled in the LMS, not in this app.
