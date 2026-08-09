#!/usr/bin/env python3
"""Generate the standalone lab files (labs/lab-NN-*.md) and labs/README.md index
from the same single source that drives the deck, LP and LG.

Each lab file carries the FULL step-by-step instructions — the slide deck stays
visual and never shows numbered steps.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
ACT = DOMAIN1 + DOMAIN2 + DOMAIN3

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs")
os.makedirs(LABS, exist_ok=True)

TOPICS = {t["num"]: t for t in C.TOPICS}

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-{2,}", "-", s)

# remove superseded lab files so a renumber never leaves orphans
for f in os.listdir(LABS):
    if f.startswith("lab-") and f.endswith(".md"):
        os.remove(os.path.join(LABS, f))

written = []
for a in ACT:
    t = TOPICS[a["topic"]]
    name = f"lab-{a['num']:02d}-{slug(a['title'])}.md"
    out = [
        f"# Lab {a['num']} — {a['title']}",
        "",
        f"**Course:** {C.TITLE} ({C.COURSE_CODE})  ",
        f"**Topic {t['code']}:** {t['title']}  ",
        f"**Maps to:** {a['objective']}  ",
        f"**Tools:** {a['services']}",
        "",
        "## Goal",
        "",
        a["desc"],
        "",
        "## What you'll build",
        "",
        a["build"],
        "",
        "## Before you start",
        "",
        "- Sign in to the tools listed above with your own free-tier account.",
        "- Use fictitious or non-confidential material only — never enter personal, client or "
        "commercially sensitive data into a public generative AI tool.",
        "- Verify every AI-generated fact, figure and citation before you rely on it.",
        "",
        "## Step-by-step",
        "",
    ]
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        out.append(f"{i}. {instr}")
        if cmd:
            out += ["", f"   ```", f"   {cmd}", "   ```", ""]
    out += [
        "",
        "## Test it",
        "",
        a["test"],
        "",
        "## What you learned",
        "",
        f"- {a['objective']}",
        f"- You produced: {a['build']}",
        "- You practised verifying and challenging AI output rather than accepting the first draft.",
        "",
        "---",
        "",
        f"*{C.TITLE} · {C.COURSE_CODE} · {C.ORG} · Version {C.VERSION}*",
        "",
    ]
    with open(os.path.join(LABS, name), "w") as f:
        f.write("\n".join(out))
    written.append((a, name))

# ---- index ----
idx = [
    f"# Hands-On Labs — {C.TITLE}",
    "",
    f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Conducted by:** {C.ORG}  |  "
    f"**Version {C.VERSION} · {C.VERSION_DATE}**",
    "",
    f"{len(ACT)} hands-on labs across {len(C.TOPICS)} topics. Full step-by-step instructions are in each "
    "lab file and in the Learner Guide; the slide deck stays visual and carries only each lab's "
    "objective, deliverable and verification step.",
    "",
    "## Responsible use",
    "",
    "All labs use generative AI tools on their free tiers with your own account. Do not enter "
    "confidential, personal or client-identifying data into any public generative AI tool. Treat every "
    "AI output as a draft and verify it before relying on it.",
    "",
]
for t in C.TOPICS:
    acts = [(a, n) for a, n in written if a["topic"] == t["num"]]
    idx += [f"## Topic {t['code']} — {t['title']}", "", t["subtitle"], "",
            "| Lab | Title | Maps to | Tools |", "| --- | --- | --- | --- |"]
    for a, n in acts:
        idx.append(f"| {a['num']} | [{a['title']}]({n}) | {a['objective'].split(' — ')[0]} | {a['services']} |")
    idx.append("")

idx += ["## Learning outcomes", ""] + [f"- {lo}" for lo in C.LEARNING_OUTCOMES] + [""]
with open(os.path.join(LABS, "README.md"), "w") as f:
    f.write("\n".join(idx))

print(f"Saved {len(written)} lab files + README.md to {LABS}")
