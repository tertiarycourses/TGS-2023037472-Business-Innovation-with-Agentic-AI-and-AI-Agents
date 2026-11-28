"""v54 (owner, 23 Nov 2026): six principles of AI security (Guardrails added) with one page per principle.

Content and incidents follow TGS-2025052468 Agentic AI Applications with Claude Code (deck v30 slides 80 and 84-89,
LG 3.3 AI Security), rewritten for business leaders: no settings.json, the same incidents and visual structures.
Sources (as cited there): Bloomberg, 2 May 2023 (Samsung); Fortune, 23 Jul 2025 (Replit / SaaStr);
Moffatt v. Air Canada, 2024 BCCRT 149; PDPC, Guide on Managing and Notifying Data Breaches under the PDPA;
anthropic.com/glasswing, 7 Apr 2026 (Claude Mythos Preview); Google Workspace Gmail API scopes.
"""
import ccdeck as K
from ccdeck import (header, card, text, rich, icon, line, circle, box, footer, tip,
                    ACC, TEAL, PLUM, CHAR, PANEL, WHITE, INK, MUTED, SOFT, LIGHT, SERIF, MONO, DIM)

AMBER = "D9A13B"
RED = "C2603F"
CREAM = "F3EEE6"
K_ = "Topic 3 · E · AI security"

SEC6 = [("Data Control", "WHAT AI CAN SEE", "Label your data public, internal, confidential, restricted; decide which labels the AI may read."),
        ("Permission Control", "WHAT AI CAN DO", "Grant only the verbs the job needs: read, write, send, pay, delete."),
        ("Guardrails", "WHAT AI MUST NEVER DO", "Rules checked outside the model, before every action: caps, blocks, filters."),
        ("Human in the Loop", "WHO APPROVES", "A person approves high-impact actions: sends, payments, deletions."),
        ("Traceability", "WHAT HAPPENED", "Log every request, tool call and result so you can audit and roll back."),
        ("Right-Sized Models", "NOT THE MOST POWERFUL", "Use the smallest model that passes your checks; more power needs more control.")]


def overview(D):
    s = D.new(); header(D, s, K_ + " controls", "Six Principles That Keep Your Agents Safe",
                        "Your agents read your inbox, spend your money and speak for your brand. Six controls keep what they see and do safe, reviewable and accountable.")
    g = 0.16; w = (12.1 - 5 * g) / 6; top, h = 2.55, 3.7
    for i, (t, lab, d) in enumerate(SEC6):
        x = 0.6 + i * (w + g); dk = i == 2
        card(s, x, top, w, h, fill=CHAR if dk else WHITE)
        text(s, x + 0.14, top + 0.18, w - 0.28, 0.45, str(i + 1), 24, ACC, bold=True, font=SERIF, autofit=False)
        text(s, x + 0.14, top + 0.7, w - 0.28, 0.75, t, 16, WHITE if dk else INK, bold=True, font=SERIF, minpt=11, lh=1.0)
        text(s, x + 0.14, top + 1.45, w - 0.28, 0.4, lab, 9, ACC, bold=True, minpt=7.5, lh=1.0)
        text(s, x + 0.14, top + 1.9, w - 0.28, h - 2.0, d, 12, SOFT if dk else MUTED, minpt=9, lh=1.1)
    tip(D, s, "At Meridian: read-only Gmail and ServiceNow, masked tenant data, hard caps on what the agent may say and do, coordinator "
              "approval on urgent jobs, every action logged, a small model for triage. One page per principle follows.", y=6.35)
    return s


def _kicker(n): return f"{K_} · {n} of 6 · {SEC6[n - 1][0]}"


