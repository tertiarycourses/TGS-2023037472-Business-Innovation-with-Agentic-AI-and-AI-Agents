"""
Topic 1 — Introduction to Business Innovation and Generative AI (K1, K2, A1, A2).

Labs 1-4. STAGE 1-2 of the connected production pipeline: the learner picks ONE
business idea and carries it through every remaining lab in the course.

Pipeline: research (Lab 3) -> evaluate (Lab 4) -> canvas (Lab 5) -> script (Lab 7)
-> voiceover (Lab 8) -> soundtrack (Lab 9) -> video (Lab 10) -> presentation (Lab 11).
"""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Compare Predictive and Generative AI on a Business Task",
        objective="K1 — distinguish current predictive AI from emerging generative AI and describe where each creates business value.",
        desc="Run the same customer-feedback data through a predictive framing and a generative framing, then contrast what each produces and when a business should reach for which.",
        build="A one-page comparison table showing predictive vs generative output on the same business problem, with a recommendation on when to use each.",
        services="ChatGPT, Google Gemini or Claude (free tier)",
        steps=[
            ("Open a GenAI chat assistant (ChatGPT, Gemini or Claude) and sign in with your own free account.", ""),
            ("Paste this set of five customer reviews for a Singapore cafe: two praising the coffee but criticising the wait, two on pricing, one on staff friendliness.", ""),
            ("PREDICTIVE framing — prompt: 'Classify each review as positive, negative or neutral and give the overall sentiment score.' Note the output is a label/score derived from existing data.", ""),
            ("GENERATIVE framing — prompt: 'Write a personalised 60-word reply to each reviewer in a warm brand voice, and draft three ideas to cut wait time.' Note the output is new content that did not exist before.", ""),
            ("TIP — be specific about ROLE, TASK, FORMAT and AUDIENCE. Compare 'write a reply' against 'You are a cafe owner. Write a 60-word reply to this reviewer in a warm, apologetic tone that offers a concrete fix.' The second prompt gives a usable answer; the first gives filler.", ""),
            ("Record in a table what each framing produced, what data it needed, and the business decision each one supports. Write one sentence on when your organisation should use each.", ""),
        ],
        test="Your table clearly shows predictive AI producing a label or forecast from historical data, and generative AI producing new content — and you can justify which one fits a named task in your organisation.",
    ),
    dict(
        num=2, topic=1,
        title="Map the Generative AI Tool Landscape",
        objective="K1 — survey generative AI tools across text, image, audio, video, digital human, productivity and data analysis.",
        desc="Build a personal tool map by testing one tool in each of four modalities, so you can pick the right tool for a business need instead of defaulting to a chat assistant. These are the tools you will use for the rest of the course.",
        build="A tool map listing at least eight GenAI tools by modality, each with its business use case, pricing tier and one limitation you observed.",
        services="ChatGPT/Gemini/Claude, Perplexity, Adobe Firefly or Microsoft Designer, Suno, Canva",
        steps=[
            ("TEXT — use a chat assistant to draft a 100-word product announcement for a service in your industry.", ""),
            ("RESEARCH — use Perplexity to find two 2026 statistics about GenAI adoption in your industry, and capture the source links it cites.", ""),
            ("IMAGE — use Adobe Firefly or Microsoft Designer (free credits) to generate a hero image for that announcement. Record the exact prompt you used.", ""),
            ("AUDIO — use Suno to generate a 30-second background track. Note the licence terms shown for free-tier output.", ""),
            ("TIP — free tiers change constantly. Record for each tool: what the free tier allows, whether output carries a watermark, and whether commercial use is permitted. You will need this before publishing anything.", ""),
            ("Record each tool in a table (modality, tool, business use case, free vs paid, one limitation you hit), then add three more from the slides so your map covers video, digital human and office productivity.", ""),
        ],
        test="Your tool map covers at least four modalities you tested first-hand plus three more from the slides, and for each tool you can name the business task it best supports and one limitation.",
    ),
    dict(
        num=3, topic=1,
        title="Research a Business Idea with Perplexity and NotebookLM",
        objective="K2, A1 — investigate business strategies, and the organisation's operating context, priorities, domain and environment, to identify business opportunities created by generative AI.",
        desc="STAGE 1 OF THE PIPELINE. Choose the business idea you will carry through the whole course, then research it properly: Perplexity for the external market with cited sources, NotebookLM for synthesising the documents into a grounded briefing you can trust.",
        build="A research briefing on ONE chosen business idea: market size and trend, three competitors, the customer problem, and three verified sources — plus a NotebookLM notebook containing the underlying documents.",
        services="Perplexity (Deep Research), Google NotebookLM, ChatGPT/Gemini/Claude",
        steps=[
            ("CHOOSE YOUR IDEA — pick ONE business idea you will use for every remaining lab. Good candidates: an AI tutoring service, a sustainable food brand, an AI customer-support assistant, a wellness app, or a service from your own organisation. Write it in one sentence: 'A <product/service> for <customer> that <solves what>.'", ""),
            ("PERPLEXITY — open perplexity.ai, select Deep Research mode, and prompt: 'Research the market for <your idea> in Singapore and Southeast Asia. Cover market size, growth trend, the top three competitors and what customers complain about. Cite your sources.'", ""),
            ("TIP — Perplexity is only as good as its sources. Open at least THREE cited links and confirm the claim actually appears there. AI-cited statistics are frequently misattributed; an unverified number in a board paper destroys your credibility.", ""),
            ("Run two follow-up prompts to go deeper: 'Who is the ideal customer and what do they pay today?' and 'What regulation or risk affects this market in Singapore?'", ""),
            ("NOTEBOOKLM — open notebooklm.google.com, create a notebook named after your idea, and add your sources: paste the Perplexity findings, upload any PDF or report you found, and add relevant web links.", ""),
            ("TIP — NotebookLM answers ONLY from the sources you give it, which is why it hallucinates far less than an open chat assistant. Every answer carries an inline citation — click it to jump to the exact passage. Use Perplexity to FIND sources, NotebookLM to REASON over them.", ""),
            ("In NotebookLM ask: 'What is the core customer problem?', 'What are the three biggest risks to this idea?' and 'Where do my sources disagree?' Then generate the Briefing Doc from the Studio panel.", ""),
            ("Write your research briefing on one page: the idea in one sentence, market size and trend, three competitors, the customer problem in the customer's own words, three verified sources, and the three biggest risks.", ""),
        ],
        test="Your briefing fits one page, every statistic traces to a source you personally opened, and your NotebookLM notebook answers the core-problem question with an inline citation.",
    ),
    dict(
        num=4, topic=1,
        title="Evaluate and Prioritise Your Business Idea",
        objective="A2 — evaluate opportunities for viability, applicability to the organisation and compatibility with business goals.",
        desc="STAGE 2 OF THE PIPELINE. Stress-test the idea from Lab 3 against alternatives using an explicit scoring rubric, so the decision to proceed can be defended to management rather than being a matter of taste.",
        build="A scored opportunity register comparing your chosen idea against five alternatives on business value, feasibility, data readiness, risk and strategic fit — with a defended recommendation.",
        services="ChatGPT/Gemini/Claude, Excel or Google Sheets",
        steps=[
            ("List your chosen idea from Lab 3 plus five alternatives — draw on Lab 2's tool map and your own operational pain points.", ""),
            ("Create a scoring table with five criteria: business value, feasibility, data readiness, risk (reverse-scored) and strategic fit. Score each idea 1-5 on every criterion.", ""),
            ("TIP — use the assistant as a CHALLENGER, not a cheerleader. Prompt: 'Act as a sceptical investor. For each of these six ideas, give the single strongest reason it would fail and the data I would need to disprove that.' Chat assistants agree too readily; you must explicitly ask them to argue against you.", ""),
            ("Adjust your scores with what the challenge surfaced. Note any score you did NOT change and why — defending a score is as valuable as revising it.", ""),
            ("Weight the criteria to match your organisation's current mandate (for example business value x2 if growth is the priority) and compute a weighted total per idea.", ""),
            ("Rank all six, confirm or replace your Lab 3 choice, and write one sentence linking the winner to a named organisational objective. Record why the bottom idea was rejected — a defensible decision documents its discards.", ""),
        ],
        test="Your register scores all six ideas on the five weighted criteria, your chosen idea maps to a named organisational objective, and you can explain why the lowest-ranked idea was rejected.",
    ),
]
