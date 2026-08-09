"""
Topic 3 — Implementing and Managing Business Innovation with Generative AI Tools
(K5, K6, A5, A6).

Labs 13-18. GOVERNANCE AND AUTOMATION — the learner takes the campaign asset set
built in Topic 2 and makes it safe, measurable, communicable and finally
AUTOMATED as an agentic workflow with a human review gate.

Lab 13  risk assessment of the pipeline
Lab 14  security guardrails and AI ethics principles
Lab 15  implementation action plan
Lab 16  measurement and review
Lab 17  stakeholder communication and idea flow
Lab 18  CAPSTONE — agentic AI workflow automating Labs 3-12 with human review
"""

DOMAIN3 = [
    dict(
        num=13, topic=3,
        title="Risk-Assess Your Generative AI Pipeline",
        objective="K6 — identify and address legal, ethical and security issues in implementing business innovation with GenAI.",
        desc="Run a structured risk assessment over the ACTUAL pipeline you built in Labs 3-12 — the research, canvas, script, voice, music, video and deck — and turn every finding into a named, owned control.",
        build="A risk register covering your own pipeline stage by stage: copyright, data protection, accuracy, disclosure and security, each with a specific control and an owner.",
        services="Your Lab 3-11 artifacts, chat assistant, IMDA Model AI Governance Framework, PDPC guidelines",
        steps=[
            ("Lay out your pipeline as a table with one row per stage: research (Lab 3), canvas (5), script (7), voiceover (8), music (9), video (10), deck (11). You are assessing what you actually built, not a hypothetical system.", ""),
            ("COPYRIGHT AND OWNERSHIP — for each generated asset record who owns it and whether the free-tier licence permits commercial use. Check your Lab 10 music licence note and the Kling and ElevenLabs terms. Flag any asset you could NOT legally publish today.", ""),
            ("ACCURACY — identify every factual claim in your video and deck. Which trace to a verified Lab 3 source, and which came from an AI draft nobody checked? An unverified statistic in a customer-facing video is the highest-likelihood failure in this pipeline.", ""),
            ("DATA PROTECTION — list any personal data touched, and check handling against Singapore's PDPA obligations for consent, purpose and retention. Note anything you pasted into a public tool that should not have been.", ""),
            ("DISCLOSURE — decide where you must tell the audience that content is AI-generated. Consider the AI presenter or cloned voice, generated imagery of 'customers', and the EU AI Act's transparency duties for synthetic media.", ""),
            ("SECURITY — assess exposure to prompt injection (in a RAG or agent stage), confidential data leaking into a public model, shadow AI, and weak access control over the accounts holding your assets.", ""),
            ("BIAS TEST — run the same prompt through your pipeline with two different demographic framings and compare the outputs for unjustified differences. Record the actual prompts and what you found.", ""),
            ("For every red and amber finding write ONE specific control naming what changes, who owns it and how compliance is checked. A control that names no owner is a wish, not a control.", ""),
        ],
        test="Every pipeline stage has at least one identified risk with a specific owned control, your bias test is recorded with the actual prompts used, and you can state which of your generated assets are and are not safe to publish commercially.",
    ),
    dict(
        num=14, topic=3,
        title="Define Security Guardrails and AI Ethics Principles",
        objective="K6, A6 — establish the ethical principles and technical guardrails that govern generative AI use across the organisation.",
        desc="Convert the risks found in Lab 13 into a working governance layer: the ethics principles the organisation commits to, and the concrete guardrails that enforce them in practice.",
        build="A one-page AI governance charter: eight ethics principles with what each means in practice, plus a guardrail table mapping each risk to an input, processing, output or human control.",
        services="Chat assistant, IMDA Model AI Governance Framework, AI Verify, your Lab 13 risk register",
        steps=[
            ("Adopt the eight AI ETHICS PRINCIPLES and write what each means concretely for YOUR pipeline: TRANSPARENCY (users know when AI is used), FAIRNESS (no unjustified bias against any group), SAFETY (the system behaves within intended bounds), EXPLAINABILITY (decisions can be understood and justified), PRIVACY (personal data protected and minimised), SECURITY (resists misuse and attack), RESPONSIBILITY (a named human owns each outcome), AUDITABILITY (decisions are logged and reviewable).", ""),
            ("TIP — a principle without a behaviour is decoration. Write each as an observable commitment: not 'we value transparency' but 'every AI-generated video carries an on-screen AI-generated label and names the tools used in the description'.", ""),
            ("INPUT GUARDRAILS — define what may never enter a prompt: personal data, customer records, unreleased financials, credentials, client-identifying material. State which tools are approved for which data classification.", ""),
            ("PROCESSING GUARDRAILS — defend against prompt injection: treat all retrieved or uploaded content as untrusted, never let retrieved text change the system instruction, and restrict what tools an agent may call. This matters most for the Lab 18 agentic workflow.", ""),
            ("OUTPUT GUARDRAILS — define what must be checked before anything is published: factual claims verified against a source, licence terms confirmed, brand and tone reviewed, and AI disclosure applied where required.", ""),
            ("HUMAN-IN-THE-LOOP GUARDRAILS — decide exactly WHERE a human must approve. Rule of thumb: require human sign-off wherever output is customer-facing, carries legal or financial weight, or cannot be reversed. Name the approver role for each gate.", ""),
            ("Map each Lab 13 risk to the guardrail that mitigates it in a table (risk → guardrail type → control → owner). Any risk with no guardrail is still open — say so rather than hiding it.", ""),
            ("Write the one-page charter: the eight principles, the approved-tool list, the prohibited-data list, the disclosure rule, the human approval gates and where to ask for help.", ""),
        ],
        test="Every principle is written as an observable behaviour, every Lab 13 red or amber risk maps to a named guardrail with an owner, and your human-approval gates are specific about who approves what before publication.",
    ),
    dict(
        num=15, topic=3,
        title="Develop the Implementation Action Plan",
        objective="K5, A4 — apply best practices in the implementation process of business innovation, and develop a viable action plan in line with business strategy.",
        desc="Convert the design and its governance into a costed, owned and sequenced 90-day plan a management team could approve and track.",
        build="A 90-day action plan with phased milestones, owners, resources, dependencies, a risk register and numeric go/no-go criteria.",
        services="Excel or Google Sheets, chat assistant",
        steps=[
            ("Define the scope of a 90-day pilot for your solution — narrow enough to finish, valuable enough to matter.", ""),
            ("Break it into phases: prepare (weeks 1-2), build (3-6), pilot (7-10), review and decide (11-12).", ""),
            ("For every milestone record the owner by role, the resource needed, the dependency and the completion date.", ""),
            ("Carry the controls from Labs 13 and 14 into the plan as real work items with owners — governance that is not scheduled does not happen.", ""),
            ("Add a risk register of at least five risks (data privacy, output accuracy, user adoption, cost overrun, vendor lock-in), each with a mitigation and an owner.", ""),
            ("Use a chat assistant as a challenger: 'What is missing from this implementation plan, and what most commonly causes such pilots to fail?' Incorporate what is valid.", ""),
            ("Define the week-12 go/no-go criteria as NUMBERS that would justify scaling, pausing or stopping.", ""),
        ],
        test="Every milestone has a named owner role and date, the governance controls from Labs 13-14 appear as scheduled work, the risk register has five risks with mitigations, and the go/no-go criteria are numeric rather than subjective.",
    ),
    dict(
        num=16, topic=3,
        title="Measure and Review Innovation Success",
        objective="A5 — manage business innovation and review the success of its integration with business strategy.",
        desc="Build the measurement system that shows whether the innovation actually worked, including the pre-AI baseline without which no improvement can be claimed.",
        build="A KPI dashboard defining baseline, target and review cadence across adoption, efficiency, quality, cost and business outcome, plus a counter-metric.",
        services="Excel or Google Sheets, chat assistant",
        steps=[
            ("Define your pre-AI baseline: how long the target task takes today, what it costs and its current quality. Without this, no improvement can be proven.", ""),
            ("For your own pipeline this is concrete: how long did producing a marketing video take BEFORE (agency brief, shoot, edit) versus the hours it took you across Labs 8-11?", ""),
            ("Set one KPI in each of five categories: adoption, efficiency, quality, cost and business outcome.", ""),
            ("For every KPI record the definition, data source, baseline value, 90-day target and who reports it.", ""),
            ("Add at least one COUNTER-METRIC that would reveal harm — error rate, customer complaints, brand-consistency failures or rework — so gains are not claimed at the expense of quality.", ""),
            ("Build the dashboard with baseline, current and target columns and conditional formatting for on/off track.", ""),
            ("Define the review cadence: what is reviewed weekly, what monthly, and what triggers escalation or a stop decision.", ""),
        ],
        test="Every KPI has a real baseline number and a data source, at least one counter-metric is present, and your review cadence names who meets, how often and what decision they can make.",
    ),
    dict(
        num=17, topic=3,
        title="Build the Stakeholder Communication and Idea-Sharing Plan",
        objective="A6 — facilitate information flow among key stakeholders to empower sharing and development of innovative ideas.",
        desc="Design how the innovation is communicated and how new ideas keep flowing after the pilot, so the initiative outlives its launch.",
        build="A stakeholder map, a tailored communication plan, the published one-page AI use policy, and a mechanism for capturing and triaging new ideas.",
        services="Chat assistant, Gamma or Canva, Microsoft Teams or Slack",
        steps=[
            ("Map your stakeholders on influence and interest: executive sponsors, affected staff, IT and security, legal and compliance, customers.", ""),
            ("For each group define the message that matters to them, the channel, the frequency and the owner — an executive needs outcomes, an affected employee needs job impact.", ""),
            ("Address the adoption concern directly: draft the honest message about what the AI will and will not change about people's jobs.", ""),
            ("Publish the one-page AI use policy (derived from your Lab 14 governance charter) — approved tools, prohibited data, disclosure rules and where to ask for help — as the staff-facing artifact.", ""),
            ("Design the idea-sharing mechanism: a channel, a monthly community-of-practice session and a simple intake form for new use cases.", ""),
            ("Define how a submitted idea is triaged using the Lab 4 scoring rubric, so the pipeline stays consistent and fair.", ""),
        ],
        test="Every stakeholder group has a tailored message, channel, frequency and owner; the AI use policy fits one page and names prohibited data; and a submitted idea has a defined path to evaluation.",
    ),
    dict(
        num=18, topic=3,
        title="CAPSTONE — Automate the Pipeline with an Agentic AI Workflow and Human Review",
        objective="K5, A3, A4, A5 — design and build an agentic workflow that automates the business innovation process end to end, with human review and governance built in.",
        desc="The capstone. Everything you did by hand in Labs 3-12 becomes an automated agentic workflow — research, canvas, script, assets and deck — with a HUMAN REVIEW GATE before anything is published, and the Lab 14 guardrails enforced in the flow.",
        build="A working agentic workflow that takes a business idea as input, runs the research-to-content pipeline through AI agents, pauses for human approval, and delivers the finished asset set — with the run logged for audit.",
        services="n8n (recommended), Make.com, Copilot Studio or Zapier; plus your Lab 3-11 tool accounts",
        steps=[
            ("Map the pipeline as a flow BEFORE building: Input (business idea) → Research agent → Evaluation agent → Canvas agent → Script agent → HUMAN REVIEW GATE → Asset generation (voice, music, video) → Deck assembly → Output + notification. Draw it; you cannot automate a process you cannot draw.", ""),
            ("Open n8n (n8n.io — free cloud trial or self-hosted) and create a new workflow. Add a Form trigger that accepts the business idea, the target audience and the desired call to action.", ""),
            ("RESEARCH AGENT — add an AI Agent node with a web-search tool. System prompt: 'Research the market for the submitted idea. Return market size, three competitors, the customer problem and three source URLs. Only state facts you can cite.' Automates Lab 3.", ""),
            ("EVALUATION AGENT — add a second agent that scores the idea on the Lab 4 rubric (business value, feasibility, data readiness, risk, strategic fit) and returns a structured JSON verdict with a recommendation.", ""),
            ("TIP — force STRUCTURED OUTPUT (JSON) between agents. Free-text handoffs break downstream nodes as soon as the model phrases things differently; a defined schema makes the workflow reliable.", ""),
            ("CANVAS + SCRIPT AGENTS — chain two more agents: one drafts the nine-block canvas from the research, the next writes the 60-second script from the canvas and the research. Each receives the previous agent's structured output.", ""),
            ("HUMAN REVIEW GATE — this is the most important node. Insert a Wait-for-approval step (n8n's Wait node with an approval form, or a Teams/Slack approval message) that sends the human reviewer the research, the canvas and the script, and PAUSES the workflow. Nothing downstream runs until a person approves.", ""),
            ("TIP — place the gate BEFORE the expensive, hard-to-reverse steps. Video generation costs credits and publishing is public; approving the script first means a bad idea is stopped while it is still cheap. Give the reviewer approve / reject / request-changes, and route rejection back to the script agent with the reviewer's comments.", ""),
            ("ASSET GENERATION — after approval, call the ElevenLabs API for the voiceover and your video tool for the scenes, then store the assets. Add an error branch so a failed generation notifies a human instead of silently producing nothing.", ""),
            ("GUARDRAILS — implement your Lab 14 controls in the flow: validate that no prohibited data is in the input, treat all retrieved web content as untrusted (prompt-injection defence), restrict each agent to only the tools it needs, and add an AI-disclosure field to every output.", ""),
            ("AUDIT LOG — append each run to a Google Sheet or database: timestamp, input idea, each agent's output, who approved, when, and the final asset links. This is your AUDITABILITY principle made real, and what an assessor or regulator would ask to see.", ""),
            ("Run the workflow end to end with a fresh business idea. Deliberately REJECT at the review gate once and confirm the flow routes back and does not proceed to asset generation. A gate that cannot stop the process is not a gate.", ""),
        ],
        test="Your workflow runs from a submitted idea through research, evaluation, canvas and script; it PAUSES at the human review gate and only continues on approval; a rejection routes back without generating assets; every run is logged with the approver and timestamp; and you can point to where each Lab 14 guardrail is enforced.",
    ),
]
