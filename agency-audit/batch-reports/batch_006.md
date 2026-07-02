# Batch Summary: batch_006

## Agents Reviewed
- `paid-media/paid-media-auditor.md`: Paid Media Auditor (refactor)
- `paid-media/paid-media-paid-social-strategist.md`: Paid Social Strategist (keep)
- `paid-media/paid-media-creative-strategist.md`: Ad Creative Strategist (refactor)
- `paid-media/paid-media-programmatic-buyer.md`: Programmatic & Display Buyer (refactor)
- `marketing/marketing-growth-hacker.md`: Growth Hacker (refactor)
- `marketing/marketing-app-store-optimizer.md`: App Store Optimizer (keep)
- `marketing/marketing-ai-citation-strategist.md`: AI Citation Strategist (keep)
- `marketing/marketing-agentic-search-optimizer.md`: Agentic Search Optimizer (rewrite)
- `marketing/marketing-aeo-foundations.md`: AEO Foundations Architect (refactor)
- `marketing/marketing-seo-specialist.md`: SEO Specialist (keep)

## Recommended Actions
- Keep: 4
- Refactor: 5
- Merge: 0
- Split: 0
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Agentic Search Optimizer: the current prompt appears to encode implementation-level browser, WebMCP, checkout, booking, auth, payment, and PII-flow claims that need current-source validation and engineering/security approval before any production use.

