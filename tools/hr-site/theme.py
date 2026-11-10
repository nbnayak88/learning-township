import os, re, glob, html, posixpath
import markdown

SITE_TITLE = "BTM11 Bootcamp Demos · The Northstar Architecture"
WEBINAR = "https://hub.successlabsacademy.com/web/checkout/694af8798dd872a219700dd3"

SECTORS = [
    ("01-BTM11-ENE-energy", "energy", "Energy", "OmniVerse Energy"),
    ("02-BTM11-MAT-materials", "materials", "Materials", "OmniForge Materials"),
    ("03-BTM11-IND-industrials", "industrials", "Industrials", "OmniWorks Industrial Systems"),
    ("04-BTM11-CD-consumer-discretionary", "consumer-discretionary", "Consumer Discretionary", "OmniVibe"),
    ("05-BTM11-CS-consumer-staples", "consumer-staples", "Consumer Staples", "OmniDaily"),
    ("06-BTM11-HC-health-care", "health-care", "Health Care", "OmniHealth"),
    ("07-BTM11-FIN-financials", "financials", "Financials", "OmniCapital Financial Group"),
    ("08-BTM11-IT-information-technology", "information-technology", "Information Technology", "OmniTech"),
    ("09-BTM11-COM-communication-services", "communication-services", "Communication Services", "OmniConnect"),
    ("10-BTM11-UT-utilities", "utilities", "Utilities", "OmniGrid"),
    ("11-BTM11-RE-real-estate", "real-estate", "Real Estate", "OmniSpace"),
]
DEMO_LABEL = {"01": "Demo 01 · Case baseline", "02": "Demo 02 · EA, Signavio, LeanIX, Clean Core", "03": "Demo 03 · AI/GenAI, RAG, agents on SAP BTP", "04": "Demo 04 · Knowledge graph, context engineering", "05": "Demo 05 · Integration, Advanced Event Mesh", "06": "Demo 06 · Basis, AIOps, autonomous ops", "07": "Demo 07 · Data foundation, data products", "08": "Demo 08 · Security, zero trust for AI agents", "09": "Demo 09 · AI governance, LLMOps", "10": "Demo 10 · Migration path, Clean Core readiness", "11": "Demo 11 · Operating model, FinOps", "12": "Demo 12 · Resilience, failure drills", "13": "Demo 13 · Sustainability, green IT", "14": "Demo 14 · Low-code, pro-code, vibe code", "15": "Demo 15 · Regulation (case countries)"}

