#!/usr/bin/env python3
"""Builds the HR01-HR12 and CRM01-CRM12 public sites straight from the repo content.
Run by .github/workflows/hr-site.yml on every push; no manual steps.
Usage: python3 tools/hr-site/build.py <output_dir>"""
import os, re, glob, html, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from theme import CSS, TEMPLATE, PROGRESS, WEBINAR
import markdown

REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
ACADEMIES = [
    dict(key="hr", dir="01-HR-Human-Capital-Capability-Academy-Workforce-Monday", prefix="HR", name="HR", day="Workforce Monday", hub="HR · Workforce Monday Series", h1="Architect the HR enterprise, series by series",
         q_hub="Twelve series, one question: what must the HR system promise?", q_sector="Every sector hires, develops and protects people differently, so listen before you automate."),
    dict(key="fi", dir="03-FI-Finance-Capability-Academy-Finance-Wednesday", prefix="FI", name="Finance", day="Finance Wednesday", hub="Finance · Finance Wednesday Series", h1="Architect the finance enterprise, series by series",
         q_hub="Twelve series, one question: what must the finance function be able to prove?", q_sector="Every sector closes, pays and reports differently, so listen before you automate."),
    dict(key="proc", dir="04-PROC-Procurement-Capability-Academy-Procurement-Thursday", prefix="PROC", name="Procurement", day="Procurement Thursday", hub="Procurement · Procurement Thursday Series", h1="Architect the procurement enterprise, series by series",
         q_hub="Twelve series, one question: what must procurement be able to prove?", q_sector="Every sector buys, contracts and depends on suppliers differently, so listen before you automate."),
    dict(key="scm", dir="05-SCM-Supply-Chain-Management-Capability-Academy-Supply-Chain-Friday", prefix="SCM", name="Supply Chain", day="Supply Chain Friday", hub="Supply Chain · Supply Chain Friday Series", h1="Architect the supply chain enterprise, series by series",
         q_hub="Twelve series, one question: what must the supply chain be able to promise?", q_sector="Every sector moves goods and information differently, so listen before you automate."),
    dict(key="btm", dir="06-BTM-Business-Transformation-Capability-Academy-Transformation-Saturday", prefix="BTM", name="Business Transformation", day="Transformation Saturday", hub="Business Transformation · Transformation Saturday Series", h1="Architect the transformed enterprise, series by series",
         q_hub="Twelve series, one question: what must the enterprise be able to prove it changed?", q_sector="Every sector transforms differently, so listen before you automate."),
    dict(key="crm", dir="02-CRM-Customer-Experience-Capability-Academy-Revenue-Tuesday", prefix="CRM", name="Customer Experience", day="Revenue Tuesday", hub="Customer Experience · Revenue Tuesday Series", h1="Architect the customer enterprise, series by series",
         q_hub="Twelve series, one question: what must the customer experience promise?", q_sector="Every sector earns customer trust differently, so listen before you automate."),
]
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "docs"))
DEMOS = os.path.join(REPO, "docs", "btm11-demos")
from theme import DEMO_LABEL


def demo_list(slug, prefix):
    d = os.path.join(DEMOS, slug)
    if not os.path.isdir(d):
        return ""
    items = ""
    for f in sorted(glob.glob(d + "/[0-9][0-9]-*.html")):
        n = os.path.basename(f)[:2]
        items += f'<li><a href="{prefix}btm11-demos/{slug}/{os.path.basename(f)}">{html.escape(DEMO_LABEL.get(n, n))}</a></li>'
    return f'<section class="blk" id="demos"><h2>Bootcamp demos</h2><p>Hands-on teaching demos for this sector, from the case baseline to industry regulation.</p><ul>{items}</ul></section>' if items else ""


