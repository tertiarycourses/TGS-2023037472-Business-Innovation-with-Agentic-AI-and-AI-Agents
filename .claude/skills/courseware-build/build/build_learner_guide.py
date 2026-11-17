#!/usr/bin/env python3
"""Learner Guide (LG) DOCX + Markdown mirror, from course_data + data_bi. Cover, Document Version Control
Record and TOC each on their own page. The LG carries the depth the slides leave out, including every
knowledge point the WA tests (K1-K6)."""
import os, re, sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
import data_bi as B
import prodoc
from version_history import ALL

REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
ASSETS = os.path.join(os.path.dirname(HERE), "assets"); IMG = os.path.join(REPO, "courseware", "assets")
X = []   # blocks
def h1(t): X.append(("h1", t))
def h2(t): X.append(("h2", t))
def h3(t): X.append(("h3", t))
def p(t): X.append(("p", t))
def bl(xs): X.append(("ul", list(xs)))
def ol(xs): X.append(("ol", list(xs)))
def tbl(hd, rows, w=None): X.append(("table", hd, rows, w))
def img(path, cap, w=6.0): X.append(("img", path, cap, w))
def note(t): X.append(("note", t))
def src(t): X.append(("src", t))

# ------------------------------------------------------------------ front matter
h1("About This Course")
p(f"{C.TITLE} ({C.COURSE_CODE}) is a two-day WSQ course for managers, business owners and innovation leads. {C.PITCH}")
tbl(["Item", "Details"], [("Course", C.TITLE), ("Course code", C.COURSE_CODE), ("Skills Framework TSC", f"{C.TSC_TITLE} ({C.TSC_CODE})"),
                          ("Duration", C.CONTACT_TIME_NOTE), ("Provider", f"{C.ORG} ({C.UEN})"),
                          ("Activity Studio", f"{B.BCM_URL} (no login)"), ("Your case", "Your own organisation, in every activity and in the PP")], [1.8, 4.9])
h2("Learning Outcomes")
bl([f"{lo} (In short: {C.LO_SHORT[i]}.)" for i, lo in enumerate(C.LEARNING_OUTCOMES)])
h2("Skills Framework: Abilities and Knowledge")
bl(C.TSC_ABILITIES + C.TSC_KNOWLEDGE)
h2("How the Course Runs")
tbl(["Topic", "Outcome", "Activity (Meta Muse + group board)", "Instructions"], [
    (f"1 · {C.TOPICS[0]['title']}", "LO1 · K1, K2, A1, A2", "Activity 1 · Business Model Canvas for AI Agents (PP Task 1)", "activities/activity-01"),
    (f"2 · {C.TOPICS[1]['title']}", "LO2 · K3, K4, A3, A4", "Activity 2 · AI Agent 90-Day Action Plan (PP Task 2)", "activities/activity-02"),
    (f"3 · {C.TOPICS[2]['title']}", "LO3 · K5, K6, A5, A6", "Activity 3 · Sustain and Operate, SCALE (PP Task 3)", "activities/activity-03")], [2.3, 1.3, 2.2, 0.9])
p("Every activity is done in groups of 3-5 on one shared online board in the Activity Studio: one member (or the trainer) creates it and everyone joins with the Board ID or QR code; edits sync live. Your group types its answers into each block, can view a short "
  "example from a fictional sample company, and can copy a ready-made Meta Muse prompt that drafts the whole board. At the end each member screenshots the group board or "
  "downloads it as PNG or PDF, pastes it into the Practical Performance assessment and answers the questions individually.")
note("Work on your own organisation. Never put personal data (NRIC, phone numbers, "
     "customer names) or confidential figures on a board: boards are shared by link.")

