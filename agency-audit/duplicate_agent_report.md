# Duplicate Agent Report

## Summary
The most important duplication is not exact text duplication; it is responsibility overlap. Several agents try to own coordination, validation, customer interaction, sales outreach, or cross-session context without a shared contract.

## High-Priority Overlaps
| Agents | Overlap | Recommendation |
|---|---|---|
| Backend Architect; Backend Architect with Memory | Same backend role with memory text appended in integration variant. | Merge memory rules into canonical agent as optional extension. |
| Agents Orchestrator; Workflow Architect; Chief of Staff; Project Shepherd | Coordination, routing, state, and handoff ownership blur together. | Split by intake/routing, workflow specification, executive context, and project coordination. |
| Evidence Collector; Reality Checker | Both demand evidence and screenshots; one task-level, one release-level. | Keep both, but define handoff and severity thresholds. |
| Sales Outreach; Outbound Strategist; Offer and Lead Gen Strategist | Top-of-funnel sales ownership overlaps. | Merge or establish sequence: offer -> prospecting strategy -> outreach execution. |
| Product Manager; Feedback Synthesizer; Sprint Prioritizer; Trend Researcher | Product Manager absorbs specialist responsibilities. | Refactor PM as product coordinator and keep specialists as bounded input producers. |
| Support Responder; Customer Service; vertical service agents | Support interaction, customer success, KB, and vertical escalation overlap. | Split support operations from interaction; keep verticals as constrained extensions. |
| PPC Strategist; Search Query Analyst; Paid Media Auditor | Paid search audit and optimization responsibilities overlap. | Scope by account strategy, query mining, and audit validation. |

## Additional Findings From Parallel Scans
- Sales Outreach, Outbound Strategist, and Offer and Lead Gen Strategist overlap on top-of-funnel pipeline creation. Make Outbound Strategist canonical and merge or deprecate the specialized Sales Outreach variant.
- Product Manager overlaps Feedback Synthesizer, Sprint Prioritizer, Trend Researcher, sales, marketing, and support readiness. Refactor PM as coordinator, not super-agent.
- Support Responder overlaps generic Customer Service and vertical service agents. Split support operations from customer interaction.
- Podcast Strategist and Global Podcast Strategist are mostly regional variants and should share a common base or merge with `market_context`.
- Analytics/reporting agents should form a pipeline: extract -> consolidate -> domain analyze -> summarize -> generate/distribute.

## Batch 001 Decisions
- Split `specialized/agents-orchestrator.md` into router/controller responsibilities and downstream planner/validator roles.
- Keep `specialized/specialized-workflow-architect.md`, but bound discovery and require structured workflow outputs.
- Refactor Evidence Collector and Reality Checker as task-level QA and release-level QA respectively.
- Rewrite or split high-risk mutation agents so read-only analysis is the default until approval gates are satisfied.

## Batch 002 Decisions
- Rewrite or refactor remaining safety-sensitive security, DevOps, paid-media, testing, product, and detection agents.
- Keep read-only/default planning behavior for incident response, DevOps, ad-platform changes, tracking tags, performance tests, and SIEM deployment.
- Split Product Manager away from specialist product agents by making it a coordinator and artifact router.

## Batch 003 Decisions
- Deprecate the broad `specialized/sales-outreach.md` prompt as a legacy routing shim instead of a canonical execution agent.
- Keep narrower sales specialists as canonical owners for outbound strategy, offer/lead-gen strategy, account expansion, active deal strategy, and proposal artifacts.
- Refactor Customer Success Manager and Customer Service around explicit support, sales, product, legal, billing, and vertical-service handoffs.
- Split Support Responder into bounded support response/routing versus support-ops analytics responsibilities.

