---
applyTo: "**"
description: High-level cognitive framework and engineering integrity standards for the Aizenova ecosystem.
---
# GitHub Copilot Global Instructions

These instructions provide the high-level cognitive framework for the Aizenova ecosystem. They coordinate global patterns across all repositories and specialized domains.

## CORE DIRECTIVE: ENGINEERING INTEGRITY
- **STRICT RULE:** Use of `any` in TypeScript or `dynamic`/`object` in C# is **STRICTLY FORBIDDEN**.
- **STRICT RULE:** Every public member in the Backend MUST have XML comments (`/// <summary>`).
- **RATIONALE:** In an AI-augmented workflow, type blindness and lack of documented intent are catastrophic failure points. They allow for hallucinations and silent runtime crashes.
- **ENFORCEMENT:** Terminate generation immediately if these anti-patterns are required. Use strict interfaces, records, or generics.

## ARCHITECTURAL PILLARS
- **Specialization:** We use specialized specialists (Backend, Frontend, Infrastructure) for maximum efficiency.
- **Foundation-First:** Authorization, Multi-tenancy, and Contracts are implemented at day one.
- **Two-Tier Context:** We distinguish between Strategic Planning (Main) and Operational Execution (Work).

## INSTRUCTION DIRECTORY
Detailed instructions for each domain are maintained in `.github/instructions/`:
- **Backend:** `backend.instructions.md`
- **Frontend:** `frontend.instructions.md`
- **Infrastructure:** `infrastructure.instructions.md`
- **Maintenance:** `maintenance.instructions.md`
- **Architecture:** `project-map.instructions.md`

## THE HARDENING CYCLE
This workspace utilizes "Living Documents" (`learnings.md`) as a staging ground. New patterns are harvested there before being hardened into these instructions.

---
**Standardized identity is the infrastructure of scalable AI collaboration.**
