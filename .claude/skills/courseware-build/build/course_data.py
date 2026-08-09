"""
SINGLE SOURCE OF TRUTH — Digital Transformation and Business Innovation with
Generative AI (GenAI), WSQ course TGS-2023037472.

Content is carried forward from the previous Master Trainer deck (v30) and the
published course page, restructured into the three WSQ topics and refreshed for
2026 tooling. Every artifact (PPT, LP, LG, LG.md, labs index, assessment) is
generated from this file plus data_domain1..3.py so they stay 100% aligned.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Digital Transformation and Business Innovation with Generative AI (GenAI)"
SHORT_TITLE  = "Digital Transformation and Business Innovation with GenAI"
COURSE_CODE  = "TGS-2023037472"
VERSION      = "v38"
VERSION_DATE = "9 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2

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
    "LO1: Evaluate and investigate generative AI business strategies to identify viable opportunities compatible with organisational objectives.",
    "LO2: Develop action plans to implement business innovation with generative AI and design digital architectures to apply technologies across the business.",
    "LO3: Manage business innovation and facilitate information flow among stakeholders to review success and develop innovative ideas.",
]

# ------------------------------------------------------------------ topics (= WSQ skills domains)
TOPICS = [
    dict(num=1, code="01",
         title="Introduction to Business Innovation and Generative AI",
         subtitle="Predictive vs generative AI · GenAI tool landscape · evaluating business opportunities  (K1, K2, A1, A2)",
         weighting="LO1",
         concepts=[
            ("Predictive vs generative AI", "Predictive AI scores and forecasts from historical data; generative AI creates new text, image, audio, video and code from a prompt."),
            ("How GenAI works", "A foundation model is pre-trained on a large corpus, then aligned; at inference a prompt is turned into tokens and completed one token at a time."),
            ("Market momentum", "The generative AI market is growing at a >35% CAGR; adoption has moved from experiment to core business process in under three years."),
            ("Where value comes from", "Four value levers: revenue growth, cost and productivity, risk mitigation and sustainability."),
            ("The GenAI tool landscape", "Text, image, speech and voice, music, video, digital human, 3D, office productivity, data analysis and IP tooling."),
            ("Evaluating an opportunity", "Screen each idea for business value, feasibility, data readiness, risk and fit with organisational objectives before committing."),
         ]),
    dict(num=2, code="02",
         title="Designing Digital Architectures and Processes for Business Innovation",
         subtitle="Business Model Canvas · Design Thinking · digital architecture · action planning  (K3, K4, A3, A4)",
         weighting="LO2",
         concepts=[
            ("Business planning methodologies", "The Business Model Canvas, Value Proposition Canvas and Design Thinking give innovation a repeatable structure."),
            ("AI-powered Business Model Canvas", "Use GenAI to draft and stress-test each of the nine blocks, then validate the assumptions with evidence."),
            ("Design Thinking with GenAI", "Empathise, Define, Ideate, Prototype and Test — GenAI accelerates every stage, especially ideation and prototyping."),
            ("Digital architecture layers", "Data, model, orchestration, application and governance layers describe where AI sits in the business."),
            ("Integration patterns", "Chat assistant, RAG over company documents, workflow automation and autonomous agents are the four common patterns."),
            ("From design to action plan", "An action plan names the owner, milestone, resource, risk and success measure for every initiative."),
         ]),
    dict(num=3, code="03",
         title="Implementing and Managing Business Innovation with Generative AI Tools",
         subtitle="Best practices · legal, ethical and security issues · measuring success · stakeholder communication  (K5, K6, A5, A6)",
         weighting="LO3",
         concepts=[
            ("Implementation best practices", "Start with a narrow high-value use case, keep a human in the loop, measure a baseline and scale only what works."),
            ("Legal considerations", "Copyright and training data, model output ownership, the EU AI Act and Singapore's PDPA obligations."),
            ("AI ethics", "Transparency, fairness, safety, explainability, privacy, security, responsibility, liability and auditability."),
            ("Singapore governance", "IMDA's Model AI Governance Framework and AI Verify give organisations a practical assurance toolkit."),
            ("Security and data protection", "Prompt injection, data leakage into public models, shadow AI and access control over AI systems."),
            ("Measuring and reviewing success", "Track adoption, cycle time, quality, cost per task and business outcome against the pre-AI baseline."),
            ("Stakeholder communication", "A communication plan, AI use policy and community of practice keep ideas flowing across the organisation."),
            ("The AIM framework", "Assess, Implement, Manage — a repeatable loop for running generative AI innovation."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Understanding GenAI and evaluating business opportunities",
    2: "Designing, implementing and governing GenAI innovation",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — hands-on tasks using generative AI tools, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

# ------------------------------------------------------------------ recommended follow-on courses
RECOMMENDED = [
    "WSQ - Build Agentic AI and NLP Applications with Langflow",
    "WSQ - Build AI Agents and RAG Pipelines Without Code",
    "WSQ - Fundamentals of AI Ethics and Responsible AI",
    "WSQ - Mastering Prompt Engineering for Generative AI Content Creation",
    "WSQ - Build LLM Applications Using Langchain and Flowise",
]