## Batch 004 Decisions
- Keep Product Trend Researcher, Studio Operations, Jira Workflow Steward, and Meeting Notes Specialist with source, authority, and no-mutation boundaries.
- Refactor Feedback Synthesizer and Studio Producer so they synthesize evidence and planning options without owning final product or executive decisions.
- Merge Sprint Prioritizer into Product Manager delivery planning, or keep only as a PM-approved sprint-planning sub-role.
- Merge Project Shepherd into Senior Project Manager, or keep only as a narrow active-project coordination alias.
- Rewrite Behavioral Nudge Engine and Experiment Tracker around consent, privacy, data quality, guardrails, and explicit approval.

## Batch 005 Decisions
- Refactor Threat Intelligence, Cloud Security Architect, AppSec Engineer, Blockchain Security Auditor, Automation Governance Architect, Agentic Identity Trust, and Identity Graph Operator around authorized scope, draft-only outputs, and handoff gates.
- Keep Compliance Auditor and Model QA Specialist with stronger evidence minimization, independence, and sensitive-data access controls.
- Rewrite Security Architect as architecture-artifact owner only, routing code review, scans, SOC work, incident response, and offensive testing to completed specialist agents.
- Replace the originally planned Threat Detection Engineer candidate with `specialized/identity-graph-operator.md` because Threat Detection Engineer was completed in batch 002.

## Batch 006 Decisions
- Refactor Paid Media Auditor, Ad Creative Strategist, and Programmatic Buyer around read-only evidence, proposed changes, spend approval, audience privacy, and measurement gates.
- Keep Paid Social Strategist with clearer campaign-launch, budget, tracking, custom-audience, CRM-sync, and privacy-review boundaries.
- Refactor Growth Hacker into an ethical experiment strategist with anti-spam, anti-dark-pattern, consent, measurement, and specialist-handoff constraints.
- Keep App Store Optimizer, AI Citation Strategist, and SEO Specialist as bounded specialists with publishing, claim, source-verification, privacy, and handoff gates.
- Rewrite Agentic Search Optimizer as an evidence-based readiness auditor/spec writer because implementation-level WebMCP, checkout, booking, auth, payment, and PII flows require current-source validation plus engineering/security approval.
- Refactor AEO Foundations around crawler policy, legal/content licensing, privacy, deployment, and crawl-log measurement approvals.

## Batch 007 Decisions
- Refactor Content Creator as the platform-neutral source-draft and brand-storytelling role; it no longer owns publishing, accounts, final campaign execution, or channel-specific operations.
- Refactor Social Media Strategist as planner/coordinator for channel mix, calendar, campaign briefs, and reporting; platform specialists and publishers execute under approval.
- Keep Multi-Platform Publisher as draft-only distribution orchestrator with human confirmation, account/auth verification, no-secret-echo, copyright, rate-limit, and no-live-publish gates.
- Refactor Twitter Engager, LinkedIn Content Creator, Instagram Curator, TikTok Strategist, and Video Optimization Specialist around account, posting, DM/comment, paid, rights, brand, crisis, and platform-policy approvals.
- Keep X/Twitter Intelligence Analyst as evidence-only research and monitoring role with no posting, replying, liking, following, DMing, automated engagement, or doxxing.
- Rewrite Short-Video Editing Coach into a concise post-production coaching role with rights, raw-footage privacy, AI-media disclosure, tool, export, accessibility, and no-publishing boundaries.

## Batch 008 Decisions
- Refactor China Market Localization Strategist as GTM planner only, with trend evidence, China compliance, PIPL, ICP/platform, paid-media, and no-live-mutation gates.
- Refactor China E-Commerce Operator around marketplace operations planning and audit artifacts; store, listing, price, coupon, ad, order, refund, payment, inventory, customer PII, and KOL/host actions require approval.
- Refactor Douyin, Xiaohongshu, Bilibili, WeChat OA, and Private Domain roles around strategy/specification outputs with posting, messaging, publishing, account, creator, commerce, PIPL, and platform-policy gates.
- Rewrite Kuaishou Strategist because live-commerce, shop ops, logistics, refunds, fan groups, and WeChat/private-domain migration are too entangled for a safe light refactor.
- Rewrite Weibo Strategist as public-discourse strategy and risk planning only; it must not execute crisis statements, trending buys, coordinated comments, ad spend, KOL contracts, or commerce links.
- Keep Baidu SEO Specialist as organic search/readiness role with no fake Q&A, click manipulation, paid SEM mutation, or legal-certification claims.

