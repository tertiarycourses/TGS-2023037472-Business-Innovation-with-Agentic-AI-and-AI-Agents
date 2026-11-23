#!/usr/bin/env python3
"""Three activity folders (activities/activity-0N-<slug>/), each holding ONE step-by-step ACTIVITY-0N-Instructions.pdf:
every step, the Meta Muse prompt template (blanks highlighted), how to use the group board in the Activity
Studio (with screenshots) and what to check. Source: data_bi.py. Also writes activities/README.md (index for GitHub).
Old per-lab README.md/README.pdf and the v41-draft activities/ folders are removed by the orchestrator."""
import html, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
import data_bi as B
REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
SHOTS = os.path.join(REPO, "courseware", "assets", "screenshots")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
e = html.escape
def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
def blanks(t): return re.sub(r"\[([^\]]+)\]", lambda m: f'<span class="b">[{m.group(1)}]</span>', e(t))
def img(name, cap, w=100):
    p = os.path.join(SHOTS, name)
    return f'<figure><img src="file://{p}" style="width:{w}%"><figcaption>{e(cap)}</figcaption></figure>' if os.path.exists(p) else ""
STUDIO_IMG = {"join": ("bcm-landing.png", "Activity Studio: join your group board with the Board ID or QR code", 92),
              "muse": ("prompts-page.png", "Prompt templates: type your organisation once, fill the blanks, Copy prompt", 80),
              "capture": ("bcm-screenshot-view.png", "Screenshot view: download PNG or PDF for your PP task", 55)}

CSS = """@page{size:A4;margin:16mm 15mm}body{font:10.5pt/1.45 Calibri,Arial,sans-serif;color:#21201C}
.top{background:#21201C;color:#fff;padding:14px 18px;border-radius:8px}.top .k{color:#D97757;font-weight:700;letter-spacing:.1em;font-size:9pt}
.top h1{font-family:Cambria,Georgia,serif;margin:4px 0;font-size:20pt}.top p{margin:0;color:#C9C4B9}
.meta{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:12px 0}.meta div{border:1px solid #E3DFD6;border-radius:6px;padding:6px 8px;background:#FAF9F5}
.meta b{display:block;font-size:8.5pt;color:#C2603F;text-transform:uppercase;letter-spacing:.06em}
.step{border:1px solid #E3DFD6;border-left:4px solid #D97757;border-radius:8px;padding:10px 14px;margin:12px 0;break-inside:avoid}
.step.studio{border-left-color:#3A7D7B}.step h2{font-family:Cambria,Georgia,serif;font-size:13.5pt;margin:0 0 6px}
.n{display:inline-block;background:#D97757;color:#fff;border-radius:50%;width:22px;height:22px;text-align:center;line-height:22px;font-size:10pt;margin-right:6px}
.studio .n{background:#3A7D7B}.tag{font-size:8pt;font-weight:700;color:#3A7D7B;letter-spacing:.06em;text-transform:uppercase}
ol{margin:4px 0 6px 18px;padding:0}pre{background:#2B2924;color:#F1EDE4;border-radius:6px;padding:9px 11px;white-space:pre-wrap;font:9pt/1.4 Consolas,Menlo,monospace;margin:6px 0}
.b{background:#5A3A2C;color:#FFD9C7;border-radius:3px;padding:0 2px}.chk{color:#3A7D7B;font-weight:700}
figure{margin:6px 0;text-align:center}figure img{max-height:62mm;width:auto!important;max-width:100%;border:1px solid #E3DFD6;border-radius:6px}figcaption{font-size:8.5pt;color:#6B6862}
.qrs{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:8px 0}.qr{text-align:center;border:1px solid #E3DFD6;border-radius:8px;padding:8px}
.qr img{width:110px;height:110px;border:0}.qr b{display:block;font-size:10pt}.qr span{display:block;font-size:7.5pt;color:#6B6862;word-break:break-all}
.note{background:#FBEFD9;border-radius:6px;padding:8px 12px;margin-top:12px;font-size:9.5pt}.foot{color:#6B6862;font-size:8pt;margin-top:14px;border-top:1px solid #E3DFD6;padding-top:6px}"""

