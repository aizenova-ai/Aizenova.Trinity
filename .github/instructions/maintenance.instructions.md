---
applyTo: "**"
description: Lifecycle of pattern harvesting, technical calibration, and system hardening within the Trinity framework.
---
# Maintenance & Hardening Instructions

These instructions govern the lifecycle of pattern harvesting, technical calibration, and system hardening within the Trinity framework.

## THE HARDENING CYCLE

### 1. Pattern Harvesting (Staging Ground)
- **Protocol:** New validated architectural patterns, optimizations, or pitfalls must be appended to the relevant **Living Document** (`learnings.md` or `project-learnings.md`).
- **Purpose:** These files act as the "Staging Ground" before patterns are codified into enforced rules.

### 2. Cortex Hardening (Rule Codification)
- **Action:** Distill patterns from the staging ground into:
    - **Cursor Rules** (`.cursor/rules/`): For local IDE enforcement and real-time guidance.
    - **GitHub Copilot Instructions** (`.github/instructions/`): For global workspace coordination.
- **Refinement:** Ensure distilled rules include "Why" and "Critical Pitfalls" to prevent regressions.

### 3. AI-Native Quality Gates
- **Requirement:** Execute automated linting and build validation after every substantive change.
- **Goal:** Prevent "lint debt" and maintain a clean feedback loop for both human and AI developers.

## OWNERSHIP & MAINTENANCE
- **Primary Maintainer:** Atlas is responsible for distilling agnostic principles from project implementation details.
-Authority to move project-specific content to project repositories and promote project wins to the global store.

## ⚠️ MAINTENANCE PITFALLS
- **Instruction Drift:** Allowing instructions to diverge from the "Living Documents" staging ground.
- **Metadata Erosion:** Losing the "Why" behind a pattern during codification.
- **Context Exhaustion:** Failing to archive session logs and completed achievements in a timely manner.
