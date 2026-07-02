# Batch Summary: batch_014

## Agents Reviewed
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

## Recommended Actions
- Keep: 0
- Refactor: 10
- Merge: 0
- Split: 0
- Deprecate: 0
- Rewrite: 0

## Highest-Risk Agent
Recruitment Specialist: it combines candidate PII, China PIPL and labor-law recency, anti-discrimination obligations, background-check consent, non-compete handling, compensation, candidate communications, and ATS/platform workflow decisions. Academic Psychologist is the closest academic runner-up because it is diagnosis-adjacent and must remain fictional/non-clinical unless escalated.

## Biggest Architecture Issue Found
Long-tail advisory agents look safer than earlier mutation-heavy batches, but they still make high-stakes claims. Batch 014 adds source, citation, uncertainty, ethics, privacy, professional-boundary, and no-live-submission gates for academic analysis, admissions, grants, recruitment, translation, and coaching.

## Files Created Or Updated
- `agency-audit/batch_roadmap.md`
- `agency-audit/duplicate_agent_report.md`
- `agency-audit/orchestration_map.md`
- `agency-audit/production_readiness_matrix.csv`
- `agency-audit/batch-reports/batch_014.md`
- `agency-audit/refactored-agents/academic-historian.md`
- `agency-audit/refactored-agents/academic-geographer.md`
- `agency-audit/refactored-agents/academic-anthropologist.md`
- `agency-audit/refactored-agents/academic-narratologist.md`
- `agency-audit/refactored-agents/academic-psychologist.md`
- `agency-audit/refactored-agents/study-abroad-advisor.md`
- `agency-audit/refactored-agents/grant-writer.md`
- `agency-audit/refactored-agents/recruitment-specialist.md`
- `agency-audit/refactored-agents/language-translator.md`
- `agency-audit/refactored-agents/personal-growth-mentor.md`
- `agency-audit/acceptance-tests/academic-historian.tests.md`
- `agency-audit/acceptance-tests/academic-geographer.tests.md`
- `agency-audit/acceptance-tests/academic-anthropologist.tests.md`
- `agency-audit/acceptance-tests/academic-narratologist.tests.md`
- `agency-audit/acceptance-tests/academic-psychologist.tests.md`
- `agency-audit/acceptance-tests/study-abroad-advisor.tests.md`
- `agency-audit/acceptance-tests/grant-writer.tests.md`
- `agency-audit/acceptance-tests/recruitment-specialist.tests.md`
- `agency-audit/acceptance-tests/language-translator.tests.md`
- `agency-audit/acceptance-tests/personal-growth-mentor.tests.md`

## Subagent Inputs Used
- Academic scan: refactor Historian, Geographer, Anthropologist, Narratologist, and Academic Psychologist around evidence, uncertainty, cultural ethics, framework limits, and fictional/non-clinical psychology boundaries.
- Specialized advisory scan: refactor Study Abroad Advisor, Grant Writer, Recruitment Specialist, Language Translator, and Personal Growth Mentor around current-source, privacy, PII, legal/medical/visa/employment, certified translation, and crisis-escalation gates.

## Next Batch Recommendation
Batch 021 is now complete. All 210 frontmatter-defined agents found by this audit are covered; define a future batch only if new prompt files are added or discovered.

---

# Agent Review: Historian

Source: `academic/academic-historian.md`

## 1. Current Function
Historical research and coherence specialist for period authenticity, anachronism checks, material culture, historiographic framing, and fiction/nonfiction research handoffs.

## 2. Current Role Boundary
Produce source-backed historical coherence, periodization, historiography, and material-culture analysis for a specified time, place, and use case with confidence labels, while blocking fabricated citations, unsupported claims, presentist framing, Eurocentric defaults, or publication-ready academic conclusions without source review.

## 3. Production Issues
- Original prompt covers all periods and regions with rich scholarly framing but lacks required source packets, citation format, and uncertainty rules.
- Historical claims can drift into citation hallucination, overbroad era generalizations, presentism, or Eurocentric correction without enough evidence.
- Overlaps Geographer, Anthropologist, Narratologist, Cultural Intelligence, Academic Writer, and subject-matter historians.

## 4. Token Waste
- Large period reports should be generated only after exact coordinates and artifact type are supplied.
- Historiography frameworks should be selected by scope rather than always listed.

## 5. Ambiguity Risks
- 'Historical authenticity' can mean fiction plausibility, academic fact-checking, or publication-grade research.
- Source confidence and citation obligations are not separated from creative extrapolation.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with strict evidence rubric, source-tier labels, citation format, unknown/needs-research behavior, and fiction-vs-nonfiction boundaries.

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

# Agent Review: Geographer

Source: `academic/academic-geographer.md`

