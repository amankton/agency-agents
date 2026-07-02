# Batch Summary: batch_004

## Agents Reviewed
- `product/product-feedback-synthesizer.md`: Feedback Synthesizer (refactor)
- `product/product-sprint-prioritizer.md`: Sprint Prioritizer (merge)
- `product/product-trend-researcher.md`: Trend Researcher (keep)
- `product/product-behavioral-nudge-engine.md`: Behavioral Nudge Engine (rewrite)
- `project-management/project-management-project-shepherd.md`: Project Shepherd (refactor)
- `project-management/project-management-studio-producer.md`: Studio Producer (refactor)
- `project-management/project-management-studio-operations.md`: Studio Operations (keep)
- `project-management/project-management-experiment-tracker.md`: Experiment Tracker (rewrite)
- `project-management/project-management-jira-workflow-steward.md`: Jira Workflow Steward (keep)
- `project-management/project-management-meeting-notes-specialist.md`: Meeting Notes Specialist (keep)

## Recommended Actions
- Keep: 4
- Refactor: 3
- Merge: 1
- Split: 0
- Deprecate: 0
- Rewrite: 2

## Highest-Risk Agent
Behavioral Nudge Engine: the current prompt encourages adaptive behavioral nudges, preference memory, ADHD-oriented personalization, and channel delivery without a consent, privacy, opt-out, or dark-pattern boundary.

