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
def prompt(t): X.append(("prompt", t))

# ------------------------------------------------------------------ front matter
h1("About This Course")
p(f"{C.TITLE} ({C.COURSE_CODE}) is a two-day WSQ course for managers, business owners and innovation leads. {C.PITCH}")
tbl(["Item", "Details"], [("Course", C.TITLE), ("Course code", C.COURSE_CODE), ("Skills Framework TSC", f"{C.TSC_TITLE} ({C.TSC_CODE})"),
                          ("Duration", C.CONTACT_TIME_NOTE), ("Provider", f"{C.ORG} ({C.UEN})"),
                          ("Activity Studio", f"{B.BCM_URL} (no login)"), ("Your case", "Your own organisation, in every activity and in the PP"), ("Worked demo", "Meridian Services Pte Ltd (fictitious): one scenario per topic and a filled demo board per activity")], [1.8, 4.9])
h2("Learning Outcomes")
bl([f"{lo} (In short: {C.LO_SHORT[i]}.)" for i, lo in enumerate(C.LEARNING_OUTCOMES)])
h2("Skills Framework: Abilities and Knowledge")
bl(C.TSC_ABILITIES + C.TSC_KNOWLEDGE)
h2("How the Course Runs")
p("Use the current prompts: download activities/prompts.html from the LMS course materials or the course Activities folder, then open the downloaded file in a browser. It includes the early Muse mini activity and all three group activities. Fill the blanks, Copy prompt, then paste into Muse. The prompt text is also printed in this guide and the activity Instructions PDFs.")
tbl(["Topic", "Outcome", "Activity (Meta Muse + group board)", "Instructions"], [
    (f"1 · {C.TOPICS[0]['title']}", "LO1 · K1, K2, A1, A2", "Activity 1 · Business Model Canvas for AI Agents (PP Task 1)", "activities/activity-01"),
    (f"2 · {C.TOPICS[1]['title']}", "LO2 · K3, K4, A3, A4", "Activity 2 · AI Agent 90-Day Action Plan (PP Task 2)", "activities/activity-02"),
    (f"3 · {C.TOPICS[2]['title']}", "LO3 · K5, K6, A5, A6", "Activity 3 · Sustain and Operate, SCALE (PP Task 3)", "activities/activity-03")], [2.3, 1.3, 2.2, 0.9])
p("Every activity is done in groups of 3-5 on one shared online board in the Activity Studio: one member (or the trainer) creates it and everyone joins with the Board ID or QR code; edits sync live. Your group types its answers into each block, can view a short "
  "example from Meridian Services, a fictitious worked-demo company, or open Meridian's full demo board, and can copy a ready-made Meta Muse prompt that drafts the whole board. At the end each member screenshots the group board or "
  "downloads it as PNG or PDF, pastes it into the Practical Performance assessment and answers the questions individually.")
note("Work on your own organisation. Never put personal data (NRIC, phone numbers, "
     "customer names) or confidential figures on a board: boards are shared by link.")
note("SkillsFuture free AI subscription: Singapore Citizens aged 18+ who attend an eligible course (look for the official \u201cFree AI sub\u201d "
     "label) receive a notification to redeem one free six-month AI subscription. The eligible course end date is 16 Sep 2026 or later; submit "
     "within 60 days of the notification. Official guide: https://www.myskillsfuture.gov.sg/content/portal/en/career-resources/career-resources/"
     "education-career-personal-development/redeem-ai-subscription.html")

# ------------------------------------------------------------------ Topic 1
h1("Topic 1 — " + C.TOPICS[0]["title"])
p(C.LEARNING_OUTCOMES[0] + " (K1, K2, A1, A2)")
h2("1.1 A Short History of AI")
tbl(["Approach", "Wider adoption (illustrative)", "What changed"], [
    ("Rules", "1950s-1980s", "People write explicit if-then rules and expert systems."),
    ("Machine Learning", "1990s-2000s", "Algorithms learn patterns from training examples for predictions or classifications."),
    ("Deep Learning", "2010s", "Multi-layer neural networks learn useful features; ImageNet (2012) is a landmark."),
    ("LLM", "2020s", "Large language models learn language patterns at scale; GPT-3 (2020) is a landmark.")], [1.35, 1.45, 3.9])
p("This is a teaching progression of wider adoption, not a claim about invention dates. Machine learning and neural networks began earlier. Deep learning is a form of machine learning, and modern LLMs use deep neural networks. The approaches coexist: an agent may still use business rules, conventional software and databases.")
src("Krizhevsky et al., ImageNet Classification with Deep Convolutional Neural Networks (2012), proceedings.neurips.cc; Brown et al., Language Models are Few-Shot Learners (2020), https://arxiv.org/abs/2005.14165 ; IBM, History of Artificial Intelligence (checked 18 Nov 2026).")
h3("2023 to 2026: four engineering lenses")
p("A teaching sequence of where practitioners focused their effort. The years are emphasis markers, not invention dates; each "
  "lens overlaps the others and each adds an architecture implication.")
tbl(["Lens", "Emphasis", "Architecture implication"], [
    ("Prompt engineering", "2023", "Specify goal, audience, format and examples; version prompts like code."),
    ("Context engineering", "2024", "Retrieve the right facts at the right time (RAG, memory); control what enters the context window."),
    ("Harness engineering", "2025", "Wire tools, state, permissions, checks and logs around the model so it can act safely."),
    ("AI agents", "2026", "Delegate outcomes; design human decision boundaries, evaluation and monitoring for autonomous work.")], [1.6, 0.8, 4.3])
h3("The Agent Stairway: From Answers to Results")
tbl(["Level", "How the work is shared"], [("Chatbot", "Answers a message; no business-system action is configured in this example."),
    ("Task bot", "Performs one defined job within clear instructions."), ("Copilot", "Suggests or prepares work while a person steers and approves."),
    ("Autonomous agent", "Pursues a delegated goal using tools, checks and escalation rules.")], [1.5, 5.2])
h2("1.2 Always-On AI Agents: A Specialised Form of Agentic AI")
tbl(["", "Agentic AI", "Always-on AI agent"], [
    ("What it is", "The broad class of goal-directed AI that plans, uses tools and checks results", "A specialised persistent implementation of those capabilities"),
    ("When it runs", "May be started for one task or deployed as a continuing service", "Keeps monitoring between user messages through event or schedule triggers"),
    ("How it behaves", "Plans, acts, checks and repeats within defined limits", "Maintains state, watches for work, performs permitted tasks and escalates for approval")], [1.2, 2.8, 2.7])