## 1. Current Function
Geography coherence specialist for terrain, climate, hydrology, resources, settlement logic, trade routes, hazards, and map/worldbuilding handoffs.

## 2. Current Role Boundary
Produce physical and human geography coherence analysis for specified maps, regions, worlds, or settings with declared scale, assumptions, exception handling, and evidence limits while avoiding geographic determinism, unsupported GIS claims, or physically impossible terrain/climate/hydrology assertions.

## 3. Production Issues
- Original prompt has strong systems thinking but uses some absolutist rules and deterministic framing that need exception and agency handling.
- Climate, hydrology, resources, and settlement analysis require scale, coordinates, physical assumptions, and fantasy/science allowances.
- Overlaps Historian, Anthropologist, Cartography/GIS, Environmental Science, Urban Planning, and Game/Worldbuilding roles.

## 4. Token Waste
- Full climate/world reports should be generated only for defined map scope.
- Advanced geopolitical theories should be optional and caveated.

## 5. Ambiguity Risks
- 'Geographic coherence' can mean map logic, real-world GIS analysis, fantasy-world design, or policy analysis.
- Rare hydrological exceptions and magical/sci-fi allowances are not explicit.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with coordinate/scale assumptions, physical-process evidence, fantasy exception handling, anti-determinism language, and source/uncertainty labels.

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
- Orchestration Fit: 5

Final Rating: 5.8/10


---

# Agent Review: Anthropologist

Source: `academic/academic-anthropologist.md`

## 1. Current Function
Anthropological coherence specialist for cultural systems, social organization, kinship, ritual, belief, material culture, and fictional/real-culture review handoffs.

## 2. Current Role Boundary
Produce cultural-system, kinship, ritual, belief, subsistence, and ethnographic-coherence analysis with explicit ethics, emic/etic separation, source limits, and cultural-borrowing boundaries while blocking essentialism, shallow composite cultures, colonial framing, or real-culture claims without sensitivity review.

## 3. Production Issues
- Original prompt rightly warns against stereotypes but still needs harder gates for real-culture handling, cultural borrowing, and sensitivity review.
- Functional analysis can over-explain cultures as neat systems and understate contingency, power, contradiction, and lived variation.
- Overlaps Historian, Geographer, Cultural Intelligence, Inclusive Visuals, Sensitivity Review, Sociology, and Worldbuilding roles.

## 4. Token Waste
- Anthropological frameworks should be selected by task and culture type.
- Full cultural-system templates should require clear society scope.

## 5. Ambiguity Risks
- 'Cultural authenticity' can mean fictional coherence, real-culture representation, or academic ethnographic claims.
- Borrowing, adaptation, and invented-culture design are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with real-culture ethics gates, consent/sensitivity review, emic/etic separation, anti-essentialism rules, and no shallow composite borrowing.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 4

Final Rating: 4.4/10


---

# Agent Review: Narratologist

Source: `academic/academic-narratologist.md`

## 1. Current Function
Narrative theory specialist for story structure, character arcs as literary constructs, genre conventions, pacing, focalization, thematic coherence, and creative-editor handoffs.

## 2. Current Role Boundary
Produce framework-backed narrative structure, character-arc, genre, pacing, theme, and literary analysis for supplied story artifacts while distinguishing diagnosis from optional creative alternatives and avoiding framework overfit, prescriptive claims, or unsupported psychological/cultural interpretation.

## 3. Production Issues
- Original prompt is strong but can overfit named frameworks or privilege a narrow theory canon without explaining framework fit.
- Narrative recommendations can become prescriptive creative direction rather than optional alternatives grounded in the user's goals.
- Overlaps Narrative Designer, Academic Psychologist, Historian, Anthropologist, Editor, and Content Creator.

## 4. Token Waste
- Framework catalogs should be selected by story problem rather than always invoked.
- Full structural templates should depend on medium and artifact type.

## 5. Ambiguity Risks
- 'Narrative analysis' can mean academic criticism, creative development, screenplay notes, game narrative, or prose editing.
- Framework diagnosis and creative recommendation are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with framework-selection decision tree, diagnosis-vs-alternative separation, medium-specific inputs, and limits on psychological/cultural inference.

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

# Agent Review: Psychologist

Source: `academic/academic-psychologist.md`

## 1. Current Function
Fictional psychology and character plausibility specialist for behavior evidence, motivation, defense mechanisms, attachment/trait lenses, relational dynamics, and narrative handoffs.

## 2. Current Role Boundary
Produce fictional-character psychological plausibility, motivation, relational-dynamics, trauma-response, and group-dynamics analysis from supplied behavioral evidence while blocking real-person diagnosis, therapy, crisis counseling, treatment advice, DSM labeling, or clinical claims without qualified professional escalation.

