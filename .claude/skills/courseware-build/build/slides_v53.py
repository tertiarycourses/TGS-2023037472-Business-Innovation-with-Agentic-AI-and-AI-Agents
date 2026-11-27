"""v53 (22 Nov 2026) components and content: the consultant flow Discover -> Prove -> Transform.

Interactivity lives in the PowerPoint itself: internal hyperlinks (course map, SCALE navigator, quiz answers), room polls and
clickable knowledge checks. Links are registered while the deck is built and resolved just before save (forward references)."""
import os
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
import ccdeck as K
from ccdeck import (header, card, text, rich, icon, line, circle, box, picture, footer, tip, table,
                    ACC, ACC_D, TEAL, CHAR, PANEL, WHITE, INK, MUTED, SOFT, LIGHT, SERIF, MONO, DIM)
import data_bi as B

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", "courseware", "assets"))
def asset(*p): return os.path.join(A, *p)
GOOD = "3A7D7B"

# ------------------------------------------------------------------ internal links
ANCHORS, PENDING = {}, []
def anchor(key, s): ANCHORS[key] = s; return s
def link(shape, key): PENDING.append((shape, key)); return shape
def resolve():
    missing = sorted({k for _, k in PENDING if k not in ANCHORS})
    assert not missing, f"unresolved slide links: {missing}"
    for sh, k in PENDING: sh.click_action.target_slide = ANCHORS[k]

def button(s, x, y, w, h, label, key=None, fill=ACC, color=WHITE, size=12, url=None, bold=True, line_=None):
    """A clickable shape whose whole area is the link (text sits inside the shape, so a click anywhere works)."""
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.adjustments[0] = 0.18
    sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(fill)
    if line_: sh.line.color.rgb = RGBColor.from_string(line_); sh.line.width = Pt(1.25)
    else: sh.line.fill.background()
    sh.shadow.inherit = False
    tf = sh.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.08); tf.margin_top = tf.margin_bottom = Inches(0.02)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = label; r.font.size = Pt(size); r.font.bold = bold; r.font.name = K.SANS
    r.font.color.rgb = RGBColor.from_string(color)
    if key: link(sh, key)
    if url: sh.click_action.hyperlink.address = url
    return sh

def map_button(D, s, x=10.95, y=0.36):
    return button(s, x, y, 1.75, 0.36, "◀  Course map", "map", fill=PANEL if D.dark else WHITE,
                  color=SOFT if D.dark else INK, size=10.5, line_=None if D.dark else K.RULE)

# ------------------------------------------------------------------ attention and interaction slides
def quote(D, q, who=None, kicker="One line to remember", note=None):
    """A one-line quote, big serif type on charcoal. who=None marks a course maxim (no attribution invented)."""
    s = D.new(dark=True)
    circle(s, 11.2, -1.6, 3.6, ACC)
    text(s, 1.2, 1.25, 10.5, 0.4, kicker.upper(), 13, ACC, bold=True, autofit=False)
    text(s, 0.95, 1.55, 1.2, 1.3, "“", 110, ACC, bold=True, font=SERIF, autofit=False)
    text(s, 1.95, 2.25, 9.9, 2.7, q, 38, WHITE, bold=True, font=SERIF, cw=0.5, lh=1.08, minpt=22, anchor="m")
    text(s, 1.95, 5.15, 9.9, 0.5, f"— {who}" if who else "— Course maxim", 18, SOFT, font=SERIF, autofit=False)
    footer(D, s)
    if note: s.notes_slide.notes_text_frame.text = note
    return s