def lab_html(L):
    cv = B.CANVAS[L["canvas"]]; url = f"{B.BCM_URL}?activity={cv['key']}"
    h = [f'<div class="top"><div class="k">WSQ {e(C.COURSE_CODE)} · TOPIC {L["topic"]} · {e(cv["lo"])} · ACTIVITY {cv["num"]}</div>'
         f'<h1>Activity {L["n"]} — {e(L["title"])}</h1><p>{e(L["goal"])}</p></div>',
         '<div class="meta">'
         f'<div><b>Time</b>{L["minutes"]} min</div><div><b>Tools</b>Meta Muse app or muse.ai website + your group board</div>'
         f'<div><b>Group board</b>{e(url.replace("https://", ""))}</div><div><b>Evidence</b>{e(cv["evidence"])}</div></div>',
         '<div class="note"><b>Before you start.</b> Use the current fill-in prompts for this edition. '
         'Download <b>activities/prompts.html</b> from the LMS course materials or the course Activities folder and open it in a browser. Type your organisation once; it fills every prompt. Replace every <span class="b">[blank]</span> before you paste into Meta Muse. '
         'Muse drafts; your group decides. Never put personal data (NRIC, phone numbers, customer names) on a shared board.</div>']
    q, pts = B.PADLET_TALK[L['n']]   # v56: team padlet talk opens the group work
    h.append(f'<div class="note"><b>Start here, right after the trainer’s Meridian demo: team padlet discussion (15 min, as a group).</b> {e(q)} Join your team padlet at '
             '<b>alfredang.github.io/padlet</b> with your team code and your name, post one idea per card in this topic\'s column, then build the activity board together.<ol>'
             + ''.join(f'<li>{e(x)}</li>' for x in pts) + '</ol>'
             + ' · '.join(f'<b>Team {e(t)}</b> {c}' for t, c in B.PADLET_TEAMS) + '</div>')
    h.append(qr_html([(f'Team {t} · {c}', B.PADLET_URL + c) for t, c in B.PADLET_TEAMS]))
    if L["n"] == 1:
        h.append('<h2>Earlier in Topic 1: Mini Activity — Try Meta Muse (20 min)</h2><p>Do this just after the agent introductions. No PP screenshot is required for this mini activity.</p>')
        for i, step in enumerate(B.MINI_MUSE["steps"]):
            h.append(f'<div class="step"><h2>Mini step {i + 1} · {e(step["title"])}</h2><ol>' + ''.join(f'<li>{e(x)}</li>' for x in step["body"]) + '</ol>')
            if step.get("links") == "MUSE": h.append(qr_html(B.MUSE_LINKS))
            h.append(f'<pre>{blanks(step["prompt"])}</pre><p><b>Check:</b> {e(step["check"])}</p></div>')
        h.append('<h2>At the end of Topic 1: Activity 1 — Your Company BMC (80 min)</h2>')
        h.append(f'<div class="step"><h2>After the padlet talk · {e(B.PAIN_HUNT["title"])} ({B.PAIN_HUNT["minutes"]} min)</h2><ol>'
                 + ''.join(f'<li>{e(x)}</li>' for x in B.PAIN_HUNT["body"]) + '</ol>'
                 f'<pre>{blanks(B.PAIN_HUNT["prompt"])}</pre><p><b>Check:</b> {e(B.PAIN_HUNT["check"])}</p></div>')   # v57: hunt follows the padlet talk
        h.append('<div class="note"><b>Group task.</b> Stay in your padlet team of <b>3-5 learners</b> and choose one member\'s company. '
                 'The leader opens <b>alfredang.github.io/bcm/?activity=opportunity</b>, creates ONE Activity 1 board and names the company. '
                 'Everyone joins with its Board ID or QR code and their own name. Create your company\'s BMC across all nine blocks, '
                 'show where AI agents help, and label assumptions. Keep this company for Activities 2 and 3.</div>')
    if L["n"] == 2:
        h.append('<div class="note"><b>Group task.</b> Use one shared board and the company you chose in Activity 1. '
                 'Follow the completed Meridian example in the slides. The tasks below help you fill all nine boxes in the five plan steps. '
                 'For each evaluation metric, write the baseline, target, data source, owner and review cadence. '
                 'Agree when to scale, redesign or stop.</div>')
    if L["n"] == 3:
        h.append('<div class="note"><b>Group task.</b> Stay in groups of 3–5. Review Meridian’s completed SCALE board first. '
                 'Continue with your own company and pilot from Activity 2. Use one shared board and fill every SCALE box.</div>')
    for i, st in enumerate(L["steps"]):
        studio = st.get("studio")
        prompt = cv["muse_prompt"] if st.get("prompt") == "BOARD" else st.get("prompt")
        h.append(f'<div class="step{" studio" if studio else ""}">' + (f'<div class="tag">On the group board</div>' if studio else '<div class="tag" style="color:#C2603F">In Meta Muse</div>')
                 + f'<h2><span class="n">{i + 1}</span>{e(st["title"])}</h2><ol>' + "".join(f"<li>{e(x)}</li>" for x in st["body"]) + "</ol>")
        if st.get("links") == "MUSE": h.append(qr_html(B.MUSE_LINKS))
        if prompt: h.append(f"<pre>{blanks(prompt)}</pre>")
        if studio == "refine":
            h.append("<ol start='1' style='list-style:none;margin-left:0'><li>Each block: one idea per note, specific names, numbers and owners.</li>"
                     "<li>Type a new answer in the block's <b>Type your answer…</b> box and press Enter; click a note to edit or delete it.</li></ol>")
        if studio in STUDIO_IMG: h.append(img(*STUDIO_IMG[studio]))
        if st.get("check"): h.append(f'<div><span class="chk">Check:</span> {e(st["check"])}</div>')
        h.append("</div>")
    h.append('<div class="note"><b>For the PP.</b> Every member pastes the group board screenshot (PNG or PDF) into the PP task and writes the answers individually.</div>')
    h.append(f'<div class="foot">{e(C.TITLE)} ({e(C.COURSE_CODE)}) · {e(C.VERSION)} · {e(C.VERSION_DATE)} · © {e(C.ORG)}</div>')
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>" + "".join(h)