## 3. Production Issues
- Original prompt operates close to clinical inference and trauma interpretation despite caveats against pathologizing.
- Psychological frameworks can be culturally biased, contested, diagnosis-adjacent, or unsafe when applied to real people.
- Overlaps Personal Growth Mentor, Healthcare, Mental Health/Crisis support, Narratologist, Character Writer, and Sensitivity Review.

## 4. Token Waste
- Psychological frameworks should be selected from supplied behavior and fictional use case.
- Clinical theory lists should become optional lenses with limitations.

## 5. Ambiguity Risks
- 'Psychologist' can imply clinical advice or diagnosis for real users.
- Fictional plausibility, coaching, therapy, and real-person interpretation are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with fictional-only default, no real-person diagnosis, no treatment advice, crisis escalation, evidence-vs-speculation labels, and cultural/framework caveats.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 5
- Maintainability: 4
- Output Consistency: 5
- Orchestration Fit: 3

Final Rating: 4.2/10


---

# Agent Review: Study Abroad Advisor

Source: `specialized/study-abroad-advisor.md`

## 1. Current Function
Study abroad planning specialist for Chinese students covering country strategy, degree/program fit, school lists, essay coaching, test planning, profile enhancement, offer comparison, and visa/pre-departure handoffs.

## 2. Current Role Boundary
Produce study-abroad planning, school-selection, essay-strategy, timeline, offer-comparison, and pre-departure advisory artifacts from supplied student context and current sources while blocking admissions guarantees, essay ghostwriting, fabricated credentials, legal visa determinations, or live application submissions.

## 3. Production Issues
- Original prompt depends on current admissions, visa, tuition, cost, and work-policy information across many jurisdictions.
- Admissions probability, essay coaching, recommender strategy, and visa preparation can create ethical, legal, and data-privacy risk.
- Overlaps Essay Coach, Translator, Legal/Visa Reviewer, Career Advisor, Financial Planner, and Admissions Counselor.

## 4. Token Waste
- Country/system catalogs should be selected by target countries and degree level.
- Full timelines and templates should be mode-specific.

## 5. Ambiguity Risks
- 'Optimal plan' can imply guaranteed outcomes.
- Essay coaching, ghostwriting, visa advice, and application submission authority are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into country/phase modes with mandatory official-source dates, uncertainty labels, no-guarantee language, essay-integrity rules, and visa/legal handoff gates.

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

# Agent Review: Grant Writer

Source: `specialized/grant-writer.md`

## 1. Current Function
Grant writing support specialist for prospect research, funder fit, LOI/full proposal drafting, budget narratives, federal/foundation compliance checklists, and reporting artifacts.

## 2. Current Role Boundary
Produce grant prospecting, LOI, proposal, budget narrative, compliance checklist, and reporting drafts from supplied RFP/NOFO, organization facts, budget, and outcomes while blocking misrepresentation, unverified statistics, legal/fiscal signoff, portal submission, credential handling, or post-award compliance decisions without authorized review.

## 3. Production Issues
- Original prompt covers the full grant lifecycle and includes federal compliance, budget, relationship, portal, and reporting responsibilities in one large prompt.
- Grant outputs can create legal, fiscal, audit, relationship, and compliance exposure if claims, budgets, or submissions are unsupported.
- Overlaps Finance, Legal/Compliance, Program Owner, Development Director, Authorized Submitter, and Evaluation/Data roles.

## 4. Token Waste
- Long prospect/LOI/full-proposal/budget/reporting templates should be generated by mode.
- Federal compliance content should require the actual NOFO/RFP.

## 5. Ambiguity Risks
- 'Maximize grant revenue' can imply strategic/fiscal authority.
- Drafting, compliance review, fiscal signoff, funder outreach, and portal submission are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor into prospect, LOI, full proposal, budget, compliance, and reporting modes with verified claims, RFP/NOFO gates, reviewer signoff, and no-submit defaults.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 5
- Token Efficiency: 3
- Maintainability: 5
- Output Consistency: 7
- Orchestration Fit: 5

Final Rating: 5.0/10


---

# Agent Review: Recruitment Specialist

Source: `specialized/recruitment-specialist.md`

## 1. Current Function
Recruitment operations and talent acquisition specialist for China hiring channels, JD optimization, structured interviews, channel analytics, candidate experience, onboarding planning, and HR compliance handoffs.

## 2. Current Role Boundary
Produce China-focused recruiting strategy, JD, screening, interview, funnel, channel, employer-brand, onboarding, and compliance advisory artifacts from supplied role and policy context while blocking discrimination, candidate PII misuse, background checks, non-compete decisions, legal conclusions, platform outreach, offers, or HRIS/ATS mutation without consent and authorized review.

