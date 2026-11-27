"""SINGLE SOURCE for the v41 activities and hands-on labs.

CANVASES  - the three class activities (one per LO). Each is an online board in the Agentic AI Canvas Studio
            (https://alfredang.github.io/bcm/, no login). The same block definitions and worked
            examples drive the slides, the Learner Guide, the activity folders and the web app
            (export_bcm_templates.py writes them to the bcm repo as js/templates.js).
LABS      - thirteen hands-on labs with Meta Muse, the always-on AI agent.

Board examples (View example) are the worked demo for Meridian Services Pte Ltd, a fictitious facilities firm (v47, owner);
all figures are synthetic. Learners always work on their own organisation; Meridian is only the reference.
"""

BCM_URL = "https://alfredang.github.io/bcm/"
EXAMPLE_CO = "Meridian Services Pte Ltd (fictitious)"  # v47: Meridian is back as the worked demo (owner); learners still use their own organisation
EXAMPLE_BLURB = ("Fictional Singapore facilities-maintenance firm: 140 staff, 28,800 service requests a year, "
                 "18-minute average handling time, 14% rework, 1.4% complaints.")

# --------------------------------------------------------------------------- the three activities (one per LO)
# Each block: id, title, prompt (one-line question shown on the board), questions (guidance), example notes
# (title, description). Layout "bmc" uses the Business Model Canvas grid; "grid" a 3-column board.
CANVASES = [{'key': 'opportunity', 'num': 1, 'topic': 1, 'lo': 'LO1', 'codes': 'K1, K2, A1, A2', 'layout': 'bmc', 'minutes': 80, 'title': 'Business Model Canvas for AI Agents', 'short': 'Find the opportunities', 'pitch': 'Use nine connected business-model blocks to identify and evaluate where AI agents add value.', 'evidence': 'PP Task 1 · screenshot of your BMC', 'discuss': ['Which block of your business model would an AI agent change the most?', 'Which opportunity moves a number your leadership already tracks?', 'Which of the five capability gaps (private data, internal language, live context, action, guardrails) could stop it?'], 'blocks': [{'id': 'keyPartners', 'title': 'Key Partners', 'prompt': 'Which partners hold the data, systems or AI platforms your agents need?', 'questions': ['Which vendors own the systems agents must read or act in (CRM, ERP, Gmail, WhatsApp)?', 'Which AI platform or agent partner would you buy from or build with?', 'Who must agree before an agent touches their data?'], 'example': [('ServiceNow (ticketing vendor)', 'Holds every service request since 2019; agent API access needs a contract addendum.'), ('Meta Muse / Google Workspace', 'Always-on agent reads Gmail and Calendar for 140 staff.'), ('Building owners', 'Share sensor feeds an agent can watch for faults.')]},
 {'id': 'keyActivities', 'title': 'Key Activities', 'prompt': 'Which key activities could AI agents do, speed up or watch over?', 'questions': ['Which activities are repetitive, rule-based or full of waiting?', 'Which need judgement and must stay human?', 'Which could an always-on agent watch 24/7?'], 'example': [('Request triage (agent)', 'Agent reads 80 emails and WhatsApps a day, drafts tickets; coordinators approve.'), ('Technician scheduling', 'Agent proposes routes; supervisor confirms.'), ('Monthly client reports', 'Agent drafts from tickets; account manager reviews.')]},
 {'id': 'keyResources', 'title': 'Key Resources', 'prompt': 'Which data and know-how would make your agents smart about your business?', 'questions': ['Which dormant data (calls, chats, tickets, logs) is never analysed?', 'What do veterans know that is written nowhere?', 'Is the data clean, current and permitted?'], 'example': [('5 years of closed tickets', 'Root causes and repeat faults per site: fuel for a predictor agent.'), ('Technician photos and voice notes', 'Thousands in WhatsApp groups, never searched.'), ('Senior coordinator know-how', 'Which clients need a call, not an email.')]},
 {'id': 'valueProps', 'title': 'Value Propositions', 'prompt': 'What new or better value can AI agents deliver to your customers?', 'questions': ['Name the agent and the customer benefit in one line.', 'Faster, cheaper, more personal or entirely new?', 'Always-on (watching) or on demand?'], 'example': [('Same-day answers, 24/7', 'Always-on triage agent replies within minutes, even at 2 am.'), ('No repeat faults', 'Predictor agent flags sites likely to fail again within 30 days.'), ('Live job status', 'Agent updates the client portal as work progresses.')]},
 {'id': 'customerRel', 'title': 'Customer Relationships', 'prompt': 'How will agents change the way you serve and keep customers, and where must a human stay?', 'questions': ['Which interactions can an agent handle; which need a person?', "Who is the DRI accountable for the agent's results?", 'How does a customer reach a human fast?'], 'example': [('Agent first, human always reachable', 'Routine updates by agent; complaints and refunds by a coordinator.'), ('DRI: Head of Service Desk', 'Owns triage accuracy and handling time.'), ('Personal touch kept', 'Account managers call key clients monthly.')]},
 {'id': 'channels', 'title': 'Channels', 'prompt': 'Through which channels will your agents meet customers?', 'questions': ['Email, WhatsApp, web chat, portal, phone?', 'Read-only, draft or act in each channel?', 'Which channel goes first?'], 'example': [('Email + WhatsApp Business', 'Agent drafts every reply; coordinator sends at first.'), ('Client portal', 'Agent posts live job status.'), ('Teams channel', 'Daily 8:00 exceptions brief to supervisors.')]},
 {'id': 'customerSeg', 'title': 'Customer Segments', 'prompt': 'Which customer segments gain most from AI agents, and which still want a person?', 'questions': ['Which segment has the biggest pain an agent can fix?', 'Which segment will resist an agent?', 'Any new segment agents let you serve?'], 'example': [('Building managers (clients)', 'Want same-day answers; happy with an agent for status updates.'), ('Premium contracts', 'Expect a named human: agent supports, person serves.'), ('Small offices (new)', 'Low-cost, agent-led service tier becomes viable.')]},
 {'id': 'costStructure', 'title': 'Cost Structure', 'prompt': 'What will the agents cost, and which costs will they remove or add?', 'questions': ['Licences, integration, change, assurance costs?', 'Which costs fall (labour hours, rework)?', 'New risks that carry a cost (PDPA, errors)?'], 'example': [('Year-1 cost SGD 39,000', 'Licences 14k, integration 15k, training and change 10k.'), ('Cost removed', '38% of coordinator time spent re-keying.'), ('Risk cost', 'Human approval for 90 days to avoid misrouted urgent jobs.')]},
 {'id': 'revenueStreams', 'title': 'Revenue Streams', 'prompt': 'How will the agents grow revenue or protect it, and which objective do they serve?', 'questions': ['New or premium service, more volume, fewer lost clients?', 'Baseline today, target in 90 days?', 'Score each opportunity: value x feasibility x data readiness (1-5).'], 'example': [("Premium '2-hour response' tier", 'Agent makes the SLA affordable: +SGD 6k a month (assumption).'), ('Fewer lost contracts', 'Faster answers protect renewals; objective: same-day response.'), ('Scores', 'Triage agent 5x4x4 = 80; report agent 75; predictor 24 (park it).')]}]},
 {'key': 'actionplan', 'num': 2, 'topic': 2, 'lo': 'LO2', 'codes': 'K3, K4, A3, A4', 'layout': 'grid', 'minutes': 155, 'title': 'AI Agent 90-Day Action Plan', 'short': 'Plan the 90 days', 'pitch': 'Five steps to get started: set the goal, mine the process, plug in the agents, name the owner, run a 90-day pilot.', 'evidence': 'PP Task 2 · screenshot of your action plan board', 'discuss': ['Which step of the mined process gives the fastest visible win?', 'What must be true at day 30 for you to keep going?', 'Who is the DRI, and what decision rights do they hold?'], 'blocks': [{'id': 'objective', 'title': '1 · Objective & Outcome', 'prompt': 'Which organisational objective does this serve, and how will you know?', 'questions': ['Baseline, target and date.', 'One counter-metric that must not get worse.'], 'example': [('Same-day response for every client', 'Handling time 18 -> 11 min by day 90; complaints stay at or below 2%.')], 'letter': '1'},
 {'id': 'budget', 'title': '1 · Cost & Value', 'prompt': 'What does it cost and what does it return?', 'questions': ['Year-1 cost, recurring cost.', 'Realised benefit and ROI with a downside case.'], 'example': [('Year 1', 'Cost SGD 39,000; modelled benefit SGD 39,200 at 60% realisation.'), ('Downside', 'At 55% adoption, benefit falls; keep scope small until proven.')], 'letter': '1'},
 {'id': 'mine', 'title': '2 · Mine the Business Process', 'prompt': 'What actually happens today, step by step?', 'questions': ['Trigger, steps, handoffs, waits, rework, decisions.', 'Which dormant data shows it (emails, tickets, logs)?'], 'example': [('As-is triage: 6 steps, 3 handoffs', 'Email -> coordinator reads -> re-keys ticket -> calls client -> assigns -> chases.'), ('Friction', '38% of time spent re-keying; 14% rework from missing details.')], 'letter': '2'},
 {'id': 'integrate', 'title': '3 · Where Agents Plug In', 'prompt': 'Which steps go to an agent, which stay human?', 'questions': ['Inform, recommend, prepare, execute-with-approval, execute-with-monitoring.', 'Name the human checkpoint.'], 'example': [('Agent prepares', 'Reads email, extracts site, fault and urgency, drafts the ticket.'), ('Human approves', 'Coordinator confirms routing for urgent and VIP clients.'), ('Agent monitors', 'Watches SLA timers and alerts the supervisor.')], 'letter': '3'},
 {'id': 'architecture', 'title': '3 · Digital Architecture', 'prompt': 'Which systems, data, agents and controls make it work?', 'questions': ['Data sources, model, connectors (MCP), where people meet the agent, guardrails.', 'Custom, buy or hybrid? Exit option?'], 'example': [('Hybrid', 'Bought ticketing AI add-on + our own routing rules and terms.'), ('Connectors', 'Gmail, WhatsApp Business API, ServiceNow via MCP; read + draft only.'), ('Controls', 'Coordinator approval on urgent jobs; every agent action logged.')], 'letter': '3'},
 {'id': 'owners', 'title': '4 · DRI, Team & Resources', 'prompt': 'Who owns it and what can they mobilise?', 'questions': ['One DRI with decision rights.', 'People, budget, systems and data they may use.'], 'example': [('DRI: Head of Service Desk', 'Decides routing rules; budget SGD 39,000; 2 coordinators as reviewers.'), ('IT', 'Connectors and access reviews.'), ('DPO', 'PDPA check before go-live.')], 'letter': '4'},
 {'id': 'milestones', 'title': '5 · Pilot: 30 / 60 / 90 Days', 'prompt': 'What ships when?', 'questions': ['Quick win in 30 days.', 'Pilot scope at 60; scale decision at 90.'], 'example': [('Day 30', 'Agent drafts tickets for 2 sites; coordinators approve 100%.'), ('Day 60', '10 sites; measure handling time and rework weekly.'), ('Day 90', 'Board review: scale, redesign or stop.')], 'letter': '5'},
 {'id': 'risks', 'title': '5 · Risks & Controls', 'prompt': 'What could go wrong and what stops it?', 'questions': ['Wrong action, data leak, bias, over-reliance.', 'Kill criterion.'], 'example': [('Misrouted urgent job', 'Human approval for urgent tickets; daily sample audit.'), ('Kill criterion', 'Stop if rework rises above 20% for 2 weeks.')], 'letter': '5'},
 {'id': 'kpis', 'title': '5 · Success Measures', 'prompt': 'Which numbers decide scale, redesign or stop?', 'questions': ['Leading and lagging KPIs.', 'Who reviews, how often?'], 'example': [('KPIs', 'Handling time, first-pass accuracy, complaints, coordinator adoption.'), ('Rhythm', 'Weekly DRI review; day-90 board decision.')], 'letter': '5'}]},
 {'key': 'change', 'num': 3, 'topic': 3, 'lo': 'LO3', 'codes': 'K5, K6, A5, A6', 'layout': 'grid', 'minutes': 100, 'title': 'Sustain and Operate with AI Agents (SCALE)', 'short': 'Communicate and run it', 'pitch': 'Five moves to run the business with AI agents: Story, Commanders, Augment people, Loop information, Evaluate.', 'evidence': 'PP Task 3 · screenshot of your SCALE board', 'discuss': ['Which group hears about the change last today, and should hear first?', 'Which manager role becomes a DRI, a coach or a translator?', 'How will staff send you new ideas once the agents are live?'], 'blocks': [{'id': 'story', 'title': 'S · The Change Story', 'prompt': 'Why, what and when, in three sentences anyone can repeat.', 'questions': ['What problem are we solving?', 'What changes and what does not?'], 'example': [('Why', 'Clients wait too long and coordinators drown in re-keying.'), ('What', 'An agent drafts every ticket; people decide, approve and handle clients.'), ('Not changing', 'No one loses their job in the pilot; every client still reaches a person.')], 'letter': 'S'},
 {'id': 'stakeholders', 'title': 'S · Stakeholder Map', 'prompt': 'Who is affected, how much, and what do they worry about?', 'questions': ['Sponsor, DRIs, frontline, clients, unions, regulators.', 'Influence x impact.'], 'example': [('CEO (sponsor)', 'Wants proof by day 90.'), ('Coordinators', 'Fear replacement; want less re-keying.'), ('Clients', 'Want faster answers, not a chatbot wall.')], 'letter': 'S'},
 {'id': 'messages', 'title': 'S · Messages & Channels', 'prompt': 'What does each group hear, from whom, through which channel?', 'questions': ['Town hall, team huddle, email, FAQ, client letter.', 'Two-way: how do they reply?'], 'example': [('Coordinators', 'Huddle with the DRI + hands-on demo; weekly Q&A.'), ('Clients', 'Email from account manager: faster updates, same people.'), ('All staff', 'Intranet FAQ + anonymous question form.')], 'letter': 'S'},
 {'id': 'dri', 'title': 'C · DRIs & Agent Teams', 'prompt': 'Who is the one person accountable for each outcome?', 'questions': ['Decision rights, resource rights, boundaries.', 'Which agents report to which DRI?'], 'example': [('Service DRI', 'Triage agent + SLA watcher; owns handling time.'), ('Client-reporting DRI', 'Report agent; owns report accuracy and on-time delivery.')], 'letter': 'C'},
 {'id': 'workforce', 'title': 'A · Workforce Transition', 'prompt': 'Where will each role land, and how will you help?', 'questions': ['DRI, human-to-human, rubber-stamp, rule-bound work.', 'Reskilling and coaching plan.'], 'example': [('Senior coordinators', 'Become DRIs or coaches; 6-week agent-management training.'), ('Coordinators', 'Move to client calls and exception handling (human-to-human work).'), ('Managers who only relay', 'Retrain as translators who move tacit know-how into the company map.')], 'letter': 'A'},
 {'id': 'guardrails', 'title': 'A · Guardrails & Judgement', 'prompt': 'How do you keep people genuinely judging, not rubber-stamping?', 'questions': ['Atrophy trap: where could approval become a click?', 'PDPA, security, audit trail.'], 'example': [('Sample audits', 'Reviewers re-do 5 tickets a week unassisted.'), ('Audit trail', 'Every agent action logged with who asked and when.')], 'letter': 'A'},
 {'id': 'rhythm', 'title': 'L · Information Flow & Rhythm', 'prompt': 'How does information flow without layers of relay?', 'questions': ['Dashboards, daily brief, weekly review, monthly board.', 'Who sees what, when?'], 'example': [('Daily 8:00', 'Agent posts exceptions brief to the team channel.'), ('Weekly', 'DRI reviews KPIs and agent errors with coordinators.'), ('Monthly', 'Leadership sees one dashboard: KPIs, risks, ideas.')], 'letter': 'L'},
 {'id': 'ideas', 'title': 'L · Idea Pipeline', 'prompt': 'How do staff share and develop the next innovation?', 'questions': ['Where do ideas go? Who reviews them?', 'How do good ideas get a DRI and a budget?'], 'example': [('Idea board', 'Any staff posts an idea; the agent clusters them weekly.'), ('Monthly pitch', 'Top 3 ideas pitched to leadership; winner gets a DRI and 30 days.')], 'letter': 'L'},
 {'id': 'success', 'title': 'E · Evaluate: Review Success', 'prompt': 'How will you judge whether the innovation worked?', 'questions': ['KPIs vs baseline, adoption, quality, cost.', 'Scale, redesign, hold or stop: who decides?'], 'example': [('Day-90 review', 'Handling time 10.7 min, quality 95.1%, complaints 1.7%, adoption 77.5%.'), ('Decision', 'Scale to all 30 sites with the same approval rules.')], 'letter': 'E'}]}]