# ------------------------------------------------------------------ Topic 1
h1("Topic 1 — " + C.TOPICS[0]["title"])
p(C.LEARNING_OUTCOMES[0] + " (K1, K2, A1, A2)")
h2("1.1 A Short History of AI")
tbl(["Era", "When", "What changed"], [("Rules", "1950s-1980s", "Explicit if-then rules and expert systems; brittle outside their rules."),
     ("Learning", "1990s-2010s", "Machine learning finds patterns from examples; predictive AI scores and forecasts."),
     ("Language", "2017-2023", "The Transformer (2017) and large language models; ChatGPT (Nov 2022) brings chat to everyone."),
     ("Action", "2024 onward", "Models use tools, keep state and pursue goals: AI agents and agentic AI.")], [1.2, 1.2, 4.3])
p("These eras coexist: a modern agent still runs on ordinary software, business rules and databases.")
h3("2023 to 2026: four engineering lenses")
p("A teaching sequence of where practitioners focused their effort. The years are emphasis markers, not invention dates; each "
  "lens overlaps the others and each adds an architecture implication.")
tbl(["Lens", "Emphasis", "Architecture implication"], [
    ("Prompt engineering", "2023", "Specify goal, audience, format and examples; version prompts like code."),
    ("Context engineering", "2024", "Retrieve the right facts at the right time (RAG, memory); control what enters the context window."),
    ("Harness engineering", "2025", "Wire tools, state, permissions, checks and logs around the model so it can act safely."),
    ("AI agents", "2026", "Delegate outcomes; design human decision boundaries, evaluation and monitoring for autonomous work.")], [1.6, 0.8, 4.3])
h2("1.2 Agentic AI vs AI Agent")
tbl(["", "Agentic AI", "AI agent"], [("What it is", "The whole goal-directed system", "One worker with a defined job"),
     ("How it works", "Plans, acts, checks results and repeats; may coordinate many agents", "Model + tools + memory + instructions"),
     ("Example", "A triage workflow where several agents and humans hand work on", "Meta Muse, OpenAI Dots, a Hermes agent")], [1.2, 2.8, 2.7])
p("An always-on agent is an agent deployed to keep running between your messages: it watches an inbox or calendar and acts or "
  "alerts when something changes, within the permissions you give it.")
h2("1.3 Singapore Government News")
bl(["IMDA published the world's first Model AI Governance Framework for Agentic AI at Davos on 22 January 2026; version 1.5 (20 May 2026) "
    "folded in feedback from more than 60 organisations. Four dimensions: assess and bound the risks upfront; make humans meaningfully "
    "accountable; implement technical controls and processes; enable end-user responsibility.",
    "Enterprise Singapore's Champions of AI programme (27 October 2026) starts with 24 companies including DBS, OCBC, UOB, ST Engineering, "
    "Singapore Airlines and PSA, each building an enterprise-wide AI transformation roadmap. In its pilot, more than 280 small businesses "
    "applied agentic AI tools in marketing, sales and customer service.",
    "Synapxe's AgentSea platform (built with AWS) let public healthcare staff create more than 12,000 AI agents within three months of its "
    "May 2026 launch; over 80,000 healthcare professionals can build agents in plain language."])
src("IMDA, Artificial Intelligence in Singapore (imda.gov.sg); Enterprise Singapore media release, 27 Oct 2026; The Straits Times, 24 Aug 2026.")
h2("1.4 Always-On AI Agents: Meta Muse")
p("Meta Muse (in Singapore since 27 October 2026) is the always-on agent used in all three activities. It connects to Gmail and Google Calendar, "
  "keeps watch on your inbox, nudges you before deadlines, builds small apps called Spaces from one prompt, and asks before sending "
  "or buying anything. Use read-only connector access where offered and approve every send yourself.")
