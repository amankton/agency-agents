# Batch Summary: batch_012

## Agents Reviewed
- `finance/finance-bookkeeper-controller.md`: Bookkeeper & Controller (split)
- `finance/finance-financial-analyst.md`: Financial Analyst (refactor)
- `finance/finance-fpa-analyst.md`: FP&A Analyst (refactor)
- `finance/finance-tax-strategist.md`: Tax Strategist (rewrite)
- `finance/finance-investment-researcher.md`: Investment Researcher (refactor)
- `specialized/legal-document-review.md`: Legal Document Review (split)
- `specialized/legal-client-intake.md`: Legal Client Intake (refactor)
- `specialized/legal-billing-time-tracking.md`: Legal Billing & Time Tracking (split)
- `specialized/healthcare-customer-service.md`: Healthcare Customer Service (refactor)
- `specialized/healthcare-marketing-compliance.md`: Healthcare Marketing Compliance Specialist (rewrite)

## Recommended Actions
- Keep: 0
- Refactor: 5
- Merge: 0
- Split: 3
- Deprecate: 0
- Rewrite: 2

## Highest-Risk Agent
Healthcare Customer Service: it is live patient-facing, may handle PHI, emergencies, self-harm signals, clinical questions, billing distress, proxy access, and identity verification. Tax Strategist and Healthcare Marketing Compliance are close runners-up because they depend on current law and licensed review.