CANVAS = {c["key"]: c for c in CANVASES}

# LO2 plan (numbered steps label the Activity 2 board) / LO3 SCALE letters (Activity 3 board)
PLAN = [("1", "Set the goal", "Objective, baseline, target and counter-metric; cost and value", "target"),
        ("2", "Mine the process", "Map the real business process from dormant data", "search"),
        ("3", "Plug in the agents", "Where agents plug in, and the architecture they work in", "layers"),
        ("4", "Name the owner", "One DRI with decision and resource rights", "flag"),
        ("5", "Run a 90-day pilot", "30/60/90 pilot, risks and controls, success measures, stop rule", "flask")]
AGENT = PLAN   # v43 name kept as an alias for older imports
SCALE = [("S", "Story", "Tell every stakeholder what changes and what does not", "megaphone"),
         ("C", "Commanders", "DRIs lead agent teams; relay layers fade out gradually", "flag"),
         ("A", "Augment people", "Reskill, train for adoption, keep people judging", "users"),
         ("L", "Loop information", "Daily brief, weekly review, monthly dashboard, idea pipeline", "loop"),
         ("E", "Evaluate", "KPIs vs baseline, ROI, governance: scale, redesign, hold or stop", "chart")]

# --------------------------------------------------------------------------- the three labs (one per LO = one per activity)
# Each lab is the hands-on activity with Meta Muse: prompt steps feed the group board in the Activity Studio.
# step.prompt == 'BOARD' means the activity's board-drafting prompt (CANVAS[canvas]['muse_prompt']).
MUSE_WEB = "https://muse.ai/"
MUSE_CODE = "H1KWDZ"
MUSE_IOS = "https://apps.apple.com/sg/app/muse-from-meta/id6760173601"
MUSE_ANDROID = "https://play.google.com/store/apps/details?gl=sg&id=com.facebook.aura"
MUSE_LINKS = [("iPhone · App Store", MUSE_IOS), ("Android · Google Play", MUSE_ANDROID), ("Laptop · muse.ai", MUSE_WEB)]
LABS = [{'n': 1, 'canvas': 'opportunity', 'topic': 1, 'title': 'Business Model Canvas for AI Agents', 'minutes': 110, 'goal': 'In groups of 3-5, join one shared board and create a nine-block BMC for one member\'s company; evaluate its AI agent opportunities.', 'steps': [{'title': 'Get Meta Muse: phone app or website', 'part': 'A', 'links': 'MUSE', 'body': ["Use the Meta Muse phone app OR the muse.ai website: both work for every activity. Phone app: iPhone - open the App Store, search 'Muse from Meta' (or scan the QR code), tap Get. Android - open Google Play, search 'Muse from Meta' (or scan the QR code), tap Install.", 'Open the app and sign in with your Facebook (Meta) account. Allow notifications if asked, so the always-on agent can reach you.', 'Website: on a laptop or any browser, go to muse.ai, click Log in or Sign up, continue with your Facebook (Meta) account and finish the short onboarding.', "Redeem the trainer's invite code: Settings > General > Usage > Redeem invite code, key in H1KWDZ within 48 hours of joining.", 'Tip: using the phone app? Download the current activities/prompts.html from the LMS course materials and open it in a browser on the same device for copy and paste.', "No Facebook account? Ask your trainer to pair you with a partner for this activity; never sign in with someone else's account."], 'prompt': 'Introduce yourself in three sentences: what you can do for a business manager, what you need access to, and what you will always ask me before doing.', 'check': 'Muse is installed (phone) or open at muse.ai (laptop), you are signed in, and it answers with what it will always ask before doing.'},
 {'title': 'Connect Gmail and Google Calendar', 'part': 'A', 'body': ['Settings > Connectors > Connect beside Gmail > Continue; finish the Google sign-in.', 'Repeat for Google Calendar.', 'Choose read-only access where offered. Approve every send yourself.'], 'prompt': 'Confirm which of my apps you are connected to, and what you can and cannot do in each one.', 'check': 'Gmail and Calendar show as connected; Muse says it cannot send without your approval.'},
 {'title': 'Feel the always-on agent: triage your inbox', 'part': 'A', 'body': ['Let Muse keep watch on your inbox and rank only what needs you.'], 'prompt': "Triage my inbox down to only what matters. Mute newsletters, promotions and routine alerts. Keep a ranked list of the five emails that need me, with one line on why each matters, and keep it current as new mail arrives. Rule: anything from [your boss's name] is always in the top three.", 'check': 'A ranked list of up to five emails, each with a reason; newsletters are excluded.'},
 {'title': 'Ask Muse for the agentic AI opportunities', 'part': 'B', 'body': ['Describe your own organisation and let Muse suggest and rank the opportunities.'], 'prompt': "My organisation: [your organisation in two sentences: industry, size, customers, this year's objective]. Suggest six opportunities where an AI agent or agentic workflow could help. For each: the process it improves, the dormant data it uses, the human who stays accountable, and which of these gaps it must overcome: private data, internal language, live context, ability to act, guardrails. Then rank them by value x feasibility x data readiness and argue against your top choice.", 'check': 'Six opportunities, each with a process, data source, accountable human and capability gap; a counter-argument for #1.'},
 {'title': 'Return to your group board', 'part': 'B', 'studio': 'join', 'body': ['Reopen the Activity 1 board your group created at the start. Use the same Board ID; do not create a second board.', 'Stay in your group of 3-5 and use the company chosen at the start. The leader creates ONE Activity 1 board with the group and company name; everyone joins using its Board ID or QR and their own name.']},
 {'title': 'Let Muse draft the whole canvas', 'part': 'B', 'studio': 'muse', 'prompt': 'BOARD', 'body': ['On the board, click Copy Muse prompt (or use the prompt templates page) and fill in your organisation.', "Paste it into Meta Muse. Copy Muse's whole reply.", 'On the board, click Paste Muse answer, tick the lines you agree with, click Add.']},
 {'title': 'Refine it together', 'part': 'B', 'studio': 'refine', 'body': ['Check every note: is it specific, owned and true? Delete guesses; type better answers into each block.', "Click View example, or open Meridian's demo board, to see a finished board; then make every note about your own organisation.", 'Score your top three opportunities in Value & Objectives Fit.']},
 {'title': 'Capture your evidence', 'part': 'B', 'studio': 'capture', 'body': ['Click Screenshot view, then Download PNG or Download PDF.', 'Keep it for PP Task 1. You will answer the PP questions on your own.']}]},
 {'n': 2, 'canvas': 'actionplan', 'topic': 2, 'title': 'AI Agent 90-Day Action Plan', 'minutes': 155, 'goal': 'In groups of 3-5, use one member’s company and complete all nine boxes of its 90-day action plan on one shared board. Use Meridian’s filled plan as a guide.', 'steps': [{'title': 'Mine your business process from dormant data', 'part': 'A', 'body': ['Pick one recurring process you handle: approvals, quotes, scheduling or reporting.'], 'prompt': "Look at my emails and calendar from the last 30 days about [process, e.g. 'client quotations']. Reconstruct how this process actually runs: the trigger, each step, who does it, the handoffs, how long things wait, and where work is redone. Show it as a numbered list, then list the three biggest frictions with the evidence (email subject or meeting) for each.", 'check': 'Each step and friction cites a real email or meeting; you corrected anything Muse guessed.'},
 {'title': 'Draft your company map', 'part': 'A', 'body': ['Let Muse write the terms, relationships and rules an agent needs; correct every definition that differs from how your company really works.'], 'prompt': 'For the process [process name], draft a company map for an AI agent: (1) the 6 key entities, (2) a definition of 5 terms the way my company uses them - ask me when unsure instead of guessing, (3) how the entities relate, (4) the approvals and thresholds that apply, (5) the events that should update the map in real time.', 'check': 'Muse asked at least one clarifying question; your corrections are in the final map.'},
 {'title': 'Draft the 90-day action plan', 'part': 'B', 'body': ['Paste your top opportunity from Activity 1 and your company map from Step 2.'], 'prompt': 'Using this opportunity [paste your top opportunity from Activity 1] and this company map [paste your company map from Step 2], draft a 90-day action plan in five steps: 1 - Set the goal: objective with baseline, target and one counter-metric, plus year-1 cost and value; 2 - Mine the process: the as-is process steps and the three biggest frictions; 3 - Plug in the agents: where agents plug in (the decision level at each step) and the architecture (data, model, company map, connectors, guardrails; custom, buy or hybrid); 4 - Name the owner: one DRI with decision rights, team and budget; 5 - Run a 90-day pilot: 30/60/90 milestones, risks and controls, KPIs and a kill criterion.', 'check': 'The plan covers all five steps; every milestone has an owner and a measurable result; there is a kill criterion.'},
 {'title': 'Return to your group board', 'part': 'B', 'studio': 'join', 'body': ["Open alfredang.github.io/bcm and pick Activity 2, or scan your trainer's QR code; join your group board."]},
 {'title': 'Let Muse draft the whole action plan board', 'part': 'B', 'studio': 'muse', 'prompt': 'BOARD', 'body': ['Click Copy Muse prompt on the board, fill in your organisation, paste it into Meta Muse.', "Copy Muse's reply; on the board click Paste Muse answer, tick the lines you agree with, click Add."]},
 {'title': 'Refine it together', 'part': 'B', 'studio': 'refine', 'body': ['Go block by block, 1 to 5: check step 2 against what you mined, name one DRI, make every milestone measurable.', "Compare with View example or Meridian's demo board (link on the activity card)."]},
 {'title': 'Capture your evidence', 'part': 'B', 'studio': 'capture', 'body': ['Screenshot view, then Download PNG or PDF. Keep it for PP Task 2.']}]},
 {'n': 3, 'canvas': 'change', 'topic': 3, 'title': 'Sustain and Operate with AI Agents (SCALE)', 'minutes': 100, 'goal': 'Use the SCALE framework (Story, Commanders, Augment people, Loop information, Evaluate) to run the business with AI agents; Meta Muse drafts, your group decides.', 'steps': [{'title': 'S · Story: draft the change messages for each stakeholder', 'part': 'A', 'body': ['Write your change story and stakeholder map in a few lines first. Muse drafts; nothing is sent.'], 'prompt': "Here is our change story [paste your change story] and stakeholder map [paste your stakeholder map]. Draft three messages: (1) five talking points for a coordinator huddle that answer 'will I lose my job?' honestly, (2) a 120-word email to clients from their account manager, (3) a one-paragraph update for the leadership team with the day-90 decision gate. Do not send anything. Show me the drafts.", 'check': 'Three drafts; nothing sent; each message says what changes and what does not.'},
 {'title': 'L · Loop information: run the weekly innovation review', 'part': 'A', 'body': ['Set up the information flow: KPIs, blockers, decisions and staff ideas, every Friday.'], 'prompt': "Every Friday I review our AI initiative [initiative name]. From this week's emails and meetings, prepare: KPIs mentioned vs target, blockers, decisions I must make, and new ideas staff raised (with who raised them). End with one question I should ask the team on Monday.", 'check': 'The review cites real emails or meetings; ideas are credited to the people who raised them.'},
 {'title': 'Join your group board', 'part': 'A', 'studio': 'join', 'body': ["Open alfredang.github.io/bcm and pick Activity 3, or scan your trainer's QR code; join your group board."]},
 {'title': 'Let Muse draft the whole SCALE board', 'part': 'A', 'studio': 'muse', 'prompt': 'BOARD', 'body': ['Click Copy Muse prompt, fill in your organisation, paste it into Meta Muse.', 'Copy the reply; Paste Muse answer on the board; tick and Add.']},
 {'title': 'Refine it together', 'part': 'A', 'studio': 'refine', 'body': ['Go block by block, S to E: is every message honest, every DRI named, every guardrail real, every review metric measurable?', "Compare with View example or Meridian's demo board (link on the activity card)."]},
 {'title': 'E · Evaluate: judge before you ask', 'part': 'B', 'body': ["Write your group's scale/redesign/stop decision yourselves first, then let Muse attack it. Update the Review Success block."], 'prompt': 'Here is my decision on our AI pilot and my reasons [paste your scale/redesign/stop decision and reasons]. Do not give me your answer. Attack my reasoning: list the three weakest points, the evidence I am missing, and one question that would change my mind. Give hints, not a rewritten decision.', 'check': 'Your final decision is in your own words; you can name what changed it.'},
 {'title': 'Capture your evidence', 'part': 'B', 'studio': 'capture', 'body': ['Screenshot view, then Download PNG or PDF. Keep it for PP Task 3.']}]}]