p("This course focuses on the ALWAYS ON class: agents deployed to keep watching and working between your requests. More generally, an AI agent is a concrete software worker built with agentic capabilities; it can also be invoked for a single task. Persistence is a deployment choice, rather than a defining requirement of every AI agent. Examples here include an inbox watcher or an agent that checks deadlines on a schedule, within the permissions you give it.")
src("Anthropic, Building effective agents: https://www.anthropic.com/research/building-effective-agents (checked 18 November 2026).")
h3("How an AI Agent Works")
p("Give an agent a goal and boundaries. It uses relevant context and memory, selects a permitted tool, checks the result and decides the next step or escalates. For a service request it can extract the site and fault, draft a ticket and check required fields; a coordinator approves urgent routing. Autonomy depends on granted permissions and controls.")
h3("Seven Components of an AI Agent")
tbl(["Component", "What it does"], [(name, role) for _, name, role in B.AGENT_COMPONENTS], [2.0, 4.7])
h3("Mini Activity: Try Meta Muse (20 minutes)")
p("Try Meta Muse right after learning how an AI agent works. Spend 20 minutes on setup, access and a read-only inbox brief.")
for i, step in enumerate(B.MINI_MUSE["steps"]):
    h3(f"Mini step {i + 1}: {step['title']}")
    bl(step["body"])
    if step.get("links") == "MUSE": bl([f"{label}: {url}" for label, url in B.MUSE_LINKS])
    prompt(step["prompt"])
    p("Check: " + step["check"])
p("Debrief: what did the agent know, which access did it need, and which decision stayed with you? Use your own authorised account or the trainer's non-confidential demonstration; do not use another learner's login.")
h2("1.3 Always-On AI Agents: Meta Muse, OpenAI Dots, Claude Duet, Grok Bot, Manus Cue")
p("Meta Muse (in Singapore since 27 October 2026) is the always-on agent used in all three activities. It connects to Gmail and Google Calendar, "
  "keeps watch on your inbox, nudges you before deadlines, builds small apps called Spaces from one prompt, and asks before sending "
  "or buying anything. Use read-only connector access where offered and approve every send yourself.")
img(os.path.join(IMG, "ainative", "muse-productivity.png"), "Meta Muse productivity prompts (Muse app, Singapore, November 2026)", 2.4)
p("Deployment has moved from a harness you run yourself (OpenClaw: local or server tools and channels you wire up), to self-hosted agents "
  "on your own machine (for example Hermes Agent: local workflow, memory and reusable skills), to hosted personal agents that a provider runs for you in "
  "the cloud. This is a progression in deployment choices, not a product lineage: pick the level of control your business needs.")
tbl(["Agent", "What it does", "How to get it"], [
    ("Meta Muse (Meta)", "Manages email, schedules and goals; asks before sending or buying; Gmail, Google Calendar and Instagram connectors.",
     "In Singapore since 27 Oct 2026; core use is free, with optional subscriptions: Muse app (iOS / Android) or muse.ai."),
    ("OpenAI Dots (OpenAI)", "Ongoing responsibilities on its own cloud computer; plugins for email, calendar and files; schedules and an Activity view.",
     "Rolling out to ChatGPT Pro and Business Premium."),
    ("Claude Duet (Anthropic)", "A morning brief, then checks every few hours; 6,000+ connectors; shows exactly what it will send, pay or sign and waits.",
     "Research preview (21 Oct 2026): US Pro/Max via waitlist."),
    ("Grok Bot (xAI)", "A persistent cloud computer shared by your bots; apps, MCP and its own @mail.grokbot.com inbox; Auto Review gates sends.",
     "x.ai/bot desktop or mobile app; check your plan's access."),
    ("Manus Cue (Manus)", "Agents with their own email, phone number, wallet and computer; calls, bookings and capped payments; agent teams in a group chat.",
     "Early access since 28 Sep 2026: free with an invite code at cue.im (web, desktop, Android).")], [1.4, 3.3, 2.0])
p("Compared side by side: Meta Muse and OpenAI Dots run a single agent; Grok Bot and Manus Cue run teams of agents; Anthropic has not said "
  "for Claude Duet. Muse's core use is free in Singapore and Cue is free for now with an invite code; Dots, Grok Bot and Duet need paid "
  "plans. Models and prices were checked on 31 Oct and 1 Nov 2026, and vendors change both without notice.")
src("Meta Newsroom, 27 Oct 2026; ChatGPT Learn: Get started with your dot; Anthropic: Introducing Claude Duet; xAI docs: Grok Bot computer and apps; cue.im; BULDRR comparison, 22 Oct 2026.")
h2("1.4 Singapore Government News")
bl(["IMDA published the world's first Model AI Governance Framework for Agentic AI at Davos on 22 January 2026; version 1.5 (20 May 2026) "
    "folded in feedback from more than 60 organisations. Four dimensions: assess and bound the risks upfront; make humans meaningfully "
    "accountable; implement technical controls and processes; enable end-user responsibility.",
    "Enterprise Singapore's Champions of AI programme (27 October 2026) starts with 24 companies including DBS, OCBC, UOB, ST Engineering, "
    "Singapore Airlines and PSA, each building an enterprise-wide AI transformation roadmap. In its pilot, more than 280 small businesses "
    "applied agentic AI tools in marketing, sales and customer service.",
    "Synapxe's AgentSea platform (built with AWS) let public healthcare staff create more than 12,000 AI agents within three months of its "
    "May 2026 launch; over 80,000 healthcare professionals can build agents in plain language, and 300+ agents are shared for colleagues "
    "to reuse. A National Heart Centre cardiologist's agent summarises patient histories before clinic, halving 40+ minutes of daily "
    "pre-clerking; KK Women's and Children's Hospital uses an agent to generate daily staff rosters. Guardrails reject requests for card or "
    "ID numbers, and MOH's AI in Healthcare Guidelines keep professional judgment with people: agents prepare the work, clinicians decide."])
