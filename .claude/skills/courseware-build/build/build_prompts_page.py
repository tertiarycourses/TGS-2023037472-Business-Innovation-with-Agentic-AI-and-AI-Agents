#!/usr/bin/env python3
"""Meta Muse Prompts page: every prompt learners paste into https://muse.ai/, with Copy buttons, grouped by activity.
Single source: data_bi.py. Writes <course repo>/prompts/index.html and, if present, ~/projects/edtools/bcm/prompts.html.
Works offline (file://) and on GitHub Pages; no external scripts."""
import html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
import data_bi as B
REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
e = lambda t: html.escape(str(t))

ORG_KEY = "your organisation in two sentences"
def card(pid, kicker, title, prompt, note="", board=None):
    """A prompt TEMPLATE: one input per [placeholder] (organisation filled once, at the top), live preview, Copy copies the filled prompt."""
    import re
    b = (f'<a class="board" href="{e(B.BCM_URL)}?activity={board}" target="_blank" rel="noopener">Open the group board ↗</a>' if board else "")
    fields = []
    for ph in dict.fromkeys(re.findall(r"\[([^\]]+)\]", prompt)):
        if ph.startswith(ORG_KEY):
            fields.append('<div class="f org-note">Uses <b>Your organisation</b> from the top of the page.</div>'); continue
        big = ph.startswith("paste")
        ctl = (f'<textarea rows="3" data-ph="{e(ph)}" placeholder="{e(ph)}"></textarea>' if big
               else f'<input data-ph="{e(ph)}" placeholder="{e(ph)}">')
        fields.append(f'<label class="f"><span>{e(ph[0].upper() + ph[1:])}</span>{ctl}</label>')
    return (f'<article class="p" id="{pid}"><div class="k">{e(kicker)}</div><h3>{e(title)}</h3>'
            f'<div class="fields">{"".join(fields)}</div>'
            f'<div class="code"><button class="copy">Copy prompt</button><pre class="tpl" hidden>{e(prompt)}</pre><pre class="out"></pre></div>'
            f'<div class="foot">{e(note)} {b}</div></article>')

sec = []
nav = []
for L in B.LABS:
    cv = B.CANVAS[L["canvas"]]; sid = f"lab{L['n']}"; nav.append((sid, f"Activity {cv['num']}"))
    items = []
    for i, st in enumerate(L["steps"]):
        if not st.get("prompt"): continue
        board = st["prompt"] == "BOARD"
        items.append(card(f"l{L['n']}s{i + 1}", f"Activity {L['n']} · Step {i + 1}" + (" · draft the whole board" if board else " · Meta Muse"), st["title"],
                          cv["muse_prompt"] if board else st["prompt"],
                          ("Copy Muse's reply, then on your group board click Paste Muse answer, tick the lines you agree with, Add. Verify every note."
                           if board else "Check: " + st.get("check", "")), board=cv["key"] if board else None))
    sec.append(f'<section id="{sid}"><div class="sk">Topic {cv["topic"]} · {cv["lo"]} · {e(cv["evidence"])}</div>'
               f'<h2>Activity {L["n"]} · {e(L["title"])}</h2><p class="pitch">{e(L["goal"])} Group board: '
               f'<a href="{e(B.BCM_URL)}?activity={cv["key"]}" target="_blank" rel="noopener">{e(cv["title"])}</a>.</p>{"".join(items)}</section>')

