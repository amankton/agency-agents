# Batch Summary: batch_015

## Agents Reviewed
- `marketing/marketing-pr-communications-manager.md`: PR & Communications Manager (rewrite)
- `specialized/hr-onboarding.md`: HR Onboarding (refactor)
- `specialized/business-strategist.md`: Business Strategist (refactor)
- `specialized/change-management-consultant.md`: Change Management Consultant (refactor)
- `specialized/supply-chain-strategist.md`: Supply Chain Strategist (rewrite)
- `sales/sales-engineer.md`: Sales Engineer (refactor)
- `sales/sales-coach.md`: Sales Coach (refactor)
- `marketing/marketing-global-podcast-strategist.md`: Global Podcast Strategist (refactor)
- `marketing/marketing-podcast-strategist.md`: Podcast Strategist (refactor)
- `integrations/mcp-memory/backend-architect-with-memory.md`: Backend Architect (deprecate)

## Recommended Actions
- Keep: 0
- Refactor: 7
- Merge: 0
- Split: 0
- Deprecate: 1
- Rewrite: 2

## Highest-Risk Agent
PR & Communications Manager: it can affect public crisis statements, legal/regulatory exposure, employee/internal communications, journalist relationships, incident disclosure, executive positioning, and brand reputation. Supply Chain Strategist is the operational runner-up because supplier outreach, contracts, POs, quality, trade, logistics, inventory, and ERP/SRM actions can create direct financial and compliance exposure.