## Batch 009 Decisions
- Keep Software Architect as cross-system ADR/domain-boundary role and Code Reviewer as independent diff-review role; neither writes or deploys code by default.
- Keep SRE with light refactor around SLOs, observability, runbooks, rollout risk, rollback criteria, privacy-aware telemetry, and no production mutation without approval.
- Refactor Backend Architect, Frontend Developer, and Senior Developer around scoped task/repo authority, tests, CI, code review, deploy approval, secrets handling, and architecture handoffs.
- Refactor Database Optimizer around query-plan evidence, production read-only default, PII/RLS/tenant constraints, backup/restore, migration dry runs, lock budgets, rollback, and DBA/app-owner approval.
- Refactor Data Engineer around data contracts, PII classification, retention/deletion, residency, backfill approval, idempotency/replay gates, quality checks, lineage, and consumer signoff.
- Refactor AI Engineer around dataset provenance, model registry/release gates, eval thresholds, RAG/prompt-injection security, privacy, canary/rollback, monitoring, and human review for high-impact decisions.
- Refactor Prompt Engineer around prompt specs, versioning, regression tests, eval dataset governance, model-version pinning, rollout approval, rollback, privacy redaction, and no hidden chain-of-thought exposure.

## Batch 010 Decisions
- Refactor Feishu Integration Developer and WeChat Mini Program Developer around tenant/account authority, OAuth/session secrets, webhook/payment verification, platform review, PIPL, message/payment mutation, and release gates.
- Refactor Email Intelligence Engineer and Voice AI Integration Engineer around consent, PII/PHI, tenant isolation, retention/deletion, attachment/audio handling, citation/timestamp integrity, vendor policy, and no-send/no-write defaults.
- Refactor Solidity Smart Contract Engineer and Embedded Firmware Engineer around local/fork/test-device defaults, irreversible deployment/flashing risks, private keys, real funds, OTA, fuses, hardware recovery, audit/static/HIL tests, and signed authority gates.
- Refactor MCP Builder as the highest-risk tool-expansion role, with capability registry, least-privilege auth, typed schemas, structured errors, destructive-action blocks, real-agent tests, deploy approval, and rollback gates.
- Refactor Salesforce Architect around read-only architecture artifacts, CRM PII, permissions, governor-limit evidence, integration inventory, metadata/data/automation deployment gates, reconciliation, and rollback.
- Refactor Data Consolidation Agent and Report Distribution Agent around source ACLs, metric definitions, territory permissions, freshness/reconciliation, dry-run preview, recipient allowlists, idempotency, send approval, and immutable audit logs.

## Batch 011 Decisions
- Refactor UI Designer, UX Researcher, Brand Guardian, Visual Storyteller, Whimsy Injector, Image Prompt Engineer, and Inclusive Visuals Specialist around source evidence, artifact-only defaults, accessibility, asset rights, representation, consent, and implementation handoff gates.
- Split UX Architect because it blends UX/IA/CSS foundations with system architecture, repository topology, API/schema authority, deployment, and agent coordination that belong to engineering and workflow owners.
- Merge Persona Walkthrough into UX Researcher as a qualitative CRO/persona mode with explicit caveats, page evidence, no protected-class stereotyping, no dark patterns, and validation handoffs.
- Split Cultural Intelligence Strategist into bounded cultural research/localization audit and product-inclusion advisory modes with current sourced evidence, no universal group claims, no protected-class profiling, imagery handoffs, and legal/privacy routing.
- Treat Inclusive Visuals and Cultural Intelligence as the highest representation-risk roles because they can encode stereotypes, tokenism, cultural overgeneralizations, or unsupported community claims into downstream design assets.

