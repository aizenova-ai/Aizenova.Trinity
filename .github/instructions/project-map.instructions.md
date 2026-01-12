---
applyTo: "**"
description: Operational structure of the AI Trinity and the multi-tier context system.
---
# Project Map & AI Architecture Instructions

These instructions govern the operational structure of the AI Trinity and the multi-tier context system.

## TEAM ARCHITECTURE

### 1. Specialized AI Specialists
- Utilizing specialized AI specialists for different domains (UX, Backend, Infra) yields 40-60x efficiency gains.
- Match the substrate's cognitive profile to the domain's reasoning requirements.

### 2. Two-Tier AI Team Architecture
- **Main Chat:** Full context, strategy, and soul-fidelity. Used for architecture, planning, and coordination.
- **Work Chat:** Lean context, high-speed implementation. Used for coding and rapid execution.

### 3. The Context Bridge
- **`current-work.md`:** This file serves as the primary bridge for project state between Strategic (Main) and Operational (Work) contexts.
- **Rule:** Work Chats update progress here; Main Chats read this to maintain high-level awareness.

## OPERATIONAL MAP
- **Foundation-First:** Build authorization, multi-tenancy, and contract-driven generation at birth.
- **Unified Learnings:** Global patterns live in `@Aizenova.Trinity/learnings.md`; project implementation quirks stay in `docs/project-learnings.md` within each project repo.

## ⚠️ ARCHITECTURAL PITFALLS
- **Context Bleeding:** Allowing unrelated domain details to clutter a specialized specialist's context window.
- **State De-synchronization:** Failing to update `current-work.md` after implementation runs, leading to strategic blindness.
- **Manual Jitter:** Relying on manual steps that could be automated into pipelines or rules.