GH = "https://github.com/nbnayak88/learning-township/"
GHB, GHT = GH + "blob/main/", GH + "tree/main/"
ENT = {"ENE": "OmniVerse Energy", "MAT": "OmniForge Materials", "IND": "OmniWorks Industrial Systems", "CD": "OmniVibe", "CS": "OmniDaily", "HC": "OmniHealth Systems", "FIN": "OmniCapital Financial Group", "IT": "OmniTech", "COM": "OmniConnect", "UT": "OmniGrid", "RE": "OmniSpace"}
SECTOR_NAME = {"ENE": "Energy", "MAT": "Materials", "IND": "Industrials", "CD": "Consumer Discretionary", "CS": "Consumer Staples", "HC": "Health Care", "FIN": "Financials", "IT": "Information Technology", "COM": "Communication Services", "UT": "Utilities", "RE": "Real Estate"}
LEVELS = [("01-Pre-Foundation", "Level 1 · Pre-Foundation"), ("02-Foundation", "Level 2 · Foundation"), ("03-Essentials", "Level 3 · Essentials"), ("04-Advanced", "Level 4 · Advanced"), ("05-Ultimate", "Level 5 · Ultimate")]
FORMATS = ["webinar", "workshop", "sprint", "bootcamp", "masterclass", "superclass", "hackathon", "challenge-21-day"]
FLABEL = {"challenge-21-day": "21-day challenge"}
QUOTES = {
 "HR01": "A workforce record is a promise someone will rely on later.",
 "HR02": "Hiring is a decision about a person, not a match between two documents.",
 "HR03": "Performance is designed into the system long before it appears on a scorecard.",
 "HR04": "Leaders are grown on purpose, one honest decision at a time.",
 "HR05": "Fair reward is a rule people can explain, and a result they can trust.",
 "HR06": "Learning counts when it changes what a person is trusted to do.",
 "HR07": "A payroll run can succeed and still get a person's pay wrong.",
 "HR08": "Time is the first promise a workplace makes and the first it can break.",
 "HR09": "Insight is only useful when someone owns the decision it informs.",
 "HR10": "Experience is what the employee feels after the process has finished.",
 "HR11": "Responsible workforce AI starts with a decision, an owner and evidence.",
 "HR12": "A message that arrives is not the same as access that is right.",
 "FI01": "A close is finished when the numbers can be explained, not when the calendar says so.",
 "FI02": "Paying correctly is a promise to a supplier and a control for the business.",
 "FI03": "Revenue is real when the order, the invoice and the cash tell the same story.",
 "FI04": "Tax is a set of rules that change, so the evidence must be ready before the question.",
 "FI05": "Cash is the one number a business cannot afford to be surprised by.",
 "FI06": "A plan earns trust when its assumptions have owners and its versions have history.",
 "FI07": "Profit is a decision about allocation, so show the rule before the result.",
 "FI08": "An asset record is a promise about what the business owns and what it is worth.",
 "FI09": "A control is only real when someone owns it and evidence can prove it ran.",
 "FI10": "A finance number is useful when its definition and lineage travel with it.",
 "FI11": "Responsible finance AI starts with a decision, an owner and evidence.",
 "FI12": "Connected finance is only as reliable as the weakest handoff between systems.",
 "PROC01": "Strategy is the decision about what to buy, from whom and why, made before the first purchase order.",
 "PROC02": "A fair sourcing decision can be explained to the supplier who lost.",
 "PROC03": "A contract is a promise that someone must still remember to keep.",
 "PROC04": "Suppliers perform best when someone owns the relationship, not only the invoice.",
 "PROC05": "A purchase is complete when what was ordered, received and paid all agree.",
 "PROC06": "Resilience is decided in the quiet weeks before the disruption.",
 "PROC07": "Quality is what the supplier delivers on the day nobody is watching.",
 "PROC08": "A saving counts when finance can see it and the business can keep it.",
 "PROC09": "Risk in the supply chain is only visible to those who ask the supplier's supplier.",
 "PROC10": "Spend data is useful when everyone agrees what a category means.",
 "PROC11": "Responsible procurement AI starts with a decision, an owner and evidence.",
 "PROC12": "Connected procurement is only as reliable as the weakest handoff to a supplier.",
 "SCM01": "A supply chain is a set of promises, so design the network around the ones you can keep.",
 "SCM02": "A forecast is useful when everyone can see the assumption behind the number.",
 "SCM03": "A plan is balanced when demand, capacity and inventory agree on one version.",
 "SCM04": "The factory floor tells the truth about the plan, so listen to it.",
 "SCM05": "A shipment is delivered when the customer can prove it arrived as promised.",
 "SCM06": "Inventory is a decision about risk, held in a warehouse.",
 "SCM07": "Quality is a record you can trace, not a claim you can only make.",
 "SCM08": "Suppliers respond best to signals they can see early.",
 "SCM09": "A sustainability claim is only as strong as the evidence behind it.",
 "SCM10": "Visibility matters when someone owns the decision it triggers.",
 "SCM11": "Responsible supply chain AI starts with a decision, an owner and evidence.",
 "SCM12": "A supply ecosystem is only as reliable as the weakest handoff between partners.",
 "BTM01": "Strategy is a set of choices that someone is accountable for making.",
 "BTM02": "An architecture is a decision record, not a diagram.",
 "BTM03": "A process works when its owner can show where it breaks.",
 "BTM04": "Change lands when people can see what is different for them on Monday.",
 "BTM05": "Value is real when someone can show where it appears in the numbers.",
 "BTM06": "Data is trusted when its owner, definition and lineage travel with it.",
 "BTM07": "The cloud is a set of guardrails before it is a set of services.",
 "BTM08": "An ecosystem is only as reliable as its weakest handoff.",
 "BTM09": "Trust is built before the incident and tested during it.",
 "BTM10": "A transformation dashboard is honest when it shows what is not yet measured.",
 "BTM11": "Responsible enterprise AI starts with a decision, an owner and evidence.",
 "BTM12": "Future-ready means the next question has somewhere to land.",
 "CRM01": "A customer is one person, however many systems know a different version of them.",
 "CRM02": "Engagement earns its place when it is relevant, consented and easy to stop.",
 "CRM03": "Revenue is a promise kept in sequence, from first interest to final invoice.",
 "CRM04": "A basket is only as trustworthy as the price, stock and promise behind it.",
 "CRM05": "A fast answer is only service when the customer's problem is actually solved.",
 "CRM06": "Customers remember how the whole journey felt, not which team handled which step.",
 "CRM07": "Recurring revenue is renewed trust, earned again every cycle.",
 "CRM08": "Good operations make the right thing the easy thing at every handoff.",
 "CRM09": "Customer insight is useful only when someone owns the decision it changes.",
 "CRM10": "A digital experience is a promise the customer can test in seconds.",
 "CRM11": "Responsible customer AI starts with a decision, an owner and evidence.",
 "CRM12": "An ecosystem is only as strong as the weakest handoff between its partners.",
}
Q_LESSON = "A story earns its place when it changes the decision you make next."
SUBS = [(r"is a \*\*fictional educational case\*\*", "is an **aspirational case study**"), (r"\bfictional educational cases\b", "aspirational case studies"), (r"\bfictional educational case\b", "aspirational case study"), (r"\bfictional cases\b", "aspirational case studies"), (r"\bfictional case\b", "aspirational case study"), (r"\bfictional\b", "aspirational"), (r"\bFictional\b", "Aspirational")]


