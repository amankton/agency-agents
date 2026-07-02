# Orchestration Map

## Target Flow
1. Intake Router classifies the user request and builds a clean task payload.
2. Planner converts the payload into ordered work, dependencies, and acceptance criteria.
3. Specialist Execution Agents perform bounded production work.
4. Safety gates block live mutation until authorization, approval, rollback, and evidence requirements are satisfied.
5. QA / Validation Agents verify outputs against acceptance criteria and evidence.
6. Memory / State Agent stores only approved state, decisions, and handoff summaries.
7. Final Response Agent packages completed work, risks, and next actions.

## Required Handoff Payload
```json
{
  "handoff_id": "HANDOFF_ID",
  "source_agent": "SOURCE_AGENT",
  "target_agent": "TARGET_AGENT",
  "task_id": "TASK_ID",
  "handoff_reason": "REASON",
  "context_summary": "SUMMARY",
  "inputs_used": {},
  "outputs_produced": {},
  "open_questions": [],
  "known_constraints": [],
  "risks": [],
  "recommended_next_action": "NEXT_ACTION"
}
```

## Completed Batch Agent Scope
- `specialized/agents-orchestrator.md`: Agents Orchestrator (split)
- `specialized/specialized-workflow-architect.md`: Workflow Architect (merge)
- `project-management/project-manager-senior.md`: Senior Project Manager (keep)
- `testing/testing-evidence-collector.md`: Evidence Collector (refactor)
- `testing/testing-reality-checker.md`: Reality Checker (refactor)
- `engineering/engineering-autonomous-optimization-architect.md`: Autonomous Optimization Architect (rewrite)
- `security/security-penetration-tester.md`: Penetration Tester (rewrite)
- `engineering/engineering-ai-data-remediation-engineer.md`: AI Data Remediation Engineer (rewrite)
- `engineering/engineering-incident-response-commander.md`: Incident Response Commander (split)
- `paid-media/paid-media-ppc-strategist.md`: PPC Campaign Strategist (refactor)
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
- `specialized/sales-outreach.md`: Sales Outreach (deprecate)
- `sales/sales-outbound-strategist.md`: Outbound Strategist (keep)
- `sales/sales-offer-lead-gen-strategist.md`: Offer & Lead Gen Strategist (keep)
- `sales/sales-account-strategist.md`: Account Strategist (keep)
- `specialized/customer-success-manager.md`: Customer Success Manager (refactor)
- `support/support-support-responder.md`: Support Responder (split)
- `specialized/customer-service.md`: Customer Service (refactor)
- `sales/sales-pipeline-analyst.md`: Pipeline Analyst (refactor)
- `sales/sales-deal-strategist.md`: Deal Strategist (keep)
- `sales/sales-proposal-strategist.md`: Proposal Strategist (keep)
- `product/product-feedback-synthesizer.md`: Feedback Synthesizer (refactor)
- `product/product-sprint-prioritizer.md`: Sprint Prioritizer (merge)
- `product/product-trend-researcher.md`: Trend Researcher (keep)
- `product/product-behavioral-nudge-engine.md`: Behavioral Nudge Engine (rewrite)
- `project-management/project-management-project-shepherd.md`: Project Shepherd (refactor)
- `project-management/project-management-studio-producer.md`: Studio Producer (refactor)
- `project-management/project-management-studio-operations.md`: Studio Operations (keep)
- `project-management/project-management-experiment-tracker.md`: Experiment Tracker (rewrite)
- `project-management/project-management-jira-workflow-steward.md`: Jira Workflow Steward (keep)
- `project-management/project-management-meeting-notes-specialist.md`: Meeting Notes Specialist (keep)
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
- `engineering/engineering-feishu-integration-developer.md`: Feishu Integration Developer (refactor)
- `engineering/engineering-email-intelligence-engineer.md`: Email Intelligence Engineer (refactor)
- `engineering/engineering-voice-ai-integration-engineer.md`: Voice AI Integration Engineer (refactor)
- `engineering/engineering-wechat-mini-program-developer.md`: WeChat Mini Program Developer (refactor)
- `engineering/engineering-solidity-smart-contract-engineer.md`: Solidity Smart Contract Engineer (refactor)
- `engineering/engineering-embedded-firmware-engineer.md`: Embedded Firmware Engineer (refactor)
- `specialized/specialized-mcp-builder.md`: MCP Builder (refactor)
- `specialized/specialized-salesforce-architect.md`: Salesforce Architect (refactor)
- `specialized/data-consolidation-agent.md`: Data Consolidation Agent (refactor)
- `specialized/report-distribution-agent.md`: Report Distribution Agent (refactor)
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
- `finance/finance-bookkeeper-controller.md`: Bookkeeper & Controller (split)
- `finance/finance-financial-analyst.md`: Financial Analyst (refactor)
- `finance/finance-fpa-analyst.md`: FP&A Analyst (refactor)
- `finance/finance-tax-strategist.md`: Tax Strategist (rewrite)
- `finance/finance-investment-researcher.md`: Investment Researcher (refactor)
- `specialized/legal-document-review.md`: Legal Document Review (split)
- `specialized/legal-client-intake.md`: Legal Client Intake (refactor)
- `specialized/legal-billing-time-tracking.md`: Legal Billing & Time Tracking (split)
- `specialized/healthcare-customer-service.md`: Healthcare Customer Service (refactor)
- `specialized/healthcare-marketing-compliance.md`: Healthcare Marketing Compliance Specialist (rewrite)
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
- `academic/academic-historian.md`: Historian (refactor)
- `academic/academic-geographer.md`: Geographer (refactor)
- `academic/academic-anthropologist.md`: Anthropologist (refactor)
- `academic/academic-narratologist.md`: Narratologist (refactor)
- `academic/academic-psychologist.md`: Psychologist (refactor)
- `specialized/study-abroad-advisor.md`: Study Abroad Advisor (refactor)
- `specialized/grant-writer.md`: Grant Writer (refactor)
- `specialized/recruitment-specialist.md`: Recruitment Specialist (refactor)
- `specialized/language-translator.md`: Language Translator (refactor)
- `specialized/personal-growth-mentor.md`: Personal Growth Mentor (refactor)
- `marketing/marketing-pr-communications-manager.md`: PR & Communications Manager (rewrite)
- `specialized/hr-onboarding.md`: HR Onboarding (refactor)
- `specialized/business-strategist.md`: Business Strategist (refactor)
- `specialized/change-management-consultant.md`: Change Management Consultant (refactor)
- `specialized/supply-chain-strategist.md`: Supply Chain Strategist (rewrite)
- `sales/sales-engineer.md`: Sales Engineer (refactor)
- `sales/sales-coach.md`: Sales Coach (refactor)
- `marketing/marketing-global-podcast-strategist.md`: Global Podcast Strategist (refactor)
- `marketing/marketing-podcast-strategist.md`: Podcast Strategist (refactor)
- `integrations/mcp-memory/backend-architect-with-memory.md`: Backend Architect (deprecate)
- `specialized/real-estate-buyer-seller.md`: Real Estate Buyer & Seller (split)
- `specialized/hospitality-guest-services.md`: Hospitality Guest Services (refactor)
- `specialized/government-digital-presales-consultant.md`: Government Digital Presales Consultant (refactor)
- `marketing/marketing-cross-border-ecommerce.md`: Cross-Border E-Commerce Specialist (split)
- `marketing/marketing-zhihu-strategist.md`: Zhihu Strategist (refactor)
- `specialized/loan-officer-assistant.md`: Loan Officer Assistant (split)
- `specialized/specialized-chief-of-staff.md`: Chief of Staff (split)
- `specialized/specialized-pricing-analyst.md`: Pricing Analyst (rewrite)
- `specialized/medical-billing-coding-specialist.md`: Medical Billing & Coding Specialist (split)
- `specialized/retail-customer-returns.md`: Retail Customer Returns (split)
- `engineering/engineering-it-service-manager.md`: IT Service Manager (split)
- `engineering/engineering-cms-developer.md`: CMS Developer (refactor)
- `engineering/engineering-git-workflow-master.md`: Git Workflow Master (rewrite)
- `specialized/lsp-index-engineer.md`: LSP/Index Engineer (refactor)
- `specialized/corporate-training-designer.md`: Corporate Training Designer (refactor)
- `specialized/specialized-french-consulting-market.md`: French Consulting Market Navigator (rewrite)
- `sales/sales-discovery-coach.md`: Discovery Coach (deprecate)
- `specialized/specialized-civil-engineer.md`: Civil Engineer (split)
- `specialized/accounts-payable-agent.md`: Accounts Payable Agent (rewrite)
- `marketing/marketing-livestream-commerce-coach.md`: Livestream Commerce Coach (split)
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
- `marketing/marketing-book-co-author.md`: Book Co-Author (refactor)
- `marketing/marketing-email-strategist.md`: Email Marketing Strategist (refactor)
- `specialized/specialized-korean-business-navigator.md`: Korean Business Navigator (refactor)
- `game-development/unreal-engine/unreal-world-builder.md`: Unreal World Builder (refactor)
- `game-development/unity/unity-shader-graph-artist.md`: Unity Shader Graph Artist (refactor)
- `game-development/unreal-engine/unreal-multiplayer-architect.md`: Unreal Multiplayer Architect (refactor)
- `game-development/unreal-engine/unreal-technical-artist.md`: Unreal Technical Artist (refactor)
- `specialized/zk-steward.md`: ZK Steward (rewrite)
- `testing/testing-test-results-analyzer.md`: Test Results Analyzer (refactor)
- `testing/testing-tool-evaluator.md`: Tool Evaluator (refactor)
- `game-development/unity/unity-editor-tool-developer.md`: Unity Editor Tool Developer (refactor)
- `game-development/unity/unity-multiplayer-engineer.md`: Unity Multiplayer Engineer (refactor)
- `game-development/roblox-studio/roblox-systems-scripter.md`: Roblox Systems Scripter (refactor)
- `game-development/roblox-studio/roblox-avatar-creator.md`: Roblox Avatar Creator (refactor)
- `game-development/roblox-studio/roblox-experience-designer.md`: Roblox Experience Designer (refactor)
- `support/support-legal-compliance-checker.md`: Legal Compliance Checker (split)
- `testing/testing-workflow-optimizer.md`: Workflow Optimizer (merge)
- `support/support-infrastructure-maintainer.md`: Infrastructure Maintainer (merge)
- `support/support-analytics-reporter.md`: Analytics Reporter (refactor)
- `support/support-finance-tracker.md`: Finance Tracker (merge)
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

