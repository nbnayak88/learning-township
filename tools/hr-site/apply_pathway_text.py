#!/usr/bin/env python3
"""One-off: rewrite catalog README objectives/outputs with the series-specific text."""
import glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_text as P
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
n = 0
for p in glob.glob(REPO + "/0[1-5]-*/*/[0-9][0-9]-*/0[1-5]-*/*/README.md"):
    t = open(p, encoding="utf-8").read()
    m = re.search(r"(## Learning objective\s*\n)(.*?)(\n\n## Student output\s*\n)(.*?)(\n)", t, re.S)
    if not m or not P.is_generic(m.group(2)):
        continue
    parts = p.split("/")
    code = next(x for x in parts if re.match(r"(HR|CRM|FI|PROC|SCM)\d\d-", x))[:-0 or None].split("-")[0]
    level_no = int(parts[-3][:2])
    sm = re.search(r" Applied via .*$", m.group(2))
    obj = P.objective(code, level_no) + (sm.group(0) if sm else "")
    out = P.student_output(code, m.group(4))
    t = t[:m.start()] + m.group(1) + obj + m.group(3) + out + m.group(5) + t[m.end():]
    open(p, "w", encoding="utf-8").write(t); n += 1
print("rewrote", n)
