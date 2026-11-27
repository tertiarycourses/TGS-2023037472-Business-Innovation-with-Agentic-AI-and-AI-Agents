#!/usr/bin/env python3
"""Build the v41 deck for WSQ Business Innovation with Agentic AI and AI Agents (TGS-2023037472)
in the house design of TGS-2024043854 (ccdeck: ivory/charcoal, terracotta, Cambria headings).
Content: course_data.py + data_bi.py (activities, Muse labs, schedule) + slides_bi.py (topics)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
import data_bi as B
import ccdeck as K
from ccdeck import (cover, cards, rows, table, image, flow, trainer, header, card, text, icon, circle, tip, statement,
                    ACC, TEAL, CHAR, PANEL, WHITE, INK, MUTED, SOFT, SERIF)
import slides_bi as T
import slides_v53 as N
sys.path.insert(0, os.path.expanduser("~/.claude/skills/tertiary-ppt-design")); import trainer_badges as TB   # one profile for every deck

REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
def asset(*p): return os.path.join(REPO, "courseware", "assets", *p)

D = K.Deck(C.TITLE, C.COURSE_CODE, C.SHORT_TITLE)
VER = C.VERSION.lstrip("v")
MARK = {}
def mark(k): MARK[k] = D.n + 1

# ====================================================================== ADMIN
mark("admin")
cover(D, f"WSQ Course Code: {C.COURSE_CODE}", "Business Innovation with\nAgentic AI and AI Agents",
      f"Version {VER}  ·  {C.VERSION_DATE}", f"{C.ORG}\n{C.UEN}\nTrainer: {C.TRAINER}",
      "www.tertiarycourses.com.sg   |   enquiry@tertiaryinfotech.com   |   +65 6100 0613",
      logo=os.path.join(os.path.dirname(HERE), "assets", "tertiary-infotech-logo.png"), badge=("AGENTIC AI", "WSQ · BUSINESS INNOVATION"))

s = D.new(); header(D, s, "Housekeeping", "TRAQOM · SSG Digital Attendance")
card(s, 0.6, 1.95, 7.6, 3.6); icon(s, "phone", 0.95, 2.25, 0.62)
text(s, 1.8, 2.3, 6.2, 0.5, "Attendance is mandatory for SSG funding.", 18, INK, bold=True, font=SERIF)
text(s, 0.95, 3.1, 7.0, 2.3, "Scan the SSG QR code for AM, PM and Assessment attendance.\nTRAQOM survey and Assessment attendance on assessment day.", 17, MUTED, lh=1.3)
card(s, 8.6, 1.95, 4.1, 3.6, fill=CHAR)
text(s, 8.6, 2.35, 4.1, 0.5, "Minimum", 20, SOFT, font=SERIF, align="c", autofit=False)
text(s, 8.6, 2.85, 4.1, 1.2, "75%", 60, ACC, bold=True, font=SERIF, align="c", autofit=False)
text(s, 8.6, 4.2, 4.1, 0.6, "attendance required", 18, SOFT, font=SERIF, align="c", autofit=False)

trainer(D, "Introduction", "[ Trainer Name ]", "[ Title / Role ]",
        [("grad", "Qualifications", ""), ("star", "Expertise", ""), ("briefcase", "Experience", ""), ("mail", "Contact / Profile", "")], template=True)
trainer(D, "Introduction", "Dr. Alfred Ang", "AI Trainer & Engineer\nTertiary Infotech Academy",
        [("grad", "Qualifications", "PhD-qualified trainer specialising in AI, automation and business innovation."),
         ("robot", "Expertise", "Builds autonomous AI agents and agentic workflows for business."),
         ("users", "Experience", "Trains professionals across Singapore on practical, project-based AI skills."),
         ("medal", "Certifications", TB.CERT_LINE),
         ("linkedin", "Profile", "linkedin.com/in/angchewhoe   ·   github.com/alfredang")],
        badge=[(os.path.join(TB.ART, img), nm) for img, nm in TB.BADGES])   # v58: canonical badge row (CCAR-P, CCAR-F, CCDV-F, CCAO-F)

s = D.new(dark=True); header(D, s, "Introduction", "Let's Know Each Other", "One minute each:")
for i, (ic, t) in enumerate([("user", "Name & role"), ("building", "Your organisation"),
                             ("robot", "AI you use today"), ("target", "One process you'd hand to an agent")]):
    x = 0.6 + i * 3.08; card(s, x, 2.6, 2.9, 2.9, fill=PANEL, shadow=False)
    icon(s, ic, x + 1.0, 2.9, 0.9); text(s, x + 0.2, 4.0, 2.5, 1.3, t, 19, WHITE, bold=True, font=SERIF, align="c")

cards(D, "Housekeeping", "Ground Rules", [
    ("Phones on silent", "Step out quietly for calls.", "phone"), ("Join in", "No question is too small.", "chat"),
    ("Respect", "One conversation at a time.", "handshake"), ("Be punctual", "Back from breaks on time.", "clock"),
    ("75% attendance", "Required for funding.", "check"), ("Hands-on", "Do every activity yourself.", "tool")], cols=3, bottom=5.9, desc_pt=16)

T.big_statement(D, "Why you are here", "Stop piloting AI.\nStart running the business on it.", C.PITCH, dark=True)
N.quote(D, "…in 2025, we may see the first AI agents “join the workforce” and materially change the output of companies.",
        "Sam Altman, OpenAI CEO, “Reflections”, January 2025", kicker="Before we start",
        note="Source: https://blog.samaltman.com/reflections (checked 23 Nov 2026; the original opens 'We believe that, in 2025, ...'). Ask: has it happened in your company yet? This course is how you make it happen on purpose.")
# v53: the learner plays the AI consultant inside their own company
s = D.new(); header(D, s, "Your role in this course", "You Are the AI Consultant Inside Your Company",
                    "Three questions your CEO will ask. Three phases. One company: yours, carried through all three activities.")
for i, (ph, q, do_, out, ic) in enumerate([
        ("Discover", "\u201CWhere should we use AI agents first?\u201D", "Hunt the pain points, read the business model, score the ideas.", "Activity 1 · BMC → PP Task 1", "search"),
        ("Prove", "\u201CDoes it actually work here, and is it worth it?\u201D", "Set a baseline, test on real cases, plan a 90-day pilot with one owner.", "Activity 2 · 90-day plan → PP Task 2", "flask"),
        ("Transform", "\u201CHow do we make it stick across the company?\u201D", "Stakeholders, org chart, roles, training, process, cost and governance.", "Activity 3 · SCALE → PP Task 3", "org")]):
    x = 0.6 + i * 4.1; dk = i == 1
    card(s, x, 2.4, 3.9, 4.2, fill=CHAR if dk else WHITE)
    icon(s, ic, x + 0.3, 2.65, 0.75)
    text(s, x + 1.2, 2.62, 2.55, 0.42, f"PHASE {i + 1}", 12, ACC, bold=True, autofit=False)
    text(s, x + 1.2, 2.95, 2.55, 0.55, ph, 26, WHITE if dk else INK, bold=True, font=SERIF, autofit=False)
    text(s, x + 0.3, 3.65, 3.3, 1.0, q, 17, ACC if not dk else "F2B49B", font=SERIF, italic=True, minpt=12)
    text(s, x + 0.3, 4.7, 3.3, 1.0, do_, 14.5, SOFT if dk else MUTED, minpt=10.5)
    text(s, x + 0.3, 5.85, 3.3, 0.5, out, 13, WHITE if dk else INK, bold=True, minpt=10)
    if i < 2: K.box(s, x + 3.93, 4.3, 0.14, 0.4, fill=ACC, shape=K.MSO_SHAPE.CHEVRON)
# v54 (owner): introduce the worked example once, up front, with its plan for AI agents, so Meridian never "pops up"
s = D.new(); header(D, s, "Our worked example · fictitious", "Meet Meridian: Its Plan to Put AI Agents to Work",
                    "Each topic, you watch Meridian take one phase first. Then your group does the same for your own company.")
card(s, 0.6, 2.3, 3.85, 4.3, fill=CHAR)
icon(s, "building", 0.85, 2.5, 0.6)
text(s, 1.6, 2.5, 2.75, 0.62, "Meridian Services Pte Ltd", 17, WHITE, bold=True, font=SERIF, minpt=12, lh=1.0)
for j, (big, lab) in enumerate([("140 staff", "keep 30 commercial buildings running in Singapore"),
                                ("80 a day", "emails and WhatsApps, each re-keyed into a ticket by hand"),
                                ("18 min", "per request; an urgent 2 am leak waits until morning")]):
    y = 3.35 + j * 1.0
    text(s, 0.85, y, 3.4, 0.42, big, 21, ACC, bold=True, font=SERIF, autofit=False)
    text(s, 0.85, y + 0.42, 3.4, 0.55, lab, 12, SOFT, minpt=9.5)
for i, (ph, tp_, plan, ic) in enumerate([
        ("Discover", "Topic 1", "Maps its business model, scores the agent ideas and picks one: a triage agent that reads every request and opens the ticket.", "search"),
        ("Prove", "Topic 2", "Pilots triage at 10 sites for 90 days: 18 to 11 minutes per request, SGD 39,000, one owner, a stop rule.", "flask"),
        ("Transform", "Topic 3", "The day-90 numbers say scale. Rolls out to all 30 sites, redesigns roles, trains staff, governs agents and budgets tokens.", "org")]):
    y = 2.3 + i * 1.47
    card(s, 4.7, y, 8.0, 1.32)
    icon(s, ic, 4.95, y + 0.3, 0.72)
    text(s, 5.9, y + 0.14, 2.6, 0.36, f"{tp_} · {ph}".upper(), 12, ACC, bold=True, autofit=False)
    text(s, 5.9, y + 0.48, 6.6, 0.8, plan, 14.5, INK, minpt=10.5)
text(s, 0.6, 6.68, 12.1, 0.25, "Meridian is fictitious and every figure is synthetic. Your boards and your PP are about your own organisation.", 10, MUTED, autofit=False)

# --- learning outcomes, then LO -> topic map (user request: LOs and topics on the deck)
cards(D, "What you'll achieve", "Learning Outcomes", [
    (f"LO1 · {C.LO_SHORT[0]}", C.LEARNING_OUTCOMES[0].split(": ", 1)[1], "search"),
    (f"LO2 · {C.LO_SHORT[1]}", C.LEARNING_OUTCOMES[1].split(": ", 1)[1], "map"),
    (f"LO3 · {C.LO_SHORT[2]}", C.LEARNING_OUTCOMES[2].split(": ", 1)[1], "org")],
    cols=3, sub=f"Mapped to the TSC {C.TSC_TITLE} ({C.TSC_CODE}).", desc_pt=16)
s = D.new(); header(D, s, "Course map · click a topic to jump", "Discover → Prove → Transform: One Company, Three Phases", "BMC finds the opportunity, the 90-day plan proves it, SCALE makes it how the company works. Each ends with a group board for the PP.")
N.anchor("map", s)
for i, tp in enumerate(C.TOPICS):
    x = 0.6 + i * 4.1; dark = i == 1
    card(s, x, 2.4, 3.9, 4.3, fill=CHAR if dark else WHITE)
    N.button(s, x + 0.25, 6.12, 3.4, 0.42, f"Open Topic {tp['num']} · {C.PHASES[i]}  ▶", f"t{tp['num']}", size=12)
    circle(s, x + 0.25, 2.6, 0.75, ACC); text(s, x + 0.25, 2.6, 0.75, 0.75, str(tp["num"]), 26, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
    text(s, x + 1.15, 2.62, 2.6, 0.32, f"TOPIC {tp['num']}  ·  LO{tp['lo']+1}", 12, ACC, bold=True, autofit=False)
    text(s, x + 1.15, 2.92, 2.6, 0.5, tp["codes"], 11, SOFT if dark else MUTED, autofit=False)
    text(s, x + 0.25, 3.45, 3.4, 0.75, C.FRAME[i], 34, ACC, bold=True, font=SERIF, autofit=False)
    text(s, x + 0.25, 4.2, 3.45, 0.8, C.LO_SHORT[tp["lo"]], 17, WHITE if dark else INK, bold=True, font=SERIF, minpt=12)
    text(s, x + 0.25, 5.05, 3.45, 1.0, "\n".join("•  " + it for it in tp["items"][-2:]), 12, SOFT if dark else MUTED, lh=1.1, minpt=9)
for day in (1, 2):
    def short(x, lim=112):   # v54 QA: one line per row on the slide (cut at the last clause that fits); the LP keeps the full text
        if len(x) <= lim: return x
        for sep in ("; ", ", "):
            k = x.rfind(sep, 0, lim)
            if k > 40: return x[:k]
        return x[:x.rfind(" ", 0, lim)]
    rows_ = [(f"{a}–{b}", short(t), "Assess" if tpn == -1 else ("—" if tpn == 0 else f"LU{tpn}")) for a, b, m, k, t, tpn in B.SCHEDULE[day]]
    table(D, "Roadmap", f"Lesson Plan · Day {day} (9:30 AM – 6:30 PM)", ["Time", "Session", "LU"], rows_, colw=[1.5, 9.7, 0.9], size=11)

# --- activities, the online board and the labs
s = D.new(dark=True); header(D, s, "Roadmap · Activities", "Three Outcomes. Three Boards. Three Screenshots.",
                             "Groups build one shared board online, no login. Each member screenshots it for the PP and answers individually.")
for i, c in enumerate(sorted(B.CANVASES, key=lambda c: c["num"])):
    x = 0.6 + i * 4.1; card(s, x, 2.45, 3.9, 4.2, fill=PANEL, shadow=False)
    text(s, x + 0.2, 2.6, 2.5, 0.9, str(c["num"]), 54, ACC, bold=True, font=SERIF, autofit=False)
    text(s, x + 0.2, 3.6, 3.5, 1.1, c["title"], 22, WHITE, bold=True, font=SERIF, minpt=12)
    text(s, x + 0.2, 4.75, 3.5, 0.35, f"Topic {c['topic']} · {c['lo']}", 14, ACC, bold=True, autofit=False)
    text(s, x + 0.2, 5.15, 3.5, 1.4, c["evidence"], 16, SOFT, minpt=9.5)
# v54: the Activity Studio slides moved into Topic 1, Activity 1 Part A (owner: odd to show them at the start)

s = D.new()   # wsq-slides rule 7: title + LMS screenshot only (no kicker, no caption)
text(s, 0.6, 0.55, 12.1, 0.8, "Login to LMS and Download Course Material", 30, INK, bold=True, font=SERIF, cw=0.52)
K.picture(s, asset("screenshots", "lms-login.png"), 0.6, 1.55, maxw=12.1, maxh=5.3)
K.footer(D, s)
flow(D, "Learning Management System", "Download Course Material", [
    ("globe", "Open the LMS", "lms-tms.tertiaryinfotech.com"), ("mail", "Send OTP", "Your registered email"),
    ("lock", "Verify", "Key in the OTP"), ("folder", "Open the course", "Business Innovation with Agentic AI"),
    ("download", "Download", "Slides PDF + Learner Guide")])
# Free AI subscription (copied from TGS-2024043854 v3.10 slide 19, owner request v45; step 4 adapted: this course runs on Meta Muse)
s = flow(D, "Before we begin · SkillsFuture", "Free AI Subscription: Redeem Your Six Months", [
    ("user", "Eligibility", "Singapore Citizen; age 18+."), ("search", "Course label", "Find the official \u201cFree AI sub\u201d label."),
    ("mail", "Notification", "After attending an eligible course."),
    ("check", "Choose your AI plan", "Pick the plan you will keep using at work. This course's activities run on Meta Muse: core use is free.")],
    tipt="One free six-month subscription per person; eligible course end date 16 Sep 2026 or later; submit within 60 days of the notification.")
T.src(D, s, "SkillsFuture: How to redeem your AI subscription (official guide)",
      "https://www.myskillsfuture.gov.sg/content/portal/en/career-resources/career-resources/education-career-personal-development/redeem-ai-subscription.html")

mark("briefing")
cards(D, "Assessment", "Briefing for Assessment", [
    ("Clear your space", "Phones and materials under the table.", "inbox"), ("No recording", "No photos of the scripts.", "camera"),
    ("Open book", "Slides, Learner Guide, your activity boards.", "book"), ("Work alone", "No discussion.", "user"),
    ("Time", "WA 1 hour, then PP 1 hour.", "clock"), ("Appeals", "Available if you disagree.", "scale")], cols=3, bottom=5.9, desc_pt=16)
s = D.new(); header(D, s, "Assessment", "Assessment & Funding")
card(s, 0.6, 1.95, 6.0, 4.6); icon(s, "clipboard", 0.9, 2.25, 0.6)
text(s, 1.65, 2.3, 4.7, 0.5, "Final Assessment", 20, INK, bold=True, font=SERIF)
text(s, 0.95, 3.15, 5.4, 3.2, "•  Written Assessment (WA-SAQ) · 1 hour\n•  Practical Performance (PP) · 1 hour\n   paste your Activity 1, 2 and 3 screenshots\n•  Day 2 from 4:30 PM · open book", 16, MUTED, lh=1.3)
card(s, 6.85, 1.95, 5.85, 4.6, fill=CHAR); icon(s, "coins", 7.15, 2.25, 0.6)
text(s, 7.9, 2.3, 4.6, 0.5, "Criteria for Funding", 20, WHITE, bold=True, font=SERIF)
text(s, 7.2, 3.15, 5.3, 3.2, "Minimum 75% attendance\n(SSG digital attendance)\n\nCompetent in both WA and PP", 17, SOFT, lh=1.3)
ASSESS_FLOW = [("clipboard", "TRAQOM", "Scan the QR on the LMS; do the survey"), ("phone", "Attendance", "Assessment digital attendance"),
               ("pen", "Assessment", "WA, then PP with your screenshots"), ("send", "Submit", "Upload on the LMS or hand in a printed copy"),
               ("check", "Sign", "Assessment Summary Record")]
flow(D, "Assessment", "Assessment Flow", ASSESS_FLOW, sub="On assessment day, five steps in order.")

# ====================================================================== TOPICS
T.topic1(D, C, mark)
T.topic2(D, C, mark)
T.topic3(D, C, mark)
T.bonus(D, C, mark)   # v47: self-paced bonus topic (outside the contact hours)

# ====================================================================== WRAP-UP
mark("wrap")
s = D.new(dark=True); header(D, s, "Wrap-up", "Three Outcomes. One Business Ready to Move.")
for i, (tp, ic, line) in enumerate(zip(C.TOPICS, ["search", "map", "org"],
        ["Discover: you found and scored where AI agents pay off.", "Prove: you set a baseline, tested on real cases and planned a 90-day pilot.", "Transform: you know how to make it how the whole company works."])):
    x = 0.6 + i * 4.1; card(s, x, 2.0, 3.9, 4.4, fill=PANEL, shadow=False)
    icon(s, ic, x + 1.45, 2.3, 1.0)
    text(s, x + 0.2, 3.5, 3.5, 0.5, f"LO{i+1}", 16, ACC, bold=True, align="c", autofit=False)
    text(s, x + 0.2, 3.95, 3.5, 0.9, C.PHASES[i], 28, WHITE, bold=True, font=SERIF, align="c", minpt=15)
    text(s, x + 0.25, 4.95, 3.4, 1.3, line, 16, SOFT, align="c", minpt=11)
N.quote(D, "Pick one process. Name one owner. Prove it in 90 days.", kicker="Your next move as the AI consultant",
        note="Close: ask each learner to say aloud the one process they will start with on Monday and who will own it.")
mark("assess")
s = D.new(); header(D, s, "Assessment", "Final Assessment")
for i, (ic, t, d, dark) in enumerate([
        ("pen", "Written Assessment (WA)", "Short-Answer Questions · 1 hour · open book · five questions on Topics 1-3.", False),
        ("tool", "Practical Performance (PP)", "Scenario-based · 1 hour · open book.\nTask 1: Activity 1 BMC screenshot.\nTask 2: Activity 2 action plan screenshot.\nTask 3: Activity 3 SCALE board screenshot.\nEach with a short written analysis.", True)]):
    x = 0.6 + i * 6.15; card(s, x, 1.95, 5.95, 3.9, fill=CHAR if dark else WHITE)
    icon(s, ic, x + 0.3, 2.25, 0.6)
    text(s, x + 1.05, 2.3, 4.7, 0.5, t, 20, WHITE if dark else INK, bold=True, font=SERIF)
    text(s, x + 0.35, 3.1, 5.3, 2.6, d, 16, SOFT if dark else MUTED, lh=1.25, minpt=11)
tip(D, s, "Take the Assessment digital attendance, then upload on the LMS (lms-tms.tertiaryinfotech.com) or hand in a printed copy.", y=6.1)
flow(D, "Assessment", "Assessment Flow", ASSESS_FLOW, sub="On assessment day, five steps in order.")
s = D.new(dark=True); header(D, s, "Before you go", "Certification, TRAQOM Survey & Digital Attendance")
card(s, 0.6, 1.95, 6.0, 4.3, fill=PANEL, shadow=False); icon(s, "clipboard", 0.9, 2.25, 0.6)
text(s, 1.65, 2.3, 4.7, 0.5, "TRAQOM Survey (mandatory)", 19, WHITE, bold=True, font=SERIF)
text(s, 0.95, 3.15, 5.4, 2.9, "Complete the survey to receive your certificate.\n\nScan the TRAQOM QR code on the LMS.", 17, SOFT, lh=1.25)
card(s, 6.85, 1.95, 5.85, 4.3, fill=PANEL, shadow=False); icon(s, "phone", 7.15, 2.25, 0.6)
text(s, 7.9, 2.3, 4.6, 0.5, "Digital Attendance (Mandatory)", 19, WHITE, bold=True, font=SERIF)
text(s, 7.2, 3.15, 5.3, 2.9, "AM, PM and Assessment attendance: scan the SSG QR code.\n\nMinimum 75% for funding.", 17, SOFT, lh=1.25)
s = D.new(dark=True)
circle(s, 10.4, -1.6, 4.6, ACC); circle(s, 11.6, 4.3, 2.6, TEAL)
text(s, 0.9, 2.4, 10, 1.2, "Thank You!", 54, WHITE, bold=True, font=SERIF, autofit=False)
text(s, 0.9, 3.75, 10, 0.6, "Questions? We're here to help, during and after class.", 18, SOFT, autofit=False)
text(s, 0.9, 6.6, 11, 0.4, "enquiry@tertiaryinfotech.com   |   +65 6100 0613   |   www.tertiarycourses.com.sg", 13, K.DIM, autofit=False)
K.footer(D, s)

OUT = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
N.resolve()   # v53: course map, SCALE navigator and quiz answers are internal slide links
D.save(OUT)
mark("end")
json.dump(MARK, open(os.path.join(HERE, "slide_map.json"), "w"), indent=1)
print(f"Saved {OUT}  ({D.n} slides)")