## Biggest Architecture Issue Found
Several remaining high-priority agents were not dangerous because they run code; they were dangerous because they imply authority. Batch 015 adds explicit owner gates for executive strategy, HR onboarding, change adoption, public communications, procurement, sales evaluation, coaching data, podcast publishing, and cross-session memory so advisory work stays advisory until the accountable owner approves action.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_015.md`
- `agency-audit/refactored-agents/marketing-pr-communications-manager.md`
- `agency-audit/refactored-agents/hr-onboarding.md`
- `agency-audit/refactored-agents/business-strategist.md`
- `agency-audit/refactored-agents/change-management-consultant.md`
- `agency-audit/refactored-agents/supply-chain-strategist.md`
- `agency-audit/refactored-agents/sales-engineer.md`
- `agency-audit/refactored-agents/sales-coach.md`
- `agency-audit/refactored-agents/marketing-global-podcast-strategist.md`
- `agency-audit/refactored-agents/marketing-podcast-strategist.md`
- `agency-audit/refactored-agents/backend-architect-with-memory.md`
- `agency-audit/acceptance-tests/marketing-pr-communications-manager.tests.md`
- `agency-audit/acceptance-tests/hr-onboarding.tests.md`
- `agency-audit/acceptance-tests/business-strategist.tests.md`
- `agency-audit/acceptance-tests/change-management-consultant.tests.md`
- `agency-audit/acceptance-tests/supply-chain-strategist.tests.md`
- `agency-audit/acceptance-tests/sales-engineer.tests.md`
- `agency-audit/acceptance-tests/sales-coach.tests.md`
- `agency-audit/acceptance-tests/marketing-global-podcast-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-podcast-strategist.tests.md`
- `agency-audit/acceptance-tests/backend-architect-with-memory.tests.md`

## Subagent Inputs Used
- Enterprise advisory scan: refactor HR Onboarding, Business Strategist, and Change Management Consultant around privacy, legal, sponsor, and system-authority gates; rewrite PR & Communications Manager and Supply Chain Strategist around live public/procurement action risk.
- Sales, podcast, and memory scan: refactor Sales Engineer and Sales Coach around approved claims, POC/customer-environment authority, rep/customer privacy, and CRM/personnel boundaries; split podcast strategy into global base plus China extension; deprecate Backend Architect with Memory into governed memory extension.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: PR & Communications Manager

Source: `marketing/marketing-pr-communications-manager.md`

## 1. Current Function
Reputation and communications strategy specialist for message architecture, media materials, crisis drafts, executive thought-leadership briefs, internal communications, and communications measurement handoffs.

## 2. Current Role Boundary
Produce draft-only PR, media-relations, executive-communications, internal-communications, award, launch, and crisis-message artifacts from verified facts, audience scope, and approval context while blocking live publication, journalist outreach, crisis statements, investor/regulatory claims, breach communications, or spokesperson commitments without legal and executive approval.

## 3. Production Issues
- Original prompt strongly implies live crisis response, journalist outreach, embargo management, newswire distribution, analyst relations, and narrative control without explicit approval gates.
- PR outputs can affect legal exposure, securities/regulatory claims, incident response, employee trust, customer commitments, and public reputation.
- Overlaps Brand Guardian, Content Creator, Social Media Strategist, Multi-Platform Publisher, Incident Response, Legal, Executive Leadership, Support, and Investor Relations.

## 4. Token Waste
- Full press, crisis, internal, awards, and thought-leadership playbooks should be selected by mode.
- Static media and crisis rules should be replaced with fact, approval, and channel gates.

## 5. Ambiguity Risks
- 'Crisis communications' can mean draft support, legal-approved release, media response, or internal announcement.
- Drafting, approval, spokesperson authority, journalist outreach, and live publication are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as a draft-only reputation and message-architecture role with verified fact gates, legal/executive review, explicit channel authority, and publisher/spokesperson handoffs.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: HR Onboarding

Source: `specialized/hr-onboarding.md`

## 1. Current Function
HR onboarding coordination specialist for pre-boarding, first-day schedules, 30-60-90 plans, checklist management, manager/buddy guidance, and HR/IT/benefits handoffs.

## 2. Current Role Boundary
Produce onboarding checklists, schedules, new-hire communications, manager guides, milestone plans, and compliance-tracking drafts from approved HR policy and employee context while blocking employee-data disclosure, I-9/legal/benefits determinations, accommodation handling, background checks, payroll/benefits actions, IT provisioning, or HRIS mutation without authorized owners.

## 3. Production Issues
- Original prompt spans employee PII, benefits, tax forms, I-9, accommodations, payroll, IT provisioning, policy acknowledgments, and HRIS records without authority gates.
- Onboarding workflows carry privacy, employment-law, benefits, payroll, accessibility/accommodation, and identity-verification exposure.
- Overlaps Recruitment Specialist, HR Operations, Benefits Admin, Payroll, Employment Counsel, Privacy, IT Admin, and Manager responsibilities.

## 4. Token Waste
- Full day-one, first-week, 30-60-90, benefits, compliance, and culture templates should be generated by mode.
- Legal/compliance checklists should require jurisdiction and approved policy context.

## 5. Ambiguity Risks
- 'Manage onboarding' can imply drafting plans or mutating HRIS/payroll/IT systems.
- Compliance tracking, legal determinations, employee support, and manager coaching are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into a privacy-first onboarding coordinator with jurisdiction/policy gates, employee-data minimization, and explicit HRIS/IT/payroll/benefits handoffs.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Business Strategist

Source: `specialized/business-strategist.md`

## 1. Current Function
Business strategy decision-support specialist for competitive, market, growth, business-model, operating-model, and scenario-analysis artifacts.

## 2. Current Role Boundary
Produce strategic option framing, competitive analysis, market-entry assessment, business-model review, scenario analysis, and decision-support artifacts from supplied business context and source evidence while blocking executive decisions, capital allocation, M&A, hiring, pricing, regulated claims, or financial/legal advice without accountable owners.

## 3. Production Issues
- Original prompt uses strong management-consulting authority and can sound like it owns strategic decisions rather than producing decision support.
- Strategy recommendations can imply capital allocation, market claims, financial projections, M&A rationale, layoffs/headcount, pricing, or regulated-industry advice.
- Overlaps Product Manager, FP&A Analyst, Financial Analyst, Pricing Analyst, Legal/Compliance, Market Research, Executive Sponsor, and Operations roles.

## 4. Token Waste
- Full framework catalogs should be selected by strategic question.
- Market sizing, Five Forces, business-model, and OKR templates should not all appear unless requested.

## 5. Ambiguity Risks
- 'Actionable strategy' can mean analysis, recommendation, board memo, operating plan, or decision approval.
- Market research, financial modeling, legal/regulatory review, and executive decision rights are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as evidence-backed decision support with explicit decision rights, source confidence, scenario ranges, and specialist review before high-stakes commitments.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Change Management Consultant

Source: `specialized/change-management-consultant.md`

## 1. Current Function
Change-management planning specialist for organizational adoption, stakeholder engagement, sponsor alignment, communication planning, training readiness, resistance analysis, and sustainment handoffs.

## 2. Current Role Boundary
Produce change-impact assessments, readiness artifacts, stakeholder maps, communications/training plans, adoption metrics, and sustainment recommendations from supplied change context while blocking employee surveillance, discipline, labor/legal conclusions, HRIS actions, survey collection, live announcements, or commitments without sponsor, HR, legal, and communications approval.

## 3. Production Issues
- Original prompt presents ADKAR/Kotter/Prosci guidance but lacks hard boundaries for employee privacy, labor relations, legal review, announcements, and data collection.
- Change programs often touch restructuring, M&A, layoffs, performance management, union/labor topics, sensitive survey data, and employee communications.
- Overlaps HR Onboarding, Internal Communications, Project Manager, Product Manager, Training, Employment Counsel, Privacy, and Executive Sponsors.

## 4. Token Waste
- Framework explanations should be selected by change type and maturity.
- Full lifecycle templates should be mode-specific.

## 5. Ambiguity Risks
- 'Manage resistance' can imply coaching, planning, surveillance, discipline, or labor relations.
- Drafting communications, sending announcements, training delivery, and adoption measurement are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around sponsor authority, employee privacy, labor/legal review, communications approval, and draft-only adoption artifacts.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Supply Chain Strategist

Source: `specialized/supply-chain-strategist.md`

## 1. Current Function
Supply-chain and procurement strategy advisor for category analysis, supplier qualification planning, risk assessment, quality handoffs, inventory/logistics scenarios, and China manufacturing ecosystem research.

## 2. Current Role Boundary
Produce read-only supply-chain strategy, sourcing, supplier-risk, quality, inventory, logistics, and digitalization advisory artifacts from authorized supplier/category data while blocking supplier outreach, tenders, contracts, purchase orders, inventory/logistics changes, ERP/SRM mutation, hedging, customs/trade determinations, or regulated compliance claims without accountable owners.

## 3. Production Issues
- Original prompt is hands-on and includes procurement platforms, supplier qualification, negotiation, QC, inventory formulas, and ERP/digitalization without authority boundaries.
- Supply-chain recommendations can trigger supplier selection, contracts, import/export, product quality, payments, production schedules, inventory, logistics, sanctions, and customs compliance risk.
- Overlaps Procurement, Legal, Finance, Trade Compliance, Quality, ERP/SRM Admins, Operations, Manufacturing, and Data/Analytics roles.

## 4. Token Waste
- China platform catalogs, quality methods, inventory formulas, and ERP guidance should be generated only for the declared category and mode.
- Static platform and compliance claims need source dates.

## 5. Ambiguity Risks
- 'Find optimal suppliers' can mean research, shortlist, outreach, tender, negotiation, or contract award.
- Advisory analysis, procurement execution, compliance review, ERP action, and logistics changes are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as a read-only strategic sourcing and supply-risk advisor with category/source gates, compliance review, and explicit no-mutation procurement boundaries.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Sales Engineer

Source: `sales/sales-engineer.md`

## 1. Current Function
Pre-sales technical evaluation specialist for buyer discovery, tailored demo design, POC scoping, competitive technical positioning, solution-fit analysis, and technical-close handoffs.

## 2. Current Role Boundary
Produce technical discovery, demo strategy, POC scope, solution-architecture, objection-handling, and competitive technical evaluation artifacts from approved opportunity context while blocking customer-environment mutation, unsupported product/security claims, prospect/customer PII misuse, live POC execution, roadmap commitments, or CRM changes without account and technical owner approval.

## 3. Production Issues
- Original prompt is well scoped to pre-sales but implies POC execution and technical claims that require product, security, legal, and customer-environment authority.
- Sales engineering work touches prospect/customer PII, security architecture, integrations, benchmarks, roadmap commitments, competitive claims, and buyer trust.
- Overlaps Deal Strategist, Proposal Strategist, Backend Architect, Security Architect, Product, Account Executive, Legal, and Customer Engineering.

## 4. Token Waste
- Discovery, demo, POC, battlecard, and objection templates should be generated by deal stage.
- Competitive positioning should use supplied facts and approved claims only.

## 5. Ambiguity Risks
- 'POC execution' can mean scoping document, sandbox setup, customer environment work, or technical close.
- Product capability claims, security assurances, pricing/commercial commitments, and engineering implementation are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as the technical-evaluation and POC-spec owner with approved-claim gates, privacy controls, no customer-environment mutation, and product/security handoffs.

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
- Orchestration Fit: 5

Final Rating: 5.0/10


---

# Agent Review: Sales Coach

Source: `sales/sales-coach.md`

## 1. Current Function
Sales coaching support specialist for rep development, behavioral feedback, call review, pipeline coaching, deal prep, forecast discipline, and sales-manager handoffs.

## 2. Current Role Boundary
Produce sales coaching plans, call-feedback summaries, pipeline-review prompts, deal-coaching artifacts, and forecast-discipline recommendations from authorized rep and deal evidence while blocking personnel decisions, compensation/performance management, CRM edits, forecast approval, call-recording misuse, or persistent memory of rep/customer data without consent and manager authority.

## 3. Production Issues
- Original prompt uses manager-like authority over rep performance, forecast discipline, call recordings, and coaching memory without HR/privacy/manager boundaries.
- Sales coaching can expose employee performance data, customer/prospect data, call recordings, compensation, personnel decisions, and CRM/forecast controls.
- Overlaps Sales Leader, Pipeline Analyst, Deal Strategist, RevOps, HR/Legal, Account Executive, and Customer Success roles.

## 4. Token Waste
- Rep plan, call review, pipeline review, deal prep, and forecast artifacts should be generated by mode.
- Framework and benchmark claims should be concise and source-backed when used.

## 5. Ambiguity Risks
- 'Coach the rep' can mean private feedback, manager performance action, deal strategy, CRM hygiene, or forecast approval.
- Behavior feedback, personnel decisions, call recording access, and persistent memory are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as coaching-plan and behavior-feedback support with rep/customer privacy, consent, manager authority, and no CRM/personnel mutation.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Global Podcast Strategist

Source: `marketing/marketing-global-podcast-strategist.md`

## 1. Current Function
Canonical podcast strategy specialist for show positioning, audience development, episode systems, discoverability, community growth, analytics interpretation, and monetization planning.

## 2. Current Role Boundary
Produce platform-neutral podcast positioning, content strategy, growth, analytics, guest, community, and monetization artifacts from supplied show context while blocking guest outreach, uploads, publishing, sponsorship commitments, ad insertion, account changes, rights violations, or unsupported platform-algorithm claims without owner approval.

## 3. Production Issues
- Original prompt is a strong global podcast strategy base but mixes strategy with outreach, sponsorship, platform optimization, and account-level tactics without approval gates.
- Podcast work touches guest consent, copyright/music/clip rights, platform accounts, sponsorship disclosures, audience data, monetization, and stale platform-algorithm claims.
- Overlaps regional Podcast Strategist, Content Creator, Social Media Strategist, Multi-Platform Publisher, Paid Media, Brand, Legal, and Analytics roles.

## 4. Token Waste
- Show bible, content calendar, outreach, analytics, and monetization templates should be selected by mode.
- Platform algorithm guidance needs source dates and caveats.

## 5. Ambiguity Risks
- 'Grow a podcast' can mean strategy, guest outreach, clip production, account publishing, sponsorship sales, or paid amplification.
- Global base strategy and China-specific platform guidance are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as the canonical global podcast strategy base with source-dated platform guidance, rights/consent gates, and explicit regional/publishing/monetization handoffs.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Podcast Strategist

Source: `marketing/marketing-podcast-strategist.md`

## 1. Current Function
China podcast strategy extension for Xiaoyuzhou, Ximalaya, and related Chinese audio-platform positioning, production standards, distribution planning, community growth, and monetization handoffs.

## 2. Current Role Boundary
Produce China-market podcast positioning, platform, production, distribution, community, monetization, and analytics advisory artifacts from supplied show and market context while blocking uploads, guest contact, private-domain migration, ecommerce, sponsorship execution, platform account changes, sensitive-topic publication, or unsupported current China-platform claims without approval.

## 3. Production Issues
- Original prompt overlaps heavily with Global Podcast Strategist while adding China-specific platform, community, private-domain, ecommerce, and monetization operations.
- China podcast operations involve platform terms, PIPL/private-domain data, guest consent, regulated topics, advertising disclosure, ecommerce/affiliate links, and live account actions.
- Overlaps Global Podcast Strategist, China Market Localization, WeChat OA, Private Domain Operator, Content Creator, Multi-Platform Publisher, Legal/Compliance, and Brand.

## 4. Token Waste
- China platform catalogs, equipment guidance, production workflow, community growth, and monetization should be selected by mode.
- Current platform feature claims need source dates.

## 5. Ambiguity Risks
- 'Operations' can imply strategy, episode planning, upload, manual distribution, community management, or monetization execution.
- Global podcast base and China regional extension are not clearly split.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as the China/regional podcast extension with current-source platform gates, PIPL/content constraints, rights review, and no live publishing or community/account mutation.

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

# Agent Review: Backend Architect

Source: `integrations/mcp-memory/backend-architect-with-memory.md`

## 1. Current Function
Legacy backend-architecture variant with appended memory behavior; should be migrated to canonical backend architecture plus Memory/State Service policy.

## 2. Current Role Boundary
Deprecate the standalone memory-backed Backend Architect duplicate in favor of the canonical Backend Architect plus a governed optional memory/state extension that stores only approved architecture decisions, constraints, and handoff summaries while blocking secrets, PII, raw customer data, hidden reasoning, stale assumptions, or unapproved cross-session persistence.

## 3. Production Issues
- The prompt duplicates Backend Architect responsibilities and adds memory semantics without a data classification, retention, staleness, or deletion policy.
- Backend architecture memory can accidentally persist secrets, credentials, customer data, architecture vulnerabilities, PII, or outdated design assumptions across sessions.
- Overlaps canonical Backend Architect, Software Architect, Data Engineer, Security Architect, MCP Builder, and Memory/State Service.

## 4. Token Waste
- Backend architecture content is duplicated from the canonical agent.
- Memory guidance should be a reusable governed extension, not repeated inside a role prompt.

## 5. Ambiguity Risks
- 'Memory' can mean project facts, approved decisions, user preferences, raw logs, code snippets, or hidden reasoning.
- State ownership, retention, deletion, and stale-memory invalidation are not defined.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Deprecate the duplicate and migrate memory behavior into a governed optional extension with data classification, retention, deletion, staleness, and no-secrets/no-PII rules.

## 8. Merge / Split / Deprecate Recommendation
Decision: deprecate

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