src("IMDA, Artificial Intelligence in Singapore (imda.gov.sg); Enterprise Singapore media release, 27 Oct 2026; The Straits Times, 24 Aug 2026.")
h3("Recent Breakthroughs in Science and Mathematics")
p("After the Singapore healthcare example, consider research teams using agents to search, critique and test ideas. These cases were checked against primary announcements on 18 November 2026:")
bl(["Navier–Stokes, one of the seven Millennium Prize Problems: OpenAI published a reported singularity proof in September 2026. Clay lists the problem Active; formal verification and prize recognition are separate validation stages.",
    "Mathematics: Google reported a Courtade–Kumar conjecture proof with Lean verification on 13 November 2026.",
    "Molecular chemistry: Google's same report describes a 30-agent structure-search workflow reaching 95% first-choice accuracy on a benchmark.",
    "Life sciences: Co-Scientist generates, debates and ranks hypotheses; a 19 May 2026 report describes liver-fibrosis drug-repurposing candidates followed by laboratory tests."])
p("The transferable business pattern is parallel exploration plus an independent test: proof software, a measured benchmark or a laboratory experiment. Establish what was tested and who accepts the result before scaling the workflow.")
src("OpenAI: https://openai.com/index/navier-stokes-solution/ ; Clay: https://www.claymath.org/millennium/navier-stokes-equation/ ; Google Research: https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/ ; Google DeepMind: https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/ .")
h2("1.5 Five Scenarios of Human-AI Agent Collaboration")
tbl(["Scenario", "What it looks like", "Where you see it"], [
    ("1 · One human, one agent", "A personal agent works your inbox and calendar overnight.", "Meta Muse, OpenAI Dots, Claude Duet"),
    ("2 · Many humans, one agent", "One front-line agent answers every customer and hands hard cases to people.", "Klarna's assistant: 2.3 million chats in its first month (Feb 2024)"),
    ("3 · One human, many agents", "Specialist agents work in parallel; the founder approves hand-offs.", "Research, writing and design agents run by one person"),
    ("4 · Many humans, many agents", "Everyone builds and runs agents toward shared goals.", "Singapore public healthcare: 12,000+ AgentSea agents"),
    ("5 · Company to company", "A buyer's agent negotiates with a supplier's agent; people sign off.", "Agents with their own email, phone and wallet")], [1.8, 2.7, 2.2])
h3("One-Person Companies: Evidence and Outlook")
p("For this course, an AI-enabled one-person company is a founder using agents and software to run several functions. It is not interchangeable with a legal single-member company, a sole-proprietor registration, an own-account worker or an OPC community.")
tbl(["Location / measure", "Observed change", "Interpretation"], [("Singapore: resident regular primary own-account workers", "169,000 in 2024 to 179,200 in 2025 (+6.0%, calculated)", "Worker proxy, not an AI-OPC company count; no exponential company-growth conclusion."), ("China: OPC support communities", "95 to 618 in H1 2026 (6.5 times, calculated)", "Reported ecosystem expansion, not growth in the number or revenue of solo firms.")], [2.3, 2.0, 2.4])
p("Forward-looking example: Suzhou's official 2025–2028 action plan targets 1,000 new OPC enterprises and more than 10,000 OPC talents by 2028. This is a government policy target, not an independent market forecast or an achieved outcome. The research did not establish a comparable AI-OPC forecast for Singapore or ASEAN, or evidence sufficient to call regional company growth exponential.")
src("Singapore MOM, Labour Force in Singapore 2025, para 2.32: https://stats.mom.gov.sg/publications/report-labour-force-in-singapore-2025/ ; Digital China portal, 11 Aug 2026 (People's Daily Overseas Edition citing National OPC Development Observation Report): https://www.digitalchina.gov.cn/2026/xwzx/szkx/202608/t20260811_5356927.htm ; Suzhou government, action plan issued 25 Dec 2025: https://www.suzhou.gov.cn/szsrmzf/zfbgswj/202605/c18bb19aa5c2430abb18916662baabe6.shtml . Checked 18 Nov 2026.")
h3("AI Agents as the Interface to Software and SaaS")
p("Instead of navigating many software screens, a person describes a task to an AI agent. The agent selects configured tools, sends permitted requests to the relevant software and reports the result. An API exposes application functions; MCP standardises how tools are described and called, often with a server that wraps an existing API. MCP does not bypass authentication or the software's permissions.")
tbl(["Example request", "What the agent does", "Business benefit"], [
    ("Sales: Find overdue follow-ups and create CRM tasks for account owners.", "Read permitted CRM records, identify overdue follow-ups, create assigned tasks and report the task IDs.", "Less screen navigation; new staff can work through a familiar task description."),
    ("HR: Check my leave balance and prepare a request for next Friday.", "Read the authorised employee balance, check the policy and prepare a leave request for the manager.", "Faster routine HR self-service; the manager retains the approval decision."),
    ("Finance: List overdue invoices and draft reminders for my approval.", "Retrieve invoice status from the accounting system, prepare a review list and draft messages without sending.", "Less manual searching and re-keying; finance staff review exceptions and approve sends.")], [2.1, 2.6, 2.0])
p("These are illustrative configured workflows, not integrations supplied automatically by every agent. Faster onboarding is a benefit to test: staff still need the company's rules, judgement and approval responsibilities. Another example is a meeting assistant that checks calendars and proposes an appointment through a calendar API; inviting others needs the user's approval.")
src("MCP tools specification: https://modelcontextprotocol.io/specification/2025-06-18/server/tools ; Microsoft Graph calendar API: https://learn.microsoft.com/en-us/graph/api/user-post-events?view=graph-rest-1.0 (checked 18 November 2026).")
h3("A Service Agent: Knowledge, Live Data and Action")
p("An online-store customer asks: 'Where is my order, and can I change the delivery address?' A knowledge-only chatbot might explain the delivery policy. A configured service agent can complete a longer workflow:")
ol(["Search the approved knowledge base for the current delivery and address-change rules; explain the relevant rule.",
    "Verify the customer and use an authorised order-system tool to check this order's dispatch status.",
    "If the policy and permissions allow a change, confirm the new address, update it and provide a confirmation. If the parcel has already dispatched or the case is unusual, create a support ticket and hand over to a person."])
p("Business benefits include after-hours service, repetitive work without human fatigue and a consistent approved workflow. Additional agent instances can run the same workflow for more customers in parallel. Each customer's session and permissions must stay separate, while the instances use common live order state and duplicate-action checks. Scaling is not unlimited: hosting, API quotas, costs, monitoring and human exception-handling capacity still matter.")
h3("Multi-Agent Video Production Team")
p("A human producer briefs the team: 'Create a 30-second product-launch video for this audience, using this offer, brand guide and budget.' Specialist agents share one approved brief and a common asset folder:")
ol(["The script agent drafts the story, script and shot list. The human producer approves the script and spending cap before production.",
    "Visual and voice/music agents work in parallel on the approved shots, narration and soundtrack. They keep versioned files in the shared project folder.",
    "The editing agent assembles clips, captions and audio using connected production tools.",
    "A separate review agent checks facts, brand consistency, captions, continuity and the media-rights checklist. It flags issues for correction; its review does not replace human judgement.",
    "The human producer reviews the final video and approves release before anything is published."])
