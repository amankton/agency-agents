# Batch Summary: batch_009

## Agents Reviewed
- `engineering/engineering-backend-architect.md`: Backend Architect (refactor)
- `engineering/engineering-frontend-developer.md`: Frontend Developer (refactor)
- `engineering/engineering-software-architect.md`: Software Architect (keep)
- `engineering/engineering-senior-developer.md`: Senior Developer (refactor)
- `engineering/engineering-code-reviewer.md`: Code Reviewer (keep)
- `engineering/engineering-sre.md`: SRE (Site Reliability Engineer) (keep)
- `engineering/engineering-database-optimizer.md`: Database Optimizer (refactor)
- `engineering/engineering-data-engineer.md`: Data Engineer (refactor)
- `engineering/engineering-ai-engineer.md`: AI Engineer (refactor)
- `engineering/engineering-prompt-engineer.md`: Prompt Engineer (refactor)

## Recommended Actions
- Keep: 3
- Refactor: 7
- Merge: 0
- Split: 0
- Deprecate: 0
- Rewrite: 0

## Highest-Risk Agent
AI Engineer: it can touch sensitive data, model training, RAG/vector stores, runtime APIs, automated retraining, model releases, and high-impact AI decisions. Those surfaces need dataset provenance, evaluation thresholds, safety review, canary/rollback, monitoring, and human-review gates.

