#!/usr/bin/env python3
"""Generate the Digital Transformation and Business Innovation with GenAI Lesson
Plan (LP) DOCX in the Tertiary house format.

Cover page + Document Version Control Record + auto TOC + Arial 11pt body +
colour-coded 2-day schedule tables (9:30am-6:30pm, 8 training hours/day, 1h
lunch, tea within, final assessment on Day 2). Topics/labs come from
course_data + the domain data files so the LP stays aligned with the deck,
guide and labs.
"""
import os, sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

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

BRAND=RGBColor(0x1F,0x6F,0xEB); DARK=RGBColor(0x11,0x18,0x27); GREY=RGBColor(0x55,0x5B,0x66)
HEADER_FILL="1F6FEB"; TOPIC_FILL="E8F0FE"; BREAK_FILL="FFF4E5"; LUNCH_FILL="FDE9D9"; ASSESS_FILL="E8F7EE"

def lab_titles(nums):
    return "; ".join(f"Lab {a['num']}: {a['title']}" for a in ACT if a['num'] in nums)

# ---- slide-number index, read from the BUILT deck so the LP can never drift ----
def _deck_slide_map():
    """Return {lab_num: (first_slide, last_slide)} plus admin anchors, by reading
    the generated PPTX. Keeps the LP's Slides column always true to the deck."""
    from pptx import Presentation
    import glob, re
    cw=os.path.join(REPO,"courseware")
    decks=sorted(glob.glob(os.path.join(cw,f"*{C.VERSION}.pptx")))
    if not decks: return {},{}
    prs=Presentation(decks[0])
    labs={}; anchors={}
    for i,s in enumerate(prs.slides,1):
        text=" ".join(sh.text_frame.text for sh in s.shapes
                      if sh.has_text_frame and sh.text_frame.text)
        # Only the lab OVERVIEW ("LAB n" chip) and its VERIFY slide count as that
        # lab's slides. Admin slides mentioning "…BEFORE LAB 1" must not match.
        m=re.search(r"(?:^|\s)LAB (\d+)(?:\s*·\s*VERIFY|\s|$)",text)
        if m and ("· HANDS-ON" in text or "· VERIFY" in text):
            n=int(m.group(1))
            lo,hi=labs.get(n,(i,i))
            labs[n]=(min(lo,i),max(hi,i))
        for key,pat in (("admin","Welcome & Housekeeping"),("t1","TOPIC 01"),
                        ("t2","TOPIC 02"),("t3","TOPIC 03"),("wrap","WRAP-UP"),
                        ("assess","Briefing for Assessment")):
            if pat in text and key not in anchors: anchors[key]=i
    return labs,anchors

LAB_SLIDES,ANCHORS=_deck_slide_map()

def slides_for(labs=None,span=None):
    """Render a 'Slides n–m' cell for a set of labs or an explicit span.

    Every range is derived from the BUILT deck. A malformed range (end < start,
    which used to happen when a stale hard-coded fallback was used) is a build
    error, not something to print on a trainer's copy — so we assert."""
    if span:
        lo,hi=span
        assert lo and hi and hi>=lo, f"LP: malformed slide span {span} — deck anchors not found"
        return f"{lo}–{hi}" if lo!=hi else str(lo)
    nums=[LAB_SLIDES[n] for n in (labs or []) if n in LAB_SLIDES]
    assert nums, f"LP: no deck slides found for labs {labs}"
    lo=min(a for a,_ in nums); hi=max(b for _,b in nums)
    return f"{lo}–{hi}" if lo!=hi else str(lo)

def concept_span(first_lab):
    """Slides between a topic's section slide and its first lab overview —
    i.e. the concept slides the trainer teaches before the hands-on."""
    lab_lo=LAB_SLIDES[first_lab][0]
    # the topic section slide is the last TOPIC anchor before that lab
    starts=[v for k,v in ANCHORS.items() if k.startswith("t") and v<lab_lo]
    return (max(starts), lab_lo-1)

