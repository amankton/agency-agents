# Batch Summary: batch_011

## Agents Reviewed
- `design/design-ui-designer.md`: UI Designer (refactor)
- `design/design-ux-architect.md`: UX Architect (split)
- `design/design-ux-researcher.md`: UX Researcher (refactor)
- `design/design-brand-guardian.md`: Brand Guardian (refactor)
- `design/design-visual-storyteller.md`: Visual Storyteller (refactor)
- `design/design-whimsy-injector.md`: Whimsy Injector (refactor)
- `design/design-image-prompt-engineer.md`: Image Prompt Engineer (refactor)
- `design/design-inclusive-visuals-specialist.md`: Inclusive Visuals Specialist (refactor)
- `design/design-persona-walkthrough.md`: Persona Walkthrough Specialist (merge)
- `specialized/specialized-cultural-intelligence-strategist.md`: Cultural Intelligence Strategist (split)

## Recommended Actions
- Keep: 0
- Refactor: 7
- Merge: 1
- Split: 2
- Deprecate: 0
- Rewrite: 0

## Highest-Risk Agent
Cultural Intelligence Strategist: it has the broadest design blast radius because it can influence UI architecture, copy, localization, imagery, identity assumptions, privacy expectations, and current cultural standards. Without evidence and bounded authority, it can encode stereotypes or overgeneralizations into downstream product specs.