img(os.path.join(IMG, "ainative", "muse-productivity.png"), "Meta Muse productivity prompts (Muse app, Singapore, November 2026)", 2.4)
h2("1.5 Five Scenarios of Human-AI Agent Collaboration")
tbl(["Scenario", "What it looks like", "Where you see it"], [
    ("1 · One human, one agent", "A personal agent works your inbox and calendar overnight.", "Meta Muse, OpenAI Dots, Claude Duet"),
    ("2 · Many humans, one agent", "One front-line agent answers every customer and hands hard cases to people.", "Klarna's assistant: 2.3 million chats in its first month (Feb 2024)"),
    ("3 · One human, many agents", "Specialist agents work in parallel; the founder approves hand-offs.", "Research, writing and design agents run by one person"),
    ("4 · Many humans, many agents", "Everyone builds and runs agents toward shared goals.", "Singapore public healthcare: 12,000+ AgentSea agents"),
    ("5 · Company to company", "A buyer's agent negotiates with a supplier's agent; people sign off.", "Agents with their own email, phone and wallet")], [1.8, 2.7, 2.2])
h2("1.6 Why AI Projects Stall: Five Capability Gaps")
p("Deploy a model straight out of the box and five structural gaps appear at once:")
ol(["Private data: contracts, customer records and internal processes are blank to it.",
    "Internal language: 'active customer' or 'closed' may mean something different in your company.",
    "Live context: it does not know what changed a second ago.",
    "Ability to act: it has no permission to execute inside your systems.",
    "Guardrails: no permission controls, verification of results or audit trail."])
p("Like a brilliant graduate nobody onboards, the model stays stuck on day one. A business opportunity is viable only if you can close these gaps for it.")
h2("1.7 Investigating and Evaluating Opportunities (A1, A2)")
p("Analyse the business need before you pick technology. Gather evidence from five sources:")
tbl(["Evidence", "Questions", "Example (a service desk)"], [
    ("Stakeholders", "Who feels the pain? What does each want and fear?", "Clients chase job status; coordinators fear replacement."),
    ("Process", "Trigger, steps, hand-offs, waits, rework, decisions?", "6 steps, 3 hand-offs, 38% of time re-keying."),
    ("Data", "What data exists, is it clean, current and permitted?", "5 years of tickets; tenant phone numbers must be masked (PDPA)."),
    ("Requirements", "What must the solution do, testably, and who signs it off?", "Draft a ticket within 1 minute; coordinator approves urgent jobs."),
    ("Opportunity", "Which objective does it move, by how much, at what cost and risk?", "Handling time 18 to 11 minutes; same-day response objective.")], [1.3, 2.7, 2.7])
p("Score each idea on value, feasibility and data readiness (1-5 each) and check it serves an organisational objective. Set a veto: "
  "a score of 1 on data or risk stops the idea whatever the total. Four value levers: revenue, cost, risk and experience.")
h2("Activity 1 — Business Model Canvas for AI Agents with Meta Muse (PP Task 1)")
X.append(("canvas", "opportunity"))

# ------------------------------------------------------------------ Topic 2
h1("Topic 2 — " + C.TOPICS[1]["title"])
p(C.LEARNING_OUTCOMES[1] + " (K3, K4, A3, A4)")
h2("The 90-Day Action Plan: Five Steps to Get Started")
p("Topic 2 and Activity 2 follow one five-step plan. Each step is a numbered block on your action plan board.")
tbl(["Step", "What you do", "What you decide"], [(l, w, d) for l, w, d, _ in B.PLAN], [0.5, 1.6, 4.6])
h2("2.1 The Power of Dormant Data")
p("A company keeps two sets of records. The official set (reports, reviews, strategy papers) is polished and filtered. The second set "
  "records what actually happened: meeting audio, chat logs, edit history, customer tickets, code logs, photos and system logs. It is "
  "messy and honest, and until now too hard to read at scale. This is dormant data. Multimodal AI can now read text, audio, images, "
  "spreadsheets and logs together, so this record becomes usable.")
