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
         ("medal", "Certifications", "Claude Certified Architect, Claude Certified Developer and Claude Certified Associate (Foundations); PMP, AWS, Microsoft, CompTIA, CKA, CKAD."),
         ("linkedin", "Profile", "linkedin.com/in/angchewhoe   ·   github.com/alfredang")],
        badge=[asset("badge-ccar-f.png"), asset("badge-ccdv-f.png"), asset("claude-certified-associate.png")])

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

# --- learning outcomes, then LO -> topic map (user request: LOs and topics on the deck)
cards(D, "What you'll achieve", "Learning Outcomes", [
    (f"LO1 · {C.LO_SHORT[0]}", C.LEARNING_OUTCOMES[0].split(": ", 1)[1], "search"),
    (f"LO2 · {C.LO_SHORT[1]}", C.LEARNING_OUTCOMES[1].split(": ", 1)[1], "map"),
    (f"LO3 · {C.LO_SHORT[2]}", C.LEARNING_OUTCOMES[2].split(": ", 1)[1], "org")],
    cols=3, sub=f"Mapped to the TSC {C.TSC_TITLE} ({C.TSC_CODE}).", desc_pt=16)
s = D.new(); header(D, s, "Roadmap", "BMC → 90-Day Plan → SCALE: One Business, Three Moves", "Identify and evaluate the opportunity, plan how to start, then sustain and operate. Each ends with a group board for the PP.")
for i, tp in enumerate(C.TOPICS):
    x = 0.6 + i * 4.1; dark = i == 1
    card(s, x, 2.4, 3.9, 4.3, fill=CHAR if dark else WHITE)
    circle(s, x + 0.25, 2.6, 0.75, ACC); text(s, x + 0.25, 2.6, 0.75, 0.75, str(tp["num"]), 26, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
    text(s, x + 1.15, 2.62, 2.6, 0.32, f"TOPIC {tp['num']}  ·  LO{tp['lo']+1}", 12, ACC, bold=True, autofit=False)
    text(s, x + 1.15, 2.92, 2.6, 0.5, tp["codes"], 11, SOFT if dark else MUTED, autofit=False)
    text(s, x + 0.25, 3.45, 3.4, 0.75, C.FRAME[i], 34, ACC, bold=True, font=SERIF, autofit=False)
    text(s, x + 0.25, 4.2, 3.45, 0.8, C.LO_SHORT[tp["lo"]], 17, WHITE if dark else INK, bold=True, font=SERIF, minpt=12)
    text(s, x + 0.25, 5.05, 3.45, 1.55, "\n".join("•  " + it for it in tp["items"][-2:]), 12.5, SOFT if dark else MUTED, lh=1.15, minpt=9)
for day in (1, 2):
    rows_ = [(f"{a}–{b}", t, "Assess" if tpn == -1 else ("—" if tpn == 0 else f"LU{tpn}")) for a, b, m, k, t, tpn in B.SCHEDULE[day]]
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
s = D.new(); header(D, s, "Roadmap · Activities", "Your Online Activity Studio", "Join your group board, let Meta Muse draft, type the best answers in, download PNG or PDF.")
T.qr(s, B.BCM_URL, 0.9, 2.55, 3.0)
t = text(s, 0.6, 5.85, 3.6, 0.4, B.BCM_URL.replace("https://", ""), 15, TEAL, bold=True, align="c", autofit=False)
t.click_action.hyperlink.address = B.BCM_URL
for i, (ic, ti, de) in enumerate([("users", "Group boards", "Join with a Board ID or QR; edits sync live"), ("pen", "Type your answers", "Straight into each block"),
                                  ("sparkles", "Meta Muse drafts", "Copy the Muse prompt from the board"), ("download", "Screenshot or PDF", "Paste into the PP tasks")]):
    y = 2.45 + i * 1.05; icon(s, ic, 4.8, y, 0.75)
    text(s, 5.75, y - 0.02, 6.9, 0.45, ti, 22, INK, bold=True, font=SERIF)
    text(s, 5.75, y + 0.45, 6.9, 0.45, de, 15, MUTED)
image(D, "Roadmap · Activities", "One Board per Outcome, One Screenshot per PP Task", asset("screenshots", "bcm-landing.png"),
      caption=f"{B.BCM_URL} · join your group board with the Board ID or QR · trainers create all group boards in one go")
PURL = B.BCM_URL + "prompts.html"
s = D.new(); header(D, s, "Roadmap · Meta Muse", "Fill in the Blanks. Copy. Paste into Muse.",
                    "Every prompt is a template: type your organisation once, fill the [blanks], copy the finished prompt.")
K.picture(s, asset("screenshots", "prompts-page.png"), 0.6, 2.35, maxw=7.9, maxh=4.4)
T.qr(s, PURL, 9.55, 2.4, 2.3)
t = text(s, 8.8, 4.85, 3.9, 0.4, PURL.replace("https://", ""), 14, TEAL, bold=True, align="c", autofit=False)
t.click_action.hyperlink.address = PURL
text(s, 8.8, 5.35, 3.9, 1.3, "Every prompt for Activities 1-3, in order. Type your organisation once. Saved in your browser only.", 15, MUTED, align="c", minpt=11)
image(D, "Roadmap · Activities", "From Group Board to PP Evidence in One Click", asset("screenshots", "bcm-screenshot-view.png"),
      side=[("camera", "Screenshot view", "Clean header: course, activity, group, your name, date"),
            ("download", "PNG or PDF", "One page, ready to paste into the PP"),
            ("pen", "Your own answers", "Each member writes the PP analysis individually")])

s = D.new()   # wsq-slides rule 7: title + LMS screenshot only (no kicker, no caption)
text(s, 0.6, 0.55, 12.1, 0.8, "Login to LMS and Download Course Material", 30, INK, bold=True, font=SERIF, cw=0.52)
K.picture(s, asset("screenshots", "lms-login.png"), 0.6, 1.55, maxw=12.1, maxh=5.3)
K.footer(D, s)
flow(D, "Learning Management System", "Download Course Material", [
    ("globe", "Open the LMS", "lms-tms.tertiaryinfotech.com"), ("mail", "Send OTP", "Your registered email"),
    ("lock", "Verify", "Key in the OTP"), ("folder", "Open the course", "Business Innovation with Agentic AI"),
    ("download", "Download", "Slides PDF + Learner Guide")])

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

# ====================================================================== WRAP-UP
mark("wrap")
s = D.new(dark=True); header(D, s, "Wrap-up", "Three Outcomes. One Business Ready to Move.")
for i, (tp, ic, line) in enumerate(zip(C.TOPICS, ["search", "map", "org"],
        ["BMC: you identified and evaluated where AI agents pay off.", "90-day plan: you planned how to get started in five steps.", "SCALE: you know how to sustain, review and grow it."])):
    x = 0.6 + i * 4.1; card(s, x, 2.0, 3.9, 4.4, fill=PANEL, shadow=False)
    icon(s, ic, x + 1.45, 2.3, 1.0)
    text(s, x + 0.2, 3.5, 3.5, 0.5, f"LO{i+1}", 16, ACC, bold=True, align="c", autofit=False)
    text(s, x + 0.2, 3.95, 3.5, 0.9, C.LO_SHORT[i], 24, WHITE, bold=True, font=SERIF, align="c", minpt=15)
    text(s, x + 0.25, 4.95, 3.4, 1.3, line, 16, SOFT, align="c", minpt=11)
T.big_statement(D, "Your next move", "Pick one process.\nName one DRI.\nShip in 90 days.", "Then let the numbers decide.", dark=True)
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
D.save(OUT)
mark("end")
json.dump(MARK, open(os.path.join(HERE, "slide_map.json"), "w"), indent=1)
print(f"Saved {OUT}  ({D.n} slides)")
