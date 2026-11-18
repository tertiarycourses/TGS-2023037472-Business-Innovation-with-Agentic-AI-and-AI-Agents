"""v41 content slides: a business pitch, highly visual, minimal words, big type.
One claim per slide (assertion-evidence). Facts carry their source on the slide.
Background reading informed the concepts; no book is cited on the slides."""
import os, io
import ccdeck as K
from ccdeck import (section, cards, rows, timeline, compare, table, image, statement, prompt, flow, hub, tip, header,
                    card, text, rich, icon, line, circle, box, picture, footer, ACC, ACC_D, TEAL, PLUM, OLIVE, CHAR,
                    PANEL, WHITE, INK, MUTED, SOFT, LIGHT, IVORY, SERIF, MONO, DIM)
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches
import slides_v23 as V
import data_bi as B

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", "courseware", "assets"))
def asset(*p): return os.path.join(A, *p)
BOOK = ""   # reference reading only: never cited on slides (user, 18 Nov 2026)

# ------------------------------------------------------------------ helpers
def src(D, s, label, url=None, y=6.86):
    if not label or label.lstrip().startswith(","): return None   # book references are not shown
    t = text(s, 0.6, y, 12.1, 0.24, "Source: " + label, 9.5, TEAL if url else (DIM if D.dark else MUTED), autofit=False)
    if url: t.click_action.hyperlink.address = url
    return t

def qr(s, url, x, y, d, dark=False):
    import qrcode
    img = qrcode.make(url, border=1); bio = io.BytesIO(); img.save(bio, format="PNG"); bio.seek(0)
    card(s, x - 0.08, y - 0.08, d + 0.16, d + 0.16, fill=WHITE, shadow=not dark)
    s.shapes.add_picture(bio, Inches(x), Inches(y), Inches(d), Inches(d))

def topic_open(D, C, tp):
    """Topic divider: big title, one-line pitch, the topic's LO in full, topics on the right."""
    s = D.new(dark=True)
    circle(s, -1.7, 5.2, 4.2, ACC)
    text(s, 0.9, 0.9, 7.6, 0.45, f"TOPIC {tp['num']}  ·  {C.LO_SHORT[tp['lo']].upper()}", 12.5, ACC, bold=True, autofit=False)
    text(s, 0.85, 1.45, 7.9, 2.0, tp["title"], 36, WHITE, bold=True, font=SERIF, cw=0.52, lh=1.04)
    text(s, 0.9, 3.55, 7.7, 0.9, tp["pitch"], 20, SOFT, font=SERIF, lh=1.1)
    card(s, 0.9, 4.75, 7.6, 1.85, fill=PANEL, shadow=False)
    lo = C.LEARNING_OUTCOMES[tp["lo"]]
    text(s, 1.15, 4.88, 7.1, 0.32, f"LEARNING OUTCOME {lo.split(':')[0][2:]}   ·   {tp['codes']}", 11.5, ACC, bold=True, autofit=False)
    text(s, 1.15, 5.22, 7.1, 1.3, lo.split(": ", 1)[1], 15, WHITE, minpt=11, lh=1.1)
    n = len(tp["items"]); rowh = 0.62; ph = 0.4 + n * rowh; py = max(0.55, (7.5 - ph) / 2 - 0.1)
    card(s, 8.95, py, 3.85, ph, fill=PANEL, shadow=False)
    for i, it in enumerate(tp["items"]):
        yy = py + 0.22 + i * rowh
        text(s, 9.15, yy, 0.45, 0.42, str(i + 1), 17, ACC, bold=True, font=SERIF, autofit=False)
        text(s, 9.6, yy, 3.05, rowh, it, 13, LIGHT, minpt=9.5)
    text(s, 6.4, 7.08, 6.4, 0.3, f"© Tertiary Infotech Academy Pte Ltd  ·  {D.code}", 9, K.FOOT, align="r", autofit=False)
    return s

def bignums(D, kicker, title, nums, sub=None, dark=False, source=None, url=None, tipt=None):
    """2-4 giant numbers, each with a 2-6 word label and an optional short line."""
    s = D.new(dark=dark); header(D, s, kicker, title, sub)
    n = len(nums); gap = 0.25; w = (12.1 - gap * (n - 1)) / n; top = 2.55 if sub else 2.2; h = 3.55
    for i, it in enumerate(nums):
        big, lab = it[0], it[1]; de = it[2] if len(it) > 2 else ""
        x = 0.6 + i * (w + gap); hi = (i == 0) != dark
        card(s, x, top, w, h, fill=(CHAR if not dark else PANEL) if hi else WHITE, shadow=not dark)
        text(s, x + 0.2, top + 0.25, w - 0.4, 1.45, big, 60 if n <= 3 else 50, ACC, bold=True, font=SERIF, align="c", anchor="m", minpt=28)
        text(s, x + 0.2, top + 1.8, w - 0.4, 0.75, lab, 20, WHITE if hi else INK, bold=True, font=SERIF, align="c", minpt=13)
        if de: text(s, x + 0.25, top + 2.55, w - 0.5, h - 2.65, de, 14, SOFT if hi else MUTED, align="c", minpt=10)
    if tipt: tip(D, s, tipt, y=6.35)
    if source: src(D, s, source, url)
    return s

def icons(D, kicker, title, items, sub=None, dark=False, source=None, url=None, tipt=None, cols=None, accent=ACC, arrows=False):
    """Big icon + 1-3 word label + one short line, vertically centred. items: (icon, label, line)."""
    s = D.new(dark=dark); header(D, s, kicker, title, sub)
    n = len(items); cols = cols or n; rows_ = (n + cols - 1) // cols
    gap = 0.38 if arrows else 0.25; w = (12.1 - gap * (cols - 1)) / cols; top = 2.5 if sub else 2.15
    bot = 6.2 if (tipt or source) else 6.7; h = (bot - top - gap * (rows_ - 1)) / rows_
    lab_pt = 26 if cols <= 4 else (21 if cols == 5 else 17.5); de_pt = 18 if cols <= 4 else (15.5 if cols == 5 else 14)
    for i, (ic, lab, de) in enumerate(items):
        r, c = divmod(i, cols); x = 0.6 + c * (w + gap); y = top + r * (h + gap)
        card(s, x, y, w, h, fill=PANEL if dark else WHITE, shadow=not dark)
        d = min(1.15, h * 0.28, w * 0.45); lh_ = 0.85 if rows_ == 1 else 0.5
        block = d + 0.1 + lh_ + (1.2 if rows_ == 1 else 0.75)
        y0 = y + max(0.12, (h - block) / 2)
        icon(s, ic, x + (w - d) / 2, y0, d, fill=accent)
        text(s, x + 0.12, y0 + d + 0.1, w - 0.24, lh_, lab, lab_pt if rows_ == 1 else 18, WHITE if dark else INK, bold=True, font=SERIF, align="c", anchor="m", minpt=12)
        dy = y0 + d + 0.1 + lh_
        text(s, x + 0.18, dy, w - 0.36, max(0.3, min(1.3, y + h - dy - 0.06)), de, de_pt if rows_ == 1 else 14, SOFT if dark else MUTED, align="c", minpt=10)
        if arrows and c < cols - 1:
            box(s, x + w + 0.06, y + h / 2 - 0.2, gap - 0.12, 0.4, fill=ACC, shape=MSO_SHAPE.CHEVRON)
    if tipt: tip(D, s, tipt, y=6.32)
    if source: src(D, s, source, url)
    return s

def eras(D, kicker, title, nodes, foot=None, dark=True, sub=None):
    """Big timeline: (label, year, line). Large circles and type."""
    s = D.new(dark=dark); header(D, s, kicker, title, sub)
    n = len(nodes); w = 12.1 / n; ly = 3.9; d = 1.55
    line(s, 0.6 + w / 2, ly, 12.7 - w / 2, ly, ACC, 3)
    for i, (lab, yr, de) in enumerate(nodes):
        cx = 0.6 + w * i + w / 2
        text(s, cx - w / 2, ly - d / 2 - 0.85, w, 0.75, lab, 24, WHITE if dark else INK, bold=True, font=SERIF, align="c", anchor="b", minpt=14)
        circle(s, cx - d / 2, ly - d / 2, d, ACC)
        text(s, cx - d / 2, ly - d / 2, d, d, yr, 22, WHITE, bold=True, font=SERIF, align="c", anchor="m", minpt=12)
        text(s, cx - w / 2 + 0.1, ly + d / 2 + 0.2, w - 0.2, 1.1, de, 18, SOFT if dark else MUTED, align="c", minpt=12)
    if foot: text(s, 0.6, 6.2, 12.1, 0.5, foot, 18, ACC, bold=True, font=SERIF, align="c", minpt=12)
    return s

def hubbig(D, kicker, title, center, spokes, foot=None):
    """Hub-and-spoke with big type: centre + 6 spokes (icon, title, line)."""
    import math
    s = D.new(); header(D, s, kicker, title)
    cx, cy = 6.67, 4.05; n = len(spokes); RX, RY = 4.3, 1.75
    pos = [(cx + RX * math.cos(-math.pi / 2 + 2 * math.pi * i / n), cy + RY * math.sin(-math.pi / 2 + 2 * math.pi * i / n)) for i in range(n)]
    for px, py in pos: line(s, cx, cy, px, py, SOFT, 2, dash=True)
    card(s, cx - 1.6, cy - 0.6, 3.2, 1.2, fill=ACC)
    text(s, cx - 1.6, cy - 0.6, 3.2, 1.2, center, 22, WHITE, bold=True, font=SERIF, align="c", anchor="m", minpt=14)
    for (px, py), (ic, t, d) in zip(pos, spokes):
        w, h = 3.3, 1.12
        card(s, px - w / 2, py - h / 2, w, h)
        icon(s, ic, px - w / 2 + 0.15, py - h / 2 + 0.2, 0.7, fill=TEAL)
        text(s, px - w / 2 + 0.95, py - h / 2 + 0.08, w - 1.05, 0.45, t, 18, INK, bold=True, font=SERIF, minpt=12)
        text(s, px - w / 2 + 0.95, py - h / 2 + 0.52, w - 1.05, 0.55, d, 13, MUTED, minpt=9.5)
    if foot: tip(D, s, foot, y=6.45)
    return s