## Biggest Architecture Issue Found
The engineering cluster needs decision-right boundaries. Architecture, backend contracts, scoped implementation, review, reliability, database migration, data pipelines, model deployment, and prompt behavior changes are distinct forms of authority. Batch 009 makes repo edits scoped by ticket and makes production, data, DB, infra, model, prompt, deploy, and secrets mutation approval-gated.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_009.md`
- `agency-audit/refactored-agents/engineering-backend-architect.md`
- `agency-audit/refactored-agents/engineering-frontend-developer.md`
- `agency-audit/refactored-agents/engineering-software-architect.md`
- `agency-audit/refactored-agents/engineering-senior-developer.md`
- `agency-audit/refactored-agents/engineering-code-reviewer.md`
- `agency-audit/refactored-agents/engineering-sre.md`
- `agency-audit/refactored-agents/engineering-database-optimizer.md`
- `agency-audit/refactored-agents/engineering-data-engineer.md`
- `agency-audit/refactored-agents/engineering-ai-engineer.md`
- `agency-audit/refactored-agents/engineering-prompt-engineer.md`
- `agency-audit/acceptance-tests/engineering-backend-architect.tests.md`
- `agency-audit/acceptance-tests/engineering-frontend-developer.tests.md`
- `agency-audit/acceptance-tests/engineering-software-architect.tests.md`
- `agency-audit/acceptance-tests/engineering-senior-developer.tests.md`
- `agency-audit/acceptance-tests/engineering-code-reviewer.tests.md`
- `agency-audit/acceptance-tests/engineering-sre.tests.md`
- `agency-audit/acceptance-tests/engineering-database-optimizer.tests.md`
- `agency-audit/acceptance-tests/engineering-data-engineer.tests.md`
- `agency-audit/acceptance-tests/engineering-ai-engineer.tests.md`
- `agency-audit/acceptance-tests/engineering-prompt-engineer.tests.md`

## Subagent Inputs Used
- Core engineering scan: separated Software Architect, Backend Architect, Frontend Developer, Senior Developer, and Code Reviewer by design, implementation, review, test, deploy, and secrets authority.
- Ops/data/AI scan: separated SRE, Database Optimizer, Data Engineer, AI Engineer, and Prompt Engineer by infra, data, model, prompt, rollout, privacy, and production mutation gates.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Backend Architect

Source: `engineering/engineering-backend-architect.md`

## 1. Current Function
Backend architecture specialist for service boundaries, API design, database architecture, security requirements, scalability plans, migrations, and backend implementation guidance.

## 2. Current Role Boundary
Design backend architecture, API/data contracts, scalability/security requirements, migration plans, and implementation handoffs without directly mutating production code, databases, infrastructure, secrets, or deployments unless explicitly assigned.

## 3. Production Issues
- Overlaps Software Architect on cross-system design and Database Optimizer/Data Engineer on data architecture.
- Original prompt says build and implement backend systems, blurring architecture with code execution.
- Schema, migration, cloud, monitoring, and infrastructure guidance need review, rollback, and ownership gates.

## 4. Token Waste
- Large schema/API examples should be generated from stack and domain inputs.
- Persona and performance target text repeats architecture principles.

## 5. Ambiguity Risks
- 'Build robust applications' can imply code mutation or deployment.
- Migration and IaC ownership are not separated from design authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as backend design/contract owner with ADR, migration, API-contract, test, rollback, deploy, security, and secrets gates.

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

# Agent Review: Frontend Developer

Source: `engineering/engineering-frontend-developer.md`

## 1. Current Function
Frontend implementation specialist for modern web UI, framework components, responsive layouts, accessibility, state management, frontend performance, and tests.

## 2. Current Role Boundary
Implement scoped frontend UI, state, API integration, accessibility, performance, and tests within an approved repository/task boundary without owning final architecture, backend contracts, security exceptions, or production deployment approval.

## 3. Production Issues
- Overlaps Senior Developer on UI implementation and Software Architect on component/design-system architecture.
- Original prompt includes CI/CD and deployment integration without clear deploy authority.
- Client-side code can expose secrets or rely on unstable API contracts if inputs are missing.

## 4. Token Waste
- Framework examples should be driven by repo conventions.
- Broad performance patterns need scoped targets.

## 5. Ambiguity Risks
- 'Implement frontend deployments' can imply release authority.
- Pixel-perfect design requires source design and acceptance criteria.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with scoped code authority, API/design contract, test matrix, CI, preview, browser/device, no-client-secrets, and deploy approval gates.

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

# Agent Review: Software Architect

Source: `engineering/engineering-software-architect.md`

## 1. Current Function
Software architecture specialist for domain modeling, system design, architectural patterns, ADRs, trade-off analysis, and evolution planning.

## 2. Current Role Boundary
Define cross-system architecture, domain boundaries, ADRs, quality attributes, tradeoffs, and evolution strategy as design authority, not default implementation or deployment owner.

## 3. Production Issues
- Cleaner than most engineering prompts but overlaps Backend Architect on system design and service boundaries.
- Needs explicit no-code-by-default and decision hierarchy with specialist architects.
- Architecture recommendations need stakeholder, security, and implementation handoff gates.

## 4. Token Waste
- Lean prompt; ADR and trade-off templates are useful.
- Could add output contract without much extra text.

## 5. Ambiguity Risks
- Architecture authority vs implementation authority is not explicit.
- Fitness checks and CI constraints are not defined.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as cross-system design authority with explicit no-implementation default, ADR approval, stakeholder signoff, security review, and implementation handoff boundaries.

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


---

# Agent Review: Senior Developer

Source: `engineering/engineering-senior-developer.md`

## 1. Current Function
Senior implementation specialist for scoped full-stack or premium frontend tasks, Laravel/Livewire/FluxUI work, advanced CSS, performance tuning, and Three.js integration when approved.

## 2. Current Role Boundary
Implement assigned repository tasks within approved scope, especially Laravel/Livewire/FluxUI premium web slices, while respecting product specs over aesthetic mandates and requiring tests, review, CI, and deployment approval.

## 3. Production Issues
- Broad implementer role overlaps Frontend Developer, Backend Architect implementation, designer, performance engineer, and QA.
- Premium design mandates can override product requirements, accessibility, or existing design systems.
- Original prompt lacks strong repo scope, test, CI, code review, security, and deploy authority gates.

## 4. Token Waste
- Premium examples and effects should be optional patterns, not default requirements.
- External docs and memory references assume unavailable files.

## 5. Ambiguity Risks
- 'Premium' is subjective without design acceptance criteria.
- Full-stack implementation can cross architecture and backend boundaries.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as scoped implementer with ticket, repo, test, CI, review, deploy, accessibility, performance, and product-spec gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.0/10


---

# Agent Review: Code Reviewer

Source: `engineering/engineering-code-reviewer.md`

## 1. Current Function
Independent code review and quality specialist for PR diffs, risk findings, missing tests, security issues, maintainability, and performance feedback.

## 2. Current Role Boundary
Review supplied diffs for correctness, security, maintainability, performance, and test adequacy, using an explicit severity rubric without editing code or approving its own changes.

## 3. Production Issues
- Strong review-only intent, but needs explicit no-edit and independence rules.
- Could be confused with QA, security gatekeeper, or release approver without authority boundaries.
- Needs required CI/test evidence and secrets-in-review safeguards.

## 4. Token Waste
- Lean and useful prompt.
- Emoji severity markers should be normalized in generated prompt.

## 5. Ambiguity Risks
- Blocking authority is not defined.
- Review scope can drift into style preferences or implementation edits.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as independent reviewer with no-edit, diff-only, severity rubric, CI/test evidence, secrets, deployment-risk, and reviewer-independence gates.

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


---

# Agent Review: SRE (Site Reliability Engineer)

Source: `engineering/engineering-sre.md`

## 1. Current Function
Site reliability engineering specialist for SLOs, error budgets, observability, incident integration, toil reduction, progressive rollout design, and production risk assessment.

## 2. Current Role Boundary
Design and review reliability practices, SLOs, observability, runbooks, toil reduction, capacity plans, and rollout/incident guidance without mutating production infrastructure, running chaos tests, or deploying changes unless explicitly authorized.

## 3. Production Issues
- Touches production systems, rollouts, chaos engineering, incidents, and automation without explicit access/approval gates.
- Overlaps DevOps Automator, Incident Responder, Cloud Security Architect, Backend Architect, and Data Engineer.
- SLO and error-budget decisions can affect release governance and operational priorities.

## 4. Token Waste
- Lean prompt; examples are useful.
- Needs stronger input contract more than trimming.

## 5. Ambiguity Risks
- 'Build and maintain production systems' can imply live operations.
- Chaos engineering needs environment and blast-radius approval.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep with light refactor around production access, privacy-aware telemetry, secrets handling, blast-radius, rollout, rollback, chaos-test, incident, and deploy approval gates.

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

# Agent Review: Database Optimizer

Source: `engineering/engineering-database-optimizer.md`

## 1. Current Function
Database performance specialist for query optimization, indexes, schema design, migration strategy, connection pooling, Supabase/PlanetScale patterns, and performance evidence.

## 2. Current Role Boundary
Analyze database schemas, query plans, indexes, pooling, and migration options, then propose reversible, tested changes without applying production migrations, changing live data, or exposing credentials unless approved.

## 3. Production Issues
- Database migrations, indexes, schema changes, and query tuning can lock tables or corrupt data if executed unsafely.
- Overlaps Backend Architect, Data Engineer, SRE, and Security roles.
- Examples include SQL and app code that need environment, data classification, and rollback gates.

## 4. Token Waste
- Examples are useful but should be scoped to dialect and production constraints.
- Needs output contract and migration gate more than broad playbook.

## 5. Ambiguity Risks
- 'Build database architectures' can imply direct migration authority.
- EXPLAIN ANALYZE on production may be unsafe without read-only constraints.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with database access, PII, query-plan evidence, staging benchmark, reversible migration, lock limit, backup, rollback, and deploy gates.

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

# Agent Review: Data Engineer

Source: `engineering/engineering-data-engineer.md`

## 1. Current Function
Data engineering specialist for ETL/ELT, lakehouse architecture, dbt/Spark/streaming pipelines, data contracts, quality checks, lineage, and pipeline reliability.

## 2. Current Role Boundary
Design and implement scoped data pipelines, contracts, quality checks, lineage, and observability only within approved data access and deployment boundaries, without writing production data, backfills, or schema changes without authorization.

## 3. Production Issues
- Prompt includes large executable pipeline examples that can imply write access to data stores.
- Overlaps Database Optimizer, AI Engineer, SRE, Analytics, and Data Governance roles.
- Pipelines, CDC, backfills, and gold-layer outputs can expose PII or corrupt downstream analytics if ungated.

## 4. Token Waste
- Large code samples and medallion examples should be references or generated from stack inputs.
- Success metrics need actual SLA context.

## 5. Ambiguity Risks
- 'Build pipelines' can mean design, local code, staging deploy, or production writes.
- Data quality ownership and consumer approval are not explicit.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with data access, privacy, data contract, schema evolution, backfill, quality, lineage, staging, rollback, and deploy gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.2/10


---

# Agent Review: AI Engineer

Source: `engineering/engineering-ai-engineer.md`

## 1. Current Function
AI/ML engineering specialist for model development, RAG/LLM integration, inference APIs, MLOps, evaluation, monitoring, fairness, privacy, and production AI feature design.

## 2. Current Role Boundary
Develop, evaluate, and integrate AI/ML features within approved data, model, safety, cost, and deployment boundaries, requiring validation and human approval before production model, API, retraining, or inference changes.

## 3. Production Issues
- Prompt implies production model deployment, automated retraining, API creation, and data pipelines without explicit authority gates.
- Overlaps Data Engineer, Prompt Engineer, Backend Architect, SRE, Model QA, and Security roles.
- Sensitive training/inference data, model bias, safety, cost, and drift controls need stronger input contract.

## 4. Token Waste
- Capability lists are broad; examples should be scoped by model type and data availability.
- Generic performance targets can overpromise.

## 5. Ambiguity Risks
- 'Deploy models to production' can imply release authority.
- Bias and safety testing requirements depend on use case and data policy.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with data/model access, license, privacy, evaluation, fairness, safety, cost, monitoring, canary, rollback, and production deploy gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.2/10


---

# Agent Review: Prompt Engineer

Source: `engineering/engineering-prompt-engineer.md`

## 1. Current Function
Prompt engineering specialist for LLM behavior specs, system prompts, few-shot examples, guardrails, prompt tests, changelogs, regression suites, and multi-model compatibility.

## 2. Current Role Boundary
Design, version, and test prompts as behavioral contracts with explicit output schemas, refusal behavior, evaluation cases, model settings, and rollout controls, without exposing hidden reasoning or shipping prompt changes without regression evidence.

## 3. Production Issues
- Prompt includes chain-of-thought patterns that conflict with production hidden-reasoning boundaries.
- Production prompt changes can alter user-facing behavior without code-review, eval, or rollback gates.
- Overlaps AI Engineer, Product, QA, Safety, and Model QA roles.

## 4. Token Waste
- Prompt templates are useful but should enforce no hidden chain-of-thought exposure.
- Examples and test cases should be generated from product behavior specs.

## 5. Ambiguity Risks
- 'Ship prompts to production' can imply release authority.
- Model-specific claims need actual model/version evidence.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with prompt spec, eval suite, versioning, no hidden chain-of-thought exposure, safety review, rollout, monitoring, and rollback gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.2/10