img(os.path.join(IMG, "ainative", "dormant-data.png"), "Awakening dormant data", 5.6)
h2("2.2 The Enterprise AI Decision Layer")
p("Four connected components turn data into intelligence across the whole company:")
tbl(["Component", "Role", "Why it matters"], [
    ("Brain: the model", "Reasons, infers and judges", "Commoditising fast; a better model alone moves performance from D to D+."),
    ("Map: the ontology", "Defines business terms, entities, relationships and rules", "Lets AI anchor every action in your business context; your moat."),
    ("Navigation: live context", "Tracks every event in real time", "The map shows what should happen; navigation shows what is happening."),
    ("Operating system", "Scheduling, execution, access, control", "Lets agents act within authorised, recorded and stoppable boundaries.")], [1.6, 2.2, 2.9])
img(os.path.join(IMG, "ainative", "decision-layer.png"), "The four core components of enterprise AI decision-making", 5.4)
h3("The operating system's four subsystems")
bl(["Scheduling: plans the order of work, divides it among agents and knows how to wait days for an approval, then resume.",
    "Execution: tests each action in a sandbox first, then runs an execute-check-correct loop.",
    "Access: a universal keycard to CRM, ERP, email and documents; the Model Context Protocol (MCP) lowers the cost of each connection.",
    "Control: an agent gets the same permissions as the person who asks; identities are fixed and every action is logged."])
h2("2.3 Drawing the Company Map")
p("An ontology, or company map, is a semantic structure that defines key business terms (what a customer, contract or approval is) and "
  "how they relate. It covers people, customers, products, orders, contracts, approval flows and business rules. Without it a model "
  "cannot see why active customers are tied to payment terms, or why three more approvals follow a signed contract. Build it in "
  "layers: data sources, data models, business rules, relationships. Today it can be drawn and revised in plain language by the people "
  "who run the business (ontology 2.0), instead of taking 6-18 months of specialist work.")
p("In Activity 2 you ask Meta Muse to draft a company map for one of your own processes; your action plan builds on it.")
h2("2.4 Step 1: Mine the Business Process")
ol(["Pick one process that hurts every week.", "Pull its trail from dormant data: emails, tickets, logs, chats, meeting notes.",
    "Rebuild the real steps: trigger, actors, hand-offs, systems.", "Measure waits, rework and touch time against a baseline.",
    "Mark every decision: who judges, on what evidence, under which rule."])
h2("2.5 Step 2: Where Agentic AI and AI Agents Integrate")
p("Classify each step by how much the AI may do, and name the accountable human for each. This is the human decision boundary.")
tbl(["Level", "The AI…", "The human…"], [("Inform", "summarises or alerts", "decides everything"), ("Recommend", "ranks and suggests", "chooses"),
     ("Prepare", "drafts the ticket, reply or report", "edits and approves"), ("Execute with approval", "acts after a yes", "approves each action"),
     ("Execute with monitoring", "acts on its own", "audits samples and exceptions")], [1.8, 2.4, 2.5])
p("Choose the simplest pattern that works: deterministic automation, a grounded assistant (RAG), an agentic workflow with fixed steps, "
  "a single agent that chooses its steps, or a multi-agent team with a coordinator. More autonomy needs more controls.")
h2("2.6 Business Planning Methods for Agentic AI (K3)")
bl(["Business Model Canvas: re-read each block for agent opportunities (Activity 1).",
    "Outcome contract: population, baseline, target, owner and counter-metric agreed before building. Example (a service desk): 10,000 eligible requests (of 28,800 a year), "
    "18-minute baseline, at most 11 minutes by day 90, owned by the Head of Service Desk, complaints held at or below 2%.",
    "Evidence-based option comparison: compare options on the same criteria and evidence, not on demos.",
    "Decision rights: who may decide, approve or override, written down before go-live."])