def clean(t):
    for a, b in SUBS:
        t = re.sub(a, b, t)
    return t


def fld(txt, name):
    m = re.search(r"\*\*" + re.escape(name) + r":\*\*\s*(.+?)\s*(?:\n|$)", txt)
    return m.group(1).strip().strip("`") if m else ""


def section(txt, head):
    m = re.search(r"^## " + re.escape(head) + r"\s*\n(.*?)(?=^## |\Z)", txt, re.M | re.S)
    return " ".join(m.group(1).split()) if m else ""


def md2html(md):
    h = markdown.markdown(md, extensions=["tables", "sane_lists", "toc"], output_format="html5")
    return h.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")


INTERNAL = re.compile(r"github\.com|githubusercontent|notion\.(com|so|site)|docs\.google\.com|drive\.google\.com|\.pptx|\.xlsx", re.I)


PROSE = re.compile(r"Matching companions|synchroni|readback|Standing user approval|sector index|Planning reference|Notion|Google (Doc|Slides|Sheets|Drive)|\bDrive\b|GitHub|\bgit\b|Drive refresh", re.I)


def sanitize(md):
    """Public pages carry no repo, Notion or Google Workspace references; official resources stay."""
    out, skip = [], False
    for line in md.splitlines():
        if re.match(r"#{1,3}\s+(?:\d+\.\s+)?(Companion workspace|Source and (edition|companion) record|Matching companions)", line):
            skip = True
            continue
        if skip and re.match(r"#{1,3}\s", line):
            skip = False
        if skip:
            continue
        s = line.strip()
        if INTERNAL.search(s) and not re.match(r"R\d+\b", s):
            continue
        if re.match(r"S\d+b?\s+[—-]", s) or s.startswith(("Reviewed ", "Matching editions")):
            continue
        line = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: m.group(0) if m.group(2).startswith("http") and not INTERNAL.search(m.group(2)) else m.group(1), line)
        if not s.startswith("#") and PROSE.search(s):
            if s.startswith("|"):
                continue
            kept = [x for x in re.split(r"(?<=[.;])\s+", line) if not PROSE.search(x)]
            if not kept:
                continue
            line = " ".join(kept)
        if re.match(r"R\d+\b", s):
            line = re.sub(r"(https?://\S+)", r"[\1](\1)", line)
        out.append(line)
    return "\n".join(out)


