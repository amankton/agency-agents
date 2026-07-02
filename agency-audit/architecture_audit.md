# The Agency Architecture Audit

## Executive Summary
This clone contains 210 frontmatter-defined agent prompt files, not the 232 stated in the protocol. The system has useful specialist coverage, but it is a prompt collection more than a governed execution architecture: agents have rich personas, weak input contracts, inconsistent outputs, duplicated coordination roles, and frequent tool assumptions without failure behavior.

## System-Level Diagnosis
The repository's strongest asset is breadth. Its biggest structural weakness is orchestration ambiguity. There are multiple agents that coordinate, plan, validate, and hand off work, but no canonical router contract, agent registry, state schema, readiness taxonomy, or merge policy. High-risk agents also include live spend, production mutation, offensive security, and autonomous routing behavior without sufficient authorization gates.

## Agent Category Breakdown
| Category | Count | Notes |
|---|---:|---|
| Router / Orchestrator | 9 | Small count but high blast radius; routing and state contracts are underdefined. |
| Research / Intelligence | 0 | Includes finance/security/paid-media research, some with high-risk live-action implications. |
| Strategy / Planning | 128 | Large planning layer with overlapping PM, product, portfolio, and workflow responsibilities. |
| Execution / Production | 13 | Broad specialist roster; most agents need explicit inputs, outputs, and refusal conditions. |
| QA / Validation | 54 | Useful skepticism, but tool paths and evidence schemas need normalization. |
| Memory / State Management | 1 | Memory appears as duplicated variants instead of a governed extension pattern. |
| Tool-Use / API | 0 | Tool assumptions are often declared without fallback behavior. |
| Client-Facing Communication | 5 | Many domain specialists blur strategy, production, and communication. |
| Internal Operations | 0 | Needs deeper batch review. |
| Redundant / Deprecated / Unclear | 0 | Needs deeper batch review. |

## Top Structural Risks
1. Router, planner, PM, QA, and final response responsibilities are mixed across high-blast-radius agents.
2. Tool access is often assumed through prompt text instead of declared as available inputs with tool-failure behavior.
3. Several agents imply live mutation of production systems, ad spend, security targets, data, or routing without explicit approval contracts.

## Duplicate Or Overlapping Agents
| Agents | Overlap | Recommendation |
|---|---|---|
| Backend Architect; Backend Architect with Memory | Same backend role with memory text appended in integration variant. | Merge memory rules into canonical agent as optional extension. |
| Agents Orchestrator; Workflow Architect; Chief of Staff; Project Shepherd | Coordination, routing, state, and handoff ownership blur together. | Split by intake/routing, workflow specification, executive context, and project coordination. |
| Evidence Collector; Reality Checker | Both demand evidence and screenshots; one task-level, one release-level. | Keep both, but define handoff and severity thresholds. |
| Sales Outreach; Outbound Strategist; Offer and Lead Gen Strategist | Top-of-funnel sales ownership overlaps. | Merge or establish sequence: offer -> prospecting strategy -> outreach execution. |
| Product Manager; Feedback Synthesizer; Sprint Prioritizer; Trend Researcher | Product Manager absorbs specialist responsibilities. | Refactor PM as product coordinator and keep specialists as bounded input producers. |
| Support Responder; Customer Service; vertical service agents | Support interaction, customer success, KB, and vertical escalation overlap. | Split support operations from interaction; keep verticals as constrained extensions. |
| PPC Strategist; Search Query Analyst; Paid Media Auditor | Paid search audit and optimization responsibilities overlap. | Scope by account strategy, query mining, and audit validation. |

## Missing Architecture Components
- Canonical intake/router schema with supported request classes and unsupported-request behavior.
- Central agent registry with role, trigger, required inputs, tools, and handoff targets.
- Shared state and handoff payload standard used by all orchestrated agents.
- Evidence taxonomy for task QA vs release certification.
- Safety gate pattern for offensive security, live ops, paid-media spend, data remediation, and autonomous routing.
- Memory policy covering data minimization, staleness, tags, and unavailable memory behavior.

## Recommended Target Architecture
Use a layered architecture: Intake Router -> Planner -> Specialist Executors -> QA Validator -> Memory/State Service -> Final Response Packager. Specialist agents should not self-orchestrate beyond their boundary. The router should select agents from a registry, the planner should define dependencies and success criteria, executors should return structured artifacts, QA should verify against acceptance criteria, safety-sensitive agents should require explicit authorization gates, memory should store only governed state, and the final response agent should summarize only completed work.

## Immediate Actions
1. Continue the batch sequence in `batch_roadmap.md`, prioritizing privileged mutation, security, spend, money, and regulated-data agents.
2. Create a canonical handoff payload and require it in orchestrator, PM, workflow, QA, and safety-gated agents.
3. Make read-only recommendation the default for production mutation, security testing, ad platform changes, data remediation, and autonomous routing.
