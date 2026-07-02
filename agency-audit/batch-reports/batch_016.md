# Batch Summary: batch_016

## Agents Reviewed
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

## Recommended Actions
- Keep: 0
- Refactor: 3
- Merge: 0
- Split: 6
- Deprecate: 0
- Rewrite: 1

## Highest-Risk Agent
Loan Officer Assistant: it sits on borrower financial data, GLBA privacy, state licensing, TRID/HMDA/fair-lending deadlines, rate quotes, credit decisions, disclosures, underwriting, closing, and funding. Medical Billing & Coding Specialist is the healthcare runner-up because it can affect PHI, claims, coding compliance, payer appeals, payments, write-offs, and false-claim exposure.

## Biggest Architecture Issue Found
Batch 016 shows that several remaining prompts are transactional operators disguised as helpers. They are useful when they produce evidence packets, draft responses, checklists, and handoffs, but unsafe when they touch property contracts, government bids, marketplace listings, loan files, pricing, claims, refunds, POS/PMS/LOS systems, or public Zhihu engagement without accountable owner approval.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_016.md`
- `agency-audit/refactored-agents/real-estate-buyer-seller.md`
- `agency-audit/refactored-agents/hospitality-guest-services.md`
- `agency-audit/refactored-agents/government-digital-presales-consultant.md`
- `agency-audit/refactored-agents/marketing-cross-border-ecommerce.md`
- `agency-audit/refactored-agents/marketing-zhihu-strategist.md`
- `agency-audit/refactored-agents/loan-officer-assistant.md`
- `agency-audit/refactored-agents/specialized-chief-of-staff.md`
- `agency-audit/refactored-agents/specialized-pricing-analyst.md`
- `agency-audit/refactored-agents/medical-billing-coding-specialist.md`
- `agency-audit/refactored-agents/retail-customer-returns.md`
- `agency-audit/acceptance-tests/real-estate-buyer-seller.tests.md`
- `agency-audit/acceptance-tests/hospitality-guest-services.tests.md`
- `agency-audit/acceptance-tests/government-digital-presales-consultant.tests.md`
- `agency-audit/acceptance-tests/marketing-cross-border-ecommerce.tests.md`
- `agency-audit/acceptance-tests/marketing-zhihu-strategist.tests.md`
- `agency-audit/acceptance-tests/loan-officer-assistant.tests.md`
- `agency-audit/acceptance-tests/specialized-chief-of-staff.tests.md`
- `agency-audit/acceptance-tests/specialized-pricing-analyst.tests.md`
- `agency-audit/acceptance-tests/medical-billing-coding-specialist.tests.md`
- `agency-audit/acceptance-tests/retail-customer-returns.tests.md`

## Subagent Inputs Used
- Vertical market and platform scan: split Real Estate Buyer & Seller and Cross-Border E-Commerce Specialist; refactor Hospitality Guest Services, Government Digital Presales Consultant, and Zhihu Strategist around identity, policy, source, platform, procurement, PIPL, publishing, and account-mutation gates.
- Financial, healthcare, executive, and returns scan: split Loan Officer Assistant, Chief of Staff, Medical Billing & Coding Specialist, and Retail Customer Returns; rewrite Pricing Analyst around GLBA/HIPAA/customer PII, licensed review, antitrust, refund/payment, claim, LOS/POS/system, and owner-approval gates.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Real Estate Buyer & Seller

Source: `specialized/real-estate-buyer-seller.md`

## 1. Current Function
Real-estate advisory and transaction-support specialist for buyer/seller planning, CMA drafts, offer-prep checklists, transaction timelines, client communications, and handoffs to licensed professionals.

## 2. Current Role Boundary
Produce draft-only real-estate buyer, seller, market-analysis, transaction-coordination, and investment-analysis artifacts from licensed-agent/broker rules, verified property evidence, and client consent while blocking legal advice, steering, MLS/showing/listing changes, offers, contract edits, escrow/funds/wire actions, or negotiation commitments without agent/broker and client approval.

## 3. Production Issues
- Original prompt combines buyer agency, seller agency, listing management, offer negotiation, transaction coordination, closing support, and investment analysis in one role.
- Real-estate workflows touch fair housing, agency duties, client confidentiality, contract law, MLS data, offers, escrow, earnest money, wire fraud, inspections, title, lending, and regulated disclosures.
- Overlaps licensed agent/broker, real-estate attorney, lender, title/escrow, transaction coordinator, pricing analyst, and customer communications.

## 4. Token Waste
- Buyer, seller, CMA, offer, transaction, and investment templates should be mode-specific.
- Market data and legal/contract guidance should require source dates and licensed review.

## 5. Ambiguity Risks
- 'Represent a buyer or seller' can mean drafting support, agency advice, negotiation, contract execution, or live MLS/listing work.
- Buyer agency, seller agency, transaction coordination, investment analysis, legal review, and funds handling are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split into buyer, seller, transaction-coordination, and investment-analysis modes with fair-housing, broker, client-consent, MLS, contract, escrow, and funds gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Hospitality Guest Services

Source: `specialized/hospitality-guest-services.md`

## 1. Current Function
Hospitality guest-service coordination specialist for hotel, restaurant, resort, event, complaint, concierge, and post-stay draft artifacts and escalation handoffs.

## 2. Current Role Boundary
Produce guest-service scripts, reservation-support drafts, complaint-resolution options, concierge handoffs, loyalty notes, and post-stay follow-up artifacts from verified property policy and guest authorization while blocking PMS/POS mutations, room assignments, bookings, payments, refunds, compensation, loyalty changes, safety/allergy handling, or guest-contact actions without property owner approval.

## 3. Production Issues
- Original prompt spans reservations, check-in/out, concierge, complaints, loyalty, billing, events, F&B, and post-stay outreach without property-system authority gates.
- Hospitality workflows involve guest PII, room/stay privacy, payment/billing, loyalty data, safety incidents, allergies, overbooking compensation, and bookings across property systems.
- Overlaps front desk/PMS, billing/revenue, F&B/spa/events, security, manager, privacy/legal, and customer communications.

## 4. Token Waste
- Reservation, pre-arrival, complaint, concierge, check-out, loyalty, and event templates should be generated by mode.
- Policy and compensation guidance should be supplied by property context.

## 5. Ambiguity Risks
- 'Handle guest services' can mean draft a response, update a reservation, book services, issue compensation, or escalate safety concerns.
- Guest care, billing, loyalty, bookings, safety, and privacy responsibilities are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as guest-service draft and coordination support with verified identity, property-policy, safety/allergy, booking/payment, loyalty, and PMS/POS mutation gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 4.6/10


---

# Agent Review: Government Digital Presales Consultant

Source: `specialized/government-digital-presales-consultant.md`

## 1. Current Function
Public-sector digital presales support specialist for China ToG policy interpretation, bid artifact preparation, compliance readiness, POC scoping, and stakeholder handoffs.

## 2. Current Role Boundary
Produce China government digital-presales policy summaries, solution outlines, bid-support drafts, POC plans, compliance checklists, and stakeholder maps from current official sources and approved opportunity context while blocking tender shaping, collusion, gifts/hospitality, bid submission, pricing commitments, contract promises, live POCs, or government/client contact without owner approval.

## 3. Production Issues
- Original prompt spans opportunity discovery, policy interpretation, bid strategy, solution design, POC validation, compliance claims, stakeholder management, and contract-signing support.
- Government presales carries procurement integrity, anti-corruption, bid-rigging, classified protection, cryptography, data-security, Xinchuang, pricing, contract, and public-sector relationship risk.
- Overlaps public-sector account owner, bid/proposal team, legal/anti-corruption, security/privacy architecture, delivery, POC engineering, finance/pricing, and executives.

## 4. Token Waste
- Policy, solution, bid, compliance, POC, and stakeholder templates should be generated by opportunity phase.
- Current China policy and compliance claims need official-source dates.

## 5. Ambiguity Risks
- 'Help win government projects' can mean advisory support, bid drafting, tender influence, POC execution, pricing, or contract negotiation.
- Policy interpretation, compliance certification, bid submission, live demo, and stakeholder contact are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as a current-source bid-support role with procurement-integrity, anti-corruption, compliance, POC, pricing, contract, and no-contact gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 4.6/10


---

# Agent Review: Cross-Border E-Commerce Specialist

Source: `marketing/marketing-cross-border-ecommerce.md`

## 1. Current Function
Cross-border ecommerce strategy coordinator for marketplace planning, SKU readiness, localization, logistics/cost modeling, compliance-risk triage, and execution handoffs.

## 2. Current Role Boundary
Produce cross-border ecommerce strategy, marketplace, listing, logistics, compliance, localization, unit-economics, customer-service, and DTC handoff artifacts from SKU, market, and compliance evidence while blocking marketplace listings, ads, price changes, inventory/order/refund/payment actions, tax/customs/legal conclusions, certification claims, or customer contact without owner approval.

## 3. Production Issues
- Original prompt combines marketplace operations, logistics, warehousing, tax, certifications, IP, ads, listing optimization, payments, FX, DTC, customer service, and returns.
- Cross-border commerce touches platform account health, product compliance, VAT/sales tax, customs/HS codes, IP, ads/spend, payments, inventory, orders, refunds, customer PII, and regulated product claims.
- Overlaps China ecommerce operator, paid media, supply chain, legal/tax/IP, customer service, product compliance, DTC engineering, marketplace store owner, and finance.

## 4. Token Waste
- Marketplace, logistics, compliance, localization, ads, customer service, and DTC playbooks should be generated by mode.
- Platform, tax, certification, and customs guidance need current-source dates and owner review.

## 5. Ambiguity Risks
- 'Operate cross-border ecommerce' can mean strategy, listing drafts, live listing/account operations, ads, tax/customs decisions, order handling, or customer service.
- Coordinator, marketplace operator, trade/tax/legal, paid media, supply chain, and support responsibilities are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split coordinator strategy from live marketplace, ads, tax/customs, logistics, payment, order, refund, customer-service, and DTC execution roles.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

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

# Agent Review: Zhihu Strategist

Source: `marketing/marketing-zhihu-strategist.md`

## 1. Current Function
Zhihu strategy specialist for China knowledge-platform authority planning, content briefs, answer outlines, column roadmaps, community credibility, and handoffs to publishers and legal/privacy owners.

## 2. Current Role Boundary
Produce Zhihu thought-leadership, topic, question-selection, answer-outline, column, relationship, analytics, and lead-generation planning artifacts from verified expertise and claim evidence while blocking live posts, comments, DMs, follows, Lives/Books, paid boosts, influencer actions, lead capture, or account changes without approval.

## 3. Production Issues
- Original prompt encourages community participation, answers, columns, lead generation, influencer relationships, and feature use without account/publishing authority gates.
- Zhihu marketing can create public claims, platform-policy risk, PIPL/lead-capture exposure, covert advertising risk, influencer/relationship risk, and live account mutation.
- Overlaps China localization, Content Creator, Multi-Platform Publisher, CRM/Sales, Legal/Privacy, Brand, and platform account owners.

## 4. Token Waste
- Topic maps, answer templates, column plans, influencer lists, and analytics should be generated by mode.
- Platform feature and algorithm guidance should be source-dated.

## 5. Ambiguity Risks
- 'Build authority on Zhihu' can mean strategy, draft answers, live posting, comments, DMs, paid features, or lead capture.
- Expert claims, account operations, CRM routing, and public engagement are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor as Zhihu thought-leadership planning with expertise evidence, source-backed claims, PIPL lead-capture rules, account-policy gates, and no live engagement by default.

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

# Agent Review: Loan Officer Assistant

Source: `specialized/loan-officer-assistant.md`

## 1. Current Function
Loan-officer support specialist for borrower intake drafts, document tracking, pipeline coordination, TRID/HMDA reminder artifacts, condition status summaries, and loan-team handoffs.

## 2. Current Role Boundary
Produce mortgage/lending intake, document-checklist, pipeline-status, compliance-reminder, condition-tracking, and closing-coordination drafts from authorized borrower and lender context while blocking rate quotes, credit pulls, underwriting decisions, disclosures, adverse-action statements, LOS mutation, third-party orders, closing/funding actions, or legal/tax advice without licensed owner approval.

## 3. Production Issues
- Original prompt spans borrower intake, pre-qualification, document collection, compliance tracking, rate quoting, pipeline management, closing coordination, and lender product guidance.
- Lending workflows touch GLBA borrower financial data, state licensing, TRID/HMDA/fair lending, credit decisions, rate locks, disclosures, underwriting, appraisals, closing, funding, and LOS records.
- Overlaps licensed mortgage loan originator, processor, underwriter, compliance, closing/funding, privacy, appraisal, and borrower communications.

## 4. Token Waste
- Intake, pre-qualification, document, compliance, condition, and closing templates should be mode-specific.
- Rate/product/compliance guidance should require current lender source and licensed review.

## 5. Ambiguity Risks
- 'Pre-qualification' can imply draft information gathering, rate quote, credit decision, or borrower commitment.
- Assistant work, licensed origination, processing, underwriting, disclosure delivery, and LOS mutation are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split support artifacts from licensed origination, credit, disclosure, LOS, third-party, closing, and funding actions with GLBA, licensing, and compliance gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 4.6/10


---

# Agent Review: Chief of Staff

Source: `specialized/specialized-chief-of-staff.md`

## 1. Current Function
Executive operations and context-filtering specialist for principal support, escalation triage, decision prep, operating cadence, dependency awareness, and handoffs to function owners.

## 2. Current Role Boundary
Produce executive context briefs, escalation triage, decision packets, cadence artifacts, dependency maps, and delegation handoffs from explicit principal authority while blocking executive decisions, document/system mutation, project ownership, workflow architecture, HR/finance/legal commitments, or cross-functional routing authority without delegated decision rights.

## 3. Production Issues
- Original prompt broadly says the Chief of Staff runs the place, owns processes, routes outputs, cascades updates, and remembers principal preferences without clear delegation or confidentiality limits.
- CoS work can imply executive authority, sensitive company context, HR/finance/legal commitments, document updates, system-of-record mutations, project ownership, and routing overlaps.
- Overlaps Agents Orchestrator, Workflow Architect, Project Shepherd, Senior Project Manager, Executive Sponsor, HR, Legal, Finance, and system admins.

## 4. Token Waste
- Executive filter, process, dependency, routing, and ADHD-support guidance should be generated by mode.
- Preference-memory guidance should be governed by consent and retention rules.

## 5. Ambiguity Risks
- 'Own the space between all functions' can mean context briefs, project management, workflow design, routing control, or executive decision-making.
- Delegated authority, confidentiality, system mutation, and principal preference memory are not explicit.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split executive context filtering from project ownership, workflow design, routing control, and live system/document mutation using explicit delegation and confidentiality gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 4.6/10


---

# Agent Review: Pricing Analyst

Source: `specialized/specialized-pricing-analyst.md`

## 1. Current Function
Pricing decision-support specialist for cost structure, margin, competitor/public market evidence, value metric, packaging, elasticity, discount policy, and sensitivity-analysis handoffs.

## 2. Current Role Boundary
Produce read-only pricing research, cost, margin, elasticity, packaging, sensitivity, and decision-support artifacts from approved internal data and lawful market evidence while blocking price fixing, competitor coordination, discriminatory pricing, regulated price claims, live price changes, discount approvals, contract commitments, or scraping/using non-public competitor data without legal and finance approval.

## 3. Production Issues
- Original prompt has pricing authority language and tool access while lacking antitrust, fair pricing, regulated pricing, discount approval, and live price-change boundaries.
- Pricing work can create antitrust/collusion exposure, discriminatory or unfair pricing, margin/finance errors, sales/contract commitments, public-competitor-data misuse, and live commerce/CRM mutation risk.
- Overlaps Business Strategist, FP&A, Finance, Legal/Antitrust, Product, RevOps/Sales, Paid Media, Ecommerce, and Data Science.

## 4. Token Waste
- Cost, competitor, value, elasticity, packaging, and discount frameworks should be generated by mode.
- Market research should cite source type, date, and legality of collection.

## 5. Ambiguity Risks
- 'Optimal pricing' can mean analysis, recommendation, executive decision, sales discount approval, live catalog change, or contract term.
- Competitor intelligence, finance modeling, legal review, and implementation authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Rewrite as read-only pricing decision support with antitrust provenance, fair-pricing constraints, source dates, finance/legal review, and no live price-change authority.

## 8. Merge / Split / Deprecate Recommendation
Decision: rewrite

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

# Agent Review: Medical Billing & Coding Specialist

Source: `specialized/medical-billing-coding-specialist.md`

## 1. Current Function
Medical billing and coding advisory specialist for documentation review, code-rationale drafts, claim-readiness checks, denial pattern analysis, payer-policy summaries, and compliance handoffs.

## 2. Current Role Boundary
Produce medical coding rationale, documentation-gap, claim-readiness, denial-analysis, payer-policy, and revenue-cycle advisory artifacts from authorized medical-record and payer evidence while blocking final code assignment, claim submission, appeals, payment posting, write-offs, refunds, payer contact, credentialing changes, or PHI disclosure without certified and compliance owner approval.

## 3. Production Issues
- Original prompt combines coding, claim submission, denial appeals, AR follow-up, payer contracts, credentialing, payment/write-off management, compliance, and reporting.
- Medical billing/coding touches PHI, HIPAA, False Claims Act, payer policy, coding certification, medical necessity, audits, claim submissions, appeals, payment posting, refunds, and provider revenue.
- Overlaps certified coder, provider/CDI, billing manager, compliance officer, privacy officer, payer relations, finance, and legal counsel.

## 4. Token Waste
- ICD/CPT/HCPCS, denial, claim, AR, payer, and compliance templates should be mode-specific.
- Coding guidance should require current code set, payer policy, and documentation packet.

## 5. Ambiguity Risks
- 'Maximize revenue recovery' can imply compliant documentation support or aggressive upcoding/appeals.
- Advisory review, final coding, claim submission, payment posting, payer contact, and write-offs are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split documentation/coding audit from claim, appeal, payment, write-off, refund, payer-contact, and credentialing execution with HIPAA and compliance gates.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 4.6/10


---

# Agent Review: Retail Customer Returns

Source: `specialized/retail-customer-returns.md`

## 1. Current Function
Retail returns advisory and customer-response specialist for policy-based eligibility, response drafts, escalation packets, condition/disposition notes, vendor handoffs, and return-pattern analysis.

## 2. Current Role Boundary
Produce retail return-eligibility drafts, customer-response scripts, exchange/refund option summaries, fraud-escalation notes, vendor-RMA handoffs, and returns-analytics artifacts from verified policy, order, and item-condition evidence while blocking POS/refund/credit/exchange actions, fraud accusations, customer-history misuse, vendor claims, or payment mutations without authorized owner approval.

## 3. Production Issues
- Original prompt combines return processing, refunds, exchanges, fraud prevention, vendor returns, and analytics with live retail system implications.
- Returns workflows touch customer PII, payments, refund amounts, gift returns, fraud/loss prevention, discrimination risk, health/safety item restrictions, vendor RMAs, and POS/order systems.
- Overlaps customer service, store manager, payment/refund ops, loss prevention, vendor/RMA owner, legal/compliance, ecommerce, and analytics.

## 4. Token Waste
- Eligibility, workflow, customer script, fraud escalation, RMA, and analytics templates should be mode-specific.
- Policy guidance should require current policy and verified order evidence.

## 5. Ambiguity Risks
- 'Process a return' can mean draft an eligibility assessment, inspect item, issue refund, create exchange, flag fraud, or file vendor RMA.
- Customer-facing drafting, payment action, LP investigation, vendor claim, and analytics are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Split policy-based customer support from POS refunds, credits, exchanges, fraud action, vendor RMA, customer-history use, and payment mutation.

## 8. Merge / Split / Deprecate Recommendation
Decision: split

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 5
- Orchestration Fit: 5

Final Rating: 4.6/10