# A short try-out immediately after the agent catalogue; not a fourth PP activity.
MINI_MUSE = dict(n=0, topic=1, mini=True, title="Try Meta Muse", minutes=20,
                 steps=LABS[0]["steps"][:3])
LABS[0]["steps"] = LABS[0]["steps"][3:]
LABS[0]["minutes"] = 80
for i, step in enumerate(LABS[0]["steps"]): step["part"] = "A" if i < 3 else "B"
LABS[0]["steps"][1]["title"] = "Join your group board"
LABS[0]["steps"][1]["body"][0] = "Use the ONE Activity 1 board created by your group leader. Join with its Board ID or QR code and your own name."
# v58 (owner, 28 Nov 2026): keep the mini activity simple: connect Muse to email, find the most important emails, make a 15-second ad.
MINI_MUSE["steps"] = [
 dict(title="Connect Muse to your email", part="A", links="MUSE",
      body=["Open Muse (phone app or muse.ai), then Settings > Connectors > Connect beside Gmail and finish the Google sign-in.",
            "No Muse yet? Install 'Muse from Meta' or open muse.ai, sign in with your Facebook (Meta) account and redeem the invite code H1KWDZ.",
            "Choose read-only access where offered. Muse must ask before it sends anything.",
            "No Facebook account? Pair with a partner; never sign in with someone else's account."],
      prompt="Which email account are you connected to? Tell me what you can do in it, and what you will always ask me before doing.",
      check="Gmail shows as connected, and Muse says it will not send anything without your approval.",
      then="Tell your neighbour one thing Muse can now see, and one thing it will never do without you."),
 dict(title="Ask for your most important emails", part="A",
      body=["Let Muse read your inbox and pick out what needs you today. Nothing in the mailbox should change."],
      prompt="What are my most important emails right now? List the top five, with one line each on why it matters and what I should do next. Skip newsletters, promotions and automatic alerts. Do not send, archive or delete anything.",
      check="Five emails ranked, each with a reason and a next action; nothing in your mailbox changed.",
      then="Did Muse rank anything you would not? Ask it why, then correct it in one line."),
 dict(title="Make a 15-second social media ad", part="A",
      body=["Pick a product or service you are allowed to promote. Ask Muse for a 15-second ad presented by an AI human avatar.",
            "Label AI-generated content and check every product claim before anything is posted."],
      prompt="Create a 15-second social media video ad for [your product or service], presented by an AI human avatar, for [your target customers]. Hook them in the first 3 seconds, show one clear benefit, and end with one call to action. If you cannot make the video here, give me the script with timings (0-3 s, 3-12 s, 12-15 s), the avatar's look and voice, and the on-screen text.",
      check="A 15-second video, or a script whose timings add up to 15 seconds, with a hook, one benefit and a call to action.",
      then="Share your best hook with the group. Who in your company must approve an ad before it posts?"),
]
LABS[1]["steps"][1]["prompt"] += " Also identify the current SOP and policy owner, version and effective date; specify allowed tools, prohibited actions, approval thresholds, exception escalation and one worked example. If a rule is missing or contradictory, ask the process owner rather than inventing it."
LABS[1]["steps"][1]["check"] = "Corrected definitions and relationships, current policy sources, two approval rules, permitted actions, one live event and one exception case; the process owner validates the map."
LAB = {L['n']: L for L in LABS}

