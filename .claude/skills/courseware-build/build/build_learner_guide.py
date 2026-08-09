#!/usr/bin/env python3
"""Generate the Digital Transformation and Business Innovation with GenAI Learner
Guide as BOTH a Markdown mirror (LG-*.md at repo root) and a DOCX
(courseware/LG-*.docx) from one source, so they never diverge.

House format: cover page, Document Version Control Record, auto TOC, Arial 11pt
body, one section per lab (Maps to · Goal · What you'll build · Step-by-step ·
Test it), plus setup, the AIM framework, assessment preparation and a glossary.
All content is driven by course_data + the domain data files, keeping the LG
100% aligned with the slide deck, Lesson Plan and labs.

The LG is where the DETAILED step-by-step instructions live — the slide deck is
kept visual and deliberately carries no numbered steps.
"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
ACT=DOMAIN1+DOMAIN2+DOMAIN3
import prodoc
def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE); ASSETS=os.path.join(os.path.dirname(HERE),"assets")

# ---- Document Version Control Record (single source for BOTH the MD and DOCX) ----
VERSION_RECORD=[
 ("30.0","1 July 2025","Previous release — Learner Guide for Digital Transformation and Business Innovation with Generative AI (GenAI).","Tertiary Infotech Academy"),
 ("32",C.VERSION_DATE,"Major revision — restructured to the three WSQ topics with 18 detailed step-by-step labs; added the Skills Framework alignment, responsible-use guidance, the five-layer digital architecture, Singapore AI governance (IMDA Model AI Governance Framework, AI Verify, PDPA), the AIM framework, assessment preparation for the Written Assessment + Practical Performance, and an expanded glossary.",C.TRAINER),
 ("33",C.VERSION_DATE,"Corrected the practical instrument naming throughout to Practical Performance (PP) to match the assessment papers held on the TMS (previously labelled Case Study); PP duration aligned to 1 hour across the slides, Lesson Plan, Learner Guide and the paper.",C.TRAINER),
 ("35",C.VERSION_DATE,"Major content revision — the 15 standalone labs are replaced by 18 CONNECTED labs forming one end-to-end production pipeline: the learner chooses a single business idea and carries it through research (Perplexity + NotebookLM), scoring, Business Model Canvas, digital architecture, video script, AI voiceover (ElevenLabs), AI soundtrack (Suno), video production (Kling + CapCut) and a business presentation (Gamma). Added the six Business Model Canvas guidelines, prompting and craft tips for every GenAI tool, clickable tool links, a pipeline overview flow at the front, the four guardrail types, the eight AI ethics principles as observable behaviours, a pipeline risk assessment, and a capstone agentic AI workflow (n8n) that automates the whole pipeline with a human review gate and an audit log.",C.TRAINER),
 (C.VERSION.lstrip("v"),C.VERSION_DATE,"Layout and alignment fixes — auto-sized lab 'You'll build' panels and slide titles so long text no longer collides; two-digit lab badges no longer clip; refreshed the lesson-plan overview slide to the 18-lab structure; corrected every cross-artifact lab reference (governance controls Labs 13-14, canvas Lab 6, action plan Lab 15, AI use policy Lab 17, pitch deck Lab 12).",C.TRAINER),
]

# ---------------- block DSL (single content stream → MD + DOCX) ----------------
B=[]
def h1(t): B.append(("h1",t))
def h2(t): B.append(("h2",t))
def h3(t): B.append(("h3",t))
def p(t):  B.append(("p",t))
def bullets(xs): B.append(("bullets",xs))
def steps(xs): B.append(("steps",xs))
def code(t): B.append(("code",t))
def note(t): B.append(("note",t))
def rule(): B.append(("rule",))

# ---------------- content ----------------
h1("Introduction")
p(f"This Learner Guide accompanies the WSQ course {C.TITLE} ({C.COURSE_CODE}), conducted by {C.ORG}. "
  "It provides the detailed, step-by-step instructions for all 18 hands-on labs, organised by the three "
  "course topics. Every lab maps to a Skills Framework ability or knowledge item and to one of the three "
  "learning outcomes, so completing the labs prepares you directly for the assessment.")
p("Use this guide alongside the course slides and the lab files in the labs/ folder. The slides are "
  "deliberately visual and carry only each lab's objective, deliverable and verification step — the full "
  "numbered instructions live here in the Learner Guide, which you may use during the open-book assessment.")
p("All labs use generative AI tools on their free tiers. Sign up with your own account. Do not enter "
  "confidential, personal or client-identifying data into any public generative AI tool during this course; "
  "use fictitious or non-sensitive material for every exercise.")

h1("Course Learning Outcomes")
bullets(C.LEARNING_OUTCOMES)

h1("Skills Framework Alignment")
p(f"This course is aligned to the Skills Framework for ICT technical skill and competency "
  f"{C.TSC_TITLE} ({C.TSC_CODE}).")
h3("Abilities")
bullets(C.TSC_ABILITIES)
h3("Knowledge")
bullets(C.TSC_KNOWLEDGE)

h1("Before You Start — Tools and Accounts")
h3("What you need")
bullets([
 "A laptop with a modern web browser (Chrome or Edge recommended) and a stable internet connection.",
 "A personal email address you can use to register for the free tiers of the generative AI tools.",
 "A general-purpose AI chat assistant — ChatGPT, Google Gemini or Claude (all have a free tier).",
 "Perplexity for research with cited sources (free tier includes a limited number of deep research queries).",
 "An AI image tool — Adobe Firefly or Microsoft Designer (both give free credits).",
 "Gamma (gamma.app) for AI-generated presentations, and Canva for visual layout.",
 "Suno for AI music, and CapCut or Descript for video editing.",
 "A spreadsheet application — Microsoft Excel or Google Sheets — for the scoring and KPI labs.",
])
h3("Set up your accounts before Lab 1")
p("Register for the tools above in advance so class time is spent on the business thinking rather than on "
  "sign-up screens. Free tiers change often; if a tool is unavailable on the day, the trainer will nominate "
  "an equivalent. The method taught in each lab matters more than the specific product.")
h3("Responsible use in every lab")
bullets([
 "Never paste confidential, personal or client data into a public generative AI tool.",
 "Treat every AI output as a draft: verify facts, figures and citations before you rely on them.",
 "Check the licence terms of any generated image, music or video before any commercial use.",
 "Record which tool produced which artifact — you will need this for the assessment and for governance.",
 "Where an output will be published or sent to a customer, keep a human review step.",
])
h3("How to work through a lab")
bullets([
 "Read the objective and the 'What you'll build' statement so you know the deliverable before you start.",
 "Follow the numbered steps in order; each lab builds on the artifact produced by the previous one.",
 "Finish with the 'Test it' check — if it does not pass, revisit the step it points to.",
 "Save every deliverable; the labs are the direct preparation for the Practical Performance tasks.",
])

# ---------------- per-topic, per-lab ----------------
TOPICS_BY_NUM={t["num"]:t for t in C.TOPICS}
for t in C.TOPICS:
    h1(f"Topic {t['code']} — {t['title']}")
    p(t["subtitle"])
    h3("Key concepts")
    bullets([f"{name} — {detail}" for name,detail in t["concepts"]])
    for a in [x for x in ACT if x["topic"]==t["num"]]:
        h2(f"Lab {a['num']} — {a['title']}")
        p(f"Maps to: {a['objective']}")
        p(f"Goal: {a['desc']}")
        h3("What you'll build")
        p(a["build"]+f"   (Tools: {a['services']}.)")
        h3("Step-by-step")
        steps([(instr,cmd) for instr,cmd in a["steps"]])
        h3("Test it")
        p(a["test"])
        note(f"A standalone copy of this lab is in labs/lab-{a['num']:02d}-*.md. "
             f"Use non-confidential data throughout, and verify every AI-generated fact before relying on it.")
        rule()

h1("Putting It Together — The AIM Framework")
p("The three topics form a single repeatable loop for running generative AI innovation in an organisation. "
  "Use it after the course to take any new idea from proposal to measured outcome.")
h3("Assess")
bullets([
 "Investigate what is possible — the tool landscape and what comparable organisations have achieved (Labs 1-3).",
 "Evaluate each opportunity on business value, feasibility, data readiness, risk and strategic fit (Lab 4).",
 "Select the one or two opportunities that best match a stated organisational objective.",
])
h3("Implement")
bullets([
 "Model the business case and design the solution with the Business Model Canvas and Design Thinking (Labs 5-7).",
 "Design the digital architecture across the data, model, orchestration, application and governance layers (Lab 8).",
 "Build the pilot and prove the integration pattern works (Labs 9-10).",
 "Plan the rollout with owners, milestones, risks and go/no-go criteria (Lab 11).",
])
h3("Manage")
bullets([
 "Control the legal, ethical and security risks with named, owned controls (Labs 13-14).",
 "Measure against the pre-AI baseline, including a counter-metric that would reveal harm (Lab 14).",
 "Communicate with each stakeholder group and keep new ideas flowing into the pipeline (Lab 15).",
 "Review at the agreed cadence, then feed what you learn back into Assess.",
])
rule()

h1("Preparing for the Assessment")
p("The final assessment has two open-book instruments. You may use these slides, this Learner Guide and "
  "any approved material. Both must be passed to be assessed as 'Competent'.")
bullets([
 "Written Assessment (WA) — Short-Answer Questions, 1 hour. Tests your knowledge: the difference between "
 "predictive and generative AI, the business value levers, planning methodologies, architecture layers, "
 "legal/ethical/security issues, governance frameworks, measurement and stakeholder communication.",
 "Practical Performance (PP) — 1 hour, three hands-on tasks. You research a market and build a board-level "
 "recommendation, apply Design Thinking with GenAI, and design a GenAI-powered assistant — the same work you did in the labs.",
 "Revise by re-reading the Key concepts at the start of each topic and the 'Test it' check for each lab.",
 "Bring your own lab deliverables — the opportunity register (Lab 4), architecture (Lab 8), action plan "
 "(Lab 11) and KPI set (Lab 14) are the strongest revision material for the Practical Performance.",
 "Practise justifying decisions. Most marks are awarded for the reasoning behind a choice, not the choice itself.",
])

h1("Glossary")
gl=[
 ("Generative AI (GenAI)","AI that creates new content — text, image, audio, video or code — from a prompt, rather than only scoring or classifying existing data."),
 ("Predictive AI","AI that forecasts, scores or classifies based on patterns learned from historical labelled data."),
 ("Foundation model","A large model pre-trained on a broad corpus that can be adapted to many downstream tasks."),
 ("Prompt","The instruction and context given to a generative model to produce a desired output."),
 ("Token","The unit of text a language model processes; models generate output one token at a time."),
 ("Hallucination","Fluent, confident output from a model that is factually wrong — the reason a human review step is required."),
 ("RAG (Retrieval-Augmented Generation)","Grounding a model's answers in your own documents by retrieving relevant content and supplying it with the prompt."),
 ("AI agent","A system that plans and executes multi-step tasks using tools, rather than answering a single prompt."),
 ("Prompt injection","An attack where hostile instructions hidden in content the model reads hijack its behaviour."),
 ("Shadow AI","Staff using unapproved AI tools with company data, outside IT and compliance visibility."),
 ("Business Model Canvas (BMC)","A nine-block visual template describing how an organisation creates, delivers and captures value."),
 ("Design Thinking","A human-centred innovation method: Empathise, Define, Ideate, Prototype, Test."),
 ("Digital architecture","The structured description of how data, models, orchestration, applications and governance fit together."),
 ("Baseline","The pre-AI measurement of time, cost or quality, without which no improvement can be proven."),
 ("Counter-metric","A measure tracked to reveal harm caused by an improvement — for example error or complaint rate."),
 ("AIM framework","Assess, Implement, Manage — the repeatable loop for running generative AI business innovation."),
 ("Model AI Governance Framework","IMDA's practical Singapore guidance for deploying AI responsibly, including generative AI."),
 ("AI Verify","Singapore's AI governance testing framework and software toolkit for validating AI system behaviour."),
 ("PDPA","Singapore's Personal Data Protection Act, governing consent, purpose, retention and protection of personal data."),
 ("EU AI Act","The European Union's risk-based AI regulation, the first comprehensive AI law, including transparency duties."),
]
B.append(("dl",gl))

# ---------------- render Markdown ----------------
def _anchor(txt):
    return "".join(ch.lower() if ch.isalnum() else ("-" if ch in " -" else "") for ch in txt)

def render_md():
    out=[f"# {C.TITLE} — Learner Guide",""]
    out.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Conducted by:** {C.ORG} ({C.UEN.replace('UEN: ','UEN ')})  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    # Document Version Control Record — mirrors the DOCX record exactly
    out += ["## Document Version Control Record","",
            "| Version | Date | Description of change | Author |",
            "| --- | --- | --- | --- |"]
    for v,d,desc,author in VERSION_RECORD:
        out.append(f"| {v} | {d} | {desc} | {author} |")
    out.append("")
    # TOC (h1 + h2)
    out.append("## Contents"); out.append("")
    for kind,*rest in B:
        if kind=="h1": out.append(f"- [{rest[0]}](#{_anchor(rest[0])})")
        elif kind=="h2": out.append(f"  - [{rest[0]}](#{_anchor(rest[0])})")
    out.append("")
    for kind,*rest in B:
        if kind=="h1": out+=["",f"## {rest[0]}",""]
        elif kind=="h2": out+=["",f"### {rest[0]}",""]
        elif kind=="h3": out+=[f"**{rest[0]}**",""]
        elif kind=="p": out+=[rest[0],""]
        elif kind=="bullets": out+=[f"- {x}" for x in rest[0]]+[""]
        elif kind=="steps":
            for i,(instr,cmd) in enumerate(rest[0],1):
                out.append(f"{i}. {instr}")
                if cmd: out+=["",f"   ```bash",f"   {cmd}","   ```",""]
            out.append("")
        elif kind=="code": out+=["```bash",rest[0],"```",""]
        elif kind=="note": out+=[f"> **Note:** {rest[0]}",""]
        elif kind=="rule": out+=["---",""]
        elif kind=="dl":
            for term,defn in rest[0]: out.append(f"- **{term}** — {defn}")
            out.append("")
    return "\n".join(out)

MD_OUT=os.path.join(REPO,f"LG-{C.SHORT_TITLE}.md")
with open(MD_OUT,"w") as f: f.write(render_md())
print("Saved",MD_OUT)

# ---------------- render DOCX ----------------
BRAND=RGBColor(0x1F,0x6F,0xEB); DARK=RGBColor(0x11,0x18,0x27); GREY=RGBColor(0x55,0x5B,0x66)
INKCODE=RGBColor(0x0B,0x30,0x60)
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc,"LEARNER GUIDE",C.TITLE,C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,VERSION_RECORD)
prodoc.add_toc(doc)

def _new_numbering(doc):
    """Allocate a fresh numbering list so each lab's steps restart at 1.

    python-docx's built-in 'List Number' style shares ONE numbering instance
    document-wide, which makes the steps run 1..N across every lab.

    Each call creates its OWN <w:abstractNum> as well as its own <w:num>. Word
    would restart correctly with a shared abstractNum, but LibreOffice (which
    renders our learner-facing PDF) continues the counter across w:num instances
    that share an abstractNum — giving one abstractNum per list makes both
    renderers agree.
    """
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    numbering = doc.part.numbering_part.element
    absid = max([int(a.get(qn("w:abstractNumId"))) for a in
                 numbering.findall(qn("w:abstractNum"))] or [-1]) + 1
    abs_el = OxmlElement("w:abstractNum")
    abs_el.set(qn("w:abstractNumId"), str(absid))
    lvl = OxmlElement("w:lvl"); lvl.set(qn("w:ilvl"), "0")
    for tag, val in (("w:start", "1"), ("w:numFmt", "decimal"),
                     ("w:lvlText", "%1."), ("w:lvlJc", "left")):
        e = OxmlElement(tag); e.set(qn("w:val"), val); lvl.append(e)
    ppr = OxmlElement("w:pPr"); ind = OxmlElement("w:ind")
    ind.set(qn("w:left"), "720"); ind.set(qn("w:hanging"), "360")
    ppr.append(ind); lvl.append(ppr)
    abs_el.append(lvl)
    # all <w:abstractNum> must precede every <w:num> in numbering.xml
    last_abs = numbering.findall(qn("w:abstractNum"))
    (last_abs[-1].addnext(abs_el) if last_abs else numbering.insert(0, abs_el))
    numid = max([int(n.get(qn("w:numId"))) for n in
                 numbering.findall(qn("w:num"))] or [0]) + 1
    num = OxmlElement("w:num"); num.set(qn("w:numId"), str(numid))
    ref = OxmlElement("w:abstractNumId"); ref.set(qn("w:val"), str(absid))
    num.append(ref); numbering.append(num)
    return numid

def _apply_numbering(para, numid):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    ppr = para._p.get_or_add_pPr()
    numpr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl"); ilvl.set(qn("w:val"), "0")
    nid = OxmlElement("w:numId"); nid.set(qn("w:val"), str(numid))
    numpr.append(ilvl); numpr.append(nid); ppr.append(numpr)

def code_para(text):
    for line in text.split("\n"):
        para=doc.add_paragraph(); prodoc._shade_para(para) if hasattr(prodoc,"_shade_para") else None
        r=para.add_run(line); r.font.name="Consolas"; r.font.size=Pt(9.5); r.font.color.rgb=INKCODE

for kind,*rest in B:
    if kind=="h1": doc.add_heading(rest[0],level=1)
    elif kind=="h2": doc.add_heading(rest[0],level=2)
    elif kind=="h3":
        para=doc.add_paragraph(); r=para.add_run(rest[0]); r.bold=True; r.font.size=Pt(11); r.font.color.rgb=BRAND
    elif kind=="p": doc.add_paragraph(rest[0])
    elif kind=="bullets":
        for x in rest[0]: doc.add_paragraph(x,style="List Bullet")
    elif kind=="steps":
        numid=_new_numbering(doc)          # restart numbering at 1 for every lab
        for i,(instr,cmd) in enumerate(rest[0],1):
            para=doc.add_paragraph(style="List Number"); para.add_run(instr)
            _apply_numbering(para,numid)
            if cmd: code_para(cmd)
    elif kind=="code": code_para(rest[0])
    elif kind=="note":
        para=doc.add_paragraph(); r=para.add_run("Note: "); r.bold=True; r.font.color.rgb=BRAND
        para.add_run(rest[0]).font.size=Pt(10)
    elif kind=="rule": doc.add_paragraph("")
    elif kind=="dl":
        for term,defn in rest[0]:
            para=doc.add_paragraph(style="List Bullet")
            r=para.add_run(term+" — "); r.bold=True; para.add_run(defn)

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
DOCX_OUT=os.path.join(REPO,"courseware",f"LG-{C.SHORT_TITLE}.docx")
doc.save(DOCX_OUT)
print("Saved",DOCX_OUT)
