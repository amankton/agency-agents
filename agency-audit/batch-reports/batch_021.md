# Batch Summary: batch_021

## Agents Reviewed
- `engineering/engineering-codebase-onboarding-engineer.md`: Codebase Onboarding Engineer (refactor)
- `engineering/engineering-filament-optimization-specialist.md`: Filament Optimization Specialist (refactor)
- `engineering/engineering-minimal-change-engineer.md`: Minimal Change Engineer (keep)
- `engineering/engineering-mobile-app-builder.md`: Mobile App Builder (rewrite)
- `engineering/engineering-rapid-prototyper.md`: Rapid Prototyper (refactor)
- `engineering/engineering-technical-writer.md`: Technical Writer (keep)
- `game-development/blender/blender-addon-engineer.md`: Blender Add-on Engineer (keep)
- `game-development/game-audio-engineer.md`: Game Audio Engineer (refactor)
- `game-development/godot/godot-multiplayer-engineer.md`: Godot Multiplayer Engineer (refactor)
- `game-development/godot/godot-shader-developer.md`: Godot Shader Developer (refactor)

## Recommended Actions
- Keep: 3
- Refactor: 6
- Merge: 0
- Split: 0
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Mobile App Builder: the original prompt spans native iOS, native Android, cross-platform frameworks, backend synchronization, permissions, push, payments, app-store release, analytics, and device deployment without enough platform, privacy, signing, and release gates. Godot Multiplayer Engineer is the correctness runner-up because authority-model mistakes can create exploitable or unreliable netcode.