p("This team can reduce hand-off time and run asset work in parallel. Reuse approved instructions for the next campaign or add agent instances for more projects, while keeping each project's assets, permissions and budget separate. Measure turnaround, revision time, cost and quality. API/MCP automation depends on the production platforms exposing the necessary actions; a human can perform an unsupported step.")
h3("Multi-Agent Trading Team: A Research-to-Review Loop")
p("An illustrative trading team can assign several agents to each of five roles, coordinated by one accountable human strategy owner. In training, use paper trading:")
ol(["Data agents gather financial statements, market prices and news from authorised sources. They check quality and preserve timestamps so research does not use future information.",
    "Research agents propose algorithms or hypotheses, backtest them on historical data and generate signals. Evaluate held-out data and realistic transaction costs.",
    "Execution agents apply the approved risk checks, route simulated orders through a paper-broker API, and record orders and fills. Shared order state and unique order IDs help prevent duplicate or conflicting trades.",
    "Analysis agents reconcile profit/loss and measure drawdown, costs, slippage, signal quality and execution performance.",
    "Review agents investigate outcomes and drift, then propose a new algorithm version. Feed it back to research and testing; the human owner approves the version before live deployment."])
p("The human owner sets capital and position limits, pause conditions and approval responsibilities. Multiple agents can explore ideas and analyse evidence in parallel, but an attractive backtest or simulation is not proof of live profitability. The example describes an operating model; it does not execute real trades.")
src("Alpaca, Paper Trading: https://docs.alpaca.markets/us/docs/paper-trading (checked 18 November 2026).")
h3("Scientific Agent Team: A Literature-to-Evidence Loop")
p("Start with one research question and one accountable human researcher. Teams of specialist agents share a versioned research notebook:")
ol(["Literature agents search relevant papers, record citations, map existing evidence and identify gaps.",
    "Theory agents propose competing explanations, falsifiable hypotheses and measurable predictions.",
    "Experiment-design agents propose controls, measurements, resource needs and an analysis plan. The researcher approves the protocol before testing.",
    "Testing agents run approved simulations or coordinate authorised experiments with laboratory staff or connected instruments; they capture observations and provenance.",
    "Analysis agents compare observations with predictions, assess uncertainty and check reproducibility. Supporting and contrary evidence both return to the theory and literature teams, which revise or reject hypotheses and design the next experiment."])
p("The human researcher defines the question, approves protocols and resources, checks the validity of the evidence and decides what claims the findings support. This is an illustrative team design: an agent's proposed experiment or explanation is not experimental evidence by itself.")
h2("1.6 Meridian Services: The Scenario")
p("Meridian Services Pte Ltd is a fictitious Singapore facilities firm: 140 staff support 30 commercial buildings. About 80 emails and WhatsApps arrive daily; coordinators spend 38% of their time re-keying requests, each taking 18 minutes to handle. Meridian wants faster service without losing human care. All figures are synthetic.")
h2("1.7 What the Business Model Canvas Shows")
p("The Business Model Canvas (BMC) maps how a company creates, delivers and captures value across nine connected blocks. Start with who is served and why they choose you; link channels and relationships to the activities, resources and partners needed; then check revenue and costs. AI agents may improve several blocks, but the whole model must still make sense.")
tbl(["BMC block", "Meaning", "Meridian agent use and benefit"], [(r[0], r[1], r[2] + " " + r[3]) for r in B.BMC_BENEFITS], [1.35, 1.65, 3.7])
p("Read these proposed benefits as hypotheses. Faster replies do not guarantee retention or new revenue. The predictor is a future option, parked until its data is ready; the premium response tier also needs validation. Human approval remains on urgent jobs, complaints and refunds.")
h2("1.8 Why AI Projects Stall: Five Capability Gaps")
p("Deploy a model straight out of the box and five structural gaps appear at once:")
ol(["Private data: contracts, customer records and internal processes are blank to it.",
    "Internal language: 'active customer' or 'closed' may mean something different in your company.",
    "Live context: it does not know what changed a second ago.",
    "Ability to act: it has no permission to execute inside your systems.",
    "Guardrails: no permission controls, verification of results or audit trail."])
p("Like a brilliant graduate nobody onboards, the model stays stuck on day one. A business opportunity is viable only if you can close these gaps for it.")
h2("1.9 Investigating and Evaluating Opportunities (A1, A2)")
p("Analyse the business need before you pick technology. Gather evidence from five sources:")
tbl(["Evidence", "Questions", "Example (a service desk)"], [
    ("Stakeholders", "Who feels the pain? What does each want and fear?", "Clients chase job status; coordinators fear replacement."),
    ("Process", "Trigger, steps, hand-offs, waits, rework, decisions?", "6 steps, 3 hand-offs, 38% of time re-keying."),
    ("Data", "What data exists, is it clean, current and permitted?", "5 years of tickets; tenant phone numbers must be masked (PDPA)."),
    ("Requirements", "What must the solution do, testably, and who signs it off?", "Draft a ticket within 1 minute; coordinator approves urgent jobs."),
    ("Opportunity", "Which objective does it move, by how much, at what cost and risk?", "Handling time 18 to 11 minutes; same-day response objective.")], [1.3, 2.7, 2.7])
p("Score each idea on value, feasibility and data readiness (1-5 each) and check it serves an organisational objective. Set a veto: "
  "a score of 1 on data or risk stops the idea whatever the total. Four value levers: revenue, cost, risk and experience.")
h2("Meridian Demo: Business Model Canvas (fictitious company)")
p("Meridian Services Pte Ltd is a fictitious Singapore facilities firm: 140 staff keep 30 commercial buildings running. It receives about 80 emails and WhatsApps a day and its coordinators spend 38% of their time re-keying them into tickets; each request takes 18 minutes to handle. Its Topic 1 question: where on our business model would AI agents pay off first, and which idea do we park? Its canvas scores request triage 80, monthly client reports 75 and a repeat-fault predictor 24 (parked), and keeps a person on complaints, refunds and premium clients.")
p("Meridian's filled Activity 1 board (read-only): https://alfredang.github.io/bcm/?join=meridian-activity-1. Open it, compare it with your own, then make every note about your "
  "own organisation. Meridian is fictitious and all its figures are synthetic.")
