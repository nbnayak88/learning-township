-- Design reference; not applied. API transactions, OTP checks, membership checks,
-- expired hold cleanup and entitlement outbox processing are still required.
CREATE TABLE campaigns (
 id text PRIMARY KEY,
 starts_at timestamptz NOT NULL,
 ends_at timestamptz NOT NULL CHECK (ends_at > starts_at)
);
CREATE TABLE seats (
 campaign_id text REFERENCES campaigns(id),
 domain text NOT NULL CHECK(domain IN ('HR','CX','FI','PROC','SCM','BTM','LIT')),
 stream_id text NOT NULL,
 lab_id text NOT NULL,
 PRIMARY KEY(campaign_id,domain,stream_id,lab_id)
);
CREATE TABLE people (
 id uuid PRIMARY KEY,
 email_key text UNIQUE NOT NULL, -- server HMAC; verified canonical email
 phone_key text UNIQUE NOT NULL, -- server HMAC; verified E.164 phone
 encrypted_contacts bytea NOT NULL
);
CREATE TABLE allocations (
 id uuid PRIMARY KEY,
 campaign_id text NOT NULL,
 domain text NOT NULL,
 stream_id text NOT NULL,
 lab_id text NOT NULL,
 person_id uuid NOT NULL REFERENCES people(id),
 email_key text NOT NULL,
 phone_key text NOT NULL,
 status text NOT NULL CHECK(status IN ('held','confirmed','expired','cancelled','revoked')),
 hold_expires_at timestamptz,
 membership_checked_at timestamptz NOT NULL,
 existing_member_at_application boolean NOT NULL CHECK(existing_member_at_application=false),
 consent_version text NOT NULL,
 idempotency_key text NOT NULL,
 created_at timestamptz NOT NULL DEFAULT now(),
 FOREIGN KEY(campaign_id,domain,stream_id,lab_id) REFERENCES seats,
 UNIQUE(campaign_id,idempotency_key),
 CHECK(status <> 'held' OR hold_expires_at IS NOT NULL)
);
CREATE UNIQUE INDEX one_active_seat ON allocations(campaign_id,domain,stream_id,lab_id) WHERE status IN ('held','confirmed');
CREATE UNIQUE INDEX one_active_person ON allocations(campaign_id,person_id) WHERE status IN ('held','confirmed');
CREATE UNIQUE INDEX one_active_email ON allocations(campaign_id,email_key) WHERE status IN ('held','confirmed');
CREATE UNIQUE INDEX one_active_phone ON allocations(campaign_id,phone_key) WHERE status IN ('held','confirmed');
-- Revalidate email_key/phone_key against verified person server-side in the same
-- transaction. Clients have no direct table writes. Lock seat and person before
-- transition; mark stale holds expired before inserting replacements.
CREATE TABLE entitlement_outbox (
 id uuid PRIMARY KEY,
 allocation_id uuid NOT NULL REFERENCES allocations(id),
 event_type text NOT NULL CHECK(event_type IN ('grant','revoke')),
 event_version integer NOT NULL,
 processed_at timestamptz,
 UNIQUE(allocation_id,event_type,event_version)
);
CREATE TABLE allocation_audit (
 id uuid PRIMARY KEY,
 allocation_id uuid NOT NULL REFERENCES allocations(id),
 actor_id text NOT NULL,
 action text NOT NULL,
 reason text NOT NULL,
 created_at timestamptz NOT NULL DEFAULT now()
);