## Biggest Architecture Issue Found
The paid-media and search-growth cluster mixes advisory work with potentially live mutation. Account spend, campaign settings, tracking, audiences, app-store listings, website content, crawler policy, citations, and transactional site flows must be routed through specialist approval gates instead of being treated as direct agent execution.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_006.md`
- `agency-audit/refactored-agents/paid-media-auditor.md`
- `agency-audit/refactored-agents/paid-media-paid-social-strategist.md`
- `agency-audit/refactored-agents/paid-media-creative-strategist.md`
- `agency-audit/refactored-agents/paid-media-programmatic-buyer.md`
- `agency-audit/refactored-agents/marketing-growth-hacker.md`
- `agency-audit/refactored-agents/marketing-app-store-optimizer.md`
- `agency-audit/refactored-agents/marketing-ai-citation-strategist.md`
- `agency-audit/refactored-agents/marketing-agentic-search-optimizer.md`
- `agency-audit/refactored-agents/marketing-aeo-foundations.md`
- `agency-audit/refactored-agents/marketing-seo-specialist.md`
- `agency-audit/acceptance-tests/paid-media-auditor.tests.md`
- `agency-audit/acceptance-tests/paid-media-paid-social-strategist.tests.md`
- `agency-audit/acceptance-tests/paid-media-creative-strategist.tests.md`
- `agency-audit/acceptance-tests/paid-media-programmatic-buyer.tests.md`
- `agency-audit/acceptance-tests/marketing-growth-hacker.tests.md`
- `agency-audit/acceptance-tests/marketing-app-store-optimizer.tests.md`
- `agency-audit/acceptance-tests/marketing-ai-citation-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-agentic-search-optimizer.tests.md`
- `agency-audit/acceptance-tests/marketing-aeo-foundations.tests.md`
- `agency-audit/acceptance-tests/marketing-seo-specialist.tests.md`

## Subagent Inputs Used
- Paid-media boundary scan: recommended keeping all four paid-media roles while constraining auditor, creative, programmatic, budget, audience, tracking, and account-mutation behavior.
- Search-growth boundary scan: recommended keeping ASO, AI Citation, and SEO; refactoring Growth Hacker and AEO Foundations; and rewriting Agentic Search Optimizer around current-source validation.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Paid Media Auditor

Source: `paid-media/paid-media-auditor.md`

## 1. Current Function
Cross-platform paid-media diagnostic auditor for campaign structure, spend efficiency, tracking evidence, creative coverage, landing-page fit, and prioritized remediation.

## 2. Current Role Boundary
Audit paid-media accounts and measurement evidence in read-only mode, score findings, and route prioritized recommendations without implementing account changes.

## 3. Production Issues
- Overlaps PPC Strategist, Search Query Analyst, Tracking Specialist, paid social, creative, and programmatic roles.
- Tool list includes Write, Edit, and Bash even though an auditor should default to read-only evidence review.
- Account exports, conversion data, and offline or CRM data can include PII and budget-sensitive information.

## 4. Token Waste
- Large checklist framing should be turned into scoped audit modules.
- Impact estimates can become generic without required date range and spend context.

## 5. Ambiguity Risks
- 'Audit and optimize' can imply live edits.
- Projected impact may be invented when account data is incomplete.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as read-only diagnostic/reporting agent with account-access, PII redaction, approval, and specialist-routing gates.

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

# Agent Review: Paid Social Strategist

Source: `paid-media/paid-media-paid-social-strategist.md`

## 1. Current Function
Paid social planning specialist for Meta, TikTok, LinkedIn, X, Reddit, Pinterest, and other social ad platforms.

## 2. Current Role Boundary
Create paid social strategy, audience architecture, creative briefs, test plans, and budget recommendations without launching campaigns or uploading audiences.

## 3. Production Issues
- Overlaps Tracking Specialist on pixel, CAPI, attribution, lead forms, and CRM syncs.
- Overlaps PPC Strategist on cross-channel budget and cannibalization analysis.
- Audience uploads, lead forms, and CRM syncing require consent and privacy review.

## 4. Token Waste
- Platform playbook examples can be shorter when the account objective and audience policy are explicit.
- Some Google Ads wording is awkward for a social-first role.

## 5. Ambiguity Risks
- 'Build campaigns' can mean planning, drafting, or launching.
- Budget recommendations can be mistaken for approval to mutate spend.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as paid social strategist with clearer privacy, budget, tracking, and launch approval gates.

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

# Agent Review: Ad Creative Strategist

Source: `paid-media/paid-media-creative-strategist.md`

## 1. Current Function
Ad creative strategist for paid search, paid social, Performance Max, display, and programmatic asset planning.

## 2. Current Role Boundary
Develop paid-media creative strategy, copy variants, asset QA, and test hypotheses while requiring approval before publishing ads or changing landing-page copy.

## 3. Production Issues
- Original wording can imply direct deployment of ad variations.
- Overlaps PPC Strategist on RSA assets, ad extensions, and Performance Max asset groups.
- Overlaps Paid Social Strategist on platform-specific social creative strategy.

## 4. Token Waste
- Creative examples are useful but should be generated from brand, claim, and offer inputs.
- Platform tactics repeat work owned by channel specialists.

## 5. Ambiguity Risks
- 'Deploy new ad variations directly' needs to be removed or gated.
- Claims and compliance requirements vary by vertical and region.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as creative planning and QA role; all live publishing, claims, and landing-page mutations require approval and specialist handoff.

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

# Agent Review: Programmatic & Display Buyer

Source: `paid-media/paid-media-programmatic-buyer.md`

## 1. Current Function
Programmatic and display media planning specialist for DSPs, direct buys, ABM display, placements, deal IDs, brand safety, and viewability.

## 2. Current Role Boundary
Plan and evaluate display/programmatic media, inventory, placement, frequency, brand safety, and measurement options without committing spend or changing DSP settings.

## 3. Production Issues
- Can imply live bid, budget, placement, DSP, or partner-buy execution.
- Overlaps PPC Strategist where Google Display Network reports and exclusions intersect.
- ABM and third-party audiences need privacy, data-sharing, and consent boundaries.

## 4. Token Waste
- DSP-specific detail should be parameterized by platform and inventory scope.
- Brand-safety examples repeat unless the risk policy is supplied.

## 5. Ambiguity Risks
- 'Buyer' can imply authority to transact.
- View-through attribution and lift measurement can be overstated without experiment design.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor to separate programmatic planning from live media buying, with explicit spend, audience, brand-safety, and partner-approval gates.

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

# Agent Review: Growth Hacker

Source: `marketing/marketing-growth-hacker.md`

## 1. Current Function
Growth experiment strategist for acquisition, activation, referral, retention, conversion, and funnel opportunity discovery.

## 2. Current Role Boundary
Design ethical growth hypotheses, prioritization, and experiment readouts using supplied funnel evidence without mutating product, website, content, SEO, paid media, or lifecycle campaigns directly.

## 3. Production Issues
- Too broad and overlaps product growth, CRO, SEO, content, paid media, analytics, automation, and lifecycle roles.
- Growth-hacking language can encourage spam, dark patterns, consent bypass, or vanity metrics.
- Experiment quality depends on measurement baselines, guardrails, and statistical thresholds that are not required.

## 4. Token Waste
- Tactic lists should be secondary to experiment governance.
- Viral loop language can be shorter and more constrained.

## 5. Ambiguity Risks
- 'Implement growth tactics' can mean planning or production mutation.
- Rapid acquisition can conflict with brand, privacy, and platform rules.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around experiment governance, consent, anti-spam rules, measurement baselines, and specialist handoffs.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

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

# Agent Review: App Store Optimizer

Source: `marketing/marketing-app-store-optimizer.md`

## 1. Current Function
App Store Optimization specialist for Apple App Store, Google Play, listing metadata, keyword strategy, creative tests, ratings, reviews, and localization.

## 2. Current Role Boundary
Improve app-store discoverability and listing conversion through metadata, keyword, screenshot/video, localization, and review-signal recommendations without publishing store changes.

## 3. Production Issues
- Overlaps growth, SEO, product marketing, brand, and visual design roles.
- Store metadata, screenshots, privacy labels, and claims have platform policy and legal constraints.
- Ratings and reviews must be handled without manipulation or fake-review tactics.

## 4. Token Waste
- Detailed ASO playbooks should be driven by store and market inputs.
- Keyword examples can be generated from supplied data instead of embedded.

## 5. Ambiguity Risks
- 'Optimize listing' can imply direct publishing.
- Review strategy can be misread as soliciting or fabricating reviews.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as ASO specialist with app-store publishing, policy, privacy-label, localization, and review-integrity gates.

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

# Agent Review: AI Citation Strategist

Source: `marketing/marketing-ai-citation-strategist.md`

## 1. Current Function
AI citation and answer-engine optimization specialist for prompt audits, competitor citation mapping, source gaps, and fix-pack recommendations.

## 2. Current Role Boundary
Audit and improve how AI answer engines cite or recommend the brand through source-grounded recommendations, without promising citations or mutating websites directly.

## 3. Production Issues
- Overlaps SEO Specialist, AEO Foundations, content strategy, and agentic search roles.
- AI engines change behavior and cannot be guaranteed to cite specific sources.
- Prompting public AI systems with confidential data can leak sensitive information.

## 4. Token Waste
- Engine-specific claims should be current-source checked or framed as observations.
- Broad AEO/GEO terminology needs narrower deliverables.

## 5. Ambiguity Risks
- 'Optimize for AI recommendations' can imply control over third-party models.
- Source quality and claim verification rules are not always explicit.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as citation-audit and recommendation role with source verification, confidentiality, measurement, and no-guarantee boundaries.

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

# Agent Review: Agentic Search Optimizer

Source: `marketing/marketing-agentic-search-optimizer.md`

## 1. Current Function
Agentic search readiness auditor for AI browser task completion, structured action specs, machine-readable flows, and implementation handoffs.

## 2. Current Role Boundary
Assess agentic search and AI browsing task-completion readiness, then produce current-source implementation specifications and risk handoffs without deploying website, checkout, booking, form, auth, or payment changes.

## 3. Production Issues
- High overlap with frontend/product engineering, AEO Foundations, SEO, analytics, and security for transactional flows.
- Likely contains speculative or unverifiable WebMCP and browser-agent implementation claims.
- Touches forms, checkout, booking, authentication, payment, and PII flows that need engineering and security approval.

## 4. Token Waste
- Implementation-level standard claims should be replaced with current-source validation requirements.
- Broad AI browsing narrative is less valuable than scoped task-completion evidence.

## 5. Ambiguity Risks
- 'Implement WebMCP' can imply deploying emerging or nonstandard patterns.
- Agentic task success can be measured only with defined tasks, environments, and privacy rules.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as evidence-based readiness auditor and specification writer; implementation details require current-source validation and engineering/security approval.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 4
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 4

Final Rating: 3.8/10


---

# Agent Review: AEO Foundations Architect

Source: `marketing/marketing-aeo-foundations.md`

## 1. Current Function
AEO foundation specialist for AI crawler discoverability, parsability, robots and llms.txt options, markdown surfaces, structured content, and measurement.

## 2. Current Role Boundary
Audit and specify AI-discoverability foundations such as crawl policy options, llms.txt, markdown availability, content parsability, token budgets, and crawler-log measurement without deploying site changes.

## 3. Production Issues
- Overlaps SEO Specialist, AI Citation Strategist, Agentic Search Optimizer, content, and DevOps.
- Robots, crawler access, licensing, and AI training access can be business/legal decisions.
- Server, CDN, CMS, and content changes require website owner approval.

## 4. Token Waste
- Implementation examples should be tied to site stack and policy decisions.
- AEO terminology repeats across adjacent agents.

## 5. Ambiguity Risks
- 'Enable AI crawlers' may conflict with legal, licensing, or data-exposure strategy.
- llms.txt and markdown availability need maturity and measurement caveats.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with business/legal crawler-policy approval, deployment boundaries, privacy review, and measurement gates.

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

# Agent Review: SEO Specialist

Source: `marketing/marketing-seo-specialist.md`

## 1. Current Function
SEO specialist for technical audits, keyword clusters, SERP analysis, schema, internal linking, content optimization, cannibalization, and organic growth strategy.

## 2. Current Role Boundary
Improve traditional organic search performance through technical SEO, keyword architecture, content briefs, schema, internal links, and authority recommendations without publishing site changes or link schemes.

## 3. Production Issues
- Overlaps AEO Foundations, AI Citation Strategist, Agentic Search Optimizer, content, growth, and web performance roles.
- Website and content mutations require CMS, engineering, brand, legal, and analytics approval.
- Link-building recommendations need compliance boundaries and no manipulative schemes.

## 4. Token Waste
- Strong prompt but can move examples behind scoped deliverable templates.
- AI/AEO adjacent content should be handoff instead of role expansion.

## 5. Ambiguity Risks
- 'Optimize pages' can imply direct CMS edits.
- Ranking and traffic outcomes cannot be guaranteed.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as traditional SEO owner with explicit handoffs to AEO, AI citation, and agentic-search roles plus website/content mutation gates.

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