img(os.path.join(IMG, "screenshots", "meridian-bmc.png"), "Meridian Services (fictitious): filled Activity 1 board in the Activity Studio", 5.2)

h2("Activity 1 — Your Company's BMC in Groups of 3-5 (PP Task 1)")
p("Form a group of 3-5 and choose one member's company. The leader opens https://alfredang.github.io/bcm/?activity=opportunity, creates one Activity 1 board and names the group and company. Everyone joins using its Board ID or QR code and their own name. Create your company's nine-block BMC, showing where AI agents add value; use non-confidential facts and label assumptions. Use this same company for Activities 2 and 3.")
X.append(("canvas", "opportunity"))

# ------------------------------------------------------------------ Topic 2
h1("Topic 2 — " + C.TOPICS[1]["title"])
p(C.LEARNING_OUTCOMES[1] + " (K3, K4, A3, A4)")
h2("The 90-Day Action Plan: Five Steps to Get Started")
p("Topic 2 and Activity 2 follow one five-step plan. Each step is a numbered block on your action plan board.")
tbl(["Step", "What you do", "What you decide"], [(l, w, d) for l, w, d, _ in B.PLAN], [0.5, 1.6, 4.6])
h2("Step 1 · Set the Goal")
p("Fill Objective & Outcome and Cost & Value. Record the population, current performance, target date, owner and a quality limit before approving a pilot.")
p(B.MERIDIAN_PLAN_BOXES["objective"] + " Meridian has 10,000 eligible requests out of 28,800 a year. " + B.MERIDIAN_PLAN_BOXES["budget"])
h2("Step 2 · Mine the Business Process")
h3("Dormant Data Is a Gold Mine")
p("A company keeps two sets of records. The official set (reports, reviews, strategy papers) is polished and filtered. The second set "
  "records what actually happened: meeting audio, chat logs, edit history, customer tickets, code logs, photos and system logs. It is "
  "often fragmented, incomplete or biased, and until now too hard to analyse at scale. This is dormant data. Multimodal AI can help analyse text, audio, images, "
  "spreadsheets and logs together, so this record becomes usable.")
img(os.path.join(IMG, "ainative", "dormant-data.png"), "Awakening dormant data", 5.6)
p("Dormant data is a potential gold mine because it contains clues to recurring faults, customer needs and process delays. Value comes from a verified business decision, rather than the volume of data collected. Check permission, quality, freshness and coverage before use, then trace each finding to its source and compare the result with a baseline.")
tbl(["Source", "Opportunity", "Measure"], [("Meridian's closed tickets and technician notes", "Find repeat faults and missing information", "Repeat visits and rework rate"), ("Customer chats and complaints", "Find repeated questions and renewal concerns", "Resolution time and retention"), ("Quotation and approval timestamps", "Locate waiting and avoidable handoffs", "Lead time and conversion")], [2.1, 2.8, 1.8])
h3("Map the Current Workflow")
ol(["Pick one process that hurts every week.", "Pull its trail from dormant data: emails, tickets, logs, chats, meeting notes.",
    "Rebuild the real steps: trigger, actors, hand-offs, systems.", "Measure waits, rework and touch time against a baseline.",
    "Mark every decision: who judges, on what evidence, under which rule."])
h3("Process Mining with Meridian's Ticket Events")
p("Process mining reconstructs observed workflows from event logs. Start with one row per event and include case ID, activity and timestamp. For example, M-101 has separate rows for Request (09:00), Draft (09:04), Approval (09:10) and Dispatch (09:12). Group by case ID, sort by timestamp and compare the resulting paths. Discovery shows common paths and variants. Conformance checks their order against the approved process. Performance analysis measures elapsed times and helps locate delays and rework.")
tbl(["Case ID", "Events in timestamp order", "Time to dispatch"], B.PROCESS_MINING_TRACES, [0.9, 4.7, 1.1])
p("Meridian's SOP requires approval before dispatch. M-102 returns for missing details and takes 50 minutes from request to approval. This measures elapsed time, including work and waiting. M-103 has no approval event in the sample. Check the approval source and log completeness with the process owner before concluding the rule was breached.")
p("Apply this in Activity 2. Pick a process with an authorised event export or use these synthetic traces. Confirm the case ID and timestamp meaning. Map the common route and one exception, identify an interval worth measuring across more cases, then propose an agent action and one human control. Meridian could test an agent that flags missing details before handoff, with coordinator approval still required for dispatch.")
src("IEEE Task Force on Process Mining, Process Mining Manifesto: " + B.PROCESS_MINING_SOURCE)
h2("Step 3 · Plug In the Agents")
p("Fill Where Agents Plug In and Digital Architecture. " + B.MERIDIAN_PLAN_BOXES["integrate"] + " " + B.MERIDIAN_PLAN_BOXES["architecture"])
p("Classify each step by how much the AI may do, and name the accountable human for each. This is the human decision boundary.")
tbl(["Level", "The AI…", "The human…"], [("Inform", "summarises or alerts", "decides everything"), ("Recommend", "ranks and suggests", "chooses"),
     ("Prepare", "drafts the ticket, reply or report", "edits and approves"), ("Execute with approval", "acts after a yes", "approves each action"),
     ("Execute with monitoring", "acts on its own", "audits samples and exceptions")], [1.8, 2.4, 2.5])
p("Choose the simplest pattern that works: deterministic automation, a grounded assistant (RAG), an agentic workflow with fixed steps, "
  "a single agent that chooses its steps, or a multi-agent team with a coordinator. More autonomy needs more controls.")
h3("The Enterprise AI Decision Layer")
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
    "Control: grant a task-specific identity only the required permissions, enforce approval gates in connected systems and log actions."])
h3("Drawing the Company Map")
p("An ontology, or company map, is a semantic structure that defines key business terms (what a customer, contract or approval is) and "
  "how they relate. It covers people, customers, products, orders, contracts, approval flows and business rules. Without it a model "
  "cannot see why active customers are tied to payment terms, or why three more approvals follow a signed contract. Build it in "
  "layers: data sources, data models, business rules, relationships. Today it can be drawn and revised in plain language by the people "
  "who run the business (ontology 2.0), instead of taking 6-18 months of specialist work.")
