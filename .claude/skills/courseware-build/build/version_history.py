"""Document Version Control Record rows (shared by LP and LG). v30-v40 carried forward from the archived v40 builders."""
PRIOR = [('30.0', '1 July 2025', 'Previous release — Learner Guide for Digital Transformation and Business Innovation with Generative AI (GenAI).', 'Tertiary Infotech Academy'),
 ('32', '9 September 2026', 'Major revision — restructured to the three WSQ topics with 18 detailed step-by-step labs; added the Skills Framework alignment, responsible-use guidance, the five-layer digital architecture, Singapore AI governance (IMDA Model AI Governance Framework, AI Verify, PDPA), the AIM framework, assessment preparation for the Written Assessment + Practical Performance, and an expanded glossary.', 'Dr. Alfred Ang'),
 ('33', '9 September 2026', 'Corrected the practical instrument naming throughout to Practical Performance (PP) to match the assessment papers held on the TMS (previously labelled Case Study); PP duration aligned to 1 hour across the slides, Lesson Plan, Learner Guide and the paper.', 'Dr. Alfred Ang'),
 ('35', '9 September 2026', 'Major content revision — the 15 standalone labs are replaced by 18 CONNECTED labs forming one end-to-end production pipeline: the learner chooses a single business idea and carries it through research (Perplexity + NotebookLM), scoring, Business Model Canvas, digital architecture, video script, AI voiceover (ElevenLabs), AI soundtrack (Suno), video production (Kling + CapCut) and a business presentation (Gamma). Added the six Business Model Canvas guidelines, prompting and craft tips for every GenAI tool, clickable tool links, a pipeline overview flow at the front, the four guardrail types, the eight AI ethics principles as observable behaviours, a pipeline risk assessment, and a capstone agentic AI workflow (n8n) that automates the whole pipeline with a human review gate and an audit log.', 'Dr. Alfred Ang'),
 ('38', '9 August 2026', "Layout and alignment fixes — auto-sized lab 'You'll build' panels and slide titles so long text no longer collides; two-digit lab badges no longer clip; refreshed the lesson-plan overview slide to the 18-lab structure; corrected every cross-artifact lab reference (governance controls Labs 13-14, canvas Lab 6, action plan Lab 15, AI use policy Lab 17, pitch deck Lab 12).", 'Dr. Alfred Ang'),
 ('39', '9 September 2026', 'Retitled and realigned to the verified live course identity and outcomes. Added an ebook-informed, vendor-agnostic AI solution architecture playbook covering the 2023-2026 engineering-emphasis timeline, business requirements, build-buy-extend and agent patterns, evaluation and ROI/TCO, agent security, stakeholder adoption and executive sponsorship.', 'Dr. Alfred Ang'),
 ('40', '9 September 2026', 'Replaced the tool-production labs with 12 connected, vendor-neutral business activities. Added three recurring case studies, business-needs analysis, requirements traceability, custom-buy-hybrid sourcing, human decision boundaries, evaluation and ROI, risk/security/governance with human oversight, stakeholder and management buy-in, quick wins, role-based training and a coherent board-review capstone. Every activity has a checklist, metric sheet, mock data, editable Markdown and printable PDF copies; aligned PPT, Learner Guide, Lesson Plan and WA/PP case tasks.', 'Dr. Alfred Ang')]

V41 = ("41", "18 November 2026",
       "Complete overhaul: visual, big-type business-pitch deck in the agentic-AI house design, with the LO on every topic divider and topics "
       "renamed to the live course record. Topic 1: AI history, Agent Stairway, engineering lenses, agentic AI vs AI agent, Singapore news, "
       "always-on agents, five collaboration scenarios, capability gaps, opportunity scoring. Topic 2: AI Native concepts (dormant data, "
       "decision layer, company map, live navigation, AI flywheel), Step 1 mine the process, Step 2 where agents integrate, patterns, "
       "build/buy and the outcome contract. Topic 3: Boss AI, DRIs, smart flattening, the new workforce, atrophy trap, reviewing success, "
       "governance and information flow. Three Meta Muse activities on shared group boards (alfredang.github.io/bcm) replace the 12 v40 "
       "activities; schedule re-timed to the CP LUs (4 h / 6 h / 4 h). PP v41: screenshots of the three group boards, individual answers.",
       "Dr. Alfred Ang")
V42 = ("42", "18 November 2026",
       "QA fixes and AI Native concepts: eleven key-concept slides (Agent Stairway, five capability gaps, dormant data, decision layer, "
       "company map, live navigation, AI flywheel, Boss AI, DRI, smart flattening, atrophy trap) and an 'AI Native in 11 ideas' map; bridge "
       "slides between topics; Activity 1 uses the traditional nine Business Model Canvas blocks asked about AI agents; topic names match "
       "the live course record; caption-free scenario images, trainer on the cover, cleaner LMS slide, uniform worked-example type, "
       "prompt-panel and layout fixes; LP version record and LU column tidied.",
       "Dr. Alfred Ang")
V43 = ("43", "18 November 2026",
       "Focused and lighter: every slide tied to LO1-LO3 and business innovation with AI agents; book references removed (background "
       "reading only); four agent-centred key concepts kept (dormant data, decision layer, company map, DRI) plus how agents act safely; "
       "repeated or abstract slides removed (AI Native map, duplicate decision-layer, flywheel, Boss AI, work landscape and others).",
       "Dr. Alfred Ang")
V44 = ("44", "18 November 2026",
       "Learners work on their own organisation throughout: the named example company is removed from the slides, Learner Guide, "
       "activities, prompts and assessment (board examples stay unnamed). Topic 2 framework is now a plain five-step 90-day action plan "
       "(set the goal, mine the process, plug in the agents, name the owner, run a 90-day pilot) instead of the AGENT acronym. "
       "The 'four futures' slide is replaced by a clearer before/after slide on where people's work moves. WA-SAQ questions and "
       "PP tasks rewritten to match the slides and Activities 1-3 (same five questions and K1-K6 mapping; same three tasks and A1-A6).",
       "Dr. Alfred Ang")
ALL = PRIOR + [V41, V42, V43, V44]