# ------------------------------------------------ schedule (single source of truth for timing)
# (start, end, minutes, kind, activity_text)  kind: admin/topic/lab/break/lunch/assess/recap
A=ANCHORS
SCHEDULE = {
 1: (C.DAY_THEMES[1], [
    ("9:30","10:00",30,"admin","Welcome, trainer and learner introductions, ground rules, learning outcomes, course outline and mandatory digital attendance (AM)",
     slides_for(span=(A["admin"],A["t1"]-1))),
    ("10:00","11:00",60,"topic","Topic 1 — Introduction to Business Innovation and Generative AI: predictive vs generative AI, how GenAI works, market growth, the four business value levers, the GenAI tool landscape, industry use cases and the opportunity scoring rubric (K1, K2)",
     slides_for(span=concept_span(1))),
    ("11:00","11:15",15,"break","Tea break","—"),
    ("11:15","13:00",105,"lab","Hands-on: "+lab_titles([1,2]),slides_for([1,2])),
    ("13:00","14:00",60,"lunch","Lunch break","—"),
    ("14:00","15:15",75,"lab","Investigating and evaluating business opportunities with GenAI (A1, A2). Digital attendance (PM). STAGE 1 of the course pipeline — Hands-on: "+lab_titles([3]),slides_for([3])),
    ("15:15","15:30",15,"break","Tea break","—"),
    ("15:30","17:15",105,"lab","STAGE 2 — Hands-on: "+lab_titles([4])+". Topic 2 begins — Business planning methodologies: Design Thinking and the six rules for a good Business Model Canvas (K3). GROUP ACTIVITY — Hands-on: "+lab_titles([5]),
     slides_for(span=(LAB_SLIDES[4][0],LAB_SLIDES[5][1]))),
    ("17:15","18:30",75,"lab","STAGE 3 — GROUP ACTIVITY: "+lab_titles([6])+". Designing digital architectures with generative AI: the five layers and four integration patterns (K4, A3). Hands-on: "+lab_titles([7])+". Day 1 recap and Q&A",slides_for([6,7])),
 ]),
 2: (C.DAY_THEMES[2], [
    ("9:30","9:45",15,"recap","Day 1 recap, Q&A and mandatory digital attendance (AM)","—"),
    ("9:45","10:45",60,"topic","The content production pipeline (K4, A4): prompting the three text assistants, and the craft tips for AI voice, music and video. STAGE 4 — Hands-on: "+lab_titles([8]),slides_for([8])),
    ("10:45","11:00",15,"break","Tea break","—"),
    ("11:00","13:00",120,"lab","STAGES 5–6 — Hands-on: "+lab_titles([9,10]),slides_for([9,10])),
    ("13:00","14:00",60,"lunch","Lunch break","—"),
    ("14:00","15:15",75,"lab","Digital attendance (PM). STAGE 7 — Hands-on: "+lab_titles([11,12]),slides_for([11,12])),
    ("15:15","15:30",15,"break","Tea break","—"),
    ("15:30","16:15",45,"lab","Topic 3 — Implementation best practices; legal, ethical and security considerations; the four guardrail types, the AI ethics principles, Singapore's AI governance landscape; measuring success and stakeholder communication (K5, K6, A4, A5, A6). Hands-on: "+lab_titles([13,14,15,16,17])+". CAPSTONE — "+lab_titles([18]),slides_for([13,14,15,16,17,18])),
    ("16:15","16:30",15,"assess","Course revision, TRAQOM survey and Briefing for Assessment",
     slides_for(span=(A["wrap"],A["wrap"]+4))),
    ("16:30","17:30",60,"assess","Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book","—"),
    ("17:30","18:30",60,"assess","Practical Performance (PP) — hands-on tasks using generative AI tools, 1 hour, open book. Assessment digital attendance","—"),
 ]),
}

# ------------------------------------------------ build document
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)