p("In Activity 2 you ask Meta Muse to draft a company map for one of your own processes; your action plan builds on it.")
h3("Empower the Agent with a Business Briefing")
p("Teach the agent how your business works before asking it to run a process. Assemble an approved briefing pack and retrieve the relevant parts for each task: a business overview, process map, glossary, current SOPs and policies, worked examples and live system facts. Uploading documents alone does not ensure correct behaviour; the process owner must check understanding and outcomes.")
tbl(["Briefing component", "What to provide", "Meridian example"], B.AGENT_BRIEFING, [1.35, 2.6, 2.75])
p("For each policy record its owner, version, effective date, applicable roles, thresholds, prohibited actions and exception route. Distinguish approved instructions from historical emails and customer messages. If sources conflict or a rule is missing, the agent must ask the owner instead of inventing an answer.")
p("Meridian pilot example: the agent may read permitted request and contract records, classify requests and draft tickets. An urgent leak triggers an alert to the duty coordinator. Dispatch, external replies, purchases and refunds need human approval. These are fictitious pilot rules, not claims about a real firm's policies. Tool access and workflow gates enforce the limits; a prompt alone cannot enforce authorisation.")
ol(["Brief: give the task, process, definitions and current policy sources.", "Test: use routine, urgent, incomplete and conflicting examples with expected outcomes.", "Correct: the process owner checks source citations, proposed actions and escalation; revise the pack and rerun failures.", "Empower: start read-only, grant the smallest useful task permissions after agreed tests pass, log actions and provide a stop control.", "Maintain: assign an owner to update the briefing and retest when a process, policy or connector changes."])
p("Activity 2 output: add the approved policy sources, permissions and exception route to your company map, then carry them into the architecture and pilot controls of your 90-day plan.")
h3("Digital Architecture: Custom, Buy or Hybrid (K4, A3)")
tbl(["Layer", "What it holds"], [("Data", "Sources, quality, permissions, dormant data"), ("Model", "The chosen model(s) and their limits"),
     ("Orchestration", "Workflow, agents, memory, tools (MCP)"), ("Application", "Where people meet the AI: email, portal, chat"),
     ("Governance", "Access control, approvals, logs, evaluation, monitoring")], [1.5, 5.2])
p("Draw trust boundaries where data or actions cross systems or organisations; apply least privilege at each boundary. Decide custom, "
  "buy or hybrid on differentiation, time to value, integration fit, assurance, three-year total cost of ownership (licences, build, run, "
  "change, incidents) and an exit option. Most firms buy the platform and own the company map and rules.")
h2("Step 4 · Name the Owner")
p("Fill DRI, Team & Resources. Give one directly responsible individual the authority to change rules, allocate resources and pause the pilot. " + B.MERIDIAN_PLAN_BOXES["owners"])
h2("Step 5 · Run and Evaluate the 90-Day Pilot")
p("Fill Pilot Milestones, Risks & Controls and Success Measures. " + B.MERIDIAN_PLAN_BOXES["milestones"] + " " + B.MERIDIAN_PLAN_BOXES["risks"])
h3("Evaluation Metrics for Your Company")
p("Choose measures that fit the goal. For each measure record the baseline, target, unit, data source, review cadence and owner. Use comparable case mixes and time windows, and record how many cases qualify. For Meridian, compare minutes per eligible request and check the complaint and rework rates every week.")
tbl(["Outcome", "Measure"], B.PILOT_METRICS, [2.0, 4.7])
h3("Decision Rubric for the Pilot")
tbl(["Decision", "Rule", "Meridian example"], B.PILOT_RUBRIC, [1.05, 2.75, 2.9])
h2("Meridian Scenario: From Triage to a 90-Day Plan")
p("Meridian chose request triage. Today the work follows six steps and three handoffs. Meridian wants same-day responses and plans to cut handling time from 18 to 11 minutes by day 90. The year-one budget is SGD 39,000. A misrouted urgent job could cost a contract. Decide which steps the agent can take, who owns the outcome and what would stop the pilot. In Activity 2, apply the same questions to your own process.")
h2("Meridian Demo: 90-Day Action Plan (fictitious company)")
tbl(["Action-plan box", "Meridian's completed entry"],
    [(box["title"], B.MERIDIAN_PLAN_BOXES[box["id"]]) for box in B.CANVAS["actionplan"]["blocks"]], [2.1, 4.6])
p("Meridian's filled Activity 2 board (read-only): https://alfredang.github.io/bcm/?join=meridian-activity-2. Open it, compare it with your own, then make every note about your "
  "own organisation. Meridian is fictitious and all its figures are synthetic.")
img(os.path.join(IMG, "screenshots", "meridian-plan.png"), "Meridian Services (fictitious): filled Activity 2 board in the Activity Studio", 5.2)

h2("Activity 2 — AI Agent 90-Day Action Plan with Meta Muse (PP Task 2)")
p("Form a group of 3–5 and choose one member’s company. Use a priority from Activity 1. Create one shared board and fill all nine boxes in order. Agree on the baseline, targets, guardrails and decision rubric. Each learner saves the group’s completed board and writes their individual PP answers.")
X.append(("canvas", "actionplan"))

# ------------------------------------------------------------------ Topic 3
h1("Topic 3 — " + C.TOPICS[2]["title"])
p(C.LEARNING_OUTCOMES[2] + " (K5, K6, A5, A6)")
h2("Challenges of AI Transformation")
tbl(["Challenge", "What Meridian hears or sees"], [
    ("Resistance to change", "Coordinators trust the current workflow and want a say in how it changes."),
    ("Worry about job loss", "Staff ask whether drafting tickets is the first step in replacing their roles."),
    ("Steep learning curve", "Teams need time to practise using the agent and checking its drafts."),
    ("Trust and accountability", "Coordinators want clear approval rules and an escalation contact for mistakes."),
    ("Limited capacity", "Managers need protected time and resources to coach while running the service."),
    ("Data and reliability", "Missing request details or poor tickets can make staff revert to manual work.")], [2.0, 4.7])