h2("2.7 Digital Architecture: Custom, Buy or Hybrid (K4, A3)")
tbl(["Layer", "What it holds"], [("Data", "Sources, quality, permissions, dormant data"), ("Model", "The chosen model(s) and their limits"),
     ("Orchestration", "Workflow, agents, memory, tools (MCP)"), ("Application", "Where people meet the AI: email, portal, chat"),
     ("Governance", "Access control, approvals, logs, evaluation, monitoring")], [1.5, 5.2])
p("Draw trust boundaries where data or actions cross systems or organisations; apply least privilege at each boundary. Decide custom, "
  "buy or hybrid on differentiation, time to value, integration fit, assurance, three-year total cost of ownership (licences, build, run, "
  "change, incidents) and an exit option. Most firms buy the platform and own the company map and rules.")
h2("Activity 2 — AI Agent 90-Day Action Plan with Meta Muse (PP Task 2)")
X.append(("canvas", "actionplan"))

# ------------------------------------------------------------------ Topic 3
h1("Topic 3 — " + C.TOPICS[2]["title"])
p(C.LEARNING_OUTCOMES[2] + " (K5, K6, A5, A6)")
h2("The SCALE Framework: Five Moves to Sustain and Operate")
p("Topic 3 and Activity 3 follow one framework. Each move is a block on your SCALE board.")
tbl(["", "Move", "What you do"], [(l, w, d) for l, w, d, _ in B.SCALE], [0.4, 1.5, 4.8])
h2("3.1 The Flattened Org Chart and the DRI")
img(os.path.join(IMG, "ainative", "flattened-org.png"), "Rewrite companies in a flattened org chart", 5.4)
p("A Directly Responsible Individual (DRI), a term from Apple, is the one person accountable for an outcome: singular (one named "
  "person, not a committee), accountable (owns the outcome, not just the task) and holding the decision rights (commands the AI "
  "workforce). DRIs carry responsibility to the end, are self-driven, coordinate without formal authority and now command agents. "
  "Agents supply capability; the DRI supplies accountability.")
h3("Flatten smart, not by decree")
p("Block laid off about 4,000 people (nearly 40%) at once; about 30% of Zappos staff left after the Holacracy ultimatum in 2015; Google "
  "removed engineering managers in 2001 and reinstated them within months. Flattening by decree wipes institutional memory. The right "
  "order: preserve and codify the knowledge in the decision layer first, then simplify the hierarchy. Bayer cut from 12-13 layers to 6-7 "
  "over a planned three-year journey.")
ol(["Codify tacit know-how into the company map and skills.", "Run a business scenario test: real access to agents, a small valuable task, four "
    "boundaries (goal, time, data, token spend).", "Spot the builders; they are your first DRIs.",
    "Give each DRI matching decision rights and resource rights.", "Let relay layers fade as more DRIs emerge."])
tbl(["Type seen in the test", "What to do"], [("Learners: use AI as a better search", "Give time and coaching"),
     ("Followers: forward unchecked 'workslop'", "Do not mistake it for productivity"), ("Irreplaceable experts", "Pair with tool users; extract their knowledge"),
     ("Builders: become a small team at once", "Your first DRIs; give them authority to match")], [3.2, 3.5])
h2("3.2 A New Workforce and Tomorrow's Managers")
tbl(["Role", "Outlook"], [("Amplified commander (DRI)", "Manages many agents, raises output tenfold; most valuable"),
     ("Human-to-human work", "Trust, warmth, negotiation, calming a customer; endures"), ("Rubber-stamp manager", "Signs off AI output without judging; hollowed out"),
     ("Rule-bound, predictable work", "AI already does it better, faster, cheaper; reskill")], [2.4, 4.3])
p("Managers move from relaying information to judgement: the judge at scale who owns outcomes for agents and people; the coach who "
  "teaches teams to work with agents; the translator and connector who moves tacit knowledge into the system during transition. The "
  "manager who only holds meetings and passes on approvals is most exposed.")
