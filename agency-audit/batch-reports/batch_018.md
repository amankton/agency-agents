# Batch Summary: batch_018

## Agents Reviewed
- `spatial-computing/xr-cockpit-interaction-specialist.md`: XR Cockpit Interaction Specialist (merge)
- `specialized/specialized-document-generator.md`: Document Generator (refactor)
- `specialized/sales-data-extraction-agent.md`: Sales Data Extraction Agent (refactor)
- `support/support-executive-summary-generator.md`: Executive Summary Generator (refactor)
- `engineering/engineering-orgscript-engineer.md`: OrgScript Engineer (split)
- `spatial-computing/terminal-integration-specialist.md`: Terminal Integration Specialist (refactor)
- `marketing/marketing-reddit-community-builder.md`: Reddit Community Builder (refactor)
- `marketing/marketing-carousel-growth-engine.md`: Carousel Growth Engine (rewrite)
- `specialized/specialized-developer-advocate.md`: Developer Advocate (split)
- `spatial-computing/macos-spatial-metal-engineer.md`: macOS Spatial/Metal Engineer (split)

## Recommended Actions
- Keep: 0
- Refactor: 5
- Merge: 1
- Split: 3
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Carousel Growth Engine: the original prompt directs zero-confirmation scraping, image generation, public TikTok/Instagram publishing, analytics retrieval, persistent learning, and self-scheduling through external APIs. That combination creates account, rights, credential, privacy, spam, claims, and brand-risk exposure. Sales Data Extraction is the data runner-up because uncontrolled file watchers and database writes can corrupt reporting.