h3("Job-Market Outlook and Demand for AI Skills")
p("The World Economic Forum projects 170 million jobs created and 92 million displaced globally by 2030, yielding 78 million net jobs across technology, demographic, economic and environmental trends. AI and data roles are among the fastest-growing by percentage. Care, education and other occupations also contribute to job growth.")
src("World Economic Forum, Future of Jobs Report 2025, Jobs Outlook: " + B.WORKFORCE_SOURCES["wef"])
p("Singapore’s total employment increased by 27,700 in Q3 2026 in MOM’s advance release. Resident growth was supported by essential and public services. Construction and manufacturing contributed to non-resident growth. IMDA separately reports tech workforce growth of 2.7% to 214,000 in 2024, with AI and data and cybersecurity among the fastest-growing tech roles. The share of tech postings requiring AI skills rose from 11% in 2019 to 14% in 2024.")
src("MOM, Labour Market Advance Release Q3 2026: " + B.WORKFORCE_SOURCES["mom"] + " · IMDA, Singapore Digital Economy Report 2025: " + B.WORKFORCE_SOURCES["imda"])
h2("The SCALE Framework: Five Moves to Sustain and Operate")
p("Topic 3 and Activity 3 follow one framework. Each move is a block on your SCALE board.")
tbl(["", "Move", "What you do"], [(l, w, d) for l, w, d, _ in B.SCALE], [0.4, 1.5, 4.8])
h2("S · Story: Communicate the Change")
p("Explain why Meridian is piloting triage, what the agent will draft, what staff still decide and when the plan will be reviewed. Explain the no-job-loss commitment for the pilot. Use a team huddle for coordinators, a service update for customers and a short review for leaders. Give each group a named contact for questions.")
h2("C · Commanders: Give the Rollout an Owner")
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
h3("Progressive Implementation")
p("Start with shadow mode, where the agent drafts alongside normal work. Move to assist mode with a person approving each action. Test supervised autonomy only for low-risk tasks that pass the agreed checks. Meridian starts with two sites, expands to ten after review and keeps human approval for dispatch. The DRI pauses the rollout when quality or safety falls outside limits.")
h2("A · Augment People: Redesign Roles and Coach")
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
h3("Redesign the Job Around a Human Owner")
p("Choose a named person to own each outcome. Give that person authority to set direction, approve consequential actions, resolve exceptions, pause the workflow and update the operating rules. Define the agent’s delegated work and record what the human checks. Judge the redesigned role by outcomes such as accurate tickets, response times and safe decisions.")
tbl(["Human responsibility", "What the owner does"], [(name, action) for _, name, action in B.HUMAN_OWNER_RIGHTS], [1.6, 5.1])
p("Meridian’s Head of Service Desk sets service targets and authorises the workflows. The agent extracts request details, drafts tickets and flags urgency. Coordinators check the evidence and approve dispatch. The Head of Service Desk reviews exceptions and can pause the workflow or change the rules.")
p("A second example is Sarah, a marketing lead. The agent drafts campaign copy and decks. Sarah owns campaign outcomes, sets the creative direction, checks factual claims and approves release. She and her manager agree a two-week trial and review draft time, corrections and whether she had enough control.")
src("Dr Alfred Ang, Work Redesign for Managing AI Agents, 27 August 2026, pp. 3, 4, 6 and 9.")
h3("Coaching Example: Use the AI Coaching Simulator")
p("Ask the employee what concerns them, explore their strengths and workload, co-create a role that uses their judgment, and agree one small trial and a review date. At Meridian, the coordinator keeps urgent dispatch decisions and spends more time on customer follow-up. Give employees practice on their own work, builders training on testing and controls, and managers time for coaching.")
p("Open https://alfredang.github.io/AICoaching/ and select a worried employee in demo mode. Coach the employee, request feedback, then convert one suggestion into an action and a date. Debrief how you acknowledged the concern and agreed a supported next step.")
h2("L · Loop Information: Collect and Act on Feedback (A6)")
p("In an AI-native firm, information flows through the DRI and the decision layer instead of up and down ten layers. Set an operating "
  "rhythm: a daily 8:00 exceptions brief from the agents, a weekly DRI review with the team, a monthly one-page dashboard for the sponsor. "
  "Communicate the change per stakeholder (what changes, what does not, who to ask), and run an idea pipeline where anyone can post an "
  "idea, the agent clusters them, and the best get a DRI and 30 days.")
p("Close the loop with staff. Collect concerns and client feedback, review them weekly, name an owner for each change and tell people what was done. For example, Meridian could revise its intake form after coordinators repeatedly flag missing building details.")
h2("E · Evaluate: Decide Whether to Continue or Scale")
p("Check service outcomes, adoption, safety and staff or customer feedback against the agreed targets. Review costs and the stop rule with the DRI. Scale in stages when the evidence supports it, redesign and retest weak parts, or pause the pilot and return to the human workflow.")
h3("Legal, Ethical and Security Issues (K6)")
bl(["PDPA: collect and use personal data only for notified purposes; mask personal data before analysis; follow the PDPC Advisory "
    "Guidelines on Use of Personal Data in Generative AI (2026).", "IMDA Model AI Governance Framework for Agentic AI: bound the risk, keep "
    "humans meaningfully accountable, apply technical controls, enable users. CSA's Securing Agentic AI addendum (June 2026) adds security controls.",
    "Five agent risks (one slide each, with a Meridian example):",
    "1 Prompt injection: instructions hidden in an email, web page or PDF the agent reads give it orders; the attacker never talks to the AI. Example: a leak report ends in white text telling the triage agent to close all Tower B tickets and forward the client list. Treat everything the agent reads as data, draft only, a person approves bulk changes.",
    "2 Jailbreak: a user deliberately crafts prompts (role-play, 'test mode', step-by-step pressure) to make the AI break its own rules. Unlike prompt injection, the attacker is the person in the chat; unlike shadow AI, it is an attack. Example: a 'tenant' tells the WhatsApp agent it is now in admin test mode and asks for plant-room access codes. Keep secrets out of the agent's reach, never let it change its own permissions, red-team it before go-live.",
    "3 Data leakage: personal or confidential data flows where it should not, with or without an attacker; it can breach the PDPA. Example: a coordinator pastes a tenant's name, unit and phone number into a free chatbot. Classify data, mask personal data, have the DPO check each agent.",
    "4 Shadow AI: staff use AI tools the company has not approved and cannot see; no attack, usually good intent, but no control. Example: technicians transcribe voice notes holding tenant names with a free app. Ask what staff use without blame, offer an easier approved tool, publish one page of AI rules.",
    "5 Bias and blame: the agent learns unfair patterns and nobody owns the decision. Example: premium-contract faults get marked urgent faster than small-office faults. Name a DRI for every agent decision, compare outcomes across groups, keep an appeal route.",
    "Accountability: the organisation stays responsible for its agents' actions; keep an audit trail of who asked what and when.",
    "Ethics: transparency, fairness, explainability, human oversight; tell customers when they are dealing with an agent."])