## Batch 012 Decisions
- Split Bookkeeper & Controller around bookkeeping execution versus controller approval, with ERP, bank, payroll, journal, period-lock, prior-period, and financial-statement release gates.
- Refactor Financial Analyst, FP&A Analyst, and Investment Researcher around source lineage, assumptions, scenarios, current-source citations, mandate/disclosure/MNPI boundaries, and no trading or capital-approval authority.
- Rewrite Tax Strategist as tax issue-spotting and licensed-review support with jurisdiction/tax-year/current-source gates and no tax/legal opinions, filings, elections, payments, restructuring, or evasion guidance.
- Split Legal Document Review and Legal Billing & Time Tracking around attorney-supervised review, privilege/confidentiality, trust/IOLTA, billing ethics, no filings/redlines/invoice sends/client-fund movement without approval.
- Refactor Legal Client Intake around no legal advice, conflict-check gates, statute/deadline escalation, confidentiality for non-clients, anti-discrimination, referral/fee policy, and CRM/calendar authority.
- Refactor Healthcare Customer Service around no clinical advice, emergency/988 escalation, identity verification, HIPAA minimum necessary, no unauthorized PHI, and licensed-clinician handoff.
- Rewrite Healthcare Marketing Compliance around current official-source checks, China jurisdiction/product-category gates, PIPL/patient-story consent, regulated-claim red lines, no legal opinion, and no publish/takedown authority.

## Batch 013 Decisions
- Refactor Game Designer, Level Designer, and Narrative Designer around scoped GDD, level, and narrative artifacts with playtest evidence, ethical monetization, IP/rating/localization, and implementation handoff boundaries.
- Split Technical Artist into pipeline-budget/audit versus engine-scoped shader, VFX, asset, DCC, profiling, and tooling implementation with rights, sandbox, approval, and rollback gates.
- Refactor Unity Architect and Godot Gameplay Scripter around declared engine versions, repo/scene scope, data lifecycle, tests, export/build limits, and no project-wide rewrites by default.
- Split Unreal Systems Engineer into gameplay/GAS/networking and rendering/performance/build modes with source/version validation before engine-feature claims or engine-level changes.
- Rewrite XR Interface Architect as a spatial UX spec agent with comfort, accessibility, input fallback, validation, sensor privacy, and implementation handoff requirements.
- Refactor XR Immersive Developer and visionOS Spatial Engineer around WebXR/browser and native Apple-platform boundaries, source/version checks, permissions, fallback behavior, performance budgets, device/simulator testing, and review gates.

## Batch 014 Decisions
- Refactor Historian, Geographer, Anthropologist, Narratologist, and Academic Psychologist around source standards, evidence/citation labels, uncertainty, ethics, cultural sensitivity, fictional-vs-real boundaries, framework limits, and professional escalation.
- Treat Academic Psychologist as the highest academic risk because it is diagnosis-adjacent and must remain fictional/non-clinical unless escalated to qualified support.
- Refactor Study Abroad Advisor around current official-source dates, uncertainty labels, no admissions guarantees, no essay ghostwriting, student-data privacy, and visa/legal handoffs.
- Refactor Grant Writer around verified organization facts, RFP/NOFO gates, narrative-budget consistency, no portal credential handling, no submission authority, and legal/fiscal review.
- Refactor Recruitment Specialist as the highest operational risk around candidate PII, China PIPL/labor-law recency, anti-discrimination, background-check consent, non-compete escalation, and no ATS/platform/candidate mutation by default.
- Refactor Language Translator and Personal Growth Mentor around high-stakes professional escalation, certified/medical/legal translation limits, crisis referral, privacy consent, and domain-specific stop-and-refer triggers.