CSS = """
:root{--bg1:hsl(150 55% 97%);--bg2:hsl(200 70% 97%);--bg3:hsl(335 75% 97%);--card:hsl(0 0% 100% / .86);--ink:hsl(205 40% 14%);--muted:hsl(205 15% 38%);--line:hsl(205 30% 88%);--accent:hsl(210 62% 34%);--chip:hsl(195 45% 95%);--warn:hsl(45 100% 95%);--warnline:hsl(42 80% 62%);--deep:hsl(205 55% 20%);--lime:hsl(95 55% 46%);--pink:hsl(343 82% 62%);--sla-reading-progress-color:var(--deep)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;color:var(--ink);background:linear-gradient(160deg,var(--bg1),var(--bg2) 55%,var(--bg3)) fixed;font:400 16px/1.7 Comfortaa,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
button,input,select,textarea,dialog{font-family:Comfortaa,system-ui,sans-serif}
a{color:var(--accent)}
header.top{position:sticky;top:0;z-index:50;background:linear-gradient(100deg,hsl(95 65% 94%),hsl(190 65% 95%) 50%,hsl(335 80% 95%));border-bottom:1px solid var(--line);box-shadow:0 6px 18px hsl(205 40% 40% / .08)}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px}
.hdr{display:grid;grid-template-columns:1fr minmax(0,1.6fr) auto;gap:16px;align-items:center;padding-top:10px;padding-bottom:10px}
.hl a.brand{font-weight:700;text-decoration:none;color:var(--deep);font-size:15px;line-height:1.3;display:block}
.hl .meta{display:block;margin-top:2px}
.hq{margin:0;text-align:center;font-weight:600;font-size:15px;line-height:1.5;color:var(--deep);padding:8px 14px;border-radius:16px;background:hsl(0 0% 100% / .55);border:1px solid hsl(0 0% 100% / .8)}
.hq::before{content:"“";color:var(--pink);font-weight:700;margin-right:4px}
.hq::after{content:"”";color:var(--pink);font-weight:700;margin-left:2px}
.hr{display:flex;flex-direction:column;align-items:flex-end;text-align:right;max-width:210px}
.hr img{display:block;width:64px;height:auto;border-radius:14px}
.hr .tag{margin:4px 0 0;font-size:11px;line-height:1.35;font-weight:600;color:var(--deep)}
main{padding:24px 0 56px}
article{background:var(--card);border:1px solid hsl(0 0% 100% / .9);border-radius:22px;padding:22px 26px;box-shadow:0 10px 30px hsl(205 40% 40% / .10);backdrop-filter:blur(6px)}
h1{font-size:clamp(24px,4vw,34px);line-height:1.25;margin:0 0 8px;font-weight:700;letter-spacing:-.01em;color:var(--deep)}
h2{margin-top:34px;padding-top:10px;border-top:1px solid var(--line);font-size:22px;font-weight:700;color:var(--deep)}
h3{font-size:18px;font-weight:700}
blockquote{margin:16px 0;padding:10px 16px;background:var(--warn);border-left:4px solid var(--warnline);border-radius:12px}
blockquote p{margin:6px 0}
.tw{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:14px;background:hsl(0 0% 100% / .7)}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{padding:9px 11px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:linear-gradient(90deg,hsl(95 55% 93%),hsl(190 55% 94%));white-space:nowrap;font-weight:700}
tr:last-child td{border-bottom:0}
code{background:var(--chip);padding:1px 6px;border-radius:6px;font-size:.88em}
.meta{color:var(--muted);font-size:12px}
.chips a{display:inline-block;margin:3px 5px 3px 0;padding:4px 12px;min-height:30px;border:1px solid var(--line);border-radius:999px;background:hsl(0 0% 100% / .8);text-decoration:none;font-size:12px;font-weight:600;color:var(--deep)}
.chips a:hover{border-color:var(--lime);background:hsl(95 65% 95%)}
.done{font-weight:700}
.na{color:var(--muted)}
footer{color:var(--muted);font-size:12px;padding:0 0 32px}
.cta{display:inline-block;padding:11px 22px;border-radius:999px;background:linear-gradient(100deg,hsl(95 60% 42%),hsl(165 60% 38%) 55%,hsl(205 65% 40%));color:hsl(0 0% 100%)!important;font-weight:700;text-decoration:none;box-shadow:0 8px 22px hsl(165 55% 35% / .30);transition:transform .15s,box-shadow .15s;min-height:44px;line-height:1.4}
.cta:hover{transform:translateY(-1px) scale(1.02);box-shadow:0 12px 28px hsl(165 55% 35% / .42)}
.cta.sm{padding:5px 14px;font-size:12px;min-height:32px;margin-top:6px}
.cta.ghost{background:hsl(0 0% 100% / .85);color:var(--deep)!important;border:1px solid var(--line);box-shadow:none}
.hero{padding:30px 0 10px;text-align:left}
.pre{display:inline-block;padding:4px 12px;border-radius:999px;background:hsl(95 65% 92%);color:var(--deep);font-size:12px;font-weight:700;letter-spacing:.02em}
.hero h1{font-size:clamp(30px,5.2vw,50px);line-height:1.15;margin:14px 0 12px;letter-spacing:-.02em}
.hero .sub{font-size:clamp(16px,2vw,19px);color:var(--muted);max-width:720px;margin:0 0 14px}
.ticks{list-style:none;padding:0;margin:0 0 20px}.ticks li{padding:4px 0 4px 28px;position:relative}.ticks li::before{content:"✓";position:absolute;left:0;color:hsl(95 55% 36%);font-weight:700}
.row{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.note{font-size:12px;color:var(--muted);margin-top:10px}
section.blk{margin-top:34px}
section.blk>h2{border-top:0;margin-top:0}
.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}
.card{background:var(--card);border:1px solid hsl(0 0% 100% / .9);border-radius:22px;padding:20px 22px;box-shadow:0 10px 30px hsl(205 40% 40% / .09)}
.card h3{margin:6px 0 8px;color:var(--deep)}
.num{font-weight:700;font-size:13px;color:hsl(343 70% 50%)}
.vs{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.vs .card.a{border-top:5px solid hsl(95 55% 50%)}.vs .card.b{border-top:5px solid hsl(205 65% 50%)}
.pills a{display:inline-block;min-width:34px;text-align:center;margin:2px 3px 2px 0;padding:3px 9px;border:1px solid var(--line);border-radius:10px;background:hsl(0 0% 100% / .85);font-size:12px;font-weight:700;text-decoration:none;color:var(--deep)}
.pills a:hover{background:hsl(95 65% 93%);border-color:hsl(95 55% 50%)}
details{background:var(--card);border:1px solid hsl(0 0% 100% / .9);border-radius:16px;padding:12px 18px;margin:10px 0;box-shadow:0 6px 18px hsl(205 40% 40% / .07)}
summary{cursor:pointer;font-weight:700;color:var(--deep);min-height:28px}
.close{margin-top:38px;text-align:center;padding:34px 20px;border-radius:26px;background:linear-gradient(120deg,hsl(95 65% 92%),hsl(190 65% 93%) 50%,hsl(335 80% 94%));border:1px solid hsl(0 0% 100% / .9)}
.close h2{border:0;margin:0 0 8px}
.legend{columns:2 300px;font-size:14px}.legend div{break-inside:avoid;padding:2px 0}
@media (max-width:720px){.hdr{grid-template-columns:1fr auto;grid-template-areas:"l r" "q q"}.hl{grid-area:l}.hr{grid-area:r}.hq{grid-area:q;font-size:14px}article{padding:16px}.hr img{width:56px}}
"""

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;600;700&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<header class="top"><div class="wrap hdr"><div class="hl"><a class="brand" href="{root}index.html">{site}</a><span class="meta">SuccessLabs Academy · aspirational case studies</span><a class="cta sm" href="{webinar}" target="_blank" rel="noopener">Join the free webinar</a></div><p class="hq">{quote}</p><div class="hr"><a href="{root}index.html"><img src="{root}assets/successlabs-academy-logo.png" alt="SuccessLabs Academy logo: a flask with a globe wearing a graduation cap" width="64" height="64"></a><p class="tag">Architecting experiences for a better world.</p></div></div></header>
{progress}
<main><div class="wrap">{nav}{content}</div></main>
<footer><div class="wrap">Educational demonstration material built on aspirational case studies. Nothing here asserts an executed client implementation. <a href="{gh}">View source on GitHub</a>. Fonts load from Google Fonts and need network access to render as Comfortaa.</div></footer>
</body></html>"""

CTA_BOX = f'''<section class="close"><h2>Start with the target, then choose the path</h2><p>Join the free webinar and see how the Northstar architecture connects to the demos on this site.</p><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><p class="note">Free webinar · opens the registration page</p></section>'''

PROGRESS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reading-progress.html")).read().replace("hsl(195 20% 85% / .4)", "hsl(205 25% 80% / .55)")

QUOTES = {
    "01": "A good case begins by naming what is true, and what is still unknown.",
    "02": "Clean architecture is the courage to say no to the shortcut that costs the future.",
    "03": "An assistant is only as trustworthy as the context you let it hold.",
    "04": "Connect the facts, and the answers start to find their own way.",
    "05": "When systems speak in events, the whole enterprise can finally listen.",
    "06": "Quiet operations are built long before the alarm rings.",
    "07": "Data earns trust when someone owns it and someone can explain it.",
    "08": "Give every agent a name, a purpose and only the keys it needs.",
    "09": "Responsible AI is not a brake; it is the steering.",
    "10": "The best migration is a sequence of safe, reversible steps.",
    "11": "A service without an owner is a hope, not a design.",
    "12": "Rehearse the worst day, and the real one becomes manageable.",
    "13": "What we measure honestly, we can improve responsibly.",
    "14": "Build fast, build together, and keep the guardrails close.",
    "15": "Good architecture knows the rules of every country it serves.",
    "index": "Every great architecture begins with a question worth asking.",
}