h3("Review Meridian’s Pilot Results (K5, A5)")
bl(["Start narrow with one high-value process, a measured baseline and a named DRI.", "Keep a real human checkpoint for the first 90 days.",
    "Measure offline quality before launch and online telemetry after: cycle time, first-pass accuracy, complaints, adoption, cost per outcome.",
    "Review at a fixed gate and decide scale, redesign, hold or stop on pre-agreed criteria."])
R = C.ROI_CASE
tbl(["Day-90 metric", "Target", "Result"], [("Mean handling time", "≤ 11 min", "10.7 min"), ("Quality", "≥ 94%", "95.1%"),
     ("Complaints", "≤ 2%", "1.7%"), ("Sustained use", "≥ 70%", "77.5%"), ("Critical unsafe actions", "0", "0"),
     ("Realised benefit vs year-1 cost", "benefit ≥ cost", f"SGD {R['day90_benefit']:,} vs SGD {R['first_year_cost']:,}")], [2.6, 2.0, 2.1])
p("ROI = (realised benefit - cost) / cost. Here year-1 ROI is close to zero but recurring costs are lower, so the case for scaling rests on "
  "year 2 and on keeping quality. Always add a downside case (lower adoption, smaller time saving).")
h2("Meridian Demo: SCALE Board (fictitious company)")
p("At day 90 Meridian's numbers say scale: handling time 10.7 minutes, quality 95.1%, complaints 1.7%, adoption 77.5%. But coordinators fear replacement. Its SCALE board tells the story first (no one loses their job in the pilot), gives each outcome one DRI with an agent team, moves coordinators to client calls and exceptions, keeps people judging through weekly sample audits, sets a daily, weekly and monthly information rhythm, and decides to scale to all 30 sites with the same approval rules.")
tbl(["SCALE box", "What to decide", "Meridian’s completed entry"], [
    (box["title"], box["prompt"], B.MERIDIAN_SCALE_BOXES[box["id"]])
    for box in B.CANVAS["change"]["blocks"]
], [1.4, 2.0, 3.3])
p("Meridian's filled Activity 3 board (read-only): https://alfredang.github.io/bcm/?join=meridian-activity-3. Open it, compare it with your own, then make every note about your "
  "own organisation. Meridian is fictitious and all its figures are synthetic.")
img(os.path.join(IMG, "screenshots", "meridian-scale.png"), "Meridian Services (fictitious): filled Activity 3 board in the Activity Studio", 5.2)

h2("Activity 3 — Sustain and Operate with AI Agents (SCALE) with Meta Muse (PP Task 3)")
p("Form groups of 3–5 and continue with the same company and pilot. Join one shared board and fill every SCALE box with your own actions, owners and review measures.")
X.append(("canvas", "change"))

# ------------------------------------------------------------------ v47 bonus topic (self-paced, outside the contact hours)
h1("Bonus Topic — Communicate Your AI Transition")
p("Continue from Topic 3. Build a one-page stakeholder update from your SCALE board. Include a clear pitch, what changes for people and how they can respond. This project is self-paced after class.")
h2("Worked Example: Meridian’s AI Transition")
p("Meridian’s headline is ‘Faster service. People in charge.’ The page explains who reviews AI drafts, what happens to roles, how the pilot expands, and where to take questions. Download meridian-ai-transition.html from the course Activities folder and open it in a browser.")
img(os.path.join(IMG, "screenshots", "meridian-ai-transition.png"), "Meridian AI transition landing page", 5.8)
tbl(["Audience", "Message and next action"], [
    ("Staff", "Agents draft tickets. Coordinators retain approval, handle exceptions and get coaching. Bring an issue to the team huddle."),
    ("Clients", "Expect clearer updates and a human contact. Use the existing service desk or account manager."),
    ("Leaders", "Review service, quality, adoption and safeguards at each gate. Approve the next wave when the evidence supports it."),
], [1.5, 5.2])
h2("Create Your Stakeholder Page With Codex")
ol(["Bring in the change story, stakeholder map, messages, approvals and feedback routes from your SCALE board. Add evidence, owners and milestones from the Activity 2 plan.",
    "Give Codex one promise, each audience’s questions and its next action. Ask for a mobile-friendly page with the rollout timeline, human approval gates, results and feedback routes.",
    "Verify figures, claims, contact routes and accessibility on a phone and desktop. Get approval from the owner of the rollout and agree who should see the page.",
    "If you are authorised to share the page, ask Codex to publish with Sites. Confirm the audience settings and test access with the intended group."])
p("For current Sites access and hosting terms, see https://learn.chatgpt.com/docs/sites.")

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
     ("TCO", "Total cost of ownership over three years"), ("Atrophy trap", "Losing judgement by always deferring to AI"), ("Codex / Sites", "OpenAI's coding agent / its website builder and host in ChatGPT and Codex")], [1.8, 4.9])
h1("References")
bl(["IMDA, Model AI Governance Framework for Agentic AI v1.5 (20 May 2026).", "Enterprise Singapore, media release on AI initiatives (27 Oct 2026).",
    "The Straits Times, 24 Aug 2026: New platform to create AI agents available to all public healthcare professionals.",
    "Meta Newsroom, Muse in Singapore (27 Oct 2026); Meta Help, Connectors.", "Klarna press release, Feb 2024 (AI assistant handles two-thirds of service chats); OpenAI Sites docs, accessed 18 Nov 2026."])

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
                o += [f"**{'Task' if L['n'] == 2 else 'Step'} {i + 1} — {st['title']}**", ""] + [f"- {x}" for x in st["body"]] + ([f"- {a}: {u}" for a, u in B.MUSE_LINKS] if st.get("links") == "MUSE" else []) + [""]
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
    from docx.oxml import OxmlElement
    t.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
    for row in t.rows:
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
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
        doc.add_paragraph(f"Group board: {B.BCM_URL}?activity={cv['key']}  ·  {L['minutes']} min  ·  {cv['evidence']}  ·  current prompt templates: download activities/prompts.html from the LMS course materials")
        for i, st in enumerate(L["steps"]):
            hp = doc.add_paragraph(); hr = hp.add_run(f"{'Task' if L['n'] == 2 else 'Step'} {i + 1} — {st['title']}"); hr.bold = True
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
