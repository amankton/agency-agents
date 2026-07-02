# Batch Summary: batch_017

## Agents Reviewed
- `engineering/engineering-it-service-manager.md`: IT Service Manager (split)
- `engineering/engineering-cms-developer.md`: CMS Developer (refactor)
- `engineering/engineering-git-workflow-master.md`: Git Workflow Master (rewrite)
- `specialized/lsp-index-engineer.md`: LSP/Index Engineer (refactor)
- `specialized/corporate-training-designer.md`: Corporate Training Designer (refactor)
- `specialized/specialized-french-consulting-market.md`: French Consulting Market Navigator (rewrite)
- `sales/sales-discovery-coach.md`: Discovery Coach (deprecate)
- `specialized/specialized-civil-engineer.md`: Civil Engineer (split)
- `specialized/accounts-payable-agent.md`: Accounts Payable Agent (rewrite)
- `marketing/marketing-livestream-commerce-coach.md`: Livestream Commerce Coach (split)

## Recommended Actions
- Keep: 0
- Refactor: 3
- Merge: 0
- Split: 3
- Deprecate: 1
- Rewrite: 3

## Highest-Risk Agent
Accounts Payable Agent: it can move money across ACH, wire, API, crypto, and stablecoin rails while touching vendor bank details, duplicate detection, approvals, retries, ERP records, and fraud controls. Civil Engineer is the safety runner-up because sealed design, permits, construction directives, inspections, and code compliance require licensed professional accountability.

