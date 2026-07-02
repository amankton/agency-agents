# Batch Summary: batch_002

## Agents Reviewed
- `security/security-incident-responder.md`: Incident Responder (rewrite)
- `security/security-senior-secops.md`: Senior SecOps Engineer (refactor)
- `engineering/engineering-devops-automator.md`: DevOps Automator (refactor)
- `paid-media/paid-media-search-query-analyst.md`: Search Query Analyst (refactor)
- `paid-media/paid-media-tracking-specialist.md`: Tracking & Measurement Specialist (refactor)
- `testing/testing-api-tester.md`: API Tester (refactor)
- `testing/testing-accessibility-auditor.md`: Accessibility Auditor (refactor)
- `product/product-manager.md`: Product Manager (split)
- `security/security-threat-detection-engineer.md`: Threat Detection Engineer (refactor)
- `testing/testing-performance-benchmarker.md`: Performance Benchmarker (refactor)

## Recommended Actions
- Keep: 0
- Refactor: 8
- Merge: 0
- Split: 1
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Incident Responder: the current prompt embeds privileged forensic collection scripts and containment language without requiring legal scope, evidence handling policy, or authority gates.

## Biggest Architecture Issue Found
The remaining risk is not just vague prompting. It is agents implying production, security, advertising, telemetry, or load-test actions without a standard authorization envelope. Batch 002 extends the safety-gate pattern from batch 001 across DFIR, SecOps, DevOps, paid-media, product, testing, and detection engineering.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_002.md`
- `agency-audit/refactored-agents/security-incident-responder.md`
- `agency-audit/refactored-agents/security-senior-secops.md`
- `agency-audit/refactored-agents/engineering-devops-automator.md`
- `agency-audit/refactored-agents/paid-media-search-query-analyst.md`
- `agency-audit/refactored-agents/paid-media-tracking-specialist.md`
- `agency-audit/refactored-agents/testing-api-tester.md`
- `agency-audit/refactored-agents/testing-accessibility-auditor.md`
- `agency-audit/refactored-agents/product-manager.md`
- `agency-audit/refactored-agents/security-threat-detection-engineer.md`
- `agency-audit/refactored-agents/testing-performance-benchmarker.md`
- `agency-audit/acceptance-tests/security-incident-responder.tests.md`
- `agency-audit/acceptance-tests/security-senior-secops.tests.md`
- `agency-audit/acceptance-tests/engineering-devops-automator.tests.md`
- `agency-audit/acceptance-tests/paid-media-search-query-analyst.tests.md`
- `agency-audit/acceptance-tests/paid-media-tracking-specialist.tests.md`
- `agency-audit/acceptance-tests/testing-api-tester.tests.md`
- `agency-audit/acceptance-tests/testing-accessibility-auditor.tests.md`
- `agency-audit/acceptance-tests/product-manager.tests.md`
- `agency-audit/acceptance-tests/security-threat-detection-engineer.tests.md`
- `agency-audit/acceptance-tests/testing-performance-benchmarker.tests.md`

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Incident Responder

Source: `security/security-incident-responder.md`

## 1. Current Function
DFIR and breach-response agent for active or suspected security incidents.

## 2. Current Role Boundary
Coordinate digital forensics and incident response through scoped triage, evidence preservation, containment planning, and post-incident reporting.

## 3. Production Issues
- Embeds administrator/root forensic collection scripts directly in the active prompt.
- No required legal scope, evidence policy, chain-of-custody, or authorization input.
- Containment and eradication actions are mixed with analysis and reporting responsibilities.

## 4. Token Waste
- Large OS-specific scripts should be gated runbook references.
- War-room persona text repeats the core incident-response job.

## 5. Ambiguity Risks
- 'Containment' can mean disruptive production actions without approval.
- Threat actor attribution guidance lacks confidence and evidence thresholds.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as DFIR planner by default; move scripts behind explicit authorization and chain-of-custody gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 3
- Orchestration Fit: 3

Final Rating: 3.2/10


---

# Agent Review: Senior SecOps Engineer

Source: `security/security-senior-secops.md`

## 1. Current Function
Defensive application security review and secure implementation agent.

## 2. Current Role Boundary
Review or implement defensive application security controls against an explicit security standard and return prioritized findings with fixes.

## 3. Production Issues
- Depends on `security/17-security-pattern.md`, which is not present in the repository.
- Says it scans before reading the request, but lacks an input/tool contract for full-code scans.
- Very large embedded pattern library makes the prompt expensive and hard to maintain.

## 4. Token Waste
- Security pattern tables should be a versioned reference file.
- Repeated absolute rules inflate prompt size.

## 5. Ambiguity Risks
- Automatic scan scope is unclear when only prose or partial files are provided.
- Standard citations are impossible if the standard file is unavailable.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Require the security standard as input or use a compact baseline; emit structured findings and tool-failure states.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.6/10


---

# Agent Review: DevOps Automator

Source: `engineering/engineering-devops-automator.md`

## 1. Current Function
Infrastructure automation, CI/CD, and cloud operations agent.

## 2. Current Role Boundary
Design or update infrastructure automation and CI/CD plans with explicit environment, approval, rollback, secrets, and monitoring constraints.

## 3. Production Issues
- Encourages implementation of pipelines and infrastructure without requiring environment authority.
- Example deployment commands imply production changes without approval gates.
- No structured rollback, secrets, or blast-radius contract.

## 4. Token Waste
- Generic IaC examples dominate the prompt.
- Success metrics are broad and not tied to supplied baseline.

## 5. Ambiguity Risks
- 'Fully automated' can conflict with required human approval for production.
- Cloud/provider choice is not constrained by inputs.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as plan-first DevOps agent with privileged execution gated by environment and approval payloads.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 4
- Orchestration Fit: 4

Final Rating: 4.0/10


---

# Agent Review: Search Query Analyst

Source: `paid-media/paid-media-search-query-analyst.md`

## 1. Current Function
Paid-search query mining and negative keyword analysis agent.

## 2. Current Role Boundary
Analyze search-term data and propose negative keyword, intent, and query-sculpting changes with conflict checks and approval gates.

## 3. Production Issues
- Says to push negative keyword changes directly back to accounts.
- No conflict analysis, rollback list, date range, or account ID is required.
- Assumes live API access and actual query data.

## 4. Token Waste
- Capability list repeats PPC Strategist scope.
- Success metrics are generic without account baseline.

## 5. Ambiguity Risks
- 'Always pull actual search term report' lacks fallback behavior.
- Intent scoring is not defined as a schema.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Make proposed changes the output; require approval, conflict analysis, and rollback before any write action.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Tracking & Measurement Specialist

Source: `paid-media/paid-media-tracking-specialist.md`

## 1. Current Function
Conversion tracking, tag management, attribution, and privacy-aware measurement agent.

## 2. Current Role Boundary
Audit or design conversion tracking with explicit property IDs, event taxonomy, consent rules, data quality checks, and implementation handoff.

## 3. Production Issues
- Assumes API access to verify conversion configurations and offline imports.
- Touches consent/GDPR/CCPA territory without required privacy inputs.
- No structured evidence format for discrepancies or implementation changes.

## 4. Token Waste
- Platform capability list is broad and repetitive.
- Tracking slogans obscure missing compliance contracts.

## 5. Ambiguity Risks
- 'Every conversion is counted correctly' is fake certainty.
- Tracking discrepancy thresholds are not input-driven.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Add required account/property IDs, consent regime, read-only default, and privacy validation output.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: API Tester

Source: `testing/testing-api-tester.md`

## 1. Current Function
API functional, security, performance, and contract testing agent.

## 2. Current Role Boundary
Validate API behavior against an explicit contract, auth model, test environment, and acceptance thresholds.

## 3. Production Issues
- Assumes universal 200ms p95 and 10x load requirements.
- Example tests include credentials and live requests without test-environment constraints.
- No required API contract or auth fixture inputs.

## 4. Token Waste
- Large test suite example is better as a reference.
- Broad API-testing claims repeat across sections.

## 5. Ambiguity Risks
- '95%+ coverage' is not defined by endpoint inventory.
- Security testing scope may overlap penetration testing.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into contract-driven API QA with environment, auth, and threshold inputs.

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
- Orchestration Fit: 4

Final Rating: 4.8/10


---

# Agent Review: Accessibility Auditor

Source: `testing/testing-accessibility-auditor.md`

## 1. Current Function
WCAG and assistive-technology accessibility audit agent.

## 2. Current Role Boundary
Audit accessibility against specified standards using available automated and manual evidence, then return prioritized issues and fixes.

## 3. Production Issues
- Defaults to finding issues without a clear evidence threshold.
- Requires screen reader testing even when tools or platform access may be unavailable.
- No blocked response for missing product scope, pages, or standard level.

## 4. Token Waste
- Long protocol examples can be references.
- Advocacy language repeats practical testing rules.

## 5. Ambiguity Risks
- WCAG level and jurisdiction are not required inputs.
- Manual assistive-tech evidence expectations are not tied to available tools.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep standards-based audit role, require scope/tools/standard inputs, and block when evidence is insufficient.

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

Final Rating: 4.8/10


---

# Agent Review: Product Manager

Source: `product/product-manager.md`

## 1. Current Function
Full-lifecycle product owner spanning discovery, roadmap, PRD, GTM, sprint health, and measurement.

## 2. Current Role Boundary
Coordinate product decisions by framing problems, evaluating evidence, prioritizing options, and producing scoped product artifacts.

## 3. Production Issues
- Absorbs responsibilities already covered by feedback, trend, sprint, GTM, support, and analytics agents.
- Owns the full lifecycle without explicit handoff boundaries.
- Tool access is declared but no source hierarchy or missing-data behavior is defined.

## 4. Token Waste
- Persona narrative is long relative to the missing output contract.
- Multiple artifact templates should be routed by task type.

## 5. Ambiguity Risks
- 'Own the product from idea to impact' is too broad for one execution unit.
- Evidence requirements vary by artifact but are not validated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split into product coordinator plus bounded artifact modes; route specialist inputs instead of absorbing them.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.6/10


---

# Agent Review: Threat Detection Engineer

Source: `security/security-threat-detection-engineer.md`

## 1. Current Function
Detection engineering, threat hunting, and detection-as-code agent.

## 2. Current Role Boundary
Design, validate, and maintain detection rules with explicit log-source requirements, ATT&CK mapping, false-positive profile, and deployment controls.

## 3. Production Issues
- Includes CI/CD deployment examples without required SIEM authority or deployment gates.
- Assumes log sources and historical data exist.
- No blocked response when required telemetry is missing.

## 4. Token Waste
- Long Sigma/SIEM examples should be references.
- Maturity-program language broadens beyond rule design.

## 5. Ambiguity Risks
- 'Critical technique' priority depends on threat model not required as input.
- False-positive thresholds are not environment-specific.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into detection-as-code designer with explicit telemetry, validation, and deployment-control inputs.

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

# Agent Review: Performance Benchmarker

Source: `testing/testing-performance-benchmarker.md`

## 1. Current Function
Performance testing, benchmarking, and optimization agent.

## 2. Current Role Boundary
Design and assess performance tests using explicit baselines, load profiles, environments, metrics, and non-destructive execution limits.

## 3. Production Issues
- Assumes SLA targets such as LCP and p95 without requiring product-specific thresholds.
- Example k6 load tests could target live systems without environment gates.
- No explicit non-destructive testing or rate-limit guardrails.

## 4. Token Waste
- Long k6 example should be a reference.
- Optimization claims repeat without output schema.

## 5. Ambiguity Risks
- '95% confidence' and '10x load' need dataset and environment constraints.
- Business impact estimates can be invented without analytics inputs.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into plan/evidence-first performance agent with explicit environment and safety limits.

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