h2("3.3 The Learner's Advantage and the Atrophy Trap")
p("Stanford and MIT researchers tracking more than 5,000 customer-service agents found AI help raised issues resolved per hour by over "
  "10%, and by over 30% for new and weaker staff; a two-month hire performed like a six-month one. The difference that matters now is "
  "appetite for mental effort. But judgement decays with disuse: doctors' detection of precancerous lesions fell from 28.4% to 22.4% after "
  "the AI tool was removed, and people accepted planted wrong AI answers 80% of the time (Wharton). Ask for hints before answers, write "
  "your position first, and keep some work unassisted.")
h2("3.4 Implementation Best Practice and Reviewing Success (K5, A5)")
bl(["Start narrow with one high-value process, a measured baseline and a named DRI.", "Keep a real human checkpoint for the first 90 days.",
    "Measure offline quality before launch and online telemetry after: cycle time, first-pass accuracy, complaints, adoption, cost per outcome.",
    "Review at a fixed gate and decide scale, redesign, hold or stop on pre-agreed criteria."])
R = C.ROI_CASE
tbl(["Day-90 metric", "Target", "Result"], [("Mean handling time", "≤ 11 min", "10.7 min"), ("Quality", "≥ 94%", "95.1%"),
     ("Complaints", "≤ 2%", "1.7%"), ("Sustained use", "≥ 70%", "77.5%"), ("Critical unsafe actions", "0", "0"),
     ("Realised benefit vs year-1 cost", "benefit ≥ cost", f"SGD {R['day90_benefit']:,} vs SGD {R['first_year_cost']:,}")], [2.6, 2.0, 2.1])
p("ROI = (realised benefit - cost) / cost. Here year-1 ROI is close to zero but recurring costs are lower, so the case for scaling rests on "
  "year 2 and on keeping quality. Always add a downside case (lower adoption, smaller time saving).")
h2("3.5 Legal, Ethical and Security Issues (K6)")
bl(["PDPA: collect and use personal data only for notified purposes; mask personal data before analysis; follow the PDPC Advisory "
    "Guidelines on Use of Personal Data in Generative AI (2026).", "IMDA Model AI Governance Framework for Agentic AI: bound the risk, keep "
    "humans meaningfully accountable, apply technical controls, enable users. CSA's Securing Agentic AI addendum (June 2026) adds security controls.",
    "Prompt injection: a poisoned email or web page gives the agent orders; treat external content as data, never instructions.",
    "Data leakage and shadow AI: approved tools only; no confidential data in personal accounts.",
    "Accountability: the organisation stays responsible for its agents' actions; keep an audit trail of who asked what and when.",
    "Ethics: transparency, fairness, explainability, human oversight; tell customers when they are dealing with an agent."])
h2("3.6 Facilitating Information Flow Among Stakeholders (A6)")
p("In an AI-native firm, information flows through the DRI and the decision layer instead of up and down ten layers. Set an operating "
  "rhythm: a daily 8:00 exceptions brief from the agents, a weekly DRI review with the team, a monthly one-page dashboard for the sponsor. "
  "Communicate the change per stakeholder (what changes, what does not, who to ask), and run an idea pipeline where anyone can post an "
  "idea, the agent clusters them, and the best get a DRI and 30 days.")
h2("Activity 3 — Sustain and Operate with AI Agents (SCALE) with Meta Muse (PP Task 3)")
X.append(("canvas", "change"))

# ------------------------------------------------------------------ labs
h1("Assessment Preparation")
bl([C.ASSESSMENT["written"], C.ASSESSMENT["practical"], "Bring your three board screenshots (or PDFs): Activity 1, Activity 2 and Activity 3.",
    "Open book: slides, this Learner Guide and your boards. " + C.ASSESSMENT["note"]])