def relink(md, srcfile):
    d = os.path.dirname(srcfile)
    def sub(m):
        text, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        path, _, frag = target.partition("#")
        rel = os.path.relpath(os.path.normpath(os.path.join(d, path)), REPO).replace(os.sep, "/")
        return f"[{text}]({GHB}{rel}{'#' + frag if frag else ''})"
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", sub, md)


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)


def rel(p):
    return os.path.relpath(p, REPO).replace(os.sep, "/")


def page(site, title, desc, root, quote, nav, content, gh):
    return TEMPLATE.format(title=html.escape(title), desc=html.escape(desc), css=CSS, root=root, site=site, quote=quote, progress=PROGRESS, nav=nav, content=content, webinar=WEBINAR, gh=gh, body="")


def cta(series_title, A=None):
    return f'<section class="close"><h2>Build the decision before the tool</h2><p>Join the free webinar and learn to architect decisions you can explain, govern and recover.</p><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><p class="note">Free webinar · opens the registration page</p></section>'


def load_series(sdir, A):
    b = os.path.basename(sdir)
    m = re.match(r"([A-Z]+\d\d)-([A-Z0-9]+)-(.+)$", b)
    code, short, title = m.group(1), m.group(2), m.group(3).replace("-", " ").replace(" And ", " and ")
    title = title.replace("AI Powered", "AI-Powered").replace("Procure to Pay", "Procure-to-Pay").replace("Process Driven High Performance", "Process-Driven, High-Performance").replace("Change Ready Adaptive", "Change-Ready, Adaptive").replace("Value Driven", "Value-Driven").replace("Data Driven", "Data-Driven").replace("Digital Cloud Enabled", "Digital, Cloud-Enabled").replace("Trust Risk Resilient", "Trust and Risk-Resilient").replace("Sustainable Future Ready", "Sustainable, Future-Ready").replace("Future Ready", "Future-Ready").replace("Logistics Transportation", "Logistics & Transportation").replace("Quality Compliance", "Quality & Compliance").replace("Cost Profitability", "Cost & Profitability").replace("Governance Risk", "Governance & Risk").replace("Quality Performance", "Quality & Performance").replace("Risk Sustainable", "Risk & Sustainable").replace("Rewards Performance", "Rewards & Performance").replace("Learning Mobility", "Learning & Mobility")
    sectors = []
    for d in sorted(glob.glob(sdir + "/[0-9][0-9]-[A-Z]*-*")):
        sb = os.path.basename(d)
        mm = re.match(r"\d\d-[A-Z]+\d\d-([A-Z]+)-(.+)$", sb)
        if not mm:
            continue
        sc, slug = mm.group(1), mm.group(2)
        lessons = sorted(f for f in glob.glob(d + "/0-The-Origin-Story/sprint/*.md") if not f.endswith("README.md"))
        comp = sorted(glob.glob(d + "/0-The-Origin-Story/sprint/companions/*"))
        rows = []
        for lv, lvl in LEVELS:
            for f in FORMATS:
                p = f"{d}/{lv}/{f}/README.md"
                if os.path.exists(p):
                    t = open(p, encoding="utf-8").read()
                    rows.append(dict(level=lvl, fmt=FLABEL.get(f, f.capitalize()), pid=fld(t, "Pathway ID"), idx=fld(t, "Catalog Index"), dur=fld(t, "Duration"), obj=clean(section(t, "Learning objective")), out=clean(section(t, "Student output")), path=rel(p)))
        sectors.append(dict(code=sc, slug=slug, name=SECTOR_NAME.get(sc, slug.replace("-", " ").title()), ent=ENT.get(sc, sc), dir=sb, lesson=lessons[0] if lessons else None, comp=comp, rows=rows))
    extras = []
    for p in sorted(glob.glob(sdir + "/*")):
        n = os.path.basename(p)
        if re.match(r"\d\d-[A-Z]+\d\d-", n):
            continue
        extras.append((n, p, os.path.isdir(p)))
    return dict(code=code, short=short, title=title, dir=b, path=sdir, sectors=sectors, extras=extras)


