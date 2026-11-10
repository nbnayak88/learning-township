#!/usr/bin/env python3
"""Builds the HR01-HR12 public sites straight from the repo content.
Run by .github/workflows/hr-site.yml on every push; no manual steps.
Usage: python3 tools/hr-site/build.py <output_dir>"""
import os, re, glob, html, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from theme import CSS, TEMPLATE, PROGRESS, WEBINAR
import markdown

REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
HRDIR = os.path.join(REPO, "01-HR-Human-Capital-Capability-Academy-Workforce-Monday")
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "docs"))
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
}
Q_SECTOR = "Every sector hires, develops and protects people differently, so listen before you automate."
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


def cta(series_title):
    return f'<section class="close"><h2>Build the decision before the tool</h2><p>Join the free webinar and see how HR teams design {html.escape(series_title)} they can explain, govern and recover.</p><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><p class="note">Free webinar · opens the registration page</p></section>'


def load_series(sdir):
    b = os.path.basename(sdir)
    m = re.match(r"(HR\d\d)-([A-Z0-9]+)-(.+)$", b)
    code, short, title = m.group(1), m.group(2), m.group(3).replace("-", " ").replace(" And ", " and ")
    title = title.replace("AI Powered", "AI-Powered").replace("Rewards Performance", "Rewards & Performance").replace("Learning Mobility", "Learning & Mobility")
    sectors = []
    for d in sorted(glob.glob(sdir + "/[0-9][0-9]-HR*-*")):
        sb = os.path.basename(d)
        mm = re.match(r"\d\d-HR\d\d-([A-Z]+)-(.+)$", sb)
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
        if re.match(r"\d\d-HR\d\d-", n):
            continue
        extras.append((n, p, os.path.isdir(p)))
    return dict(code=code, short=short, title=title, dir=b, path=sdir, sectors=sectors, extras=extras)


