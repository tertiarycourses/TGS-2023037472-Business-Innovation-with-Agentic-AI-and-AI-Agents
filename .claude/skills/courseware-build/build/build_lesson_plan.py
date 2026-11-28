#!/usr/bin/env python3
"""Lesson Plan (LP) DOCX from course_data + data_bi.SCHEDULE + the deck's slide_map.json.
House format: cover page, Document Version Control Record, TOC (each on its own page), Arial 11,
colour-coded day tables with the slide numbers of the CURRENT deck on every row."""
import json, os, sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
import data_bi as B
import prodoc
from version_history import ALL

REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
MAP = json.load(open(os.path.join(HERE, "slide_map.json")))
HEADER_FILL = "1F6FEB"; TOPIC_FILL = "E8F0FE"; BREAK_FILL = "FFF4E5"; LUNCH_FILL = "FDE9D9"; ASSESS_FILL = "E8F7EE"
KIND_FILL = {"topic": TOPIC_FILL, "activity": TOPIC_FILL, "break": BREAK_FILL, "lunch": LUNCH_FILL, "assess": ASSESS_FILL,
             "admin": "F3F5F8", "recap": "F3F5F8", "lab": None}
GREY = RGBColor(0x55, 0x5B, 0x66)

def rng(a, b): return str(MAP[a]) if MAP[b] - 1 <= MAP[a] else f"{MAP[a]}–{MAP[b] - 1}"
ROUTES = [("Welcome", ("admin", "t1")), ("Topic 1 (Part A)", ("t1", "mini_muse")),   # v58: Topic 1 follows the C34 Ghana flow
          ("Mini Activity", ("mini_muse", "t1sg")), ("Topic 1 (Part B)", ("t1sg", "labs1")),
          ("Activity 1 (Part A)", ("labs1", "act1")), ("Activity 1 (Part B)", ("act1", "t1end")), ("Topic 2 (Part A)", ("t2", "t2step3")),
          ("Topic 2 (Part B)", ("t2step3", "t2test")), ("Topic 2 (Part C)", ("t2test", "act2a")), ("Activity 2 (Part A)", ("act2a", "act2b")),
          ("Activity 2 (Part B)", ("act2b", "t2end")), ("Topic 3 (Part A)", ("t3", "act3a")), ("Activity 3 (Part A)", ("act3a", "t3scale")),
          ("Topic 3 (Part B)", ("t3scale", "coachmini")), ("AI Coaching Mini Activity", ("coachmini", "t3work")), ("Topic 3 (Part C)", ("t3work", "t3loop")), ("Topic 3 (Part D)", ("t3loop", "act3")),
          ("Activity 3 (Part B)", ("act3", "t3end")), ("Course recap", ("wrap", "assess")),
          ("Written", ("assess", "end")), ("Practical", ("assess", "end"))]
def slides_for(text):
    if text.startswith("Course recap"): return f"{rng('wrap', 'assess')}; briefing {MAP['briefing']}"
    for pre, (a, b) in ROUTES:
        if text.startswith(pre): return rng(a, b)
    return "—"

doc = Document()
st = doc.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc, "LESSON PLAN", C.TITLE, C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"), course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc, ALL)
prodoc.add_toc(doc)
H = lambda t, l=1: doc.add_heading(t, level=l)

def cell(c, text, bold=False, size=9.5, color=None, fill=None):
    c.text = ""; r = c.paragraphs[0].add_run(text); r.bold = bold; r.font.size = Pt(size); r.font.name = "Arial"
    if color: r.font.color.rgb = color
    if fill: prodoc._shade_cell(c, fill)
def head(t, names):
    h = t.add_row().cells
    for i, n in enumerate(names): cell(h[i], n, bold=True, size=10, color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)