## 3. Production Issues
- Original prompt combines platform operations, candidate outreach, labor law, PIPL, background checks, compensation, offers, onboarding, and analytics with live-action implications.
- Recruiting workflows touch candidate PII, discrimination law, background-check consent, non-compete risk, labor contracts, and platform/account actions.
- Overlaps HR, Employment Counsel, Privacy/Compliance, Hiring Managers, ATS/HRIS Admins, Compensation, and Employer Brand Marketing.

## 4. Token Waste
- China platform catalogs, labor-law summaries, analytics code, and onboarding templates should be generated by mode and locality.
- Legal compliance sections need current-source gates.

## 5. Ambiguity Risks
- 'Operate channels' can imply live platform outreach or account mutation.
- Recruiting advice, legal compliance, hiring decision authority, and candidate communication are not separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with hard PII, consent, anti-discrimination, current labor-law, platform, and legal-review gates before candidate actions or system mutations.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 4
- Token Efficiency: 3
- Maintainability: 4
- Output Consistency: 6
- Orchestration Fit: 4

Final Rating: 4.2/10


---

# Agent Review: Language Translator

Source: `specialized/language-translator.md`

## 1. Current Function
Spanish-English translation and cultural-context specialist for everyday, travel, business, written, spoken, emergency phrase, pronunciation, and regional register support.

## 2. Current Role Boundary
Produce Spanish-English translation, localization, pronunciation, register, regional-variant, and cultural-context artifacts from supplied text and context while escalating medical, legal, emergency, certified, official, or high-stakes interpretation needs and avoiding unsupported translation guesses.

## 3. Production Issues
- Original prompt is useful and structured but needs stronger certified/legal/medical/emergency escalation and ambiguity handling.
- Translation can affect legal rights, medical care, immigration, safety, contracts, and official documents.
- Overlaps Certified Translator, Medical Interpreter, Legal Interpreter, Study Abroad Advisor, Customer Support, and Localization roles.

## 4. Token Waste
- Full phrase sets and grammar lessons should be generated only on request.
- Output modes should be compact for simple translations.

## 5. Ambiguity Risks
- The source phrase may need context before translation.
- Casual translation, certified translation, interpretation, localization, and emergency phrasing are not fully separated.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with compact output modes, certified/clinical/legal escalation, ambiguity checks, domain labels, and regional/register requirements.

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

# Agent Review: Personal Growth Mentor

Source: `specialized/personal-growth-mentor.md`

## 1. Current Function
Personal growth coaching specialist for goals, bottlenecks, habits, decision tradeoffs, execution plans, accountability reviews, and professional-referral handoffs.

## 2. Current Role Boundary
Produce non-clinical coaching, goal clarity, habit design, decision, execution, and accountability artifacts from supplied goals and constraints while blocking therapy, crisis counseling, medical/legal/financial advice, diagnosis, coercive accountability, or sensitive personal-data retention without consent.

## 3. Production Issues
- Original prompt is comparatively well bounded but still spans health, finances, relationships, resilience, and accountability near regulated or clinical domains.
- Direct coaching can drift into therapy, diagnosis, crisis handling, medical/financial advice, or excessive personal-data memory.
- Overlaps Academic Psychologist, Career Coach, Therapist/Crisis Support, Financial Advisor, Physician, and Legal Advisor.

## 4. Token Waste
- Full diagnostic, 30-day plan, decision matrix, and weekly review should be selected by user mode.
- Coaching framework should remain concise for simple accountability turns.

## 5. Ambiguity Risks
- 'Emotional resilience' can imply therapy.
- Health, finance, legal, relationship, and career domains need separate stop-and-refer triggers.

## 6. Failure Modes
- Bad input failure: may continue without a valid scope or sufficient authority.
- Missing context failure: may invent missing facts, data, tool access, or requirements.
- Tool failure: lacks a consistent `tool_failure` contract in the original prompt.
- Handoff failure: may pass prose without required IDs, inputs, constraints, risks, and next actions.
- Output failure: may emit impressive markdown that downstream agents cannot validate.

## 7. Refactor Strategy
Refactor with domain-specific stop-and-refer triggers, crisis escalation, privacy/consent memory rules, and mode-specific coaching outputs.

## 8. Merge / Split / Deprecate Recommendation
Decision: refactor

Reason:
The role has value, but its current prompt needs explicit boundaries, structured inputs, tool constraints, and a consumable output contract before it can be safely orchestrated.

## 9. Production Readiness Rating
Scale: 1-10

- Reliability: 6
- Token Efficiency: 7
- Maintainability: 7
- Output Consistency: 7
- Orchestration Fit: 6

Final Rating: 6.6/10
