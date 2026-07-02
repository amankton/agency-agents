# Batch Summary: batch_008

## Agents Reviewed
- `marketing/marketing-china-market-localization-strategist.md`: China Market Localization Strategist (refactor)
- `marketing/marketing-china-ecommerce-operator.md`: China E-Commerce Operator (refactor)
- `marketing/marketing-douyin-strategist.md`: Douyin Strategist (refactor)
- `marketing/marketing-kuaishou-strategist.md`: Kuaishou Strategist (rewrite)
- `marketing/marketing-xiaohongshu-specialist.md`: Xiaohongshu Specialist (refactor)
- `marketing/marketing-bilibili-content-strategist.md`: Bilibili Content Strategist (refactor)
- `marketing/marketing-wechat-official-account.md`: WeChat Official Account Manager (refactor)
- `marketing/marketing-weibo-strategist.md`: Weibo Strategist (rewrite)
- `marketing/marketing-baidu-seo-specialist.md`: Baidu SEO Specialist (keep)
- `marketing/marketing-private-domain-operator.md`: Private Domain Operator (refactor)

## Recommended Actions
- Keep: 1
- Refactor: 7
- Merge: 0
- Split: 0
- Deprecate: 0
- Rewrite: 2

## Highest-Risk Agent
Private Domain Operator: it carries the most direct customer-contact and PII risk because WeCom/SCRM tags, customer groups, private chats, Mini Program/order joins, opt-outs, and lifecycle automations can affect real people immediately.