h1("Glossary")
tbl(["Term", "Meaning"], [("Agentic AI", "A goal-directed AI system that plans, acts with tools, checks results and repeats"),
     ("AI agent", "One AI worker: a model with tools, memory and instructions"), ("Always-on agent", "An agent that keeps running and watching between your messages"),
     ("Dormant data", "Unused operational records: calls, chats, tickets, logs, edit history"), ("Ontology / company map", "Definitions of business terms, entities, relationships and rules"),
     ("Decision layer", "Model + company map + live navigation + operating system"), ("DRI", "Directly Responsible Individual: the one person accountable for an outcome"),
     ("MCP", "Model Context Protocol: a standard way to connect agents to business systems"), ("Outcome contract", "Population, baseline, target, owner, counter-metric"),
     ("TCO", "Total cost of ownership over three years"), ("Atrophy trap", "Losing judgement by always deferring to AI")], [1.8, 4.9])
h1("References")
bl(["IMDA, Model AI Governance Framework for Agentic AI v1.5 (20 May 2026).", "Enterprise Singapore, media release on AI initiatives (27 Oct 2026).",
    "The Straits Times, 24 Aug 2026: New platform to create AI agents available to all public healthcare professionals.",
    "Meta Newsroom, Muse in Singapore (27 Oct 2026); Meta Help, Connectors.", "Klarna press release, Feb 2024: AI assistant handles two-thirds of customer service chats."])

# ------------------------------------------------------------------ canvas renderer helper (MD + DOCX share the data)
def canvas_rows(key):
    cv = B.CANVAS[key]
    return cv, [(b["title"], b["prompt"], "; ".join(f"{t}: {d}".rstrip(".") for t, d in b["example"]) + ".") for b in cv["blocks"]]

def lab_of(key): return next(L for L in B.LABS if L["canvas"] == key)
def step_prompt(L, st): return B.CANVAS[L["canvas"]]["muse_prompt"] if st.get("prompt") == "BOARD" else st.get("prompt")
# ------------------------------------------------------------------ Markdown mirror
def md():
    o = [f"# Learner Guide — {C.TITLE}", "", f"**{C.COURSE_CODE} · Version {C.VERSION.lstrip('v')} · {C.VERSION_DATE} · {C.ORG}**", ""]
    for b in X:
        k = b[0]
        if k in ("h1", "h2", "h3"): o += ["#" * int(k[1]) + " " + b[1], ""]
        elif k == "p": o += [b[1], ""]
        elif k == "note": o += ["> " + b[1], ""]
        elif k == "src": o += ["*Source: " + b[1] + "*", ""]
        elif k == "ul": o += [f"- {x}" for x in b[1]] + [""]
        elif k == "ol": o += [f"{i+1}. {x}" for i, x in enumerate(b[1])] + [""]
        elif k == "table":
            o += ["| " + " | ".join(b[1]) + " |", "|" + "---|" * len(b[1])] + ["| " + " | ".join(str(c) for c in r) + " |" for r in b[2]] + [""]
        elif k == "img": o += [f"*[Figure: {b[2]}]*", ""]
        elif k == "prompt": o += ["```text", b[1], "```", ""]
        elif k == "canvas":
            cv, rows = canvas_rows(b[1]); L = lab_of(b[1])
            o += [L["goal"], ""]
            for i, st in enumerate(L["steps"]):
                o += [f"**Step {i + 1} — {st['title']}**", ""] + [f"- {x}" for x in st["body"]] + ([f"- {a}: {u}" for a, u in B.MUSE_LINKS] if st.get("links") == "MUSE" else []) + [""]
                if step_prompt(L, st): o += ["```text", step_prompt(L, st), "```", ""]
                if st.get("check"): o += [f"Check: {st['check']}", ""]
            o += [cv["pitch"], "", f"Board: {B.BCM_URL}?activity={cv['key']} · {cv['minutes']} min · {cv['evidence']}", "",
                  "Discuss: " + " ".join(cv["discuss"]), "", "| Block | Question | Example (fictional sample company) |", "|---|---|---|"]
            o += [f"| {a} | {q} | {e} |" for a, q, e in rows] + [""]
    return "\n".join(o)