# Adapted from TGS-2024043854, Human–AI Workforce v3.10, slide 60.
AGENT_COMPONENTS = [
    ("brain", "Model", "Reasons and proposes the next action."),
    ("tool", "Tools", "Read records, calculate and act."),
    ("book", "Skills", "Reusable procedures and checks."),
    ("memory", "Memory", "Approved facts carried across tasks."),
    ("folder", "Knowledge base", "Curated documents and evidence."),
    ("file", "Instructions", "Goal, policy and expected output."),
    ("shield", "Runtime controls", "Loop, permissions, limits and logs."),
]
CLAUDE_CODE_COMPONENT_EXAMPLES = {
    "Model": "Opus, Sonnet, Haiku via /model",
    "Tools": "Read, Edit, Bash and MCP tools",
    "Skills": ".claude/skills/<name>/SKILL.md",
    "Memory": "Auto memory (MEMORY.md)",
    "Knowledge base": "Repo, docs and @-mentioned files",
    "Instructions": "Your prompt and CLAUDE.md",
    "Runtime controls": "Permissions, hooks and settings.json",
}
CLAUDE_CODE_COMPONENT_SOURCE = "https://code.claude.com/docs/en/features-overview"

# Concise worked answers for all nine boxes on the learner-facing plan.
MERIDIAN_PLAN_BOXES = {
    "objective": "Same-day response. Cut handling time from 18 to ≤11 min by day 90. Keep complaints at ≤2%.",
    "budget": "Year 1 costs SGD 39,000. Modelled benefit SGD 39,200 at 60% realisation. Test a lower-adoption case.",
    "mine": "Map six steps and three handoffs. Ticket traces show missing details and rework. Baseline rework 14%.",
    "integrate": "Agent checks details, drafts tickets and flags urgent cases. Coordinator approves dispatch.",
    "architecture": "Hybrid: ticketing add-on and Meridian rules. Read and draft access, approval gates and action logs.",
    "owners": "Head of Service Desk owns results and budget. Two coordinators review. IT manages connectors and access.",
    "milestones": "Day 30: 2 sites with full review. Day 60: 10 sites if checks pass. Day 90: board decides whether to scale.",
    "risks": "Escalate urgent jobs to the duty coordinator. Pause if rework exceeds 20% for two weeks.",
    "kpis": "Weekly review: handling time, accuracy, rework and complaints. Day 90: scale, redesign or stop.",
}

MERIDIAN_SCALE_BOXES = {
    "story": "Shorten queues. Agents draft tickets, people approve dispatch. No job losses during the pilot.",
    "stakeholders": "Sponsor: CEO. Coordinators redesign handoffs. Clients test updates. DPO checks tenant-data use.",
    "messages": "Supervisor runs staff huddles and Q&A. Account manager explains faster updates and the human contact.",
    "dri": "Head of Service Desk owns handling time and quality. Can change rules, grant access via IT and pause the agent.",
    "workforce": "Shift coordinators from re-keying to follow-up and exceptions. Coach on live tasks with a weekly check-in.",
    "guardrails": "Coordinators approve dispatch. Log decisions. Supervisors re-check five tickets each week without AI.",
    "rhythm": "Daily agent exceptions brief. Weekly DRI feedback review. Monthly dashboard for the sponsor.",
    "ideas": "Staff submit issues and ideas. DRI assigns an owner, tests changes and tells staff what happened.",
    "success": "Day 90: 10.7 min, 95.1% quality, 1.7% complaints. Board scales to 30 sites with the same approvals.",
}

