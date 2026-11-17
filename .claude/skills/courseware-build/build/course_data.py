"""SINGLE SOURCE OF TRUTH - WSQ Business Innovation with Agentic AI and AI Agents (TGS-2023037472).

v41 (18 Nov 2026): rebuilt in the house design of TGS-2024043854 (ccdeck: ivory/charcoal, terracotta,
Cambria). course_data.py (metadata, outcomes, topics) + data_bi.py (activities, Muse labs, schedule)
drive the deck, LP, LG, activity/lab folders and the online activity boards (bcm).
The previous v40 engine is kept in build/archive-v40/.
"""
from data_bi import SCHEDULE, CANVASES, LABS, BCM_URL   # noqa: F401  (re-exported for the builders)

# ------------------------------------------------------------------ metadata
TITLE        = "Business Innovation with Agentic AI and AI Agents"
SHORT_TITLE  = "Business Innovation with Agentic AI and AI Agents"
COURSE_CODE  = "TGS-2023037472"
VERSION      = "v44"
VERSION_DATE = "18 November 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-business-innovation-with-agentic-ai-and-ai-agents.html"
REPO_URL     = "https://github.com/tertiarycourses/TGS-2023037472-Digital-Transformation-and-Business-Innovation-with-Generative-AI-GenAI"
PITCH        = "Turn agentic AI from a demo into a business advantage: find the opportunity, plan the build, lead the change."
CONTACT_TIME_NOTE = "16 hours in total (14 hours training + 2 hours assessment) over 2 days, 9:30 am-6:30 pm; 1-hour lunch not counted; the assessment runs on Day 2 from 4:30 pm."

# ------------------------------------------------------------------ Skills Framework TSC
TSC_TITLE = "Business Innovation"
TSC_CODE  = "ICT-SNA-5003-1.1"
TSC_ABILITIES = [
    "A1: Investigate business strategies to identify business opportunities.",
    "A2: Evaluate opportunities for viability, applicability to the organisation and compatibility with business goals and objectives.",
    "A3: Design digital architectures to structure the application of digital technologies to different parts of the business.",
    "A4: Develop a viable action plan to implement the business innovation processes, in accordance with the organisation's business strategies.",
    "A5: Manage business innovation to review success of integration with the organisation's business strategies.",
    "A6: Facilitate information flow among key stakeholders to empower sharing and development of innovative ideas.",
]
TSC_KNOWLEDGE = [
    "K1: Current and emerging industry-accepted technology services and business models.",
    "K2: The organisation's operating context, business priorities, domain and environment.",
    "K3: Business planning process and methodologies relating to business innovation.",
    "K4: Application of digitisation to the business.",
    "K5: Best practices in implementation process of business innovation.",
    "K6: Legal, ethical and security issues relating to implementation of business innovation.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Evaluate and investigate agentic AI and AI agents business strategies to identify viable opportunities compatible with organizational objectives.",
    "LO2: Develop action plans to implement business innovation with agentic AI and design digital architectures to apply technologies across the business.",
    "LO3: Manage business innovation and facilitate information flow among stakeholders to review success and develop innovative ideas.",
]
FRAME = ["BMC", "90-Day Plan", "SCALE"]   # the course spine: LO1 BMC -> LO2 five-step 90-day plan -> LO3 SCALE
LO_SHORT = ["Identify and Evaluate AI Agent Business Opportunities", "Action Plan to Get Started with AI Agents", "Sustain and Operate the Business with AI Agents"]

# ------------------------------------------------------------------ topics
TOPICS = [
 dict(num=1, code="01", lo=0, codes="K1, K2, A1, A2", day="Day 1 AM",
      title="Identifying Business Innovation Opportunities with Agentic AI and AI Agents",
      short="Identify and evaluate opportunities",
      pitch="Agents now do real work. Find where they pay off in your business.",
      items=["History of AI, the Agent Stairway and the 2023-2026 engineering lenses", "Agentic AI vs AI agent", "Singapore government news",
             "Always-on AI agents (Meta Muse)", "Five scenarios of human-AI agent collaboration",
             "Five capability gaps and evaluating opportunities", "Activity 1 · Business Model Canvas for AI Agents (identify and evaluate)"]),
 dict(num=2, code="02", lo=1, codes="K3, K4, A3, A4", day="Day 1 PM - Day 2 AM",
      title="Designing Digital Architectures and AI Agent Implementation Plans",
      short="Action Plan to Get Started",
      pitch="Five steps: set the goal, mine the process, plug in the agents, name the owner, run a 90-day pilot. A plan you can start on Monday.",
      items=["Dormant data and the enterprise AI decision layer", "The company map and how agents act safely",
             "The five-step 90-day action plan: goal, process, where agents plug in, owner, pilot", "Patterns, custom/buy/hybrid and TCO",
             "Activity 2 · AI Agent 90-Day Action Plan"]),
 dict(num=3, code="03", lo=2, codes="K5, K6, A5, A6", day="Day 2 PM",
      title="Managing AI-Driven Innovation, Governance and Stakeholder Collaboration",
      short="Sustain and Operate",
      pitch="SCALE: story, commanders, augment people, loop information, evaluate. Keep it running and growing.",
      items=["The SCALE framework, the flattened org chart and the DRI", "Where work moves: a new workforce and tomorrow's managers", "Training for adoption and the atrophy trap",
             "Reviewing success: metrics, ROI, governance, PDPA",
             "Activity 3 · Sustain and Operate (SCALE)"]),
]
DAY_THEMES = {1: "Identify and evaluate AI agent opportunities (BMC), then start the 90-day action plan",
              2: "Finish the 90-day action plan, then sustain and operate with SCALE; assessment"}

# ------------------------------------------------------------------ assessment (methods fixed by the approved CP: WA-SAQ + PP)
ASSESSMENT = dict(
    written="Written Assessment (WA) - Short-Answer Questions (SAQ), 1 hour, open book. Five questions (K1-K6).",
    practical="Practical Performance (PP) - scenario-based, 1 hour, open book. Task 1 pastes your Activity 1 canvas screenshot; Task 2 your Activity 2 action plan; Task 3 your Activity 3 change board; each with a written analysis (A1-A6).",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

RECOMMENDED = [
    "WSQ - Build a Human-AI Workforce with Autonomous AI Agents",
    "WSQ - Build AI Agents and RAG Pipelines Without Code",
    "WSQ - Fundamentals of AI Ethics and Responsible AI",
]

# Synthetic ROI case (unnamed sample company) shared by the deck, LG and PP Task 3.
ROI_CASE = dict(eligible_cases=10000, baseline_mean_min=18, pilot_mean_min=11, labour_rate=42, realisation=0.60,
                first_year_cost=39000, day90_benefit=39200)
