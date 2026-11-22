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
    tip(D, s, "Do not default to the biggest model. Give each agent the smallest one that passes your checks; it is cheaper, faster and easier to control.", y=6.35)
    return s


def security6(D, kicker=None):
    """Overview, then one page per principle (owner, v54)."""
    s = overview(D)
    for f in (data_control, permission_control, guardrails, human_in_loop, traceability, right_sized):
        f(D)
    return s