def qr_html(links):
    import base64, io, qrcode
    cells = []
    for label, url in links:
        bio = io.BytesIO(); qrcode.make(url, border=1).save(bio, format="PNG")
        cells.append(f'<div class="qr"><img src="data:image/png;base64,{base64.b64encode(bio.getvalue()).decode()}"><b>{e(label)}</b><span>{e(url.replace("https://", ""))}</span></div>')
    return '<div class="qrs">' + "".join(cells) + "</div>"

def to_pdf(page, out):
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, "p.html"); open(src, "w", encoding="utf-8").write(page)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                        f"--print-to-pdf={out}", "file://" + src], check=True, capture_output=True)

def main():
    root = os.path.join(REPO, "activities"); os.makedirs(root, exist_ok=True)
    idx = [f"# Activities — {C.TITLE}", "", "Three activities, one per learning outcome: Meta Muse supplies the inputs, your group "
           f"refines the board in the Activity Studio ({B.BCM_URL}), and every member screenshots it for the PP.", "",
           "Current prompt templates: download prompts.html from this activities folder (LMS course materials) and open the downloaded file in your browser. All prompt text is also printed in the Instructions PDFs.", "", "The first section of Activity 1 Instructions is the earlier 20-minute Meta Muse mini activity; the BMC group task takes 80 minutes at the end of Topic 1.", "", 'Topic 3 interactive tools (download and open in a browser): activity-03-sustain-and-operate-with-ai-agents-scale/ai-readiness-scorecard.html (Activity 3 Part A) and token-cost-calculator.html (Topic 3 token budget drill).', "", 'Bonus sample: download [meridian-ai-dashboard.html](meridian-ai-dashboard.html) and open it in your browser. It is the dashboard the bonus topic asks you to vibe code: Meridian’s results against targets, SCALE progress, rollout, guardrails and decisions (fictitious company, synthetic figures).', "", "| Activity | Title | Topic | Group board | Instructions |", "|---|---|---|---|---|"]
    for L in B.LABS:
        cv = B.CANVAS[L["canvas"]]; f = f"activity-{L['n']:02d}-{slug(cv['title'])}"; d = os.path.join(root, f); os.makedirs(d, exist_ok=True)
        to_pdf(lab_html(L), os.path.join(d, f"ACTIVITY-{L['n']:02d}-Instructions.pdf"))
        if L["n"] == 3:   # v53: interactive Topic 3 tools (readiness scorecard, token cost calculator) ship in the Activity 3 folder
            import shutil
            for t in ("ai-readiness-scorecard.html", "token-cost-calculator.html"):
                shutil.copy(os.path.join(HERE, "tools", t), os.path.join(d, t))
        idx.append(f"| {L['n']} | {L['title']} | {L['topic']} ({cv['lo']}) | {B.BCM_URL}?activity={cv['key']} | {f}/ACTIVITY-{L['n']:02d}-Instructions.pdf |")
    open(os.path.join(root, "README.md"), "w", encoding="utf-8").write("\n".join(idx) + "\n")
    print("activities written:", [L["n"] for L in B.LABS])

if __name__ == "__main__": main()
