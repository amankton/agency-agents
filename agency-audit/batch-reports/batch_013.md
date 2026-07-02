# Batch Summary: batch_013

## Agents Reviewed
- `game-development/game-designer.md`: Game Designer (refactor)
- `game-development/level-designer.md`: Level Designer (refactor)
- `game-development/narrative-designer.md`: Narrative Designer (refactor)
- `game-development/technical-artist.md`: Technical Artist (split)
- `game-development/unity/unity-architect.md`: Unity Architect (refactor)
- `game-development/unreal-engine/unreal-systems-engineer.md`: Unreal Systems Engineer (split)
- `game-development/godot/godot-gameplay-scripter.md`: Godot Gameplay Scripter (refactor)
- `spatial-computing/xr-interface-architect.md`: XR Interface Architect (rewrite)
- `spatial-computing/xr-immersive-developer.md`: XR Immersive Developer (refactor)
- `spatial-computing/visionos-spatial-engineer.md`: visionOS Spatial Engineer (refactor)

## Recommended Actions
- Keep: 0
- Refactor: 7
- Merge: 0
- Split: 2
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Unreal Systems Engineer: it combines fast-moving engine-feature claims, C++/Blueprint boundaries, GAS networking, rendering, Nanite/Lumen, Mass, Chaos, build tooling, and performance guidance. Wrong or stale advice can push expensive engine-level refactors or unsafe build changes. Technical Artist is the closest runner-up because it spans assets, shaders, VFX, DCC scripts, profiling, and licensing.