def scen(D, n, title, hook, ex, img, tipt):
    """Collaboration scenario, big type: hook + three named examples left, illustration right."""
    s = D.new(); header(D, s, "Topic 1 · Five scenarios", f"Scenario {n} · {title}")
    picture(s, V.t1a(img.replace(".jpg", "_clean.jpg")), 8.35, 1.85, maxw=4.35, maxh=4.0)
    text(s, 8.35, 5.95, 4.35, 0.35, f"{n}. {title.upper()}", 12, TEAL, bold=True, align="c", minpt=9)
    text(s, 0.6, 1.85, 7.5, 1.3, hook, 24, INK, bold=True, font=SERIF, minpt=16, lh=1.08)
    for i, (ic, t, d) in enumerate(ex):
        y = 3.3 + i * 0.98; icon(s, ic, 0.6, y, 0.72, fill=TEAL)
        text(s, 1.5, y - 0.04, 6.6, 0.45, t, 19, INK, bold=True, font=SERIF, minpt=13)
        text(s, 1.5, y + 0.4, 6.6, 0.5, d, 15, MUTED, minpt=11)
    tip(D, s, tipt, y=6.35)
    return s

def big_statement(D, kicker, big, small=None, source=None, dark=True):
    s = statement(D, kicker, big, small, dark=dark)
    if source: src(D, s, source)
    return s

def full_image(D, kicker, title, path, line_=None, source=None, dark=False):
    s = D.new(dark=dark); header(D, s, kicker, title)
    bot = 6.3 if line_ else 6.8
    picture(s, path, 0.6, 1.75, maxw=12.1, maxh=bot - 1.8)
    if line_:
        rich(s, 0.6, 6.38, 12.1, 0.45, [[("▸  ", dict(color=ACC, bold=True, size=16)),
                                         (line_, dict(color=SOFT if dark else INK, size=16, font=SERIF, bold=True))]])
    if source: src(D, s, source)
    return s

def vs(D, kicker, title, left, right, sub=None, source=None):
    """Two big panels: (heading, icon, [2-3 short lines])."""
    s = D.new(); header(D, s, kicker, title, sub)
    top = 2.45 if sub else 2.0; bot = 6.55
    for j, (hd, ic, ls) in enumerate([left, right]):
        x = 0.6 + j * 6.15; dk = j == 1
        card(s, x, top, 5.95, bot - top, fill=CHAR if dk else WHITE)
        icon(s, ic, x + 0.35, top + 0.35, 0.9, fill=ACC if dk else TEAL)
        text(s, x + 1.45, top + 0.35, 4.3, 0.9, hd, 26, WHITE if dk else INK, bold=True, font=SERIF, anchor="m", minpt=15)
        text(s, x + 0.4, top + 1.55, 5.2, bot - top - 1.7, "\n".join(ls), 20, SOFT if dk else MUTED, minpt=12, lh=1.35)
    if source: src(D, s, source)
    return s

def ladder(D, kicker, title, steps, sub=None, source=None, foot=None):
    """Rising staircase: (label, line). Autonomy grows left to right."""
    s = D.new(); header(D, s, kicker, title, sub)
    n = len(steps); gap = 0.15; w = (12.1 - gap * (n - 1)) / n; base = 6.25
    for i, (lab, de) in enumerate(steps):
        h = 1.7 + i * 0.55; x = 0.6 + i * (w + gap); y = base - h
        card(s, x, y, w, h, fill=CHAR if i == n - 1 else (ACC if i == n - 2 else WHITE))
        dk = i >= n - 2
        text(s, x + 0.15, y + 0.15, w - 0.3, 0.85, lab, 21, WHITE if dk else INK, bold=True, font=SERIF, minpt=12)
        text(s, x + 0.15, y + 1.05, w - 0.3, h - 1.15, de, 17, LIGHT if dk else MUTED, minpt=10)
    line(s, 0.6, base + 0.2, 12.7, base + 0.2, ACC, 2.5, arrow=True)
    text(s, 9.0, base + 0.25, 3.7, 0.3, "more autonomy, more controls", 11, ACC, bold=True, align="r", autofit=False)
    if source: src(D, s, source)
    return s

def quadrant(D, kicker, title, q, xlab, ylab, sub=None, source=None):
    """2x2 map. q: [(title, line)] for TL, TR, BL, BR."""
    s = D.new(); header(D, s, kicker, title, sub)
    x0, y0, W, H = 1.5, 2.0, 11.0, 4.5; w, h = W / 2 - 0.08, H / 2 - 0.08
    fills = [WHITE, CHAR, ACC, WHITE]
    for i, (t, d) in enumerate(q):
        r, c = divmod(i, 2); x = x0 + c * (W / 2); y = y0 + r * (H / 2)
        f = fills[i]; dk = f in (CHAR, ACC)
        card(s, x, y, w, h, fill=f)
        text(s, x + 0.25, y + 0.2, w - 0.5, 0.6, t, 24, WHITE if dk else INK, bold=True, font=SERIF, minpt=14)
        text(s, x + 0.25, y + 0.85, w - 0.5, h - 0.95, d, 15, LIGHT if dk else MUTED, minpt=10)
    text(s, x0, y0 + H + 0.05, W, 0.3, xlab, 12, ACC, bold=True, align="c", autofit=False)
    tb = text(s, 0.0, y0 + H / 2 - 0.2, 1.4, 0.5, ylab, 11, ACC, bold=True, align="c", autofit=False)
    if source: src(D, s, source)
    return s

def board(D, kicker, canvas, title=None, sub=None, example=True):
    """Draw an activity board: every block with one worked-example note, all in ONE font size."""
    s = D.new(); header(D, s, kicker, title or f"Activity {canvas['num']} · {canvas['title']}", sub or canvas["pitch"])
    bl = canvas["blocks"]; top = 2.45; bot = 6.55; cells = []
    if canvas["layout"] == "bmc":
        cw = 12.1 / 5; th = (bot - top) * 0.68; bh = (bot - top) - th - 0.08
        ids = {b["id"]: b for b in bl}
        for bid, c, r, span in [("keyPartners", 0, 0, 2), ("keyActivities", 1, 0, 1), ("keyResources", 1, 1, 1), ("valueProps", 2, 0, 2),
                                ("customerRel", 3, 0, 1), ("channels", 3, 1, 1), ("customerSeg", 4, 0, 2)]:
            cells.append((ids[bid], 0.6 + c * cw, top + r * th / 2, cw - 0.06, th / 2 * span - 0.06, bid == "valueProps"))
        for k, bid in enumerate(("costStructure", "revenueStreams")):
            cells.append((ids[bid], 0.6 + k * 6.05, top + th + 0.02, 6.0, bh, False))
    else:
        n = len(bl); cols = 3; rows_ = (n + cols - 1) // cols; gap = 0.08
        cw = (12.1 - gap * (cols - 1)) / cols; ch = (bot - top - gap * (rows_ - 1)) / rows_
        for i, b in enumerate(bl):
            r, c = divmod(i, cols); cells.append((b, 0.6 + c * (cw + gap), top + r * (ch + gap), cw, ch, i == 0))
    def body(b):
        if not (example and b["example"]): return b["prompt"]
        t, d = b["example"][0]; lim = 78 if canvas["layout"] == "bmc" else 140
        if len(t) + len(d) > lim:  # keep the first WHOLE clause; never an ellipsis mid-sentence (QA v43)
            for sep in ("; ", ": ", ", "):
                if sep in d and len(t) + d.index(sep) <= lim: d = d[:d.index(sep)].rstrip(".") + "."; break
        return f"{t}: {d}"
    pt = min(K.fit(body(b), w - 0.34, h - (0.78 if example else 0.6), 18, 9, lh=1.05, cw=0.55) for b, x, y, w, h, hi in cells)
    tpt = min(K.fit(b["title"], w - 0.2, 0.34, 14, 8, cw=0.62) for b, x, y, w, h, hi in cells)
    for b, x, y, w, h, hi in cells:
        card(s, x, y, w, h, fill=CHAR if hi else WHITE, shadow=False, line=K.RULE)
        text(s, x + 0.1, y + 0.06, w - 0.2, 0.34, b["title"], tpt, ACC, bold=True, font=SERIF, autofit=False)
        card(s, x + 0.1, y + 0.42, w - 0.2, h - 0.52, fill=PANEL if hi else "FBEFD9", shadow=False)
        text(s, x + 0.17, y + 0.46, w - 0.34, h - 0.6, body(b), pt, LIGHT if hi else INK, autofit=False, lh=1.05)
    return s