## Biggest Architecture Issue Found
High-stakes verticals blend draft analysis with licensed practice and live operations. Batch 012 separates source-backed artifacts from filings, trades, fund movement, legal/tax/medical advice, PHI disclosure, regulated publication, trust-account actions, and accounting mutations.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_012.md`
- `agency-audit/refactored-agents/finance-bookkeeper-controller.md`
- `agency-audit/refactored-agents/finance-financial-analyst.md`
- `agency-audit/refactored-agents/finance-fpa-analyst.md`
- `agency-audit/refactored-agents/finance-tax-strategist.md`
- `agency-audit/refactored-agents/finance-investment-researcher.md`
- `agency-audit/refactored-agents/legal-document-review.md`
- `agency-audit/refactored-agents/legal-client-intake.md`
- `agency-audit/refactored-agents/legal-billing-time-tracking.md`
- `agency-audit/refactored-agents/healthcare-customer-service.md`
- `agency-audit/refactored-agents/healthcare-marketing-compliance.md`
- `agency-audit/acceptance-tests/finance-bookkeeper-controller.tests.md`
- `agency-audit/acceptance-tests/finance-financial-analyst.tests.md`
- `agency-audit/acceptance-tests/finance-fpa-analyst.tests.md`
- `agency-audit/acceptance-tests/finance-tax-strategist.tests.md`
- `agency-audit/acceptance-tests/finance-investment-researcher.tests.md`
- `agency-audit/acceptance-tests/legal-document-review.tests.md`
- `agency-audit/acceptance-tests/legal-client-intake.tests.md`
- `agency-audit/acceptance-tests/legal-billing-time-tracking.tests.md`
- `agency-audit/acceptance-tests/healthcare-customer-service.tests.md`
- `agency-audit/acceptance-tests/healthcare-marketing-compliance.tests.md`

## Subagent Inputs Used
- Finance scan: split Bookkeeper & Controller; refactor Financial Analyst, FP&A Analyst, and Investment Researcher; rewrite Tax Strategist around current-law gates and licensed review.
- Legal/healthcare scan: split Legal Document Review and Legal Billing; refactor Legal Intake and Healthcare Customer Service; rewrite Healthcare Marketing Compliance around legal, PHI, and regulatory gates.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Bookkeeper & Controller

Source: `finance/finance-bookkeeper-controller.md`

## 1. Current Function
Bookkeeping and controllership specialist for close checklists, reconciliations, journal-entry drafts, financial statement support, internal controls, audit readiness, and accounting operations governance.

## 2. Current Role Boundary
Prepare accounting close, reconciliation, control, and draft financial-record artifacts from authorized source data while separating bookkeeping execution from controller review and blocking live bank, payroll, vendor, ERP, journal, period-lock, prior-period, and financial-statement release actions without approval.

## 3. Production Issues
- Original prompt blends day-to-day bookkeeping execution, controller approval, financial statement release, SOX controls, payroll, AP/AR, bank, ERP, and audit readiness into one role.
- Accounting operations can affect financial statements, payroll, vendors, bank activity, taxes, audit evidence, and stakeholder reporting.
- Overlaps Accounts Payable, Finance Tracker, FP&A, Financial Analyst, Tax Strategist, payroll, audit, and ERP administration roles.

## 4. Token Waste
- Large close templates should be generated from entity, period, accounting basis, ERP, and approval matrix.
- Operational playbook should be split from controller-review authority.

## 5. Ambiguity Risks
- 'Maintain financial records' can imply posting to the ERP or releasing statements.
- Controller review, bookkeeping entry preparation, and cash movement authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split bookkeeping execution from controller approval with source records, approval matrix, segregation-of-duties, read-only ERP default, draft entries, audit logs, PII redaction, prior-period gates, and financial-statement release controls.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.0/10


---

# Agent Review: Financial Analyst

Source: `finance/finance-financial-analyst.md`

## 1. Current Function
Financial analysis specialist for models, forecasts, valuations, unit economics, scenario analysis, KPI dashboards, business cases, and decision-support narratives.

## 2. Current Role Boundary
Produce financial models, scenario analysis, variance insights, and decision-support artifacts from reconciled source data with explicit assumptions, sensitivity, limitations, and audience boundaries, without approving capital allocation, external disclosures, trades, or operational system mutations.

## 3. Production Issues
- Original prompt can imply capital-allocation recommendations and board/external decision support without approval boundaries.
- Financial models can create false precision when assumptions, source lineage, and sensitivity analysis are missing.
- Overlaps FP&A, Investment Researcher, Pricing Analyst, Business Strategist, Data/Analytics, and CFO roles.

## 4. Token Waste
- Model templates should be selected by decision objective and data availability.
- Broad finance catalog should become scoped modeling modes.

## 5. Ambiguity Risks
- 'Investment decisions' can be internal capital allocation or regulated investment advice.
- Forecasts can be mistaken for facts if actuals/projections are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with source lineage, actual/projection separation, assumptions, base/upside/downside cases, sensitivity, model versioning, internal-use boundaries, no investment advice, and no system mutation gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.6/10


---

# Agent Review: FP&A Analyst

Source: `finance/finance-fpa-analyst.md`

## 1. Current Function
Financial planning and analysis specialist for AOP, rolling forecasts, budget vs actuals, driver-based planning, headcount planning, variance explanations, and executive operating reviews.

## 2. Current Role Boundary
Produce FP&A planning, forecasting, budget variance, driver, and tradeoff artifacts from approved targets and closed actuals without approving budgets, headcount, procurement, compensation, external guidance, or planning-system loads without owner authorization.

## 3. Production Issues
- FP&A outputs influence budget, headcount, procurement, compensation, and external expectations.
- Original prompt can imply business-owner or board approval authority rather than analysis and planning support.
- Overlaps Financial Analyst, Pricing Analyst, Business Strategist, Sales Pipeline Analyst, Finance Tracker, HR/recruiting, and CFO roles.

## 4. Token Waste
- Planning templates should be generated from AOP cadence, cost-center map, and driver definitions.
- Generic FP&A playbook should be scoped to plan/forecast/variance mode.

## 5. Ambiguity Risks
- 'Own the forecast' can imply approval authority.
- Budget-owner communications and planning-system loads are not separated from analysis.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with approved targets, closed actuals, driver definitions, budget owners, plan/forecast/actual separation, tradeoff framing, forecast validation, and no budget/headcount/procurement approval gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.6/10


---

# Agent Review: Tax Strategist

Source: `finance/finance-tax-strategist.md`

## 1. Current Function
Tax strategy and compliance support specialist for issue spotting, jurisdictional fact gathering, planning alternatives, uncertain-position risk summaries, deadline awareness, and CPA/attorney handoffs.

## 2. Current Role Boundary
Produce source-backed tax issue spotting, planning questions, risk summaries, deadline flags, and licensed-review packets for specified jurisdictions and tax years without providing tax/legal opinions, filings, elections, payments, entity restructurings, transfer-pricing implementation, or evasion guidance.

## 3. Production Issues
- Original prompt overstates tax optimization authority across changing, multi-jurisdictional law and can read like professional tax/legal advice.
- Tax recommendations can affect filings, elections, entity structures, transfer pricing, penalties, audits, privilege, and cash obligations.
- Overlaps Legal Compliance, Legal Document Review, Bookkeeper/Controller, Financial Analyst, payroll, HR, international advisors, and CPA/attorney reviewers.

## 4. Token Waste
- Broad tax-code catalog should be replaced by scoped issue-spotting and licensed-review packets.
- Optimization language needs current-source and uncertainty gates.

## 5. Ambiguity Risks
- 'Minimize liability' can drift into aggressive positions or evasion-adjacent advice.
- Tax strategy, legal opinion, filing authority, and implementation authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as tax issue-spotting and licensed-review support with current primary-source citations, jurisdiction/tax-year gates, uncertainty ratings, deadline flags, no tax/legal opinion, no filing/election/payment authority, and no evasion guidance.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 4
- Maintainability: 3
- Output Consistency: 4
- Orchestration Fit: 2

Final Rating: 3.2/10


---

# Agent Review: Investment Researcher

Source: `finance/finance-investment-researcher.md`

## 1. Current Function
Investment research specialist for fundamental/quantitative research, diligence, valuation, thesis development, catalysts, downside analysis, portfolio context, and risk summaries.

## 2. Current Role Boundary
Produce institutional-style investment research, valuation, diligence, and risk analysis from current primary sources with clear horizon, mandate, conflicts, and compliance caveats, without personalized investment advice, suitability determinations, trading, order placement, MNPI use, or market-moving publication authority.

## 3. Production Issues
- Investment research can become personalized advice, suitability assessment, trading signal, or market-moving publication.
- Original prompt implies actionable investment opportunities without enough mandate, conflict, MNPI, data-license, or compliance boundaries.
- Overlaps Financial Analyst, Business Strategist, Trend Researcher, Legal/Compliance, Data/Analytics, and portfolio management roles.

## 4. Token Waste
- Research templates should be generated from asset class, mandate, horizon, and source packet.
- Performance claims should be evidence-backed and caveated.

## 5. Ambiguity Risks
- 'Actionable insights' can imply trading recommendations.
- Primary-source requirements need timestamps and current data validation.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with mandate/horizon, current primary-source citations, source timestamps, bull/base/bear cases, downside quantification, thesis breakers, conflicts/MNPI attestation, no personalized advice, and no trading gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.4/10


---

# Agent Review: Legal Document Review

Source: `specialized/legal-document-review.md`

## 1. Current Function
Legal document review support specialist for contract summaries, litigation document issue spotting, risk flags, version comparison, clause checklists, and attorney-ready review packets.

## 2. Current Role Boundary
Perform attorney-supervised first-pass document intake, summary, issue spotting, clause flagging, and version comparison with citations to supplied documents, while blocking legal advice, definitive enforceability/compliance conclusions, filings, redlines, counterparty communications, or legal language changes without attorney approval.

## 3. Production Issues
- Original prompt spans contracts, litigation, real estate, compliance, version comparison, and risk review across jurisdictions and practice areas.
- Legal review can become unauthorized practice of law if findings are framed as legal conclusions rather than attorney-review flags.
- Overlaps contract redlining, litigation support, privacy/compliance, legal intake, and attorney roles.

## 4. Token Waste
- Long legal review playbooks should be scoped by document type, client role, jurisdiction, and attorney playbook.
- Risk templates should be generated from review purpose.

## 5. Ambiguity Risks
- 'Compliance checking' can imply definitive legal conclusions.
- First-pass review, redlining, and attorney legal judgment are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split document review support from attorney legal judgment with supplied-document citations, client-role/jurisdiction gates, attorney playbook, privilege handling, no legal advice, no redline/filing/counterparty authority.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.0/10


---

# Agent Review: Legal Client Intake

Source: `specialized/legal-client-intake.md`

## 1. Current Function
Legal client intake support specialist for matter triage, prospect information collection, conflict-check preparation, urgency flagging, consultation routing, and attorney-ready intake summaries.

## 2. Current Role Boundary
Collect and organize prospective-client intake information, urgency signals, conflict-check inputs, and consultation handoff summaries under firm policies without providing legal advice, promising outcomes, clearing conflicts, or scheduling consultations before conflict and authority gates are satisfied.

## 3. Production Issues
- Intake touches confidential prospect information before representation and can trigger conflict, deadline, fee, referral, and anti-discrimination obligations.
- Original prompt can imply case qualification, conflict clearance, and scheduling authority without attorney/admin gates.
- Overlaps customer service, CRM/calendar operators, legal document review, sales intake, conflict-check admins, and attorneys.

## 4. Token Waste
- Practice-area scripts should be generated from firm scope and jurisdiction.
- Generic intake examples should become policy-bound summary fields.

## 5. Ambiguity Risks
- 'Qualify prospects' can imply legal assessment.
- Scheduling and consultation routing depend on conflict status and firm policy.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with no legal advice, conflict pending blocks, statute/deadline escalation, confidentiality for non-clients, anti-discrimination, referral/fee policy, CRM/calendar authority gates, and attorney-ready summaries.

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

# Agent Review: Legal Billing & Time Tracking

Source: `specialized/legal-billing-time-tracking.md`

## 1. Current Function
Legal billing and time-tracking support specialist for time capture standards, billing narratives, invoice review, WIP/AR reporting, realization analysis, collections drafts, and trust-account compliance checks.

## 2. Current Role Boundary
Prepare legal time-entry, billing narrative, invoice review, WIP/AR, collections, and trust-account analysis as draft/report artifacts while separating billing operations from attorney approval and blocking invoice sending, write-downs, write-offs, trust disbursements, payment plans, collections escalation, or ledger mutations without authorization.

## 3. Production Issues
- Original prompt spans time capture, billing narratives, invoice generation, collections, trust accounting, write-offs, and payment plans in one role.
- Legal billing errors can create ethical violations, client disputes, trust-account/IOLTA violations, overbilling, and bar discipline risk.
- Overlaps finance controller/bookkeeper, legal operations, accounts receivable, practice management admins, and responsible attorneys.

## 4. Token Waste
- Billing standards should be generated from fee agreement, rate card, billing guidelines, and matter ledger.
- Trust-account content needs separate authority gates.

## 5. Ambiguity Risks
- 'Maximize revenue recovery' can conflict with ethical billing constraints.
- Draft billing narratives, invoice sends, and trust movements are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split billing draft/review from invoice/trust/collections execution with fee agreement, billing guidelines, matter ledger, trust policy, attorney approval, immutable audit logs, no unilateral write-offs, no client-fund movement, and no silent ledger mutation.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 4
- Maintainability: 3
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.4/10


---

# Agent Review: Healthcare Customer Service

Source: `specialized/healthcare-customer-service.md`

## 1. Current Function
Healthcare customer service specialist for patient support triage, appointment/billing/insurance routing, complaint intake, emergency recognition, identity verification, HIPAA-aware responses, and escalation handoffs.

## 2. Current Role Boundary
Provide empathetic, HIPAA-aware patient support triage, routing, and administrative guidance within verified identity, minimum-necessary PHI, emergency, clinical-escalation, billing, insurance, callback, and documentation boundaries without diagnosing, interpreting results, recommending treatment, or disclosing PHI to unauthorized parties.

## 3. Production Issues
- Live patient support can encounter emergencies, self-harm, clinical questions, PHI, billing distress, insurance denials, and identity-verification failures.
- Original prompt includes broad support workflows and memory of patient details without enough explicit data-minimization and verification gates.
- Overlaps customer service, billing support, insurance specialists, nurse triage, patient advocates, risk/compliance, and clinical staff.

## 4. Token Waste
- Long scripts should be selected by inquiry type and verification state.
- Memory language should become explicit minimum-necessary state fields.

## 5. Ambiguity Risks
- 'Clinical Questions' routing can drift into advice if blocked-state rules are weak.
- Appointment/billing/account actions depend on identity verification and tool permission.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with no clinical advice, emergency/988 escalation, HIPAA minimum-necessary, identity/proxy verification, no unauthorized PHI, clinical routing, appointment/billing permission gates, and documented callback/handoff commitments.

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
- Orchestration Fit: 3

Final Rating: 4.0/10


---

# Agent Review: Healthcare Marketing Compliance Specialist

Source: `specialized/healthcare-marketing-compliance.md`

## 1. Current Function
Healthcare marketing compliance support specialist for China healthcare advertising risk review, claim checks, content modifications, certificate checks, platform-rule handoffs, privacy/PIPL routing, and legal/compliance approval packets.

## 2. Current Role Boundary
Review healthcare marketing content for China-focused regulatory, platform, privacy, claim, and approval risks using current official sources and counsel/compliance review, without issuing legal opinions, publishing/taking down content, changing accounts, or approving regulated medical/pharma/device claims alone.

## 3. Production Issues
- Original prompt is extremely broad, current-law dependent, and jurisdiction-specific, with detailed regulatory assertions that can become stale.
- Healthcare marketing content can create legal, patient privacy, PIPL, medical advertising, prescription drug, device, supplement, medical aesthetics, and platform enforcement risk.
- Overlaps legal reviewer, privacy reviewer, China market/localization, content creator, paid media, platform operators, brand guardian, and healthcare subject-matter experts.

## 4. Token Waste
- Long regulation catalog should be replaced with current-source review requirements and blocked states.
- Compliance advice needs official citations and counsel approval rather than memorized claims.

## 5. Ambiguity Risks
- 'Keeps marketing legal' can sound like a legal opinion.
- Review, modify, approve, publish, and takedown authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite with current official-source requirements, China jurisdiction/product-category gates, no legal opinion, approval certificate checks, prescription/device/aesthetic red lines, PIPL/patient-story consent, source staleness blocks, no publish/takedown authority, and counsel approval gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 3
- Maintainability: 3
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.2/10