## Biggest Architecture Issue Found
Game, engine, and spatial roles blend artifact production with editor, asset, code, build, device, and platform mutation. Batch 013 separates design specs from implementation, requires source/version validation for engine and platform facts, and gates live scene, asset, build, app-store, device, sensor-data, publishing, and unlicensed-asset actions.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_013.md`
- `agency-audit/refactored-agents/game-designer.md`
- `agency-audit/refactored-agents/level-designer.md`
- `agency-audit/refactored-agents/narrative-designer.md`
- `agency-audit/refactored-agents/technical-artist.md`
- `agency-audit/refactored-agents/unity-architect.md`
- `agency-audit/refactored-agents/unreal-systems-engineer.md`
- `agency-audit/refactored-agents/godot-gameplay-scripter.md`
- `agency-audit/refactored-agents/xr-interface-architect.md`
- `agency-audit/refactored-agents/xr-immersive-developer.md`
- `agency-audit/refactored-agents/visionos-spatial-engineer.md`
- `agency-audit/acceptance-tests/game-designer.tests.md`
- `agency-audit/acceptance-tests/level-designer.tests.md`
- `agency-audit/acceptance-tests/narrative-designer.tests.md`
- `agency-audit/acceptance-tests/technical-artist.tests.md`
- `agency-audit/acceptance-tests/unity-architect.tests.md`
- `agency-audit/acceptance-tests/unreal-systems-engineer.tests.md`
- `agency-audit/acceptance-tests/godot-gameplay-scripter.tests.md`
- `agency-audit/acceptance-tests/xr-interface-architect.tests.md`
- `agency-audit/acceptance-tests/xr-immersive-developer.tests.md`
- `agency-audit/acceptance-tests/visionos-spatial-engineer.tests.md`

## Subagent Inputs Used
- Game/creative scan: refactor Game Designer, Level Designer, Narrative Designer, and Godot Gameplay Scripter; split Technical Artist around pipeline governance versus engine-specific implementation.
- Engine/spatial scan: refactor Unity Architect, XR Immersive Developer, and visionOS Spatial Engineer; split Unreal Systems Engineer around gameplay/GAS versus rendering/performance; rewrite XR Interface Architect as a spatial UX spec agent.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Game Designer

Source: `game-development/game-designer.md`

## 1. Current Function
Game design specialist for mechanics, core loops, progression, economy specifications, onboarding flows, tuning hypotheses, and designer-to-engineering handoffs.

## 2. Current Role Boundary
Produce scoped gameplay, mechanic, loop, progression, economy, onboarding, and GDD artifacts from supplied design pillars and constraints while labeling all tuning values as hypotheses and blocking code implementation, analytics changes, economy configuration, manipulative monetization, or live content changes without approval.

## 3. Production Issues
- Original prompt spans mechanics, economies, onboarding, behavioral economics, retention, and cross-genre design across all genres without enough project scope or authority boundaries.
- Economy and retention guidance can drift into manipulative monetization, dark patterns, or unsupported numeric certainty if ethics and playtest gates are absent.
- Overlaps Level Designer, Narrative Designer, Product Manager, Data Analyst, Monetization, and engine gameplay implementers.

## 4. Token Waste
- Long GDD templates should be selected by game-design mode and supplied project context.
- Behavioral and economy sections should become optional bounded modules.

## 5. Ambiguity Risks
- 'Balance with data' can imply validated values when only hypotheses exist.
- Design authority, implementation authority, and monetization approval are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into scoped GDD modes with required project inputs, placeholder-value labeling, ethical monetization limits, playtest criteria, and structured engineering handoffs.

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

# Agent Review: Level Designer

Source: `game-development/level-designer.md`

## 1. Current Function
Level design specialist for spatial flow, critical-path readability, encounter pacing, blockout specs, environmental storytelling briefs, and art/engineering handoffs.

## 2. Current Role Boundary
Produce level layout, pacing, encounter, navigation, blockout, and environmental-storytelling specifications from supplied mechanics and constraints while defaulting to draft artifacts and blocking direct engine scene edits, art locks, fairness claims, or performance decisions without playtest and owner approval.

## 3. Production Issues
- Original prompt assumes blockout, screenshot, and editor workflows without declaring whether engine tools or scene files are available.
- Readability, encounter fairness, and pacing claims require playtest evidence, accessibility context, and target input/camera constraints.
- Overlaps Game Designer, Narrative Designer, Technical Artist, Environment Art, QA, and engine/world-building implementers.

## 4. Token Waste
- Large level templates should be generated only when a level mode and artifact type are requested.
- Advanced procedural/speedrun/multiplayer guidance should be optional modules.

## 5. Ambiguity Risks
- 'Design levels' can mean paper spec, greybox edit, encounter tuning, or final art pass.
- Art direction, gameplay-critical geometry, and performance ownership are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with a strict level-spec output contract, read-only default, playtest evidence fields, accessibility/readability checks, and art/engineering handoff boundaries.

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
- Orchestration Fit: 4

Final Rating: 5.4/10


---

# Agent Review: Narrative Designer

Source: `game-development/narrative-designer.md`

## 1. Current Function
Narrative design specialist for story systems, branching dialogue, world bible consistency, character voice, lore maps, environmental story briefs, and narrative-gameplay handoffs.

## 2. Current Role Boundary
Produce narrative architecture, dialogue, branching, lore, character voice, and environmental-storytelling artifacts from supplied canon and project constraints while blocking IP clearance claims, real-person likeness use, live transmedia publication, engine implementation, or rating/localization approval without owner review.

## 3. Production Issues
- Original prompt is strong creatively but lacks a source-of-truth hierarchy for canon, world bible, IP constraints, and content-rating limits.
- Transmedia, ARG, real-person, localization, and social-media narrative ideas can create publication, privacy, cultural, or IP risk.
- Overlaps Game Designer, Level Designer, Content Creator, Cultural Intelligence, Localization, Legal/IP Review, and dialogue implementation roles.

## 4. Token Waste
- Dialogue, lore, branch, and environmental templates should be selected by artifact type.
- Advanced systemic/transmedia sections should become gated optional modes.

## 5. Ambiguity Risks
- 'Implement narrative systems' can mean authoring artifacts or changing engine dialogue tooling.
- Canon authority, IP clearance, content rating, and publication authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with source-of-truth hierarchy, IP/rating/localization gates, branch-complexity limits, engine-ready schemas, and live-publication blocks.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 5
- Maintainability: 5
- Output Consistency: 6
- Orchestration Fit: 4

Final Rating: 5.0/10


---

# Agent Review: Technical Artist

Source: `game-development/technical-artist.md`

## 1. Current Function
Technical art specialist for asset budgets, shader/VFX planning, LOD and compression standards, rendering performance analysis, DCC/editor validation tooling, and art-to-engine handoffs.

## 2. Current Role Boundary
Prepare art-pipeline budgets, shader/VFX specs, asset-validation rules, profiling findings, and implementation handoffs while separating pipeline governance from engine-specific shader/tool execution and blocking live asset, DCC, import, repo, or build mutations without sandboxed approval and rollback.

## 3. Production Issues
- Original prompt combines visual standards, shader/VFX implementation, asset pipeline governance, profiling, DCC scripts, ML upscaling, and tooling across multiple engines.
- A bad technical-art action can break builds, corrupt assets, regress GPU performance, violate platform budgets, or introduce unlicensed/AI-derived asset risk.
- Overlaps Unity/Unreal/Godot engineers, rendering engineers, environment art, build/CI, performance QA, legal/IP review, and asset pipeline owners.

## 4. Token Waste
- Asset-budget, shader, VFX, profiling, and tooling sections should be separate modes.
- Cross-engine examples should be generated only for the declared engine and pipeline.

## 5. Ambiguity Risks
- 'Build tools' and 'write shaders' can mean advisory snippets or repo/editor mutation.
- Pipeline governance and engine-specific implementation authority are mixed.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split pipeline-budget/audit authority from engine-scoped shader, VFX, and tooling implementation with sandbox, profiling, rights, approval, and rollback gates.

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
- Orchestration Fit: 4

Final Rating: 4.2/10


---

# Agent Review: Unity Architect

Source: `game-development/unity/unity-architect.md`

## 1. Current Function
Unity architecture specialist for modular component design, ScriptableObject patterns, prefab/scene dependencies, designer workflow, package choices, and scoped Unity gameplay architecture handoffs.

## 2. Current Role Boundary
Produce Unity architecture, refactor, data-lifecycle, ScriptableObject, prefab, scene, package, and implementation handoff artifacts for a scoped Unity version/project while avoiding absolutist pattern mandates, project-wide rewrites, build/release changes, or live asset/scene mutations without tests and approval.

## 3. Production Issues
- Original prompt over-mandates ScriptableObjects and contains pattern tensions around runtime scene references, mutable SO state, and editor persistence.
- Unity architecture depends heavily on version, project scale, target platforms, packages, save/networking requirements, and designer workflow.
- Overlaps Unity gameplay engineers, technical designers, technical artists, build/release owners, Addressables/DOTS specialists, and code reviewers.

## 4. Token Waste
- Large code examples should be emitted only for requested patterns.
- ScriptableObject doctrine should become a decision tree.

## 5. Ambiguity Risks
- 'Architect' can mean advisory ADR, implementation patch, or project-wide refactor.
- Runtime SO state, scene references, build settings, and release authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with a Unity-versioned decision tree, runtime-data lifecycle rules, scoped repo/change boundaries, tests, and compact architecture output contracts.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 4
- Maintainability: 6
- Output Consistency: 7
- Orchestration Fit: 6

Final Rating: 5.8/10


---

# Agent Review: Unreal Systems Engineer

Source: `game-development/unreal-engine/unreal-systems-engineer.md`

## 1. Current Function
Unreal Engine systems specialist for UE gameplay architecture, C++/Blueprint boundaries, GAS/network replication, rendering/performance constraints, module dependencies, and source-validated implementation handoffs.

## 2. Current Role Boundary
Produce version-gated Unreal Engine systems, GAS, C++/Blueprint, networking, rendering, Nanite/Lumen, performance, module, and build artifacts while splitting gameplay/GAS engineering from rendering/performance engineering and blocking stale engine claims, broad refactors, build-tool mutation, or live project changes without official-source validation and approval.

## 3. Production Issues
- Original prompt combines GAS, C++ architecture, Blueprint policy, Nanite/Lumen, Mass, Chaos, Lyra, build tooling, and performance across fast-moving Unreal versions.
- Confident hard rules about engine features can become stale and drive expensive or wrong engine-level refactors.
- Overlaps Unreal gameplay engineers, GAS specialists, rendering technical artists, build engineers, multiplayer engineers, performance QA, and platform certification owners.

## 4. Token Waste
- GAS, rendering, Mass/Chaos, Lyra, and build examples should be selected only for the declared mode.
- Engine facts should be version-gated rather than memorized as universal rules.

## 5. Ambiguity Risks
- 'Systems Engineer' can mean gameplay/GAS implementation, rendering optimization, architecture ADR, or build-system mutation.
- Designer-facing Blueprint policy and C++ implementation authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split into Unreal Gameplay/GAS and Unreal Rendering/Performance modes with official-source version gates, scoped mutation authority, tests, and rollback requirements.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 4
- Maintainability: 5
- Output Consistency: 7
- Orchestration Fit: 6

Final Rating: 5.4/10


---

# Agent Review: Godot Gameplay Scripter

Source: `game-development/godot/godot-gameplay-scripter.md`

## 1. Current Function
Godot 4 gameplay implementation specialist for typed GDScript/C# systems, signal integrity, scene composition, Resource data, Autoload hygiene, and isolated-scene validation.

## 2. Current Role Boundary
Produce scoped Godot gameplay architecture, GDScript/C# implementation, signal, node-composition, scene, Autoload, and test artifacts for a declared Godot version while blocking project-wide rewrites, export/release changes, native/GDExtension work, or security-sensitive networking decisions without explicit approval.

## 3. Production Issues
- Original prompt assumes code and project mutation authority without an explicit repo, scene, version, or test boundary.
- Godot API behavior, GDScript/C# interop, GDExtension, networking, and export settings are version- and platform-sensitive.
- Overlaps Game Designer, Unity/Unreal implementers, networking engineers, code review, QA, and build/export owners.

## 4. Token Waste
- Signal, Autoload, C#, Resource, GDExtension, and networking examples should be emitted only for the scoped implementation mode.
- Broad architecture doctrine should become validation checklists.

## 5. Ambiguity Risks
- 'Build gameplay systems' can mean code patch, architecture spec, or project-wide rewrite.
- Autoload, networking authority, native extension, and export responsibilities are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with Godot-version gates, repo/scene scope, typed signal contracts, isolated tests, tool-failure handling, and PR-ready output schema.

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
- Orchestration Fit: 5

Final Rating: 4.8/10


---

# Agent Review: XR Interface Architect

Source: `spatial-computing/xr-interface-architect.md`

## 1. Current Function
XR interface architecture specialist for spatial UX flows, interface placement, input modality design, comfort/accessibility heuristics, discoverability, and developer handoff specifications.

## 2. Current Role Boundary
Produce spatial UX, interaction, comfort, accessibility, input, layout, and validation specifications for AR/VR/XR applications from declared device and use context while blocking implementation, device debugging, sensor-data collection, medical comfort claims, or platform decisions without evidence and owner review.

## 3. Production Issues
- Original prompt is too underspecified for production and lacks required inputs, output format, comfort thresholds, accessibility rules, and validation gates.
- XR interface decisions can affect motion sickness, accessibility, safety, sensor privacy, and device-specific usability.
- Overlaps UX Researcher, Accessibility Auditor, XR Immersive Developer, visionOS Spatial Engineer, Unity/Unreal XR engineers, and product owners.

## 4. Token Waste
- Short prompt should be rewritten as structured spatial UX contract rather than expanded persona prose.
- Generic capabilities need validation and handoff sections.

## 5. Ambiguity Risks
- 'Design spatial interfaces' can mean UX specification, prototype, implementation, or device debugging.
- Comfort, accessibility, privacy, and platform ownership are not defined.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as a spatial UX spec agent with required device/use inputs, comfort/accessibility gates, validation checklist, privacy boundaries, and implementation handoff schema.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 8
- Maintainability: 5
- Output Consistency: 3
- Orchestration Fit: 4

Final Rating: 5.0/10


---

# Agent Review: XR Immersive Developer

Source: `spatial-computing/xr-immersive-developer.md`

## 1. Current Function
WebXR implementation specialist for browser-based AR/VR/XR apps, Three.js/A-Frame/Babylon integrations, session setup, input handling, hit testing, fallbacks, and performance-aware 3D interaction code.

## 2. Current Role Boundary
Produce scoped WebXR and browser-based immersive implementation plans or patches with feature detection, permissions, fallback behavior, performance budgets, accessibility, privacy, and deployment constraints while blocking native-platform claims, sensor-data misuse, live deployment, or unsupported cross-device guarantees.

## 3. Production Issues
- Original prompt claims broad cross-platform capability without required browser/device support, permissions, privacy, or fallback gates.
- WebXR features vary across browsers and devices, and world/camera/hand/gaze data can carry privacy and safety implications.
- Overlaps XR Interface Architect, visionOS Spatial Engineer, Unity/Unreal XR, frontend engineers, 3D technical artists, QA, and deployment owners.

## 4. Token Waste
- Framework guidance should be generated only for the declared WebXR stack.
- Compatibility and fallback matrices should replace generic claims.

## 5. Ambiguity Risks
- 'Build immersive experiences' can mean scaffold, code patch, debugging, deployment, or UX design.
- Browser permissions, HTTPS, device support, and privacy boundaries are not specified.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with browser/device feature matrices, fallback rules, privacy/security constraints, performance budgets, framework-specific outputs, and deployment gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 8
- Maintainability: 6
- Output Consistency: 4
- Orchestration Fit: 5

Final Rating: 5.6/10


---

# Agent Review: visionOS Spatial Engineer

Source: `spatial-computing/visionos-spatial-engineer.md`

## 1. Current Function
Native visionOS implementation specialist for SwiftUI/RealityKit spatial interfaces, windows, volumes, immersive spaces, ornaments, gestures, asset integration, performance, and Apple-platform handoffs.

## 2. Current Role Boundary
Produce native visionOS SwiftUI, RealityKit, spatial window, volume, immersive scene, gesture, accessibility, and performance artifacts for a declared SDK/deployment target while version-gating platform facts and blocking cross-platform claims, app-store/review decisions, device-only validation claims, or live project mutation without approval.

## 3. Production Issues
- Original prompt is version-pinned and can become stale as visionOS, SwiftUI, RealityKit, and Apple design guidance evolve.
- Native visionOS work depends on SDK, Xcode, deployment target, hardware availability, privacy, accessibility, and app review requirements.
- Overlaps XR Interface Architect, XR Immersive Developer, iOS/macOS engineers, RealityKit/Metal specialists, Apple platform QA, and design-system owners.

## 4. Token Waste
- Feature catalog should be version-gated by SDK/deployment target.
- Documentation links should become required source/version inputs instead of assumed current facts.

## 5. Ambiguity Risks
- 'Build native volumetric interfaces' can mean specification, code patch, device testing, or app-review readiness.
- visionOS-specific ownership and cross-platform XR boundaries are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with SDK/deployment-target gates, source validation, backward-compatible patterns, Apple HIG/privacy/app-review constraints, and explicit simulator/device test boundaries.

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
- Orchestration Fit: 6

Final Rating: 6.0/10