H("Course Information")
t = doc.add_table(rows=0, cols=2); t.style = "Table Grid"
for k, v in [("Course Title", C.TITLE), ("WSQ Course Reference", C.COURSE_CODE),
             ("Training Provider", f"{C.ORG} ({C.UEN.replace('UEN: ', 'UEN ')})"),
             ("Skills Framework TSC", f"{C.TSC_TITLE} ({C.TSC_CODE})"), ("Duration", C.CONTACT_TIME_NOTE),
             ("Mode", "Instructor-led; three step-by-step activities with the Meta Muse always-on agent (phone app or muse.ai website) on shared group boards (no login); learner laptop or phone"),
             ("Learner case", "Each group works on its own organisation (one member's company). Meridian Services (fictitious) is the worked demo: one scenario slide per topic and a filled demo board per activity"),
             ("Activity Studio", B.BCM_URL), ("Slide deck", f"{C.SHORT_TITLE}-{C.VERSION}.pptx ({MAP['end'] - 1} slides)"),
             ("Trainer", C.TRAINER)]:
    c = t.add_row().cells; cell(c[0], k, bold=True, size=10, fill=TOPIC_FILL); cell(c[1], v, size=10)
prodoc.set_widths(t, [1.8, 5.0])

H("Learning Outcomes")
doc.add_paragraph("On completion of this course, learners will be able to:")
for lo in C.LEARNING_OUTCOMES: doc.add_paragraph(style="List Bullet").add_run(lo)

H("Topics, Outcomes and Slides")
tt = doc.add_table(rows=0, cols=4); tt.style = "Table Grid"; head(tt, ["Topic", "Content", "LO · K & A", "Slides"])
tslides = {1: rng("t1", "t1end"), 2: rng("t2", "t2end"), 3: rng("t3", "bonus")}   # v58 QA: the "Next · Topic N" bridge is in no topic range
for tp in C.TOPICS:
    c = tt.add_row().cells
    cell(c[0], f"Topic {tp['num']}: {tp['title']}", bold=True, fill=TOPIC_FILL); cell(c[1], "; ".join(tp["items"]))
    cell(c[2], f"LO{tp['lo'] + 1} · {tp['codes']}"); cell(c[3], tslides[tp["num"]])
prodoc.set_widths(tt, [2.0, 3.0, 1.0, 0.8])

H("Learning Units (approved Course Proposal)")
lt_ = doc.add_table(rows=0, cols=4); lt_.style = "Table Grid"; head(lt_, ["LU", "Topic and outcome", "K & A", "Duration"])
for tp in C.TOPICS:
    n = tp["num"]; mins = sum(r[2] for d in B.SCHEDULE for r in B.SCHEDULE[d] if r[5] == n and r[3] != "lunch")
    assert mins == B.LU_HOURS[n] * 60, (n, mins)   # CP governs LU durations
    c = lt_.add_row().cells
    cell(c[0], f"LU{n}", bold=True, fill=TOPIC_FILL); cell(c[1], f"Topic {n}: {tp['title']} (LO{tp['lo'] + 1})")
    cell(c[2], tp["codes"]); cell(c[3], f"{B.LU_HOURS[n]} h")
c = lt_.add_row().cells
cell(c[0], "Assessment", bold=True, fill=ASSESS_FILL); cell(c[1], "WA-SAQ (1 h) + PP (1 h), Day 2 from 4:30 pm"); cell(c[2], "K1-K6, A1-A6"); cell(c[3], "2 h")
prodoc.set_widths(lt_, [1.15, 3.65, 1.2, 0.8])   # 'Assessment' fits on one line
r = doc.add_paragraph().add_run("LU durations include tea breaks and recaps, as scheduled; total 14 h training + 2 h assessment = 16 h.")
r.italic = True; r.font.size = Pt(9.5)

H("Assessment")
for a in [C.ASSESSMENT["written"], C.ASSESSMENT["practical"], "Open book: course slides, Learner Guide and the learner's own activity boards.",
          "Final assessment on Day 2 from 4:30 pm.", C.ASSESSMENT["note"]]:
    doc.add_paragraph(style="List Bullet").add_run(a)

