# Batch Summary: batch_005

## Agents Reviewed
- `security/security-threat-intelligence-analyst.md`: Threat Intelligence Analyst (refactor)
- `security/security-compliance-auditor.md`: Compliance Auditor (refactor)
- `security/security-cloud-security-architect.md`: Cloud Security Architect (refactor)
- `security/security-appsec-engineer.md`: Application Security Engineer (refactor)
- `security/security-architect.md`: Security Architect (rewrite)
- `security/security-blockchain-security-auditor.md`: Blockchain Security Auditor (refactor)
- `specialized/automation-governance-architect.md`: Automation Governance Architect (refactor)
- `specialized/agentic-identity-trust.md`: Agentic Identity & Trust Architect (refactor)
- `specialized/specialized-model-qa.md`: Model QA Specialist (keep)
- `specialized/identity-graph-operator.md`: Identity Graph Operator (refactor)

## Recommended Actions
- Keep: 1
- Refactor: 8
- Merge: 0
- Split: 0
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Blockchain Security Auditor: the current prompt contains exploit-style examples and audit tooling without requiring written scope, commit/deployment mapping, private disclosure rules, or fork/testnet-only proof-of-concept limits.

## Biggest Architecture Issue Found
The security program cluster has strong expertise but weak decision-rights separation. Architecture, AppSec, cloud guardrails, intelligence, compliance, blockchain audit, automation governance, identity trust, model QA, and identity graph operations all need explicit boundaries between draft/advisory artifacts, authorized testing, live enforcement, data access, and production mutation.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_005.md`
- `agency-audit/refactored-agents/security-threat-intelligence-analyst.md`
- `agency-audit/refactored-agents/security-compliance-auditor.md`
- `agency-audit/refactored-agents/security-cloud-security-architect.md`
- `agency-audit/refactored-agents/security-appsec-engineer.md`
- `agency-audit/refactored-agents/security-architect.md`
- `agency-audit/refactored-agents/security-blockchain-security-auditor.md`
- `agency-audit/refactored-agents/automation-governance-architect.md`
- `agency-audit/refactored-agents/agentic-identity-trust.md`
- `agency-audit/refactored-agents/specialized-model-qa.md`
- `agency-audit/refactored-agents/identity-graph-operator.md`
- `agency-audit/acceptance-tests/security-threat-intelligence-analyst.tests.md`
- `agency-audit/acceptance-tests/security-compliance-auditor.tests.md`
- `agency-audit/acceptance-tests/security-cloud-security-architect.tests.md`
- `agency-audit/acceptance-tests/security-appsec-engineer.tests.md`
- `agency-audit/acceptance-tests/security-architect.tests.md`
- `agency-audit/acceptance-tests/security-blockchain-security-auditor.tests.md`
- `agency-audit/acceptance-tests/automation-governance-architect.tests.md`
- `agency-audit/acceptance-tests/agentic-identity-trust.tests.md`
- `agency-audit/acceptance-tests/specialized-model-qa.tests.md`
- `agency-audit/acceptance-tests/identity-graph-operator.tests.md`

## Candidate Adjustment
`security/security-threat-detection-engineer.md` was listed in the roadmap for batch 005 but had already been completed in batch 002. This batch uses `specialized/identity-graph-operator.md` instead because it carries closely related identity, PII, tenant-isolation, and mutation-governance risk.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Threat Intelligence Analyst

Source: `security/security-threat-intelligence-analyst.md`

## 1. Current Function
Cyber threat intelligence, adversary tracking, MITRE ATT&CK mapping, IOC enrichment, malware/campaign analysis, and detection-rule development agent.

## 2. Current Role Boundary
Produce source-rated cyber threat intelligence, ATT&CK mapping, IOC packages, detection opportunities, and defensive recommendations without deploying rules or interacting with threat actors.

## 3. Production Issues
- Overlaps Threat Detection Engineer on detection rules and hunting logic.
- Includes IOC enrichment code, YARA/Sigma/Snort examples, and threat hunting guidance that may be mistaken for live deployment.
- No required TLP/source handling, legal authorization, or collection boundary inputs.

## 4. Token Waste
- Large detection-rule and script examples should be reference material.
- Threat-actor persona text repeats the analytical standards.

## 5. Ambiguity Risks
- 'Build detection rules' can mean draft, validate, or deploy.
- Attribution and confidence levels require source reliability rules.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as intelligence producer with source handling, confidence, and deployment-boundary gates.

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

# Agent Review: Compliance Auditor

Source: `security/security-compliance-auditor.md`

## 1. Current Function
Technical compliance readiness, controls assessment, evidence collection, policy mapping, and audit support agent.

## 2. Current Role Boundary
Assess technical compliance readiness against scoped frameworks by mapping controls, evidence, gaps, remediation owners, exceptions, and audit-readiness status.

## 3. Production Issues
- Can imply certification or legal compliance judgment beyond technical readiness.
- Evidence collection and control testing need audit scope, framework version, and data-handling rules.
- Overlaps Senior SecOps, Cloud Security Architect, and AppSec Engineer on control implementation.

## 4. Token Waste
- Framework examples are compact but still need a stronger input contract.
- Persona content is less important than audit scope and evidence rules.

## 5. Ambiguity Risks
- 'Certification' can imply guaranteed audit outcome.
- Compliance findings can become legal advice without boundaries.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as technical readiness assessor with scoped framework, evidence, minimization, and legal-boundary controls.

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

# Agent Review: Cloud Security Architect

Source: `security/security-cloud-security-architect.md`

## 1. Current Function
Multi-cloud security architecture, zero trust, IAM, IaC security, logging, detection, and compliance automation agent.

## 2. Current Role Boundary
Design cloud security architecture, IAM guardrails, IaC policy, logging, and posture-improvement plans for approved cloud environments without applying live changes.

## 3. Production Issues
- Includes Terraform, Kubernetes, and CI/CD examples that may be interpreted as deployable production changes.
- Overlaps DevOps Automator, SRE, Threat Detection Engineer, Compliance Auditor, and Security Architect.
- Cloud posture assessment can require privileged cloud access and sensitive architecture data.

## 4. Token Waste
- Long IaC and workflow snippets belong behind approval gates or references.
- Architecture slogans repeat least-privilege principles.

## 5. Ambiguity Risks
- 'Implement automated response' can mean disruptive containment actions.
- Cloud provider assumptions may not match the target environment.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as plan-first cloud security architect with explicit access, approval, and rollback gates.

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

# Agent Review: Application Security Engineer

Source: `security/security-appsec-engineer.md`

## 1. Current Function
Application security, secure SDLC, threat modeling, secure code review, SAST/DAST integration, and developer enablement agent.

## 2. Current Role Boundary
Review application security design and code evidence, produce threat models, secure requirements, findings, and SDLC guardrails without running unauthorized scans or offensive tests.

## 3. Production Issues
- Embeds vulnerable/fixed code and dependency-audit scripts that may imply tool execution.
- Overlaps Security Architect, Penetration Tester, API Tester, and Compliance Auditor.
- Manual penetration testing and DAST references need explicit environment, authorization, and non-destructive limits.

## 4. Token Waste
- Large code examples should be references.
- Breach anecdotes and persona text are less useful than scope and evidence requirements.

## 5. Ambiguity Risks
- 'Never approve code' can imply gate authority the agent may not have.
- Security testing scope may overlap offensive assessment.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as evidence-based AppSec reviewer with explicit environment, authorization, and gate-authority inputs.

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

# Agent Review: Security Architect

Source: `security/security-architect.md`

## 1. Current Function
Security architecture, threat modeling, trust-boundary analysis, secure-by-design review, and risk-based security design agent.

## 2. Current Role Boundary
Design system-level security models, threat boundaries, risk reviews, and defense-in-depth requirements while routing implementation, scans, and incident work to specialists.

## 3. Production Issues
- Strongly positioned as blueprint role but still includes secure code review, testing, and CI/CD examples.
- Overlaps AppSec Engineer on code/SDLC and Cloud Security Architect on cloud guardrails.
- Security findings need authorization, evidence, and severity rubric inputs.

## 4. Token Waste
- Some code and CI examples duplicate AppSec content.
- Adversarial mindset text is longer than the handoff rules.

## 5. Ambiguity Risks
- 'Perform security testing' can drift into pentesting.
- Copy-paste remediation code may be unsafe without stack context.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as architecture-artifact specialist and remove code review, testing, SOC, and IR ownership from the active role.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 3.6/10


---

# Agent Review: Blockchain Security Auditor

Source: `security/security-blockchain-security-auditor.md`

## 1. Current Function
Smart contract security audit, DeFi vulnerability analysis, formal verification, exploit analysis, and audit report writing agent.

## 2. Current Role Boundary
Perform authorized smart-contract audit planning, evidence-based review, invariant analysis, and defensive reporting with exploit demonstrations limited to agreed scope.

## 3. Production Issues
- Contains exploit-style Solidity examples and audit scripts without an active authorization gate.
- Audit scope, deployed bytecode verification, chain/network, and disclosure channel are not required inputs.
- Overlaps Penetration Tester and AppSec Engineer but carries higher financial-loss and exploit demonstration risk.

## 4. Token Waste
- Exploit snippets should be gated reference material.
- Adversarial persona text adds heat without scope controls.

## 5. Ambiguity Risks
- 'Proof-of-concept exploit' can be unsafe outside private audit scope.
- Formal verification and tool availability are assumed.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with authorization-first audit scope, fork/testnet-only PoCs, and strictly private defensive reporting limits.

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

# Agent Review: Automation Governance Architect

Source: `specialized/automation-governance-architect.md`

## 1. Current Function
Governance-first business automation reviewer for n8n-style workflows and integration processes.

## 2. Current Role Boundary
Assess business automations for value, risk, maintainability, rollout controls, evidence, fallback, and re-audit triggers before implementation.

## 3. Production Issues
- Overlaps orchestrator on workflow design and execution.
- Touches auth, token lifecycle, source-of-truth, and data mapping without full data governance boundaries.
- Needs clearer authority limits and risk thresholds for approval recommendations.

## 4. Token Waste
- Lean prompt; little bloat.
- Decision framework is useful but could be more structured for scoring.

## 5. Ambiguity Risks
- 'Approve' may be confused with production authorization.
- Recommended architecture can drift into implementation.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as advisory governance role with production-approval, data, fallback, and evidence gates.

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

# Agent Review: Agentic Identity & Trust Architect

Source: `specialized/agentic-identity-trust.md`

## 1. Current Function
Agent identity and trust architecture for autonomous agents, delegation chains, credentials, evidence records, and verification protocols.

## 2. Current Role Boundary
Design agent identity, authentication proofs, scoped delegation verification, trust evidence schemas, and fail-closed authorization requirements for multi-agent systems.

## 3. Production Issues
- Overlaps Security Architect and IAM roles on identity policy and credential lifecycle.
- Overlaps orchestrator on agent registry, delegation routing, and runtime enforcement.
- Design examples imply issuing access or writing evidence infrastructure without authority separation.

## 4. Token Waste
- Code sketches are useful but should be subordinate to architecture contract.
- Identity-failure anecdotes repeat the zero-trust principle.

## 5. Ambiguity Risks
- 'Implement credential lifecycle' can mean design requirements or grant production access.
- Trust scoring can be mistaken for runtime authorization decision ownership.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor to separate design/specification from runtime access grants and enforcement.

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

# Agent Review: Model QA Specialist

Source: `specialized/specialized-model-qa.md`

## 1. Current Function
Independent ML/statistical model QA, replication, calibration, monitoring, fairness, interpretability, and audit-grade reporting agent.

## 2. Current Role Boundary
Independently audit models built by others using reproducible data reconstruction, replication, calibration, drift, fairness, interpretability, and severity-rated findings.

## 3. Production Issues
- Strong role boundary but needs explicit conflict-of-interest and sensitive-data authorization gates.
- Examples assume access to raw data, protected attributes, model objects, and runtime environment.
- Can be confused with model builder or deployment approver.

## 4. Token Waste
- Metric code examples are useful but lengthy.
- Failure-mode narrative repeats audit skepticism.

## 5. Ambiguity Risks
- 'Audit full lifecycle' may include governance approval beyond QA.
- Fairness testing requires lawful basis and protected-attribute handling rules.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as independent QA role with conflict-of-interest, sensitive-data, and reproducibility gates.

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

# Agent Review: Identity Graph Operator

Source: `specialized/identity-graph-operator.md`

## 1. Current Function
Shared identity graph operator for entity resolution, canonical IDs, merge/split proposals, conflict handling, PII masking, and graph integrity.

## 2. Current Role Boundary
Operate entity identity resolution through tenant-scoped, evidence-backed canonical IDs, merge/split proposals, confidence thresholds, and audited graph mutation protocols.

## 3. Production Issues
- Can mutate identity graph records, merge/split entities, and reveal PII without explicit governance envelope.
- Overlaps data/master-data roles, orchestrator routing, security tenant/PII authorization, and Agentic Identity Trust.
- Success metrics such as zero identity conflicts and p99 latency are not tied to an actual graph or SLA inputs.

## 4. Token Waste
- Matching code examples are useful but need stronger data-stewardship context.
- Integration table broadens beyond identity resolution.

## 5. Ambiguity Risks
- 'Direct merge' can be unsafe for high-impact entities.
- Agent identity and entity identity can be confused despite the note.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with data stewardship, PII, tenant isolation, proposal-first, and high-impact merge approval rules.

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
