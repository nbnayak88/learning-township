#!/usr/bin/env python3
"""One-off: turn the LIT placeholder READMEs (literal backslash-n text) into structured catalog records."""
import glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lit_text as T
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SECTOR = {"ENE":"Energy","MAT":"Materials","IND":"Industrials","CD":"Consumer Discretionary","CS":"Consumer Staples","HC":"Health Care","FIN":"Financials","IT":"Information Technology","COM":"Communication Services","UT":"Utilities","RE":"Real Estate"}
TIER = {"01-Pre-Foundation":("Pre-Foundation",1),"02-Foundation":("Foundation",2),"03-Essentials":("Essentials",3),"04-Advanced":("Advanced",4),"05-Ultimate":("Ultimate",5)}
DUR = {"webinar":"45-60 mins","workshop":"2-3 hours","sprint":"1-2 weeks","bootcamp":"4-6 weeks","masterclass":"2-4 hours","superclass":"1-2 days","hackathon":"48-72 hours","challenge-21-day":"21 days"}
FL = {"challenge-21-day":"21-Day Challenge","masterclass":"MasterClass","superclass":"SuperClass"}
n = 0
for p in glob.glob(REPO + "/07-LIT-*/LIT[0-9][0-9]-*/[0-9][0-9]-LIT[0-9][0-9]-*/0[1-5]-*/*/README.md"):
    parts = p.split("/")
    fmt, tier = parts[-2], parts[-3]
    sd = parts[-4]
    code = re.match(r"\d\d-(LIT\d\d)-([A-Z]+)-", sd).group(1); sc = re.match(r"\d\d-(LIT\d\d)-([A-Z]+)-", sd).group(2)
    tname, lv = TIER[tier]
    old = open(p, encoding="utf-8").read()
    access = "Premium/Paid" if lv >= 2 or "Paid" in old else "Premium/Paid"
    fl = FL.get(fmt, fmt.capitalize())
    title = re.match(r"# (.*?) — ", old.replace("\\n", "\n")).group(1)
    txt = f"""# {title} — {SECTOR[sc]} Sector — {fl}

**Pathway ID:** `PATH-{code}-{sc}-{tname}-{fl.replace(' ','').replace('-','')}`  
**Unit ID:** {code}-{sc}  
**Academy:** Leadership and Identity Transformation Academy (LIT)  
**Series:** {code}  
**GICS Sector:** {SECTOR[sc]} ({sc})  
**Curriculum Tier:** {tname} (Level {lv})  
**Learning Format:** {fl}  
**Duration:** {DUR[fmt]}  
**Access:** {access}

## Learning objective
{T.objective(code, lv)} Applied via {fl} mode for {SECTOR[sc]}.

## Student output
{T.output(code, lv)}

## Activity-first learning principle
Explore an authentic leadership or identity challenge from this sector. Complete a decision simulation, reflect on choices and consequences, and keep evidence across spiritual, social, academic, professional and personal life goals. Reflection is voluntary and personal; this is not therapy, counselling or a promise of any outcome.

## Publication note
This is a catalog record, **not proof that a course is live or purchasable**. Allocated member names are intentionally excluded from the public repository for privacy.
"""
    open(p, "w", encoding="utf-8").write(txt); n += 1
print("rewrote", n)