CSS = """:root{--ivory:#FAF9F5;--char:#21201C;--panel:#2E2C26;--acc:#D97757;--accd:#C2603F;--teal:#3A7D7B;--muted:#6B6862;--rule:#E3DFD6;--code:#2B2924}
*{box-sizing:border-box}body{margin:0;background:var(--ivory);color:var(--char);font:16px/1.5 Calibri,"Segoe UI",system-ui,sans-serif}
header{background:var(--char);color:#fff;padding:28px 6vw 22px}header .k{color:var(--acc);font-weight:700;letter-spacing:.12em;font-size:12px;text-transform:uppercase}
h1,h2,h3{font-family:Cambria,Georgia,"Source Serif 4",serif}h1{margin:6px 0 4px;font-size:34px}header p{color:#C9C4B9;margin:0;max-width:820px}
nav{position:sticky;top:0;z-index:5;background:var(--ivory);border-bottom:1px solid var(--rule);padding:10px 6vw;display:flex;gap:8px;flex-wrap:wrap}
nav a{color:var(--char);text-decoration:none;border:1px solid var(--rule);border-radius:999px;padding:5px 14px;font-weight:600;font-size:14px;background:#fff}nav a:hover{border-color:var(--acc);color:var(--accd)}
main{padding:10px 6vw 60px;max-width:1100px}section{margin-top:34px}.sk{color:var(--teal);font-weight:700;font-size:12px;letter-spacing:.1em;text-transform:uppercase}
h2{font-size:28px;margin:4px 0}.pitch{color:var(--muted);margin:0 0 14px}
.p{background:#fff;border:1px solid var(--rule);border-left:4px solid var(--acc);border-radius:10px;padding:16px 18px;margin:14px 0;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.p .k{color:var(--accd);font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase}.p h3{margin:2px 0 10px;font-size:20px}
.code{position:relative;background:var(--code);border-radius:8px}pre{margin:0;padding:16px 92px 16px 16px;color:#F1EDE4;font:14px/1.45 Consolas,Menlo,monospace;white-space:pre-wrap;word-break:break-word}
.copy{position:absolute;top:10px;right:10px;background:var(--acc);color:#fff;border:0;border-radius:6px;padding:7px 14px;font-weight:700;cursor:pointer}.copy:hover{background:var(--accd)}.copy.ok{background:var(--teal)}
.fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:10px;margin-bottom:12px}.f span{display:block;font-size:13px;font-weight:700;color:var(--muted);margin-bottom:3px}
.f input,.f textarea,#org{width:100%;border:1px solid var(--rule);border-radius:8px;padding:8px 10px;font:15px Calibri,system-ui,sans-serif;background:#FFFDF8}.f input:focus,.f textarea:focus,#org:focus{outline:2px solid var(--acc);border-color:var(--acc)}
.org-note{font-size:13px;color:var(--teal);align-self:end}.orgbox{margin-top:16px;max-width:900px}.orgbox span{display:block;color:#C9C4B9;font-size:14px;margin-bottom:6px}#org{background:#fff;color:var(--char)}
mark{background:#5A3A2C;color:#FFD9C7;border-radius:3px;padding:0 2px}mark.done{background:transparent;color:#BFE3D8}
.foot{color:var(--muted);font-size:14px;margin-top:8px}.board{margin-left:6px;color:var(--teal);font-weight:700}
.how{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}.how span{background:var(--panel);color:#fff;border-radius:8px;padding:6px 12px;font-size:14px}
footer{color:var(--muted);font-size:13px;padding:20px 6vw;border-top:1px solid var(--rule)}a{color:var(--teal)}"""
JS = r"""const ORG='your organisation in two sentences';const org=document.getElementById('org');org.value=localStorage.getItem('bi.org')||'';
const esc=t=>t.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
function fill(card,html){const t=card.querySelector('.tpl').textContent;const vals={};card.querySelectorAll('[data-ph]').forEach(i=>vals[i.dataset.ph]=i.value.trim());
return t.replace(/\[([^\]]+)\]/g,(m,ph)=>{const v=ph.startsWith(ORG)?org.value.trim():(vals[ph]||'');if(!html)return v||m;return v?'<mark class="done">'+esc(v)+'</mark>':'<mark>'+esc(m)+'</mark>'});}
function render(card){const t=card.querySelector('.tpl').textContent;const parts=t.split(/(\[[^\]]+\])/);
card.querySelector('.out').innerHTML=parts.map(p=>{const m=p.match(/^\[([^\]]+)\]$/);if(!m)return esc(p);const ph=m[1];const inp=card.querySelector('[data-ph="'+CSS.escape(ph)+'"]');
const v=ph.startsWith(ORG)?org.value.trim():(inp?inp.value.trim():'');return v?'<mark class="done">'+esc(v)+'</mark>':'<mark>'+esc(p)+'</mark>'}).join('');}
const cards=[...document.querySelectorAll('.p')];cards.forEach(c=>{c.querySelectorAll('[data-ph]').forEach(i=>{const k='bi.'+c.id+'.'+i.dataset.ph;i.value=localStorage.getItem(k)||'';i.addEventListener('input',()=>{localStorage.setItem(k,i.value);render(c)})});render(c);
c.querySelector('.copy').addEventListener('click',async e=>{const b=e.currentTarget;const t=fill(c,false);const left=(t.match(/\[[^\]]+\]/g)||[]).length;
try{await navigator.clipboard.writeText(t)}catch(x){const ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();document.execCommand('copy');ta.remove()}
b.textContent=left?('Copied · '+left+' blank'+(left>1?'s':'')+' left'):'Copied';b.classList.add('ok');setTimeout(()=>{b.textContent='Copy prompt';b.classList.remove('ok')},2200)})});
org.addEventListener('input',()=>{localStorage.setItem('bi.org',org.value);cards.forEach(render)});"""
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Meta Muse Prompts · {e(C.TITLE)}</title><style>{CSS}</style></head><body>
<header><div class="k">WSQ {e(C.COURSE_CODE)} · Meta Muse prompts</div><h1>Copy. Paste into Meta Muse. Paste the answer into your board.</h1>
<p>{e(C.TITLE)}. Open <a href="https://muse.ai/" target="_blank" rel="noopener" style="color:#F2B49B">muse.ai</a> (or the Muse app), copy a prompt, replace the [ ] parts, then paste Muse's reply into your group board in the <a href="{e(B.BCM_URL)}" style="color:#F2B49B">Activity Studio</a>.</p>
<div class="orgbox"><label><span>Your organisation (two sentences: industry, size, customers, this year's objective). Fills every prompt that needs it; saved in this browser only.</span>
<textarea id="org" rows="2" placeholder="e.g. We are a Singapore facilities-maintenance firm with 140 staff serving 30 commercial buildings. This year we want same-day response for every client."></textarea></label></div>
<div class="how"><span>0 · Fill in the blanks</span><span>1 · Copy the prompt</span><span>2 · Paste into Meta Muse</span><span>3 · Check the answer</span><span>4 · Paste into your group board</span><span>5 · Screenshot for the PP</span></div></header>
<nav>{"".join(f'<a href="#{i}">{e(t)}</a>' for i, t in nav)}</nav>
<main>{"".join(sec)}</main>
<footer>Muse drafts; you decide. Never paste personal data (NRIC, phone numbers, customer names) into a shared board. © {e(C.ORG)} · {e(C.VERSION)} · {e(C.VERSION_DATE)}</footer>
<script>{JS}</script></body></html>"""
outs = [os.path.join(REPO, "prompts", "index.html")]
bcm = os.path.expanduser("~/projects/edtools/bcm")
if os.path.isdir(bcm): outs.append(os.path.join(bcm, "prompts.html"))
for o in outs:
    os.makedirs(os.path.dirname(o), exist_ok=True); open(o, "w", encoding="utf-8").write(page); print("wrote", o)