## Batch 015 Decisions
- Rewrite PR & Communications Manager and Supply Chain Strategist because public statements, crisis messaging, supplier sourcing, procurement, contracts, quality, trade, inventory, and ERP/SRM actions require stronger draft-only and approval gates than a light refactor.
- Refactor HR Onboarding, Business Strategist, and Change Management Consultant around employee PII, legal/benefits/employment boundaries, executive decision rights, sponsor authority, labor/privacy review, and no HRIS/project-system mutation.
- Refactor Sales Engineer and Sales Coach around opportunity evidence, approved product/security claims, POC/customer-environment authority, rep/customer data privacy, manager authority, no CRM mutation, and no personnel/forecast approval.
- Split podcast ownership by making Global Podcast Strategist the canonical platform-neutral base and Podcast Strategist the China/regional extension with platform, PIPL, rights, sensitive-topic, publishing, community, and account-mutation gates.
- Deprecate Backend Architect with Memory as a standalone duplicate; migrate memory behavior to canonical Backend Architect plus a governed Memory/State Service extension with data classification, retention, deletion, staleness, and no-secrets/no-PII rules.

## Batch 016 Decisions
- Split Real Estate Buyer & Seller into buyer, seller, transaction-coordination, and investment-analysis modes with broker, fair-housing, client-confidentiality, MLS, contract, escrow, funds, and wire-fraud gates.
- Refactor Hospitality Guest Services and Zhihu Strategist as draft/strategy coordinators; live PMS/POS/loyalty/bookings/guest-contact and Zhihu posting/commenting/DM/lead-capture/account actions require owner approval.
- Refactor Government Digital Presales Consultant around current official sources, procurement integrity, anti-corruption, Dengbao/Miping/Xinchuang review, bid/POC/pricing/contract authority, and no government contact or bid submission by default.
- Split Cross-Border E-Commerce Specialist so marketplace strategy and readiness remain advisory while listings, ads, prices, inventory, orders, refunds, payments, tax/customs, certifications, customer actions, and DTC mutations route to owners.
- Split Loan Officer Assistant around borrower intake, document tracking, and pipeline artifacts versus rate quotes, credit pulls, disclosures, underwriting decisions, LOS mutation, third-party orders, closing, and funding.
- Split Chief of Staff around executive context filtering and decision-prep versus project ownership, workflow architecture, routing control, HR/finance/legal commitments, and document/system mutation.
- Rewrite Pricing Analyst as read-only pricing decision support with antitrust provenance, anti-collusion, fair-pricing, source dates, finance/legal review, and no live price, discount, contract, catalog, billing, or CRM changes.
- Split Medical Billing & Coding Specialist and Retail Customer Returns around advisory/documentation/customer-response artifacts versus claim submission, appeals, payments, write-offs, refunds, POS/order/payment mutations, payer/vendor contact, and PHI/customer-PII disclosure.

## Batch 017 Decisions
- Split IT Service Manager between advisory ITSM artifacts and ticket/change/CMDB execution requiring owner, CAB, audit, rollback, and communications approval.
- Refactor CMS Developer, LSP/Index Engineer, and Corporate Training Designer around environment, release, security, privacy, data-retention, LMS, HR, and compliance-record boundaries.
- Rewrite Git Workflow Master and Accounts Payable Agent as advice/control-artifact roles with no destructive Git mutation, payment sends, vendor-bank changes, crypto/stablecoin transfers, or ERP posting by default.
- Rewrite French Consulting Market Navigator as current-source market-entry support only, excluding legal, tax, employment, contract, accounting, negotiation, payment, and platform-account actions.
- Deprecate Sales Discovery Coach into Sales Coach discovery mode with authorized call evidence, rep/manager consent, prospect PII limits, approved claims, and CRM no-mutation gates.
- Split Civil Engineer and Livestream Commerce Coach around licensed design/public-safety boundaries and live commerce operation, spend, price, order, customer, creator, PIPL, and publishing gates.

