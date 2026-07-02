# Batch Summary: batch_020

## Agents Reviewed
- `game-development/unity/unity-editor-tool-developer.md`: Unity Editor Tool Developer (refactor)
- `game-development/unity/unity-multiplayer-engineer.md`: Unity Multiplayer Engineer (refactor)
- `game-development/roblox-studio/roblox-systems-scripter.md`: Roblox Systems Scripter (refactor)
- `game-development/roblox-studio/roblox-avatar-creator.md`: Roblox Avatar Creator (refactor)
- `game-development/roblox-studio/roblox-experience-designer.md`: Roblox Experience Designer (refactor)
- `support/support-legal-compliance-checker.md`: Legal Compliance Checker (split)
- `testing/testing-workflow-optimizer.md`: Workflow Optimizer (merge)
- `support/support-infrastructure-maintainer.md`: Infrastructure Maintainer (merge)
- `support/support-analytics-reporter.md`: Analytics Reporter (refactor)
- `support/support-finance-tracker.md`: Finance Tracker (merge)

## Recommended Actions
- Keep: 0
- Refactor: 6
- Merge: 3
- Split: 1
- Deprecate: 0
- Rewrite: 0

## Highest-Risk Agent
Legal Compliance Checker: the original prompt can drift into legal advice, compliance certification, stale regulatory claims, contract/policy approval, filing, and customer or regulator communications without licensed review. Infrastructure Maintainer and Finance Tracker are close runners-up because they touch production infrastructure and money controls.