def poll(D, kicker, question, options, how="Raise 1, 2, 3 or 4 fingers, or type A, B, C or D in the chat.", note=None):
    """Room poll: one question, four answers, instant show of hands. The trainer reads the room, then reveals the point."""
    s = D.new(dark=True); header(D, s, kicker + " · Room poll", question)
    for i, opt in enumerate(options):
        r, c = divmod(i, 2); x = 0.6 + c * 6.1; y = 2.3 + r * 1.75
        card(s, x, y, 5.95, 1.55, fill=PANEL, shadow=False)
        circle(s, x + 0.3, y + 0.33, 0.9, ACC)
        text(s, x + 0.3, y + 0.33, 0.9, 0.9, "ABCD"[i], 30, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
        text(s, x + 1.45, y + 0.15, 4.3, 1.25, opt, 21, WHITE, font=SERIF, anchor="m", minpt=13)
    icon(s, "users", 0.6, 5.98, 0.58, fill=TEAL)
    text(s, 1.35, 6.0, 11.3, 0.55, how, 17, SOFT, anchor="m", minpt=12)
    if note: s.notes_slide.notes_text_frame.text = note
    return s

LIVE_HOW = "Vote with the QR code on the next slide, or raise 1, 2, 3 or 4 fingers."

def live_poll(D, topic, kicker, question):
    """v58 (owner): the room poll runs live on alfredang.github.io/livepoll, laid out as the C34 Ghana join slide:
    question left, results button, room code; right, the app's lime room code over a QR that opens the vote."""
    import io, qrcode
    code = B.LIVE_POLLS[topic]
    join, results = f"{B.LIVEPOLL_URL}?join={code}", f"{B.LIVEPOLL_URL}?results={code}"
    s = D.new(dark=True)
    text(s, 0.65, 0.46, 7.0, 0.36, f"Topic {topic} · Live poll".upper(), 14, ACC, bold=True, autofit=False)
    text(s, 0.65, 1.26, 7.0, 1.9, question, 32, WHITE, bold=True, font=SERIF, anchor="m", minpt=24, cw=0.52, lh=1.05)
    text(s, 0.69, 3.35, 6.7, 0.55, "Scan to vote. Open results to see the live tally.", 20, "E8E5DE", autofit=False)
    button(s, 0.71, 4.18, 3.05, 0.71, "Open the Poll Result", url=results, fill="E8E5DE", color=INK, size=20)
    text(s, 0.69, 5.04, 6.7, 0.45, f"If prompted, enter {code}.", 17, "C9C4B9", autofit=False)
    text(s, 8.16, 1.15, 4.4, 0.4, "SCAN TO VOTE", 16, WHITE, bold=True, align="c", autofit=False)
    card(s, 8.16, 1.84, 4.4, 3.2, fill="0E0E0C", shadow=False)
    text(s, 8.16, 1.95, 4.4, 1.05, code, 58, "C8F06A", bold=True, font=SERIF, align="c", anchor="m", autofit=False)
    card(s, 9.4, 3.08, 1.92, 1.82, fill=WHITE, shadow=False)
    img = qrcode.make(join, border=1); bio = io.BytesIO(); img.save(bio, format="PNG"); bio.seek(0)
    pic = s.shapes.add_picture(bio, Inches(9.55), Inches(3.15), Inches(1.68), Inches(1.68))
    pic.click_action.hyperlink.address = join
    footer(D, s)
    s.notes_slide.notes_text_frame.text = (
        f"Live poll room {code} (always active, one question). Learners scan the QR or open {join}. Show the tally: {results}. "
        "Before each new class clear the old votes: python3 courseware/.claude/scripts/livepoll_rooms.py --reset (then --verify). "
        "If the app is down, run the poll by show of hands from the previous slide.")
    return s

def pains(D, kicker, title, stat, stat_label, items, sub=None, source=None, url=None, stat_note=None):
    """Pain points: one dark evidence panel on the left, the named pains on the right."""
    s = D.new(); header(D, s, kicker, title, sub)
    top = 2.45 if sub else 2.05; bot = 6.55
    card(s, 0.6, top, 3.9, bot - top, fill=CHAR)
    text(s, 0.8, top + 0.35, 3.5, 0.35, "THE EVIDENCE", 12, ACC, bold=True, autofit=False)
    text(s, 0.8, top + 0.8, 3.5, 1.5, stat, 54, ACC, bold=True, font=SERIF, anchor="m", minpt=26)
    text(s, 0.8, top + 2.35, 3.5, 1.3, stat_label, 18, WHITE, bold=True, font=SERIF, minpt=12)
    if stat_note: text(s, 0.8, top + 3.6, 3.5, bot - top - 3.7, stat_note, 12.5, SOFT, minpt=9.5)
    n = len(items); gap = 0.12; h = (bot - top - gap * (n - 1)) / n
    for i, (t, d) in enumerate(items):
        y = top + i * (h + gap)
        card(s, 4.75, y, 7.95, h)
        box(s, 4.75, y, 0.09, h, fill=ACC)
        text(s, 5.05, y + 0.06, 2.95, h - 0.12, t, 17, INK, bold=True, font=SERIF, anchor="m", minpt=11)
        text(s, 8.05, y + 0.06, 4.5, h - 0.12, d, 13.5, MUTED, anchor="m", minpt=9.5)
    if source:
        from slides_bi import src
        src(D, s, source, url)
    return s

QUIZ = {}
def quiz(D, topic, qs):
    """Clickable knowledge check: a question slide whose four answers each jump to a reveal slide (answer + why)."""
    for n, (q, opts, ok, why) in enumerate(qs, 1):
        kq, kr = f"q{topic}-{n}", f"q{topic}-{n}r"
        s = anchor(kq, D.new()); header(D, s, f"Topic {topic} · Knowledge check · Question {n} of {len(qs)}", q,
                                      "Click your answer. Discuss with your neighbour first.")
        map_button(D, s)
        for i, o in enumerate(opts):
            r, c = divmod(i, 2)
            sh = button(s, 0.6 + c * 6.1, 2.5 + r * 1.85, 5.95, 1.6, f"{'ABCD'[i]}   {o}", kr, fill=WHITE, color=INK, size=19,
                        bold=False, line_=K.RULE)
            sh.text_frame.paragraphs[0].alignment = PP_ALIGN.LEFT; sh.text_frame.margin_left = Inches(0.3)
        text(s, 0.6, 6.35, 12.1, 0.4, "Clicking any answer opens the explanation.", 12, MUTED, autofit=False)
        s = anchor(kr, D.new()); header(D, s, f"Topic {topic} · Knowledge check · Answer {n} of {len(qs)}", q)
        map_button(D, s)
        for i, o in enumerate(opts):
            r, c = divmod(i, 2); x = 0.6 + c * 6.1; y = 2.05 + r * 1.2; right = i == ok
            card(s, x, y, 5.95, 1.05, fill=GOOD if right else WHITE, shadow=right, line=None if right else K.RULE)
            text(s, x + 0.3, y + 0.05, 5.4, 0.95, f"{'ABCD'[i]}   {o}", 16, WHITE if right else DIM, bold=right, anchor="m", minpt=10.5)
        card(s, 0.6, 4.6, 12.1, 1.55, fill=CHAR)
        rich(s, 0.9, 4.72, 11.5, 1.35, [[("WHY  ", dict(color=ACC, bold=True, size=15)), (why, dict(color=WHITE, size=17, font=SERIF))]], anchor="m")
        nxt = f"q{topic}-{n + 1}" if n < len(qs) else None
        if nxt: button(s, 10.35, 6.35, 2.35, 0.45, "Next question  ▶", nxt, size=12)
        else: text(s, 6.6, 6.4, 6.1, 0.4, "Knowledge check complete · continue", 12.5, ACC, bold=True, align="r", autofit=False)
    return s

def handson(D, kicker, title, sub, prompt_text, do, check, minutes=None, prompt_label="PROMPT  ·  activities/prompts.html"):
    """Short hands-on exercise: what to do (left), the prompt (centre), what good looks like (right)."""
    s = D.new(); header(D, s, kicker + (f" · {minutes} min" if minutes else ""), title, sub)
    top, bot = 2.45, 6.7
    card(s, 0.6, top, 3.6, bot - top, fill=CHAR)
    text(s, 0.85, top + 0.2, 3.1, 0.35, "DO THIS", 12, ACC, bold=True, autofit=False)
    for i, d in enumerate(do):
        y = top + 0.65 + i * 1.15
        circle(s, 0.85, y + 0.03, 0.42, ACC)
        text(s, 0.85, y + 0.03, 0.42, 0.42, str(i + 1), 13, WHITE, bold=True, align="c", anchor="m", autofit=False)
        text(s, 1.38, y - 0.03, 2.7, 1.1, d, 13.5, WHITE, minpt=9.5)
    card(s, 4.4, top, 5.6, bot - top, fill=K.CODEBG)
    for k, c in enumerate(("E06C5A", "E5B454", "7DB36B")): circle(s, 4.6 + k * 0.24, top + 0.18, 0.13, c)
    text(s, 5.4, top + 0.1, 4.5, 0.3, prompt_label, 10.5, DIM, autofit=False)
    text(s, 4.62, top + 0.5, 5.2, bot - top - 0.62, prompt_text, 15, "F1EDE4", font=MONO, minpt=9, cw=0.66, lh=1.06)
    card(s, 10.2, top, 2.5, bot - top)
    icon(s, "check", 10.45, top + 0.25, 0.62, fill=TEAL)
    text(s, 10.4, top + 1.0, 2.15, 0.4, "Good looks like", 15, INK, bold=True, font=SERIF, autofit=False)
    text(s, 10.4, top + 1.45, 2.15, bot - top - 1.55, check, 13, MUTED, minpt=9.5)
    return s

# ------------------------------------------------------------------ visuals
def orgtree(D, kicker, title, sub):
    """Outcome-tree org chart (Meridian, fictitious): leaders own outcomes; teams mix people and agents."""
    s = D.new(); header(D, s, kicker, title, sub)
    def node(x, y, w, lead, team, kind="mix"):
        card(s, x, y, w, 0.95, fill=WHITE, line=K.RULE)
        icon(s, "user", x + 0.12, y + 0.12, 0.36, fill=ACC)
        text(s, x + 0.55, y + 0.08, w - 0.6, 0.42, lead, 13.5, INK, bold=True, font=SERIF, anchor="m", minpt=9.5)
        fill = CHAR if kind == "agent" else "F1EDE4"
        card(s, x + 0.08, y + 0.52, w - 0.16, 0.36, fill=fill, shadow=False)
        text(s, x + 0.18, y + 0.53, w - 0.75, 0.34, team, 11, WHITE if kind == "agent" else INK, anchor="m", minpt=8.5)
        for j, ic in enumerate(["robot"] if kind == "agent" else ["user", "robot"]):
            icon(s, ic, x + w - 0.36 - j * 0.3, y + 0.565, 0.27, fill=ACC if ic == "robot" else TEAL)
        return x + w / 2, y, y + 0.95
    cx, _, cb = node(5.05, 2.3, 3.2, "CEO · AI sponsor", "Strategy & AI office: 2 people + agents")
    kids = [(0.6, "Head of Service Desk", "DRI · handling time"), (3.65, "Account Director", "DRI · client retention"),
            (6.7, "Operations Manager", "DRI · first-time fix"), (9.75, "Finance Lead", "DRI · cost per job")]
    teams = ["Coordinators + triage agent", "Account team + report agent", "Technicians + job-notes agent", "Finance team + invoice agent"]
    line(s, cx, cb, cx, cb + 0.3, K.MUTED, 1.5)
    line(s, 0.6 + 1.475, cb + 0.3, 9.75 + 1.475, cb + 0.3, K.MUTED, 1.5)
    for (x, lead, dri), tm in zip(kids, teams):
        line(s, x + 1.475, cb + 0.3, x + 1.475, 3.85, K.MUTED, 1.5)
        node(x, 3.85, 2.95, lead, tm)
        text(s, x, 4.84, 2.95, 0.3, dri, 11.5, ACC, bold=True, align="c", autofit=False)
    line(s, 0.9, 4.8, 0.9, 5.45, K.MUTED, 1.5, dash=True)   # left of the DRI label (QA v53: crossed it)
    card(s, 0.6, 5.45, 2.95, 0.6, fill=CHAR)
    text(s, 0.75, 5.47, 2.3, 0.56, "Overnight alerts: agent-run, audited daily", 11, WHITE, anchor="m", minpt=8.5)
    icon(s, "robot", 3.12, 5.6, 0.3, fill=ACC)
    lx = 4.0
    for ic, lab, fill in [("user", "Leader who owns an outcome (DRI)", WHITE), ("users", "Human + agent team", "F1EDE4"), ("robot", "Agent-run value stream, human-audited", CHAR)]:
        card(s, lx, 5.5, 2.85, 0.5, fill=fill, shadow=False, line=K.RULE)
        text(s, lx + 0.12, 5.5, 2.65, 0.5, lab, 10.5, WHITE if fill == CHAR else INK, anchor="m", minpt=8)
        lx += 2.95
    tip(D, s, "Ask of every box: which outcome does this person own, and which agents work for them? A box that only relays messages is the one to redesign.", y=6.3)
    return s

def line_chart(D, kicker, title, cats, series, sub=None, source=None, ymin=1, ymax=5, tipt=None):
    """Native PowerPoint line chart (editable): series = [(name, values, hex)]."""
    s = D.new(); header(D, s, kicker, title, sub)
    cd = CategoryChartData(); cd.categories = cats
    for name, vals, _ in series: cd.add_series(name, vals)
    top = 2.4 if sub else 2.0
    gf = s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(0.6), Inches(top), Inches(12.1), Inches(6.2 - top), cd)
    ch = gf.chart; ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout = False
    ch.legend.font.size = Pt(13); ch.legend.font.name = K.SANS
    va = ch.value_axis; va.minimum_scale = ymin; va.maximum_scale = ymax; va.major_unit = 1
    va.tick_labels.font.size = Pt(11); va.has_major_gridlines = True
    va.major_gridlines.format.line.color.rgb = RGBColor.from_string("E3DFD6")
    ca = ch.category_axis; ca.tick_labels.font.size = Pt(12); ca.tick_labels.font.name = K.SANS
    for plot in ch.plots:
        for ser, (_, _, hexc) in zip(plot.series, series):
            ser.format.line.color.rgb = RGBColor.from_string(hexc); ser.format.line.width = Pt(3)
            ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb = RGBColor.from_string(hexc)
            ser.marker.size = 9; ser.smooth = False
            ser.data_labels.show_value = True; ser.data_labels.font.size = Pt(11); ser.data_labels.font.bold = True
            ser.data_labels.font.color.rgb = RGBColor.from_string(hexc); ser.data_labels.position = XL_LABEL_POSITION.ABOVE
            ser.data_labels.number_format = "0.00"; ser.data_labels.number_format_is_linked = False
    if tipt: tip(D, s, tipt, y=6.3)
    if source:
        from slides_bi import src
        src(D, s, source)
    return s

