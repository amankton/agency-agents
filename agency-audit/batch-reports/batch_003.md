# Batch Summary: batch_003

## Agents Reviewed
- `specialized/sales-outreach.md`: Sales Outreach (deprecate)
- `sales/sales-outbound-strategist.md`: Outbound Strategist (keep)
- `sales/sales-offer-lead-gen-strategist.md`: Offer & Lead Gen Strategist (keep)
- `sales/sales-account-strategist.md`: Account Strategist (keep)
- `specialized/customer-success-manager.md`: Customer Success Manager (refactor)
- `support/support-support-responder.md`: Support Responder (split)
- `specialized/customer-service.md`: Customer Service (refactor)
- `sales/sales-pipeline-analyst.md`: Pipeline Analyst (refactor)
- `sales/sales-deal-strategist.md`: Deal Strategist (keep)
- `sales/sales-proposal-strategist.md`: Proposal Strategist (keep)

## Recommended Actions
- Keep: 5
- Refactor: 3
- Merge: 0
- Split: 1
- Deprecate: 1
- Rewrite: 0

## Highest-Risk Agent
Support Responder: the current prompt blends customer-facing support, support operations, analytics code, KB ownership, customer success, and retention into one agent without enough policy, authority, or escalation boundaries.

## Biggest Architecture Issue Found
The sales and post-sale cluster is not primarily a dangerous-tool problem. It is an ownership problem. Broad prompts attempt to own the whole customer lifecycle, which makes routing unstable and allows customer/account facts, commercial terms, support policy, or promises to be invented when source evidence is missing.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_003.md`
- `agency-audit/refactored-agents/sales-outreach.md`
- `agency-audit/refactored-agents/sales-outbound-strategist.md`
- `agency-audit/refactored-agents/sales-offer-lead-gen-strategist.md`
- `agency-audit/refactored-agents/sales-account-strategist.md`
- `agency-audit/refactored-agents/customer-success-manager.md`
- `agency-audit/refactored-agents/support-support-responder.md`
- `agency-audit/refactored-agents/customer-service.md`
- `agency-audit/refactored-agents/sales-pipeline-analyst.md`
- `agency-audit/refactored-agents/sales-deal-strategist.md`
- `agency-audit/refactored-agents/sales-proposal-strategist.md`
- `agency-audit/acceptance-tests/sales-outreach.tests.md`
- `agency-audit/acceptance-tests/sales-outbound-strategist.tests.md`
- `agency-audit/acceptance-tests/sales-offer-lead-gen-strategist.tests.md`
- `agency-audit/acceptance-tests/sales-account-strategist.tests.md`
- `agency-audit/acceptance-tests/customer-success-manager.tests.md`
- `agency-audit/acceptance-tests/support-support-responder.tests.md`
- `agency-audit/acceptance-tests/customer-service.tests.md`
- `agency-audit/acceptance-tests/sales-pipeline-analyst.tests.md`
- `agency-audit/acceptance-tests/sales-deal-strategist.tests.md`
- `agency-audit/acceptance-tests/sales-proposal-strategist.tests.md`

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Sales Outreach

Source: `specialized/sales-outreach.md`

## 1. Current Function
Broad B2B sales outreach prompt covering prospecting, cold outreach, objection handling, proposal writing, and pipeline management.

## 2. Current Role Boundary
Serve only as a legacy sales-intake fallback that routes outreach, offer, deal, proposal, and pipeline work to narrower canonical sales agents.

## 3. Production Issues
- Duplicates Outbound Strategist, Offer and Lead Gen Strategist, Deal Strategist, Proposal Strategist, and Pipeline Analyst responsibilities.
- Claims full lifecycle ownership from ICP to closed deals without handoff boundaries.
- Does not require consent, opt-out, CRM authority, claims substantiation, or approved offer context before outreach artifacts are produced.

## 4. Token Waste
- Large embedded templates duplicate specialist sales prompts.
- Persona and memory prose obscures the need for a routing contract.

## 5. Ambiguity Risks
- 'Pipeline management' can mean analysis, CRM updates, or deal strategy.
- Proposal writing overlaps a dedicated proposal agent without compliance or pricing inputs.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Deprecate as a canonical execution agent and preserve only as a migration shim to route legacy calls.

## 8. Merge / Split / Deprecate Recommendation
Decision: deprecate

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 3
- Maintainability: 3
- Output Consistency: 3
- Orchestration Fit: 3

Final Rating: 3.0/10


---

# Agent Review: Outbound Strategist

Source: `sales/sales-outbound-strategist.md`

## 1. Current Function
Signal-based outbound strategy and multi-channel prospecting sequence agent.

## 2. Current Role Boundary
Design signal-based outbound strategy, ICP/account tiering, sequence architecture, and reply-rate optimization up to booked-meeting readiness.

## 3. Production Issues
- Overlaps legacy Sales Outreach and Offer and Lead Gen Strategist on ICP, cold outreach, and channel sequencing.
- Benchmarks and signal sources are asserted without requiring data provenance.
- No explicit compliance, opt-out, or sending-authority gate is required.

## 4. Token Waste
- Long outbound methodology examples can be references.
- Persona language repeats the relevance-first selling principle.

## 5. Ambiguity Risks
- 'Build pipeline' could imply sending or CRM mutation.
- Signal freshness thresholds depend on available tooling and market context.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as the canonical outbound strategy agent with explicit compliance and non-sending defaults.

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

# Agent Review: Offer & Lead Gen Strategist

Source: `sales/sales-offer-lead-gen-strategist.md`

## 1. Current Function
Top-of-funnel offer, lead magnet, and lead-generation strategy agent.

## 2. Current Role Boundary
Design validated offers, lead magnets, capture requirements, nurture prerequisites, channel selection, and amplifier strategy before execution.

## 3. Production Issues
- Can drift into outbound execution, paid media, content operations, and affiliate operations.
- Guarantee and risk-reversal recommendations need legal, financial, and fulfillment constraints.
- Lead capture touches privacy and consent without requiring data collection policy inputs.

## 4. Token Waste
- Value-equation and channel examples are repeated at length.
- Motivational language adds less value than source requirements and kill criteria.

## 5. Ambiguity Risks
- 'Rule of 100' can imply unsafe volume without channel, consent, and capacity constraints.
- Guarantee recommendations may become unsupported commercial promises.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as top-of-funnel architect and require evidence, economics, and consent gates before execution handoff.

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

# Agent Review: Account Strategist

Source: `sales/sales-account-strategist.md`

## 1. Current Function
Post-sale account growth, QBR, stakeholder mapping, churn prevention, and expansion strategy agent.

## 2. Current Role Boundary
Plan post-sale account expansion using account health, stakeholder maps, QBR evidence, churn signals, and customer-value business cases.

## 3. Production Issues
- Expansion planning overlaps Customer Success Manager, Deal Strategist, Pipeline Analyst, and Proposal Strategist.
- Assumes usage, support, NRR, and relationship data are available.
- Can imply commercial action without AE, legal, discount, or contract authority.

## 4. Token Waste
- QBR and churn templates duplicate Customer Success Manager material.
- Expansion success rhetoric repeats without a source-data contract.

## 5. Ambiguity Risks
- 'Execute expansion' may mean planning, customer outreach, proposal creation, or negotiation.
- Health score rules are not tied to product-specific thresholds.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as post-sale account strategy agent while encoding health-first and commercial-authority boundaries.

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

# Agent Review: Customer Success Manager

Source: `specialized/customer-success-manager.md`

## 1. Current Function
Customer success lifecycle agent spanning onboarding, health scoring, QBRs, churn prevention, expansion identification, and renewal support.

## 2. Current Role Boundary
Manage post-sale customer health through onboarding, adoption, QBRs, churn-risk plans, renewal readiness, and expansion identification without owning support or commercial execution.

## 3. Production Issues
- Blends CSM lifecycle ownership with support escalation, retention, expansion, renewals, and sales motion.
- Assumes product usage, ticket, contract, and relationship data exist.
- May overpromise roadmap, discounts, concessions, or renewal terms to save accounts.

## 4. Token Waste
- Large frameworks repeat Account Strategist and Support Responder concepts.
- Persona history and memory claims are longer than the role boundary.

## 5. Ambiguity Risks
- 'Expansion' can mean identification, strategy, proposal, or closing.
- Renewal management overlaps commercial and legal ownership.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into a post-sale health coordinator with explicit support, sales, product, and legal handoff boundaries.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.2/10


---

# Agent Review: Support Responder

Source: `support/support-support-responder.md`

## 1. Current Function
Broad customer support prompt mixing frontline response, support operations, analytics, KB management, proactive success, and retention.

## 2. Current Role Boundary
Provide bounded support-response planning, escalation routing, macro/KB guidance, and support-ops recommendations from supplied policies and ticket context.

## 3. Production Issues
- Acts as frontline support, support operations, KB manager, analytics reporter, customer success, and retention agent.
- Embedded analytics code assumes data shape and execution context.
- SLA, refund, billing, and retention guidance are not tied to account policy or authority limits.

## 4. Token Waste
- Large Python analytics example belongs in a reference or separate support-ops agent.
- Support culture language repeats the same service-quality goals.

## 5. Ambiguity Risks
- 'Resolve issue' may mean draft reply, execute account changes, approve refunds, or route escalation.
- Proactive customer success overlaps CSM.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split customer-facing response from support-ops analytics; use this artifact as the bounded support-response and routing contract.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

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

# Agent Review: Customer Service

Source: `specialized/customer-service.md`

## 1. Current Function
Generic any-industry customer service agent for inquiries, complaints, account support, refunds, retention, and escalation.

## 2. Current Role Boundary
Handle low-risk Tier 1 customer interactions using supplied business policies, verified customer context, and escalation rules.

## 3. Production Issues
- Generic any-industry scope overlaps Support Responder and vertical support specialists.
- Retention guidance can become dark-pattern cancellation friction if not governed by policy.
- Account, refund, order, billing, and identity verification actions need authority and policy inputs.

## 4. Token Waste
- Many conversation templates duplicate support macros.
- Universal service persona text is longer than the policy contract.

## 5. Ambiguity Risks
- 'There is always something you can do' can conflict with policy, safety, or regulation.
- Refund and cancellation handling may require live account authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into canonical Tier 1 customer interaction agent with vertical and exception handoffs.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.2/10


---

# Agent Review: Pipeline Analyst

Source: `sales/sales-pipeline-analyst.md`

## 1. Current Function
Revenue operations pipeline analytics, deal health, and forecast diagnostics agent.

## 2. Current Role Boundary
Analyze CRM pipeline health, forecast ranges, coverage, velocity, data quality, and at-risk opportunities from supplied pipeline data.

## 3. Production Issues
- Deal scoring and MEDDPICC guidance overlaps Deal Strategist.
- Assumes CRM and historical benchmark data exist.
- Forecast methodology can imply false precision when data quality is poor.

## 4. Token Waste
- Detailed MEDDPICC content duplicates Deal Strategist.
- Advanced analytics claims exceed the minimum pipeline report contract.

## 5. Ambiguity Risks
- 'Data-driven sales coaching' may become people management or tactical deal strategy.
- AI-driven forecast scoring is mentioned without model or validation inputs.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as read-only RevOps analyst and hand tactical opportunity plans to Deal Strategist.

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

# Agent Review: Deal Strategist

Source: `sales/sales-deal-strategist.md`

## 1. Current Function
MEDDPICC opportunity assessment, competitive positioning, win planning, and deal inspection agent.

## 2. Current Role Boundary
Create active-opportunity strategy using MEDDPICC evidence, competitive context, buyer process, champion testing, and close-path risk mitigation.

## 3. Production Issues
- Overlaps Pipeline Analyst on deal health and Proposal Strategist on competitive positioning.
- Benchmark claims are presented without requiring local historical evidence.
- Commercial teaching and landmine tactics need ethical, claims, and buyer-context constraints.

## 4. Token Waste
- Long methodology primer could be a reference.
- Success metrics should be supplied by business context.

## 5. Ambiguity Risks
- 'Win planning' can imply contacting buyers, changing price, or writing proposals.
- Competitive landmines can drift into negative or unsupported competitor claims.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as active-opportunity strategist with clear evidence, ethics, and commercial authority boundaries.

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

# Agent Review: Proposal Strategist

Source: `sales/sales-proposal-strategist.md`

## 1. Current Function
Proposal, RFP, win-theme, executive-summary, and narrative strategy agent.

## 2. Current Role Boundary
Design proposal and RFP artifacts with win themes, executive summary, narrative architecture, compliance overlay, and evidence-backed language.

## 3. Production Issues
- Win themes and competitive framing overlap Deal Strategist.
- Pricing and compliance sections require approved inputs from legal, finance, and solution owners.
- Can invent buyer research, proof points, or claims if evidence is missing.

## 4. Token Waste
- Narrative methodology examples are useful but long.
- Content quality slogans repeat the evidence-backed requirement.

## 5. Ambiguity Risks
- 'Proposal writing' can mean strategy, drafting, compliance matrix, final submission, or pricing authority.
- Black-hat review language needs ethical and evidence constraints.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as proposal artifact specialist with evidence, compliance, pricing, and legal approval gates.

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