WORKFORCE_SOURCES = {
    "wef": "https://www.weforum.org/publications/the-future-of-jobs-report-2025/2-jobs-outlook",
    "mom": "https://www.mom.gov.sg/newsroom/press-releases/2026/1030-labour-market-advance-release-3q-2026",
    "imda": "https://www.imda.gov.sg/-/media/imda/files/about/resources/corporate-publications/annual-report/imda-sgde-report-fy2024-2025.pdf",
}

HUMAN_OWNER_RIGHTS = [
    ("target", "Direct", "Set the goal and limits on data, tools and actions."),
    ("search", "Challenge", "Check evidence and test assumptions."),
    ("check", "Decide", "Approve consequential actions and release decisions."),
    ("alert", "Escalate", "Handle exceptions, pause work and own recovery."),
    ("tool", "Improve", "Update instructions, tools and rules based on results."),
]

PILOT_METRICS = [
    ("Productivity", "Completed requests per staff hour or staff minutes per request"),
    ("Revenue growth", "Change in eligible revenue or renewals against a comparable baseline"),
    ("Cost reduction", "Cost per resolved case, including tools, training and human review"),
    ("Customer satisfaction", "Customer satisfaction score and complaints per 100 requests"),
    ("Defects and returns", "Reworked tickets, defective outputs or returned orders as a share of total"),
    ("Operational efficiency", "Time from receipt to resolution and share completed within the SLA"),
    ("Missed schedules", "Missed appointments or deadlines as a share of scheduled work"),
]

PILOT_RUBRIC = [
    ("Scale", "Core targets met, quality limits respected and evidence supports the result.", "10.7 min and 1.7% complaints meet the targets. Verify rework and controls before expanding."),
    ("Redesign or hold", "A target is missed or evidence is incomplete. Fix the cause and retest.", "If handling is 13 min with complaints within limit, investigate delays and retest."),
    ("Stop", "A stop rule is triggered. Pause the agent and revert to the human workflow.", "Pause if rework exceeds 20% for two consecutive weeks."),
]

PROCESS_MINING_SOURCE = "https://www.vdaalst.com/publications/p658.pdf"
PROCESS_MINING_TRACES = [
    ("M-101", "09:00 Request → 09:04 Draft → 09:10 Approval → 09:12 Dispatch", "12 min"),
    ("M-102", "09:00 Request → 09:04 Draft → 09:08 Returned for details → 09:45 Redraft → 09:50 Approval → 09:53 Dispatch", "53 min"),
    ("M-103", "09:00 Request → 09:04 Draft → 09:08 Dispatch", "8 min"),
]

AGENT_BRIEFING = [
    ("Business purpose", "Products, customers, service promises and success measures", "Meridian: draft accurate triage tickets; target 18 to 11 minutes per request."),
    ("Operations and process", "Trigger, steps, roles, handoffs, systems, inputs and outputs", "Request arrives → classify → draft ticket → coordinator approves → dispatch → close."),
    ("Company language and data", "Entity definitions, relationships, permitted records and live status", "Link each building to its contract, assets, service level and responsible coordinator."),
    ("Policies and authority", "Approved SOPs, versions, thresholds, exclusions and escalation owner", "Urgent leak: alert the duty coordinator; no autonomous dispatch, refunds or external sends."),
    ("Examples and validation", "Good cases, exceptions, expected outcomes and a named reviewer", "Test routine, urgent, incomplete and conflicting requests; owner signs off before the pilot.")
]


# Topic 1 BMC teaching rows: definition, agent use and business benefit; all Meridian figures are synthetic.
BMC_BENEFITS = [
    ("Customer Segments", "Who the business serves", "Building managers need fast status updates; premium clients keep a named human.", "A routine service agent frees account managers for complex client needs."),
    ("Value Propositions", "Why customers choose it", "Triage drafts tickets and tracks requests around the clock.", "Faster acknowledgement and clearer job status; urgent faults still escalate to people."),
    ("Channels", "How the business reaches customers", "Agents draft email and WhatsApp replies and prepare portal updates.", "More consistent updates across channels; coordinators approve sends during the pilot."),
    ("Customer Relationships", "How customers are supported and retained", "Routine status queries go to the agent; complaints and refunds go to coordinators.", "Responsive service with a reachable human; the service-desk head owns quality."),
    ("Revenue Streams", "How the business earns money", "Test a premium two-hour response tier; faster updates may protect renewals.", "A possible SGD 6,000/month uplift is an assumption to validate, not booked revenue."),
    ("Key Activities", "What the business must do well", "Agents draft triage tickets, propose schedules and compile client reports.", "Less re-keying and reporting work; supervisors retain dispatch decisions."),
    ("Key Resources", "The assets and know-how it needs", "Use permitted tickets, technician notes and coordinator routing knowledge.", "Make operational knowledge reusable; clean and mask data before access."),
    ("Key Partners", "The external parties it relies on", "Ticketing vendor, agent platform and building owners agree data/API access.", "Connect the service workflow with clear access rights and partner responsibilities."),
    ("Cost Structure", "What running the business costs", "Budget SGD 39,000 in year one for licences, integration, training and change.", "Test whether time saved exceeds full costs; include human review and assurance.")
]

# --------------------------------------------------------------------------- schedule (9:30-18:30, 8 training hours a day)
# (start, end, minutes, kind, text, topic)
# (start, end, minutes, kind, text, LU) - LU durations follow the approved CP: LU1 4 h, LU2 6 h, LU3 4 h (+ 2 h assessment).
LU_HOURS = {1: 4, 2: 6, 3: 4}
SCHEDULE = {
 1: [
  ('9:30', '9:50', 20, 'admin', 'Welcome, digital attendance, trainer, learning outcomes, ground rules, course materials and the SkillsFuture free AI subscription', 1),
  ('9:50', '10:25', 35, 'topic', 'Topic 1 (Part A) - AI history; 2023-2026 lenses; Agent Stairway; agentic AI and always-on agents; seven components with Claude Code examples', 1),
  ('10:25', '10:45', 20, 'lab', 'Mini Activity - Try Meta Muse: sign in, connect permitted apps and try a read-only inbox brief; discuss ongoing monitoring and approvals', 1),
  ('10:45', '11:00', 15, 'break', 'Tea break', 1),
  ('11:00', '11:35', 35, 'topic', 'Topic 1 (Part B) - always-on agents, deployment and product comparison, Singapore news; science and mathematics; five collaboration scenarios; OPC evidence and policy targets; software/SaaS interface, service, video, paper-trading and scientific agent teams', 1),
  ('11:35', '12:10', 35, 'topic', 'Topic 1 (Part C) - Meridian scenario; nine-block BMC; agent benefits across all dimensions; gaps, value and scoring; completed Meridian BMC', 1),
  ('12:10', '12:40', 30, 'activity', 'Activity 1 (Part A) - groups of 3-5 choose one company, create and join one board, ask for opportunities and draft its BMC', 1),
  ('12:40', '13:40', 60, 'lunch', 'Lunch break', 0),
  ('13:40', '14:30', 50, 'activity', 'Activity 1 (Part B) - verify and refine all nine BMC blocks, score opportunities and capture individual PP Task 1 evidence', 1),
  ('14:30', '14:55', 25, 'topic', 'Topic 2 (Part A) - Steps 1 and 2: set the goal and mine the process using dormant data, event logs and Meridian ticket traces', 2),
  ('14:55', '15:55', 60, 'topic', 'Topic 2 (Part B) - Step 3: choose agent roles and approvals, then design the decision layer, company map, policies and access', 2),
  ('15:55', '16:10', 15, 'break', 'Tea break', 2),
  ('16:10', '17:10', 60, 'topic', 'Topic 2 (Part C) - finish Step 3 sourcing. Step 4 name the owner. Step 5 run and evaluate the pilot. Meridian scenario and completed nine-box plan', 2),
  ('17:10', '18:15', 65, 'activity', 'Activity 2 (Part A) - groups of 3-5 choose a company, mine its process and draft its company map', 2),
  ('18:15', '18:30', 15, 'recap', 'Day 1 recap, Q&A and PM digital attendance', 2),
 ],
 2: [
  ('9:30', '9:45', 15, 'recap', 'Day 1 recap and AM digital attendance', 2),
  ('9:45', '11:15', 90, 'activity', 'Activity 2 (Part B) - Muse drafts the 90-day action plan and the group board; the group refines it (PP Task 2 evidence)', 2),
  ('11:15', '11:30', 15, 'break', 'Tea break', 2),
  ('11:30', '12:20', 50, 'topic', 'Topic 3 (Part A) - transformation challenges, then SCALE: Story and communication, Commanders and phased rollout, Augment people through job-market evidence, human ownership, job redesign and AI Coaching', 3),
  ('12:20', '13:00', 40, 'topic', 'Topic 3 (Part B) - Loop information through staff and client feedback. Evaluate governance, five agent risks, security and human oversight', 3),
  ('13:00', '14:00', 60, 'lunch', 'Lunch break', 0),
  ('14:00', '14:20', 20, 'topic', 'Topic 3 (Part C) - Evaluate results against targets and review the Meridian scenario and all nine completed SCALE boxes before Activity 3', 3),
  ('14:20', '15:35', 75, 'activity', 'Activity 3 (Part A) - Muse drafts the change messages and weekly review; Muse drafts the group board; the group refines it (PP Task 3 evidence)', 3),
  ('15:35', '15:50', 15, 'break', 'Tea break', 3),
  ('15:50', '16:15', 25, 'lab', "Activity 3 (Part B) - judge before you ask: test your group's decision against Muse; capture the board; gallery walk and debrief", 3),
  ('16:15', '16:30', 15, 'assess', 'Course recap and Briefing for Assessment', 3),
  ('16:30', '17:30', 60, 'assess', 'Written Assessment (WA-SAQ) - 1 hour, open book; TRAQOM survey and assessment attendance first', -1),
  ('17:30', '18:30', 60, 'assess', 'Practical Performance (PP) - 1 hour, open book; paste the group board screenshots; upload on the LMS or hand in a printed copy', -1),
 ],
}