def build_series(S, A, peers):
    code = S["code"]; out = f"{OUT}/{code.lower()}"
    site = f"{code} · {S['title']}"
    ghdir = GHT + rel(S["path"])
    cta_html = cta(S["title"])
    for s in S["sectors"]:
        if s["lesson"]:
            md = clean(sanitize(open(s["lesson"], encoding="utf-8").read()))
            title = md.splitlines()[0].lstrip("# ").strip()
            nav = f'<p class="meta"><a href="../index.html">All sectors</a> · <a href="{s["slug"]}.html">{html.escape(s["name"])}</a></p>'
            write(f"{out}/sectors/{s['slug']}-origin-story.html", page(site, title + " · " + site, title, "../", Q_LESSON, nav, f"<article>{md2html(md)}</article>" + cta_html, GHB + rel(s["lesson"])))
        comp_html = ""
        trs = "".join(f"<tr><td>{r['level']}</td><td>{r['fmt']}</td><td><code>{html.escape(r['pid'])}</code></td><td>{html.escape(r['idx'])}</td><td>{html.escape(r['dur'])}</td><td>{html.escape(r['obj'])}</td><td>{html.escape(r['out'])}</td></tr>" for r in s["rows"])
        lesson_card = f'<div class="card"><span class="num">LEVEL 0 · THE ORIGIN STORY</span><h3>Two-hour Origin Story sprint</h3><p>A free community lesson with the origins, the general story, future perspectives, a persona-led case and a small build experiment.</p><a class="cta" href="{s["slug"]}-origin-story.html">Open the lesson</a></div>' if s["lesson"] else '<div class="card"><span class="num">LEVEL 0 · THE ORIGIN STORY</span><h3>Lesson in preparation</h3><p>The Origin Story lesson for this sector is not published yet. It appears here automatically once it is added.</p></div>'
        demos_html = demo_list(s["slug"], "../../") if code == "BTM11" else ""
        body = f"""
<section class="hero"><span class="pre">{html.escape(s['name'])} · {code}</span>
<h1>{html.escape(s['ent'])}: {html.escape(S['title'])}</h1>
<p class="sub">An aspirational case study for the {html.escape(s['name'])} sector. Start with the Origin Story lesson, then see every pathway record in the catalog.</p>
<div class="row"><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><a class="cta ghost" href="#catalog">See the pathway catalog</a></div></section>
<section class="blk"><div class="grid">{lesson_card}<div class="card"><span class="num">LEVELS 1 TO 5</span><h3>{len(s['rows'])} pathway records</h3><p>Pre-Foundation to Ultimate, across webinar, workshop, sprint, bootcamp, masterclass, superclass, hackathon and 21-day challenge formats.</p></div></div></section>
{demos_html}
<section class="blk" id="catalog"><h2>Pathway catalog</h2>
<blockquote><p><strong>Publication note:</strong> these are catalog records. They are <strong>not proof that a course is live or purchasable</strong>.</p></blockquote>
<div class="tw"><table><thead><tr><th>Level</th><th>Format</th><th>Pathway ID</th><th>Index</th><th>Duration</th><th>Learning objective</th><th>Student output</th></tr></thead><tbody>{trs}</tbody></table></div></section>
"""
        nav = f'<p class="meta"><a href="../index.html">All sectors</a> · {html.escape(s["name"])}</p>'
        write(f"{out}/sectors/{s['slug']}.html", page(site, f"{s['ent']} · {site}", f"{code} pathway catalog for {s['name']}", "../", A["q_sector"], nav, body + cta_html, f"{GHT}{rel(S['path'])}/{s['dir']}"))
    cards = "".join(f'<div class="card"><span class="num">{html.escape(s["name"])}</span><h3>{html.escape(s["ent"])}</h3><p class="meta">{len(s["rows"])} pathway records</p><p>{("<a href=sectors/" + s["slug"] + "-origin-story.html>Origin lesson</a> · ") if s["lesson"] else ""}<a href="sectors/{s["slug"]}.html">Catalog</a></p></div>' for s in S["sectors"])
    import collections
    cnt = collections.defaultdict(collections.Counter)
    for s in S["sectors"]:
        for r in s["rows"]:
            cnt[(r["level"], r["fmt"])][r["dur"]] += 1
    dur = {}
    for (lv, fm), c in cnt.items():
        dur.setdefault(lv, {})[fm] = c.most_common(1)[0][0]
    fmts = [FLABEL.get(f, f.capitalize()) for f in FORMATS]
    trs = "".join("<tr><td><strong>%s</strong></td>%s</tr>" % (lvl, "".join(f"<td>{html.escape(dur.get(lvl, {}).get(f, '—'))}</td>" for f in fmts)) for _, lvl in LEVELS)
    total = sum(len(s["rows"]) for s in S["sectors"])
    ex = ""
    demos_card = '<section class="blk"><div class="card"><span class="num">BOOTCAMP DEMOS</span><h3>15 hands-on demos for each sector</h3><p>The BTM11 bootcamp demo library, from the case baseline to industry regulation.</p><a class="cta" href="../btm11-demos/index.html">Open the demos</a></div></section>' if code == "BTM11" and os.path.isdir(DEMOS) else ""
    if S["extras"]:
        items = "".join(f'<li><a href="{(GHT if d else GHB) + rel(p)}" target="_blank" rel="noopener">{html.escape(n)}{"/" if d else ""}</a></li>' for n, p, d in S["extras"])
        ex = f'<section class="blk"><h2>More from this series</h2><p>Supporting files and toolkits kept alongside the sector folders on GitHub.</p><ul>{items}</ul></section>'
    others = " · ".join(f'<a href="../{c.lower()}/index.html">{c}</a>' if c != code else f"<strong>{c}</strong>" for c in peers)
    idx = f"""
<section class="hero"><span class="pre">Free live webinar · 11 sectors · {A["day"]}</span>
<h1>{html.escape(S['title'])}</h1>
<p class="sub">{code}: eleven aspirational case studies, a free Origin Story lesson for each, and the full pathway catalog.</p>
<ul class="ticks"><li>Read the free Origin Story lesson for your sector</li><li>See every pathway across five levels and eight formats</li><li>Plan your route from Pre-Foundation to Ultimate</li></ul>
<div class="row"><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><a class="cta ghost" href="#sectors">Explore the sectors</a></div>
<p class="note">Free webinar · opens the registration page · aspirational case studies, no client work implied</p></section>
{demos_card}<section class="blk" id="sectors"><h2>Explore by sector</h2><p>Each card is one aspirational case study with its own Origin Story lesson and pathway records.</p><div class="grid">{cards}</div></section>
<section class="blk"><h2>The learning path</h2><p>Every sector has the same five levels and eight formats, plus the Level 0 Origin Story. Durations come from the catalog records.</p><div class="tw"><table><thead><tr><th>Level</th>{"".join(f"<th>{f}</th>" for f in fmts)}</tr></thead><tbody>{trs}</tbody></table></div>
<p class="meta">{total} pathway records across {len(S['sectors'])} sectors.</p></section>
<section class="blk"><h2>Questions</h2>
<details><summary>Are these real companies?</summary><p>No. Each enterprise is an aspirational case study built to teach architecture. No client is named or implied.</p></details>
<details><summary>Are all pathways live courses?</summary><p>No. The catalog records are not proof that a course is live or purchasable. Check each record and its source file.</p></details>
<details><summary>Is the webinar free?</summary><p>The button opens a registration page for a free webinar. Check the page for the session details.</p></details>
<details><summary>Does this page update itself?</summary><p>Yes. It is rebuilt automatically whenever the source content changes.</p></details>
<p class="meta">Other series: {others} · <a href="../{A["key"]}/index.html">All {A["name"]} series</a></p></section>
""" + cta_html
    write(f"{out}/index.html", page(site, site, f"{code}: {S['title']} across 11 aspirational case studies", "", QUOTES.get(code, QUOTES["HR11"]), "", idx, ghdir))
    os.makedirs(out + "/assets", exist_ok=True)
    shutil.copy(HERE + "/assets/successlabs-academy-logo.png", out + "/assets/successlabs-academy-logo.png")
    return total