def stack(D, kicker, title, layers, sub=None, tipt=None):
    """Layered governance stack, widest at the base: (label, who, what)."""
    s = D.new(); header(D, s, kicker, title, sub)
    n = len(layers); top = 2.4 if sub else 2.0; bot = 6.25 if tipt else 6.7; gap = 0.08
    h = (bot - top - gap * (n - 1)) / n
    for i, (lab, who, what) in enumerate(layers):
        inset = (n - 1 - i) * 0.14; y = top + i * (h + gap); x = 0.6 + inset; w = 12.1 - 2 * inset
        dk = i == 0
        card(s, x, y, w, h, fill=CHAR if dk else WHITE, line=None if dk else K.RULE)
        text(s, x + 0.2, y, 0.5, h, str(i + 1), 22, ACC, bold=True, font=SERIF, anchor="m", autofit=False)
        text(s, x + 0.7, y + 0.03, 2.9, h - 0.06, lab, 16, WHITE if dk else INK, bold=True, font=SERIF, anchor="m", minpt=10.5)
        text(s, x + 3.65, y + 0.03, 2.2, h - 0.06, who, 12, ACC, bold=True, anchor="m", minpt=9)
        text(s, x + 5.9, y + 0.03, w - 6.05, h - 0.06, what, 13, SOFT if dk else MUTED, anchor="m", minpt=9)
    if tipt: tip(D, s, tipt, y=6.35)
    return s