def activity_intro(D, kicker, canvas, C):
    """Activity hand-out: what to do, discuss, link + QR to the online board, PP evidence."""
    s = D.new(dark=True)
    url = f"{B.BCM_URL}?activity={canvas['key']}"
    header(D, s, kicker, f"Activity {canvas['num']} · {canvas['title']}", canvas["pitch"])
    card(s, 0.6, 2.45, 7.6, 4.1, fill=PANEL, shadow=False)
    text(s, 0.9, 2.6, 7.0, 0.4, "DISCUSS IN YOUR TEAM", 13, ACC, bold=True, autofit=False)
    for i, q in enumerate(canvas["discuss"]):
        y = 3.1 + i * 1.08
        circle(s, 0.9, y + 0.05, 0.5, ACC)
        text(s, 0.9, y + 0.05, 0.5, 0.5, str(i + 1), 16, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
        text(s, 1.6, y, 6.4, 1.0, q, 17, WHITE, font=SERIF, minpt=11)
    card(s, 8.45, 2.45, 4.25, 4.1, fill=ACC_D, shadow=False)
    qr(s, url, 9.55, 2.7, 2.05, dark=True)
    text(s, 8.6, 4.95, 3.95, 0.4, "Join your group board", 17, WHITE, bold=True, font=SERIF, align="c", autofit=False)
    t = text(s, 8.6, 5.38, 3.95, 0.34, f"alfredang.github.io/bcm · Activity {canvas['num']}", 13, WHITE, bold=True, align="c", autofit=False)
    t.click_action.hyperlink.address = url
    text(s, 8.6, 5.75, 3.95, 0.75, f"No login · one board per group · {canvas['minutes']} min\nEach member: screenshot + own PP answers", 12.5, LIGHT, align="c", minpt=9.5)
    return s

def muse_board(D, kicker, cv):
    """Let Meta Muse draft the whole board; learners verify, edit and type it in."""
    s = D.new(); header(D, s, kicker, f"Let Meta Muse Draft Your Activity {cv['num']} Board", "Muse drafts every block in one go. You verify, cut, sharpen, then type it in.")
    top, bot = 2.4, 6.75
    card(s, 0.6, top, 8.6, bot - top, fill=K.CODEBG)
    for k, c in enumerate(("E06C5A", "E5B454", "7DB36B")): circle(s, 0.82 + k * 0.24, top + 0.18, 0.13, c)
    text(s, 1.6, top + 0.1, 7.4, 0.3, "PROMPT (short view)  ·  full template: board › Copy Muse prompt, or the prompts page", 11, DIM, autofit=False)
    shown = (f"Act as my innovation consultant. Our organisation: [your organisation in two sentences]. Draft our {cv['title']}:\n"
             + "\n".join(f"{i + 1}. {b['title']}" for i, b in enumerate(cv["blocks"]))
             + "\nTwo specific notes per block; mark guesses (assumption).\nReply as numbered blocks so I can paste it into our board.")
    text(s, 0.85, top + 0.5, 8.1, bot - top - 0.62, shown, 14, "F1EDE4", font=MONO, minpt=9, cw=0.68, lh=1.04)
    for i, (ic, t, d) in enumerate([("sparkles", "Muse drafts", "Every block, with sources"), ("eyecheck", "You verify", "Strike guesses and generic lines"),
                                     ("pen", "You own it", "Type the best notes into the board")]):
        y = top + i * 1.45; icon(s, ic, 9.5, y + 0.05, 0.75)
        text(s, 10.4, y + 0.02, 2.4, 0.45, t, 19, INK, bold=True, font=SERIF, minpt=12)
        text(s, 10.4, y + 0.5, 2.4, 0.85, d, 14, MUTED, minpt=10)
    return s

STUDIO_ICON = {"join": "users", "muse": "wand", "refine": "pen", "capture": "camera"}
def muse_get(D):
    """Activity 1, Step 1: install Meta Muse on the phone, or sign up on the web; three QR codes."""
    s = D.new(); header(D, s, "Topic 1 · Activity 1 · Step 1", "Step 1 · Get Meta Muse: Phone App or Website",
                        "Either works for every activity. Sign in with your Facebook (Meta) account.")
    how = ["Search 'Muse from Meta' or scan · Get · open · sign in", "Search 'Muse from Meta' or scan · Install · open · sign in",
           "Go to muse.ai · Log in or Sign up · continue with Facebook"]
    for i, ((label, url), h_) in enumerate(zip(B.MUSE_LINKS, how)):
        x = 0.6 + i * 4.1; card(s, x, 2.35, 3.9, 4.0, fill=CHAR if i == 2 else WHITE)
        qr(s, url, x + 0.95, 2.6, 2.0, dark=i == 2)
        t = text(s, x + 0.15, 4.8, 3.6, 0.5, label, 22, WHITE if i == 2 else INK, bold=True, font=SERIF, align="c", minpt=14)
        t.click_action.hyperlink.address = url
        text(s, x + 0.2, 5.35, 3.5, 0.9, h_, 15, SOFT if i == 2 else MUTED, align="c", minpt=11)
    tip(D, s, "Then Settings › General › Usage › Redeem invite code: H1KWDZ (within 48 hours). Allow notifications on your phone.", y=6.5)
    return s

def concept(D, term, topic):
    """Key concept: the term, a one-sentence definition, a real example."""
    c = B.AI_NATIVE_BY[term]
    s = D.new(); header(D, s, f"Topic {topic} · Key concept", c["term"], c["gist"])
    icon(s, c["icon"], 0.6, 2.45, 1.5)
    card(s, 2.4, 2.35, 10.3, 2.55)
    text(s, 2.7, 2.5, 9.8, 2.3, c["definition"], 22, INK, font=SERIF, minpt=14, lh=1.12)
    card(s, 2.4, 5.1, 10.3, 1.45, fill=CHAR)
    rich(s, 2.7, 5.22, 9.8, 1.25, [[("IN PRACTICE   ", dict(color=ACC, bold=True, size=14)), (c["example"], dict(color=WHITE, size=19, font=SERIF))]], anchor="m")
    return s

def framework(D, kicker, name, title, rows, sub, dark=False, tipt=None):
    """Five-step plan (numbers) / SCALE (letters): five big marks, each with its move and what you decide."""
    s = D.new(dark=dark); header(D, s, kicker, title, sub)
    w = 12.1 / 5
    for i, (letter, word, line, ic) in enumerate(rows):
        x = 0.6 + i * w
        card(s, x + 0.06, 2.45, w - 0.12, 3.9, fill=CHAR if i % 2 else WHITE, shadow=not dark)
        text(s, x + 0.06, 2.55, w - 0.12, 1.3, letter, 66, ACC, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
        text(s, x + 0.2, 3.9, w - 0.4, 0.7, word, 21, WHITE if i % 2 else INK, bold=True, font=SERIF, align="c", minpt=13)
        text(s, x + 0.22, 4.65, w - 0.44, 1.6, line, 14.5, SOFT if i % 2 else MUTED, align="c", minpt=10)
    if tipt: tip(D, s, tipt, y=6.5)
    return s

def lab_overview(D, L):
    """Lab N at a glance: every step, Meta Muse steps then the group-board steps."""
    cv = B.CANVAS[L["canvas"]]
    items = [(STUDIO_ICON.get(st.get("studio"), "sparkles"), f"Step {i + 1}", st["title"]) for i, st in enumerate(L["steps"])]
    icons(D, f"Topic {L['topic']} · Activity {cv['num']}", f"Activity {L['n']} · {L['title']}", items,
          sub=L["goal"], cols=4, arrows=False, tipt=f"{L['minutes']} min · Meta Muse + your group board · {cv['evidence']}")

def _short(t, n=120):
    """Subtitle: the first whole sentence or clause that fits. Never cut mid-sentence with an ellipsis (QA v43)."""
    if len(t) <= n: return t
    cut = max(t.rfind(". ", 0, n), t.rfind(": ", 0, n), t.rfind("; ", 0, n))
    return t[:cut].rstrip(" .:;") + "." if cut > 40 else t

def step_slide(D, L, i, title=None):
    """One Meta Muse prompt step, big type: prompt panel left, what to do and what to check right."""
    st = L["steps"][i]
    s = D.new(); header(D, s, f"Topic {L['topic']} · Activity {L['n']} · Step {i + 1} of {len(L['steps'])}", title or f"Step {i + 1} · {st['title']}", _short(st["body"][0]))
    top, bot = 2.4, 6.75
    card(s, 0.6, top, 8.0, bot - top, fill=K.CODEBG)
    for k, c in enumerate(("E06C5A", "E5B454", "7DB36B")): circle(s, 0.82 + k * 0.24, top + 0.18, 0.13, c)
    text(s, 1.6, top + 0.1, 6.8, 0.3, "PROMPT TEMPLATE  ·  fill the [blanks] on alfredang.github.io/bcm/prompts.html  ·  paste into Meta Muse", 10.5, DIM, autofit=False)
    text(s, 0.85, top + 0.5, 7.5, bot - top - 0.62, st["prompt"], 18, "F1EDE4", font=MONO, minpt=9.5, cw=0.66, lh=1.08)
    side = [("check", "You should see", st.get("check", "")), ("kanban", "Then", "Keep the answer: it feeds your group board in this activity.")]
    rh = (bot - top) / len(side)
    for j, (ic, t, d) in enumerate(side):
        y = top + j * rh; icon(s, ic, 8.9, y + 0.05, 0.7)
        text(s, 9.75, y + 0.05, 3.0, 0.5, t, 20, INK, bold=True, font=SERIF, minpt=13)
        text(s, 9.75, y + 0.6, 3.0, rh - 0.7, d, 16, MUTED, minpt=10.5)
    return s

def board_steps(D, L):
    """How to use the Activity Studio in this lab: join, Muse drafts, refine, capture."""
    cv = B.CANVAS[L["canvas"]]; url = f"{B.BCM_URL}?activity={cv['key']}"
    SHORT = {"join": "Board ID or QR + your name", "muse": "Copy prompt, paste Muse's reply", "refine": "Verify, edit, type it in", "capture": "PNG or PDF for the PP"}
    LABEL = {"join": "Join the group board", "muse": "Muse drafts the board", "refine": "Refine together", "capture": "Capture evidence"}
    items = [(STUDIO_ICON[st["studio"]], LABEL[st["studio"]], SHORT[st["studio"]]) for st in L["steps"] if st.get("studio")]
    s = icons(D, f"Topic {L['topic']} · Activity {L['n']} · Activity Studio", f"On Your Group Board: {cv['title']}", items, arrows=True,
              sub=f"{url.replace('https://', '')}  ·  one board per group, no login  ·  each member answers the PP individually")
    return s

def topic1(D, C, mark):
    tp = C.TOPICS[0]; K1 = "Topic 1 · Identify and evaluate"
    mark("t1"); topic_open(D, C, tp)
    meridian_scene(D, K1 + " · Meridian scenario", "Meet Meridian: 80 Requests a Day, Every One Re-Keyed by Hand",
        "A fictitious Singapore firm you will follow through all three activities. Watch what it does; then do it for your own business.", [
        ("building", "Meridian Services Pte Ltd", "140 staff keep 30 commercial buildings running across Singapore."),
        ("inbox", "The pain", "80 emails and WhatsApps a day. Coordinators spend 38% of their time re-keying them into tickets."),
        ("clock", "The cost", "18 minutes per request; an urgent leak at 2 am waits until morning."),
        ("rocket", "The new business", "Meridian Assist: an always-on agent it runs in-house first, then sells.")],
        "Where on our business model would AI agents pay off first, and which idea do we park?", "Meridian's Topic 1 question")
    big_statement(D, K1, "AI stopped talking.\nIt started working.", "Agents read your inbox, run your workflows and wait for your yes.")
    # --- history
    eras(D, "Topic 1 · History of AI", "Seventy Years: From Rules to Action", [
        ("Rules", "1950s–80s", "Expert systems"), ("Learning", "1990s–2010s", "Learn from examples"),
        ("Language", "2017–2023", "Transformers, ChatGPT"), ("Action", "2024 →", "Agents use tools")],
        foot="Each era still runs underneath the next.")
    ladder(D, "Topic 1 · History of AI", "The Agent Stairway: From Answers to Results", [
        ("Chatbot", "You ask, it answers. It cannot act."), ("Task bot", "One clear job, precise instructions."),
        ("Copilot", "Suggests; you steer and approve every step."), ("Autonomous agent", "Goal in, result out, while you sleep.")],
        sub="The big jump is copilot → agent: from prompt-and-response to delegating a goal.")
    eras(D, "Topic 1 · History of AI", "2023 → 2026: Four Engineering Lenses", [
        ("Prompts", "2023", "Say it well"), ("Context", "2024", "Feed the right facts"),
        ("Harness", "2025", "Wire tools, state, checks"), ("Agents", "2026", "Delegate outcomes")],
        foot="Prompt, context and harness engineering, then AI agents: emphasis markers, not invention dates.")
    # --- agentic AI vs AI agent
    vs(D, "Topic 1 · Agentic AI vs AI agent", "Agentic AI Is the System. An Agent Does the Work.",
       ("Agentic AI", "network", ["The whole goal-driven system", "Plans → acts → checks → repeats", "Can run one agent or a team"]),
       ("AI agent", "robot", ["One worker with one job", "Model + tools + memory + rules", "Meta Muse · OpenAI Dots · Hermes"]))
    # --- Singapore government news
    mark("t1sg")
    bignums(D, "Topic 1 · Singapore government news", "Singapore Is Betting the Country on Agents", [
        ("1st", "agentic AI governance framework", "IMDA, launched at Davos, 22 Jan 2026"),
        ("24", "Champions of AI", "DBS, SIA, PSA, ST Engineering and more"),
        ("280+", "SMEs piloted agentic AI", "Marketing, sales and customer service")],
        source="IMDA (Jan; v1.5 20 May 2026) · Enterprise Singapore media release, 27 Oct 2026 · The Straits Times",
        url="https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence")
    sg_health(D)
    # --- always-on agents
    mark("t1always")
    s = D.new(); header(D, s, "Topic 1 · Always-on AI agents", "Always-On Agents Work While You Sleep",
                        "Meta Muse keeps watch on your inbox, calendar and goals, then asks before it acts.")
    picture(s, asset("ainative", "muse-productivity.png"), 0.7, 2.3, maxw=2.1, maxh=4.4)
    for i, (ic, t, d) in enumerate([("eye", "Keeps watch", "Ranks what matters as mail arrives"),
                                     ("calendar", "Nudges you", "Before the moment, not after"),
                                     ("shield", "Asks first", "Every send and purchase waits for you"),
                                     ("wand", "Builds for you", "A Space: a small app from one prompt")]):
        r, c = divmod(i, 2); x = 3.3 + c * 4.75; y = 2.35 + r * 2.15
        card(s, x, y, 4.55, 1.95); icon(s, ic, x + 0.3, y + 0.35, 0.9)
        text(s, x + 1.4, y + 0.3, 3.0, 0.55, t, 23, INK, bold=True, font=SERIF)
        text(s, x + 1.4, y + 0.9, 3.0, 0.95, d, 15, MUTED, minpt=11)
    src(D, s, "Meta Muse app (Singapore, Nov 2026) · Meta Newsroom: Muse in Singapore, 27 Oct 2026", V.NEWS)
    agent_evolution(D)
    big_five(D)
    for a_ in APPS: app_page(D, a_)
    # --- five collaboration scenarios
    mark("t1scen")
    icons(D, "Topic 1 · Five scenarios", "Five Ways Humans and Agents Team Up", [
        ("user", "1 : 1", "You and your agent"), ("users", "Many : 1", "One agent serves everyone"),
        ("robot", "1 : Many", "You run an AI team"), ("building", "Many : Many", "The whole firm runs on agents"),
        ("handshake", "Firm : Firm", "Your agent meets theirs")], cols=5)
    SC = [
        (1, "One Human, One AI Agent", "Your chief of staff that never clocks off",
         "Your agent reads the inbox overnight. A brief, a clash and a draft are waiting at 7 am.",
         [("sparkles", "Always-on assistants", "Meta Muse, OpenAI Dots, Claude Duet."), ("mail", "The morning brief", "Inbox + calendar in one page, every morning."),
          ("calendar", "A guard on your diary", "Flags the double-booking before you say yes.")], "pattern1.jpg", "Personal assistant",
         "It drafts. You commit."),
        (2, "Multiple Humans, One AI Agent", "One agent answers every customer at once",
         "One front-line agent clears the routine questions at 2 am and hands the hard ones to a person.",
         [("users", "Klarna's assistant", "2.3M chats in month one: two-thirds of its service chats (Feb 2024)."),
          ("chat", "WhatsApp Business bots", "One number, every customer, any hour."), ("inbox", "Helpdesk in the team chat", "Staff ask it too.")],
         "pattern2.jpg", "Customer service", "Always give the bot an exit to a human."),
        (3, "One Human, Multiple AI Agents", "One founder, a whole AI staff",
         "Specialist agents work in parallel. You approve the hand-offs.",
         [("kanban", "Research → draft → review", "An agent per step, you at the gates."), ("megaphone", "A marketing team of agents", "Writer, designer, scheduler."),
          ("building", "The one-person company", "You are the board.")], "pattern3.jpg", "One-person company", "One person still means oversight."),
        (4, "Multiple Humans, Multiple AI Agents", "When the whole organisation runs on agents",
         "Everyone builds and runs agents toward shared goals. Agents become part of the workforce.",
         [("hospital", "Singapore public healthcare", "80,000+ staff, 12,000+ AgentSea agents."), ("flask", "Stanford's virtual biotech", "37,000 AI scientist agents."),
          ("org", "DRIs + agent teams", "Topic 3: how to run it.")], "pattern4.jpg", None, "Scale needs owners, permissions and audit trails."),
        (5, "Inter-Company Collaboration", "Your agent negotiates with their agent",
         "A buyer's agent asks for quotes; a supplier's agent checks stock and replies. People sign off.",
         [("cart", "Agents meet businesses", "Muse with Grab and Singapore Airlines as they roll out."), ("mail", "Agents with their own inbox", "Grok Bot @mail.grokbot.com."),
          ("phone", "Agents with identity", "Manus Cue: own email, phone, wallet.")], "pattern5.jpg", None, "Treat the other firm's agent as untrusted."),
    ]
    for n, t, p, hook, ex, img, use, tipt in SC:
        scen(D, n, t, hook, ex, img, tipt)
    # --- hands-on 1-5 (Muse)
    mark("labs1")
    L1 = B.LAB[1]
    lab_overview(D, L1)
    muse_get(D)
    V.muse_invite(D, "Topic 1 · Activity 1 · Step 1 (continued)")
    step_slide(D, L1, 0, title="Step 1 · Say Hello: Your First Prompt to Meta Muse")
    for i in (1, 2): step_slide(D, L1, i)
    # --- five capability gaps
    mark("t1gaps")
    big_statement(D, "Topic 1 · Why AI projects stall", "A genius new hire.\nStuck on day one.",
                  "Plug a model in straight out of the box and five gaps appear at once.")
    icons(D, "Topic 1 · Five capability gaps", "Five Gaps Between a Smart Model and Useful Work", [
        ("lock", "Private data", "Your contracts and records are blank to it"),
        ("book", "Your language", "'Active customer' means what, here?"),
        ("clock", "Live context", "Blind to what changed a second ago"),
        ("hand", "Can't act", "No permission inside your systems"),
        ("shield", "No guardrails", "No controls, checks or audit trail")], cols=5,
        tipt="Every opportunity you pick must close these five gaps. Topic 2 shows how.")
    # --- value and evaluation
    icons(D, "Topic 1 · Where value comes from", "Four Levers. Pick the One Your Board Tracks.", [
        ("trend", "Revenue", "Sell more, faster"), ("coins", "Cost", "Fewer hours per outcome"),
        ("shield", "Risk", "Fewer errors, better compliance"), ("smile", "Experience", "Faster answers, happier staff")], cols=4)
    s = D.new(); header(D, s, "Topic 1 · Evaluate the opportunity", "Score It Before You Build It",
                        "Viable = valuable × feasible × data-ready, and it moves an objective you already own.")
    for i, (w, lab) in enumerate([("Value", "moves a KPI"), ("Feasibility", "can we build it?"), ("Data", "clean, permitted?"), ("Fit", "serves our goals?")]):
        x = 0.6 + i * 3.1; card(s, x, 2.6, 2.85, 2.2, fill=CHAR if i == 3 else WHITE)
        text(s, x, 2.75, 2.85, 0.95, w, 34, ACC, bold=True, font=SERIF, align="c", anchor="m", minpt=20)
        text(s, x, 3.75, 2.85, 0.6, lab, 18, WHITE if i == 3 else INK, font=SERIF, align="c")
        text(s, x, 4.3, 2.85, 0.4, "pass / fail gate" if i == 3 else "score 1-5", 12, SOFT if i == 3 else MUTED, align="c", autofit=False)
        if i < 3: text(s, x + 2.82, 3.25, 0.3, 0.6, "×" if i < 2 else "→", 30, ACC, bold=True, align="c", autofit=False)
    rich(s, 0.6, 5.2, 12.1, 1.2, [[("Example:  ", dict(color=ACC, bold=True, size=20, font=SERIF)),
                                   ("triage agent 5 × 4 × 4 = 80  ·  report agent 75  ·  fault predictor 24 → park it", dict(color=INK, size=20, font=SERIF))]])
    tip(D, s, "Set a veto: any score of 1 on data or risk stops the idea, whatever the total.", y=6.3)
    # --- activity 1
    mark("act1")
    c1 = B.CANVAS["opportunity"]
    activity_intro(D, "Topic 1 · Activity 1", c1, C)
    step_slide(D, L1, 3)
    board_steps(D, L1)
    muse_board(D, "Topic 1 · Activity 1 · Step 6 · Meta Muse", c1)
    meridian_shot(D, "Topic 1 · Activity 1 · Meridian's demo board", "Meridian's Canvas: All Nine Blocks, Filled In",
        "A finished Activity 1 board for the fictitious Meridian. Open it on your phone and compare it with yours.", "meridian-bmc.png", 1, [
        ("Value first.", "Same-day answers, 24/7: the block every other block serves."),
        ("Scored, not guessed.", "Triage 80, reports 75, predictor 24: park it."),
        ("A human stays.", "Complaints, refunds and premium clients keep a person.")])
    board(D, "Topic 1 · Activity 1 · Meridian's demo board", c1, "Meridian's Canvas, Block by Block",
          "The first note of each block, readable. The live board holds three per block.", example=True)
    board(D, "Topic 1 · Activity 1 · Your board", c1, "Your Canvas: The Question Each Block Answers",
          "Answer every block for your own organisation. Screenshot your group board for PP Task 1.", example=False)
    big_statement(D, "Next · Topic 2 · Action Plan to Get Started", "You found the opportunity.\nNow plan how to get started.",
                  "Give the agents what they lack, your data, your language and safe access, then write the 90-day plan.")
    mark("t1end")


# ------------------------------------------------------------------ v45: slides copied from C690 Human-AI Collaboration
# (owner request, 18 Nov 2026): Singapore healthcare 12,000+ agents, OpenClaw -> self-hosted -> hosted agents, one page per
# always-on agent (Meta Muse, OpenAI Dots, Claude Duet, Grok Bot) with its YouTube Short. Facts and sources as in C690 v2.0.
def links_row(s, items, y=6.86):
    """Several clickable source links on one line: [(label, url)]."""
    n = len(items); w = 12.1 / max(n, 1)
    for i, (lab, url) in enumerate(items):
        t = text(s, 0.6 + i * w, y, w - 0.1, 0.24, lab + " · click", 9.5, TEAL, autofit=False)
        t.click_action.hyperlink.address = url

def sg_health(D):
    s = D.new(); header(D, s, "Topic 1 · Singapore in the news", "Singapore Healthcare: 12,000+ AI Agents in Three Months",
                        "AgentSea, Synapxe's agentic AI platform built with AWS, lets public healthcare staff build their own agents in plain language.")
    for i, (big, lab, d) in enumerate([("12,000+", "AI agents created", "By healthcare professionals, from the end-May 2026 launch to 24 Aug 2026."),
                                       ("80,000+", "healthcare professionals", "Everyone in Singapore's public health sector can create agents, with little or no coding."),
                                       ("300+", "agents shared", "Published for colleagues to reuse and adapt for their own work.")]):
        x = 0.6 + i * 4.1; dk = i == 0
        card(s, x, 2.3, 3.9, 1.95, fill=CHAR if dk else WHITE)
        text(s, x + 0.25, 2.4, 3.4, 0.8, big, 36, ACC, bold=True, font=SERIF, autofit=False)
        text(s, x + 0.25, 3.15, 3.4, 0.35, lab, 15, WHITE if dk else INK, bold=True, autofit=False)
        text(s, x + 0.25, 3.5, 3.4, 0.7, d, 11.5, SOFT if dk else MUTED, minpt=9)
    for i, (ic, t, d) in enumerate([("hospital", "Cardiologist, National Heart Centre", "An agent summarises patient histories before clinic, halving 40+ minutes of daily pre-clerking. He still verifies and makes the clinical assessment."),
                                    ("calendar", "KK Women's and Children's Hospital", "An agent generates daily staff rosters, cutting manual data entry and transcription errors."),
                                    ("shield", "Guardrails and governance", "Rejects requests for card or ID numbers; MOH's updated AI in Healthcare Guidelines keep professional judgment with people.")]):
        x = 0.6 + i * 4.1
        card(s, x, 4.45, 3.9, 1.8); icon(s, ic, x + 0.25, 4.6, 0.45)
        text(s, x + 0.82, 4.6, 2.95, 0.45, t, 13, INK, bold=True, font=SERIF, minpt=10)
        text(s, x + 0.25, 5.15, 3.45, 1.05, d, 11.5, MUTED, minpt=9)
    tip(D, s, "Agents prepare the work; clinicians verify and decide. The same pattern works in your business.", y=6.35)
    links_row(s, [("The Straits Times, 24 Aug 2026: New platform to create AI agents available to all public healthcare professionals",
                   "https://www.straitstimes.com/tech/new-platform-to-create-ai-agents-available-to-all-public-healthcare-professionals")])

def agent_evolution(D):
    s = D.new(dark=True); header(D, s, "Topic 1 · Deployment evolution", "OpenClaw → Self-Hosted Agents → Hosted Personal Agents",
                                 "From a harness you run yourself to an always-on agent someone else hosts for you.")
    for i, (top, mid, d) in enumerate([("OpenClaw", "Configurable harness", "Local or server tools and channels you wire up yourself."),
                                       ("Self-hosted agents", "Desktop + skills", "On your own machine, e.g. Hermes Agent: local workflow, memory and reusable skills."),
                                       ("Hosted agents", "Managed cloud", "Meta Muse, OpenAI Dots, Claude Duet, Grok Bot and Manus Cue."),
                                       ("Your choice", "Work + control", "Access, oversight, cost and data boundaries decide the fit.")]):
        x = 0.6 + i * 3.05
        text(s, x, 2.45, 2.85, 0.4, top, 17, ACC, bold=True, font=SERIF, align="c", autofit=False)
        circle(s, x + 0.43, 2.95, 2.0, ACC)
        text(s, x + 0.43, 3.45, 2.0, 1.0, mid, 17, WHITE, bold=True, font=SERIF, align="c", anchor="m", minpt=12)
        text(s, x, 5.1, 2.85, 0.9, d, 13, SOFT, align="c", minpt=10)
        if i < 3: text(s, x + 2.6, 3.65, 0.5, 0.6, "→", 28, ACC, bold=True, align="c", autofit=False)
    tip(D, s, "A progression in deployment choices, not a product lineage: pick the level of control your business needs.", y=6.35)

APPS = [
 dict(key="muse", kicker="Topic 1 · Always-on agent · Meta Muse", title="Meta Muse: What It Does and How to Set It Up",
      sub="Meta · in Singapore since 27 Oct 2026 · core use free, optional subscriptions · used in every activity of this course",
      can=[("sparkles", "Does the work", "Manages email, coordinates schedules and turns long-term goals into action plans."),
           ("plug", "Connected apps", "Gmail, Google Calendar and Instagram; Grab, Shopee and Singapore Airlines are rolling out."),
           ("shield", "Asks before acting", "Checks with you before sending an email or making a purchase; retrieve-only connectors."),
           ("lock", "Secure and mostly free", "Muse Secure VM keeps passwords and payment methods out of the agent's view.")],
      steps=[("Install", "Muse from Meta (iOS / Android) or muse.ai."), ("Sign in", "Complete onboarding; link your Meta accounts."),
             ("Connect Gmail", "Settings → Connectors → Connect beside Gmail → Continue."), ("Authorise", "Finish the Google login; repeat for Google Calendar."),
             ("Approvals", "Keep retrieve-only where offered; approve every send or invite.")],
      tip="Shortcut: ask \u201cConnect my Gmail\u201d. Partner features roll out progressively; no bookings or purchases in class.",
      video="https://www.youtube.com/shorts/zuAAjV5dNMA",
      links=[("Meta Newsroom: Muse in SG", "https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/"),
             ("Meta Help: Connectors", "https://www.meta.com/help/superintelligence/1687253048996149/"),
             ("Muse iOS (SG)", "https://apps.apple.com/sg/app/muse-from-meta/id6760173601"),
             ("Muse Android (SG)", "https://play.google.com/store/apps/details?gl=sg&id=com.facebook.aura")]),
 dict(key="dots", kicker="Topic 1 · Always-on agent · OpenAI Dots", title="OpenAI Dots: What It Does and How to Set It Up",
      sub="OpenAI · rolling out to ChatGPT Pro and Business Premium · check whether your plan has it",
      can=[("target", "Ongoing responsibilities", "Give one dot several long-running jobs instead of one-off chats."),
           ("server", "Its own cloud computer", "Works in its own browser; optionally on your computer while the ChatGPT app is open."),
           ("plug", "Plugins and channels", "Email, calendar and files through plugins; Slack and other contact methods for messages."),
           ("clock", "Delegates and schedules", "Hands parts to ChatGPT Work or Codex; fixed schedules, event triggers, an Activity view.")],
      steps=[("Open dots", "ChatGPT app or desktop browser; not mobile web."), ("Create a dot", "Follow the intro; name it and pick its look."),
             ("Plugins", "Connect email, calendar and files plugins; authorise each one."), ("Channels", "Optional: profile → Add a contact method such as Slack."),
             ("Assign work", "Describe an ongoing responsibility, its sources and your decisions.")],
      tip="A messaging channel does not grant inbox access. Ending a chat does not stop assigned work: check Activity.",
      video="https://www.youtube.com/shorts/gdHwOn2kvT8",
      links=[("ChatGPT Learn: Get started with your dot", "https://learn.chatgpt.com/docs/dots/getting-started")]),
 dict(key="duet", kicker="Topic 1 · Always-on agent · Claude Duet", title="Claude Duet: What It Does and How to Set It Up",
      sub="Anthropic research preview · 21 Oct 2026 · US Pro/Max via waitlist · reference route",
      can=[("calendar", "Morning brief, then watching", "A daily brief, then checks every few hours; messages you only when something needs you."),
           ("server", "Works while you are away", "Its own virtual machine and browser: meetings, dashboards, forecasts and prototypes."),
           ("plug", "6,000+ connectors", "Gmail, Slack, QuickBooks, Stripe, HubSpot, Docusign, Canva, Shopify and more."),
           ("shield", "You approve actions", "Shows exactly what it will send, pay, sign or delete and waits; some actions stay off-limits.")],
      steps=[("Get access", "Pro or Max plan; join the Claude Duet waitlist on claude.com."), ("Install", "Open the Claude Duet app (iOS / Android) or claude.ai once invited."),
             ("Carry context", "Memory, skills and apps carry over from your Claude account."), ("Connect apps", "Add Gmail, Calendar, Slack or others from the Claude Marketplace."),
             ("Set the brief", "Tell it what to watch and how often; approve every send or payment.")],
      tip="Reference route only. Background checks use your plan limits; some actions stay off-limits even with approval.",
      video="https://www.youtube.com/shorts/7G5hOD6oF4M",
      links=[("Anthropic: Introducing Claude Duet", "https://claude.com/resources/articles/claude-duet")]),
 dict(key="grok", kicker="Topic 1 · Always-on agent · Grok Bot", title="Grok Bot: What It Does and How to Set It Up",
      sub="xAI · Grok Bot documentation, updated 28 Oct 2026 · check your plan's access",
      can=[("server", "Persistent cloud computer", "Browser, command line and files; keeps working while your laptop is closed."),
           ("robot", "Several bots, one computer", "Each bot has its own screen; sessions, files and logins are shared across your bots."),
           ("mail", "Apps, MCP and its own email", "Gmail, Calendar, Sheets, Slack and Notion; mail to its @mail.grokbot.com address starts routines."),
           ("eye", "Watch, take over, review", "Live computer view; take control for a sign-in or CAPTCHA; Auto Review gates sends.")],
      steps=[("Install", "Start at x.ai/bot; get the desktop or mobile app and sign in."), ("Create a bot", "Sidebar + → Create a Bot → name it → Create."),
             ("Connect apps", "Open Connect apps (mobile: avatar → Connect apps); add Gmail."), ("Authorise", "Finish the Google login; repeat for Google Calendar."),
             ("Verify", "Both show under Installed; \u201cAdded\u201d is not signed in, so fix \u201cNeeds auth\u201d.")],
      tip="All bots on one account share a cloud computer and logins. The bot's @mail.grokbot.com inbox is not your Gmail.",
      video="https://www.youtube.com/shorts/Gm_dlNAVOGI",
      links=[("xAI docs: Grok Bot computer and apps", "https://docs.x.ai/grok-bot/computer-and-apps")]),
]


BIG5 = [  # C690 v2.0 slide 33 (models checked 31 Oct, pricing 1 Nov 2026)
 ("muse", "Meta Muse", "Meta", ("Muse Spark", "Muse Wonder coming soon, subscribers first"), "Personal email, schedules and goals; errands with Grab, Shopee and SIA as partners roll out", ("Single agent only", "one assistant works for you"), ("Free", "core use, Singapore")),
 ("dots", "OpenAI Dots", "OpenAI", ("GPT-6 Astra", "its own cloud computer, 24/7"), "Ongoing goals inside ChatGPT, Slack and Teams; hands code to Codex", ("Single agent only", "one agent per goal"), ("Paid", "ChatGPT Pro · Business Premium")),
 ("grok", "Grok Bot", "xAI", ("Grok 4.6 → 4.7", "4.7 is trained for the Grok Bot harness"), "A team of named bots (Research, Sales, Ops) on one shared cloud computer", ("Multi-agent", "named bots work as a team"), ("Paid", "Premium from US$30/mo")),
 ("duet", "Claude Duet", "Anthropic", ("Claude Opus 5.5", "chosen for judgement: what needs you"), "A morning brief, business inbox, invoices and follow-ups; asks before it sends, pays or signs", ("Unknown", "Anthropic has not said"), ("Paid", "US Pro/Max · waitlist")),
 ("cue", "Manus Cue", "Manus", ("Manus 2.0 harness", "model not published by Manus"), "Agents with their own email, phone and wallet: calls, bookings, capped payments", ("Multi-agent", "agents share a group chat and a goal"), ("Free for now", "early access · invite code")),
]

def big_five(D):
    s = D.new(); header(D, s, "Topic 1 · The big five always-on agents", "Same Always-On Idea, Five Different Brains",
                        "The model decides how it thinks; the use case decides whether it fits your job. Pick by the job, then check who can get it.")
    w = 12.1 / 5
    for i, (k, name, vendor, model, use, multi, price) in enumerate(BIG5):
        x = 0.6 + i * w; cw = w - 0.12
        card(s, x, 2.25, cw, 4.35)
        picture(s, asset("apps", f"{k}-logo.png"), x + 0.15, 2.38, maxw=0.5, maxh=0.5, frame=False)
        text(s, x + 0.75, 2.36, cw - 0.85, 0.32, name, 14, INK, bold=True, font=SERIF, autofit=False)
        text(s, x + 0.75, 2.66, cw - 0.85, 0.26, vendor, 10.5, MUTED, autofit=False)
        y = 3.05
        for lab, big_, small in (("MODEL INSIDE", model[0], model[1]), ("USE IT FOR", use, None), ("SINGLE OR MULTI-AGENT", multi[0], multi[1]), ("PRICING", price[0], price[1])):
            text(s, x + 0.15, y, cw - 0.3, 0.2, lab, 8.5, ACC, bold=True, autofit=False)
            if small is None:
                text(s, x + 0.15, y + 0.22, cw - 0.3, 0.72, big_, 10.5, INK, minpt=8.5); y += 1.0
            else:
                text(s, x + 0.15, y + 0.21, cw - 0.3, 0.26, big_, 12, INK, bold=True, minpt=9)
                text(s, x + 0.15, y + 0.47, cw - 0.3, 0.3, small, 9.5, MUTED, minpt=8); y += 0.86
    t = text(s, 0.6, 6.76, 12.1, 0.24, "Models checked 31 Oct, pricing 1 Nov 2026, from Meta, OpenAI, xAI, Anthropic and Manus; vendors change both "
             "without notice. Comparison: BULDRR, 22 Oct 2026 · click", 9, TEAL, autofit=False)
    t.click_action.hyperlink.address = "https://buldrr.com/claude-duet-vs-muse-vs-grokbot-vs-dots"

APPS.append(dict(key="cue", kicker="Topic 1 · Always-on agent · Manus Cue", title="Manus Cue: What It Does and How to Set It Up",
      sub="Manus · early access since 28 Sep 2026 · free with an invite code · reference route",
      can=[("user", "Agent identity", "Each agent has its own email address, phone number, wallet and computer."),
           ("phone", "Calls, messages, payments", "Takes forwarded calls, emails from its own address and pays within the budget you set."),
           ("users", "Agent teams", "Agents share a group chat and a goal; you make the final call."),
           ("plug", "Connectors and routines", "Gmail, Trip.com, Oura and more; routines repeat your steps; scan a QR code to create an agent.")],
      steps=[("Get Cue", "cue.im on the web, desktop or Android; iOS pending."), ("Invite code", "Sign up with an invite code from your trainer or a user."),
             ("Create an agent", "Give it one responsibility and the context it needs."), ("Identity + limits", "Choose its email, phone, wallet; set budgets and approvals."),
             ("Connect + routines", "Connect Gmail or other services, then define routines for repeat steps.")],
      tip="Reference route only. Keep wallet budgets small; require approval for payments, calls and messages.",
      video="https://www.youtube.com/shorts/ZW7gCKTLtpo",
      links=[("Cue by Manus: cue.im", "https://cue.im/")]))

def app_page(D, a):
    from pptx_online_video import add_online_video
    s = D.new(); header(D, s, a["kicker"], a["title"], a["sub"])
    picture(s, asset("apps", f"{a['key']}-logo.png"), 11.55, 0.4, maxw=1.15, maxh=1.15, frame=False)
    card(s, 0.6, 2.3, 4.85, 3.95); text(s, 0.85, 2.42, 4.4, 0.35, "What it can do", 14, ACC, bold=True, font=SERIF, autofit=False)
    for i, (ic, t, d) in enumerate(a["can"]):
        y = 2.85 + i * 0.84; icon(s, ic, 0.85, y + 0.04, 0.38)
        text(s, 1.35, y, 3.95, 0.3, t, 12.5, INK, bold=True, autofit=False)
        text(s, 1.35, y + 0.3, 3.95, 0.52, d, 10.5, MUTED, minpt=8.5)
    card(s, 5.6, 2.3, 4.45, 3.95, fill=CHAR, shadow=False); text(s, 5.85, 2.42, 4.0, 0.35, "How to set it up", 14, ACC, bold=True, font=SERIF, autofit=False)
    for i, (t, d) in enumerate(a["steps"]):
        y = 2.82 + i * 0.65; circle(s, 5.85, y + 0.04, 0.36, ACC)
        text(s, 5.85, y + 0.04, 0.36, 0.36, str(i + 1), 12, WHITE, bold=True, align="c", anchor="m", autofit=False)
        text(s, 6.35, y, 3.55, 0.28, t, 12.5, WHITE, bold=True, autofit=False)
        text(s, 6.35, y + 0.27, 3.55, 0.36, d, 10, SOFT, minpt=8)
    # 9:16 frame for a YouTube Short; the poster carries a play button and "Click to play"; fallback link under it
    add_online_video(s, a["video"], 10.5, 2.3, 2.0, 3.55, poster=asset("apps", f"{a['key']}-poster-play.jpg"), name=a["title"].split(":")[0] + " (YouTube Short)")
    tip(D, s, a["tip"], y=6.35)
    links_row(s, a["links"])

# ------------------------------------------------------------------ v47: Meridian worked demo (fictitious) and the bonus topic
# Owner request, 18 Nov 2026: a Meridian scenario per topic, a screenshot of Meridian's filled demo board per activity
# (live, read-only reference boards meridian-activity-1/2/3 on the Activity Studio), and a self-paced bonus topic:
# ChatGPT Plus (free AI subscription, if eligible) -> Codex in the ChatGPT desktop app builds Meridian's website -> deploy with Sites.
MERIDIAN_SITE = "https://alfredang.github.io/bcm/meridian/"
SITES_DOC = "https://learn.chatgpt.com/docs/sites"
def demo_url(n): return f"{B.BCM_URL}?join=meridian-activity-{n}"

def meridian_scene(D, kicker, title, sub, facts, ask, ask_label):
    """Meridian scenario: four facts on the left, this topic's question for Meridian on the right."""
    s = D.new(); header(D, s, kicker, title, sub)
    top, bot = 2.45, 6.55; rh = (bot - top) / len(facts)
    card(s, 0.6, top, 7.4, bot - top)
    for i, (ic, t, d) in enumerate(facts):
        y = top + 0.2 + i * rh; icon(s, ic, 0.9, y + 0.02, 0.55)
        text(s, 1.65, y - 0.02, 6.1, 0.36, t, 16, INK, bold=True, font=SERIF, autofit=False)
        text(s, 1.65, y + 0.36, 6.1, rh - 0.45, d, 14, MUTED, minpt=10)
    card(s, 8.25, top, 4.45, bot - top, fill=CHAR)
    text(s, 8.55, top + 0.25, 3.9, 0.35, ask_label.upper(), 12, ACC, bold=True, autofit=False)
    text(s, 8.55, top + 0.7, 3.9, 2.5, ask, 22, WHITE, bold=True, font=SERIF, minpt=14, lh=1.08)
    text(s, 8.55, bot - 0.95, 3.9, 0.8, "Meridian is fictitious; all figures are synthetic. Your board and your PP are about your own organisation.",
         11.5, SOFT, minpt=9)
    return s

def meridian_shot(D, kicker, title, sub, img, n, notes):
    """Meridian's filled demo board as a real Activity Studio screenshot, with a QR to the live board."""
    s = D.new(); header(D, s, kicker, title, sub)
    x, y, w, h = picture(s, asset("screenshots", img), 0.6, 2.3, maxw=6.6, maxh=4.5)
    url = demo_url(n); rx = 7.65
    card(s, rx, 2.3, 5.05, 2.2, fill=CHAR)
    qr(s, url, rx + 0.25, 2.5, 1.8, dark=True)
    text(s, rx + 2.25, 2.5, 2.65, 0.75, "Open Meridian's live board", 17, WHITE, bold=True, font=SERIF, minpt=12, lh=1.0)
    t = text(s, rx + 2.25, 3.3, 2.65, 0.5, f"alfredang.github.io/bcm\n?join=meridian-activity-{n}", 10.5, "7FB8B6", autofit=False)
    t.click_action.hyperlink.address = url
    text(s, rx + 2.25, 3.85, 2.65, 0.55, "Read it, zoom in, copy the structure. Do not edit it.", 10.5, SOFT, minpt=8.5)
    for i, (t_, d) in enumerate(notes):
        yy = 4.75 + i * 0.68
        circle(s, rx, yy + 0.03, 0.4, ACC)
        text(s, rx, yy + 0.03, 0.4, 0.4, str(i + 1), 13, WHITE, bold=True, align="c", anchor="m", autofit=False)
        rich(s, rx + 0.55, yy - 0.02, 4.5, 0.66, [[(t_ + "  ", dict(color=INK, bold=True, size=13.5, font=SERIF)),
                                                (d, dict(color=MUTED, size=12))]])
    return s

def bonus_open(D):
    s = D.new(dark=True)
    circle(s, -1.7, 5.2, 4.2, ACC)
    text(s, 0.9, 0.9, 7.6, 0.45, "BONUS TOPIC  ·  SELF-PACED  ·  OPTIONAL", 12.5, ACC, bold=True, autofit=False)
    text(s, 0.85, 1.45, 7.9, 2.0, "Put Your Business Online: Build a Website with Codex, Ship It with Sites", 34, WHITE, bold=True, font=SERIF, cw=0.52, lh=1.04)
    text(s, 0.9, 3.75, 7.7, 0.9, "ChatGPT Plus includes Codex, and Plus hosting covers Sites. Describe the site, check it, deploy it.", 19, SOFT, font=SERIF, lh=1.1)
    card(s, 0.9, 4.95, 7.6, 1.6, fill=PANEL, shadow=False)
    text(s, 1.15, 5.08, 7.1, 0.32, "OUTSIDE THE 16 CONTACT HOURS  ·  NOT ASSESSED", 11.5, ACC, bold=True, autofit=False)
    text(s, 1.15, 5.42, 7.1, 1.05, "Do it after class with your Activity 1 to 3 boards as the content. The worked example is Meridian Assist.", 15, WHITE, minpt=11, lh=1.1)
    items = ["Claim ChatGPT Plus", "Brief Codex like a web designer", "Build and preview with Codex", "Deploy with Sites and share", "Meridian Assist: the finished site"]
    rowh = 0.62; ph = 0.4 + len(items) * rowh; py = max(0.55, (7.5 - ph) / 2 - 0.1)
    card(s, 8.95, py, 3.85, ph, fill=PANEL, shadow=False)
    for i, it in enumerate(items):
        yy = py + 0.22 + i * rowh
        text(s, 9.15, yy, 0.45, 0.42, str(i + 1), 17, ACC, bold=True, font=SERIF, autofit=False)
        text(s, 9.6, yy, 3.05, rowh, it, 13, LIGHT, minpt=9.5)
    text(s, 6.4, 7.08, 6.4, 0.3, f"© Tertiary Infotech Academy Pte Ltd  ·  {D.code}", 9, K.FOOT, align="r", autofit=False)
    return s

SITE_PROMPT = ("Build a one-page business website for Meridian Assist, the always-on AI maintenance agent from "
               "Meridian Services Pte Ltd, a fictitious Singapore facilities firm.\n"
               "Audience: building managers who want same-day answers.\n"
               "Sections: hero with a one-line promise and a 'Book a demo' button; what it does (3 cards); "
               "how it works (connect, triage, monitor, decide at day 90); plans; trust (human approval, PDPA, audit trail); contact.\n"
               "Content: use only the facts in my Activity 1-3 boards (pasted below). Mark anything else (assumption).\n"
               "Style: ivory background, charcoal text, terracotta #D97757 accents, serif headings; mobile-first; one index.html; no tracking.\n"
               "Then show me a preview and list every claim on the page so I can check it.")

def bonus(D, C, mark):
    """Self-paced bonus topic (v47): ChatGPT Plus -> Codex -> Sites. Outside the CP contact hours, not assessed."""
    from ccdeck import flow as _flow
    KB = "Bonus · Build your business website"
    mark("bonus"); bonus_open(D)
    s = _flow(D, KB + " · Step 1", "Eligible? Your Free AI Subscription Can Cover ChatGPT Plus, with Codex.", [
        ("medal", "Redeem", "Singapore Citizens 18+: the SkillsFuture free AI subscription (admin slide at the start)."),
        ("check", "Choose ChatGPT Plus", "One of the plans offered; six months, one per person. After that, Plus is paid."),
        ("download", "Get the desktop app", "Install the ChatGPT desktop app (formerly the Codex app), sign in, open Codex."),
        ("globe", "Sites is in your plan", "Plus includes Sites: 125 hosting credits a month.")],
        tipt="Sites hosting comes with Plus, Pro, Business and Enterprise. Free for now; from 1 Jan 2027, use above the monthly allowance is paid.")
    links_row(s, [("OpenAI: Sites (official docs)", SITES_DOC),
                  ("SkillsFuture: redeem your AI subscription", "https://www.myskillsfuture.gov.sg/content/portal/en/career-resources/career-resources/education-career-personal-development/redeem-ai-subscription.html")])
    s = prompt(D, KB + " · Step 2", "Brief Codex Like You Would Brief a Web Designer", SITE_PROMPT,
               sub="Your three activity boards already hold the content: customers, value, plan, proof. Paste them in.",
               side=[("target", "One page, one goal", "Every section pushes to 'Book a demo'."),
                     ("eyecheck", "Claims you can prove", "Numbers come from your boards, or are marked (assumption)."),
                     ("lock", "No personal data", "No names, phones or NRIC numbers on a public page.")],
               label="PROMPT  ·  the Meridian version; swap in your own business")
    flow(D, KB + " · Step 3", "Build, Preview, Deploy: Four Moves with Codex", [
        ("folder", "New project", "Open Codex in the desktop app; make a folder such as meridian-site."),
        ("chat", "Paste the brief", "Codex writes the page. Ask for changes in plain words."),
        ("eye", "Preview and check", "Read every claim; try the phone view and every button."),
        ("rocket", "Deploy with Sites", "Ask Codex to publish it with Sites, review the preview, deploy, get the URL.")],
        sub="You describe and decide. Codex writes the code; Sites hosts it.",
        tipt="Check who can open the site under Share before you send the link.")
    s = D.new(); header(D, s, KB + " · Step 4", "Meridian Assist: One Website, Built from Three Boards",
                        "The demo site for the fictitious Meridian. Every section traces back to a note on Activity 1, 2 or 3.")
    picture(s, asset("screenshots", "meridian-website.png"), 0.6, 2.35, maxw=7.6, maxh=4.4)
    card(s, 8.55, 2.35, 4.15, 4.4, fill=CHAR)
    qr(s, MERIDIAN_SITE, 9.6, 2.6, 2.05, dark=True)
    t = text(s, 8.7, 4.85, 3.85, 0.4, "alfredang.github.io/bcm/meridian", 13, "7FB8B6", bold=True, align="c", autofit=False)
    t.click_action.hyperlink.address = MERIDIAN_SITE
    text(s, 8.75, 5.3, 3.75, 1.35, "Hero = Activity 1 value proposition\nHow it works = Activity 2 pilot\nTrust = Activity 3 guardrails\n(course copy on GitHub Pages)",
         12.5, SOFT, align="c", minpt=9.5, lh=1.15)
    return s

# ================================================================== TOPIC 2
def topic2(D, C, mark):
    tp = C.TOPICS[1]; K2 = "Topic 2 · Action plan"
    mark("t2"); topic_open(D, C, tp)
    meridian_scene(D, K2 + " · Meridian scenario", "Meridian Picked Triage. Now It Needs a Plan the CEO Will Fund.",
        "Same fictitious firm, Topic 2: turn the winning idea into a 90-day plan with one owner and a kill switch.", [
        ("target", "The goal", "Same-day response for every client: handling time from 18 to 11 minutes by day 90."),
        ("route", "The process", "Six steps and three handoffs today, from email to coordinator to ticket to technician."),
        ("coins", "The budget", "SGD 39,000 in year 1: licences, integration, training and change."),
        ("shield", "The worry", "A misrouted urgent job. One leak sent to the wrong team costs a contract.")],
        "Which steps go to the agent, who owns the result, and what stops the pilot?", "Meridian's Topic 2 question")
    framework(D, "Topic 2 · The 90-day action plan", "PLAN", "Five Steps to Get Started with AI Agents", B.PLAN,
              "Every slide in this topic serves one step. Activity 2 is the 90-day plan for your business.",
              tipt="Steps 1 and 2 first: no agent before a goal and a real process.")
    big_statement(D, K2, "Your best data is asleep.", "The real story of your company sits in calls, chats and tickets nobody reads. AI can now read all of it.")
    concept(D, "Dormant data", 2)
    full_image(D, "Topic 2 · Step 2 · Mine the process", "Awaken the Data You Already Own", asset("ainative", "dormant-data.png"),
               "Digitise what you already have: text, audio, images, spreadsheets and logs, read by one model.")
    mark("t2layer")
    concept(D, "Enterprise AI decision layer", 2)
    full_image(D, "Topic 2 · Step 3 · Plug in the agents", "Four Parts Turn Data into Decisions", asset("ainative", "decision-layer.png"),
               "Brain, map, navigation, operating system: wired across the whole company.")
    mark("t2map")
    concept(D, "Company map (ontology)", 2)
    hubbig(D, "Topic 2 · Step 3 · Plug in the agents", "The Map Teaches AI How Your Business Works", "Company map", [
        ("user", "People", "Who decides what"), ("users", "Customers", "What 'active' means here"), ("box", "Products", "SKU = product code?"),
        ("cart", "Orders", "Life cycle and states"), ("file", "Contracts", "Linked to obligations"), ("check", "Approvals", "Three more after signing")],
        foot="Ontology 2.0: drawn in plain language by the people who run the business, and revised any day.")
    icons(D, "Topic 2 · Step 3 · Plug in the agents", "Four Subsystems Let Agents Act Safely", [
        ("calendar", "Scheduling", "Plans the steps. Knows how to wait."), ("flask", "Execution", "Tests first: execute, check, correct"),
        ("plug", "Access", "One keycard to CRM, ERP, email (MCP)"), ("eye", "Control", "Your permissions. Every action logged.")], cols=4,
        tipt="An agent never has more rights than the person who asks it.")
    # --- Step 1 / Step 2
    mark("t2steps")
    icons(D, "Topic 2 · Step 2 · Mine the process", "Step 2: Mine the Business Process", arrows=True, items=[
        ("target", "Pick one", "A process that hurts weekly"), ("inbox", "Pull the trail", "Emails, tickets, logs, chats"),
        ("list", "Rebuild it", "Trigger, steps, hand-offs"), ("clock", "Measure", "Waits, rework, touch time"),
        ("hand", "Mark decisions", "Who judges, on what evidence")],
        sub="See what really happens, not what the SOP says.", tipt="Example: 6 steps, 3 hand-offs, 38% of the time spent re-keying.")
    ladder(D, "Topic 2 · Step 3 · Plug in the agents", "Step 3: Where Agents Plug In", [
        ("Inform", "Summarise, alert"), ("Recommend", "Rank, suggest"), ("Prepare", "Draft the ticket"),
        ("Execute with approval", "Acts after your yes"), ("Execute with monitoring", "Acts; you audit")],
        sub="Climb the Agent Stairway one rung at a time. Each rung needs a named human.")
    vs(D, "Topic 2 · Step 3 · Plug in the agents", "Example: A Service Desk Before and After",
       ("Before", "user", ["Coordinator reads 80 emails a day", "Re-keys every ticket by hand", "18 min a request · 14% rework"]),
       ("After", "robot", ["Agent drafts every ticket in 1 min", "Coordinator approves and calls clients", "Target 11 min · rework below 12%"]))
    mark("t2arch")
    ladder(D, "Topic 2 · Step 3 · Plug in the agents", "Choose the Simplest Pattern That Works", [
        ("Automation", "Fixed rules"), ("Assistant", "Grounded answers"), ("Agentic workflow", "Fixed steps, AI inside"),
        ("Single agent", "Chooses its own steps"), ("Multi-agent", "A team with a hub")])
    icons(D, "Topic 2 · Step 3 · Plug in the agents", "Build, Buy or Both? Decide on Five Numbers", [
        ("star", "Our edge", "Is it what makes us different?"), ("rocket", "Time to value", "Weeks or months?"), ("plug", "Integration", "Fits our systems?"),
        ("coins", "3-year TCO", "Licences + build + run + change"), ("route", "Exit", "Can we leave cleanly?")], cols=5,
        tipt="Most firms land on hybrid: buy the platform, own the company map and the rules.")
    s = D.new(dark=True); header(D, s, "Topic 2 · Step 1 · Set the goal", "Step 1: Write the Contract Before You Write the Prompt")
    for i, (w, ex) in enumerate([("Population", "10,000 eligible of 28,800"), ("Baseline", "18 min"), ("Target", "≤ 11 min by day 90"),
                                 ("Owner", "Head of Service Desk"), ("Counter-metric", "Complaints ≤ 2%")]):
        x = 0.6 + i * 2.46; card(s, x, 2.3, 2.3, 3.4, fill=PANEL, shadow=False)
        text(s, x, 2.55, 2.3, 0.6, str(i + 1), 34, ACC, bold=True, font=SERIF, align="c", autofit=False)
        text(s, x + 0.1, 3.3, 2.1, 0.9, w, 21, WHITE, bold=True, font=SERIF, align="c", minpt=13)
        text(s, x + 0.1, 4.35, 2.1, 1.2, ex, 15, SOFT, align="c", minpt=10)
    tip(D, s, "Example values for a service-desk agent. No baseline, no owner, no counter-metric: no build.", y=6.1)
    # --- activities 3 and 2, labs 7-10
    mark("act2a")
    c2 = B.CANVAS["actionplan"]
    L2 = B.LAB[2]
    activity_intro(D, "Topic 2 · Activity 2", c2, C)
    lab_overview(D, L2)
    for i in range(2): step_slide(D, L2, i)
    mark("act2b")
    step_slide(D, L2, 2)
    board_steps(D, L2)
    muse_board(D, "Topic 2 · Activity 2 · Step 5 · Meta Muse", c2)
    meridian_shot(D, "Topic 2 · Activity 2 · Meridian's demo board", "Meridian's 90-Day Plan: Five Steps, Nine Blocks, One Owner",
        "A finished Activity 2 board for the fictitious Meridian. Every step has a number, a name or a date.", "meridian-plan.png", 2, [
        ("Mined first.", "Six steps, three handoffs, 38% re-keying: then agents."),
        ("One DRI.", "Head of Service Desk owns it, with a SGD 39,000 budget."),
        ("A kill switch.", "Stop if rework tops 20% for two weeks.")])
    board(D, "Topic 2 · Activity 2 · Meridian's demo board", c2, "Meridian's 90-Day Plan, Block by Block",
          "The first note of each block, readable. The live board holds the full plan.", example=True)
    board(D, "Topic 2 · Activity 2 · Your board", c2, "Your 90-Day Plan: The Question Each Block Answers",
          "Steps 1 to 5, for your own organisation. Screenshot your group board for PP Task 2.", example=False)
    big_statement(D, "Next · Topic 3 · Sustain and Operate", "The plan is live.\nNow keep it running.",
                  "Run the business on DRIs and agent teams, keep people judging, review the numbers and keep new ideas coming.")
    mark("t2end")

# ================================================================== TOPIC 3
def topic3(D, C, mark):
    tp = C.TOPICS[2]; K3 = "Topic 3 · Sustain and operate"
    mark("t3"); topic_open(D, C, tp)
    meridian_scene(D, K3 + " · Meridian scenario", "Day 90 at Meridian: the Numbers Say Scale. The People Are Nervous.",
        "Same fictitious firm, Topic 3: keep the agents running, the coordinators judging and the ideas coming.", [
        ("chart", "The result", "Handling time 10.7 minutes, quality 95.1%, complaints 1.7%, adoption 77.5%."),
        ("users", "The mood", "Coordinators fear replacement; clients want faster answers, not a chatbot wall."),
        ("org", "The next step", "Scale from 10 sites to all 30 with the same approval rules."),
        ("lightbulb", "The opening", "Meridian Assist could become a product for other building managers.")],
        "How do we scale it without losing our people, our judgement or our clients' trust?", "Meridian's Topic 3 question")
    framework(D, "Topic 3 · The SCALE framework", "SCALE", "SCALE: Five Moves to Sustain and Operate with AI Agents", B.SCALE,
              "Run the business on agents without losing your people or your judgement. Activity 3 is your SCALE board.",
              tipt="Story before structure: people hear what changes for them before any role changes.")
    full_image(D, "Topic 3 · C · Commanders", "Rewrite the Org Chart Around DRIs", asset("ainative", "flattened-org.png"),
               "Fewer layers. One accountable person per outcome. Agents do the volume.")
    concept(D, "DRI (Directly Responsible Individual)", 3)
    icons(D, "Topic 3 · C · Commanders", "Flatten Smart: Five Moves, No Shock", arrows=True, items=[
        ("memory", "Codify", "Tacit know-how into the map"), ("flask", "Test", "Real task, real agents"),
        ("search", "Spot builders", "Who turns into a team?"), ("medal", "Give rights", "Goal, decision and resource rights"),
        ("layers", "Flatten slowly", "Relay layers fade out")],
        sub="Bayer went from 12-13 layers to 6-7 over a planned three-year journey.", tipt="Run old and new side by side (Kotter's dual operating system).")
    mark("t3work")
    vs(D, "Topic 3 · A · Augment people", "Agents Take the Routine. Move Your People Up.",
       ("Work that shrinks", "stop", ["Rule-bound tasks agents do cheaper", "Relaying messages up and down layers", "Signing off without really checking"]),
       ("Work that grows", "trend", ["Directing a team of agents as the DRI", "Judging the exceptions agents flag", "Human work: trust, negotiation, care"]),
       sub="Plan where each role goes before the agents arrive.")
    icons(D, "Topic 3 · A · Augment people", "Managers Move from Relay to Judgement", [
        ("gavel", "Judge at scale", "Owns outcomes for agents + people"), ("users", "Coach", "Teaches teams to work with agents"),
        ("network", "Translate", "Moves tacit know-how into the system"), ("stop", "Relay", "Only passes messages: most exposed")], cols=4)
    bignums(D, "Topic 3 · A · Augment people", "Train Everyone: AI Lifts Beginners Most", [
        ("10%+", "more issues solved per hour", "5,000+ support agents (Stanford & MIT)"),
        ("30%+", "for new and weaker staff", "The gains went mostly to novices"),
        ("2 = 6", "months of experience", "A 2-month hire matched a 6-month one")])
    bignums(D, "Topic 3 · A · Augment people", "Judgement Is a Muscle. Use It or Lose It.", [
        ("−6 pts", "cancer-lesion detection", "28.4% → 22.4% once doctors lost the AI tool"),
        ("80%", "accepted planted errors", "Wharton: wrong AI answers taken as right"),
        ("10 min", "is enough to weaken", "Carnegie Mellon problem-solving study")],
        tipt="Ask for hints before answers. Write your view first. Keep some work unassisted.")
    # --- review success, governance
    mark("t3review")
    bignums(D, "Topic 3 · E · Evaluate", "Day 90: The Numbers Decide", [
        ("10.7", "minutes per request", "from 18 · target ≤ 11"), ("95.1%", "quality", "target ≥ 94%"),
        ("1.7%", "complaints", "limit 2%"), ("77.5%", "staff adoption", "target ≥ 70%")],
        tipt="Example pilot: benefit SGD 39,200 vs year-1 cost SGD 39,000. Scale, redesign, hold or stop?")
    icons(D, "Topic 3 · E · Evaluate", "Singapore's Rulebook for Agents", [
        ("alert", "Bound the risk", "Assess and limit upfront"), ("user", "Humans accountable", "Meaningful oversight"),
        ("tool", "Technical controls", "Test, monitor, change-manage"), ("users", "Users responsible", "Train the people using agents")], cols=4,
        sub="IMDA Model AI Governance Framework for Agentic AI · four dimensions",
        source="IMDA MGF for Agentic AI v1.5 (20 May 2026) · CSA Securing Agentic AI addendum (Jun 2026) · PDPA",
        url="https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence")
    icons(D, "Topic 3 · E · Evaluate", "Four Ways an Agent Can Hurt You", [
        ("bolt", "Prompt injection", "A poisoned email gives orders"), ("lock", "Data leakage", "PDPA data in the wrong place"),
        ("eye", "Shadow AI", "Staff using unapproved tools"), ("scale", "Bias and blame", "Who answers for the decision?")], cols=4,
        tipt="Least privilege · human approval on anything irreversible · full audit trail.")
    hubbig(D, "Topic 3 · L · Loop information", "Information Flows Through the DRI, Not Up Ten Layers", "DRI + agents", [
        ("star", "Sponsor", "Monthly one-page dashboard"), ("users", "Staff", "Weekly review and Q&A"), ("smile", "Clients", "Faster updates, same people"),
        ("robot", "Agents", "Daily 8:00 exceptions brief"), ("lightbulb", "Idea pipeline", "Anyone posts; best get a DRI"), ("shield", "Risk & DPO", "Audit trail on demand")],
        foot="Daily brief · weekly review · monthly board: the operating rhythm of an AI-native firm.")
    # --- activity 4, labs 11-13
    mark("act3")
    c4 = B.CANVAS["change"]
    L3 = B.LAB[3]
    activity_intro(D, "Topic 3 · Activity 3", c4, C)
    lab_overview(D, L3)
    for i in range(2): step_slide(D, L3, i)
    board_steps(D, L3)
    muse_board(D, "Topic 3 · Activity 3 · Step 4 · Meta Muse", c4)
    meridian_shot(D, "Topic 3 · Activity 3 · Meridian's demo board", "Meridian's SCALE Board: Story to Evaluation, Filled In",
        "A finished Activity 3 board for the fictitious Meridian. Notice how often a person still decides.", "meridian-scale.png", 3, [
        ("Story first.", "No one loses their job in the pilot; every client reaches a person."),
        ("DRIs, not layers.", "One DRI per outcome, each with its own agent team."),
        ("Judged by numbers.", "Day-90 review, then scale to all 30 sites.")])
    board(D, "Topic 3 · Activity 3 · Meridian's demo board", c4, "Meridian's SCALE Board, Block by Block",
          "The first note of each block, readable. The live board holds the full version.", example=True)
    board(D, "Topic 3 · Activity 3 · Your board", c4, "Your SCALE Board: The Question Each Block Answers",
          "Story, Commanders, Augment people, Loop information, Evaluate, for your own organisation. Screenshot your group board for PP Task 3.", example=False)
    mark("lab13")
    step_slide(D, L3, 5)
    mark("t3end")