## Biggest Architecture Issue Found
Batch 020 exposes a support-operations tail where several prompts are duplicate operator roles instead of canonical owners. Workflow, infrastructure, and finance tracking should merge into existing Workflow Architect, SRE/DevOps, and finance clusters, while analytics and Unity/Roblox roles need tighter data, editor, backend, marketplace, publishing, and no-live-mutation gates.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_020.md`
- `agency-audit/refactored-agents/unity-editor-tool-developer.md`
- `agency-audit/refactored-agents/unity-multiplayer-engineer.md`
- `agency-audit/refactored-agents/roblox-systems-scripter.md`
- `agency-audit/refactored-agents/roblox-avatar-creator.md`
- `agency-audit/refactored-agents/roblox-experience-designer.md`
- `agency-audit/refactored-agents/support-legal-compliance-checker.md`
- `agency-audit/refactored-agents/testing-workflow-optimizer.md`
- `agency-audit/refactored-agents/support-infrastructure-maintainer.md`
- `agency-audit/refactored-agents/support-analytics-reporter.md`
- `agency-audit/refactored-agents/support-finance-tracker.md`
- `agency-audit/acceptance-tests/unity-editor-tool-developer.tests.md`
- `agency-audit/acceptance-tests/unity-multiplayer-engineer.tests.md`
- `agency-audit/acceptance-tests/roblox-systems-scripter.tests.md`
- `agency-audit/acceptance-tests/roblox-avatar-creator.tests.md`
- `agency-audit/acceptance-tests/roblox-experience-designer.tests.md`
- `agency-audit/acceptance-tests/support-legal-compliance-checker.tests.md`
- `agency-audit/acceptance-tests/testing-workflow-optimizer.tests.md`
- `agency-audit/acceptance-tests/support-infrastructure-maintainer.tests.md`
- `agency-audit/acceptance-tests/support-analytics-reporter.tests.md`
- `agency-audit/acceptance-tests/support-finance-tracker.tests.md`

## Subagent Inputs Used
- Game and Roblox scan: refactored Unity editor/multiplayer and Roblox systems/avatar/experience roles around engine/platform source evidence, assets, DataStores, backend services, marketplace rules, minors, monetization, publish authority, and rollback.
- Support and testing scan: split Legal Compliance Checker, merged Workflow Optimizer, Infrastructure Maintainer, and Finance Tracker into canonical clusters, and refactored Analytics Reporter as the BI analysis role with lineage, privacy, metric, and send gates.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Unity Editor Tool Developer

Source: `game-development/unity/unity-editor-tool-developer.md`

## 1. Current Function
Unity editor-automation specialist for EditorWindows, PropertyDrawers, AssetPostprocessors, ScriptedImporters, validators, pipeline tooling, and artist/developer workflow handoffs.

## 2. Current Role Boundary
Produce Unity Editor tool specs, scoped editor-extension code plans, validation checklists, and pipeline-automation handoffs from approved Unity project evidence while blocking destructive AssetPostprocessor behavior, build-blocking validators, asset mutation, source-control commits, or runtime API leakage without owner approval.

## 3. Production Issues
- Original prompt provides useful editor tooling rules but lacks project/version, asmdef/runtime separation, asset mutation, source-control, and rollback gates.
- Editor tools can silently mutate assets, block builds, corrupt imports, leak UnityEditor APIs into runtime assemblies, or confuse artists with unsafe UI.
- Overlaps Unity Architect, Technical Artist, Build Engineer, Code Reviewer, QA Owner, and Workflow Optimizer.

## 4. Token Waste
- EditorWindow, PropertyDrawer, AssetPostprocessor, and validation templates should be generated by mode.
- Code examples should require Unity version and repo context.

## 5. Ambiguity Risks
- 'Build editor tool' can mean spec, local prototype, asset processor, build validator, source-control change, or production pipeline automation.
- Tool design, asset mutation, build gating, and release authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as a version-gated editor-tool spec and implementation agent with explicit asset/build/source-control mutation approval.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.4/10


---

# Agent Review: Unity Multiplayer Engineer

Source: `game-development/unity/unity-multiplayer-engineer.md`

## 1. Current Function
Unity multiplayer networking specialist for Netcode for GameObjects, Unity Gaming Services Relay/Lobby, authority models, state sync, prediction, latency testing, and security handoffs.

## 2. Current Role Boundary
Produce Unity multiplayer architecture, NGO/UGS integration specs, authority-model reviews, latency-test plans, security findings, and backend handoffs from approved project evidence while blocking live backend changes, Relay/Lobby credential use, server deployment, anticheat conclusions, or production networking code mutation without owner approval.

## 3. Production Issues
- Original prompt includes version-sensitive NGO/UGS guidance, Relay/Lobby setup, prediction/reconciliation, and anti-cheat claims without validation and deploy gates.
- Unity multiplayer work can touch backend credentials, server deployment, matchmaking, player data, cheat surfaces, and live network reliability.
- Overlaps Unity Architect, Gameplay Engineer, AppSec, SRE/DevOps, Performance Benchmarker, QA, and Release Manager.

## 4. Token Waste
- NGO, UGS, prediction, and authority guidance should be mode-specific.
- Code snippets should require Unity/NGO/UGS versions and project topology.

## 5. Ambiguity Risks
- 'Build multiplayer' can mean architecture, code, Relay/Lobby setup, latency test, backend deploy, security review, or production release.
- Architecture, implementation, backend credentials, and release authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around source-dated networking guidance, security review, simulated-latency evidence, and no live backend/server mutation by default.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 6

Final Rating: 5.4/10


---

# Agent Review: Roblox Systems Scripter

Source: `game-development/roblox-studio/roblox-systems-scripter.md`

## 1. Current Function
Roblox platform systems specialist for Luau architecture, server-authoritative game logic, RemoteEvent/RemoteFunction validation, DataStore safety, module organization, and platform QA handoffs.

## 2. Current Role Boundary
Produce governed Roblox Luau system specs, RemoteEvent security reviews, DataStore migration plans, ModuleScript architecture, and Studio test handoffs from approved place evidence while blocking live place publishing, DataStore mutation, exploitable remotes, economy/currency changes, or player-data handling without owner approval.

## 3. Production Issues
- Original prompt has strong Roblox security guidance but assumes implementation authority for RemoteEvents, DataStores, and module architecture.
- Roblox systems work can expose exploitable remotes, lose player data, exceed DataStore limits, mutate economies, or publish live place changes.
- Overlaps Roblox Experience Designer, AppSec, Data/Analytics, QA, Product/Game Designer, and live-ops owners.

## 4. Token Waste
- RemoteEvent, DataStore, and ModuleScript templates should be generated by task.
- Full code examples should require place/module context.

## 5. Ambiguity Risks
- 'Script Roblox systems' can mean architecture, code snippet, Studio edit, DataStore migration, live publish, or economy change.
- Design, code, data persistence, and publish authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into governed Luau systems support with RemoteEvent/DataStore gates and publish/data mutation approvals.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.4/10


---

# Agent Review: Roblox Avatar Creator

Source: `game-development/roblox-studio/roblox-avatar-creator.md`

## 1. Current Function
Roblox UGC/avatar pipeline specialist for accessory/clothing specs, rigging/cage checks, texture standards, body-type compatibility, moderation readiness, and marketplace handoffs.

## 2. Current Role Boundary
Produce Roblox avatar and UGC pipeline specs, asset QA checklists, rig/cage/body-test plans, marketplace-readiness notes, and in-experience avatar-system handoffs from approved assets while blocking public Marketplace submission, pricing, copyrighted content, commercial claims, or live asset publishing without rights and owner approval.

## 3. Production Issues
- Original prompt includes current UGC limits, marketplace submission prep, avatar customization systems, and business considerations without source-date and rights gates.
- Avatar work can violate IP, fail moderation, break body compatibility, create commercial marketplace exposure, or mutate live avatar systems.
- Overlaps Technical Artist/DCC Artist, Roblox Systems Scripter, Art Director, Legal/IP Reviewer, Marketplace Owner, and QA.

## 4. Token Waste
- UGC specs, rigging, clothing, and marketplace checklists should be selected by item type.
- Current Roblox limits require source-date validation.

## 5. Ambiguity Risks
- 'Create avatar item' can mean concept, DCC asset QA, rigging guidance, in-experience system, marketplace submission, pricing, or publication.
- Asset creation, technical QA, rights clearance, and commercial submission are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as Roblox UGC/avatar pipeline specialist with current official specs, rights, body-test, pricing, and submission gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.4/10


---

# Agent Review: Roblox Experience Designer

Source: `game-development/roblox-studio/roblox-experience-designer.md`

## 1. Current Function
Roblox experience product-design specialist for core loops, onboarding, progression, ethical monetization, social mechanics, discovery readiness, and implementation handoffs.

## 2. Current Role Boundary
Produce Roblox experience design specs, onboarding, retention-loop, monetization, progression, social-feature, and analytics plans from approved player and policy context while blocking dark patterns, child-targeted pressure, pay-to-win drift, DataStore/economy mutation, live publishing, or unsupported retention/revenue guarantees.

## 3. Production Issues
- Original prompt combines Roblox UX/product design with monetization systems, DataStore progression, marketplace mechanics, and implementation patterns.
- Roblox audiences often include minors, so monetization, scarcity, ads, analytics, and social loops need child-safety, platform-policy, and privacy controls.
- Overlaps Game Designer, Product Manager, Roblox Systems Scripter, Legal/Compliance, Analytics Reporter, QA, and Live Ops.

## 4. Token Waste
- Game Pass, Developer Product, Daily Reward, and SEO templates should be selected by design scope.
- Policy/pricing claims require current-source validation.

## 5. Ambiguity Risks
- 'Design Roblox experience' can mean concept, monetization design, Luau implementation, DataStore schema, live ops, analytics, or publication.
- Design specs, implementation, monetization approval, and live publishing are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as design/spec role for Roblox loops, onboarding, monetization, and metrics, routing implementation and live ops elsewhere.

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

# Agent Review: Legal Compliance Checker

Source: `support/support-legal-compliance-checker.md`

## 1. Current Function
Legal/compliance issue-spotting and routing specialist for privacy, security, content, operational, and regulatory control mapping with licensed-review handoffs.

## 2. Current Role Boundary
Split Legal Compliance Checker into compliance issue-spotting, current-source control mapping, policy draft, and routing modes that produce draft risk artifacts while blocking legal advice, compliance certification, policy approval, contract changes, regulatory filings, or customer/legal communications without licensed counsel or compliance owner review.

## 3. Production Issues
- Original prompt broadly claims legal and compliance expertise across GDPR, CCPA, HIPAA, SOX, PCI-DSS, contracts, privacy policies, and incident procedures.
- Compliance checking can become unauthorized legal advice, stale regulatory claims, false certification, privacy mishandling, or contract/policy mutation.
- Overlaps Legal Document Review, Security Compliance Auditor, Healthcare Marketing Compliance, Tax Strategist, external counsel, and compliance owners.

## 4. Token Waste
- Framework-specific compliance templates should be generated only for declared jurisdiction/framework.
- Regulatory citations require current sources and source dates.

## 5. Ambiguity Risks
- 'Check compliance' can mean issue spotting, legal opinion, policy drafting, control implementation, certification, regulatory filing, or contract review.
- Advisory drafts, licensed legal conclusions, and system/policy changes are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split into legal/compliance issue-spotting and routing with draft-only artifacts and licensed review for opinions, contracts, filings, and certification.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 3.8/10


---

# Agent Review: Workflow Optimizer

Source: `testing/testing-workflow-optimizer.md`

## 1. Current Function
Legacy process-optimization specialist whose useful functions should become Workflow Architect optimization mode with Change Management and Automation Governance handoffs.

## 2. Current Role Boundary
Merge Workflow Optimizer into Workflow Architect as a data-driven optimization mode that produces current-state maps, bottleneck analyses, automation candidates, and business-case drafts while blocking live workflow/system mutation, automation implementation, staffing changes, or ROI claims without process owner and change-management approval.

## 3. Production Issues
- Original prompt duplicates Workflow Architect, Change Management, Automation Governance, Tool Evaluator, Jira Workflow Steward, Analytics, and Finance roles.
- Workflow optimization can over-automate, mutate live processes, disrupt teams, mishandle employee/customer data, or overstate ROI.
- Process changes require baseline evidence, affected-user context, process owner approval, and change-management planning.

## 4. Token Waste
- Large optimization-framework code examples should be replaced by concise process artifacts.
- Automation recommendations should be mode-specific and evidence-backed.

## 5. Ambiguity Risks
- 'Optimize workflow' can mean analysis, future-state design, automation implementation, tool purchase, staffing change, or system mutation.
- Business-case drafting, automation build, and operational change authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Merge as data-driven optimization mode under Workflow Architect, producing specs and business cases without implementing automation.

## 8. Merge / Split / Deprecate Recommendation
Decision: merge

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.0/10


---

# Agent Review: Infrastructure Maintainer

Source: `support/support-infrastructure-maintainer.md`

## 1. Current Function
Legacy infrastructure maintenance specialist whose planning functions should route to SRE, DevOps Automator, Cloud Security Architect, Incident Response, and service owners.

## 2. Current Role Boundary
Merge Infrastructure Maintainer into SRE as infrastructure health and maintenance planning that produces read-only reliability, monitoring, backup/DR, cost, security, and change-plan artifacts while blocking production mutation, IaC applies, secret access, patching, backup deletion, or incident command without service-owner and DevOps approval.

## 3. Production Issues
- Original prompt duplicates SRE, DevOps Automator, Cloud Security Architect, Incident Responder, Database Optimizer, and Compliance Auditor while implying production operations.
- Infrastructure maintenance can mutate production systems, expose secrets, apply Terraform/cloud changes, alter monitoring, delete backups, or affect uptime.
- Production infrastructure requires SLO evidence, IaC source-of-truth, change/rollback policy, security constraints, backup/DR validation, and accountable owner approval.

## 4. Token Waste
- Terraform/Prometheus examples should be removed from generic prompt unless requested.
- Infrastructure domain detail should be selected by SRE/DevOps task.

## 5. Ambiguity Risks
- 'Maintain infrastructure' can mean read-only health review, SRE planning, IaC changes, patching, incident command, cost changes, or production deploy.
- Planning, implementation, incident command, and compliance authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Merge into SRE as infrastructure health and maintenance planning, with implementation routed to DevOps under explicit approval.

## 8. Merge / Split / Deprecate Recommendation
Decision: merge

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 3.8/10


---

# Agent Review: Analytics Reporter

Source: `support/support-analytics-reporter.md`

## 1. Current Function
Business intelligence analysis specialist for metrics, dashboards, segmentation, statistical summaries, KPI reporting, data quality, and executive-summary handoffs.

## 2. Current Role Boundary
Produce BI analysis, metric definitions, data-quality findings, dashboard specs, statistical summaries, and decision-support reports from approved source data while blocking PII disclosure, unsupported causal/statistical claims, dashboard mutation, automated reporting sends, or strategic commitments without data owner approval.

## 3. Production Issues
- Original prompt includes dashboards, statistical models, predictive models, automated reporting, and strategic recommendations without data lineage and publication gates.
- Analytics reporting can leak PII, create metric drift, overstate causality, mutate dashboards, or send stale reports to stakeholders.
- Overlaps Data Engineer, Data Consolidation Agent, Finance/FP&A, Product Manager, Marketing/Growth, Executive Summary Generator, and Evidence Collector.

## 4. Token Waste
- SQL/Python/dashboard examples should be selected by analysis scope and data source.
- Predictive modeling should require sufficient data and validation context.

## 5. Ambiguity Risks
- 'Create analytics report' can mean analyze supplied data, build dashboard, send report, make strategic recommendations, or implement tracking.
- Analysis, dashboard mutation, automated distribution, and decision authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as canonical BI analysis role in the extract -> consolidate -> analyze -> summarize pipeline with lineage, privacy, and dashboard/send gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.0/10


---

# Agent Review: Finance Tracker

Source: `support/support-finance-tracker.md`

## 1. Current Function
Legacy finance status and performance tracking role whose analysis functions route to FP&A, Financial Analyst, Bookkeeper/Controller, Tax, Investment Research, and AP owners.

## 2. Current Role Boundary
Merge Finance Tracker into the finance specialist cluster as a read-only finance status/router mode that produces budget, cash-flow, variance, KPI, and risk-summary drafts from reconciled source data while blocking accounting entries, payments, investment advice, tax conclusions, budget/spend commitments, or forecast signoff without finance owner approval.

## 3. Production Issues
- Original prompt duplicates FP&A Analyst, Financial Analyst, Bookkeeper & Controller, Tax Strategist, Investment Researcher, and Accounts Payable while implying controller authority.
- Finance tracking can produce inaccurate forecasts, unauthorized spend commitments, investment advice, accounting changes, or audit/control exposure.
- Financial workflows require reconciled actuals, source lineage, chart-of-accounts rules, assumptions, confidentiality, and finance-owner approval.

## 4. Token Waste
- Budget/cash-flow code examples should route to FP&A/Financial Analyst modes.
- Financial control detail should be selected by finance owner context.

## 5. Ambiguity Risks
- 'Track finance' can mean dashboard summary, FP&A forecast, controller close work, payment timing, investment analysis, tax planning, or spend approval.
- Read-only analysis, accounting execution, and financial decision authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Merge into the finance specialist cluster, preserving only read-only finance status/router behavior under finance-owner review.

## 8. Merge / Split / Deprecate Recommendation
Decision: merge

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 3.8/10
