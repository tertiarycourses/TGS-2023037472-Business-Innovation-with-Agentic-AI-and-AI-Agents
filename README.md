# Digital Transformation and Business Innovation with Generative AI (GenAI)

**WSQ Course Code:** TGS-2023037472
**Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)
**Duration:** 2 days · 16 training hours · assessment 2 hours
**Skills Framework:** Business Innovation — `ICT-SNA-5003-1.1`
**Version:** v38 · 9 August 2026

Course page: <https://www.tertiarycourses.com.sg/wsq-digital-transformation-and-business-innovation-with-generative-ai-genai.html>

---

## The course in one line

You choose **one business idea** on Day 1 and carry it through **18 connected labs** —
research it, score it, model it, design it, produce a marketing video for it, pitch it,
govern it, and finally **automate the entire pipeline as an agentic AI workflow with a
human review gate.** Nothing is rebuilt from scratch; each lab consumes the artifact the
previous one produced.

```
Research → Evaluate → Design Thinking → Business Model Canvas → Architecture
   → Script → Voiceover → Soundtrack → Video → Pitch deck
      → Risk → Guardrails & Ethics → Action plan → KPIs → Comms → CAPSTONE (agentic workflow)
```

## Learning outcomes

| | Outcome |
|---|---|
| **LO1** | Evaluate and investigate generative AI business strategies to identify viable opportunities compatible with organisational objectives. |
| **LO2** | Develop action plans to implement business innovation with generative AI and design digital architectures to apply technologies across the business. |
| **LO3** | Manage business innovation and facilitate information flow among stakeholders to review success and develop innovative ideas. |

## The 18 labs

### Topic 1 — Introduction to Business Innovation and Generative AI  (K1, K2, A1, A2)
| # | Lab | Tools |
|---|---|---|
| 1 | [Compare Predictive and Generative AI](labs/lab-01-compare-predictive-and-generative-ai-on-a-business-task.md) | ChatGPT · Gemini · Claude |
| 2 | [Map the Generative AI Tool Landscape](labs/lab-02-map-the-generative-ai-tool-landscape.md) | Perplexity · Firefly · Suno |
| 3 | [Research a Business Idea](labs/lab-03-research-a-business-idea-with-perplexity-and-notebooklm.md) | Perplexity · NotebookLM |
| 4 | [Evaluate and Prioritise Your Business Idea](labs/lab-04-evaluate-and-prioritise-your-business-idea.md) | Chat assistant · Sheets |

### Topic 2 — Designing Digital Architectures and Processes  (K3, K4, A3, A4)
| # | Lab | Tools |
|---|---|---|
| 5 | [**GROUP** — Design Thinking Sprint](labs/lab-05-group-activity-run-a-design-thinking-sprint-in-design-thinking-studio.md) | [Design Thinking Studio](https://alfredang.github.io/designthinking/) |
| 6 | [**GROUP** — Business Model Canvas](labs/lab-06-group-activity-build-a-business-model-canvas-in-bmc-studio.md) | [BMC Studio](https://alfredang.github.io/bcm/) |
| 7 | [Design the Digital Architecture](labs/lab-07-design-the-digital-architecture-for-your-solution.md) | Draw.io · Canva |
| 8 | [Script a Marketing Video](labs/lab-08-script-a-marketing-video-for-your-business-idea.md) | ChatGPT · Gemini · Copilot 365 |
| 9 | [Create the AI Voiceover](labs/lab-09-create-the-ai-voiceover.md) | ElevenLabs |
| 10 | [Generate the Background Soundtrack](labs/lab-10-generate-the-background-soundtrack-with-suno.md) | Suno |
| 11 | [Produce the Video](labs/lab-11-produce-the-video-with-kling-and-an-ai-video-editor.md) | Kling AI · CapCut |
| 12 | [Build the Business Presentation](labs/lab-12-build-the-business-presentation-with-your-video.md) | Gamma |

### Topic 3 — Implementing and Managing Business Innovation  (K5, K6, A5, A6)
| # | Lab | Tools |
|---|---|---|
| 13 | [Risk-Assess Your GenAI Pipeline](labs/lab-13-risk-assess-your-generative-ai-pipeline.md) | IMDA MAGF · PDPA |
| 14 | [Security Guardrails and AI Ethics Principles](labs/lab-14-define-security-guardrails-and-ai-ethics-principles.md) | AI Verify |
| 15 | [Develop the Implementation Action Plan](labs/lab-15-develop-the-implementation-action-plan.md) | Sheets |
| 16 | [Measure and Review Innovation Success](labs/lab-16-measure-and-review-innovation-success.md) | Sheets |
| 17 | [Stakeholder Communication and Idea-Sharing](labs/lab-17-build-the-stakeholder-communication-and-idea-sharing-plan.md) | Gamma · Teams |
| 18 | [**CAPSTONE** — Agentic AI Workflow with Human Review](labs/lab-18-capstone-automate-the-pipeline-with-an-agentic-ai-workflow-and-human-review.md) | n8n |

## Repository contents

```
courseware/     slide deck (PPTX + PDF), Lesson Plan and Learner Guide (DOCX + PDF)
labs/           the 18 hands-on labs, one file each, plus an index
LG-*.md         the Learner Guide as Markdown (mirrors the DOCX)
.claude/skills/courseware-build/
                the single source — course_data.py + data_domain1..3.py drive
                EVERY artifact, so the deck, LP, LG and labs can never drift apart
```

### Rebuilding the courseware

All artifacts are generated from one content module. Edit `course_data.py` or
`data_domainN.py`, then:

```bash
bash .claude/skills/courseware-build/build/build_courseware.sh
```

This regenerates the deck, Lesson Plan, Learner Guide (DOCX + Markdown), the labs and
all PDFs, with page-numbered tables of contents.

Requires `python-pptx`, `python-docx`, `pypdf` and LibreOffice (`soffice`) for PDF export.

## Responsible use

Every lab runs on free-tier generative AI tools with the learner's own account.
Do not enter confidential, personal or client-identifying data into any public
generative AI tool. Treat every AI output as a draft and verify it before relying on it —
Labs 13 and 14 cover the risk assessment, guardrails and AI ethics principles in full.

## Not in this repository

The assessment papers and answer keys are trainer-only and are distributed through
Google Drive and the LMS, never here.

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · [tertiarycourses.com.sg](https://www.tertiarycourses.com.sg)