## Biggest Architecture Issue Found
Batch 017 shows that service and workflow helpers can mutate operational systems and trust records: IT tickets, CMS content/admin state, Git history, code indexes, LMS records, market/legal assumptions, CRM discovery records, payments, sealed designs, and live commerce actions. The batch turns those prompts into evidence, draft, and control-artifact producers until authority, source evidence, privacy, licensed review, auditability, and rollback are explicit.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_017.md`
- `agency-audit/refactored-agents/engineering-it-service-manager.md`
- `agency-audit/refactored-agents/engineering-cms-developer.md`
- `agency-audit/refactored-agents/engineering-git-workflow-master.md`
- `agency-audit/refactored-agents/lsp-index-engineer.md`
- `agency-audit/refactored-agents/corporate-training-designer.md`
- `agency-audit/refactored-agents/specialized-french-consulting-market.md`
- `agency-audit/refactored-agents/sales-discovery-coach.md`
- `agency-audit/refactored-agents/specialized-civil-engineer.md`
- `agency-audit/refactored-agents/accounts-payable-agent.md`
- `agency-audit/refactored-agents/marketing-livestream-commerce-coach.md`
- `agency-audit/acceptance-tests/engineering-it-service-manager.tests.md`
- `agency-audit/acceptance-tests/engineering-cms-developer.tests.md`
- `agency-audit/acceptance-tests/engineering-git-workflow-master.tests.md`
- `agency-audit/acceptance-tests/lsp-index-engineer.tests.md`
- `agency-audit/acceptance-tests/corporate-training-designer.tests.md`
- `agency-audit/acceptance-tests/specialized-french-consulting-market.tests.md`
- `agency-audit/acceptance-tests/sales-discovery-coach.tests.md`
- `agency-audit/acceptance-tests/specialized-civil-engineer.tests.md`
- `agency-audit/acceptance-tests/accounts-payable-agent.tests.md`
- `agency-audit/acceptance-tests/marketing-livestream-commerce-coach.tests.md`

## Subagent Inputs Used
- Technical/service scan: split IT Service Manager; refactor CMS Developer, LSP/Index Engineer, and Corporate Training Designer; rewrite Git Workflow Master around service, environment, repository, privacy, release, LMS, and mutation gates.
- Commercial/regulated scan: rewrite French Consulting Market Navigator and Accounts Payable Agent; deprecate Discovery Coach into Sales Coach; split Civil Engineer and Livestream Commerce Coach around licensed, payment, platform, spend, customer, and public-safety gates.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: IT Service Manager

Source: `engineering/engineering-it-service-manager.md`

## 1. Current Function
IT service-management specialist for ITIL-aligned service design, incident/problem/change process artifacts, SLA reporting drafts, CMDB governance, knowledge-base planning, and improvement handoffs.

## 2. Current Role Boundary
Produce ITSM service-catalog, incident, problem, change, SLA, CMDB, knowledge, and continual-improvement advisory artifacts from approved service context while blocking ticket mutation, incident command, change approval, production actions, CMDB writes, SLA commitments, or user communications without service-owner, CAB, and communications approval.

## 3. Production Issues
- Original prompt combines ITSM advisory design with incident command, change control, SLA governance, CMDB maintenance, and service communications.
- ITSM execution can mutate tickets, status pages, change records, CMDB CIs, SLAs, user communications, and production workflows.
- Overlaps SRE, DevOps Automator, Incident Responder, Change Manager, CMDB Owner, IT Ops, Service Owners, and Support Infrastructure.

## 4. Token Waste
- Service catalog, incident, problem, change, SLA, CMDB, and CSI templates should be generated by mode.
- ITIL framework detail should be concise unless the artifact requires it.

## 5. Ambiguity Risks
- 'Manage IT service' can mean process design, ticket updates, incident command, CAB approval, or production remediation.
- Advisory, operational, communication, and system-of-record authorities are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split advisory ITSM design from ticket/change/CMDB execution with authority, audit, rollback, and communications approval gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 4.6/10


---

# Agent Review: CMS Developer

Source: `engineering/engineering-cms-developer.md`

## 1. Current Function
Code-first CMS implementation specialist for Drupal and WordPress architecture, themes, plugins/modules, editorial workflows, accessibility, performance, security, and release handoffs.

## 2. Current Role Boundary
Produce Drupal/WordPress content-model, theme, plugin/module, block, audit, and implementation artifacts for an approved local or staging scope while blocking production publishing, admin changes, plugin installation, database migration, deploys, secrets access, or content edits without content, security, accessibility, and release-owner approval.

## 3. Production Issues
- Original prompt is implementation-oriented but lacks environment, content-owner, deployment, admin, plugin, database, and rollback gates.
- CMS work can mutate production content, site settings, plugins/modules, databases, credentials, SEO metadata, accessibility, and security posture.
- Overlaps Frontend Developer, DevOps Automator, Security Reviewer, Accessibility Auditor, SEO Specialist, Content Owner, and Release Manager.

## 4. Token Waste
- WordPress and Drupal guidance should be selected by declared stack and version.
- Full boilerplates should appear only when code generation is requested.

## 5. Ambiguity Risks
- 'Deliver production-ready CMS implementation' can mean local code, staging deploy, production publish, or admin UI mutation.
- Content modeling, code changes, plugin vetting, content publishing, and release authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as local/staging CMS implementation with stack/version, content-owner, security, accessibility, deploy, database, and rollback gates.

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

# Agent Review: Git Workflow Master

Source: `engineering/engineering-git-workflow-master.md`

## 1. Current Function
Git workflow steward for branching strategy, commit hygiene, safe recovery plans, PR preparation, CI/release coordination, and repository-governance handoffs.

## 2. Current Role Boundary
Produce Git workflow, branching, recovery, PR hygiene, history-cleanup, release-tag, and CI-friendly guidance from repository policy and branch state while blocking branch deletion, force-push, rebase, merge, tag, release, remote mutation, or destructive recovery commands without explicit repo authority, clean backup, CI evidence, and rollback plan.

## 3. Production Issues
- Original prompt includes advanced Git operations and cleanup workflows without requiring repo authority, branch ownership, backup, CI state, or release gates.
- Git advice can destroy work, rewrite shared history, bypass branch protection, trigger releases, delete branches/tags, or alter auditability.
- Overlaps Code Reviewer, Senior Developer, Release Manager, Repo Maintainer, CI Owner, Security Reviewer, and Project Manager.

## 4. Token Waste
- Branching strategy, rebase, worktree, bisect, recovery, and release guidance should be generated by mode.
- Diagrams and command sequences should be included only when requested.

## 5. Ambiguity Risks
- 'Clean up history' can mean advice, local fixup, shared rebase, force-push, or release-tag rewrite.
- Advisory guidance, local operations, remote mutation, release authority, and destructive recovery are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as a Git workflow steward with advice-first behavior and explicit authority, backup, CI, release, and rollback gates for mutation.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 7
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 5.0/10


---

# Agent Review: LSP/Index Engineer

Source: `specialized/lsp-index-engineer.md`

## 1. Current Function
LSP and semantic-code-index specialist for local/sandbox language-server orchestration, graph generation, symbol indexing, cache design, and code-intelligence performance handoffs.

## 2. Current Role Boundary
Produce privacy-safe LSP orchestration, semantic-index, graph-schema, cache, performance, and implementation artifacts for an approved repo allowlist while blocking secret indexing, private-data capture, external egress, persistent storage, hooks/watchers, or runtime tool changes without repo owner, security, and privacy approval.

## 3. Production Issues
- Original prompt assumes broad codebase indexing, file watchers, git hooks, WebSockets, caches, and cross-language semantic graph generation without privacy and secret boundaries.
- Indexing can capture secrets, proprietary code, personal data, vendor code, generated artifacts, hidden files, and sensitive dependency graphs.
- Overlaps Backend Architect, DevOps Automator, Security Reviewer, Privacy Reviewer, Repo Owner, and developer tooling owners.

## 4. Token Waste
- LSP protocol, graph schema, cache, and performance guidance should be selected by language/runtime.
- Large architecture snippets should require implementation scope.

## 5. Ambiguity Risks
- 'Build code intelligence' can mean design spec, local prototype, repo-wide index, daemon deployment, or telemetry/export.
- Local indexing, persistent storage, external egress, hooks, and production tooling are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around local/sandbox indexing, repo allowlists, secret exclusion, retention controls, and no hooks or egress without approval.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.6/10


---

# Agent Review: Corporate Training Designer

Source: `specialized/corporate-training-designer.md`

## 1. Current Function
Corporate learning-design specialist for training-needs analysis, instructional design, blended learning, course assets, trainer development, leadership programs, compliance training, and evaluation handoffs.

## 2. Current Role Boundary
Produce corporate training needs-analysis, curriculum, course-package, trainer-development, leadership, onboarding, compliance-training, and evaluation artifacts from approved business and HR context while blocking employee assessment decisions, 360/HIPO actions, compliance-record changes, LMS mutations, legal/HR conclusions, or manager communications without HR, privacy, and compliance approval.

## 3. Production Issues
- Original prompt spans employee data, assessments, 360 feedback, HIPO/succession, compliance training records, LMS platforms, HR policy, and China PIPL/legal topics.
- Training design can affect employee evaluation, promotion, compliance attestations, privacy, labor relations, safety, anti-corruption, and system-of-record training data.
- Overlaps HR/People Ops, L&D, Employment Counsel, Privacy, Compliance, HR Onboarding, Change Management, and LMS admins.

## 4. Token Waste
- TNA, curriculum, micro-course, TTT, leadership, compliance, and evaluation templates should be mode-specific.
- Platform catalogs should be generated only when selection is in scope.

## 5. Ambiguity Risks
- 'Design training system' can mean draft curriculum, collect employee data, assign courses, update LMS, or evaluate performance.
- Learning design, employee assessment, compliance records, HR decisions, and system mutation are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with learner-data, HR/legal, compliance-record, LMS-mutation, and manager-communication gates while keeping training design artifact-focused.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.6/10


---

# Agent Review: French Consulting Market Navigator

Source: `specialized/specialized-french-consulting-market.md`

## 1. Current Function
French consulting market decision-support specialist for ESN/SI ecosystem mapping, rate-positioning ranges, platform strategy, freelance structure comparison, payment-risk planning, and licensed-review handoffs.

## 2. Current Role Boundary
Produce current-source French IT consulting, ESN/SI, freelance platform, TJM positioning, portage salarial, payment-cycle, and negotiation decision-support artifacts from declared residency, entity, and market context while blocking legal, tax, employment, immigration, accounting, contract, filing, platform-account, or payment advice without licensed local review.

## 3. Production Issues
- Original prompt gives concrete French tax, employment, portage, platform, and rate guidance that can become stale or jurisdiction-dependent.
- Freelance consulting guidance touches legal structure, residency, tax/social charges, employment classification, contracts, non-competes, payment delays, and platform/account actions.
- Overlaps Tax Strategist, Legal Document Review, Financial Analyst, Business Strategist, Pricing Analyst, and local French accountant/counsel.

## 4. Token Waste
- ESN, platform, rate, portage, and contract playbooks should be mode-specific.
- Static rates and margins need source dates and confidence labels.

## 5. Ambiguity Risks
- 'Optimize French freelance setup' can mean market education, legal entity choice, tax planning, contract review, or platform account changes.
- Market advice, legal/tax/accounting advice, and platform/action authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as current-source French freelance market decision support with legal/tax/employment/accounting, contract, filing, platform, and payment-action gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

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

# Agent Review: Discovery Coach

Source: `sales/sales-discovery-coach.md`

## 1. Current Function
Legacy discovery-methodology coaching specialist whose responsibilities should be folded into Sales Coach with explicit call evidence, rep consent, prospect PII, CRM, and manager boundaries.

## 2. Current Role Boundary
Deprecate the standalone Discovery Coach prompt into Sales Coach as a discovery-only coaching mode that produces call-prep, question-design, current-state mapping, gap-quantification, and coaching artifacts while blocking prospect contact, CRM edits, call-recording misuse, personnel decisions, or unsupported product claims.

## 3. Production Issues
- Discovery Coach overlaps heavily with Sales Coach's call coaching, deal prep, behavioral feedback, and qualification discipline.
- Discovery coaching can expose prospect PII, call recordings, rep performance data, product claims, and CRM/pipeline records.
- Standalone prompt increases routing ambiguity across Sales Coach, Sales Engineer, Deal Strategist, Pipeline Analyst, RevOps, and HR.

## 4. Token Waste
- SPIN, Gap Selling, and Sandler guidance should be selected as a Sales Coach mode.
- Duplicate coaching frameworks should not live in a standalone agent.

## 5. Ambiguity Risks
- 'Coach discovery' can mean call-prep advice, call-recording review, live call participation, CRM updates, or rep performance management.
- Rep coaching, prospect communication, product claims, and personnel decisions are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Deprecate into Sales Coach as discovery-only mode with call-recording consent, PII minimization, no prospect contact, no CRM edits, and no personnel decisions.

## 8. Merge / Split / Deprecate Recommendation
Decision: deprecate

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.6/10


---

# Agent Review: Civil Engineer

Source: `specialized/specialized-civil-engineer.md`

## 1. Current Function
Civil/structural engineering advisory specialist for basis-of-design, preliminary calculations, code/source mapping, geotechnical coordination notes, documentation review, and licensed-EOR handoffs.

## 2. Current Role Boundary
Produce civil/structural engineering advisory calculations, code matrices, basis-of-design drafts, constructability notes, and review checklists from supplied licensed-engineer scope and source data while blocking sealed design, drawings, permit/AHJ submissions, construction directives, site inspections, final safety decisions, or code compliance certification without licensed engineer of record approval.

## 3. Production Issues
- Original prompt implies broad structural analysis, geotechnical design, construction documentation, code compliance, RFIs, and international standard authority.
- Civil/structural engineering affects public safety, permits, construction, liability, code compliance, geotechnical risk, and licensed professional responsibility.
- Overlaps licensed engineer of record, geotechnical engineer, AHJ/permit owner, architect, construction manager, safety QA, and legal/insurance reviewers.

## 4. Token Waste
- Global code catalogs should be generated only for declared jurisdiction and code edition.
- Calculation templates should be scoped to preliminary/advisory use.

## 5. Ambiguity Risks
- 'Design structures' can mean preliminary advice, sealed calculations, construction drawings, RFI responses, inspections, or AHJ submissions.
- Advisory calculations and licensed engineering deliverables are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split advisory calculations and code matrices from sealed design, drawings, RFIs, inspections, AHJ submissions, and construction directives requiring licensed approval.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.6/10


---

# Agent Review: Accounts Payable Agent

Source: `specialized/accounts-payable-agent.md`

## 1. Current Function
Accounts-payable control and payment-preparation specialist for invoice review, vendor verification, fraud checks, approval packets, payment batch drafts, exception routing, and audit handoffs.

## 2. Current Role Boundary
Produce accounts-payable controls, invoice intake, three-way-match, vendor-verification, duplicate-payment, approval-routing, payment-batch, and audit-log preparation artifacts while blocking autonomous payment sends, vendor bank changes, crypto/stablecoin transfers, ERP/payment mutations, recurring payment setup, or payment-rail retries without dual approval and treasury/controller authority.

## 3. Production Issues
- Original prompt explicitly describes autonomous payment execution across ACH, wire, crypto, stablecoins, payment APIs, retries, and vendor registry memory.
- AP workflows are high-risk for fraud, duplicate payments, vendor bank compromise, sanctions/tax compliance, approval bypass, irreversible crypto transfer, and ERP/payment-system mutation.
- Overlaps Bookkeeper/Controller, Finance, Treasury, Procurement, Legal/Tax, ERP Admin, Fraud/Security, and Payment Operations.

## 4. Token Waste
- Payment rail execution code should be replaced with controls and approval artifacts.
- Vendor registry and memory behavior should be governed by ERP/vendor-master rules.

## 5. Ambiguity Risks
- 'Process payments autonomously' can mean prepare AP packet or actually move money.
- Invoice review, vendor setup, approval, payment execution, ERP posting, and retry authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as AP controls and payment-prep only, requiring vendor verification, three-way match, dual approval, fraud checks, and no payment or vendor-bank mutation by default.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 7
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 3

Final Rating: 5.6/10


---

# Agent Review: Livestream Commerce Coach

Source: `marketing/marketing-livestream-commerce-coach.md`

## 1. Current Function
Livestream commerce coaching specialist for host development, script planning, product sequencing, platform-compliance review, traffic funnel analysis, and operator handoffs.

## 2. Current Role Boundary
Produce livestream host-training, script, product-sequencing, compliance-review, traffic-analysis, and post-stream coaching artifacts from approved platform and product evidence while blocking live-room operation, posting, paid spend, coupons, price/inventory/order/refund changes, creator contracts, customer contact, or regulated product claims without store, platform, legal, and paid-media approval.

## 3. Production Issues
- Original prompt combines coaching with live-room operations, Qianchuan paid traffic, product sequencing, platform compliance, pricing urgency, coupons, inventory, and sales conversion.
- Livestream commerce can mutate platform accounts, paid spend, pricing, coupons, inventory, orders, customer data, creator deals, regulated claims, and public content in real time.
- Overlaps China E-Commerce Operator, Paid Media, Multi-Platform Publisher, Legal/Compliance, Store Owner, Customer Service, Creator/KOL management, and Supply Chain.

## 4. Token Waste
- Host training, script, product sequencing, traffic, compliance, and analytics templates should be mode-specific.
- Platform metrics and rules need current source dates.

## 5. Ambiguity Risks
- 'Coach livestream operations' can mean training artifact, live operator instruction, paid campaign action, pricing/coupon changes, or customer/order handling.
- Coaching, publishing, ad spend, commerce operations, creator deals, and customer actions are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split host/script coaching and analytics from live-room execution, paid spend, publishing, coupons, prices, inventory, orders, refunds, creator deals, and customer actions.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 5

Final Rating: 5.6/10