## Biggest Architecture Issue Found
Batch 018 exposes medium-priority prompts that still cross hard boundaries: generated documents can leak or overwrite data, sales ETL can write bad metrics, executive summaries can invent unsupported commitments, terminal and Metal agents can touch devices/sessions, and community/growth agents can act publicly. The fix is draft/local/staging by default, with source lineage, version validation, rights, privacy, accessibility, owner approval, and no-public-action gates.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_018.md`
- `agency-audit/refactored-agents/xr-cockpit-interaction-specialist.md`
- `agency-audit/refactored-agents/specialized-document-generator.md`
- `agency-audit/refactored-agents/sales-data-extraction-agent.md`
- `agency-audit/refactored-agents/support-executive-summary-generator.md`
- `agency-audit/refactored-agents/engineering-orgscript-engineer.md`
- `agency-audit/refactored-agents/terminal-integration-specialist.md`
- `agency-audit/refactored-agents/marketing-reddit-community-builder.md`
- `agency-audit/refactored-agents/marketing-carousel-growth-engine.md`
- `agency-audit/refactored-agents/specialized-developer-advocate.md`
- `agency-audit/refactored-agents/macos-spatial-metal-engineer.md`
- `agency-audit/acceptance-tests/xr-cockpit-interaction-specialist.tests.md`
- `agency-audit/acceptance-tests/specialized-document-generator.tests.md`
- `agency-audit/acceptance-tests/sales-data-extraction-agent.tests.md`
- `agency-audit/acceptance-tests/support-executive-summary-generator.tests.md`
- `agency-audit/acceptance-tests/engineering-orgscript-engineer.tests.md`
- `agency-audit/acceptance-tests/terminal-integration-specialist.tests.md`
- `agency-audit/acceptance-tests/marketing-reddit-community-builder.tests.md`
- `agency-audit/acceptance-tests/marketing-carousel-growth-engine.tests.md`
- `agency-audit/acceptance-tests/specialized-developer-advocate.tests.md`
- `agency-audit/acceptance-tests/macos-spatial-metal-engineer.tests.md`

## Subagent Inputs Used
- Spatial/tooling scan: recommended merging XR Cockpit into XR Interface Architect, refactoring Terminal Integration, splitting macOS Spatial/Metal and OrgScript, and splitting Developer Advocate around public-action and version gates.
- Document/data/community scan: recommended refactoring Document Generator, Sales Data Extraction, Executive Summary, and Reddit Community Builder while rewriting Carousel Growth as draft-only due autonomous publish/schedule/API risk.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: XR Cockpit Interaction Specialist

Source: `spatial-computing/xr-cockpit-interaction-specialist.md`

## 1. Current Function
Legacy cockpit-specific XR interaction role for seated control layouts, spatial dashboards, input constraints, comfort checks, and platform implementation handoffs.

## 2. Current Role Boundary
Merge the standalone XR Cockpit Interaction Specialist into XR Interface Architect as a cockpit-mode design pattern that produces seated XR cockpit interaction specs, control maps, comfort notes, and implementation handoffs while blocking direct simulator, vehicle, sensor, or production XR deployment work without platform-owner validation.

## 3. Production Issues
- Original prompt blends cockpit UX design with A-Frame/Three.js implementation and simulator-style control mechanics.
- Cockpit XR work can affect comfort, accessibility, spatial safety, sensor privacy, and simulator training fidelity.
- Overlaps XR Interface Architect, XR Immersive Developer, visionOS Spatial Engineer, Technical Artist, and Accessibility Auditor.

## 4. Token Waste
- Cockpit patterns should be a mode of XR Interface Architect, not a full duplicate role.
- Implementation details should route to engine/platform agents only when scoped.

## 5. Ambiguity Risks
- 'Build cockpit controls' can mean a UX spec, prototype, simulator integration, device input mapping, or live training environment change.
- Design authority, implementation authority, and validation authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Merge cockpit-specific design into XR Interface Architect as a mode and route implementation to platform agents with comfort, accessibility, privacy, and validation gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: merge

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 8
- Maintainability: 5
- Output Consistency: 3
- Orchestration Fit: 3

Final Rating: 4.6/10


---

# Agent Review: Document Generator

Source: `specialized/specialized-document-generator.md`

## 1. Current Function
Programmatic document-generation specialist for code-created PDFs, slide decks, spreadsheets, Word documents, charts, templates, accessibility, and artifact handoffs.

## 2. Current Role Boundary
Produce PDF, PPTX, DOCX, XLSX, and report-generation scripts or artifacts from approved source data, templates, brand assets, and output paths while blocking unsupported claims, confidential-data leakage, file overwrites, external distribution, signatures, submissions, or publication without owner approval.

## 3. Production Issues
- Original prompt focuses on document creation tools but lacks source-data, rights, confidentiality, overwrite, accessibility, and distribution gates.
- Generated documents can contain confidential data, regulated claims, brand assets, financial/legal statements, or stale metrics.
- Overlaps Content Creator, Technical Writer, Brand Guardian, Analytics Reporter, Legal/Compliance, and office-document tooling owners.

## 4. Token Waste
- Library guidance should be selected by target format and runtime.
- Full generation scripts should appear only when artifact generation is in scope.

## 5. Ambiguity Risks
- 'Generate a professional document' can mean draft script, create local artifact, overwrite a file, send a document, or submit a formal deliverable.
- Artifact creation, content approval, and external distribution are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as artifact-only document generation with format contracts, source/rights/confidentiality gates, accessibility checks, output-path controls, and no distribution by default.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 7
- Maintainability: 6
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 5.8/10


---

# Agent Review: Sales Data Extraction Agent

Source: `specialized/sales-data-extraction-agent.md`

## 1. Current Function
Sales ETL intake specialist for Excel metric extraction, schema mapping, idempotent import design, audit logs, staging validation, and downstream reporting handoffs.

## 2. Current Role Boundary
Produce governed sales-metric extraction specs, dry-run parsers, staging import plans, reconciliation reports, and event contracts for approved Excel sources while blocking uncontrolled file watchers, production database writes, duplicate imports, representative matching changes, or downstream event emission without Sales Ops, data, privacy, and DBA approval.

## 3. Production Issues
- Original prompt describes real-time directory monitoring, fuzzy Excel parsing, representative matching, PostgreSQL inserts, and downstream events without authority gates.
- Sales data extraction can corrupt metrics, duplicate imports, expose PII, misattribute reps, and trigger downstream reports from bad data.
- Overlaps Data Engineer, Data Consolidation Agent, Database Optimizer, Salesforce Architect, Sales Ops, RevOps, and Privacy Reviewer.

## 4. Token Waste
- File-watcher and database-write logic should be generated only when implementation authority is explicit.
- Metric mapping should be declarative and source-specific.

## 5. Ambiguity Risks
- 'Monitor files' can mean design a pipeline, run a local dry-run, install a watcher, write to staging, or mutate production reporting tables.
- Extraction, validation, persistence, and event emission are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into governed ETL intake with dry-run/staging defaults, idempotent imports, reconciliation, PII controls, and explicit downstream event contracts.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 7
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 5.2/10


---

# Agent Review: Executive Summary Generator

Source: `support/support-executive-summary-generator.md`

## 1. Current Function
Executive-communication specialist for source-grounded SCQA briefs, key findings, impact summaries, recommendation drafts, uncertainty labels, and decision handoffs.

## 2. Current Role Boundary
Produce concise executive summaries from approved source packets, metrics, and decision context while blocking invented numbers, unsupported recommendations, owner/timeline commitments, confidential disclosure, or executive decision substitution when evidence is incomplete.

## 3. Production Issues
- Original prompt forces quantified findings and owner/timeline recommendations even when source evidence may be insufficient.
- Executive summaries can overstate certainty, invent metrics, expose confidential data, or imply decisions the source packet does not support.
- Overlaps Business Strategist, Chief of Staff, Analytics Reporter, Finance Tracker, Product Manager, and Evidence Collector.

## 4. Token Waste
- Consulting-framework detail should be compressed unless the user asks for method explanation.
- Templates should be selected by executive artifact type and evidence quality.

## 5. Ambiguity Risks
- 'Write for executives' can mean summarize evidence, recommend actions, assign owners, or make a decision.
- Briefing, decision recommendation, and authority to commit resources are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as a source-grounded executive brief role with insufficient-evidence outputs, metric lineage, confidentiality labels, and no unsupported commitments.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 5
- Maintainability: 6
- Output Consistency: 7
- Orchestration Fit: 6

Final Rating: 6.0/10


---

# Agent Review: OrgScript Engineer

Source: `engineering/engineering-orgscript-engineer.md`

## 1. Current Function
OrgScript DSL specialist for parser/linter/formatter/CLI work and business-process modeling with grammar/version validation and workflow-owner handoffs.

## 2. Current Role Boundary
Split OrgScript work into toolchain engineering and process-modeling modes that produce grammar-aware code changes, .orgs models, validators, diagnostics, and export artifacts only from approved specs/SOPs while blocking unsupported language constructs, automation deployment, repo mutation, or business-policy commitments without owner approval.

## 3. Production Issues
- Original prompt combines parser/toolchain engineering with business-process modeling and assumes local grammar and CLI commands exist.
- OrgScript outputs can encode business rules, trigger automation, or alter parser semantics used by downstream AI workflows.
- Overlaps Workflow Architect, Senior Developer, Evidence Collector, Technical Writer, Product Manager, and process owners.

## 4. Token Waste
- Grammar examples and implementation guidance should be generated by mode.
- Process-model templates should be concise unless the source SOP requires expansion.

## 5. Ambiguity Risks
- 'Implement OrgScript' can mean edit parser code, draft a process model, run validation, export Mermaid, or deploy automation.
- Toolchain changes and business-policy modeling are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split into OrgScript Toolchain Engineer and OrgScript Process Modeler modes sharing grammar/version, validation, edit, export, and process-owner gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 7
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 5.4/10


---

# Agent Review: Terminal Integration Specialist

Source: `spatial-computing/terminal-integration-specialist.md`

## 1. Current Function
SwiftTerm terminal integration specialist for Apple-platform terminal rendering, input handling, scrollback, SSH I/O bridging specs, accessibility, and performance handoffs.

## 2. Current Role Boundary
Produce SwiftTerm terminal-emulation integration specs, scoped code guidance, rendering/performance test plans, and accessibility handoffs for approved Apple-platform apps while blocking SSH credential handling, shell process control, clipboard mutation, live session recording, or production app changes without security, repo, and release approval.

## 3. Production Issues
- Original prompt is useful but lacks version gates, security boundaries, structured outputs, and explicit PTY/SSH/process I/O authority.
- Terminal integration can expose shell output, credentials, clipboard data, SSH sessions, command streams, and accessibility-sensitive text.
- Overlaps Senior Developer, API Tester, Accessibility Auditor, Performance Benchmarker, Application Security Engineer, and Apple platform owners.

## 4. Token Waste
- SwiftTerm and terminal-protocol detail should be selected by task type.
- General ANSI/VT100 explanations should be omitted unless relevant to the bug or feature.

## 5. Ambiguity Risks
- 'Integrate terminal' can mean UI spec, local code change, SSH session bridge, process execution, clipboard support, or production release.
- Rendering guidance, security-sensitive I/O, and release authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as narrow SwiftTerm integration with versioned API gates, PTY/SSH security constraints, accessibility/performance checks, and explicit process-I/O authority.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 7
- Maintainability: 6
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 5.8/10


---

# Agent Review: Reddit Community Builder

Source: `marketing/marketing-reddit-community-builder.md`

## 1. Current Function
Reddit community strategy specialist for subreddit research, value-first content planning, draft engagement, reputation monitoring, AMA preparation, and platform-risk handoffs.

## 2. Current Role Boundary
Produce Reddit community research, strategy, draft engagement plans, AMA prep, monitoring summaries, and crisis-escalation handoffs from approved subreddit, brand, and disclosure context while blocking posting, commenting, voting, DMing, moderator outreach, ads, astroturfing, or reputation actions without account-owner and legal/comms approval.

## 3. Production Issues
- Original prompt emphasizes authentic engagement but includes community participation, monitoring, AMAs, ads, and reputation responses without account/action gates.
- Reddit work can become spam, undisclosed affiliation, brigading, platform bans, unsupported claims, or crisis escalation.
- Overlaps Social Media Strategist, Content Creator, Multi-Platform Publisher, Paid Social Strategist, PR & Communications, Support Responder, and Legal/Compliance.

## 4. Token Waste
- Karma and engagement targets should be replaced with evidence-based health metrics.
- Subreddit and AMA templates should be selected by scope.

## 5. Ambiguity Risks
- 'Build Reddit community' can mean strategy, drafting, monitoring, live comments, moderator outreach, ads, or crisis response.
- Strategy, account engagement, paid promotion, and support/comms response are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as Reddit strategy and draft-engagement planning with live posts, replies, AMAs, ads, and reputation actions gated by account-owner approval.

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

# Agent Review: Carousel Growth Engine

Source: `marketing/marketing-carousel-growth-engine.md`

## 1. Current Function
Draft-only carousel creative and analytics-learning specialist for TikTok/Instagram slide briefs, website evidence extraction, prompt plans, visual QA checklists, captions, and publisher handoffs.

## 2. Current Role Boundary
Rewrite the autonomous carousel growth engine into a draft-only carousel creative, compliance, and analytics-learning specialist that produces source-grounded slide briefs, prompts, QA reports, captions, and proposed learning notes while blocking scraping beyond approved URLs, image generation without rights review, API credential use, public posting, music selection, scheduling, cron loops, or analytics retention without explicit platform-owner approval.

## 3. Production Issues
- Original prompt instructs zero-confirmation website scraping, Gemini image generation, direct TikTok/Instagram publishing, analytics fetching, learning storage, and self-scheduling.
- Autonomous social publishing can misuse credentials/APIs, scrape unauthorized content, violate rights, publish misleading claims, use unlicensed music, damage accounts, or retain analytics/PII.
- Overlaps Content Creator, Social Media Strategist, Instagram Curator, TikTok Strategist, Short-Video Editing Coach, Multi-Platform Publisher, Brand Guardian, Legal/Privacy, and account owners.

## 4. Token Waste
- Hardcoded API scripts, model names, endpoints, and cron behavior should be removed from the prompt.
- Carousel structure should be a reusable mode, not a mandate to publish.

## 5. Ambiguity Risks
- 'Generate and publish a carousel' can mean brief, draft assets, generated images, scheduled post, public feed upload, analytics fetch, or persistent learning loop.
- Creative drafting, generation, publishing, analytics, and scheduling authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite into draft-only carousel creative and analytics learning; publishing, scheduling, music, credentials, generation, and account actions route to approved platform owners.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 2
- Token Efficiency: 3
- Maintainability: 2
- Output Consistency: 3
- Orchestration Fit: 1

Final Rating: 2.2/10


---

# Agent Review: Developer Advocate

Source: `specialized/specialized-developer-advocate.md`

## 1. Current Function
Developer relations specialist for DX audits, technical content specs, sample-app plans, community engagement drafts, developer feedback synthesis, and product handoffs.

## 2. Current Role Boundary
Split Developer Advocate into DX audit, technical content, community engagement, and voice-of-developer modes that produce evidence-backed artifacts, tested sample-code plans, community-response drafts, and product feedback while blocking public posting, issue replies, roadmap commitments, event outreach, code publication, or community-data retention without disclosure, privacy, product, and account approval.

## 3. Production Issues
- Original prompt spans DX engineering, technical content, community response, ambassador programs, events, roadmap communication, and product feedback in one role.
- DevRel work can publish inaccurate code, expose secrets, overpromise roadmap items, mishandle community PII, or publicly represent the company without approval.
- Overlaps Technical Writer, Product Feedback Synthesizer, Product Manager, Content Creator, Reddit Community Builder, Application Security Engineer, and Support.

## 4. Token Waste
- DX audit, tutorial, community, and roadmap templates should be mode-specific.
- Extensive content templates should appear only when requested.

## 5. Ambiguity Risks
- 'Advocate for developers' can mean internal synthesis, content drafting, sample app implementation, public issue response, event work, or roadmap messaging.
- Internal evidence work, code publication, and public engagement authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split DevRel into DX audit, technical content, community engagement, and voice-of-developer modes with no-public-action, code-test, disclosure, privacy, and roadmap gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.8/10


---

# Agent Review: macOS Spatial/Metal Engineer

Source: `spatial-computing/macos-spatial-metal-engineer.md`

## 1. Current Function
Apple-platform Metal rendering and spatial-computing specialist for macOS/visionOS performance specs, rendering pipelines, profiling plans, comfort constraints, and platform-agent handoffs.

## 2. Current Role Boundary
Split macOS Spatial/Metal work into Metal rendering/performance and visionOS spatial-integration handoff modes that produce version-gated architecture, profiling, shader/rendering, comfort, and implementation artifacts while blocking unsupported platform claims, unrealistic frame-rate guarantees, asset/sensor misuse, device deployment, or production builds without Apple-platform, security, accessibility, and release approval.

## 3. Production Issues
- Original prompt includes aggressive 90fps/25k-node defaults, large embedded examples, and platform claims that may be stale or hardware-dependent.
- Metal/spatial work can affect device performance, thermal limits, sensor privacy, accessibility, asset rights, and production app stability.
- Overlaps visionOS Spatial Engineer, XR Interface Architect, XR Immersive Developer, Technical Artist, Performance Benchmarker, and Senior Developer.

## 4. Token Waste
- Large Metal and Compositor code blocks should be replaced by version-gated implementation contracts.
- Performance targets should be input-driven, not hardcoded.

## 5. Ambiguity Risks
- 'Build spatial Metal renderer' can mean architecture, shader prototype, profiling, visionOS integration, device test, or production build.
- Rendering/performance ownership and visionOS spatial integration are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split Metal rendering/performance ownership from visionOS spatial integration with source/version gates, input-driven performance targets, profiling evidence, and release boundaries.

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
