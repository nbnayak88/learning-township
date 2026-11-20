# Bright Friday — seat ownership and access plan

Status: review proposal, 20 November 2026. Separate replica; existing SuperLabs applications and navigation remain unchanged. No live applications accepted by this prototype.

## Campaign model

Let’s make everyone’s career brighter. A volunteering initiative offering new community members a place to learn, practise and contribute.

| Inventory | Allocation |
|---|---|
| HR, CX, FI, PROC, SCM, BTM, LIT | 240 seats in each enterprise domain |
| Per domain | 12 domain workstreams × 20 labs |
| Total | 7 × 240 = 1,680 seats |
| Seat identity | BF2026 + domain + workstream + canonical lab ID |
| Person limit | Proposed: one active campaign seat across ALL domains |
| Ownership | Volunteer stewardship of one stream–lab combination; no equity, employment, admin credentials or exclusive ownership of learning content |
| Access | Proposed ₹0 campaign entitlement, with scope documented before launch; not an implied Diamond membership |
| Dates | Proposed 27 Nov 2026 00:00 IST to 26 Nov 2027 00:00 IST, next Bright Friday |
| Late joiners | Same fixed cohort end; do not promise a fresh 365 days to late arrivals |
| Renewal | No auto-charge; optional future participation or paid membership requires a separate decision |

The 12 rows are business-domain workstreams, not the 12 architecture roles. Apply all 12 architecture perspectives as learning lenses: Enterprise; Business; Integration; Domain; Cloud & Infrastructure; Application & Process; AI; Security; Industry; Data; UI/UX; Technology. Each participant chooses one of the 11 GICS sectors as the case context. Lab names and stream labels are copied from the current SuperLabs source catalog, rather than reconstructed from older naming lists.

## Airline-style journey

1. Browse public availability without providing personal details. Seat colors: available, selected, temporarily held, confirmed, unavailable. The review page only shows available, selected and local demo allocations.
2. Selecting any seat opens the exact community checkout URL in an iframe: https://hub.successlabsacademy.com/web/checkout/694af8798dd872a219700dd3 . Always include an external-opening fallback. A checkout visit or completion is not a seat confirmation.
3. Before a LIVE hold: collect name, email, mobile/WhatsApp number, optional LinkedIn profile, sector and consent. Verify BOTH email and mobile using OTPs. WhatsApp and mobile are the same phone identity. A typed LinkedIn URL is never proof of account ownership; optional OAuth would need a separate integration.
4. Screen against an authoritative existing-community roster BEFORE the campaign join action. Record application time and membership snapshot: a new applicant who subsequently joins using the provided link remains eligible; an existing member at initial application does not. Pass an opaque application ID through the join flow if supported. If attribution or roster lookup is uncertain, leave the application pending manual review.
5. In one transaction: check identity uniqueness campaign-wide, lock available seat, expire stale holds and create a ten-minute hold. Server time is authoritative. No hold for a casual visitor merely opening a seat.
6. Confirm eligibility and commitment before expiry. Server atomically converts the hold to confirmed and creates an entitlement event. Send a private seat reference and dates only after confirmation. Grant access through an idempotent integration worker; report access provisioning separately if it fails.
7. Full inventory: offer verified waitlisting, one queue position per person and domain preference. A waitlist entry is not ownership. Offer a released seat for 24 hours; expire the offer and advance in order. These timings are proposed and configurable.

## Existing-member exclusion

Current members do not apply and retain their current access. Import the membership roster through a private read-only integration or controlled admin import. Match canonical email OR E.164 phone, including historical/alternate identities where available. Existing member allocations are flagged for review, notified privately and revoked from this campaign after review. Release their campaign seat and cancel only the campaign entitlement; do not remove existing paid/community rights. Provide a correction/appeal route for mistaken matches. Do not expose roster or contact hashes in GitHub, page source, browser bundles or public Notion pages.

## Identity and concurrency architecture

GitHub Pages is a static frontend. It cannot enforce identity verification, cross-device duplicates or simultaneous seat claims alone. Deploy a separate private API and transactional PostgreSQL database; configure the review copy against that API only after launch approval. Existing applications remain untouched.

- Normalize email by trimming and lowercasing; do not strip dots or plus tags automatically across arbitrary providers. Normalize phone with a country selector and libphonenumber to E.164, then verify it.
- Generate server-side HMAC-SHA256 identity lookup keys with a secret pepper. Store contact values encrypted for authorised support use. Plain SHA hashes are insufficient protection for real phone numbers. The prototype stores only ordinary hashes of fictional input locally and is not production identity storage.
- Enforce a unique active seat, unique active campaign person, unique active campaign email key and unique active campaign phone key. A match of either email OR phone blocks another seat, even with the other contact changed or a different domain selected.
- One transaction must lock inventory, upsert canonical identity, screen eligibility and insert a hold. Unique constraints resolve racing requests. Return HTTP 409 for unavailable inventory and a private generic duplicate message. Never reveal another person’s identity or seat.
- Use an idempotency key on hold and confirmation requests; replays return the same result. Reject mismatched/expired OTP tokens, reuse of verification grants, tampered seat IDs and client-supplied status or entitlement dates.
- Identity matching limits duplication by verified contacts; it cannot prove one biological person across entirely different contact identities. Optional manual review and verified LinkedIn ownership can strengthen suspicious-case checks.
- Add rate limits, OTP resend limits, bot protection, server-side validation, scoped sessions and admin RBAC. Keep privileged keys out of static files. Use CORS allowlisting for the deployed frontend and appropriate CSRF protection for cookie sessions.