# --------------------------------------------------------------------------- Muse drafts each board
def muse_prompt(cv):  # block titles carry the plan step numbers / SCALE letters
    """Copy-ready Meta Muse prompt that drafts every block of an activity board, in a paste-ready format
    (the board's "Paste Muse answer" helper matches lines by block number and title)."""
    blocks = "\n".join(f"{i+1}. {b['title']}: {b['prompt']}" for i, b in enumerate(cv["blocks"]))
    return (f"Act as my innovation consultant. Our organisation: [your organisation in two sentences: industry, size, customers, this year's objective]. "
            f"Draft our {cv['title']} with these {len(cv['blocks'])} blocks:\n{blocks}\n\n"
            f"Rules: two specific notes per block, at most 15 words each, with names, numbers and owners. Use my email and calendar "
            f"only where relevant and name the source. Mark guesses as (assumption).\n"
            f"Reply ONLY in this format, so I can paste it into our board:\n"
            f"1. {cv['blocks'][0]['title']}\n- first note\n- second note\n2. {cv['blocks'][1]['title']}\n- first note\n- second note\n"
            f"(continue to block {len(cv['blocks'])}). End with: Verify first: the three notes I should check.")
for _c in CANVASES: _c["muse_prompt"] = muse_prompt(_c)

# --------------------------------------------------------------------------- AI Native key concepts (Kai-Fu Lee, AI Native, 2026)
# term, one-line gist, definition (paraphrased from the book), example, chapter, icon
AI_NATIVE = [
 dict(term="Agent Stairway", gist="Chatbot → agentic workflow → agentic AI → AI agents", ch=3, icon="trend",
      definition="Four steps of AI help: a chatbot answers; an agentic workflow runs fixed steps you designed, with the model doing each step; agentic AI takes a goal and chooses its own steps, tools and checks; AI agents run as persistent workers that watch for work and act within limits between your requests. The big jump is from workflow to agentic AI: you stop scripting the steps and start delegating the goal.",
      example="Agentic workflow: every new email is summarised and filed by a fixed flow. AI agent: watches the inbox overnight, handles the routine and asks you only about the exceptions."),
 dict(term="Five capability gaps", gist="Why smart models stall", ch=6, icon="alert",
      definition="Out of the box, a model does not know your private data or your internal language, cannot see live changes, cannot act in your systems and has no guardrails.",
      example="It cannot tell what 'active customer' means in your company."),
 dict(term="Dormant data", gist="The honest record nobody reads", ch=6, icon="memory",
      definition="The second, unofficial record of a company: meeting audio, chats, edit history, tickets, code logs, photos and system logs. Messy but truthful. Digitising the business starts here: AI agents can now read this record and turn it into evidence for decisions.",
      example="A ticket closed as 'resolved' that the same customer reopens the next day."),
 dict(term="Enterprise AI decision layer", gist="Brain + map + navigation + OS", ch=6, icon="layers",
      definition="The system that lets AI agents work safely across the company: a model (brain), a company map (your business glossary and rules), live events (navigation) and an operating system that schedules, tests, connects and controls every agent.",
      example="A better model moves you from D to D+; the other three parts take you to A."),
 dict(term="Company map (ontology)", gist="Your business, defined for AI", ch=6, icon="map",
      definition="The definitions an AI agent needs before it can act: your business terms, entities, relationships and approval rules (customer, contract, approval). Written in plain language by the people who run the business.",
      example="'Closed' = technician sign-off AND client confirmation, not just 'job done'."),
 dict(term="Live navigation", gist="The map, updated every second", ch=6, icon="route",
      definition="The real-time record of what is happening (deals signed, approvals given, payments missed) that keeps the map current, so the AI knows what is actually happening, not just what should.",
      example="An overdue payment instantly flags every risk assessment for that customer."),
 dict(term="AI flywheel", gist="Advantage that compounds", ch=6, icon="loop",
      definition="A closed loop in which agents, skills and company knowledge improve with every task. It replaces old moats: the earlier you start, the further ahead you pull. Commit, capture knowledge, choose learning agents, start small, connect the loops.",
      example="Each resolved ticket teaches the triage agent; its routing gets better every week."),
 dict(term="Boss AI", gist="The CEO's God's-eye view", ch=7, icon="eye",
      definition="A leader's agent system built on the decision layer that reads dormant data to see the company as it really is, beating the 'lossy compression' of reports filtered at every level. Four engines: perception, performance monitoring, strategic reasoning, talent management.",
      example="It flags 'high-intent' deals that have not replied in weeks before the quarter ends."),
 dict(term="DRI (Directly Responsible Individual)", gist="One name, one outcome", ch=8, icon="flag",
      definition="The one person accountable for an outcome: a single named person who owns the result and holds the decision rights. A DRI sets goals for a team of AI agents, checks their work and answers for the result; agents bring capability, the DRI brings accountability.",
      example="The Head of Service Desk owns handling time and commands the triage and SLA agents."),
 dict(term="Smart flattening", gist="Codify first, then flatten", ch=8, icon="layers",
      definition="Remove relay layers gradually: capture tacit knowledge in the decision layer, find DRIs through real agent tests, give them authority, and let information-passing roles fade, never by decree.",
      example="Bayer went from 12-13 layers to 6-7 over a planned three-year journey."),
 dict(term="Atrophy trap", gist="Judgement decays with disuse", ch=9, icon="pause",
      definition="Relying on AI without thinking weakens human judgement ('cognitive surrender'). Keep judging: ask for hints before answers, write your view first, keep some work unassisted.",
      example="Doctors' detection rate fell from 28.4% to 22.4% after their AI tool was taken away."),
]
AI_NATIVE_BY = {c["term"]: c for c in AI_NATIVE}