def shot(D, kicker, title, path, steps, sub=None, label=None, tipt=None):
    """Screenshot of an interactive tool on the left, numbered steps on the right."""
    s = D.new(); header(D, s, kicker, title, sub)
    top = 2.4 if sub else 2.0; bot = 6.2 if tipt else 6.7
    picture(s, path, 0.6, top, maxw=7.4, maxh=bot - top)
    if label:
        t = text(s, 0.6, bot + 0.02, 7.4, 0.28, label, 10.5, TEAL, bold=True, align="c", autofit=False)
    for i, (t_, d) in enumerate(steps):
        y = top + i * (bot - top) / len(steps)
        circle(s, 8.35, y + 0.04, 0.5, ACC)
        text(s, 8.35, y + 0.04, 0.5, 0.5, str(i + 1), 16, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
        text(s, 9.0, y, 3.7, 0.45, t_, 17, INK, bold=True, font=SERIF, minpt=12)
        text(s, 9.0, y + 0.45, 3.7, (bot - top) / len(steps) - 0.5, d, 13.5, MUTED, minpt=9.5)
    if tipt: tip(D, s, tipt, y=6.4)
    return s


# ================================================================== content (sources checked 22 Nov 2026)
MCK_2025 = "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025"
MCK_MAR25 = "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value"
METR = "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
GALLUP = "https://www.gallup.com/workplace/704252/workplace-separates-adopters-and-holdouts.aspx"
GARTNER = "https://www.gartner.com/en/newsroom/press-releases/2024-10-22-gartner-unveils-top-predictions-for-it-organizations-and-users-in-2025-and-beyond"
PROSCI_SPONSOR = "https://www.prosci.com/resources/articles/primary-sponsors-role-and-importance"
PROSCI_PROF = "https://www.prosci.com/blog/ai-adoption-challenges-how-to-turn-adoption-into-business-value"
PROSCI_LEAD = "https://www.prosci.com/blog/leading-ai-integration-what-separates-results-from-stalled-ai-investment"
MCK_ORG26 = "https://www.mckinsey.com/~/media/mckinsey/business%20functions/people%20and%20organizational%20performance/our%20insights/the%20state%20of%20organizations/2026/the-state-of-organizations-2026-vf.pdf"
KPMG = "https://kpmg.com/au/en/insights/artificial-intelligence-ai/trust-in-ai-global-insights-2025.html"

# ---------------------------------------------------------------- Topic 1 · Discover
# v58 (owner, 28 Nov 2026): Topic 1 follows the C34 Ghana Topic 1: the leaders' quotes open the always-on agents section.
LEADERS = (
    ("Sundar Pichai", "CEO of Google and Alphabet",
     "The conversation has gone from ‘Can we build an agent?’ to ‘How do we manage thousands of them?’",
     "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/ (Cloud Next 2026)",
     "pichai", "Lawrence Jackson / The White House, 4 May 2023, cropped. U.S. public domain. https://commons.wikimedia.org/wiki/File:V20230504LJ-0199-2.jpg"),
    ("Satya Nadella", "CEO of Microsoft",
     "… agents now can reason over those live transactions along with petabytes of historical records in real time.",
     "https://news.microsoft.com/events/wp-content/uploads/2026/11/Nadella_TRANSCRIPT_Ignite-Keynote_Nov-2026.pdf (Ignite, Nov 2026)",
     "nadella", "Lawrence Jackson / The White House, 4 May 2023, cropped. U.S. public domain. https://commons.wikimedia.org/wiki/File:V20230504LJ-0199-2.jpg"),
    ("Jensen Huang", "Founder and CEO of NVIDIA", "The age of AI Agentics is here.",
     "https://fortune.com/2025/01/07/nvidias-jensen-huang-says-ai-agents-are-a-multi-trillion-dollar-opportunity/ (CES, Jan 2025)",
     "huang", "Daniel Torok / The White House, cropped. U.S. public domain. https://commons.wikimedia.org/wiki/File:Jen-Hsun_Huang_2025.jpg"),
    ("Bill Gates", "Co-founder and former CEO of Microsoft",
     "Agents are not only going to change how everyone interacts with computers. They’re also going to upend the software industry…",
     "https://www.gatesnotes.com/ai-agents (Gates Notes, Nov 2023)",
     "gates", "Office of U.S. Senator Chris Coons, cropped. U.S. public domain. https://commons.wikimedia.org/wiki/File:Bill_Gates_-_Nov._8,_2019.jpg"),
)
MOLLICK = ("The shift from chatbot to agent is the most important change in how people use AI since ChatGPT launched.",
           "https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the?action=share")

def t1_leaders(D):
    """Four leaders on AI agents with portraits, plus Ethan Mollick (copied from C34 Ghana v57-based deck, agent_quote.py)."""
    s = D.new(dark=True)
    circle(s, 11.2, -1.6, 3.6, ACC)
    text(s, 0.62, 0.43, 10.0, 0.33, "TOPIC 1 · ALWAYS-ON AI AGENTS", 14, ACC, bold=True, autofit=False)
    text(s, 0.62, 0.83, 10.3, 0.6, "What Leaders Say About AI Agents", 32, WHITE, bold=True, font=SERIF, autofit=False)
    notes = ["Read one line per leader, then ask: which of these is already true in your company, and which is still a slide?"]
    for (who, role, q, src_, slug, credit), (x, y) in zip(LEADERS, [(0.65, 1.61), (6.73, 1.61), (0.65, 3.49), (6.73, 3.49)]):
        h = 1.74 if y < 3 else 2.03
        card(s, x, y, 5.94, h, fill=PANEL, shadow=False)
        pic = s.shapes.add_picture(asset("portraits", f"{slug}.jpg"), Inches(x + 0.12), Inches(y + 0.12), Inches(1.375), Inches(1.5))
        pic._element.nvPicPr.cNvPr.set("descr", f"Photograph of {who}")
        text(s, x + 1.65, y + 0.1, 4.13, 0.34, who, 20, "F2A383", bold=True, autofit=False)
        text(s, x + 1.65, y + 0.44, 4.13, 0.27, role, 12.5, "E8E5DE", autofit=False)
        text(s, x + 1.65, y + 0.76, 4.13, h - 0.86, f"“{q}”", 16.5, WHITE, font=SERIF, minpt=12, lh=1.05)
        notes += [f"{who} quotation source: {src_}", f"{who} photograph: {credit}"]
    card(s, 0.65, 5.65, 12.02, 1.04, fill=PANEL, shadow=False)
    text(s, 0.9, 5.8, 2.3, 0.36, "Ethan Mollick", 20, "F2A383", bold=True, autofit=False)
    text(s, 0.9, 6.17, 2.3, 0.3, "Wharton professor", 13, "E8E5DE", autofit=False)
    text(s, 3.15, 5.72, 9.3, 0.88, f"“{MOLLICK[0]}”", 19, WHITE, font=SERIF, anchor="m", minpt=14, lh=1.05)
    notes.append(f"Ethan Mollick quotation source: {MOLLICK[1]} (17 Feb 2026)")
    text(s, 0.65, 6.74, 12.0, 0.26, "Sources: Pichai, Google Cloud Next, 22 Apr 2026 · Nadella, Microsoft Ignite keynote, Nov 2026 · Huang, CES, Jan 2025 · "
         "Gates, Gates Notes, Nov 2023 · Mollick, One Useful Thing, 17 Feb 2026. Links in the notes.", 9.5, K.DIM, autofit=False)
    footer(D, s)
    s.notes_slide.notes_text_frame.text = "\n".join(notes)
    return s

def t1_tools_skills(D):
    """v58: from the C34 Ghana Topic 1, with Meridian examples."""
    return K.compare(D, "Topic 1 · Tools and skills", "Tools Act. Skills Guide the Work.",
        ("Tool · a callable operation", "tool", ["Read a new request from the shared inbox.", "Open a ticket in ServiceNow or book a technician's visit."]),
        ("Skill · a reusable procedure", "book", ["Define how to triage a request and route it.", "Define what a complete ticket holds and how to check it."]),
        tipt="Permissions still govern what any agent may do with its tools.")

def t1_decision(D):
    """v58: from the C34 Ghana Topic 1 decision slide: the scored ideas become one pilot, one next, one parked."""
    s = D.new(); header(D, s, "Topic 1 · Choose the first pilot", "Three Options for Meridian: Pilot, Queue, Park",
                        "Start where the data is ready, the work repeats and a person can verify the outcome.")
    for i, (label, action, ev) in enumerate((
            ("80 · Pilot request triage", "Into Topic 2's 90-day pilot", "Reads every request and opens the ticket. A coordinator approves urgent routing."),
            ("75 · Monthly client reports", "Next in line", "Second-highest score. Build it once the triage pilot proves the data flow."),
            ("24 · Park the fault predictor", "Score it again later", "Lowest score. Revisit when value, feasibility or data improves."))):
        x = 0.6 + i * 4.1; dk = i == 0
        card(s, x, 2.53, 3.9, 3.8, fill=CHAR if dk else WHITE)
        text(s, x + 0.23, 2.8, 3.38, 0.65, label, 20, WHITE if dk else INK, bold=True, font=SERIF, minpt=16)
        text(s, x + 0.23, 3.57, 3.38, 0.42, action, 16, "F2B49B" if dk else ACC_D, bold=True, minpt=14)
        text(s, x + 0.23, 4.24, 3.38, 1.48, ev, 17, SOFT if dk else INK, minpt=15)
    return s

def t1_open(D):
    poll(D, "Topic 1 · Discover", "How Much of Your Team's Week Could an AI Agent Take On Today?",
         ["Under 10%: our work is mostly judgement and relationships", "10-30%: some drafting, sorting and chasing",
          "30-50%: a lot of re-keying, reports and status updates", "Over 50%: most of our week is rule-based paperwork"],
         how=LIVE_HOW, note="Count hands, note the spread on the whiteboard. Return to it after the pain-point hunt before Activity 1: did the estimate move once people listed real tasks and hours?")
    live_poll(D, 1, "Topic 1 · Discover", "How Much of Your Team's Week Could an AI Agent Take On Today?")
    pains(D, "Topic 1 · Where companies get stuck", "Most Firms Use AI. Few Can Show It in the Numbers.",
          "39%", "see any EBIT impact from AI, though 88% use it in at least one function",
          [("Tools before problems", "“We bought the licences; now find a use.” The search starts from the product, not the pain."),
           ("Ideas chosen by hype", "The demo that wowed the board wins, not the process that bleeds hours every week."),
           ("Data not ready", "The records sit in inboxes, spreadsheets and heads: scattered, messy or off-limits."),
           ("Nobody owns the result", "The idea belongs to IT, so no one in the business answers for the number."),
           ("No baseline", "Nobody measured the 'before', so nobody can prove the 'after'.")],
          sub="Your first job as the AI consultant: find the opportunity that moves a number the CEO already tracks.",
          source="McKinsey, The state of AI in 2025 (5 Nov 2025, n=1,993)", url=MCK_2025,
          stat_note="Respondents' organisations. High performers were nearly three times as likely to have redesigned workflows.")

def t1_functions(D):
    from slides_bi import icons
    icons(D, "Topic 1 · Where agents pay off", "Every Function Has a Process That Bleeds Hours", [
        ("trend", "Sales", "Qualify leads overnight; draft the follow-up the rep sends"),
        ("chat", "Customer service", "Answer, check order status, hand hard cases to a person"),
        ("coins", "Finance", "Match invoices to orders; flag exceptions for approval"),
        ("user", "HR", "Screen applications against criteria; book interviews"),
        ("gear", "Operations", "Triage requests, plan schedules, chase overdue jobs"),
        ("megaphone", "Marketing", "Draft campaign variants; report weekly what worked")], cols=3,
        sub="Illustrative patterns, not vendor claims. Your pain-point hunt will find your own.",
        tipt="Look for work that is high-volume, rule-guided and easy to check: agents pay off there first.")

# v58 (owner): the Topic 1 knowledge check was removed (Topic 1 follows the C34 Ghana flow); Topics 2 and 3 keep theirs.

def t1_hunt(D):
    quote(D, "Point your first AI agent at the pain, not at the platform.", kicker="Topic 1 · Activity 1")   # v56: maxims about AI agents too
    h = B.PAIN_HUNT
    # v58 (owner asked "is it for the padlet?"): yes; the hunt now happens on the team padlet, the Muse prompt is optional
    handson(D, "Topic 1 · Activity 1 · On your team padlet", "Pain-Point Hunt: Post Three Time-Sinks, Vote for One",
            "Still on your team padlet: post the work that wastes the most hours. The most-liked card goes on your BMC.",
            h["prompt"], ["Alone, 3 min: post three cards on your team padlet, one task each, with rough hours per week.",
                          "Together, 2 min: group the repeats and like the cards you agree with. The most-liked card wins.",
                          "Carry the winner into your BMC as your first opportunity."], h["check"], minutes=h["minutes"],
            prompt_label="OPTIONAL  ·  ask Muse to check your top three")

# ---------------------------------------------------------------- Topic 2 · Prove
def t2_open(D):
    quote(D, "Success in the LLM space isn’t about building the most sophisticated system. It’s about building the right system for your needs.",
          "Anthropic, “Building Effective Agents”, December 2024", kicker="Topic 2 · Prove",
          note="Source: https://www.anthropic.com/research/building-effective-agents (19 Dec 2024; original: 'Success in the LLM space isn't about ...'; checked 23 Nov 2026). Point: prove the simplest agent that fixes one process against a baseline before anyone buys a platform.")
    poll(D, "Topic 2 · Prove", "AI Promises Greater Efficiency. Has It Delivered That for You?",
         ["Yes, and we measured it", "Yes, it feels faster", "Not yet", "It created more work to check"],
         how=LIVE_HOW, note="B is the trap: feeling faster is not being faster. The next slide shows experts who felt 20% faster and measured 19% slower.")
    live_poll(D, 2, "Topic 2 · Prove", "AI Promises Greater Efficiency. Has It Delivered That for You?")
    pains(D, "Topic 2 · Where pilots stall", "Pilot Purgatory: Where Good Ideas Go to Wait",
          "−19%", "measured change in speed; the same developers expected +24%",
          [("Five demo cases, five hundred real ones", "The demo passes; the messy, urgent and incomplete cases fail."),
           ("No baseline", "Nobody timed the 'before', so the 'after' is a feeling."),
           ("Self-reported gains", "“It feels faster” is an adoption signal, not a business benefit."),
           ("Surprise bills", "Agent loops re-read their context every step: token use multiplies."),
           ("Nobody owns go / no-go", "The pilot never ends and never scales."),
           ("Works in the chat, not in the system", "Staff still re-key the agent's output into the tool they use.")],
          sub="Your second job as the AI consultant: prove it works here, on real cases, against a baseline.",
          source="METR randomised trial, 16 experienced developers, 246 tasks (10 Jul 2025)", url=METR,
          stat_note="After the trial they still believed AI had sped them up by 20%.")

def t2_test(D, mark):
    from slides_bi import icons, bignums
    mark("t2test")
    quote(D, "Trust the test, not the demo.", kicker="Topic 2 · Test before you trust")
    icons(D, "Topic 2 · Test before you trust", "Build a 30-Case Test Set Before the Pilot Starts", [
        ("inbox", "18 routine", "The everyday cases that make up most of the volume"),
        ("alert", "4 urgent", "The ones that must reach a person fast"),
        ("search", "4 incomplete", "Missing site, contact or details: does it ask?"),
        ("scale", "2 conflicting", "Two rules disagree: does it escalate?"),
        ("bolt", "2 hostile", "A hidden instruction in the email: does it obey?")], cols=5,
        sub="Real, anonymised cases from your mined process, with the right answer written down first by the process owner.",
        tipt="Meridian: 30 past requests from 2 sites, answers agreed by two senior coordinators before the agent saw them.")
    from ccdeck import cards
    cards(D, "Topic 2 · Test before you trust", "Score Every Output on Four Checks", [
        ("Correct", "Facts, site, fault and urgency are right. One wrong urgent case fails the round.", "check"),
        ("Complete", "Every required field is filled, or the agent asks for what is missing.", "list"),
        ("Compliant", "It follows the approval rules and never sends, pays or deletes on its own.", "shield"),
        ("Cost", "A person can approve it in under 2 minutes; tokens per case stay within budget.", "coins")], cols=4,
        sub="Your group scores every row. The agent's self-score is a claim, not a result.",
        tipt="Set the bar before you test: Meridian moves to assist mode only at 27 of 30 correct and 30 of 30 urgent cases escalated.")
    from ccdeck import flow
    flow(D, "Topic 2 · Test before you trust", "Three Test Rounds, Then a Decision", [
        ("history", "Replay", "Run the 30 past cases offline. Compare with the agreed answers."),
        ("eye", "Shadow", "Agent drafts on live cases; staff still do the work; compare daily."),
        ("check", "Assist", "Agent drafts; a person approves every action; measure time and rework."),
        ("flag", "Decide", "Day 90: scale, redesign, hold or stop on the numbers.")],
        sub="Each round earns the next. Topic 3 takes the winners from one team to the whole company.")
    bignums(D, "Topic 2 · Measure, don't ask", "Feeling Faster Is Not Being Faster", [
        ("+24%", "expected", "Developers' forecast of the AI speed-up"),
        ("−19%", "measured", "Actual change in time per task"),
        ("+20%", "still believed", "Their estimate after the trial")],
        sub="Measure real output against the baseline from Step 1. Self-reported gains show adoption, not benefit.",
        source="METR, Measuring the impact of early-2025 AI on experienced open-source developer productivity (10 Jul 2025)", url=METR)

def t2_handson_test(D):
    st = B.LAB[2]["steps"][3]
    handson(D, "Topic 2 · Activity 2 · Task 4 of 8", "Test Before You Trust: Score 10 Real Cases", st["body"][0],
            st["prompt"], ["Pick 10 anonymised cases: 6 routine, 2 urgent, 1 incomplete, 1 conflicting.",
                           "Paste them into Muse with the prompt. Nothing is sent.",
                           "Re-score every row as a group. Write the pass rate and your go/no-go bar into Success Measures."],
            st["check"], minutes=20)

T2_QUIZ = [
    ("Before You Choose an Agent, What Must Step 1 Record?",
     ["The vendor and the licence price", "The baseline, the target and one counter-metric", "The prompt you will use", "The model name"], 1,
     "No agent before a goal. Meridian: 18 minutes per request today, 11 or less by day 90, complaints at or below 2%."),
    ("The Agent Passed Five Demo Cases. What Is Your Next Move?",
     ["Go live on all sites", "Run a 30-case test set with urgent, incomplete and conflicting cases", "Buy more licences", "Ask staff whether they like it"], 1,
     "The demo is five cases; the business is five hundred. Test the hard cases, set the bar first, then shadow and assist."),
    ("Staff Say They Are 25% Faster. Measured Time per Request Went Up. Which Do You Trust?",
     ["The staff survey", "The measured time against the baseline", "The vendor's benchmark", "The average of the two"], 1,
     "Self-reported gains are an adoption signal. In METR's trial, developers felt 20% faster and were 19% slower."),
]

# ---------------------------------------------------------------- Topic 3 · Transform
def t3_open(D, mark):
    """v54 order (kept for reference). v55 calls t3_quote, t3_cartoon and t3_challenges separately."""
    t3_quote(D); t3_cartoon(D); t3_challenges(D)

def t3_quote(D):
    quote(D, "From the boardroom to the frontline, every worker will need to think like the CEO of an agent-powered startup.",
          "Microsoft 2025 Work Trend Index, April 2025", kicker="Topic 3 · Transform",
          note="Source: https://blogs.microsoft.com/blog/2025/04/23/the-2025-annual-work-trend-index-the-frontier-firm-is-born/ (checked 23 Nov 2026). Point: when everyone manages agents, the org chart, job descriptions, training and governance all have to change. That is Topic 3.")

def t3_cartoon(D):
    from slides_bi import full_image
    full_image(D, "Topic 3 · C · The future organisation", "AI Made Work Generation Almost Free. Owning the Work Is Still Expensive.",
               asset("v53", "office-baby-generator.png"),
               "Making the output is easy. Checking, approving and owning 500 of them a day is the real job.")

def t3_challenges(D):
    poll(D, "Topic 3 · The challenges", "Is Your Organisation Built to Benefit from AI?",
         ["Yes: roles and workflows were redesigned", "Partly: some teams have changed how they work",
          "Not yet: AI is a personal tool people use alone", "We have not started"],
         how=LIVE_HOW, note="Most rooms answer C. That is the point of Topic 3: personal AI skill does not add up to company capability, and it leaves when the person leaves.")
    live_poll(D, 3, "Topic 3 · The challenges", "Is Your Organisation Built to Benefit from AI?")
    pains(D, "Topic 3 · The challenges · why transformations stall", "Six Reasons the Change Does Not Stick",
          "72%", "of 10,018 leaders say their organisation is not fully ready for the changes ahead",
          [("Aimed at the wrong target", "Awareness campaigns and prompt classes, when the gaps are judgement and incentives."),
           ("Skills that walk out the door", "The know-how lives in a few enthusiasts' chats. When they leave, it leaves."),
           ("Managers without time", "Asked to coach AI use on top of a full day, with no change to their targets."),
           ("Token bills nobody owns", "Usage grows faster than anyone can prove value; then a blanket ban arrives."),
           ("Shadow AI and policy lag", "Staff use tools nobody approved; the policy arrives after the incident."),
           ("Leaders over-rate themselves", "Prosci: on 1:1 AI conversations, leaders rate themselves 3.55 of 5; employees see 2.38.")],
          sub="Your third job as the AI consultant: make it the way the company works, not a tool a few people use.",
          source="McKinsey, The State of Organizations 2026 (n = 10,018 leaders) · Prosci, Leading AI integration (Sep 2026)", url=MCK_ORG26)

def t3_outcomes(D):
    from slides_bi import bignums
    table(D, "Topic 3 · The challenges · outputs to outcomes", "Adoption Runs Projects. Transformation Runs the Business.",
          ["", "Adoption operating model", "Transformation operating model"], [
              ["Conditions", "Known rules and known unknowns; plan it once", "Unknown unknowns: markets, customers and the technology keep moving"],
              ["Funding", "Fixed budget tied to a scope; new work needs new approval", "Steady funding for a value stream, adjusted to outcomes"],
              ["Time", "Start and end date; success declared at go-live", "Continuous ownership; success measured over the life cycle"],
              ["Success", "On time, on budget, scope delivered", "Customer, employee and business outcomes delivered"],
              ["Risk", "Reduced up front with heavy planning", "Reduced by fast iteration, learning and options"],
              ["Teams", "People lent to a project, then moved on", "Stable teams that own an outcome, with their agents"],
              ["AI", "Speeds up output; magnifies planning and alignment gaps", "Scales iteration, learning and outcome delivery"]],
          colw=[1.6, 5.0, 5.5], size=12.5, hi_col=2,
          sub="You cannot build a one-off project team around a technology that changes every quarter.")
    bignums(D, "Topic 3 · The challenges · outputs to outcomes", "The Value Sits in Redesigned Work, Not in More Usage", [
        ("88%", "use AI", "in at least one business function"),
        ("39%", "see EBIT impact", "any level, at enterprise level"),
        ("~3×", "high performers", "more likely to have redesigned workflows")],
        sub="Usage is nearly universal; profit is not. The firms that win redesign whole workflows and measure them.",
        source="McKinsey, The state of AI in 2025 (5 Nov 2025)", url=MCK_2025)
    bignums(D, "Topic 3 · The challenges · who owns AI", "Put Ownership Where the Decisions Are Made", [
        ("#1", "workflow redesign", "Of 25 attributes tested, the biggest effect on EBIT impact"),
        ("CEO", "owns governance", "One element most correlated with bottom-line impact; strongest at large firms"),
        ("28%", "actually do it", "say their CEO oversees AI governance")],
        sub="AI is not an IT project. The CEO sponsors it; the people who run each process own its results.",
        source="McKinsey, The state of AI: How organizations are rewiring to capture value (12 Mar 2025)", url=MCK_MAR25)

def t3_diagnostic(D, mark):
    from ccdeck import cards, rows
    mark("act3a")
    cards(D, "Topic 3 · Activity 3 Part A · AI readiness diagnostic · 15 min", "Score Your Company on Six Dimensions of Readiness",
          [(f"{n}   /20", d) for n, d in B.READINESS_DIMS], cols=3,
          sub="Four statements each, scored 1-5 for how things are today, not how you hope they are. Alone, 5 minutes.", desc_pt=14,
          tipt="Open ai-readiness-scorecard.html from the Activity 3 folder (LMS download). Nothing leaves your browser.")
    shot(D, "Topic 3 · Activity 3 Part A · Hands-on", "Your Readiness Shape in Five Minutes", asset("v53", "readiness-scorecard.png"), [
        ("Score alone", "Tap 1-5 on all 24 statements. Be honest: this is for you."),
        ("Read the shape", "The radar shows your lowest dimension. That is where the change will stall."),
        ("Copy the scores", "Paste them into the Step 1 prompt; Muse names a 30-day move."),
        ("Share the shape", "In your group, share the lowest dimension, not the number.")],
        label="activities/activity-03-…/ai-readiness-scorecard.html · works offline · nothing is sent")
    rows(D, "Topic 3 · Activity 3 Part A · Breakout · 10 min", "Share the Shape, Not the Score", [
        ("search", "Which dimension came out lowest, and does it surprise you?", "Share numbers only if you want to."),
        ("eye", "What does that low score look like day to day?", "Give one concrete example from your own team this month."),
        ("users", "Who would have to act differently for it to move?", "Name the role, and what stops them today."),
        ("flag", "What is one change you could make in the next 30 days without new budget?", "Write it down: it goes into your SCALE board.")],
        dark=True, tipt="Introduce yourself first in 60 seconds: name, organisation, role, and what you are curious about in AI adoption.")

def scale_nav(D, rows_):
    """SCALE framework slide whose five columns jump to their sections (clickable navigator)."""
    from slides_bi import framework
    rows_ = [(l, w_, d, ic) for (l, w_, _x, ic), d in zip(rows_, ["Stakeholders, sponsors and an honest story",
             "Outcome org chart; DRIs lead people + agents", "Redesign jobs, train for ability, coach",
             "Build AI into the process, not the person", "Govern, cost, secure; judge vs baseline"])]
    s = framework(D, "Topic 3 · The SCALE framework · click a letter", "SCALE", "SCALE: Five Moves That Make the Change Stick", rows_,
                  "You have seen the future org and why change stalls. These five moves make the change last.",
                  tipt="Click a column to jump to it. Each section ends with a ◀ SCALE button back here.")
    anchor("scale", s)
    w = 12.1 / 5
    for i, (letter, *_rest) in enumerate(rows_):
        button(s, 0.6 + i * w + 0.25, 5.8, w - 0.5, 0.42, f"Go to {letter}  ▶", f"s{letter}", size=12)
    return s

def back_scale(D, s, letter):
    anchor(f"s{letter}", s)
    button(s, 10.95, 0.36, 1.75, 0.36, "◀  SCALE", "scale", fill=PANEL if D.dark else WHITE,
           color=SOFT if D.dark else INK, size=10.5, line_=None if D.dark else K.RULE)

def t3_story(D):
    from slides_bi import quadrant
    from ccdeck import rows, loop
    quadrant(D, "Topic 3 · S · Buy-in · stakeholders", "Map Who Can Stop It and Who Has to Live With It", [
        ("Keep satisfied", "Board, finance, legal and the data protection officer: brief them early, show the controls and the numbers."),
        ("Manage closely", "CEO sponsor, heads of department, IT and security: co-own the plan, decide together, meet weekly."),
        ("Monitor", "Vendors and teams outside the pilot: share updates; watch for knock-on effects."),
        ("Involve and inform", "Frontline staff, clients and staff representatives: ask what the plan misses; tell them what changes first.")],
        "Interest in the change  →", "Power  ↑",
        sub="Meridian: coordinators had the least power and the most to lose. They heard the story first.")
    table(D, "Topic 3 · S · Buy-in", "Three Standard Moves, Aimed at the Wrong Target", ["The usual move", "The hidden assumption", "What works instead"], [
        ["Awareness campaigns", "People don't know why AI matters", "Most already use AI (66% regularly, KPMG 2025). Explain why it matters to this company and this role."],
        ["More town halls and leadership videos", "Resistance is a communication problem", "It is usually an incentive problem: change time, targets and recognition. No video fixes an incentive."],
        ["Tool and prompt training", "Prompting is the gap", "The gap is judgement: knowing whether the output is good enough to send. People who lack it cannot see that they do."]],
        colw=[2.8, 3.3, 6.0], size=12.5, sub="Right intentions, wrong assumptions: three activities most AI programmes run first.",
        tipt="Source: KPMG & University of Melbourne, Trust, attitudes and use of AI: a global study 2025 (48,000+ people, 47 countries).")
    loop(D, "Topic 3 · S · Buy-in · one person at a time", "ADKAR Is a Loop, Not a Line", [
        ("lightbulb", "Awareness", "Why this change, here, now"), ("heart", "Desire", "What is in it for me and my team"),
        ("book", "Knowledge", "How to work with the agent"), ("tool", "Ability", "Doing it on real work, with coaching"),
        ("medal", "Reinforcement", "Recognition, targets and habits that hold")],
        sub="The plan reads left to right. In practice, every new model or tool restarts the loop: sense, adjust, repeat.",
        foot="Successful AI integration happens one person at a time.")

def t3_sponsor(D):
    from ccdeck import rows
    s = rows(D, "Topic 3 · C · Lead by example · the C-suite", "What an Effective AI Sponsor Does Differently", [
        ("eye", "Active and visible, all the way through", "Present across the whole life cycle, not just the launch. The common failure: the sponsor who delegates and disappears."),
        ("users", "Builds a coalition", "Sponsorship cascades through peers and people managers. One keen executive with unaligned heads reads, from below, as no sponsor at all."),
        ("megaphone", "Communicates directly", "Staff want the business reason from the most senior person, not routed through IT or the project team."),
        ("sparkles", "Shows fluency", "Sponsors who use the tools themselves, and say so, give everyone else permission to experiment.")],
        sub="Prosci: active and visible sponsorship has been the top contributor to change success in every benchmarking report since 1998.",
        dark=False)
    from slides_bi import src
    src(D, s, "Prosci, The primary sponsor's role and importance (Prosci benchmarking since 1998)", PROSCI_SPONSOR)

def t3_commanders(D):
    from slides_bi import vs
    s = orgtree(D, "Topic 3 · C · The future organisation · Meridian", "Draw the Org Chart Around Outcomes, Not Functions",
                "Each leader owns one outcome and a team of people and agents. Some value streams run on agents, audited by a person.")
    back_scale(D, s, "C")
    return s

def t3_managers(D):
    from slides_bi import vs
    vs(D, "Topic 3 · C · The future organisation · managers", "Middle Managers Become Outcome Managers",
       ("Observed: managers are the lever", "check", ["Gallup, Feb 2026, 23,717 US staff:", "78% with strongly supportive managers use AI often; 44% of the rest do."]),
       ("Forecast: 'AI will gut middle management'", "alert", ["Gartner, Oct 2024: by 2026, 20% of firms flatten with AI, cutting over half of middle managers.", "A forecast, not an observation."]),
       sub="Plan for the evidence, not the headline: give managers time, targets and authority to run human + agent teams.",
       source="Gallup (12 Apr 2026) · Gartner press release (22 Oct 2024)")

def t3_augment(D):
    t3_coaching_gap(D); t3_training_ability(D)

def t3_training_ability(D):
    from slides_bi import vs
    vs(D, "Topic 3 · A · AI training", "Training That Transfers Knowledge vs Training That Builds Ability",
       ("Knowledge only", "book", ["One-off tool and prompt classes", "E-learning completion targets", "Static policy decks", "Confidence surveys"]),
       ("Builds ability", "tool", ["Practice on their own work", "Daily coaching from the manager", "Teams judge real output together", "Feedback on output, not self-rating"]),
       sub="Prosci: user proficiency is the largest AI adoption challenge, 38% of those reported.",
       source="Prosci, AI adoption challenges (Sep 2026)")

def t3_coaching_gap(D):
    from slides_bi import bignums
    bignums(D, "Topic 3 · A · AI coaching", "Leaders Think They Coach. Staff Don't See It.", [
        ("3.55", "leaders' self-rating", "How often they hold 1:1 AI conversations (of 5)"),
        ("2.38", "employees' view", "How often employees see it happen (of 5)"),
        ("1.17", "the gap", "Widest on private, hard-to-verify behaviours")],
        sub="Make coaching visible: ask employees what they have seen, not only leaders what they did.",
        source="Prosci, Leading AI integration: what separates results from stalled AI investment (Sep 2026)", url=PROSCI_LEAD)

def t3_loop(D):
    from slides_bi import vs
    from ccdeck import flow
    s = quote(D, "If the AI skill lives in one person, it leaves with them.", kicker="Topic 3 · L · Loop AI into the process")
    back_scale(D, s, "L")
    vs(D, "Topic 3 · L · Process, not person", "Personal AI Skill Is Not Company Capability",
       ("Lives in a person", "user", ["Prompts in one person's chat history", "Know-how in one enthusiast's head", "Gone when they resign or transfer", "Nobody else can check or improve it"]),
       ("Lives in the process", "org", ["Playbook in the SOP and the system", "Shared, versioned prompts and skills", "An owner and a backup owner", "New staff inherit it on day one"]),
       sub="The test: if your best AI user left on Friday, would Monday's work still run the same way?")
    flow(D, "Topic 3 · L · Build it into the process", "Five Moves to Make AI Part of How the Work Runs", [
        ("route", "Map the process", "Use the mined process from Step 2 of your plan."),
        ("file", "Write the playbook", "Instructions, examples, checks: inside the SOP, not a personal chat."),
        ("plug", "Work inside the system", "Agent sits in the ticketing, CRM or ERP staff already use."),
        ("check", "Write in the checkpoints", "Which steps a person approves, named in the SOP."),
        ("history", "Version and own it", "Owner, backup owner, change log, review date.")],
        sub="Agents join the operation the way a new procedure does: documented, owned, trained and audited.")
    table(D, "Topic 3 · L · AI capability register", "Keep a Register of Every Agent and Who Owns It",
          ["Process", "Agent", "Owner (DRI)", "Backup owner", "Playbook lives in", "Controls", "Measure"],
          [list(r) for r in B.CAPABILITY_REGISTER], colw=[1.45, 1.6, 1.6, 1.45, 2.0, 2.3, 1.7], size=11,
          sub="Meridian (fictitious). One row per agent. When someone leaves, the row tells the next person exactly what to pick up.",
          tipt="Review the register monthly with the risk owner. An agent without an owner is switched off.")

def t3_govern(D, mark):
    from slides_bi import icons, bignums
    s = stack(D, "Topic 3 · E · Govern", "Six Layers of AI Governance, From Boardroom to Desk", [
        ("Accountable owner", "CEO-level sponsor", "An AI steering group chaired by a senior executive; it approves the register and the budget."),
        ("Acceptable-use policy", "Everyone signs", "One page: what AI may be used for, what never, and who to ask."),
        ("Data classes", "Data protection officer", "Public, internal, confidential, personal: which class may go into which tool (PDPA)."),
        ("Approved tools", "IT and security", "The list, how to request a new tool, and how fast you will answer."),
        ("Approval thresholds", "Process owners (DRIs)", "Which agent actions need a person: sends, payments, deletions, anything affecting people."),
        ("Incident response", "Duty manager", "How to pause an agent, who to call, how to tell the people affected.")],
        sub="Light enough to read, strong enough to stop a bad day. Meridian's policy fits on two pages.",
        tipt="Shadow AI is a signal, not a crime: if staff use unapproved tools, the approved path is too slow.")
    back_scale(D, s, "E")
    table(D, "Topic 3 · E · Govern access", "Three Ways Organisations Now Govern AI Access",
          ["Model", "What changes", "Reported examples", "Leadership question"], [
              ["Restricted use", "Some tools blocked for certain work, data or locations", "Nvidia keeps Claude Fable to lower-stakes work (Sep 2026). Booz Allen bars it from the cyber software it sells. Goldman Sachs and JPMorgan removed Claude for Hong Kong staff (Apr-Jun 2026).", "Are our limits based on real risk, or on caution?"],
              ["Earned access", "The tool comes after training or reading the AI policy", "Telstra: Copilot training before a licence, 18,000+ completions. Softcat: an 11-minute video and the AI policy first.", "What is the minimum proof of readiness before access?"],
              ["Rationed use", "Unlimited use replaced by a budget per person or tool", "Uber: US$1,500 a month per person per AI coding tool (Jun 2026). Walmart: fixed token allowance for its in-house coding assistant. Accenture: US$29 a month per person on Claude, more from project budgets.", "How do we share the budget without starving high-value work?"]],
          colw=[1.7, 2.6, 5.0, 2.8], size=11, hi_col=0,
          sub="Most firms will use all three: restrict the risky, earn the powerful, ration the expensive.",
          tipt="Sources (news reports, some on anonymous sources): The Information/PYMNTS, Bloomberg, FT via Reuters, UTS HTI case study, Microsoft, 404 Media.")
    mark("t3cost")
    quote(D, "Every token is a purchase order. Someone should approve the budget.", kicker="Topic 3 · E · Token cost")
    bignums(D, "Topic 3 · E · Token cost", "Agents Multiply Tokens: Chat Is One Call, an Agent Is Many", [
        ("1×", "a chat", "One question in, one answer out"),
        ("4-10×", "an agent task", "Plans, calls tools, checks; re-reads its context every step"),
        ("80×", "price spread", "US$0.50 vs US$40 per million output tokens, smallest to largest model")],
        sub="You pay for every token in and out, on every step. Cost is set by the model, the context size and the number of steps.",
        source="Anthropic API list prices, checked 22 Nov 2026", url=B.TOKEN_PRICE_SOURCE)
    table(D, "Topic 3 · E · Token cost", "Price the Model to the Job, Not the Other Way Round",
          ["Model", "Input, US$ per 1M tokens", "Output, US$ per 1M tokens", "Use it for"],
          [[m, f"{i:.2f}", f"{o:.2f}", u] for m, i, o, u in B.TOKEN_PRICES], colw=[3.0, 2.6, 2.6, 3.9], size=14,
          sub="One million tokens is roughly 750,000 words. Batch processing is 50% off; cached input costs 2.5-10% of the input price, by model.",
          tipt="Prices change often: check the vendor's page and date-stamp it in your plan. Anthropic list prices, 22 Nov 2026.")
    icons(D, "Topic 3 · E · Token cost", "Five Levers to Cut the Bill Without Cutting Quality", [
        ("route", "Route", "Smallest model that passes your 30-case test"),
        ("memory", "Cache", "Re-use fixed instructions: 90-97.5% off"),
        ("calendar", "Batch", "Run non-urgent work overnight at half price"),
        ("pen", "Trim", "Shorter context, shorter answers, fewer steps"),
        ("gauge", "Budget", "Per team, alert at 80%, owner reviews monthly")], cols=5,
        tipt="Manage cost per outcome, not cost per token: dollars per ticket triaged against the staff minutes it saved.")
    shot(D, "Topic 3 · E · Token budget drill · 5 min", "Drill: Price One Agent for One Month", asset("v53", "token-calculator.png"), [
        ("Load Meridian", "80 requests a day, 4 steps, Haiku 5.5: about US$3 a month."),
        ("Switch the model", "The same work on Fable 5.2 costs about US$211. Which one passes your test?"),
        ("Pull the levers", "Raise caching, batch the reports, trim the steps."),
        ("Write the budget", "Put the monthly cap and alert into Guardrails & Judgement.")],
        label="activities/activity-03-…/token-cost-calculator.html",
        tipt="At Meridian's scale the model bill is small; integration, review time and change effort are the big costs. At 10,000 staff it is not.")

T3_QUIZ = [
    ("Your Best AI User Resigns and the Team's Results Drop. What Was Missing?",
     ["A more powerful model", "More prompt training", "The capability lived in a person, not in the process", "A bigger budget"], 2,
     "Write the playbook into the SOP and the system, give every agent an owner and a backup owner, and keep the capability register current."),
    ("Token Spend Doubled This Quarter. What Is Your First Move?",
     ["Ban AI until next year", "Route to the smallest model that passes the test, cache, batch and set team budgets", "Move everyone to the most powerful model", "Ignore it: AI is strategic"], 1,
     "Pull the five levers and manage cost per outcome. A blanket ban drives the work into shadow AI."),
    ("Staff Paste Client Data Into a Free Chatbot to Save Time. What Is It, and Your First Response?",
     ["Jailbreak: retrain the model", "Shadow AI: ask what they use, give them an easier approved tool and one page of rules", "Bias: audit outcomes by client group", "Prompt injection: block all email"], 1,
     "Shadow AI is helpful staff without a safe path. Banning drives it underground; a better approved tool brings it into the open. Check PDPA exposure with the DPO."),
]