prodoc.add_cover_page(doc,"LESSON PLAN",C.TITLE,C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,[
 ("30.0","1 July 2025","Previous release — 2-day lesson plan for Digital Transformation and Business Innovation with Generative AI (GenAI).","Tertiary Infotech Academy"),
 ("32",C.VERSION_DATE,"Major revision — restructured to the three WSQ topics with 15 hands-on labs; refreshed the GenAI tool landscape, added the five-layer digital architecture, Singapore AI governance (IMDA Model AI Governance Framework, AI Verify, PDPA), the KPI/measurement framework and the stakeholder communication plan; assessment aligned to Written Assessment (SAQ) + Practical Performance (PP).",C.TRAINER),
 ("33",C.VERSION_DATE,"Corrected the practical instrument naming throughout to Practical Performance (PP) to match the assessment papers held on the TMS (previously labelled Case Study); PP duration aligned to 1 hour across the slides, Lesson Plan, Learner Guide and the paper.",C.TRAINER),
 ("35",C.VERSION_DATE,"Major content revision — the 15 standalone labs are replaced by 18 CONNECTED labs forming one end-to-end production pipeline: the learner chooses a single business idea and carries it through research (Perplexity + NotebookLM), scoring, Business Model Canvas, digital architecture, video script, AI voiceover (ElevenLabs), AI soundtrack (Suno), video production (Kling + CapCut) and a business presentation (Gamma). Added the six Business Model Canvas guidelines, prompting and craft tips for every GenAI tool, clickable tool links, a pipeline overview flow at the front, the four guardrail types, the eight AI ethics principles as observable behaviours, a pipeline risk assessment, and a capstone agentic AI workflow (n8n) that automates the whole pipeline with a human review gate and an audit log.",C.TRAINER),
 (C.VERSION.lstrip("v"),C.VERSION_DATE,"Layout and alignment fixes — auto-sized lab 'You'll build' panels and slide titles so long text no longer collides; two-digit lab badges no longer clip; refreshed the lesson-plan overview slide to the 18-lab structure; corrected every cross-artifact lab reference (governance controls Labs 13-14, canvas Lab 6, action plan Lab 15, AI use policy Lab 17, pitch deck Lab 12).",C.TRAINER),
])
prodoc.add_toc(doc)

def H(text,level=1):
    h=doc.add_heading(text,level=level); return h

H("Course Information",1)
info=[("Course Title",C.TITLE),("WSQ Course Reference",C.COURSE_CODE),
      ("Training Provider",C.ORG+"  ("+C.UEN.replace('UEN: ','UEN ')+")"),
      ("Duration","2 days · 8 training hours per day (16 hours)"),
      ("Daily Timing","9:30 am – 6:30 pm (1-hour lunch; tea breaks within training time)"),
      ("Mode","Instructor-led, hands-on labs using generative AI tools, with group discussion and presentation"),
      ("Skills Framework",f"{C.TSC_TITLE} ({C.TSC_CODE})"),
      ("Target Audience","Business owners, managers, executives and professionals driving digital transformation and innovation"),
      ("Trainer",C.TRAINER)]
t=doc.add_table(rows=0,cols=2); t.style="Table Grid"
for k,v in info:
    c=t.add_row().cells; c[0].text=""; r=c[0].paragraphs[0].add_run(k); r.bold=True; r.font.size=Pt(10)
    prodoc._shade_cell(c[0],TOPIC_FILL)
    c[1].text=""; c[1].paragraphs[0].add_run(v).font.size=Pt(10)

H("Learning Outcomes",1)
doc.add_paragraph("On completion of this course, learners will be able to:")
for lo in C.LEARNING_OUTCOMES:
    p=doc.add_paragraph(style="List Bullet"); p.add_run(lo).font.size=Pt(10.5)

H("Assessment",1)
for a in [C.ASSESSMENT["written"],C.ASSESSMENT["practical"],
          "Format: Open Book — course slides, Learner Guide and approved materials only.",
          "Final assessment is conducted on Day 2 from 4:30 pm.",
          "Learners must be assessed as 'Competent' in both instruments.",C.ASSESSMENT["note"]]:
    p=doc.add_paragraph(style="List Bullet"); p.add_run(a).font.size=Pt(10.5)