def build_hub(all_s, A):
    site = A["hub"]
    cards = "".join(f'<div class="card"><span class="num">{S["code"]}</span><h3>{html.escape(S["title"])}</h3><p class="meta">{len(S["sectors"])} sectors · {sum(len(s["rows"]) for s in S["sectors"])} pathway records</p><p><a href="../{S["code"].lower()}/index.html">Open {S["code"]}</a></p></div>' for S in all_s)
    body = f"""<section class="hero"><span class="pre">Free live webinar · 12 series · {A["day"]}</span>
<h1>{A["h1"]}</h1>
<p class="sub">Twelve series, eleven sectors each. Every page updates automatically when the source content changes.</p>
<div class="row"><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><a class="cta ghost" href="#series">Explore the series</a></div></section>
<section class="blk" id="series"><h2>Choose a series</h2><div class="grid">{cards}</div></section>""" + cta("")
    write(f"{OUT}/{A['key']}/index.html", page(site, site, f"All {A['name']} series", f"../{A['key']}/", A["q_hub"], "", body, ""))
    os.makedirs(OUT + f"/{A['key']}/assets", exist_ok=True)
    shutil.copy(HERE + "/assets/successlabs-academy-logo.png", OUT + f"/{A['key']}/assets/successlabs-academy-logo.png")