def build_series(S):
    code = S["code"]; out = f"{OUT}/{code.lower()}"
    site = f"{code} · {S['title']}"
    ghdir = GHT + rel(S["path"])
    cta_html = cta(S["title"])
    for s in S["sectors"]:
        if s["lesson"]:
            md = clean(relink(open(s["lesson"], encoding="utf-8").read(), s["lesson"]))
            title = md.splitlines()[0].lstrip("# ").strip()
            nav = f'<p class="meta"><a href="../index.html">All sectors</a> · <a href="{s["slug"]}.html">{html.escape(s["name"])}</a></p>'
            write(f"{out}/sectors/{s['slug']}-origin-story.html", page(site, title + " · " + site, title, "../", Q_LESSON, nav, f"<article>{md2html(md)}</article>" + cta_html, GHB + rel(s["lesson"])))
        comp_html = ""
        if s["comp"]:
            links = "".join(f'<li><a href="{GHB}{rel(c)}" target="_blank" rel="noopener">{html.escape(os.path.basename(c))}</a></li>' for c in s["comp"])
            comp_html = f'<section class="blk"><h2>Companion files</h2><p>Files published alongside the lesson on GitHub.</p><ul>{links}</ul></section>'
        trs = "".join(f"<tr><td>{r['level']}</td><td>{r['fmt']}</td><td><code>{html.escape(r['pid'])}</code></td><td>{html.escape(r['idx'])}</td><td>{html.escape(r['dur'])}</td><td>{html.escape(r['obj'])}</td><td>{html.escape(r['out'])}</td><td><a href=\"{GHB}{r['path']}\" target=\"_blank\" rel=\"noopener\">Record</a></td></tr>" for r in s["rows"])
        lesson_card = f'<div class="card"><span class="num">LEVEL 0 · THE ORIGIN STORY</span><h3>Two-hour Origin Story sprint</h3><p>A free community lesson with the origins, the general story, future perspectives, a persona-led case and a small build experiment.</p><a class="cta" href="{s["slug"]}-origin-story.html">Open the lesson</a></div>' if s["lesson"] else ""
        body = f"""
<section class="hero"><span class="pre">{html.escape(s['name'])} · {code}</span>
<h1>{html.escape(s['ent'])}: {html.escape(S['title'])}</h1>
<p class="sub">An aspirational case study for the {html.escape(s['name'])} sector. Start with the Origin Story lesson, then see every pathway record in the catalog.</p>
<div class="row"><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><a class="cta ghost" href="#catalog">See the pathway catalog</a></div></section>
<section class="blk"><div class="grid">{lesson_card}<div class="card"><span class="num">LEVELS 1 TO 5</span><h3>{len(s['rows'])} pathway records</h3><p>Pre-Foundation to Ultimate, across webinar, workshop, sprint, bootcamp, masterclass, superclass, hackathon and 21-day challenge formats.</p></div></div></section>
{comp_html}
<section class="blk" id="catalog"><h2>Pathway catalog</h2>
<blockquote><p><strong>Publication note:</strong> these are catalog records from the GitHub repository. They are <strong>not proof that a course is live or purchasable</strong>. Each record links to its source file.</p></blockquote>
<div class="tw"><table><thead><tr><th>Level</th><th>Format</th><th>Pathway ID</th><th>Index</th><th>Duration</th><th>Learning objective</th><th>Student output</th><th>Source</th></tr></thead><tbody>{trs}</tbody></table></div></section>
"""
        nav = f'<p class="meta"><a href="../index.html">All sectors</a> · {html.escape(s["name"])}</p>'
        write(f"{out}/sectors/{s['slug']}.html", page(site, f"{s['ent']} · {site}", f"{code} pathway catalog for {s['name']}", "../", Q_SECTOR, nav, body + cta_html, f"{GHT}{rel(S['path'])}/{s['dir']}"))
    cards = "".join(f'<div class="card"><span class="num">{html.escape(s["name"])}</span><h3>{html.escape(s["ent"])}</h3><p class="meta">{len(s["rows"])} pathway records</p><p>{("<a href=sectors/" + s["slug"] + "-origin-story.html>Origin lesson</a> · ") if s["lesson"] else ""}<a href="sectors/{s["slug"]}.html">Catalog</a></p></div>' for s in S["sectors"])
    first = S["sectors"][0]; dur = {}
    for r in first["rows"]:
        dur.setdefault(r["level"], {})[r["fmt"]] = r["dur"]
    fmts = [FLABEL.get(f, f.capitalize()) for f in FORMATS]
    trs = "".join("<tr><td><strong>%s</strong></td>%s</tr>" % (lvl, "".join(f"<td>{html.escape(dur.get(lvl, {}).get(f, '—'))}</td>" for f in fmts)) for _, lvl in LEVELS)
    total = sum(len(s["rows"]) for s in S["sectors"])
    ex = ""
    if S["extras"]:
        items = "".join(f'<li><a href="{(GHT if d else GHB) + rel(p)}" target="_blank" rel="noopener">{html.escape(n)}{"/" if d else ""}</a></li>' for n, p, d in S["extras"])
        ex = f'<section class="blk"><h2>More from this series</h2><p>Supporting files and toolkits kept alongside the sector folders on GitHub.</p><ul>{items}</ul></section>'
    others = " · ".join(f'<a href="../{c.lower()}/index.html">{c}</a>' if c != code else f"<strong>{c}</strong>" for c in sorted(QUOTES))
    idx = f"""
<section class="hero"><span class="pre">Free live webinar · 11 sectors · Workforce Monday</span>
<h1>{html.escape(S['title'])}</h1>
<p class="sub">{code}: eleven aspirational case studies, a free Origin Story lesson for each, and the full pathway catalog.</p>
<ul class="ticks"><li>Read the free Origin Story lesson for your sector</li><li>See every pathway across five levels and eight formats</li><li>Follow each record back to its source on GitHub</li></ul>
<div class="row"><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><a class="cta ghost" href="#sectors">Explore the sectors</a></div>
<p class="note">Free webinar · opens the registration page · aspirational case studies, no client work implied</p></section>
<section class="blk" id="sectors"><h2>Explore by sector</h2><p>Each card is one aspirational case study with its own Origin Story lesson and pathway records.</p><div class="grid">{cards}</div></section>
<section class="blk"><h2>The learning path</h2><p>Every sector has the same five levels and eight formats, plus the Level 0 Origin Story. Durations come from the catalog records.</p><div class="tw"><table><thead><tr><th>Level</th>{"".join(f"<th>{f}</th>" for f in fmts)}</tr></thead><tbody>{trs}</tbody></table></div>
<p class="meta">{total} pathway records across {len(S['sectors'])} sectors. Source: <a href="{ghdir}">GitHub</a>.</p></section>
{ex}
<section class="blk"><h2>Questions</h2>
<details><summary>Are these real companies?</summary><p>No. Each enterprise is an aspirational case study built to teach architecture. No client is named or implied.</p></details>
<details><summary>Are all pathways live courses?</summary><p>No. The catalog records are not proof that a course is live or purchasable. Check each record and its source file.</p></details>
<details><summary>Is the webinar free?</summary><p>The button opens a registration page for a free webinar. Check the page for the session details.</p></details>
<details><summary>Does this page update itself?</summary><p>Yes. It is rebuilt from the GitHub repository whenever the repository changes.</p></details>
<p class="meta">Other HR series: {others} · <a href="../hr/index.html">All HR series</a></p></section>
""" + cta_html
    write(f"{out}/index.html", page(site, site, f"{code}: {S['title']} across 11 aspirational case studies", "", QUOTES.get(code, QUOTES["HR11"]), "", idx, ghdir))
    os.makedirs(out + "/assets", exist_ok=True)
    shutil.copy(HERE + "/assets/successlabs-academy-logo.png", out + "/assets/successlabs-academy-logo.png")
    return total


