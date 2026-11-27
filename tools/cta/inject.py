#!/usr/bin/env python3
"""Inject the shared SuccessLabs membership CTA in final static HTML build output.

Idempotent, stdlib-only, and non-destructive: preserves source files, existing CTAs,
scripts, layout, and external links. Executed after assembling the Pages artifact.
"""
from pathlib import Path
import argparse
import re
import sys

DIAMOND = "https://hub.successlabsacademy.com/web/checkout/6acddf11e7fb7ec634b9b08a"
GOLD = "https://hub.successlabsacademy.com/web/checkout/6acdde57b1df6a998599d4c1"
SILVER = "https://hub.successlabsacademy.com/web/checkout/6acddceafab478f3ec7968de"
MARKER = "sla-membership-cta-v1"
STYLES = """<style id="sla-membership-cta-styles">
.sla-membership-cta{box-sizing:border-box;position:relative;margin:28px auto 20px;max-width:1200px;padding:18px 22px;background:linear-gradient(115deg,#e8ffd4 0%,#d7f7c6 42%,#f4ffed 100%);color:#173d20;border:1px solid #acd992;border-radius:18px;box-shadow:0 10px 28px rgba(37,91,36,.09);font:500 14px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif;clear:both}
.sla-membership-cta *{box-sizing:border-box}
.sla-membership-cta .sla-membership-eyebrow{font-size:11px;letter-spacing:.12em;text-transform:uppercase;font-weight:800;color:#3f772e}
.sla-membership-cta h2{color:#173d20;font-size:clamp(19px,2.6vw,27px);font-weight:800;line-height:1.3;margin:5px 0 6px}
.sla-membership-cta p{margin:0 0 14px;color:#365340;font-size:14px}
.sla-membership-options{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.sla-membership-options a{display:flex;min-height:52px;align-items:center;justify-content:space-between;gap:10px;padding:12px 14px;border:1px solid #96cb7d;border-radius:11px;background:#fff;color:#194b28!important;font-size:13px;font-weight:750;text-decoration:none!important;line-height:1.3;transition:transform .18s ease,box-shadow .18s ease}
.sla-membership-options a:hover{transform:translateY(-2px);box-shadow:0 5px 12px rgba(29,86,30,.14);background:#f8fff4}
.sla-membership-options a:focus-visible{outline:3px solid #17652d;outline-offset:3px}
.sla-membership-options a[data-tier="diamond"]{background:#205c2a;color:#fff!important;border-color:#205c2a}
.sla-membership-options a[data-tier="diamond"]:hover{background:#164b21}
.sla-membership-options a span:last-child{flex:none;font-size:18px}
@media(max-width:680px){.sla-membership-cta{margin:16px 12px;padding:16px}.sla-membership-options{grid-template-columns:1fr}.sla-membership-options a{min-height:48px}}
@media(prefers-reduced-motion:reduce){.sla-membership-options a{transition:none}.sla-membership-options a:hover{transform:none}}
</style>"""
COMPONENT = f"""<!-- {MARKER}:begin -->
{STYLES}
<section class="sla-membership-cta" aria-labelledby="sla-membership-cta-title">
  <div class="sla-membership-eyebrow">SuccessLabs Academy · Your next learning milestone</div>
  <h2 id="sla-membership-cta-title">Turn Learning into Career Mastery</h2>
  <p>Explore a membership or certification pathway that matches your ambition. Architecting Experiences for a Better World.</p>
  <nav class="sla-membership-options" aria-label="SuccessLabs membership and certification pathways">
    <a data-tier="diamond" href="{DIAMOND}" target="_blank" rel="noopener noreferrer"><span>Join Diamond Certification</span><span aria-hidden="true">↗</span></a>
    <a data-tier="gold" href="{GOLD}" target="_blank" rel="noopener noreferrer"><span>Join Gold Certification</span><span aria-hidden="true">↗</span></a>
    <a data-tier="silver" href="{SILVER}" target="_blank" rel="noopener noreferrer"><span>Join Silver Membership</span><span aria-hidden="true">↗</span></a>
  </nav>
</section>
<!-- {MARKER}:end -->"""
RE_BODY = re.compile(r"</body\s*>", re.I)
RE_HTML = re.compile(r"<html(?:\s|>)", re.I)
RE_MARKER = re.compile(r"<!--\s*"+MARKER+r":begin\s*-->.*?<!--\s*"+MARKER+r":end\s*-->", re.S | re.I)

def inject(source):
    # Reuse the component if already present; guarantees one CTA on repeated deploys.
    source = RE_MARKER.sub("", source)
    if not RE_HTML.search(source) or not RE_BODY.search(source):
        return source, False
    output = RE_BODY.sub(lambda m: COMPONENT+"\n"+m.group(0), source, count=1)
    return output, True

def main():
    p = argparse.ArgumentParser()
    p.add_argument("site", type=Path)
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    if not args.site.is_dir():
        sys.exit(f"Missing site directory: {args.site}")
    files = sorted(args.site.rglob("*.html"))
    changed = 0
    eligible = 0
    for path in files:
        original = path.read_text(encoding="utf-8")
        output, is_eligible = inject(original)
        if not is_eligible:
            continue
        eligible += 1
        if original != output:
            changed += 1
            if not args.check:
                path.write_text(output, encoding="utf-8")
        if output.count(f"<!-- {MARKER}:begin -->") != 1 or any(url not in output for url in (DIAMOND,GOLD,SILVER)):
            sys.exit(f"Invalid CTA in {path}")
    if args.check and changed:
        sys.exit(f"CTA not normalized in {changed} files")
    if not files or not eligible:
        sys.exit("No eligible HTML pages found")
    print(f"SuccessLabs CTA: {eligible} eligible HTML pages; {changed} {'noncompliant' if args.check else 'updated'}; {len(files)-eligible} skipped (non-document fragments)")

if __name__ == "__main__":
    main()
