# Batch Summary: batch_007

## Agents Reviewed
- `marketing/marketing-content-creator.md`: Content Creator (refactor)
- `marketing/marketing-social-media-strategist.md`: Social Media Strategist (refactor)
- `marketing/marketing-multi-platform-publisher.md`: Multi-Platform Publisher (keep)
- `marketing/marketing-twitter-engager.md`: Twitter Engager (refactor)
- `marketing/marketing-x-twitter-intelligence-analyst.md`: X/Twitter Intelligence Analyst (keep)
- `marketing/marketing-linkedin-content-creator.md`: LinkedIn Content Creator (refactor)
- `marketing/marketing-instagram-curator.md`: Instagram Curator (refactor)
- `marketing/marketing-tiktok-strategist.md`: TikTok Strategist (refactor)
- `marketing/marketing-video-optimization-specialist.md`: Video Optimization Specialist (refactor)
- `marketing/marketing-short-video-editing-coach.md`: Short-Video Editing Coach (rewrite)

## Recommended Actions
- Keep: 2
- Refactor: 7
- Merge: 0
- Split: 0
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Twitter Engager: it sits closest to live public interaction because replies, DMs, crisis responses, support issues, and thought-leadership engagement can become account actions without explicit approval tiers.

## Biggest Architecture Issue Found
The broad marketing cluster needs a job-boundary split. Source drafting, social planning, channel specialization, public engagement, intelligence, draft-only publishing, video packaging, and post-production coaching are distinct roles. The safe default is draft/spec/recommendation unless account authority and approval tiers are explicit.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_007.md`
- `agency-audit/refactored-agents/marketing-content-creator.md`
- `agency-audit/refactored-agents/marketing-social-media-strategist.md`
- `agency-audit/refactored-agents/marketing-multi-platform-publisher.md`
- `agency-audit/refactored-agents/marketing-twitter-engager.md`
- `agency-audit/refactored-agents/marketing-x-twitter-intelligence-analyst.md`
- `agency-audit/refactored-agents/marketing-linkedin-content-creator.md`
- `agency-audit/refactored-agents/marketing-instagram-curator.md`
- `agency-audit/refactored-agents/marketing-tiktok-strategist.md`
- `agency-audit/refactored-agents/marketing-video-optimization-specialist.md`
- `agency-audit/refactored-agents/marketing-short-video-editing-coach.md`
- `agency-audit/acceptance-tests/marketing-content-creator.tests.md`
- `agency-audit/acceptance-tests/marketing-social-media-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-multi-platform-publisher.tests.md`
- `agency-audit/acceptance-tests/marketing-twitter-engager.tests.md`
- `agency-audit/acceptance-tests/marketing-x-twitter-intelligence-analyst.tests.md`
- `agency-audit/acceptance-tests/marketing-linkedin-content-creator.tests.md`
- `agency-audit/acceptance-tests/marketing-instagram-curator.tests.md`
- `agency-audit/acceptance-tests/marketing-tiktok-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-video-optimization-specialist.tests.md`
- `agency-audit/acceptance-tests/marketing-short-video-editing-coach.tests.md`

## Subagent Inputs Used
- Broad content/social scan: split Content Creator as source-draft, Social Media Strategist as planner, Multi-Platform Publisher as draft-only orchestrator, and Twitter Engager as approved platform executor.
- Channel/video scan: keep the role set while separating X/Twitter intelligence, LinkedIn/Instagram/TikTok strategy, video packaging, and short-video post-production; no direct publishing, messaging, profile edits, ads, or credential use without approval.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Content Creator

Source: `marketing/marketing-content-creator.md`

## 1. Current Function
Content strategy and drafting specialist for brand storytelling, editorial themes, campaign copy, long-form drafts, and reusable source assets.

## 2. Current Role Boundary
Create platform-neutral content strategy, source drafts, brand storytelling, and repurposable assets without owning final campaign strategy, account actions, or publishing.

## 3. Production Issues
- Too broad: covers strategy, calendars, distribution, analytics, SEO, video, UGC, and community engagement.
- Overlaps Social Media Strategist, Multi-Platform Publisher, SEO Specialist, channel specialists, and video roles.
- Needs stronger source, claim, copyright, brand, and draft-only boundaries before external use.

## 4. Token Waste
- Compact prompt, but broad capability lists make routing ambiguous.
- Success metrics imply outcomes without source data or channel ownership.

## 5. Ambiguity Risks
- 'Manage content' can imply publishing or final campaign ownership.
- UGC and influencer content need rights and consent checks.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as source-draft and brand storytelling role with draft-only, claim, copyright, privacy, and handoff gates.

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

# Agent Review: Social Media Strategist

Source: `marketing/marketing-social-media-strategist.md`

## 1. Current Function
Cross-platform social media strategist for professional networks, campaign planning, channel mix, audience development, calendar strategy, and reporting.

## 2. Current Role Boundary
Plan and coordinate social strategy, audience, channel mix, calendar, campaign briefs, and performance recommendations while routing execution to channel owners and approved publishing tools.

## 3. Production Issues
- Overlaps Content Creator on content calendars and adaptation.
- Overlaps Twitter Engager, LinkedIn Content Creator, Instagram Curator, and TikTok Strategist on platform execution.
- Campaign execution, paid social strategy, employee advocacy, and real-time engagement need account and approval boundaries.

## 4. Token Waste
- Useful workflow but repeated platform tactics should become handoff guidance.
- Metric targets require baseline and platform context.

## 5. Ambiguity Risks
- 'Campaign execution' can imply posting, DMs, ad changes, or community replies.
- Crisis and employee advocacy work need approval and escalation owners.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as planner/coordinator with explicit no-posting, no-DM, no-ad-change, crisis-escalation, and channel handoff rules.

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

# Agent Review: Multi-Platform Publisher

Source: `marketing/marketing-multi-platform-publisher.md`

## 1. Current Function
Draft-only publishing orchestrator for multi-platform Chinese content distribution, platform fit checks, draft sync, rate control, and per-platform status reporting.

## 2. Current Role Boundary
Validate platform fit, account/auth status, platform constraints, and human confirmation, then create or sync draft-only platform artifacts and return draft URLs without publishing live.

## 3. Production Issues
- Strong draft-first boundary already exists, but tool templates can still tempt unapproved execution.
- Handles account cookies, credentials, local tools, and platform sessions that need secret-handling rules.
- Content adaptation overlaps Content Creator and regional platform strategists.

## 4. Token Waste
- Long tool templates and platform matrices should be governed by scoped target platforms.
- Mojibaked source text reduces maintainability.

## 5. Ambiguity Risks
- 'Sync' must mean draft-only sync, not publish.
- Credential and cookie handling is not explicit enough.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep with stronger credential, cookie, no-secret-echo, draft-only, copyright, platform-terms, and human-confirmation gates.

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

# Agent Review: Twitter Engager

Source: `marketing/marketing-twitter-engager.md`

## 1. Current Function
X/Twitter engagement execution specialist for replies, threads, community interaction, Spaces support, and real-time engagement under approved playbooks.

## 2. Current Role Boundary
Draft or execute X/Twitter engagement only under an approved strategy, account permission, safe-response matrix, and approval tier, escalating DMs, support, crisis, legal, and brand-risk items.

## 3. Production Issues
- Blurs planner, executor, content creator, community manager, and crisis responder.
- Overlaps Social Media Strategist, Content Creator, X/Twitter Intelligence Analyst, support, and brand roles.
- Mentions DMs, crisis responses, real-time engagement, and thought leadership without enough approval gates.

## 4. Token Waste
- Engagement tactics should be driven by a supplied playbook and queue.
- Viral and authority language repeats broad social goals.

## 5. Ambiguity Risks
- 'Engage' can mean draft, approve, or send live replies.
- Crisis response and customer support need escalation, not autonomous posting.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as platform executor with explicit draft-vs-live tiers, DM privacy, account permission, crisis escalation, and brand-safe response matrix.

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

# Agent Review: X/Twitter Intelligence Analyst

Source: `marketing/marketing-x-twitter-intelligence-analyst.md`

## 1. Current Function
X/Twitter research and social intelligence specialist for trend detection, brand monitoring, competitor intelligence, audience mapping, and campaign risk assessment.

## 2. Current Role Boundary
Produce evidence-backed X/Twitter intelligence from public or authorized data, preserving URLs, timestamps, query scope, confidence, and caveats without engaging, posting, or targeting individuals.

## 3. Production Issues
- Strong evidence and privacy rules already exist.
- Can still overlap Twitter Engager if recommended actions look like direct response execution.
- Monitoring and alerts need owner, cadence, privacy, and data-source boundaries.

## 4. Token Waste
- Prompt is focused and useful; little bloat.
- Templates are helpful but should be tied to a scoped decision question.

## 5. Ambiguity Risks
- 'Alert setup' can imply live webhooks or ongoing monitoring operations.
- Audience research can drift into personal profiling if not bounded.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as evidence-first intelligence role with clear separation from engagement execution and stronger monitoring authorization boundaries.

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

# Agent Review: LinkedIn Content Creator

Source: `marketing/marketing-linkedin-content-creator.md`

## 1. Current Function
LinkedIn content specialist for professional thought leadership, personal brand, post drafts, carousels, profile optimization, and inbound opportunity content.

## 2. Current Role Boundary
Create LinkedIn thought-leadership drafts, profile recommendations, calendars, and engagement guidance under brand, claim, voice, and approval rules without posting, commenting, connecting, or sending DMs autonomously.

## 3. Production Issues
- Overlaps Social Media Strategist and Content Creator on calendar, positioning, and drafting.
- Includes engagement and connection-request tactics that can become live account actions.
- Algorithm and inbound-opportunity claims need baseline and no-guarantee framing.

## 4. Token Waste
- Long examples and playbooks should be generated from voice, audience, and goal inputs.
- Audience playbooks can become references rather than active prompt body.

## 5. Ambiguity Risks
- 'Respond to every comment' can imply live commenting.
- Connection requests and DMs need privacy and approval boundaries.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as LinkedIn-specific draft and profile advisor with no autonomous posting, comment, connection, or DM actions.

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

# Agent Review: Instagram Curator

Source: `marketing/marketing-instagram-curator.md`

## 1. Current Function
Instagram channel specialist for visual storytelling, aesthetic systems, Reels/Stories/feed planning, community guidance, UGC, shopping, and performance recommendations.

## 2. Current Role Boundary
Plan Instagram visual strategy, grid, formats, creative briefs, community guidance, and shopping recommendations without posting, tagging products, changing catalogs, responding to DMs, or publishing live changes.

## 3. Production Issues
- Overlaps Content Creator, Social Media Strategist, visual design, TikTok Strategist, and commerce roles.
- Shopping tags, catalog setup, influencer partnerships, UGC, and DMs require account, rights, and privacy gates.
- Metric targets such as UGC volume and reach growth need baseline and category context.

## 4. Token Waste
- Prompt is moderate but broad across creative, commerce, and community.
- Success targets are generic without baseline data.

## 5. Ambiguity Risks
- 'Community cultivation' can imply live replies or DMs.
- Shopping setup can imply catalog/account mutation.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with visual, commerce, rights, UGC, DM, and publishing approval boundaries.

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

# Agent Review: TikTok Strategist

Source: `marketing/marketing-tiktok-strategist.md`

## 1. Current Function
TikTok channel strategist for short-form creative concepts, trend analysis, creator partnerships, community guidance, TikTok Shop, and paid creative strategy.

## 2. Current Role Boundary
Plan TikTok-native content, trend use, creator collaboration, community response, and performance strategy under brand, youth/privacy, creator, paid, and publishing approval gates.

## 3. Production Issues
- Overlaps Content Creator, Social Media Strategist, Instagram Curator, Short-Video Editing Coach, and Paid Social Strategist.
- Viral, Gen Z/Gen Alpha, creator partnership, ads, shop, and crisis language need privacy, youth, disclosure, and approval boundaries.
- High metric targets can overpromise platform outcomes.

## 4. Token Waste
- Many platform tactics repeat without requiring brand fit or rights inputs.
- Viral mechanics language should be tempered with no-guarantee framing.

## 5. Ambiguity Risks
- 'Create viral content' can imply production, posting, or paid promotion.
- Creator partnerships and Spark Ads can imply contracts, permissions, or account mutations.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around TikTok-native strategy with youth/privacy, creator, paid, music-rights, disclosure, and publishing gates.

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

# Agent Review: Video Optimization Specialist

Source: `marketing/marketing-video-optimization-specialist.md`

## 1. Current Function
Video marketing optimization specialist for YouTube/video SEO, retention structure, titles, thumbnails, chapters, metadata, and cross-platform packaging.

## 2. Current Role Boundary
Optimize video packaging, retention structure, metadata, chapters, thumbnail concepts, and syndication recommendations without uploading videos, changing channel metadata, placing ads, or altering monetization settings.

## 3. Production Issues
- Overlaps Short-Video Editing Coach, Content Creator, SEO Specialist, Social Media Strategist, and channel specialists.
- Mentions monetization, ad placement, sponsorship integration, and algorithm outcomes that require approvals and no-guarantee framing.
- Metadata and channel changes can mutate live accounts.

## 4. Token Waste
- Prompt is moderate but algorithm targets should depend on video and baseline data.
- Generic lift targets can be misleading.

## 5. Ambiguity Risks
- 'Optimize metadata' can mean recommendations or live channel edits.
- Sponsorship and monetization advice can cross legal/commercial boundaries.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as recommendation/specification role with account, rights, sponsor, monetization, and no-guarantee boundaries.

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

# Agent Review: Short-Video Editing Coach

Source: `marketing/marketing-short-video-editing-coach.md`

## 1. Current Function
Short-video editing coach for pacing, cuts, color, audio, subtitles, motion graphics, export settings, and tool-specific workflow guidance.

## 2. Current Role Boundary
Coach short-video post-production decisions, editing workflow, tool selection, export specs, and QA using supplied footage and platform requirements without uploading, publishing, or using unlicensed assets.

## 3. Production Issues
- Very long encyclopedia-style prompt with extensive software, camera, color, audio, motion, subtitle, and export guidance.
- Overlaps Video Optimization Specialist, TikTok Strategist, Instagram Curator, and production editors.
- AI asset generation, music, subtitles, templates, and export recommendations need licensing, accessibility, and platform rules.

## 4. Token Waste
- Large tutorial sections should be reference material selected by task type.
- Repeated technique catalog overwhelms the input/output contract.

## 5. Ambiguity Risks
- 'Hands-on coach' can imply editing files directly.
- Tool selection and export advice depends on supplied environment and target platforms.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite into a concise task-routed coaching prompt with references for detailed editing techniques and explicit rights, tool, platform, and publishing boundaries.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 2
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 4

Final Rating: 3.6/10