if __name__ == "__main__":
    for A in ACADEMIES:
        root = os.path.join(REPO, A["dir"])
        if not os.path.isdir(root):
            continue
        all_s = [load_series(d, A) for d in sorted(glob.glob(root + "/" + A["prefix"] + "[0-9][0-9]-*")) if os.path.isdir(d)]
        peers = [S["code"] for S in all_s]
        for S in all_s:
            n = build_series(S, A, peers)
            print(S["code"], S["title"], len(S["sectors"]), "sectors", n, "records")
        build_hub(all_s, A)

    # Academies landing page (Monday to Saturday)
    order = ["hr", "crm", "fi", "proc", "scm", "btm"]
    byk = {A["key"]: A for A in ACADEMIES}
    cards = ""
    for k in order:
        A = byk[k]
        cards += (f'<div class="card"><span class="num">{A["day"]}</span><h3>{html.escape(A["name"])} Academy</h3>'
                  f'<p class="meta">12 series · 11 sectors each</p><p>{html.escape(A["q_hub"])}</p>'
                  f'<p><a href="../{k}/index.html">Open the {html.escape(A["name"])} series</a></p></div>')
    body = f"""<section class="hero"><span class="pre">Free live webinar · Six capability academies</span>
<h1>Architect the enterprise, one capability at a time</h1>
<p class="sub">Six academies, twelve series each, eleven sectors per series. Every page updates automatically when the source content changes.</p>
<div class="row"><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><a class="cta ghost" href="#academies">Choose an academy</a></div></section>
<section class="blk" id="academies"><h2>Choose an academy</h2><div class="grid">{cards}</div></section>""" + cta("")
    write(f"{OUT}/academies/index.html", page("Capability Academies", "Capability Academies", "SuccessLabs Academy capability academies", "../academies/", "Six academies, one question: what must the enterprise be able to prove?", "", body, ""))
    os.makedirs(OUT + "/academies/assets", exist_ok=True)
    shutil.copy(HERE + "/assets/successlabs-academy-logo.png", OUT + "/academies/assets/successlabs-academy-logo.png")