def build_hub(all_s):
    site = "HR · Workforce Monday Series"
    cards = "".join(f'<div class="card"><span class="num">{S["code"]}</span><h3>{html.escape(S["title"])}</h3><p class="meta">{len(S["sectors"])} sectors · {sum(len(s["rows"]) for s in S["sectors"])} pathway records</p><p><a href="../{S["code"].lower()}/index.html">Open {S["code"]}</a></p></div>' for S in all_s)
    body = f"""<section class="hero"><span class="pre">Free live webinar · 12 series · Workforce Monday</span>
<h1>Architect the HR enterprise, series by series</h1>
<p class="sub">Twelve HR series, eleven sectors each. Every page is rebuilt from the GitHub repository automatically.</p>
<div class="row"><a class="cta" href="{WEBINAR}" target="_blank" rel="noopener">Reserve My Free Seat</a><a class="cta ghost" href="#series">Explore the series</a></div></section>
<section class="blk" id="series"><h2>Choose a series</h2><div class="grid">{cards}</div></section>""" + cta("HR architecture")
    write(f"{OUT}/hr/index.html", page(site, site, "All HR series", "../hr/", "Twelve series, one question: what must the HR system promise?", "", body, GHT + "01-HR-Human-Capital-Capability-Academy-Workforce-Monday"))
    os.makedirs(OUT + "/hr/assets", exist_ok=True)
    shutil.copy(HERE + "/assets/successlabs-academy-logo.png", OUT + "/hr/assets/successlabs-academy-logo.png")


if __name__ == "__main__":
    all_s = [load_series(d) for d in sorted(glob.glob(HRDIR + "/HR[0-9][0-9]-*")) if os.path.isdir(d)]
    for S in all_s:
        n = build_series(S)
        print(S["code"], S["title"], len(S["sectors"]), "sectors", n, "records")
    build_hub(all_s)