def data_control(D):
    s = D.new(); header(D, s, _kicker(1), "Four Labels Decide What the Agent May Read",
                        "April 2023: Samsung engineers pasted internal code into ChatGPT. By May, Samsung had restricted generative AI.")
    tiers = [("globe", "PUBLIC", TEAL, "Brochure, website copy, published prices", 4, "Any approved AI tool"),
             ("building", "INTERNAL", AMBER, "SOPs, meeting notes, the staff handbook", 3, "Company AI account only"),
             ("file", "CONFIDENTIAL", ACC, "Client contracts, financials, pricing models", 2, "Named project, masked first"),
             ("lock", "RESTRICTED", PLUM, "NRIC numbers, passwords, health records", 0, "The AI never sees it")]
    text(s, 2.75, 2.25, 3.4, 0.3, "WHAT IT HOLDS", 9.5, MUTED, bold=True, autofit=False)
    text(s, 6.2, 2.25, 2.4, 0.3, "HOW MUCH THE AI MAY SEE", 9.5, MUTED, bold=True, autofit=False)
    for i, (ic, lab, col, holds, n, rule) in enumerate(tiers):
        y = 2.6 + i * 0.9
        card(s, 0.6, y, 8.1, 0.8)
        box(s, 0.6, y, 2.0, 0.8, fill=col, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
        icon(s, ic, 0.75, y + 0.17, 0.46, fill=col)
        text(s, 1.3, y + 0.22, 1.3, 0.36, lab, 11, WHITE, bold=True, minpt=8, autofit=False)
        text(s, 2.75, y + 0.08, 3.3, 0.64, holds, 12, INK, minpt=9, anchor="m")
        for k in range(4):
            box(s, 6.2 + k * 0.58, y + 0.14, 0.5, 0.2, fill=col if k < n else LIGHT, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3)
        text(s, 6.2, y + 0.4, 2.4, 0.36, rule, 11.5, INK, bold=True, minpt=9, autofit=False)
    card(s, 8.95, 2.25, 3.75, 2.35, fill=CHAR)
    text(s, 9.2, 2.42, 3.3, 0.3, "AT MERIDIAN", 11, ACC, bold=True, autofit=False)
    text(s, 9.2, 2.8, 3.3, 1.75, "The triage agent reads the service inbox and ServiceNow tickets. Tenant names and phone numbers are "
         "masked first. HR, finance and contracts are never connected.", 13, SOFT, minpt=10, lh=1.1)
    card(s, 8.95, 4.75, 3.75, 1.45, fill=CREAM, shadow=False)
    icon(s, "shield", 9.15, 4.98, 0.55)
    text(s, 9.85, 4.9, 2.75, 1.25, "Sort first, connect second. Label the data before any agent touches it.", 12.5, INK, bold=True, minpt=9.5, lh=1.05)
    tip(D, s, "Keep restricted data out of every folder and mailbox the agent can reach; a rule in the prompt is not a lock.", y=6.35)
    return s


def permission_control(D):
    s = D.new(); header(D, s, _kicker(2), "Authorise the Verb, Not Just the Agent",
                        "July 2025: Replit's agent deleted SaaStr's production database in a code freeze. Delete was never its verb.")
    verbs = [("eye", "Read"), ("pen", "Write"), ("edit", "Edit"), ("stop", "Delete"), ("send", "Send"), ("wallet", "Pay")]
    agents = [("Research agent", "Answers from your documents", "AXXXXX"),
              ("Triage agent", "Meridian: reads requests, opens tickets", "AAQXQX"),
              ("Customer agent", "Replies to clients", "AQXXQQ")]
    col = {"A": TEAL, "Q": AMBER, "X": RED}; mark_ = {"A": "✓", "Q": "?", "X": "✕"}
    card(s, 0.6, 2.25, 8.3, 4.0)
    text(s, 0.85, 2.5, 2.3, 0.3, "AUTHORISATION MATRIX", 9.5, MUTED, bold=True, autofit=False)
    for j, (ic, v) in enumerate(verbs):
        x = 3.3 + j * 0.92
        icon(s, ic, x + 0.12, 2.38, 0.48, fill=CHAR)
        text(s, x - 0.1, 2.9, 0.92, 0.3, v, 11, INK, bold=True, align="c", autofit=False)
    for i, (a, d, row) in enumerate(agents):
        y = 3.3 + i * 0.82
        box(s, 0.75, y, 8.0, 0.72, fill=CREAM if i % 2 == 0 else WHITE)
        text(s, 0.9, y + 0.06, 2.35, 0.32, a, 12.5, INK, bold=True, font=SERIF, autofit=False)
        text(s, 0.9, y + 0.37, 2.35, 0.32, d, 9.5, MUTED, minpt=8, autofit=False)
        for j, c in enumerate(row):
            x = 3.3 + j * 0.92 + 0.16
            circle(s, x, y + 0.15, 0.42, col[c])
            text(s, x, y + 0.15, 0.42, 0.42, mark_[c], 13, WHITE, bold=True, align="c", anchor="m", autofit=False)
    for k, (c, lab) in enumerate([("A", "Allow"), ("Q", "Ask a human first"), ("X", "Deny")]):
        x = 0.9 + k * 2.4
        circle(s, x, 5.85, 0.3, col[c]); text(s, x, 5.85, 0.3, 0.3, mark_[c], 10, WHITE, bold=True, align="c", anchor="m", autofit=False)
        text(s, x + 0.4, 5.84, 1.9, 0.32, lab, 11.5, INK, bold=True, autofit=False)
    card(s, 9.15, 2.25, 3.55, 2.3, fill=CHAR)
    text(s, 9.4, 2.42, 3.1, 0.3, "GIVE EACH AGENT ITS OWN ID", 11, ACC, bold=True, autofit=False)
    text(s, 9.4, 2.8, 3.1, 1.7, "Never let an agent use a staff member's login. Its own account means its own rights, its own log "
         "and one switch to revoke.", 13, SOFT, minpt=10, lh=1.1)
    card(s, 9.15, 4.7, 3.55, 1.55, fill=CREAM, shadow=False)
    text(s, 9.35, 4.82, 3.2, 1.35, "Deny beats ask beats allow. Start read-only; add one verb at a time, and review the rights every month.",
         12.5, INK, bold=True, minpt=9.5, lh=1.05)
    tip(D, s, "Google splits Gmail access into gmail.readonly and gmail.send. Copy that split: reading is one right, sending is another.", y=6.35)
    return s


def guardrails(D):
    s = D.new(); header(D, s, _kicker(3), "Guardrails: Rules the Agent Cannot Talk Its Way Past",
                        "A prompt is a request. A guardrail is a rule checked outside the model, before the action runs. It holds even when the agent is fooled.")
    steps = [("chat", "Customer asks", "“Refund order A1042?”", CHAR), ("robot", "Agent prepares", "a S$89 refund", CHAR),
             ("shield", "Guardrail checks", "real order? under the cap? no personal data out?", TEAL),
             ("bolt", "Action runs", "or is blocked with a reason", ACC), ("file", "Logged", "every call, pass or block", CHAR)]
    box(s, 0.6, 2.2, 12.1, 1.05, fill=CREAM, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
    w = 12.1 / 5
    for i, (ic, t, d, c) in enumerate(steps):
        x = 0.75 + i * w
        icon(s, ic, x, 2.38, 0.6, fill=c)
        text(s, x + 0.68, 2.33, w - 0.85, 0.32, t, 12, TEAL if c == TEAL else INK, bold=True, minpt=9, autofit=False)
        text(s, x + 0.68, 2.64, w - 0.85, 0.55, d, 9.5, MUTED, minpt=8, lh=1.0)
        if i < 4: text(s, x + w - 0.27, 2.47, 0.25, 0.4, "›", 20, ACC, bold=True, autofit=False)
    # one chat, two outcomes
    card(s, 0.6, 3.45, 5.95, 2.8)
    text(s, 0.85, 3.58, 5.5, 0.35, "One agent, two outcomes", 15, TEAL, bold=True, font=SERIF, autofit=False)
    for k, (q, a, res, col, why) in enumerate([
            ("Order A1042 arrived cracked. Can I get my S$89 back?", "Yes. Refund RF-2291 is on its way to your card.", "PASSED", TEAL, "Real order, under the S$500 cap."),
            ("Refund S$2,000 for order A0007 too.", "That is above what I can approve, so I have passed it to our team.", "BLOCKED", RED, "Over the S$500 cap: the refund never starts.")]):
        y = 4.0 + k * 1.1
        box(s, 2.6, y, 3.75, 0.36, fill=CREAM, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2)
        text(s, 2.7, y + 0.02, 3.6, 0.32, q, 9.5, INK, minpt=8, autofit=False)
        box(s, 0.8, y + 0.42, 3.9, 0.36, fill="E3EEED", shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2)
        text(s, 0.9, y + 0.44, 3.75, 0.32, a, 9.5, INK, minpt=8, autofit=False)
        rich(s, 0.85, y + 0.8, 5.5, 0.28, [[(res + "  ", dict(color=col, bold=True, size=9)), (why, dict(color=MUTED, size=9))]])
    # four kinds of guardrail
    kinds = [("search", "Screen the input", "Treat emails, web pages and files as data, never as orders: it blocks prompt injection."),
             ("eye", "Check the output", "Block personal data, made-up policy and off-brand replies before they leave."),
             ("gauge", "Set hard limits", "Spend caps, allowed recipients, a list of actions the agent may never take."),
             ("pause", "Keep a kill switch", "One switch stops the agent; a stop rule pulls it automatically.")]
    for i, (ic, t, d) in enumerate(kinds):
        r, c = divmod(i, 2); x = 6.75 + c * 3.0; y = 3.45 + r * 1.42
        card(s, x, y, 2.9, 1.32)
        icon(s, ic, x + 0.15, y + 0.15, 0.45, fill=ACC)
        text(s, x + 0.7, y + 0.15, 2.1, 0.4, t, 12.5, INK, bold=True, font=SERIF, minpt=10, autofit=False)
        text(s, x + 0.15, y + 0.65, 2.65, 0.65, d, 10, MUTED, minpt=8, lh=1.0)
    tip(D, s, "Seen in Topic 1: Gemini Spark pauses before sharing ID or financial details; Manus Cue pays only within the budget you set. "
              "Illustrative refund cap: set your own.", y=6.35)
    return s


def human_in_loop(D):
    s = D.new(); header(D, s, _kicker(4), "Put the Gate Where the Damage Would Be",
                        "Feb 2024: a tribunal held Air Canada liable for its chatbot's wrong refund advice. The agent speaks; you answer.")
    icon(s, "robot", 0.8, 3.65, 0.95, fill=CHAR)
    text(s, 0.45, 4.7, 1.7, 0.6, "Agent proposes a refund", 12, INK, bold=True, align="c", minpt=9)
    line(s, 1.8, 4.12, 2.55, 4.12, color=CHAR, w=2, arrow=True)
    d_ = box(s, 2.6, 3.32, 1.6, 1.6, fill=ACC, shape=K.MSO_SHAPE.DIAMOND)
    text(s, 2.75, 3.85, 1.3, 0.55, "How big is the risk?", 11, WHITE, bold=True, align="c", anchor="m", minpt=8)
    routes = [("bolt", "AUTO-RUN", TEAL, "Under S$50", "The agent acts on its own and logs what it did."),
              ("hand", "HUMAN GATE", AMBER, "S$50 to S$500", "The agent stops and waits. A supervisor approves or rejects before anything happens."),
              ("user", "ESCALATE", RED, "Over S$500, a legal threat or a low-confidence answer", "The agent hands the whole case, with its context, to a manager.")]
    for i, (ic, lab, col, t, d) in enumerate(routes):
        y = 2.25 + i * 1.42
        line(s, 4.2, 4.12, 5.0, y + 0.62, color=col, w=2, arrow=True)
        card(s, 5.05, y, 7.65, 1.28)
        box(s, 5.05, y, 1.6, 1.28, fill=col, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
        icon(s, ic, 5.55, y + 0.15, 0.55, fill=col)
        text(s, 5.1, y + 0.78, 1.5, 0.35, lab, 10.5, WHITE, bold=True, align="c", minpt=8, autofit=False)
        text(s, 6.85, y + 0.17, 5.7, 0.4, t, 14, INK, bold=True, font=SERIF, minpt=10)
        text(s, 6.85, y + 0.6, 5.7, 0.62, d, 12, MUTED, minpt=9.5)
    text(s, 0.6, 5.5, 4.2, 0.6, "Illustrative thresholds. At Meridian, urgent jobs, complaints and premium clients go to the coordinator on shift.",
         10.5, MUTED, italic=True, minpt=8.5)
    tip(D, s, "Seen in Topic 1: Claude Duet shows exactly what it will send, pay or sign, then waits. Watch for rubber-stamping: a 2-second approval is no review.", y=6.35)
    return s


def traceability(D):
    s = D.new(); header(D, s, _kicker(5), "The Log Is How You Find the Leak",
                        "A customer list turns up on a paste site. Without logs you have a guess. With logs you have a timeline, a culprit and a fix.")
    box(s, 10.9, 0.45, 1.8, 0.3, fill=CHAR, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
    text(s, 10.9, 0.47, 1.8, 0.26, "ILLUSTRATIVE SCENARIO", 8, WHITE, bold=True, align="c", autofit=False)
    ev = [("09:02", "chat", "Prompt", "“Summarise our Q3 customers”", CHAR), ("09:03", "folder", "Read", "customers.csv", CHAR),
          ("09:04", "globe", "Web page", "carries a hidden instruction", AMBER), ("09:05", "alert", "Leak", "uploads the file to a paste site", RED),
          ("09:06", "file", "Logged", "audit log writes it; alert fires", TEAL)]
    line(s, 1.4, 2.85, 11.9, 2.85, color=LIGHT, w=3)
    for i, (tm, ic, t, d, col) in enumerate(ev):
        x = 0.6 + i * 2.45
        text(s, x, 2.2, 1.6, 0.3, tm, 11, MUTED, font=MONO, align="c", autofit=False)
        icon(s, ic, x + 0.5, 2.55, 0.6, fill=col)
        text(s, x - 0.3, 3.22, 2.2, 0.3, t, 12, RED if col == RED else INK, bold=True, align="c", autofit=False)
        text(s, x - 0.3, 3.5, 2.2, 0.5, d, 10, MUTED, align="c", minpt=8)
    card(s, 0.6, 4.15, 5.9, 2.05, fill=K.CODEBG)
    text(s, 0.8, 4.25, 5.5, 0.28, "audit log: the line that cracks the case", 10, DIM, font=MONO, autofit=False)
    text(s, 0.8, 4.6, 5.6, 1.5, "09:03 agent=analyst-helper  tool=Read\n      file=customers.csv  asked-by=analyst\n"
         "09:05 agent=analyst-helper  tool=Upload\n      to=paste-site.example  outcome=success", 12, "F1EDE4", font=MONO, minpt=9, lh=1.1)
    qs = [("user", "Who asked?", "the analyst's request at 09:02"), ("file", "What did it touch?", "customers.csv, at 09:03"),
          ("map", "Where did it go?", "paste-site.example, at 09:05"), ("stop", "How do you contain it?", "block the site, revoke access, assess under the PDPA")]
    for i, (ic, q, a) in enumerate(qs):
        y = 4.15 + i * 0.52
        card(s, 6.7, y, 6.0, 0.46)
        icon(s, ic, 6.8, y + 0.05, 0.36, fill=ACC)
        rich(s, 7.3, y + 0.08, 5.3, 0.32, [[(q + "  ", dict(color=INK, bold=True, size=11)), (a, dict(color=MUTED, size=10.5))]])
    tip(D, s, "PDPA: assess a suspected breach within 30 days; if it is notifiable, tell PDPC within 3 calendar days. No logs, no answer.", y=6.35)
    return s


def right_sized(D):
    s = D.new(); header(D, s, _kicker(6), "More Power, Harder to Control",
                        "Anthropic keeps Claude Mythos Preview out of general release: it exploits software flaws like few humans can.")
    text(s, 0.6, 2.2, 5.0, 0.3, "Control effort climbs with capability", 12, INK, bold=True, autofit=False)
    text(s, 0.6, 2.47, 5.0, 0.28, "Rule of thumb, not a benchmark", 10, MUTED, autofit=False)
    steps = [("Haiku", TEAL, "Narrow jobs", "triage, sorting, extraction; allowlist the tools", 1.5),
             ("Sonnet", AMBER, "Everyday work", "drafting and analysis; add approval rules and tests", 2.15),
             ("Opus", ACC, "Long autonomous runs", "plus a sandbox and human review", 2.8),
             ("Mythos Preview", PLUM, "Not generally available", "partners only, until better safeguards exist", 3.4)]
    for i, (n, col, t, d, h) in enumerate(steps):
        x = 0.6 + i * 2.05; y = 6.2 - h
        box(s, x, y, 1.9, h, fill=col)
        icon(s, "lock" if i == 3 else "cpu", x + 0.1, y + 0.1, 0.36, fill=col)
        text(s, x + 0.5, y + 0.12, 1.35, 0.32, n, 11.5, WHITE, bold=True, minpt=9, autofit=False)
        text(s, x + 0.1, y + 0.5, 1.75, 0.3, t, 10.5, WHITE, bold=True, minpt=8.5, autofit=False)
        text(s, x + 0.1, y + 0.8, 1.75, h - 0.85, d, 10, WHITE, minpt=8)
    line(s, 0.7, 4.55, 8.3, 2.65, color=CHAR, w=2.5, arrow=True)
    card(s, 8.95, 2.2, 3.75, 2.25, fill=CREAM, shadow=False)
    text(s, 9.15, 2.3, 3.4, 0.36, "Size it in three steps", 14, INK, bold=True, font=SERIF, autofit=False)
    for k, t in enumerate(["Start with the smallest model.", "Prove it on your own 30-case test.", "Step up only when the test fails."]):
        y = 2.8 + k * 0.52
        circle(s, 9.15, y, 0.38, ACC); text(s, 9.15, y, 0.38, 0.38, str(k + 1), 11, WHITE, bold=True, align="c", anchor="m", autofit=False)
        text(s, 9.65, y + 0.03, 2.95, 0.36, t, 12, INK, minpt=9, autofit=False)
    card(s, 8.95, 4.6, 3.75, 1.6, fill=CHAR)
    text(s, 9.15, 4.72, 3.4, 0.3, "AT MERIDIAN", 11, ACC, bold=True, autofit=False)
    text(s, 9.15, 5.05, 3.4, 1.1, "Triage runs on Haiku 5.5: about US$3 a month for 80 requests a day, against US$211 on Fable 5.2.",
         12, SOFT, minpt=9.5, lh=1.05)
    text(s, 0.6, 6.78, 12.1, 0.25, "Source: Anthropic, Project Glasswing and Claude Mythos Preview (anthropic.com/glasswing, 7 Apr 2026)", 8, MUTED, autofit=False)
    tip(D, s, "Do not default to the biggest model. Give each agent the smallest one that passes your checks: the bill is lower and every step is easier to audit.", y=6.35)
    return s


def security6(D, kicker=None):
    """Overview, then one page per principle (owner, v54)."""
    s = overview(D)
    for f in (data_control, permission_control, guardrails, human_in_loop, traceability, right_sized):
        f(D)
    return s


# ------------------------------------------------------------------ DRI (owner, 23 Nov 2026: "the part on the DRI is missing")
# v52 had a DRI org-chart slide plus a concept card; v53 cut the slide and left only the text card. WA Q5 asks for
# "the role of the DRI", so v55 teaches it in three designed pages right after the outcome org chart.
# Sources: Fortune, "How Apple works: inside the world's biggest startup" (May 2011: DRIs at Apple; QA v55: supports use, not coinage);
# GitLab Handbook, "Directly Responsible Individuals (DRI)" (handbook.gitlab.com, checked 23 Nov 2026).
KD = "Topic 3 · C · The future organisation · DRI"


def _person(s, x, y, d, fill):
    icon(s, "user", x, y, d, fill=fill)


def dri_meet(D):
    s = D.new(); header(D, s, KD, "One Outcome, One Name: Meet the DRI",
                        "Made famous at Apple: every task carries a person's name. Agents can do the work; they cannot answer for it.")
    # before / after panel
    card(s, 0.6, 2.3, 7.55, 2.45)
    text(s, 0.85, 2.42, 3.3, 0.3, "WITHOUT A DRI", 10, RED, bold=True, autofit=False)
    text(s, 4.55, 2.42, 3.3, 0.3, "WITH A DRI", 10, TEAL, bold=True, autofit=False)
    line(s, 4.35, 2.5, 4.35, 4.6, K.RULE, 1.0)
    for i in range(5):                                   # a committee around a question mark
        _person(s, 0.8 + i * 0.66, 2.95, 0.5, MUTED)
    circle(s, 1.9, 3.6, 0.55, RED)
    text(s, 1.9, 3.6, 0.55, 0.55, "?", 20, WHITE, bold=True, align="c", anchor="m", autofit=False)
    text(s, 0.8, 4.18, 3.4, 0.5, "Five owners means no owner. “The AI did it.”", 12, INK, minpt=9, lh=1.0)
    _person(s, 5.75, 2.82, 0.62, ACC)                     # one name, a mixed team below
    icon(s, "flag", 6.22, 2.76, 0.3, fill=CHAR)
    team = [("robot", ACC), ("robot", ACC), ("user", TEAL), ("robot", ACC), ("user", TEAL)]
    for j, (ic, col) in enumerate(team):
        x = 4.62 + j * 0.66
        line(s, 6.06, 3.44, x + 0.2, 3.62, K.MUTED, 1.0)
        icon(s, ic, x, 3.62, 0.4, fill=col)
    text(s, 4.55, 4.18, 3.5, 0.5, "One name answers. People and agents do the volume.", 12, INK, minpt=9, lh=1.0)
    # definition
    card(s, 8.4, 2.3, 4.3, 2.45, fill=CHAR)
    text(s, 8.65, 2.42, 3.9, 0.3, "DIRECTLY RESPONSIBLE INDIVIDUAL", 10, ACC, bold=True, autofit=False)
    text(s, 8.65, 2.78, 3.85, 1.1, "The one named person accountable for an outcome, with the rights to deliver it.",
         17, WHITE, font=SERIF, minpt=12, lh=1.05)
    text(s, 8.65, 3.95, 3.85, 0.7, "Agents bring capability.\nThe DRI brings accountability.", 13, SOFT, bold=True, minpt=10, lh=1.05)
    # three properties
    props = [("user", "Singular", "One named person. Not a committee, not a department, not “the AI team”."),
             ("target", "Accountable", "Owns the outcome, not just the task. Answers when the agent gets it wrong."),
             ("gavel", "Empowered", "Holds decision and resource rights, commands the agent team, can press stop.")]
    w = (12.1 - 0.3) / 3
    for i, (ic, t, d) in enumerate(props):
        x = 0.6 + i * (w + 0.15)
        card(s, x, 4.95, w, 1.3)
        icon(s, ic, x + 0.18, 5.12, 0.5, fill=ACC)
        text(s, x + 0.82, 5.08, w - 0.95, 0.4, t, 16, INK, bold=True, font=SERIF, autofit=False)
        text(s, x + 0.82, 5.45, w - 0.95, 0.75, d, 11.5, MUTED, minpt=9, lh=1.05)
    tip(D, s, "GitLab runs its company handbook on DRIs: the DRI consults the people affected, then makes the final call.", y=6.38)
    text(s, 0.6, 6.78, 12.1, 0.25, "Sources: Fortune, “How Apple works” (May 2011) · GitLab Handbook, Directly Responsible Individuals",
         8, MUTED, autofit=False)
    return s


def dri_charter(D):
    s = D.new(); header(D, s, KD + " at Meridian", "Meridian's DRI Charter: One Page, One Owner",
                        "Write the DRI's rights down. An owner without a budget, rule changes or a stop button is a scapegoat, not a DRI.")
    rows = [("OUTCOME", "Handling time from 18 to ≤11 minutes by day 90; complaints ≤2%"),
            ("DRI", "Head of Service Desk  ·  backup: the senior coordinator"),
            ("AGENT TEAM", "Triage agent drafts tickets; SLA agent flags late jobs; 2 coordinators review"),
            ("DECISION RIGHTS", "Changes routing rules and the playbook; decides what the agent may draft"),
            ("RESOURCE RIGHTS", "SGD 39,000 year-1 budget; system access granted through IT"),
            ("STOP BUTTON", "Pauses the agent if rework tops 20% for two weeks"),
            ("BOUNDARIES", "Coordinators approve every dispatch; tenant-data questions go to the DPO"),
            ("RHYTHM", "Daily 8:00 exceptions brief · weekly review · monthly dashboard to the CEO")]
    card(s, 0.6, 2.3, 8.15, 3.95)
    for i, (k, v) in enumerate(rows):
        y = 2.4 + i * 0.47
        if i % 2 == 0: box(s, 0.7, y, 7.95, 0.44, fill=CREAM)
        text(s, 0.85, y + 0.02, 1.95, 0.4, k, 10, ACC if k != "STOP BUTTON" else RED, bold=True, anchor="m", autofit=False)
        text(s, 2.85, y + 0.02, 5.75, 0.4, v, 12, INK, bold=(k == "DRI"), anchor="m", autofit=False)   # one size for every row (QA v55)
    card(s, 9.0, 2.3, 3.7, 2.2, fill=CHAR)
    icon(s, "scale", 9.22, 2.48, 0.5, fill=ACC)
    text(s, 9.85, 2.5, 2.75, 0.5, "Rights match the responsibility", 13.5, WHITE, bold=True, font=SERIF, minpt=10, lh=1.0, anchor="m")
    text(s, 9.22, 3.12, 3.3, 1.3, "If the DRI owns handling time, the DRI must also be able to change the rules, spend the budget and stop the agent.",
         12, SOFT, minpt=9.5, lh=1.08)
    card(s, 9.0, 4.65, 3.7, 1.6, fill=CREAM, shadow=False)
    text(s, 9.2, 4.75, 3.35, 0.3, "YOUR ACTIVITY 3 BOARD", 10, ACC, bold=True, autofit=False)
    text(s, 9.2, 5.07, 3.35, 1.12, "Block C · DRIs & Agent Teams asks for exactly this: one name, decision rights, resource rights, boundaries.",
         12, INK, minpt=9.5, lh=1.06)
    tip(D, s, "Every agent in the capability register has an owner and a backup owner. A row that names a team instead of a person has no DRI yet.", y=6.38)
    return s


def dri_does(D):
    s = D.new(); header(D, s, KD, "What a DRI Does, and What a DRI Does Not Do",
                        "Not a hero who does all the work. Not a manager who signs whatever the agent drafts.")
    cols = [("check", TEAL, "A DRI DOES", [
                ("users", "Consult the people affected, then make the final call"),
                ("target", "Set the agents' goal, limits and checks"),
                ("eye", "Read the exceptions and sample the agents' work every week"),
                ("megaphone", "Answer for the result, good or bad, and report back")]),
            ("stop", RED, "A DRI DOES NOT", [
                ("tool", "Do all the work alone"),
                ("pause", "Wait for consensus before deciding"),
                ("thumbs", "Rubber-stamp whatever the agent drafts"),
                ("robot", "Say “the AI did it” when something goes wrong")])]
    for c, (hic, col, head, items) in enumerate(cols):
        x = 0.6 + c * 6.15
        card(s, x, 2.3, 5.95, 3.2)
        icon(s, hic, x + 0.22, 2.42, 0.5, fill=col)
        text(s, x + 0.85, 2.47, 4.8, 0.4, head, 14, col, bold=True, anchor="m", autofit=False)
        for i, (ic, t) in enumerate(items):
            y = 3.08 + i * 0.6
            icon(s, ic, x + 0.3, y + 0.04, 0.4, fill=CHAR if c == 0 else MUTED)
            text(s, x + 0.88, y, 4.9, 0.5, t, 14, INK, anchor="m", minpt=10, lh=1.0)
    card(s, 0.6, 5.68, 12.1, 0.62, fill=CHAR)
    rich(s, 0.85, 5.7, 11.7, 0.58, [[("TEST YOUR BOARD   ", dict(color=ACC, bold=True, size=13)),
         ("Write one person's name next to every outcome. A team, a committee or “the AI” means you have no DRI yet.",
          dict(color=WHITE, size=14, font=SERIF))]], anchor="m")
    tip(D, s, "Bias and Blame (Topic 3 · E) shows what happens when no one owns an agent's decision.", y=6.42)
    return s


def dri(D):
    """Three DRI pages: concept, Meridian's charter, does / does not (v55)."""
    first = dri_meet(D)
    dri_charter(D); dri_does(D)
    return first


def future_org(D):
    """v55 (owner): open Topic 3 with the future organisation: flatter, people + agents, projects driven by DRIs."""
    s = D.new(); header(D, s, "Topic 3 · C · The future organisation", "Fewer Layers, Mixed Teams, Projects Driven by DRIs",
                        "When agents take the relaying, reporting and first drafts, the layers that only pass work along thin out.")
    # TODAY: a tall pyramid of relay layers
    card(s, 0.6, 2.3, 4.6, 2.75)
    text(s, 0.85, 2.4, 4.1, 0.3, "TODAY · MANY LAYERS, WORK RELAYED", 10, MUTED, bold=True, autofit=False)
    for r, n in enumerate([1, 2, 3, 4, 6, 8]):
        y = 2.8 + r * 0.33; w_ = 0.32; g = 0.12; tot = n * w_ + (n - 1) * g; x0 = 2.9 - tot / 2
        for k in range(n):
            box(s, x0 + k * (w_ + g), y, w_, 0.22, fill=SOFT if r < 5 else LIGHT, line=K.RULE)
    text(s, 0.85, 4.8, 4.1, 0.25, "Status climbs up, instructions trickle down", 10.5, MUTED, align="c", autofit=False)
    text(s, 5.3, 3.35, 0.5, 0.6, "→", 30, ACC, bold=True, align="c", autofit=False)
    # TOMORROW: sponsor, DRIs, mixed teams
    card(s, 5.9, 2.3, 6.8, 2.75)
    text(s, 6.15, 2.4, 6.3, 0.3, "AI-NATIVE · THREE LAYERS, ONE NAME PER PROJECT", 10, TEAL, bold=True, autofit=False)
    icon(s, "star", 9.05, 2.72, 0.5, fill=CHAR)
    text(s, 9.6, 2.78, 2.8, 0.4, "CEO · AI sponsor", 12, INK, bold=True, autofit=False)
    projects = ["Handling time", "Client retention", "First-time fix"]
    for j, pj in enumerate(projects):
        x = 6.25 + j * 2.12
        line(s, 9.3, 3.22, x + 0.95, 3.45, K.MUTED, 1.0)
        card(s, x, 3.45, 1.9, 0.5, fill=CREAM, shadow=False)
        icon(s, "flag", x + 0.08, 3.52, 0.36, fill=ACC)
        text(s, x + 0.5, 3.47, 1.38, 0.46, "DRI · " + pj, 10, INK, bold=True, anchor="m", minpt=8, lh=1.0)
        for k, (ic, col) in enumerate([("user", TEAL), ("robot", ACC), ("robot", ACC), ("user", TEAL)]):
            line(s, x + 0.95, 3.95, x + 0.2 + k * 0.45 + 0.16, 4.12, K.MUTED, 0.75)
            icon(s, ic, x + 0.2 + k * 0.45, 4.12, 0.32, fill=col)
    text(s, 6.15, 4.6, 6.3, 0.3, "People judge and decide; agents do the volume; one DRI owns each project", 10.5, MUTED, align="c", autofit=False)
    # three shifts
    shifts = [("layers", "Fewer layers", "Agents absorb the relay work: status reports, hand-offs, first drafts, follow-ups."),
              ("users", "People + agents, one team", "Every team mixes staff and agents. People set goals, judge exceptions and own clients."),
              ("flag", "Projects driven by DRIs", "Each project has one named owner with the rights, budget and stop button to deliver it.")]
    w = (12.1 - 0.3) / 3
    for i, (ic, t, d) in enumerate(shifts):
        x = 0.6 + i * (w + 0.15)
        card(s, x, 5.2, w, 1.1, fill=CHAR if i == 2 else WHITE)
        icon(s, ic, x + 0.16, 5.33, 0.46, fill=ACC)
        text(s, x + 0.75, 5.27, w - 0.85, 0.36, t, 14.5, WHITE if i == 2 else INK, bold=True, font=SERIF, autofit=False)
        text(s, x + 0.75, 5.62, w - 0.85, 0.65, d, 11, SOFT if i == 2 else MUTED, minpt=8.5, lh=1.03)
    tip(D, s, "This is where Topic 3 ends up. First, Meridian's version of it; then the challenges that stop most companies getting there.", y=6.42)
    return s


# --- v56 (owner, 23 Nov 2026): ontology-driven agents, Topic 3 Part D (L: build AI into the workflow) ---
KO = "Topic 3 · L · Ontology-driven agents"


def _node(s, x, y, w, h, ic, title, sub, fill, col):
    box(s, x, y, w, h, fill=fill, line=col, lw=1.25, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
    icon(s, ic, x + 0.1, y + (h - 0.4) / 2, 0.4, fill=col)
    text(s, x + 0.56, y + 0.06, w - 0.62, h - 0.12 if not sub else 0.34, title, 11.5, INK, bold=True, anchor="m" if not sub else "t",
         minpt=9, lh=1.0, autofit=False)
    if sub:
        text(s, x + 0.56, y + 0.38, w - 0.62, h - 0.42, sub, 8.5, MUTED, minpt=7, lh=1.0, autofit=False)


def ontology_loop(D):
    s = D.new(); header(D, s, KO, "Ontology-Driven Agents: Your Company Map Checks Every Move",
                        "A plain agent writes a query that looks right and is still wrong. An ontology-driven agent checks it against how your business fits together.")
    # the loop diagram (redrawn): ontology on top feeds query generation and enforcement
    card(s, 0.6, 2.3, 7.9, 3.95)
    G, Y, P, R, B_ = "E8F3EC", "FBF1DC", "EFEAF6", "F8E6E1", "E6EEF7"
    _node(s, 2.75, 2.45, 3.4, 0.72, "network", "Ontology", "Entities · relationships · constraints", P, PLUM)
    _node(s, 0.75, 3.75, 1.55, 0.72, "user", "User intent", None, B_, "4A78A8")
    _node(s, 2.65, 3.75, 1.75, 0.72, "brain", "Query generation", None, "E3F2F1", TEAL)
    _node(s, 4.65, 3.75, 2.0, 0.72, "shield", "Ontology check", "Validation and control", Y, AMBER)
    _node(s, 7.15, 3.75, 1.2, 0.72, "chart", "Result", None, G, "3F8F5A")
    _node(s, 4.55, 5.15, 2.2, 0.72, "chat", "Feedback", "Exact rule broken, machine-readable", R, RED)
    line(s, 4.45, 3.17, 4.45, 3.4, PLUM, 1.25, dash=True)          # ontology feeds both boxes
    line(s, 3.52, 3.4, 5.65, 3.4, PLUM, 1.25, dash=True)
    line(s, 3.52, 3.4, 3.52, 3.75, PLUM, 1.25, arrow=True, dash=True)
    line(s, 5.65, 3.4, 5.65, 3.75, PLUM, 1.25, arrow=True, dash=True)
    line(s, 2.3, 4.11, 2.65, 4.11, CHAR, 1.5, arrow=True)
    line(s, 4.4, 4.11, 4.65, 4.11, CHAR, 1.5, arrow=True)
    line(s, 6.65, 4.11, 7.15, 4.11, "3F8F5A", 1.75, arrow=True)
    text(s, 6.62, 3.82, 0.55, 0.25, "Valid", 8.5, "3F8F5A", bold=True, align="c", autofit=False)
    line(s, 5.65, 4.47, 5.65, 5.15, RED, 1.5, arrow=True)
    text(s, 5.72, 4.65, 0.8, 0.25, "Invalid", 8.5, RED, bold=True, autofit=False)
    line(s, 4.55, 5.51, 3.52, 5.51, RED, 1.5)                      # feedback returns to query generation
    line(s, 3.52, 5.51, 3.52, 4.47, RED, 1.5, arrow=True)
    text(s, 0.8, 5.25, 2.6, 0.85, "The agent fixes its own query until the ontology accepts it. Nothing wrong reaches you.", 10.5, MUTED,
         minpt=8.5, lh=1.05)
    # definition
    card(s, 8.75, 2.3, 3.95, 2.2, fill=CHAR)
    text(s, 9.0, 2.42, 3.5, 0.3, "ONTOLOGY-DRIVEN AGENT", 10, ACC, bold=True, autofit=False)
    text(s, 9.0, 2.78, 3.5, 1.65, "An AI agent that reasons, writes queries and acts through a structured model of your business, "
         "not through raw tables or patterns alone.", 14, WHITE, font=SERIF, minpt=11, lh=1.05)
    parts = [("ENTITIES", "What exists: client, building, contract, job, technician"),
             ("RELATIONSHIPS", "How they link: a job sits in a building under one contract"),
             ("CONSTRAINTS", "What must hold: 'closed' needs the client's confirmation")]
    for i, (h, d) in enumerate(parts):
        y = 4.62 + i * 0.55
        card(s, 8.75, y, 3.95, 0.48, shadow=False)
        text(s, 8.88, y + 0.05, 1.35, 0.38, h, 8.5, PLUM, bold=True, anchor="m", autofit=False)
        text(s, 10.2, y + 0.03, 2.45, 0.42, d, 9.5, INK, anchor="m", minpt=7.5, lh=1.0)
    tip(D, s, "Your Topic 2 company map is your ontology. Palantir AIP and Microsoft Fabric IQ (Nov 2025) put one under their agents.", y=6.38)
    text(s, 0.6, 6.82, 12.1, 0.22, "Sources: Palantir Foundry docs, The Ontology system · Microsoft Fabric blog, Introducing Microsoft Fabric IQ (Nov 2025)",
         8, MUTED, autofit=False)
    return s


def ontology_meridian(D):
    s = D.new(); header(D, s, KO + " at Meridian", "Same Question, Two Agents: Only One Gets It Right",
                        "The coordinator asks: “Which urgent jobs breached their response promise this week?” Both agents answer in seconds.")
    # left: plain agent
    card(s, 0.6, 2.3, 5.85, 3.2)
    text(s, 0.85, 2.42, 5.4, 0.3, "PLAIN AGENT · READS THE TABLES", 10, RED, bold=True, autofit=False)
    steps_l = [("Counts a job as done when status = 'done'", "The technician ticked it; the client never confirmed."),
               ("Applies the 4-hour promise to every urgent job", "Only Premium contracts carry 4 hours; Standard has 8."),
               ("Returns 19 jobs, neatly formatted", "Looks valid. Twelve are wrong. Nobody can tell.")]
    for i, (a, b) in enumerate(steps_l):
        y = 2.82 + i * 0.86
        circle(s, 0.85, y + 0.06, 0.4, RED)
        text(s, 0.85, y + 0.06, 0.4, 0.4, str(i + 1), 12, WHITE, bold=True, align="c", anchor="m", autofit=False)
        text(s, 1.42, y, 4.9, 0.36, a, 12.5, INK, bold=True, minpt=9.5, lh=1.0)
        text(s, 1.42, y + 0.36, 4.9, 0.4, b, 11, MUTED, minpt=8.5, lh=1.0)
    # right: ontology-driven agent
    card(s, 6.85, 2.3, 5.85, 3.2, fill=CHAR)
    text(s, 7.1, 2.42, 5.4, 0.3, "ONTOLOGY-DRIVEN AGENT · READS THE COMPANY MAP", 10, TEAL, bold=True, autofit=False)
    steps_r = [("Drafts the same query; the check rejects it", "Feedback: “Closed = technician sign-off AND client confirmation.”"),
               ("Rewrites it through the links", "Job → building → contract → SLA tier: 4 h Premium, 8 h Standard."),
               ("Returns 7 jobs, each traceable", "Every row shows the rule it was checked against.")]
    for i, (a, b) in enumerate(steps_r):
        y = 2.82 + i * 0.86
        circle(s, 7.1, y + 0.06, 0.4, TEAL)
        text(s, 7.1, y + 0.06, 0.4, 0.4, str(i + 1), 12, WHITE, bold=True, align="c", anchor="m", autofit=False)
        text(s, 7.67, y, 4.9, 0.36, a, 12.5, WHITE, bold=True, minpt=9.5, lh=1.0)
        text(s, 7.67, y + 0.36, 4.9, 0.4, b, 11, SOFT, minpt=8.5, lh=1.0)
    # bottom: actions are checked too + what to do on Monday
    w = (12.1 - 0.3) / 3
    rows = [("lock", "Actions, not just answers", "The agent tries to send an uncertified technician to a lift job. The constraint blocks it before dispatch."),
            ("file", "Written by the business", "Ops and account managers own the definitions. IT encodes them; the DRI signs off each change."),
            ("history", "Versioned like the SOP", "When a contract tier changes, update the map once; every agent follows it next morning.")]
    for i, (ic, t, d) in enumerate(rows):
        x = 0.6 + i * (w + 0.15)
        card(s, x, 5.65, w, 1.05)
        icon(s, ic, x + 0.16, 5.78, 0.44, fill=ACC)
        text(s, x + 0.72, 5.72, w - 0.82, 0.34, t, 13.5, INK, bold=True, font=SERIF, autofit=False)
        text(s, x + 0.72, 6.05, w - 0.82, 0.62, d, 10.5, MUTED, minpt=8.5, lh=1.03)
    text(s, 0.6, 6.82, 12.1, 0.22, "Meridian Services Pte Ltd is fictitious; all figures are synthetic.", 8, MUTED, autofit=False)
    return s


def ontology(D):
    ontology_loop(D)
    ontology_meridian(D)


# --- v56 (owner, 23 Nov 2026): five team padlets; QR + room code on the slide that opens each activity's group work
def padlet_teams(D, topic):
    import data_bi as B
    from slides_bi import qr
    q, pts = B.PADLET_TALK[topic]
    s = D.new(); header(D, s, f"Topic {topic} · Activity {topic} · Team padlet · 15 min", "Join Your Team Padlet: Talk First, Then Build",
                        ("You have seen Activity 1 and its BMC board. Talk for 15 minutes as a team of 3-5, then fill your own board." if topic == 1 else
                         "You have seen Activity 2 and its plan board. Talk for 15 minutes as a team of 3-5, then fill your own board." if topic == 2 else "You just saw Meridian fill each box. Talk for 15 minutes as a team of 3-5, then fill your own board."))   # v59 (owner): T1 padlet follows the board intro   # v57: demo -> padlet -> activity
    g = 0.18; w = (12.1 - 4 * g) / 5; top = 2.3
    for i, (team, code) in enumerate(B.PADLET_TEAMS):
        x = 0.6 + i * (w + g); dk = i % 2 == 0
        card(s, x, top, w, 2.95, fill=CHAR if dk else WHITE)
        text(s, x + 0.1, top + 0.12, w - 0.2, 0.42, "Team " + team, 17, WHITE if dk else INK, bold=True, font=SERIF, align="c", autofit=False)
        qr(s, B.PADLET_URL + code, x + (w - 1.55) / 2, top + 0.62, 1.55, dark=dk)
        text(s, x + 0.1, top + 2.3, w - 0.2, 0.5, code, 22, ACC, bold=True, font=MONO, align="c", anchor="m", autofit=False)
    card(s, 0.6, 5.42, 12.1, 0.95, shadow=False)
    text(s, 0.82, 5.5, 11.6, 0.3, "DISCUSS · 15 MIN · " + q.upper(), 9.5, ACC, bold=True, autofit=False)
    for k, ptxt in enumerate(pts):
        text(s, 0.82 + k * 3.95, 5.8, 3.75, 0.55, f"{k + 1}. {ptxt}", 11, INK, minpt=8.5, lh=1.02)
    tip(D, s, "Scan the QR or key in your team code at alfredang.github.io/padlet. One idea per card; board screenshots go in the last column.", y=6.5)
    return s


# ------------------------------------------------------------------ v57 (owner, 23 Nov 2026): the six AI Coaching profiles
# One overview and one page per worried employee of the AI Coaching simulator (data_bi.COACH_PROFILES). Sarah's page keeps the
# v54 worked-example title "From Campaign Producer to Marketing Owner".
KC = "Topic 3 · A · Job redesign · AI coaching"


def coach_overview(D):
    import data_bi as B
    s = D.new(); header(D, s, KC + " · six profiles", "Six People, Six Fears, Six Jobs Worth Keeping",
                        "Each fears the agent for a different reason. Each ends up owning a decision the agent cannot make.")
    g = 0.2; w = (12.1 - 2 * g) / 3; h = 1.88
    for i, p in enumerate(B.COACH_PROFILES):
        x = 0.6 + (i % 3) * (w + g); y = 2.3 + (i // 3) * (h + 0.16); dk = i in (0, 4)
        card(s, x, y, w, h, fill=CHAR if dk else WHITE)
        icon(s, p["ic"], x + 0.22, y + 0.22, 0.55)
        text(s, x + 0.92, y + 0.14, w - 1.05, 0.42, p["name"], 20, WHITE if dk else INK, bold=True, font=SERIF, autofit=False)
        text(s, x + 0.92, y + 0.52, w - 1.05, 0.3, p["role"], 12, SOFT if dk else MUTED, autofit=False)
        text(s, x + 0.22, y + 0.92, w - 0.44, 0.28, p["tension"].upper(), 9.5, ACC, bold=True, autofit=False)
        text(s, x + 0.22, y + 1.2, w - 0.44, 0.6, "Owns: " + p["own_short"], 12.5,
             WHITE if dk else INK, minpt=9, lh=1.02)
    tip(D, s, "One page per person follows: what they say, the strength to build on, the job they own and a safe two-week experiment.", y=6.45)
    return s


def coach_profile(D, i, p):
    s = D.new(); header(D, s, f"{KC} · profile {i} of 6 · {p['name']}", p["title"], p["sub"])
    top, hh = 2.35, 3.95
    card(s, 0.6, top, 4.5, hh, fill=CHAR)
    circle(s, 0.85, top + 0.25, 0.85, ACC)
    text(s, 0.85, top + 0.25, 0.85, 0.85, p["name"][0], 30, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
    text(s, 1.9, top + 0.24, 3.05, 0.45, p["name"], 22, WHITE, bold=True, font=SERIF, autofit=False)
    text(s, 1.9, top + 0.7, 3.05, 0.35, p["role"], 12.5, SOFT, autofit=False)
    text(s, 0.85, top + 1.32, 4.0, 0.28, "WHAT " + p["name"].upper() + " SAYS", 9.5, ACC, bold=True, autofit=False)
    text(s, 0.85, top + 1.62, 4.0, 2.1, "\u201c" + p["says"] + "\u201d", 17, WHITE, font=SERIF, italic=True, minpt=11, lh=1.1)
    rows = [("robot", "THE AGENT NOW DOES", p["agent"]),
            ("star", "STRENGTH TO BUILD ON, IN " + p["name"].upper() + "'S OWN WORDS", "\u201c" + p["strength"] + "\u201d"),
            ("flag", "THE JOB " + p["name"].upper() + " OWNS NOW", p["owns"]),
            ("calendar", "SAFE EXPERIMENT", p["trial"])]
    rh = (hh - 3 * 0.1) / 4
    for k, (ic, lab, body) in enumerate(rows):
        y = top + k * (rh + 0.1); hi = k == 2
        card(s, 5.35, y, 7.35, rh, fill=CREAM if hi else WHITE, shadow=not hi)
        icon(s, ic, 5.55, y + (rh - 0.5) / 2, 0.5, fill=TEAL if k == 1 else ACC)
        text(s, 6.25, y + 0.08, 6.3, 0.26, lab, 9.5, ACC if k != 1 else TEAL, bold=True, autofit=False)
        text(s, 6.25, y + 0.34, 6.3, rh - 0.4, body, 13.5, INK, minpt=9.5, lh=1.02)
    tip(D, s, f"Practise this conversation: alfredang.github.io/AICoaching, Demo mode, choose {p['name']}. Fictional profile.", y=6.48)
    return s


def coach_profiles(D):
    import data_bi as B
    coach_overview(D)
    for i, p in enumerate(B.COACH_PROFILES, 1):
        s = coach_profile(D, i, p)
        s.notes_slide.notes_text_frame.text = (f"Fictional profile from the AI Coaching simulator (github.com/alfredang/AICoaching, scenario '{p['name']}'). "
            "Quote = the simulator's opening line, cut with ellipses. Safe experiment = course suggestion. "
            + ("Worked example adapted from Dr Alfred Ang, Work Redesign for Managing AI Agents, 27 August 2026, page 9." if i == 1 else ""))