H("Course Schedule")
for day in (1, 2):
    H(f"Day {day} — {C.DAY_THEMES[day]}", 2)
    tb = doc.add_table(rows=0, cols=5); tb.style = "Table Grid"; tb.alignment = WD_TABLE_ALIGNMENT.CENTER
    head(tb, ["Time", "Duration", "Topic / Activity", "LU", "Slides"])
    total = 0
    for a, b, m, kind, text, tpn in B.SCHEDULE[day]:
        c = tb.add_row().cells; f = KIND_FILL.get(kind); bold = kind in ("topic", "activity", "assess")
        cell(c[0], f"{a}–{b}", bold=bold, fill=f); cell(c[1], f"{m} min", fill=f); cell(c[2], text, bold=bold, fill=f)
        cell(c[3], "Assess" if tpn == -1 else ("—" if tpn == 0 else f"LU{tpn}"), fill=f)
        cell(c[4], "—" if kind in ("break", "lunch") else slides_for(text), fill=f)
        if kind != "lunch": total += m
    prodoc.set_widths(tb, [1.0, 0.75, 3.4, 0.75, 0.95])
    r = doc.add_paragraph().add_run(f"Training time excluding lunch: {total} minutes ({total // 60} hours), including tea breaks and any assessment.")
    r.italic = True; r.font.size = Pt(9.5); r.font.color.rgb = GREY
    assert total == 480, (day, total)

# Each activity's stated minutes (deck hand-out, Instructions PDF) must equal its timetable rows (QA v48: 120 vs 75 + 25).
for cv in B.CANVASES:
    rows_ = [r for day_ in (B.SCHEDULE.values() if isinstance(B.SCHEDULE, dict) else [B.SCHEDULE]) for r in day_]
    sched = sum(r[2] for r in rows_ if str(r[4]).startswith(f"Activity {cv['num']} "))
    assert sched == cv["minutes"], f"Activity {cv['num']}: canvas says {cv['minutes']} min, schedule gives {sched} min"
    lab_ = next(L for L in B.LABS if L["canvas"] == cv["key"])
    assert lab_["minutes"] == sched, f"Activity {cv['num']}: lab says {lab_['minutes']} min, schedule gives {sched} min"
doc.add_paragraph("AI Coaching Mini Activity (10 min, Day 2): in pairs, learners coach a worried employee on the AI Coaching simulator (https://alfredang.github.io/AICoaching/), read its feedback, swap and debrief. It is practice for SCALE A (Augment people), not a PP activity.")
doc.add_paragraph("Mini Activity (20 min): right after the six always-on agents are introduced, learners try Meta Muse in three steps (connect email, ask for the most important emails, ask for a 15-second social media ad with an AI human avatar) using the first section of Activity 1 Instructions. It is separate from the three PP group-board activities. A current offline prompts.html is included in activities/.")
H("Activities (one per learning outcome)")
at = doc.add_table(rows=0, cols=5); at.style = "Table Grid"; head(at, ["Activity", "What learners do", "Group board", "Topic · LO", "Assessment evidence"])
for L in B.LABS:
    cv = B.CANVAS[L["canvas"]]; c = at.add_row().cells
    cell(c[0], f"Activity {cv['num']}", bold=True, fill=TOPIC_FILL)
    cell(c[1], f"{L['title']}: " + "; ".join(f"{i + 1}. {st['title']}" for i, st in enumerate(L["steps"])))
    cell(c[2], f"{cv['title']}\n{B.BCM_URL}?activity={cv['key']}"); cell(c[3], f"Topic {cv['topic']} · {cv['lo']} ({cv['codes']})")
    cell(c[4], cv["evidence"])
prodoc.set_widths(at, [0.8, 2.7, 1.4, 1.0, 0.95])
doc.add_paragraph("Materials: one folder per activity under activities/ with a step-by-step Instructions PDF; current fill-in prompts in activities/prompts.html, downloaded from the LMS and opened in a browser. Learners without Meta Muse may run the same prompts in any assistant connected to their own "
                  "email; never use another person's account.")

H("Bonus Topic (self-paced, outside the contact hours)")
doc.add_paragraph(f"Slides {rng('bonus', 'wrap')}: self-paced. Opens with Andrej Karpathy's HackerTube, built with Claude Code in about two hours (6:46 video). Then vibe code an AI transformation dashboard from the Activity 2 plan and the SCALE board with a coding agent (Codex or Claude Code). The Meridian example is activities/meridian-ai-dashboard.html. Share with Sites after class.")

prodoc.add_page_numbers(doc); prodoc.enable_update_fields(doc)
OUT = os.path.join(REPO, "courseware", f"LP-{C.SHORT_TITLE}.docx")
doc.save(OUT); print("Saved", OUT)