# =========================================================================== v53 (22 Nov 2026): consultant flow
# Discover (T1) -> Prove (T2) -> Transform (T3). Owner brief: test and evaluate agents in Topic 2; a deep, company-wide AI
# transformation in Topic 3 (stakeholders, org chart, job redesign, training, coaching, AI built into processes so it survives
# staff turnover, token cost, security, governance and policies). Board block titles are unchanged (PP evidence, v44 papers).
SCHEDULE = {
 1: [
  ('9:30', '9:50', 20, 'admin', "Welcome, digital attendance, trainer, learning outcomes, your role as your company's AI consultant, ground rules, course materials and the SkillsFuture free AI subscription", 1),
  ('9:50', '10:40', 50, 'topic', 'Topic 1 (Part A) - live poll; where companies get stuck; AI history and the 2023-2026 lenses; Agent Stairway (chatbot, agentic workflow, agentic AI, AI agents); always-on agents; the seven components; tools and skills; what leaders say about AI agents; six always-on agents, one page each', 1),
  ('10:40', '11:00', 20, 'lab', 'Mini Activity - Try Meta Muse: connect your email, ask for your most important emails, then ask for a 15-second social media ad with an AI human avatar', 1),
  ('11:00', '11:15', 15, 'break', 'Tea break', 1),
  ('11:15', '12:10', 55, 'topic', 'Topic 1 (Part B) - Singapore and AgentSea; five ways humans and agents team up; use cases by function; nine-block BMC and the Meridian scenario; five capability gaps; value levers and opportunity scoring; Meridian demo: how to fill each BMC block; choose the first pilot', 1),
  ('12:10', '12:40', 30, 'activity', 'Activity 1 (Part A) - overview; 15-min team padlet discussion (what AI agents can do); pain-point hunt on the padlet; the padlet team of 3-5 chooses one company, joins one board and drafts its BMC', 1),
  ('12:40', '13:40', 60, 'lunch', 'Lunch break', 0),
  ('13:40', '14:30', 50, 'activity', 'Activity 1 (Part B) - verify and refine all nine BMC blocks, score opportunities and capture individual PP Task 1 evidence', 1),
  ('14:30', '14:55', 25, 'topic', 'Topic 2 (Part A) - room poll; pilot purgatory; Step 1 set the goal and baseline; Step 2 mine the process from dormant data and event logs', 2),
  ('14:55', '15:55', 60, 'topic', 'Topic 2 (Part B) - Step 3 plug in the agents: the decision layer and company map in plain English, business briefing, policies into permissions, patterns, build or buy', 2),
  ('15:55', '16:10', 15, 'break', 'Tea break', 2),
  ('16:10', '17:10', 60, 'topic', 'Topic 2 (Part C) - test before you trust: test set, four checks, shadow to autonomy; Step 4 name the owner; Step 5 run and evaluate the pilot; knowledge check; Meridian demo: how to fill each plan box', 2),
  ('17:10', '18:15', 65, 'activity', 'Activity 2 (Part A) - 15-min team padlet discussion (which action plan to focus on); the padlet team chooses a company, mine its process and write the company map the agent needs', 2),
  ('18:15', '18:30', 15, 'recap', 'Day 1 recap, Q&A and PM digital attendance', 2),
 ],
 2: [
  ('9:30', '9:45', 15, 'recap', 'Day 1 recap and AM digital attendance', 2),
  ('9:45', '11:15', 90, 'activity', 'Activity 2 (Part B) - Muse drafts the 90-day plan; the group tests the agent on 10 real cases, then completes the group board (PP Task 2 evidence)', 2),
  ('11:15', '11:30', 15, 'break', 'Tea break', 2),
  ('11:30', '12:05', 35, 'topic', 'Topic 3 (Part A) - the future organisation: fewer layers, people + agent teams, projects driven by DRIs; then the challenges of AI transformation', 3),
  ('12:05', '12:20', 15, 'activity', 'Activity 3 (Part A) - AI readiness diagnostic: score six dimensions, then share the shape with your group', 3),
  ('12:20', '13:00', 40, 'topic', 'Topic 3 (Part B) - SCALE: five moves that make the change stick; A job redesign around decisions; AI coaching with GROW and the six simulator profiles', 3),
  ('13:00', '14:00', 60, 'lunch', 'Lunch break', 0),
  ('14:00', '14:10', 10, 'lab', 'AI Coaching Mini Activity - in pairs, coach a worried employee on the AI Coaching simulator, read the feedback, swap and debrief', 3),
  ('14:10', '14:35', 25, 'topic', 'Topic 3 (Part C) - AI training that builds ability; progressive change; buy-in (story, stakeholders, ADKAR); C-suite and managers lead by example', 3),
  ('14:35', '15:05', 30, 'topic', 'Topic 3 (Part D) - L build AI into the workflow and processes; E evaluate and govern: policy stack, access, token cost drill, agent risks, six security principles; knowledge check; Meridian demo: how to fill each SCALE box', 3),
  ('15:05', '15:20', 15, 'break', 'Tea break', 3),
  ('15:20', '16:15', 55, 'activity', "Activity 3 (Part B) - 15-min team padlet discussion (org change, DRI, ontology); Muse drafts the change messages and the SCALE board; the group refines it and judges the decision (PP Task 3 evidence)", 3),
  ('16:15', '16:30', 15, 'assess', 'Course recap and Briefing for Assessment', 3),
  ('16:30', '17:30', 60, 'assess', 'Written Assessment (WA-SAQ) - 1 hour, open book; TRAQOM survey and assessment attendance first', -1),
  ('17:30', '18:30', 60, 'assess', 'Practical Performance (PP) - 1 hour, open book; paste the group board screenshots; upload on the LMS or hand in a printed copy', -1),
 ],
}

# --- Activity 1: open with a five-minute pain-point hunt (inside Part A; minutes unchanged)
PAIN_HUNT = dict(title="Pain-point hunt: three time-sinks, one vote", minutes=5,
                 body=["Alone, 3 minutes: on your team padlet, post three cards, one per task that wastes the most hours in your team each week, each with a rough number of hours.",
                       "Together, 2 minutes: read the cards, group the repeats and like the ones you agree with. The most-liked card is your first BMC opportunity. Optional: ask Muse to check the top three with the prompt below."],
                 prompt="My team: [team and role]. Our three biggest weekly time-sinks: [1, hours], [2, hours], [3, hours]. For each, tell me whether an AI agent could take it on today (yes, partly or no), what data it would need, and who would have to approve its work. Rank the three by hours saved. Mark guesses as (assumption).",
                 check="Three time-sinks with hours; one ranked first; the data and the approver named for each.")

# --- Activity 2: the company map in plain English, then test before you trust
_L2 = LABS[1]
_L2["steps"][1].update(
    title="Write the company map your agent needs",
    body=["In plain English: the words, records, rules and approvals an agent must know. Correct every definition that differs from how your company really works."],
    prompt="For the process [process name], write a one-page company map for an AI agent, in plain English: (1) five terms the way my company uses them (ask me when unsure; do not guess), (2) the key records and how they link (customer, request, contract, approval), (3) the approval rules and thresholds, with the policy owner and version, (4) what the agent may and may not do, (5) the live events that should update the map.",
    check="Plain-English definitions you corrected; two approval rules with the policy owner; what the agent may and may not do; one live event.")
_L2["steps"].insert(3, dict(
    title="Test before you trust: score 10 real cases", part="B",
    body=["Pick 10 anonymised cases from your mined process: 6 routine, 2 urgent, 1 incomplete, 1 conflicting. Your group re-scores every row: the agent's self-score is a claim, not a result."],
    prompt="Act as the agent in our pilot for [process]. Here are 10 anonymised cases [paste them]. For each case, give your output, then check it against our four tests: Correct (facts right), Complete (all required fields), Compliant (follows our approval rules), Cost (a person can approve it in under 2 minutes). Return a table: case, your output, the four tests (pass or fail), what a person must fix. Do not send or change anything.",
    check="Your group's own pass rate (for example 7 of 10), the failed cases named, and a go/no-go bar written into Success Measures (for example 9 of 10 correct before assist mode)."))
_L2["goal"] = "In groups of 3-5, use one member’s company: mine the process, write the company map, test the agent on 10 real cases and complete all nine boxes of its 90-day plan on one shared board."

# --- Activity 3: Part A readiness diagnostic (15 min) + Part B SCALE board (55 min)
_L3 = LABS[2]
_steps = _L3["steps"]
_story, _join, _muse, _refine, _judge, _capture = _steps[0], _steps[2], _steps[3], _steps[4], _steps[5], _steps[6]
READINESS_TOOL = "activities/activity-03-sustain-and-operate-with-ai-agents-scale/ai-readiness-scorecard.html"
TOKEN_TOOL = "activities/activity-03-sustain-and-operate-with-ai-agents-scale/token-cost-calculator.html"
_diag = dict(title="Score your AI readiness: six dimensions", part="A",
             body=["Open ai-readiness-scorecard.html from the Activity 3 folder (LMS download). Alone, 5 minutes: score your company on six dimensions, then copy the result.",
                   "In your group, 10 minutes: share the shape, not the score. Which dimension came out lowest, and does it surprise you?"],
             prompt="Here are my company's AI readiness scores out of 20 [paste the six scores from the scorecard]. Our company: [two sentences]. Name our lowest dimension, what it looks like day to day, who would have to act differently for it to move, and one change we can make in the next 30 days without new budget. 120 words at most.",
             check="Six scores and a radar chart; your group names its lowest dimension and one 30-day change that needs no new budget.")
for st in (_story, _join, _muse, _refine, _judge, _capture): st["part"] = "B"
_refine["body"] = ["Go block by block, S to E: is every message honest, every DRI named (with a backup owner), every guardrail real, every review metric measurable?",
                   "Add one AI-policy rule and a monthly token budget to Guardrails & Judgement, and name where each agent's playbook lives so it survives staff turnover.",
                   "Compare with View example or Meridian's demo board (link on the activity card)."]
_L3["steps"] = [_diag, _story, _join, _muse, _refine, _judge, _capture]
_L3["minutes"] = 70
CANVAS["change"]["minutes"] = 70
_L3["goal"] = "Score your company's AI readiness, then use SCALE (Story, Commanders, Augment people, Loop information, Evaluate) to plan the company-wide change; Meta Muse drafts, your group decides."
LAB = {L['n']: L for L in LABS}

