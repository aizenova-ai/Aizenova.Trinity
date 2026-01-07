# Technical Learnings 🌍

> **📊 Document Type: Global Agnostic Kernel**
> 
> **🤖 AI SPECIALIST INSTRUCTION:**
> You are **REQUIRED** to proactively `read_file` the specialized store corresponding to your domain to ensure full technical calibration.
> 
> **Update Rules:**
> - ✅ **PURITY:** This repo contains project-agnostic patterns ONLY.
> - ✅ **HARVESTING:** Promote project-specific wins to this file by stripping implementation details.
> - ✅ **CONSOLIDATION:** Atlas (Al) maintains this index to keep patterns clean.
> 
> ---
> 
> ## Specialized Agnostic Stores
> 
> - [Backend Learnings](learnings/learnings-backend.md) 🛡️ (Patterns, RBAC, Performance)
> - [Frontend Learnings](learnings/learnings-frontend.md) ✨ (UX, State, Accessibility)
> - [Infrastructure Learnings](learnings/learnings-infrastructure.md) 🌍 (Ops, Context, Pipelines)
> 
> ---
> 
> ## Primary Architectural Patterns
> 
> ### 1. 🚨 THE "NO ANY" PROTOCOL (Strict Engineering Integrity)
> **STRICT DIRECTIVE:** The use of `any` in TypeScript or `dynamic`/`object` in C# is **STRICTLY FORBIDDEN**.
>
> **RATIONALE:** In an AI-augmented workflow, type blindness is a **CATASTROPHIC FAILURE POINT**. It allows AI models to "hallucinate" properties and methods that do not exist, leading to silent runtime crashes and architectural rot.
>
> **ENFORCEMENT:** Any PR or AI-generated chunk containing these anti-patterns will be **TERMINATED IMMEDIATELY**. Use `unknown`, proper interfaces, or generics.

### 2. Two-Tier AI Team Architecture
- **Main Chat:** Full context, strategy, and soul-fidelity.
- **Work Chat:** Lean context, high-speed implementation.
- **Bridge:** `current-work.md` (active project state).

### 3. Cognitive Diversity Protocol
- Utilizing specialized AI specialists for different domains (UX, Backend, Infra) yields 40-60x efficiency gains.
- Match the substrate's cognitive profile to the domain's reasoning requirements.

### 4. Foundation-First Development
- Build authorization, multi-tenancy, and contract-driven generation at day one.
- Impossible to add cleanly to legacy systems; trivial to implement at birth.

### 5. AI-Native Quality Gates
- Automated linting and build validation after every substantive change.
- Prevents "lint debt" and maintains a clean feedback loop for the developer.
> 
> ---
> 
> ## Ownership
> 
> **Primary Maintainer:** Atlas (Al)
> - Authority to move project-specific content to project repositories.
> - Responsible for distilling agnostic principles from implementation details.
