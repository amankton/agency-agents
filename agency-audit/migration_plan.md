# Migration Plan

## Phase 1: Govern The Control Plane
Replace batch 001 prompts in a staging registry first. Do not overwrite original files until the refactored agents pass acceptance tests.

## Phase 2: Normalize Contracts
Apply the same required-input, output-schema, tool-failure, authorization-gate, and handoff-payload structure to each remaining high-priority batch.

## Phase 3: Merge Duplicates
Merge duplicate variants into canonical agents as optional modules. Deprecate duplicate prompt files after consumers have migrated.

## Phase 4: Validate Workflows
Run acceptance tests for each refactored agent and add one orchestrated smoke test: Router -> Planner -> Executor -> Evidence Collector -> Reality Checker -> Final Response.

## Phase 5: Registry Adoption
Create a central agent registry from `agent_manifest.json` and use it as the only source for routing, triggers, tools, safety gates, and handoff targets.