# --- v56 (owner, 23 Nov 2026): five team padlets, one 15-min group discussion at the start of each activity (inside its minutes).
# Rooms on alfredang.github.io/padlet (Firestore padlet-7c3eb), owned by the trainer's Google account; each room has one
# column per topic with the questions pinned, plus a column for board screenshots.
PADLET_URL = "https://alfredang.github.io/padlet/?room="
# v58 (owner, 28 Nov 2026): one live-poll room per topic room poll on alfredang.github.io/livepoll (Firebase, always active).
# Created by courseware/.claude/scripts/livepoll_rooms.py; --verify checks them, --reset clears the votes before a new class.
LIVEPOLL_URL = "https://alfredang.github.io/livepoll/"
LIVE_POLLS = {1: "469720", 2: "919649", 3: "299409"}
PADLET_TEAMS = [("Catalyst", "W2GQC7"), ("Horizon", "XBMF8X"), ("Momentum", "5APT8X"), ("Pioneer", "JRSUDS"), ("Quantum", "B39XG6")]
PADLET_TALK = {
    1: ("What business innovation can AI agents do for us?",
        ["Which tasks in your companies could an AI agent take on today?",
         "Which block of the business model would it change most: customers, channels, activities or costs?",
         "Which idea moves a number your boss already tracks? That one goes on your Activity 1 BMC."]),
    2: ("Which action plan should we focus on?",
        ["Which process should your 90-day pilot start with, and why that one?",
         "What must be true at day 30 for you to keep going?",
         "Who is the DRI, and what can they decide without asking? Carry the answers into your Activity 2 plan."]),
    3: ("Org change, DRI and ontology: how do we drive AI transformation?",
        ["What does your organisation look like with fewer layers and mixed teams of people and agents?",
         "Which outcome needs a DRI first, and which business rules must agents never get wrong (your ontology)?",
         "What will stall the change, and who must lead by example? Carry the answers into your SCALE board."]),
}

# --- v57 (owner, 23 Nov 2026): the six worried-employee profiles of the AI Coaching simulator, one page each in Topic 3 job redesign.
# Name, role, tension, words and strength follow alfredang/AICoaching (role-play-simulator/index.html SCENARIOS + DEMO_PROFILES,
# README "Six coaching scenarios", commit 3b2b513). Quotes are the simulator openers, cut with ellipses. All six are fictional.
# Pronouns only where the simulator states them (Sarah, Mei Ling: she; David: he); Arjun, Aisha and Farah are written by name.
# The safe experiments are course suggestions for the four GROW moves, not part of the simulator.
COACH_PROFILES = [
    dict(name="Sarah", own_short="Campaign direction, brand quality and final approval", role="Marketing Executive", tension="Fear and work identity", ic="megaphone",
         title="From Campaign Producer to Marketing Owner",
         sub="The agent now does what she thought was her job. Show her the part it cannot do.",
         says="… It writes the campaign copy AND builds the slide decks. That's… that's basically my whole job. So what exactly do you still need me for?",
         agent="An AI copywriting agent drafts the campaign copy and builds the slide decks.",
         strength="I know our clients and what sounds authentic in the Singapore market.",
         owns="Campaign direction, brand quality and final approval. She sets the goal and brand voice; the agent drafts.",
         trial="Two weeks: the agent drafts, Sarah directs and approves. Review draft time, corrections and whether she had enough control."),
    dict(name="David", own_short="Escalations, bot knowledge and answer quality", role="Customer Service Officer", tension="Anger and betrayal", ic="chat",
         title="From Answering Every Enquiry to Owning the Hard Ones",
         sub="Eight years in the job and a bot took most of it. Let him vent; his edge cases are what the bot lacks.",
         says="That WhatsApp bot is answering 80% of the enquiries now. Eight years I've been doing this job. Eight years! … Honestly, this whole thing is a slap in the face.",
         agent="A WhatsApp bot answers 80% of customer enquiries in seconds.",
         strength="I can calm an angry customer and I know the product edge cases the bot keeps missing.",
         owns="Escalations, the bot's knowledge and answer quality, with authority to pull a bad answer.",
         trial="Two weeks: David takes every escalation and logs each wrong bot answer. Review fixes made, repeat questions and complaints."),
    dict(name="Mei Ling", own_short="Data validation, output audit and stakeholder interpretation", role="Data Analyst", tension="Anxiety and withdrawal", ic="chart",
         title="From Report Builder to Owner of the Numbers",
         sub="She has half-decided to resign, and says so early. Keep her, and what she knows about your data.",
         says="… The reports they generate are honestly better than mine, and faster. I've been thinking… maybe I should just resign before I get retrenched. …",
         agent="AI agents analyse the Excel data and write the reports automatically.",
         strength="I catch data problems and can explain what the numbers mean to stakeholders.",
         owns="Data validation, output audit and stakeholder interpretation: no agent report goes out unchecked.",
         trial="Two weeks with training: Mei Ling audits every agent report before release. Review errors caught and stakeholder questions answered."),
    dict(name="Arjun", own_short="Architecture, code review, tests and security gates", role="Software Developer", tension="Scepticism and professional pride", ic="code",
         title="From Writing Every Line to Owning the Architecture",
         sub="Distrust of code nobody has read is exactly the control you need.",
         says="I saw the coding agent complete that feature in twenty minutes — code, tests, everything. … And honestly, I don't trust code nobody truly understands.",
         agent="A coding agent writes a feature, with code and tests, in twenty minutes.",
         strength="I understand the architecture, debug the hard failures and spot security trade-offs.",
         owns="Architecture, code review, tests and security gates. The role grows more senior, not smaller.",
         trial="One sprint: Arjun sets the tests and security gates, the agent codes, nothing merges without Arjun's review. Review defects and rework."),
    dict(name="Aisha", own_short="Release control, exceptions, rollback and web quality", role="Web Operations Executive", tension="Control and accountability", ic="globe",
         title="From Blamed for the Agent to In Charge of the Release",
         sub="Blamed for changes no one can stop. Hand over the stop button along with the blame.",
         says="… if an agent breaks a page or publishes the wrong price, I know who will be blamed — me. That doesn't feel like a better job.",
         agent="Agents update product pages, run SEO checks and publish campaigns overnight.",
         strength="I know the CMS, the brand rules and all the strange launch-day exceptions.",
         owns="Release control, exceptions, rollback and web quality, with real approval rights.",
         trial="Two weeks: nothing goes live without Aisha's release check, and Aisha holds the rollback. Review errors stopped and time to publish."),
    dict(name="Farah", own_short="Bias review, policy guardrails, appeals and human decisions", role="HR Executive", tension="Ethics and human purpose", ic="scale",
         title="From Rubber Stamp to Guardian of Fair Decisions",
         sub="Farah's objection is your fairness policy. Make it Farah's job.",
         says="… this agent is screening people and drafting performance reviews. Those decisions affect real careers. If my role becomes rubber-stamping an algorithm, I don't want it …",
         agent="An agent screens job applicants and drafts performance reviews.",
         strength="I notice context an algorithm misses, and people trust me with difficult conversations.",
         owns="Bias review, policy guardrails, appeals and the human decision on every career outcome.",
         trial="One hiring round: the agent shortlists, Farah reviews each rejection for bias and a person decides. Review overturned rejections."),
]

# --- Topic 3 evidence (owner's attachment, v53). Each figure is re-checked before the slide ships; see notes on each slide.
READINESS_DIMS = [  # (name, what a high score looks like), each scored /20 (four statements x 1-5)
    ("Leadership and AI vision", "Leaders explain AI's value, back a roadmap of quick wins and long-term goals, and use it themselves"),
    ("Change management", "A formal approach, adjusted from feedback; experiments encouraged; training and coaching on time"),
    ("Transparency and trust", "AI decisions are explained; ethics, privacy and data policies understood; concerns acted on"),
    ("Organisational capability", "Training is open to all, expertise is on hand, AI outcomes sit in KPIs, good practice is shared"),
    ("People and roles", "AI is seen as an opportunity, resistance is low and each role's needs are met"),
    ("Data and infrastructure", "Data is good enough and reachable, tools support AI, technical barriers rarely block experiments"),
]
TOKEN_PRICES = [  # Anthropic API list prices, USD per million tokens (input, output); checked 22 Nov 2026
    ("Claude Haiku 5.5", 0.10, 0.50, "Triage, tagging, routing"),
    ("Claude Sonnet 5.5", 2.00, 10.00, "Everyday drafting and agents"),
    ("Claude Opus 5.5", 4.00, 20.00, "Hard reasoning, long agent runs"),
    ("Claude Fable 5.2", 8.00, 40.00, "The most demanding work"),
]
TOKEN_PRICE_SOURCE = "https://platform.claude.com/docs/en/about-claude/pricing"
CAPABILITY_REGISTER = [  # Meridian (fictitious): where each agent capability lives, so it survives staff turnover
    ("Request triage", "Triage agent (draft only)", "Head of Service Desk", "Senior coordinator", "Playbook v1.3 in ServiceNow", "Read Gmail + tickets; coordinator approves dispatch", "Minutes per request; rework"),
    ("Monthly client report", "Report agent", "Account Director", "Account manager", "Report skill v2.0 in shared drive", "Masked tenant data; manager signs off", "Hours per report; errors found"),
    ("Technician job notes", "Voice-to-report agent", "Operations Manager", "Team lead, East", "Approved app + template v1.1", "No tenant names in audio; 30-day deletion", "Reports filed same day"),
]