## Biggest Architecture Issue Found
The design and UX cluster needs a sharper artifact and evidence map. Research, persona simulation, UX architecture, UI specs, brand governance, visual storytelling, prompt writing, inclusive-visual review, whimsy, and cultural intelligence are distinct jobs. Batch 011 makes design work draft/review/handoff-first, blocks unsupported cultural or research claims, and routes implementation, publishing, legal, community, and accessibility approvals to their owners.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_011.md`
- `agency-audit/refactored-agents/design-ui-designer.md`
- `agency-audit/refactored-agents/design-ux-architect.md`
- `agency-audit/refactored-agents/design-ux-researcher.md`
- `agency-audit/refactored-agents/design-brand-guardian.md`
- `agency-audit/refactored-agents/design-visual-storyteller.md`
- `agency-audit/refactored-agents/design-whimsy-injector.md`
- `agency-audit/refactored-agents/design-image-prompt-engineer.md`
- `agency-audit/refactored-agents/design-inclusive-visuals-specialist.md`
- `agency-audit/refactored-agents/design-persona-walkthrough.md`
- `agency-audit/refactored-agents/specialized-cultural-intelligence-strategist.md`
- `agency-audit/acceptance-tests/design-ui-designer.tests.md`
- `agency-audit/acceptance-tests/design-ux-architect.tests.md`
- `agency-audit/acceptance-tests/design-ux-researcher.tests.md`
- `agency-audit/acceptance-tests/design-brand-guardian.tests.md`
- `agency-audit/acceptance-tests/design-visual-storyteller.tests.md`
- `agency-audit/acceptance-tests/design-whimsy-injector.tests.md`
- `agency-audit/acceptance-tests/design-image-prompt-engineer.tests.md`
- `agency-audit/acceptance-tests/design-inclusive-visuals-specialist.tests.md`
- `agency-audit/acceptance-tests/design-persona-walkthrough.tests.md`
- `agency-audit/acceptance-tests/specialized-cultural-intelligence-strategist.tests.md`

## Subagent Inputs Used
- Core UX scan: refactored UI Designer, UX Researcher, and Brand Guardian; split UX Architect away from system/API/repo authority; merged Persona Walkthrough into UX Researcher as a CRO/persona mode.
- Visual and cultural scan: refactored Visual Storyteller, Whimsy Injector, Image Prompt Engineer, and Inclusive Visuals; split Cultural Intelligence around sourced research, localization audit, product inclusion, and representation/legal/privacy handoffs.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: UI Designer

Source: `design/design-ui-designer.md`

## 1. Current Function
UI design specialist for visual systems, component libraries, design tokens, responsive screens, interaction states, accessibility, and implementation handoff artifacts.

## 2. Current Role Boundary
Create scoped UI design systems, component specs, responsive states, accessibility notes, and developer handoffs from approved product, brand, and platform inputs without editing repositories, publishing design systems, or inventing brand/product constraints.

## 3. Production Issues
- Original prompt is useful but implies comprehensive design-system creation without enough product, brand, platform, licensing, or handoff constraints.
- Overlaps UX Architect, Brand Guardian, Frontend Developer, Accessibility Auditor, Inclusive Visuals, and Visual Storyteller.
- Design assets, fonts, images, icons, and brand choices need rights, accessibility, responsive, and implementation-contract gates.

## 4. Token Waste
- Large design-token examples should be generated from brand and platform inputs.
- Generic aesthetic rules should be replaced by project-specific design constraints.

## 5. Ambiguity Risks
- 'Pixel-perfect interface creation' can imply direct Figma or repo mutation.
- Brand and product constraints can be invented when source guidelines are missing.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with product/brand/platform inputs, design-artifact-only default, responsive states, WCAG checks, asset rights, developer handoff, no repo edits, and no live design-system publishing gates.

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

# Agent Review: UX Architect

Source: `design/design-ux-architect.md`

## 1. Current Function
UX architecture and implementation-foundation specialist for information architecture, flows, layouts, CSS/design-system foundations, responsive strategy, accessibility patterns, and handoff structure.

## 2. Current Role Boundary
Define scoped UX architecture, information architecture, layout foundations, interaction patterns, accessibility requirements, and developer handoffs while routing system architecture, repository topology, API/schema authority, deployment, and agent coordination to engineering or workflow owners.

## 3. Production Issues
- Original prompt overreaches into repository topology, API/schema enforcement, system architecture, and agent coordination from a design role.
- Mandatory theme-toggle rule is too universal and may conflict with product, brand, or accessibility requirements.
- Overlaps Software Architect, Backend Architect, Frontend Developer, Workflow Architect, Product Manager, Orchestrator, and UI Designer.

## 4. Token Waste
- Large CSS and architecture examples should be scoped to product and stack constraints.
- Universal defaults like theme toggle should become optional requirements.

## 5. Ambiguity Risks
- 'Own repository topology' conflicts with engineering architecture authority.
- UX foundation can be mistaken for implementation or deployment authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split UX/IA/CSS foundation from system architecture and orchestration authority; refactor with product/stack context, optional theme rules, accessibility/performance budgets, and engineering handoff gates.

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
- Orchestration Fit: 2

Final Rating: 3.4/10


---

# Agent Review: UX Researcher

Source: `design/design-ux-researcher.md`

## 1. Current Function
UX research specialist for research plans, usability studies, behavioral analysis, analytics synthesis, interview/survey interpretation, accessibility research, and actionable design recommendations.

## 2. Current Role Boundary
Plan, synthesize, and report UX research using explicit research questions, evidence sources, consent/privacy rules, methodology limits, and confidence levels without inventing participants, quotes, sample sizes, statistical certainty, or contacting users without approval.

## 3. Production Issues
- Research prompts can fabricate participants, quotes, sample sizes, or statistical confidence if source evidence is missing.
- Real user research involves consent, PII, recordings, recruitment, incentives, and privacy obligations.
- Overlaps Persona Walkthrough, Product Feedback Synthesizer, Product Manager, Analytics Reporter, Accessibility Auditor, and Academic Psychologist.

## 4. Token Waste
- Methodology templates are useful but should be selected by research question and evidence source.
- Broad research catalog should become modes with confidence labeling.

## 5. Ambiguity Risks
- 'Conduct research' can mean plan, synthesize existing evidence, or contact real users.
- Synthetic persona hypotheses can be confused with validated findings.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with research question, evidence basis, consent/privacy, no invented participants or certainty, confidence labels, inclusion criteria, read-only analytics, and actionable handoff gates.

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
- Orchestration Fit: 4

Final Rating: 4.6/10


---

# Agent Review: Brand Guardian

Source: `design/design-brand-guardian.md`

## 1. Current Function
Brand strategy and governance specialist for brand foundations, identity systems, voice/tone, messaging architecture, brand audits, guidelines, and implementation alignment.

## 2. Current Role Boundary
Create and audit brand strategy, identity, voice, consistency, and implementation guidance from approved brand/business evidence without making legal/IP determinations, changing public assets, issuing crisis statements, or publishing brand changes without approval.

## 3. Production Issues
- Original prompt blends brand strategy, visual identity, legal trademark protection, public crisis management, and monitoring without authority boundaries.
- Brand recommendations can create IP, licensing, legal, cultural, accessibility, and public-communications risk.
- Overlaps UI Designer, Visual Storyteller, PR/Communications, Marketing Content, Legal Compliance, Cultural Intelligence, and Inclusive Visuals.

## 4. Token Waste
- Large brand-framework examples should be generated from business and brand inputs.
- Legal/IP language should be converted to handoff triggers.

## 5. Ambiguity Risks
- 'Protect brand IP' can imply legal advice or filings.
- Crisis and monitoring language can imply public communications authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with brand evidence, business context, asset rights, legal/IP handoff, no public mutation, no crisis authority, accessibility/cultural checks, and approval gates.

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

# Agent Review: Visual Storyteller

Source: `design/design-visual-storyteller.md`

## 1. Current Function
Visual communication and storytelling specialist for narrative arcs, storyboards, multimedia concepts, campaign visuals, information design, and brand-aligned visual content specs.

## 2. Current Role Boundary
Translate approved messages, data, and brand context into visual narrative specs, storyboards, content structures, and accessible handoffs without publishing, uploading, generating final assets, or making unsupported performance/cultural claims.

## 3. Production Issues
- Original prompt can drift from narrative specification into content production, publishing, or unsupported emotional/performance claims.
- Visual storytelling depends on source-data truth, asset rights, brand guidelines, accessibility, localization, and cultural review.
- Overlaps UI Designer, Brand Guardian, Whimsy Injector, Image Prompt Engineer, Inclusive Visuals, and Cultural Intelligence.

## 4. Token Waste
- Narrative frameworks are useful but should be selected by channel and creative brief.
- Generic visual examples should be replaced by source-evidence mapping.

## 5. Ambiguity Risks
- 'Create visual campaigns' can imply final asset generation or upload.
- Complex information can be oversimplified if source data is not supplied.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with creative brief, source-evidence mapping, brand/channel constraints, asset rights, accessibility/localization, cultural review, no-publish, and no-final-generation gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.8/10


---

# Agent Review: Whimsy Injector

Source: `design/design-whimsy-injector.md`

## 1. Current Function
Brand personality and delightful interaction specialist for purposeful whimsy, microinteractions, empty/error states, motion concepts, microcopy, and engagement moments.

## 2. Current Role Boundary
Design purposeful, accessible, performance-aware delight, microcopy, motion, and playful interaction specs that support user tasks and brand voice without introducing dark patterns, hidden tracking, distracting gamification, inaccessible motion, or live production edits.

## 3. Production Issues
- Whimsy can harm usability if it distracts from tasks, increases cognitive load, or becomes dark-pattern gamification.
- Motion, Easter eggs, humor, and hidden features require accessibility, performance, cultural, and brand-safety gates.
- Overlaps Brand Guardian, UI Designer, UX Architect, UX Researcher, Persona Walkthrough, and content/copy roles.

## 4. Token Waste
- Large whimsy taxonomy should be selected by user job, brand, and context.
- Examples should become checklists and gated design specs.

## 5. Ambiguity Risks
- 'Create shareable moments' can imply manipulative social loops.
- Easter eggs or gamification can imply production code or analytics changes.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with user-task purpose, brand voice, reduced-motion/screen-reader fallbacks, performance budget, cultural review, no dark patterns, no hidden tracking, and no production-edit gates.

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

# Agent Review: Image Prompt Engineer

Source: `design/design-image-prompt-engineer.md`

## 1. Current Function
AI image prompt engineering specialist for photography-style prompts, platform parameters, composition, lighting, negative prompts, variants, and brand-aligned visual prompt systems.

## 2. Current Role Boundary
Produce structured image-generation prompts, variants, negative prompts, and review checklists from approved briefs, platforms, rights, brand, safety, and subject-consent inputs without generating, uploading, or publishing images unless explicitly authorized.

## 3. Production Issues
- Image prompts can create likeness, IP/logo, rights, safety, identity, deception, and representation risks.
- Original prompt implies optimization for generative platforms without enough usage rights, subject consent, or publish/generation boundaries.
- Overlaps Visual Storyteller, Inclusive Visuals, Brand Guardian, UI/UX, marketing, and content roles.

## 4. Token Waste
- Photography taxonomy is useful but should be generated only for the chosen platform and brief.
- Style examples need rights-aware constraints.

## 5. Ambiguity Risks
- 'Professional-quality photography' can imply generating final images.
- Referencing real artists, brands, or people can create rights or likeness issues.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with prompt-artifact-only default, platform parameters, rights/reference/subject-consent policy, brand usage, safety exclusions, representation checks, no unauthorized likeness/IP, and generation/publishing gates.

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

# Agent Review: Inclusive Visuals Specialist

Source: `design/design-inclusive-visuals-specialist.md`

## 1. Current Function
Inclusive visual representation specialist for bias-aware image/video prompt constraints, dignity checks, anti-stereotype reviews, physical-reality checks, and community-validation gates.

## 2. Current Role Boundary
Create representation-aware prompt constraints, QA checklists, and review guidance for human imagery using supplied community, market, rights, and approval context without speaking as a community authority, inferring sensitive traits, generating/publishing assets, or making unsupported cultural claims.

## 3. Production Issues
- Representation guidance can encode stereotypes, tokenism, exoticism, or overconfident claims if not grounded in community context.
- Prompt examples can imply authority to generate or publish sensitive identity imagery without consent or review.
- Overlaps Image Prompt Engineer, Cultural Intelligence Strategist, UX Researcher, Brand Guardian, Visual Storyteller, and accessibility review.

## 4. Token Waste
- Strong examples should become scoped prompt architectures and QA checklists.
- Universal representation claims need evidence and uncertainty labels.

## 5. Ambiguity Risks
- 'Defeats systemic AI biases' can overpromise model control.
- Cultural specificity can become stereotyping without sourced context or community review.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with community context, rights/consent, no community-authority claims, no sensitive-trait inference, anti-stereotype constraints, physical-reality checks, uncertainty labels, and community/brand/legal approval gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.8/10


---

# Agent Review: Persona Walkthrough Specialist

Source: `design/design-persona-walkthrough.md`

## 1. Current Function
Persona walkthrough and conversion-analysis specialist for simulated page reviews, five-second tests, fold-by-fold monologues, LIFT/Cialdini/Fogg assessment, CTA reachability, and CRO hypotheses.

## 2. Current Role Boundary
Run qualitative persona-based CRO walkthroughs as a UX Researcher mode using supplied page evidence and persona context, clearly labeling outputs as hypotheses rather than validated user research and avoiding protected-class stereotyping, dark-pattern recommendations, or live site actions.

## 3. Production Issues
- Persona simulation can be mistaken for real user evidence or statistical research.
- Psychological and cultural persona traits can become stereotyping if not scoped and caveated.
- Overlaps UX Researcher, Behavioral Nudge Engine, CRO/marketing roles, Accessibility Auditor, Academic Psychologist, and UI Designer.

## 4. Token Waste
- Detailed persona templates are useful but should depend on supplied page and persona context.
- Framework lists should become structured output sections.

## 5. Ambiguity Risks
- 'Become other people' can sound like authoritative claims about groups.
- Conversion recommendations can drift into dark patterns if guardrails are absent.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Merge into UX Researcher as a CRO/persona-walkthrough mode with page evidence, persona source, qualitative caveat, no protected-class stereotyping, no dark patterns, no live page actions, and validation handoff gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: merge

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

# Agent Review: Cultural Intelligence Strategist

Source: `specialized/specialized-cultural-intelligence-strategist.md`

## 1. Current Function
Cultural intelligence and inclusion strategy specialist for product-exclusion audits, localization/i18n blindspot reviews, cultural context briefs, representation handoffs, and structurally inclusive design recommendations.

## 2. Current Role Boundary
Audit product flows, copy, imagery, forms, localization, and design assumptions for cultural exclusion using sourced, current, locale-specific evidence while avoiding universal claims, protected-class profiling, legal overreach, live mutations, or unsourced cultural generalizations.

## 3. Production Issues
- Broad role covers UI architecture, copy, localization, imagery, identity, privacy expectations, and cultural standards, creating high orchestration overlap.
- Original prompt requires autonomous research and strong cultural claims without enough source, jurisdiction, community-review, or legal/privacy boundaries.
- Overlaps Inclusive Visuals, UX Researcher, Persona Walkthrough, Brand Guardian, UI Designer, UX Architect, localization, privacy, and legal roles.

## 4. Token Waste
- Compelling examples should become an evidence-backed audit schema.
- Broad cultural intelligence scope should be split into cultural research/localization audit and product-inclusion advisory modes.

## 5. Ambiguity Risks
- 'Cultural intelligence' can overgeneralize groups or treat culture as static.
- Legal, regional, cultural, accessibility, and personal-preference concerns can be conflated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split into bounded cultural research/localization audit and product-inclusion advisory modes with current sourced evidence, no universal-group claims, no protected-class profiling, imagery handoff, legal/privacy routing, and approval gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 4.0/10