open(os.path.join(REPO, f"LG-{C.SHORT_TITLE}.md"), "w", encoding="utf-8").write(md())

# ------------------------------------------------------------------ DOCX
doc = Document(); st = doc.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc, "Learner Guide", C.TITLE, C.VERSION.lstrip("v"), org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc, ALL)
prodoc.add_toc(doc)
def table(hd, rows, w):
    t = doc.add_table(rows=1, cols=len(hd)); t.style = "Table Grid"
    for i, h in enumerate(hd):
        c = t.rows[0].cells[i]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = RGBColor(255, 255, 255)
        prodoc._shade_cell(c, "1F6FEB")
    for row in rows:
        cs = t.add_row().cells
        for i, v in enumerate(row):
            cs[i].text = ""; r = cs[i].paragraphs[0].add_run(str(v)); r.font.size = Pt(9.5)
    if w: prodoc.set_widths(t, w)
    doc.add_paragraph()
for b in X:
    k = b[0]
    if k in ("h1", "h2", "h3"): doc.add_heading(b[1], level=int(k[1]))
    elif k == "p": doc.add_paragraph(b[1])
    elif k == "note":
        r = doc.add_paragraph().add_run("Note: " + b[1]); r.italic = True
    elif k == "src":
        r = doc.add_paragraph().add_run("Source: " + b[1]); r.font.size = Pt(9); r.font.color.rgb = RGBColor(0x55, 0x5B, 0x66)
    elif k == "ul":
        for x in b[1]: doc.add_paragraph(x, style="List Bullet")
    elif k == "ol":
        for i, x in enumerate(b[1]): doc.add_paragraph(f"{i+1}. {x}")
    elif k == "table": table(b[1], b[2], b[3])
    elif k == "img":
        if os.path.exists(b[1]):
            doc.add_picture(b[1], width=Inches(b[3]))
            r = doc.add_paragraph().add_run(b[2]); r.italic = True; r.font.size = Pt(9)
    elif k == "prompt":
        pp = doc.add_paragraph(); r = pp.add_run(b[1]); r.font.name = "Consolas"; r.font.size = Pt(9.5)
        prodoc._shade_cell if False else None
    elif k == "canvas":
        cv, rows = canvas_rows(b[1]); L = lab_of(b[1])
        doc.add_paragraph(L["goal"])
        doc.add_paragraph(f"Group board: {B.BCM_URL}?activity={cv['key']}  ·  {L['minutes']} min  ·  {cv['evidence']}  ·  prompt templates: {B.BCM_URL}prompts.html")
        for i, st in enumerate(L["steps"]):
            hp = doc.add_paragraph(); hr = hp.add_run(f"Step {i + 1} — {st['title']}"); hr.bold = True
            for x in st["body"]: doc.add_paragraph(x, style="List Bullet")
            if st.get("links") == "MUSE":
                for lab_, url in B.MUSE_LINKS: doc.add_paragraph(f"{lab_}: {url}", style="List Bullet")
            if step_prompt(L, st):
                pp = doc.add_paragraph(); rr = pp.add_run(step_prompt(L, st)); rr.font.name = "Consolas"; rr.font.size = Pt(9)
            if st.get("check"):
                cr = doc.add_paragraph().add_run("Check: " + st["check"]); cr.italic = True
        doc.add_paragraph("Discuss in your team:")
        for q in cv["discuss"]: doc.add_paragraph(q, style="List Bullet")
        table(["Block", "Question", "Example (fictional sample company)"], rows, [1.5, 2.2, 3.0])
prodoc.add_page_numbers(doc); prodoc.enable_update_fields(doc)
OUT = os.path.join(REPO, "courseware", f"LG-{C.SHORT_TITLE}.docx")
doc.save(OUT); print("Saved", OUT)