## Biggest Architecture Issue Found
Batch 021 closes the audit frontier and shows the last remaining issue class: useful specialists with strong craft knowledge but broad implementation surfaces. The engineering tail needs scoped task, source, version, and publication boundaries; the game/DCC tail needs engine/tool version, rights, profiling, and no live project or asset mutation gates.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_021.md`
- `agency-audit/refactored-agents/engineering-codebase-onboarding-engineer.md`
- `agency-audit/refactored-agents/engineering-filament-optimization-specialist.md`
- `agency-audit/refactored-agents/engineering-minimal-change-engineer.md`
- `agency-audit/refactored-agents/engineering-mobile-app-builder.md`
- `agency-audit/refactored-agents/engineering-rapid-prototyper.md`
- `agency-audit/refactored-agents/engineering-technical-writer.md`
- `agency-audit/refactored-agents/blender-addon-engineer.md`
- `agency-audit/refactored-agents/game-audio-engineer.md`
- `agency-audit/refactored-agents/godot-multiplayer-engineer.md`
- `agency-audit/refactored-agents/godot-shader-developer.md`
- `agency-audit/acceptance-tests/engineering-codebase-onboarding-engineer.tests.md`
- `agency-audit/acceptance-tests/engineering-filament-optimization-specialist.tests.md`
- `agency-audit/acceptance-tests/engineering-minimal-change-engineer.tests.md`
- `agency-audit/acceptance-tests/engineering-mobile-app-builder.tests.md`
- `agency-audit/acceptance-tests/engineering-rapid-prototyper.tests.md`
- `agency-audit/acceptance-tests/engineering-technical-writer.tests.md`
- `agency-audit/acceptance-tests/blender-addon-engineer.tests.md`
- `agency-audit/acceptance-tests/game-audio-engineer.tests.md`
- `agency-audit/acceptance-tests/godot-multiplayer-engineer.tests.md`
- `agency-audit/acceptance-tests/godot-shader-developer.tests.md`

## Subagent Inputs Used
- Engineering tail scan: kept Minimal Change Engineer and Technical Writer, refactored Codebase Onboarding, Filament Optimization, and Rapid Prototyper, and rewrote Mobile App Builder as a platform-routing role with release/privacy gates.
- Game and DCC tail scan: kept Blender Add-on Engineer, refactored Game Audio, Godot Multiplayer, and Godot Shader around middleware/native choices, server authority, renderer compatibility, dry-run/export safety, version evidence, and profiling.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Codebase Onboarding Engineer

Source: `engineering/engineering-codebase-onboarding-engineer.md`

## 1. Current Function
Read-only codebase orientation specialist for new engineers, subsystem walkthroughs, entry-point discovery, and evidence-grounded execution traces.

## 2. Current Role Boundary
Produce repository orientation maps, entry-point inventories, and code-path walkthroughs from inspected files only while labeling inference, disclosing uninspected areas, and blocking code review, refactor advice, or repo mutation unless explicitly handed off.

## 3. Production Issues
- Original prompt has strong read-only discipline but uses a rigid three-level output that can waste tokens on small questions.
- Absolute no-inference language conflicts with necessary repository classification and should become labeled inference.
- Large repos can be over-summarized if inspection scope, excluded paths, and depth are not explicit.

## 4. Token Waste
- Deep-dive sections should be optional based on requested output depth.
- Repo maps and trace tables should be generated only for the chosen scope.

## 5. Ambiguity Risks
- 'Onboard me' can mean repo map, subsystem trace, architecture walkthrough, first-contribution guide, or code review.
- Read-only orientation, implementation advice, and docs production are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around explicit inspection scope, optional depth, evidence citations, inference labels, and read-only orientation boundaries.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 8
- Token Efficiency: 6
- Maintainability: 8
- Output Consistency: 8
- Orchestration Fit: 8

Final Rating: 7.6/10


---

# Agent Review: Filament Optimization Specialist

Source: `engineering/engineering-filament-optimization-specialist.md`

## 1. Current Function
Filament PHP admin-interface specialist for resource forms, tables, navigation, relation managers, structural layout, and admin workflow optimization.

## 2. Current Role Boundary
Produce Filament resource optimization plans, field inventories, layout patches, and admin-UX validation checklists from approved Laravel/Filament project evidence while blocking production admin, database, permission, navigation, or deploy mutations without owner approval and tests.

## 3. Production Issues
- Original prompt has useful structural UX discipline but is too absolute about tabs, range sliders, icons, and field thresholds.
- Filament and Laravel APIs are version-sensitive, so examples need version gates and project-style constraints.
- Admin-panel changes can affect permissions, database relationships, production workflows, and operator error rates.

## 4. Token Waste
- Long code examples should be replaced by mode-specific snippets.
- Optimization hierarchy should produce only changes relevant to the resource being inspected.

## 5. Ambiguity Risks
- 'Optimize Filament' can mean audit, layout recommendation, code patch, relation manager refactor, permission change, or production rollout.
- UX advice, code edits, DB/schema changes, and deploy authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor by preserving structural UX expertise while adding version checks, field inventories, project-style constraints, tests, and deployment gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 7
- Token Efficiency: 5
- Maintainability: 7
- Output Consistency: 8
- Orchestration Fit: 7

Final Rating: 6.8/10


---

# Agent Review: Minimal Change Engineer

Source: `engineering/engineering-minimal-change-engineer.md`

## 1. Current Function
Surgical implementation specialist for small diffs, bug fixes, constrained feature changes, and scope-creep control.

## 2. Current Role Boundary
Deliver the smallest scoped code or documentation change that satisfies an explicit task and acceptance criteria while surfacing follow-ups separately and allowing broader investigation only when the failing behavior requires it.

## 3. Production Issues
- Original prompt is already strong and production-aligned, with excellent scope discipline.
- Some rules are too rigid for multi-file bugs or root-cause investigation that genuinely requires wider reading.
- Needs explicit acceptance criteria, allowed-files boundary, and test/failing-behavior gates.

## 4. Token Waste
- Motivational examples should be compressed in the production prompt.
- Scope self-check should be generated only when useful for the task size.

## 5. Ambiguity Risks
- 'Minimal' can mean smallest diff, shallow investigation, or refusing necessary cross-file fixes.
- Investigation scope and edit scope need separate boundaries.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep, with a small clarification that minimal surface area still allows sufficient investigation for multi-file root causes.

## 8. Merge / Split / Deprecate Recommendation
Decision: keep

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 9
- Token Efficiency: 8
- Maintainability: 9
- Output Consistency: 9
- Orchestration Fit: 9

Final Rating: 8.8/10


---

# Agent Review: Mobile App Builder

Source: `engineering/engineering-mobile-app-builder.md`

## 1. Current Function
Mobile application build coordinator for platform selection, scoped mobile implementation, offline/data architecture, native integrations, test planning, and release handoffs.

## 2. Current Role Boundary
Rewrite into a mobile delivery router and bounded implementation agent that selects native iOS, native Android, React Native, Flutter, or Expo paths from current project evidence while blocking app-store submission, signing/provisioning, production backend mutation, push/IAP/payment changes, analytics/PII collection, or device deployment without explicit approval.

## 3. Production Issues
- Original prompt is too broad across iOS, Android, React Native, Flutter, backend sync, security, stores, analytics, subscriptions, and CI/CD.
- Framework examples and platform guidance are version-sensitive and can go stale quickly.
- Mobile work can touch signing, provisioning, app stores, push notifications, in-app purchases, analytics, PII, device capabilities, and production APIs.

## 4. Token Waste
- Full Swift/Kotlin/React Native examples should move behind platform modes.
- Offline, analytics, auth, and store sections should be optional based on the product scope.

## 5. Ambiguity Risks
- 'Build mobile app' can mean platform strategy, prototype, native implementation, cross-platform implementation, release prep, or app-store launch.
- Architecture, code edits, native credentials, backend changes, and release authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as a routing and bounded implementation prompt with platform-specific modes, source dates, privacy gates, and explicit release authority.

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
- Orchestration Fit: 6

Final Rating: 5.0/10


---

# Agent Review: Rapid Prototyper

Source: `engineering/engineering-rapid-prototyper.md`

## 1. Current Function
Rapid prototype and MVP validation specialist for hypothesis testing, minimum viable flows, stack selection, and prototype-to-production handoff planning.

## 2. Current Role Boundary
Produce validation-focused prototype specs, small working proofs, experiment plans, and learning summaries from explicit hypotheses while separating prototype shortcuts from production readiness and blocking live deploy, analytics, auth, user-data, paid-service, or external-account mutation without approval.

## 3. Production Issues
- Original prompt usefully prioritizes learning but encourages auth, analytics, A/B testing, and deployment by default.
- Stack examples are dated and assume specific vendors and versions.
- Prototype-to-production claims can create false confidence if shortcuts, security, privacy, and data quality are not labeled.

## 4. Token Waste
- Boilerplate stack examples should be replaced by stack-selection criteria.
- Analytics/auth/A-B sections should be generated only when tied to the hypothesis.

## 5. Ambiguity Risks
- 'Prototype' can mean throwaway mock, user-testable MVP, production seed, low-code workflow, or live experiment.
- Learning artifact, code implementation, deployment, and production commitment are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around hypothesis gates, optional analytics/auth, prototype-versus-production labeling, and no live external-service mutation by default.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 4
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 7

Final Rating: 5.8/10


---

# Agent Review: Technical Writer

Source: `engineering/engineering-technical-writer.md`

## 1. Current Function
Developer documentation specialist for README, API reference, tutorial, conceptual guide, docs audit, style, and docs-as-code handoffs.

## 2. Current Role Boundary
Produce developer documentation, API references, READMEs, tutorials, docs audits, and maintenance plans from verified source-of-truth evidence while blocking invented code examples, unsupported claims, docs-site publication, CI changes, or repo mutation without owner approval.

## 3. Production Issues
- Original prompt is strong and broadly safe, but assumes engineer interviews, support analytics, and docs pipelines are always available.
- Large templates add token weight for small README or doc-fix tasks.
- Publishing, docs CI, versioning, and generated API references need explicit source and owner gates.

## 4. Token Waste
- Long README/OpenAPI/Docusaurus templates should be selected by doc type.
- Full content-ops sections should be optional for small docs tasks.

## 5. Ambiguity Risks
- 'Write docs' can mean audit, draft, edit existing docs, generate API reference, configure docs site, publish, or change CI.
- Drafting, code-example validation, repo edits, and publication authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep, with a lightweight mode, source-of-truth gates, and clearer separation between audit, draft, repo edit, and publication workflows.

## 8. Merge / Split / Deprecate Recommendation
Decision: keep

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 8
- Token Efficiency: 6
- Maintainability: 8
- Output Consistency: 8
- Orchestration Fit: 8

Final Rating: 7.6/10


---

# Agent Review: Blender Add-on Engineer

Source: `game-development/blender/blender-addon-engineer.md`

## 1. Current Function
Blender Python tooling specialist for add-ons, operators, panels, validators, exporters, batch processing, asset-pipeline checks, and artist workflow automation.

## 2. Current Role Boundary
Produce Blender add-on specs, scoped Python/bpy implementation plans, asset validation checklists, exporter dry runs, and pipeline handoffs from approved scene evidence while blocking destructive rename/delete/apply/export overwrite, path writes, or source-control mutation without explicit approval.

## 3. Production Issues
- Original prompt is solid and already emphasizes non-destructive Blender workflow.
- Example exporter needs stronger path validation, dry-run behavior, source preservation, and add-on registration gates.
- Blender API and export behavior are version-sensitive and should be scoped to target engine/export format.

## 4. Token Waste
- Asset validator and exporter examples should be generated only by tool scope.
- Long advanced sections should be compressed in production prompt.

## 5. Ambiguity Risks
- 'Build Blender add-on' can mean spec, validation script, exporter, UI panel, batch tool, actual file writes, or production pipeline adoption.
- Validation, auto-fix, export, destructive cleanup, and source-control authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep with tightened Blender version, dry-run, path-validation, source-preservation, and explicit asset/export mutation gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: keep

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 8
- Token Efficiency: 7
- Maintainability: 8
- Output Consistency: 8
- Orchestration Fit: 8

Final Rating: 7.8/10


---

# Agent Review: Game Audio Engineer

Source: `game-development/game-audio-engineer.md`

## 1. Current Function
Interactive game-audio specialist for FMOD, Wwise, native engine audio, adaptive music, spatial audio, performance budgets, and audio implementation handoffs.

## 2. Current Role Boundary
Produce interactive audio architecture, middleware/native-engine implementation specs, audio budgets, adaptive music plans, spatial-audio QA notes, and engine handoffs from approved project evidence while blocking asset import, middleware project mutation, mix changes, build changes, or platform certification claims without owner approval.

## 3. Production Issues
- Original prompt is strong but too absolute that all audio must use FMOD/Wwise, which may not fit small projects, Godot/native audio, or prototypes.
- Compression, voice-limit, and platform rules need engine, middleware, platform, and hardware gates.
- Audio work can mutate middleware projects, engine integration code, asset imports, mix buses, and build/certification settings.

## 4. Token Waste
- FMOD/Wwise/native examples should be selected by middleware choice.
- Budget tables and parameter specs should be generated only for relevant content categories.

## 5. Ambiguity Risks
- 'Do game audio' can mean sound design, middleware architecture, code integration, budget spec, mix review, asset import, or certification readiness.
- Creative direction, implementation, asset mutation, and performance certification are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor to preserve middleware expertise while making native engine audio a first-class fallback and gating budgets, assets, runtime ownership, and mix/build changes.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 7
- Token Efficiency: 6
- Maintainability: 7
- Output Consistency: 7
- Orchestration Fit: 8

Final Rating: 7.0/10


---

# Agent Review: Godot Multiplayer Engineer

Source: `game-development/godot/godot-multiplayer-engineer.md`

## 1. Current Function
Godot networking specialist for MultiplayerAPI, ENet/WebRTC, RPCs, scene replication, authority models, lobby/matchmaking handoffs, and latency/security testing.

## 2. Current Role Boundary
Produce Godot multiplayer architecture, authority maps, RPC/security reviews, replication plans, latency-test plans, and backend handoffs from approved Godot project evidence while blocking contradictory authority patterns, insecure RPCs, production networking code mutation, backend/server deploy, or release claims without approval.

## 3. Production Issues
- Original prompt contains an internal contradiction between server-owned gameplay state and sample authority assigned to client peer IDs.
- Examples blur client input collection, server simulation, RPC context, and replicated state, which can teach fragile netcode patterns.
- Godot multiplayer work can touch backend services, server deployment, cheat surfaces, player data, and release reliability.

## 4. Token Waste
- ENet, WebRTC, lobby, relay, and protocol sections should be selected by topology.
- Examples should be shorter and source-versioned.

## 5. Ambiguity Risks
- 'Build Godot multiplayer' can mean architecture, server-authoritative loop, P2P variant, RPC review, lobby backend, latency test, or deployment.
- Architecture, code mutation, backend ownership, and release readiness are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with a server-authoritative baseline, explicit authority tables, source-dated Godot version gates, and separate optional P2P/client-authority variants.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 6
- Maintainability: 6
- Output Consistency: 6
- Orchestration Fit: 8

Final Rating: 6.4/10


---

# Agent Review: Godot Shader Developer

Source: `game-development/godot/godot-shader-developer.md`

## 1. Current Function
Godot rendering and shader specialist for CanvasItem, Spatial, VisualShader, post-processing, renderer compatibility, and shader performance review.

## 2. Current Role Boundary
Produce Godot shader specs, scoped shader/material plans, renderer compatibility reviews, performance budgets, and VFX handoffs from approved visual references while blocking misleading renderer claims, material/scene mutation, mobile GPU regressions, or project setting changes without version validation and approval.

## 3. Production Issues
- Original prompt is strong but some renderer/depth/post-process claims need Godot-version verification.
- Heavy shader examples create token cost and can be misleading when renderer target or platform budget is unknown.
- Shader work can mutate materials, scenes, project rendering settings, imported textures, and mobile performance characteristics.

## 4. Token Waste
- Shader examples should be selected by shader type and renderer target.
- Deep post-processing and compute sections should be optional.

## 5. Ambiguity Risks
- 'Create Godot shader' can mean spec, code shader, VisualShader graph, material setup, post-process, performance audit, or scene/project mutation.
- VFX design, shader implementation, renderer settings, and performance signoff are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with compressed examples, source-versioned renderer notes, platform budgets, and explicit material/scene/project mutation gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 7
- Token Efficiency: 6
- Maintainability: 7
- Output Consistency: 7
- Orchestration Fit: 8

Final Rating: 7.0/10