## API contract

| Endpoint | Responsibility |
|---|---|
| GET /campaigns/BF2026/seats?domain=HR | Public seat IDs/status only; no names or contacts |
| POST /applications | Record initial eligibility snapshot before campaign joining |
| POST /verifications/email and /phone | Rate-limited OTP delivery |
| POST /verifications/confirm | Short-lived server verification grants bound to applicant and contact |
| POST /holds | Verified contacts, membership check, atomic seat claim, idempotency key |
| POST /reservations/confirm | Hold token, consent version, atomic confirmation and outbox event |
| DELETE /reservations/me | Authenticated withdrawal; revoke campaign entitlement and release seat |
| POST /waitlist | Verified deduplicated queue entry |
| Admin review/revoke/reassign | RBAC, reason, private notification, audit history, preserved member rights |

## Stewardship and learning evidence

Proposed onboarding: within seven days, write a personal learning intention, choose a GICS case and define the first experiment. Monthly: produce one useful learning asset or experiment, share a short reflection and attend one peer review. Quarterly: demonstrate evidence of a practical improvement and support another learner. Define a simple rubric: problem clarity, decision rationale, working evidence and reusable contribution. Apply the relevant architecture perspectives rather than forcing 12 disconnected documents for every activity.

Publish only consented display names and contribution links, never contacts. Ownership is a responsibility to cultivate a shared learning space; other learners can still use the lab. Explain the exact free-access resource bundle before opening applications. Do not promise employment, certification, proprietary SAP systems or premium-tier benefits unless separately provided.

Inactivity proposal: private check-in after 30 days, support and an extension opportunity, then admin review after 60 days. No automatic removal for inactivity in the review version. Publish the final policy before participants consent.

## Systems of record

- GitHub: versioned frontend, public inventory definition, plan, schema and deployment. No participant data.
- Private database/API: authoritative identities, holds, allocations, membership snapshots, consent and entitlement events.
- Notion: optional private coordinator views, review tasks and contribution evidence links; never the transactional seat lock. Existing relevant hub: https://app.notion.com/p/3d2ce6de60898117ac92d0f349c0dbb0 . No existing Notion pages changed.
- Google Drive: optional restricted evidence folders; discovered SuperLabs folder: https://drive.google.com/drive/folders/1aJBs1Ssu1Nk8mRczT0Y3Q8kBdCiUh_7T . Do not change folder access automatically.
- LinkedIn: optional supporting profile and contribution visibility; a people-search connector does not authenticate applicants. No profile scraping or contact outreach is part of this replica.

## Implementation sequence

1. Review this independent page and confirm cohort dates, entitlement scope, global one-seat rule and contribution expectations.
2. Provision the private backend, schema migrations and secret management. Seed exactly 240 seats per domain from catalog.json.
3. Connect email/mobile OTP services and the authoritative membership source. Implement the initial-membership snapshot and campaign join attribution.
4. Implement transaction-backed allocation, waitlist, admin review, expiry jobs and an idempotent entitlement outbox/reconciler.
5. Run acceptance tests below using isolated test identities and a test membership roster. Review mobile accessibility and iframe behavior.
6. Open the new campaign route only when backend checks pass. Add links to existing applications only at the location the founder later specifies.
7. Daily reconciliation: confirmed allocations vs campaign access; pending provisioning retries; existing-member conflicts; expired holds; aggregate inventory. At cohort end expire only campaign entitlements. Schedule operational jobs in the backend during implementation, not as assumed existing automations.

## Required acceptance tests before launch

- Exactly 7 domains, 12 unique streams per domain, 20 unique labs and 1,680 distinct seat IDs.
- Same email with a different phone is blocked; same phone with a different email is blocked; case/whitespace email and equivalent phone formats match.
- Same contact in another domain is blocked; concurrent holds by one person yield at most one active allocation.
- Two verified people racing for one seat yield one success; stale holds can be reclaimed safely.
- Existing member is rejected before holding; an erroneous allocation is revoked without deleting existing rights.
- A genuinely new applicant joining through the checkout after application is not misclassified as an existing member.
- Invalid or expired OTP, replayed confirmation, forged identity or modified seat ID cannot grant access.
- Failed membership lookup fails closed to pending review; failed access provisioning is retryable and does not allocate twice.
- Browser refresh, multiple tabs, cross-device requests and API retries preserve consistent server state.
- Waitlist promotion, cancellation, reassignment and end-date expiry preserve all uniqueness constraints and audit history.
- Public responses and static repository contain no names, emails, phones, OTPs, identity hashes or secrets.
- All 1,680 seat buttons open the supplied checkout; blocked framing has a working fallback; keyboard focus returns to the seat after the dialog closes.

## Current prototype boundary

All seven domain matrices use the existing catalog. Seat buttons embed the supplied live checkout. A separate fictional-data demo checks local email OR phone hashes across domains and prevents local duplicate seats. It rejects self-declared existing members. It has no live roster, OTP provider, shared allocation database, waitlist processor, notifications or access provisioning. Browser-local checks are resettable and not sufficient for launch. Treat every inventory count as demo state, never live scarcity.