H("Skills Framework Alignment",1)
doc.add_paragraph(f"This course is aligned to the Skills Framework for ICT — {C.TSC_TITLE} ({C.TSC_CODE}).")
p=doc.add_paragraph(); p.add_run("Abilities").bold=True
for a in C.TSC_ABILITIES:
    q=doc.add_paragraph(style="List Bullet"); q.add_run(a).font.size=Pt(10.5)
p=doc.add_paragraph(); p.add_run("Knowledge").bold=True
for k in C.TSC_KNOWLEDGE:
    q=doc.add_paragraph(style="List Bullet"); q.add_run(k).font.size=Pt(10.5)

def set_cell(cell,text,bold=False,size=9.5,color=None,fill=None,align=None):
    cell.text=""; p=cell.paragraphs[0]
    if align: p.alignment=align
    r=p.add_run(text); r.bold=bold; r.font.size=Pt(size); r.font.name="Arial"
    if color: r.font.color.rgb=color
    if fill: prodoc._shade_cell(cell,fill)

KIND_FILL={"topic":TOPIC_FILL,"break":BREAK_FILL,"lunch":LUNCH_FILL,"assess":ASSESS_FILL,
           "admin":"F3F5F8","recap":"F3F5F8","lab":None}

H("Course Schedule",1)
for day,(theme,rows) in SCHEDULE.items():
    H(f"Day {day} — {theme}",2)
    tbl=doc.add_table(rows=0,cols=4); tbl.style="Table Grid"; tbl.alignment=WD_TABLE_ALIGNMENT.CENTER
    hdr=tbl.add_row().cells
    for i,htext in enumerate(["Time","Duration","Topic / Activity","Slides"]):
        set_cell(hdr[i],htext,bold=True,size=10,color=RGBColor(0xFF,0xFF,0xFF),fill=HEADER_FILL)
    training=0
    for start,end,mins,kind,text,slides in rows:
        cells=tbl.add_row().cells; fill=KIND_FILL.get(kind)
        set_cell(cells[0],f"{start}–{end}",bold=(kind in ("topic","assess")),size=9.5,fill=fill)
        set_cell(cells[1],f"{mins} min",size=9.5,fill=fill)
        set_cell(cells[2],text,bold=(kind in ("topic","assess")),size=9.5,fill=fill)
        set_cell(cells[3],slides,size=9.5,fill=fill,align=WD_ALIGN_PARAGRAPH.CENTER)
        if kind!="lunch": training+=mins
    # widths — Topic/Activity gets the space; autofit off so Word honours them
    tbl.autofit=False
    try: tbl.allow_autofit=False
    except Exception: pass
    for row in tbl.rows:
        row.cells[0].width=Inches(0.95); row.cells[1].width=Inches(0.7)
        row.cells[2].width=Inches(4.55); row.cells[3].width=Inches(0.7)
    p=doc.add_paragraph(); r=p.add_run(f"Total training time: {training} minutes ({training//60} hours)."); r.italic=True; r.font.size=Pt(9.5); r.font.color.rgb=GREY
    assert training==480, f"Day {day} training minutes = {training}, expected 480"

H("Lab Reference (aligned to the learning outcomes)",1)
tt=doc.add_table(rows=0,cols=3); tt.style="Table Grid"
hdr=tt.add_row().cells
for i,htext in enumerate(["Topic","Learning outcome","Labs"]):
    set_cell(hdr[i],htext,bold=True,size=10,color=RGBColor(0xFF,0xFF,0xFF),fill=HEADER_FILL)
for tp in C.TOPICS:
    acts=[a for a in ACT if a["topic"]==tp["num"]]
    cells=tt.add_row().cells
    set_cell(cells[0],f"Topic {tp['code']}: {tp['title']}",bold=True,size=9.5,fill=TOPIC_FILL)
    set_cell(cells[1],tp["weighting"],size=9.5,fill=TOPIC_FILL)
    set_cell(cells[2],", ".join(f"Lab {a['num']}" for a in acts),size=9.5)

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
OUT=os.path.join(REPO,"courseware",f"LP-{C.SHORT_TITLE}.docx")
doc.save(OUT)
print("Saved",OUT)