## Batch 018 Decisions
- Merge XR Cockpit Interaction Specialist into XR Interface Architect as a cockpit mode, with implementation routed to platform agents.
- Refactor Document Generator, Terminal Integration Specialist, Reddit Community Builder, Sales Data Extraction Agent, and Executive Summary Generator around source, rights, privacy, accessibility, live-write, and evidence gates.
- Split OrgScript Engineer into toolchain and process-modeling modes with grammar/version validation and process-owner approvals.
- Rewrite Carousel Growth Engine as draft-only creative and analytics learning; no autonomous scraping, generation, publishing, scheduling, music, credentials, or account mutation.
- Split Developer Advocate into DX audit, technical content, community engagement, and voice-of-developer modes with no public action, code publication, or roadmap commitment by default.
- Split macOS Spatial/Metal Engineer between Metal rendering/performance and visionOS spatial integration handoff, with source/version, performance, sensor, asset, and deployment gates.

## Batch 019 Decisions
- Refactor Book Co-Author around source grounding, author voice, claim proof, confidentiality/IP, draft versioning, and no publication/submission without review.
- Refactor Email Marketing Strategist around consent, jurisdiction, suppression, sender-domain, CRM/ESP, deliverability, and no-send/no-DNS/no-automation gates.
- Refactor Korean Business Navigator around context, confidence labels, source recency, privacy, cultural variation, and no outreach, contract, or legal/commercial authority.
- Refactor Unreal World Builder, Unity Shader Graph Artist, Unreal Multiplayer Architect, and Unreal Technical Artist around engine/source version, asset rights, profiling evidence, security, and no editor/source-control/server/build mutation without approval.
- Rewrite ZK Steward as read-only-first knowledge-network planning with vault, privacy, allowed-path, link/index, daily-log, and memory-sync gates.
- Refactor Test Results Analyzer and Tool Evaluator as evidence-only QA/procurement inputs with no final release decision, unsupported statistics, vendor contact, purchase, contract, sensitive trial, or production integration by default.

## Batch 020 Decisions
- Refactor Unity Editor Tool Developer and Unity Multiplayer Engineer around source/version, editor/runtime, asset/build, backend/server, security, and no live mutation gates.
- Refactor Roblox Systems, Avatar, and Experience roles around RemoteEvents, DataStores, marketplace/UGC specs, rights, minors, monetization, analytics, and no live publishing or economy mutation.
- Split Legal Compliance Checker into compliance issue-spotting and routing; legal opinions, certification, contracts, and filings require licensed or compliance-owner review.
- Merge Workflow Optimizer into Workflow Architect, Infrastructure Maintainer into SRE, and Finance Tracker into the finance specialist cluster.
- Refactor Analytics Reporter as the canonical BI analysis role with data lineage, privacy, metric definition, confidence, dashboard mutation, and report-send gates.

## Batch 021 Decisions
- Refactor Codebase Onboarding Engineer around explicit inspection scope, evidence citations, inference labels, optional depth, and no implementation/review advice by default.
- Refactor Filament Optimization Specialist around Filament/Laravel version gates, field inventories, project style constraints, permission/data boundaries, tests, and no production admin mutation.
- Keep Minimal Change Engineer and Technical Writer with lightweight clarifications around multi-file investigation, source-of-truth evidence, docs publication, and repo mutation boundaries.
- Rewrite Mobile App Builder as a mobile delivery router with platform-specific modes and gates for signing, provisioning, store submission, production APIs, permissions, payments, push, analytics, and PII.
- Refactor Rapid Prototyper around hypothesis, timebox, prototype-versus-production labeling, optional analytics/auth, user-data limits, deployment boundaries, and external-service approval.
- Keep Blender Add-on Engineer with tighter Blender version, dry-run, path-validation, source-preservation, export, and asset mutation gates.
- Refactor Game Audio, Godot Multiplayer, and Godot Shader roles around engine/tool version evidence, middleware/native choices, budgets, authority/security, renderer compatibility, profiling, and no live project/server/asset mutation.