## Biggest Architecture Issue Found
The product/project-management cluster needs a decision-rights map. Feedback, trends, sprint planning, experiments, project coordination, studio operations, Jira workflow, and meeting notes all produce inputs for decisions, but several prompts imply they can make commitments, mutate tools, or steer users directly without PM, delivery, privacy, or executive approval.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_004.md`
- `agency-audit/refactored-agents/product-feedback-synthesizer.md`
- `agency-audit/refactored-agents/product-sprint-prioritizer.md`
- `agency-audit/refactored-agents/product-trend-researcher.md`
- `agency-audit/refactored-agents/product-behavioral-nudge-engine.md`
- `agency-audit/refactored-agents/project-management-project-shepherd.md`
- `agency-audit/refactored-agents/project-management-studio-producer.md`
- `agency-audit/refactored-agents/project-management-studio-operations.md`
- `agency-audit/refactored-agents/project-management-experiment-tracker.md`
- `agency-audit/refactored-agents/project-management-jira-workflow-steward.md`
- `agency-audit/refactored-agents/project-management-meeting-notes-specialist.md`
- `agency-audit/acceptance-tests/product-feedback-synthesizer.tests.md`
- `agency-audit/acceptance-tests/product-sprint-prioritizer.tests.md`
- `agency-audit/acceptance-tests/product-trend-researcher.tests.md`
- `agency-audit/acceptance-tests/product-behavioral-nudge-engine.tests.md`
- `agency-audit/acceptance-tests/project-management-project-shepherd.tests.md`
- `agency-audit/acceptance-tests/project-management-studio-producer.tests.md`
- `agency-audit/acceptance-tests/project-management-studio-operations.tests.md`
- `agency-audit/acceptance-tests/project-management-experiment-tracker.tests.md`
- `agency-audit/acceptance-tests/project-management-jira-workflow-steward.tests.md`
- `agency-audit/acceptance-tests/project-management-meeting-notes-specialist.tests.md`

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Feedback Synthesizer

Source: `product/product-feedback-synthesizer.md`

## 1. Current Function
Product feedback collection, qualitative synthesis, sentiment analysis, feature request analysis, and product insight reporting agent.

## 2. Current Role Boundary
Synthesize supplied voice-of-customer feedback into evidence-backed themes, sentiment, frequency, representative quotes, confidence, and product-risk signals.

## 3. Production Issues
- Overlaps Product Manager on discovery, roadmap prioritization, journey mapping, and feature scoring.
- Overlaps Trend Researcher on competitive and market signal analysis.
- Assumes multi-channel collection and analytics data without privacy, source, or consent constraints.

## 4. Token Waste
- Broad capability lists repeat PM and analytics roles.
- Dashboard and prediction claims exceed the core feedback-synthesis job.

## 5. Ambiguity Risks
- 'Actionable recommendations' can become roadmap decisions.
- Sentiment and theme accuracy claims are not tied to source quality or sample size.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as voice-of-customer synthesis only; PM and delivery roles keep decision ownership.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.6/10


---

# Agent Review: Sprint Prioritizer

Source: `product/product-sprint-prioritizer.md`

## 1. Current Function
Agile sprint planning, feature prioritization, resource allocation, velocity analysis, and stakeholder alignment agent.

## 2. Current Role Boundary
Produce PM-approved backlog sequencing, capacity tradeoffs, dependency risks, and sprint planning options without owning roadmap or stakeholder commitments.

## 3. Production Issues
- Heavily overlaps Product Manager on backlog ownership, RICE scoring, roadmap timing, scope control, and stakeholder alignment.
- Claims delivery success targets without requiring team history, capacity, or estimation confidence.
- Mixes prioritization analysis with team coaching, release planning, and resource allocation authority.

## 4. Token Waste
- Framework primer repeats standard product-management material.
- Success-metric targets are generic rather than input-driven.

## 5. Ambiguity Risks
- 'Commitment' can imply team or stakeholder commitments the agent cannot make.
- Resource allocation can mean analysis or manager authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Merge into Product Manager delivery-planning mode or keep only as a bounded sub-role with PM decision ownership.

## 8. Merge / Split / Deprecate Recommendation
Decision: merge

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 4

Final Rating: 4.0/10


---

# Agent Review: Trend Researcher

Source: `product/product-trend-researcher.md`

## 1. Current Function
Market intelligence, emerging trend, competitive analysis, market sizing, consumer insight, and technology scouting agent.

## 2. Current Role Boundary
Produce external market intelligence with cited sources, source freshness, confidence levels, competitive signals, trend implications, and explicit caveats.

## 3. Production Issues
- Overlaps Product Manager on opportunity assessment and strategic recommendations.
- Overlaps Feedback Synthesizer on consumer sentiment and user signal interpretation.
- Prediction and market sizing claims lack required source quality, recency, and confidence contracts.

## 4. Token Waste
- Broad research tool lists are less useful than required source schema.
- Prediction accuracy targets are unrealistic without a validation history.

## 5. Ambiguity Risks
- 'Drive product strategy' can imply decision authority.
- Market data may be stale, paid, unavailable, or jurisdiction-specific.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as external market intelligence specialist with mandatory source quality and decision-boundary controls.

## 8. Merge / Split / Deprecate Recommendation
Decision: keep

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.6/10


---

# Agent Review: Behavioral Nudge Engine

Source: `product/product-behavioral-nudge-engine.md`

## 1. Current Function
Behavioral psychology nudge, notification cadence, motivation, and micro-sprint interaction design agent.

## 2. Current Role Boundary
Design consent-respecting nudge strategies and interaction-pattern specs that reduce cognitive load while preserving user autonomy, opt-out, and notification preferences.

## 3. Production Issues
- Encourages adaptive behavioral nudges without explicit consent, preference, privacy, or manipulation boundaries.
- References ADHD and user psyche without clinical, sensitive-data, or profiling safeguards.
- Example copy implies drafting and sending through channels without approval gates.

## 4. Token Waste
- Persona language is stronger than the missing ethics contract.
- Example code implies implementation before consent and experiment design are defined.

## 5. Ambiguity Risks
- 'Maximize motivation' can become coercive engagement optimization.
- Autonomous memory updates can conflict with privacy and user control.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as autonomy-preserving interaction design with consent, privacy, and experiment guardrails.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.6/10


---

# Agent Review: Project Shepherd

Source: `project-management/project-management-project-shepherd.md`

## 1. Current Function
Cross-functional project coordination, timeline management, stakeholder alignment, resource planning, and risk management agent.

## 2. Current Role Boundary
Coordinate cross-functional delivery through project charters, dependency maps, risk registers, stakeholder updates, and change-control recommendations.

## 3. Production Issues
- Overlaps Agents Orchestrator, Product Manager, Senior Project Manager, Studio Producer, and Studio Operations.
- Claims budget, resource, and delivery outcomes without authority or baseline inputs.
- Can imply execution ownership rather than coordination and reporting.

## 4. Token Waste
- Generic PM templates duplicate Senior Project Manager outputs.
- Success metrics are broad and not tied to project constraints.

## 5. Ambiguity Risks
- 'Manage resources' can mean reporting, recommending, or assigning people.
- Change control requires decision authority not defined in the prompt.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Merge into Senior Project Manager or keep only as a narrow active-project delivery-coordination alias.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.4/10


---

# Agent Review: Studio Producer

Source: `project-management/project-management-studio-producer.md`

## 1. Current Function
Executive creative strategy, portfolio orchestration, resource allocation, budget planning, and studio leadership agent.

## 2. Current Role Boundary
Own strategic creative/technical portfolio planning and executive review while routing day-to-day execution and operations to delivery and studio-operations roles.

## 3. Production Issues
- Blends executive portfolio strategy, creative direction, project management, operations, resource allocation, and business development.
- Overlaps Project Shepherd on coordination and Studio Operations on operational systems.
- ROI, delivery, market, and client outcomes are asserted without source data or authority.

## 4. Token Waste
- Executive persona and success claims repeat strategy themes.
- Templates combine portfolio review with operational reporting.

## 5. Ambiguity Risks
- 'Resource allocation' can mean portfolio recommendation or actual staffing authority.
- Creative vision and business strategy ownership are not bounded.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as creative/studio production planner with executive decisions and portfolio approval outside the agent.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.6/10


---

# Agent Review: Studio Operations

Source: `project-management/project-management-studio-operations.md`

## 1. Current Function
Day-to-day studio operations, SOP design, resource coordination, vendor management, process optimization, and operational reporting agent.

## 2. Current Role Boundary
Improve studio operating systems through SOPs, resource coordination, vendor/process metrics, operational support, and continuous-improvement plans.

## 3. Production Issues
- Overlaps Studio Producer on portfolio resource allocation and Project Shepherd on delivery coordination.
- Assumes authority over vendors, facilities, tools, and costs.
- Operational metrics and savings claims require supplied baseline data.

## 4. Token Waste
- Generic operational excellence prose repeats process-improvement concepts.
- Success targets are static rather than context-specific.

## 5. Ambiguity Risks
- 'Implement' can imply executing changes, purchasing tools, or changing workflows.
- Resource coordination can become staffing authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as studio operations specialist with explicit authority and implementation gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: keep

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.8/10


---

# Agent Review: Experiment Tracker

Source: `project-management/project-management-experiment-tracker.md`

## 1. Current Function
Experiment design, A/B test management, statistical analysis, hypothesis validation, and experiment portfolio tracking agent.

## 2. Current Role Boundary
Track experiment design, approvals, instrumentation readiness, guardrails, results, and decisions without launching or interpreting beyond supplied data quality.

## 3. Production Issues
- Mixes experiment design, launch execution, statistical analysis, rollout decisions, and product recommendations.
- Assumes 95% confidence, sample-size reliability, and instrumentation quality without input data.
- Touches privacy, consent, and user-experience risk without mandatory approval gates.

## 4. Token Waste
- Statistical methodology claims are generic.
- Success metrics overpromise experiment significance and implementation rate.

## 5. Ambiguity Risks
- 'Execute experiments' can mean coordination, launch, analysis, or product rollout.
- Go/no-go recommendation can be mistaken for decision authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as experiment registry and decision-support agent with explicit data-quality, consent, approval, and inconclusive-result handling.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.4/10


---

# Agent Review: Jira Workflow Steward

Source: `project-management/project-management-jira-workflow-steward.md`

## 1. Current Function
Jira-linked Git workflow, branch naming, commit hygiene, PR structure, release traceability, and delivery governance agent.

## 2. Current Role Boundary
Prepare Jira-linked Git workflow guidance, branch/commit/PR templates, traceability checks, and delivery packets under repository-specific policies.

## 3. Production Issues
- Can imply branch, commit, PR, or Jira ticket mutation without declaring tool authority.
- Hardcodes branch strategy, Gitmoji, and Jira policy that may conflict with local repository rules.
- Includes executable hook code and external references without fallback or versioning context.

## 4. Token Waste
- Gitmoji and hook examples are useful references but too prominent for a general contract.
- Traceability rhetoric repeats the core role.

## 5. Ambiguity Risks
- 'Enforce' can mean advise, validate, block, or mutate repositories.
- Jira-linked workflow may not apply to every project or task.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as policy-aware workflow advisor with explicit tool authority and local repository policy inputs.

## 8. Merge / Split / Deprecate Recommendation
Decision: keep

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.8/10


---

# Agent Review: Meeting Notes Specialist

Source: `project-management/project-management-meeting-notes-specialist.md`

## 1. Current Function
Meeting transcript and rough-note extractor for structured decisions, action items, and open questions.

## 2. Current Role Boundary
Extract decisions, action items, open questions, attendees, and date from supplied meeting content without inventing or editorializing.

## 3. Production Issues
- Strong source-as-data discipline already exists.
- Tool list includes Write/Edit even though most uses only need output generation.
- Could benefit from a standard blocked response and handoff payload for missing meeting basics.

## 4. Token Waste
- Minimal; examples are compact and useful.

## 5. Ambiguity Risks
- Clarification behavior can be awkward in batch processing.
- Output destination is not explicitly governed.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep with light standardization around blocked output, confidentiality, and approved writing.

## 8. Merge / Split / Deprecate Recommendation
Decision: keep

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 5.0/10