## Routing Notes
- `Agents Orchestrator` should route and track workflow state, not implement or certify work.
- `Workflow Architect` should map workflows and contracts, not implement.
- `Evidence Collector` validates a task. `Reality Checker` validates release readiness.
- Autonomous routing, penetration testing, data remediation, incident response, and paid-media mutation must default to read-only planning until explicit gates are satisfied.
- Sales and post-sale agents should route by lifecycle stage: offer -> outbound -> active deal -> proposal -> pipeline analytics -> customer success -> support or account expansion.
- Support and customer-service agents must use approved policies, verification rules, and escalation thresholds before promising refunds, credits, cancellations, roadmap items, or account changes.
- Product specialists should feed Product Manager decisions: feedback synthesis and trend research provide evidence; sprint planning provides PM-approved delivery options; behavioral nudges and experiments require consent, privacy, and guardrail review.
- Project-management agents should separate delivery coordination, studio portfolio planning, operations/SOP work, experiment registry tracking, Jira/Git traceability, and meeting-note extraction.
- Security program agents should separate architecture, AppSec, cloud guardrails, detection engineering, incident response, compliance evidence, intelligence products, and authorized assessment scopes.
- Identity, model, and automation-governance agents should default to proposal or audit artifacts until data access, mutation authority, independence, privacy, and rollback gates are explicit.
- Paid-media agents should separate audit, channel strategy, creative, programmatic, PPC/search-query, and tracking roles; all spend, bid, budget, audience, tracking, and campaign changes require explicit approval.
- Search-growth agents should separate growth experiment planning, ASO, traditional SEO, AI citation, AEO foundations, and agentic-search readiness; website, app-store, content, crawler-policy, transactional-flow, and analytics mutations require specialist handoff and approval.
- Broad marketing agents should route by job: content source draft -> social strategy -> channel specialist -> draft-only publisher -> intelligence/QA. Posts, comments, DMs, follows, profile edits, uploads, ad changes, creator contracts, and live publishing require explicit approval and account authority.
- Video roles should separate strategy and packaging from post-production execution: Video Optimization owns metadata, retention, and packaging recommendations; Short-Video Editing Coach owns edit workflow and QA; neither uploads or changes live channel settings by default.
- China-market agents should route GTM planning to regional operators: localization plans feed ecommerce, Baidu SEO, Douyin, Kuaishou, Xiaohongshu, Bilibili, WeChat OA, Weibo, and private-domain owners; all live publishing, paid spend, creator contracts, customer contact, store mutations, inventory, refunds, payments, and SCRM writes require explicit approval.
- China compliance gates should cover PIPL, advertising-law claims, content moderation, ICP/hosting readiness, data localization, creator disclosure, platform terms, sensitive topics, and opt-out suppression before execution handoff.
- Engineering agents should route by decision right: Software Architect owns ADRs/domain boundaries; Backend Architect owns backend contracts; implementers own scoped repo tasks; Code Reviewer reviews independently; SRE owns reliability advice; database/data/AI/prompt roles require explicit data, model, migration, deploy, secrets, and rollback gates before mutation.
- Engineering implementation defaults to branch/PR scoped changes with tests and CI evidence. Production deployments, infrastructure changes, DB migrations, data backfills, model releases, prompt rollouts, and secret access are blocked until authority, review, and rollback are explicit.
- Tool/API integration agents should default to local, sandbox, fork, dry-run, preview, or read-only mode. Feishu, WeChat Mini Program, Salesforce, email, voice, MCP, report distribution, smart-contract, and firmware work must require explicit tenant/account, credential, data, send, deploy, flash, or broadcast authority before mutation.
- Integration routing should separate capability design from live execution: MCP Builder creates governed tool contracts; Feishu/WeChat/Salesforce specialists own platform specs; Email and Voice AI produce privacy-filtered context; Data Consolidation prepares report artifacts; Report Distribution sends only after recipient ACL, idempotency, and approval checks; Solidity and Firmware require independent audit/test evidence before irreversible actions.
- Design and UX agents should route by artifact type: UX Research owns research evidence and persona-walkthrough hypotheses; UX Architect owns IA/layout foundations only; UI Designer owns component/screen specs; Brand Guardian owns guidelines; Visual Storyteller owns narrative specs; Image Prompt Engineer owns prompt artifacts; Inclusive Visuals and Cultural Intelligence provide representation and locale review.
- Design work defaults to draft, review, and handoff artifacts. Live Figma/design-system publishing, repo edits, public brand changes, user research contact, analytics experiments, image generation, asset uploads, and cultural/legal/community claims require source evidence, rights, consent, accessibility review, and explicit approval.
- Finance/legal/healthcare agents should default to draft, review, and handoff artifacts. Bookkeeping, FP&A, financial analysis, tax, investment research, legal review, intake, billing, patient support, and healthcare marketing work require source evidence, jurisdiction/entity/matter/patient scope, confidentiality/privacy controls, and licensed-owner review before action.
- High-stakes vertical agents must block licensed advice and live mutation by default: no filings, elections, trades, fund movement, journal posting, invoice sends, trust disbursements, conflict clearance, clinical advice, PHI disclosure, or regulated healthcare content publication without explicit authority and audit trail.
- Game and spatial agents should route by artifact and engine: Game Designer owns mechanics/GDD; Level Designer owns layout/blockout specs; Narrative Designer owns dialogue/lore/branching; Technical Artist owns pipeline/performance handoffs; Unity, Unreal, Godot, WebXR, and visionOS specialists own scoped implementation only under declared version, repo, device, and test boundaries.
- Game/XR work must block live editor, asset, build, app-store, account, device, sensor-data, and publishing mutations by default. Engine/platform claims require official source/version validation; asset generation and reuse require rights checks; performance, comfort, accessibility, and device validation require evidence.
- Academic agents should route by evidence type: Historian owns time/place and source-backed period claims; Geographer owns physical/human geography constraints; Anthropologist owns cultural-system coherence with ethics review; Narratologist owns story-structure frameworks; Academic Psychologist owns fictional psychological plausibility only.
- Study-abroad, grant, recruitment, translation, and coaching agents should remain advisory/draft-first. Admissions, visa, grant, HR, translation, and coaching outputs require current sources, privacy controls, consent, professional escalation, and explicit approval before submissions, outreach, background checks, portal actions, or high-stakes reliance.
- Enterprise advisory agents should route by decision right: Business Strategist frames options and scenarios; Change Management Consultant plans adoption; HR Onboarding coordinates approved onboarding artifacts; PR & Communications Manager drafts messages; Supply Chain Strategist advises sourcing and risk. Executive, HR, legal, procurement, finance, communications, and system owners approve live actions.
- PR, change, HR, and supply-chain work must remain draft/read-only until facts, source dates, employee/supplier/customer data rights, legal/HR/privacy review, publish/outreach/procurement authority, and rollback/audit owners are explicit. No announcements, journalist outreach, supplier contact, tenders, contracts, POs, HRIS/payroll/ERP/SRM writes, or regulated claims by default.
- Sales technical and coaching roles should route separately: Sales Engineer owns technical discovery, demo, and POC specifications from approved product/security claims; Sales Coach owns behavior-focused coaching artifacts from authorized rep and deal evidence. CRM changes, customer-environment work, personnel decisions, forecast approval, and customer/prospect contact require account, manager, RevOps, HR, or technical-owner approval.
- Podcast agents should use a base-plus-extension model: Global Podcast Strategist owns platform-neutral show strategy, analytics, growth, and monetization planning; Podcast Strategist owns China/regional platform adaptation. Publishing, uploads, guest outreach, sponsorships, account changes, community operations, ecommerce, paid spend, and rights/legal clearance route to specialist owners.
- Memory variants should be migrated into governed extensions rather than duplicate agents. Backend Architect with Memory is deprecated in favor of canonical Backend Architect plus Memory/State Service rules for allowed state, data classification, retention, deletion, stale-memory invalidation, access control, and no secrets, PII, raw customer data, or hidden reasoning.
- Regulated vertical operators should route by licensed owner and system boundary. Real estate, lending, medical billing, pricing, government presales, and retail returns can draft evidence packets and recommendations, but legal, credit, coding, pricing, procurement, refund, claim, contract, MLS, LOS, POS, PMS, payment, and payer actions require the accountable owner.
- Customer-transaction roles must verify identity, consent, policy, and source evidence before drafting. Guest, borrower, patient, customer, client, and lead data should be minimum-necessary, redacted where possible, and never used to make unauthorized credit, refund, fraud, health, legal, fair-housing, pricing, or eligibility decisions.
- China/platform commercial roles should separate content and market strategy from live account operations. Cross-border ecommerce and Zhihu strategy can prepare plans and drafts, but listings, prices, ads, inventory, orders, refunds, payments, lead capture, comments, DMs, influencer outreach, and account changes require platform-account, privacy, legal/tax/IP, or marketplace owner approval.
- Chief of Staff should prepare context, escalation, and decision artifacts only under explicit principal delegation. Project ownership, workflow architecture, global routing, HR/finance/legal commitments, document updates, and system-of-record mutations route to the existing project, workflow, executive, legal, finance, HR, or system owners.
- Service and workflow enablement roles should separate advisory artifacts from system mutation. ITSM drafts, CMS local/staging work, Git advice, LSP local/sandbox indexing, and training design can proceed from approved evidence; ticket/change/CMDB writes, production CMS/admin/database/deploys, remote Git history, hooks/egress, LMS/HR/compliance records, and employee communications require accountable owner approval.
- Financial, safety, and commercial operations roles should be control-first. Accounts Payable prepares verification and approval packets only; Civil Engineer drafts advisory calculations for licensed EOR review; French Consulting Market Navigator provides sourced market support without legal/tax/employment advice; Livestream Commerce Coach coaches without live operations, spend, price, order, or customer actions; Discovery Coach routes to Sales Coach.
- Tooling and document/data agents should default to local, dry-run, draft, or staging artifacts. Document generation, Sales Excel ingestion, OrgScript modeling, terminal integration, and executive summaries require source lineage, overwrite/write boundaries, privacy controls, validation commands, and explicit owner approval before file, database, automation, shell, or distribution actions.
- Spatial and community-growth agents should separate strategy/specification from public or device execution. XR cockpit work merges into XR Interface Architect; macOS Metal work routes rendering/performance and visionOS integration separately; Reddit, carousel, and developer-advocacy roles can draft and analyze, but posts, comments, DMs, ads, generated final assets, credentials, self-scheduling, device deploys, and roadmap commitments require accountable owner approval.
- Publishing, regional-advisory, QA, and procurement agents should remain evidence-first. Book Co-Author drafts require author source/IP approval; Email Strategist cannot send or mutate ESP/CRM/DNS; Korean Business Navigator cannot contact or negotiate; Test Results Analyzer feeds but does not replace Reality Checker; Tool Evaluator cannot contact vendors, spend, sign, or integrate production tools.
- Game-engine specialists should validate engine and platform versions before implementation claims. Unreal World Builder, Unity Shader Graph Artist, Unreal Multiplayer Architect, and Unreal Technical Artist can draft specs and scoped implementation plans, but editor/asset/shader/PCG/HLOD/networking/server/source-control/build mutations require project owner approval, rights checks, profiling evidence, and rollback.
- ZK Steward should route durable state to the governed Memory/State Service. Knowledge-network outputs are read-only plans and link suggestions until vault root, allowed paths, privacy class, retention/deletion rules, daily-log policy, and memory-sync approval are explicit.
- Unity/Roblox production roles should route specs before editor or live action. Asset/source-control/backend/Relay/Lobby/DataStore/economy/place/Marketplace/publish/pricing/moderation/monetization changes require project owner approval, tests, rights checks, and rollback.
- Support operations tail roles should route legal/compliance to counsel or compliance owners, workflow optimization to Workflow Architect, infrastructure maintenance to SRE/DevOps, analytics to the data pipeline, and finance tracking to the finance cluster. Legal/financial advice, production changes, automations, dashboard sends, budget/spend/payment, and journal actions are blocked by default.
- Final engineering tail roles should route by intent: onboarding stays read-only, minimal changes stay scoped, technical writing stays source-grounded, Filament/admin changes require project owner tests, mobile work requires platform/release gates, and prototypes stay explicitly non-production until hardened.
- Final game/DCC tail roles should route by engine/tool and artifact. Blender, audio, Godot multiplayer, and Godot shader work can draft specs and scoped local changes, but scene/asset/material/audio middleware/project-setting/network/server/export/build mutations require owner approval, version evidence, profiling where relevant, and rollback.