## Biggest Architecture Issue Found
The China-market cluster has strong domain value but mixes planning, publishing, ecommerce operations, paid media, creator contracting, private-domain contact, and compliance-heavy regional execution. Batch 008 separates GTM planning from operator roles and makes live platform, store, CRM, payment, inventory, ad, customer-contact, and creator-contract actions approval-gated.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_008.md`
- `agency-audit/refactored-agents/marketing-china-market-localization-strategist.md`
- `agency-audit/refactored-agents/marketing-china-ecommerce-operator.md`
- `agency-audit/refactored-agents/marketing-douyin-strategist.md`
- `agency-audit/refactored-agents/marketing-kuaishou-strategist.md`
- `agency-audit/refactored-agents/marketing-xiaohongshu-specialist.md`
- `agency-audit/refactored-agents/marketing-bilibili-content-strategist.md`
- `agency-audit/refactored-agents/marketing-wechat-official-account.md`
- `agency-audit/refactored-agents/marketing-weibo-strategist.md`
- `agency-audit/refactored-agents/marketing-baidu-seo-specialist.md`
- `agency-audit/refactored-agents/marketing-private-domain-operator.md`
- `agency-audit/acceptance-tests/marketing-china-market-localization-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-china-ecommerce-operator.tests.md`
- `agency-audit/acceptance-tests/marketing-douyin-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-kuaishou-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-xiaohongshu-specialist.tests.md`
- `agency-audit/acceptance-tests/marketing-bilibili-content-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-wechat-official-account.tests.md`
- `agency-audit/acceptance-tests/marketing-weibo-strategist.tests.md`
- `agency-audit/acceptance-tests/marketing-baidu-seo-specialist.tests.md`
- `agency-audit/acceptance-tests/marketing-private-domain-operator.tests.md`

## Subagent Inputs Used
- GTM/ecommerce/search/private-domain scan: separated localization planning from ecommerce, Baidu SEO, WeChat OA, and private-domain owners; flagged PIPL, ICP, store, payment, inventory, and customer-contact gates.
- Platform/channel scan: refactored Douyin, Xiaohongshu, and Bilibili; rewrote Kuaishou and Weibo due to live-commerce, fan migration, trending, crisis, KOL, ad, and public-discourse risks.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: China Market Localization Strategist

Source: `marketing/marketing-china-market-localization-strategist.md`

## 1. Current Function
China GTM and localization planner for trend validation, market sizing, cultural adaptation, platform-role mapping, phase-gate planning, and evidence-backed channel strategy.

## 2. Current Role Boundary
Produce China market trend intelligence, localization strategy, channel mix, phase gates, KPI design, and specialist handoffs without mutating accounts, stores, ads, CRM, inventory, payments, or customer communications.

## 3. Production Issues
- Too full-stack: overlaps ecommerce, Baidu SEO, Douyin, Xiaohongshu, WeChat OA, private-domain, live commerce, paid media, and supply-chain roles.
- Original prompt implies execution of ad accounts, content calendars, private-domain funnels, live commerce, and dashboards.
- Trend, comment, and social listening data require source freshness, PIPL, citation, and platform-policy handling.

## 4. Token Waste
- Large playbooks and templates should be generated from scoped market inputs.
- Execution checklists imply downstream operator work that needs handoff.

## 5. Ambiguity Risks
- 'Executable GTM' can imply live implementation authority.
- Budget ranges, product selection, and supply-chain readiness need owner approval.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as GTM planner only with source freshness, compliance, PIPL, no-mutation, and explicit specialist handoff gates.

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

# Agent Review: China E-Commerce Operator

Source: `marketing/marketing-china-ecommerce-operator.md`

## 1. Current Function
China ecommerce operations specialist for Taobao, Tmall, Pinduoduo, JD, Douyin Shop, live commerce planning, marketplace campaigns, and storefront optimization.

## 2. Current Role Boundary
Plan and audit China marketplace operations, listings, pricing scenarios, promo mechanics, campaign calendars, inventory forecasts, live commerce ops, and dashboards while requiring approval for all store, price, ad, order, refund, payment, and inventory changes.

## 3. Production Issues
- Overlaps GTM strategy, Douyin/Kuaishou live commerce, Xiaohongshu seeding, private-domain retention, and paid media.
- Original prompt implies direct store operation, ad campaign execution, price changes, live commerce, inventory updates, and post-sale workflows.
- Order, refund, settlement, customer PII, and inventory data are high-risk operational surfaces.

## 4. Token Waste
- Campaign battle plans are useful but should be parameterized by platform, event, and SKU.
- Generic GMV and ROAS targets need margin and baseline data.

## 5. Ambiguity Risks
- 'Operate stores' can mean analysis, proposed changes, or live marketplace mutation.
- KOL and host management can imply contracts and payments.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with hard approval gates for store mutations, prices, discounts, ads, inventory, orders, refunds, payments, customer PII, and creator/host contracts.

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

# Agent Review: Douyin Strategist

Source: `marketing/marketing-douyin-strategist.md`

## 1. Current Function
Douyin channel strategist for short-video scripts, completion-rate planning, traffic operations recommendations, livestream commerce planning, and account diagnostics.

## 2. Current Role Boundary
Plan Douyin short-video, account positioning, content matrix, DOU+/Qianchuan recommendations, and livestream commerce strategy without posting, boosting, launching ads, operating live rooms, or changing commerce settings.

## 3. Production Issues
- Overlaps TikTok Strategist, China E-Commerce Operator, Paid Social Strategist, Short-Video Editing Coach, and China GTM.
- Touches DOU+, Qianchuan ads, matrix accounts, livestream commerce, comments, and product selling.
- Minor protection, advertising-law claims, live commerce claims, and external-platform restrictions require explicit safeguards.

## 4. Token Waste
- Platform tactics should be generated from account and performance context.
- Algorithm claims need no-guarantee framing and current evidence.

## 5. Ambiguity Risks
- 'Traffic operations' can imply live boosting or ad mutation.
- Livestream commerce planning can drift into payments, inventory, and host operations.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as Douyin planning specialist with explicit posting, boosting, paid, livestream, commerce, youth, music-rights, and claims gates.

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

# Agent Review: Kuaishou Strategist

Source: `marketing/marketing-kuaishou-strategist.md`

## 1. Current Function
Kuaishou platform strategist for lower-tier market content, trust-based community growth, fan group planning, live commerce strategy, and grassroots audience development.

## 2. Current Role Boundary
Plan Kuaishou audience, content, grassroots community, fan group, and live commerce briefs without posting, messaging fans, operating shops, changing product data, running ads, making guarantees, or executing logistics/inventory/refund actions.

## 3. Production Issues
- Overlaps Douyin Strategist, China E-Commerce Operator, Private Domain Operator, Short-Video Editing Coach, and China GTM.
- Original prompt implies fan-group setup, live commerce operations, customer service, logistics, inventory, and product curation.
- Lower-tier audience and live commerce framing require consumer protection, claims, refund, and platform policy controls.
- Mojibaked source text and heavy operator scope reduce maintainability.

## 4. Token Waste
- Long playbooks should be scoped by account maturity, product, and audience evidence.
- Cultural framing repeats authenticity principles.

## 5. Ambiguity Risks
- 'Build fan groups' can imply private-domain migration and customer contact.
- Live commerce operations can imply order, refund, inventory, or logistics authority.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as Kuaishou strategy and live-commerce brief role with explicit anti-misrepresentation, no pressure-sale, fan-contact consent, commerce, shop, inventory, refund, logistics, creator/host, and consumer-protection gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 4

Final Rating: 3.6/10


---

# Agent Review: Xiaohongshu Specialist

Source: `marketing/marketing-xiaohongshu-specialist.md`

## 1. Current Function
Xiaohongshu channel specialist for lifestyle content strategy, aesthetic storytelling, trend participation, notes, community recommendations, and KOC/UGC planning.

## 2. Current Role Boundary
Plan Xiaohongshu lifestyle positioning, note concepts, aesthetic direction, keyword/tag strategy, KOC/UGC recommendations, and community guidance without posting, commenting, DMing, seeding contracts, paid boosts, or shop mutations.

## 3. Production Issues
- Overlaps Content Creator, China GTM, China E-Commerce Operator, Instagram Curator, and social channel specialists.
- Community engagement, KOC collaboration, UGC, CTAs, and conversion tracking can imply live account or commerce actions.
- Lifestyle claims, product seeding, reviews, and before/after content need rights and disclosure controls.

## 4. Token Waste
- Moderate prompt but platform best practices should be driven by category and audience evidence.
- Generic viral metrics can overpromise.

## 5. Ambiguity Risks
- 'Engage with community' can imply comments or DMs.
- Creator partnerships can imply contracts and compensation.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with no-posting, no-DM/comment, no-creator-contract, rights, disclosure, claims, and commerce gates.

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

# Agent Review: Bilibili Content Strategist

Source: `marketing/marketing-bilibili-content-strategist.md`

## 1. Current Function
Bilibili channel strategist for UP growth, long-form video strategy, danmaku culture, cover/title planning, fan community, branded content, and platform-native monetization guidance.

## 2. Current Role Boundary
Plan Bilibili content strategy, UP creator positioning, danmaku interaction design, video packaging, community guidance, and monetization recommendations without uploading, publishing, seeding fake engagement, changing account settings, or executing brand deals.

## 3. Production Issues
- Overlaps Video Optimization Specialist, Short-Video Editing Coach, Content Creator, China GTM, and creator partnership roles.
- Prompt recommends first-hour danmaku seeding and community activation that could become engagement manipulation.
- Touches brand deals, tipping, paid courses, live streaming, ecommerce, and account/community actions.

## 4. Token Waste
- Long cultural and algorithm sections should be scoped by vertical and channel evidence.
- Success metrics need baseline and no-guarantee framing.

## 5. Ambiguity Risks
- 'Publishing and community activation' can imply live uploads and comments.
- Danmaku seeding can cross into fake engagement if not transparently bounded.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with upload, engagement, danmaku, sponsorship, live stream, monetization, rights, and no-fake-engagement gates.

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

# Agent Review: WeChat Official Account Manager

Source: `marketing/marketing-wechat-official-account.md`

## 1. Current Function
WeChat Official Account strategist for OA editorial planning, subscriber engagement, menu architecture, auto-reply design, content briefs, and conversion recommendations.

## 2. Current Role Boundary
Plan WeChat Official Account content strategy, editorial calendar, menu/auto-reply design, subscriber analytics, and Mini Program handoff recommendations without publishing, mass sending, changing menus, exporting follower data, or mutating Mini Program/payment integrations.

## 3. Production Issues
- Overlaps Private Domain Operator, WeChat/WeCom lifecycle, Mini Program commerce, CRM, and Content Creator.
- Less explicit about OA account type, send limits, content moderation, follower data, and admin mutation boundaries.
- Mass sends, menu changes, auto-replies, segmentation, and Mini Program links can affect subscribers and payments.

## 4. Token Waste
- Prompt is useful but needs account-type and send-limit context.
- Conversion language should be bounded by consent and account authority.

## 5. Ambiguity Risks
- 'Manage OA' can imply publishing or admin changes.
- Subscriber engagement can imply segmentation and data export.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor around OA account type, send limits, content moderation, PIPL, follower data, menu/admin mutation, and Mini Program/payment gates.

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

# Agent Review: Weibo Strategist

Source: `marketing/marketing-weibo-strategist.md`

## 1. Current Function
Weibo strategy specialist for public discourse, topics, Super Topics, sentiment, KOL planning, fan economy, advertising recommendations, and crisis readiness.

## 2. Current Role Boundary
Produce Weibo public-discourse strategy, topic planning, sentiment monitoring, KOL/ad recommendations, Super Topic guidance, and crisis playbooks without posting, boosting, buying trending placements, coordinating comments, running ads, or issuing crisis statements.

## 3. Production Issues
- Very broad: account operations, trending topics, Super Topics, fan culture, KOLs, ads, sentiment, crisis, commerce, and analytics.
- Closest to public narrative manipulation, crisis response, paid amplification, coordinated commenting, and bot-like engagement risks.
- Advertising, KOL contracts, public statements, sensitive topics, and fan operations need strict approval and compliance gates.

## 4. Token Waste
- Large operational playbook should be reduced to decision trees and handoff templates.
- Trending and crisis examples imply execution authority.

## 5. Ambiguity Risks
- 'Make your brand trend' can imply buying/boosting or manipulating public discourse.
- Comment management can imply coordinated or fake engagement.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as public-discourse strategy and risk role with no live posting, no manipulation, no crisis authority, and strict ad/KOL/compliance gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 3
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 4
- Orchestration Fit: 3

Final Rating: 3.4/10


---

# Agent Review: Baidu SEO Specialist

Source: `marketing/marketing-baidu-seo-specialist.md`

## 1. Current Function
Baidu organic SEO specialist for Chinese search visibility, ICP readiness, technical SEO, Baidu webmaster recommendations, keyword strategy, content briefs, and ecosystem trust signals.

## 2. Current Role Boundary
Assess and improve Baidu organic search readiness through ICP/hosting checks, technical SEO audits, Chinese keyword research, content briefs, Baidu ecosystem recommendations, and compliance-aware handoffs without publishing, paid SEM changes, fake seeding, or click manipulation.

## 3. Production Issues
- Minor overlap with China GTM, content strategy, SEM, reputation management, and technical web roles.
- ICP, China hosting, content moderation, and data localization advice need citation and legal-review boundaries.
- Baidu ecosystem seeding can drift into fake Q&A, reputation manipulation, or click manipulation.

## 4. Token Waste
- SEO checklists are useful but should depend on site and ICP status.
- Ranking targets need no-guarantee framing.

## 5. Ambiguity Risks
- 'Build authority' can imply manipulative seeding.
- ICP guidance can sound like legal advice.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Keep as Baidu organic SEO role with stronger no-manipulation, ICP/legal citation, data-localization, analytics privacy, and SEM handoff boundaries.

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

# Agent Review: Private Domain Operator

Source: `marketing/marketing-private-domain-operator.md`

## 1. Current Function
Private-domain and WeCom lifecycle operations specialist for SCRM architecture, community SOPs, segmentation design, consented outreach, Mini Program handoffs, and retention analytics.

## 2. Current Role Boundary
Design WeCom/SCRM private-domain lifecycle systems, segmentation, consented outreach templates, community SOPs, Mini Program handoffs, and reporting without directly messaging customers, adding groups, writing tags, changing automations, or joining payment/order data without approval.

## 3. Production Issues
- Highest private-data and direct-customer-contact risk in the batch.
- Overlaps ecommerce retention, WeChat OA, Mini Program commerce, customer service, sales, and data/identity roles.
- Original prompt includes auto-tagging, group operations, private chat scripts, order joins, coupons, payment data, and customer outreach.

## 4. Token Waste
- Long configuration examples should become implementation specs gated by SCRM authority.
- SQL and automation examples imply direct data access and writes.

## 5. Ambiguity Risks
- 'Operate private domain' can imply direct customer contact.
- Segmentation and churn prediction can become profiling without consent and governance.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with strict PIPL, consent, opt-out, PII minimization, profiling, SCRM write, customer-contact, payment/order, and Mini Program approval gates.

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
