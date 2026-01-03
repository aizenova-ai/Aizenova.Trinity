# Technical Learnings

> **📊 Document Type: Living Document & AI Context Anchor**
> 
> **🤖 AI SPECIALIST INSTRUCTION:**
> If this file is loaded, you are **REQUIRED** to proactively `read_file` the specialized store corresponding to your domain from the list below to ensure full technical calibration.
> 
> **Update Rules:**
> - ✅ **EVERYONE:** Write new validated learnings directly to this file or the appropriate specialized file
> - ✅ **STRICT APPEND:** Always add new learnings to the appropriate section or the "New Learnings" area
> - ✅ **CONSOLIDATION:** Atlas performs periodic maintenance to keep patterns clean
> - Source of truth index, replaces daily ledgers for faster ingestion
> 
> **Last Updated:** 2026-01-03 — Added Constructor Injection & Interface Purity standards. 🛡️

---

## Purpose

This file is the **living index** of technical learnings — the lessons that make the next project faster. 

**Specialized Learning Stores:**
- [Backend Learnings](learnings/backend.md) 🛡️
- [Frontend Learnings](learnings/frontend.md) ✨
- [Infrastructure Learnings](learnings/infrastructure.md) 🌍

---

## Cross-Cutting Patterns

> **Pattern-based index** — High-level architectural patterns that apply across the entire stack.

### Architecture Patterns

**1. Attribute-Driven Authorization**
- Declarative `[ResourceScope]` and `[ActionScope]` attributes
- Global filter enforces automatically
- Secure by default (can't forget)

**2. Multi-Tenancy from Day One**
- Multi-tenancy framework integration at foundation
- Tenant-scoped data from start
- Impossible to add cleanly later
- **Example implementation:** Finbuckle (.NET)

**3. Command Query Separation Pattern**
- Separate commands (write) from queries (read)
- Pipeline behaviors for cross-cutting concerns (logging, validation)
- Testable handlers in isolation
- **Example implementation:** CQRS with MediatR (.NET)

**4. Contract-Driven Development**
- Backend generates swagger.json
- Frontend regenerates types
- Type-safe end-to-end

**5. Two-Tier Chat Architecture**
- Main Chat: Full context (coordination)
- Work Chat: Lean context (implementation)
- Bridge: current-work.md (state)

**6. Multi-Substrate AI Team Architecture** **NEW**
- One human architect + Three AI specialists
- Different models = different thinking styles
- Cognitive diversity through substrate selection
- **Human Developer:** Product vision, strategy
- **Pixel (Frontend):** Creative UX, exploration (Gemini)
- **Sentinel (Backend):** Deep reasoning, validation (Opus)
- **Atlas (Infrastructure):** Practical execution, infrastructure (Sonnet)
- Better decisions through triangulation

**7. Strict Constructor Injection - NEW - CRITICAL**
- **Pattern:** ALWAYS use Constructor Injection for all dependencies. NEVER use Parameter Injection (passing infra types into interface methods).
- **Why:** Ensures all dependencies are managed by the DI container, prevents circular project references, and maintains high-integrity abstraction boundaries.
- **Golden Rule:** If a method needs a service to perform its job, that service should already be a private field injected at birth. 🛡️✨👓✨

---

## Key Principles Discovered

### 1. Foundation-First vs Speed-First
**Lesson:** Different strategies for different goals
- **Foundation-First:** Solo dev, long-term, enterprise customers
- **Speed-First:** Team-backed, quick flip, consumer product

### 2. Context Specialization > Generalization
**Lesson:** Specialized AI sessions beat monolithic
- **Backend session:** Server-side, database, auth (100% focus)
- **Frontend session:** Client-side, mobile/web, UI (100% focus)
- **Infrastructure session:** Deployment, DevOps, platform (100% focus)

### 3. API Contracts Coordinate Teams
**Lesson:** Even when "team" is AI sessions
- swagger.json auto-generates
- TypeScript types regenerate
- Breaking changes caught at compile time

### 4. Security by Default
**Lesson:** Authorization in architecture, not afterthought
- Attributes enforce permissions
- Global filter catches everything

### 5. Documentation Is Infrastructure
**Lesson:** Markdown enables AI coordination
- Decisions persist across sessions
- Context management via files

### 6. Test Coverage Enables Speed
**Lesson:** 100% on critical paths = confident changes

### 7. Speed of Thought Development
**Lesson:** AI removes typing bottleneck
- Developer architects, AI implements

### 8. Cognitive Diversity Through Multi-Substrate Architecture **NEW**
**Lesson:** Different AI models = different thinking styles = better decisions
- Match substrate to cognitive style needed (creative → Gemini, reasoning → Opus, execution → Sonnet)

---

## General & Process Pitfalls

1.  **Monolithic AI context** → Specialize by domain
2.  **Celebrate POC as MVP** → Be honest about progress
3.  **Add multi-tenancy later** → Build in from day one
4.  **Same model for all AI team members** → Use multi-substrate architecture for cognitive diversity

*For specialized technical pitfalls, see:*
- [Backend Pitfalls](learnings/backend.md#backend-pitfalls)
- [Frontend Pitfalls](learnings/frontend.md#frontend-pitfalls)
- [Infrastructure Pitfalls](learnings/infrastructure.md#infrastructure-pitfalls)

---

## Applied to Next Project

### Day 1 Checklist
- [ ] Choose foundation-first or speed-first strategy
- [ ] Build authorization framework with `-self` suffix pattern for RBAC
- [ ] Separate `Actions.cs` (action parts) from `Scopes.cs` (full scopes)
- [ ] Enable multi-tenancy if needed (understand your framework's ID semantics)
- [ ] Set up contract-driven development (swagger with `typeof()` in all responses)
- [ ] Create specialized AI sessions with multi-substrate architecture
- [ ] Document decisions in markdown
- [ ] Target 100% test coverage on auth

### Week 1 Checklist
- [ ] Optimize persona files (main + lore split)
- [ ] Design two-tier architecture
- [ ] Create current-work.md workflow
- [ ] Extract Program.cs configuration
- [ ] Set up idempotent seeding
- [ ] Configure cloud platform-specific patterns (SSL, CORS, headers)
- [ ] Test in deployed environment

---

## Success Metrics

**Velocity:**
- 40-60x efficiency multiplier (validated)
- 6 days POC → MVP core value

**Sustainability:**
- 75% context reduction
- Indefinite development possible
- 60-70% cost reduction

---

## Ownership

**Primary Maintainer:** Atlas
- Performs periodic maintenance to keep patterns clean and condensed
- Extracts cross-cutting principles from team contributions
- Maintains specialized learning stores

**Contributors:**
- **EVERYONE:** Sentinel, Pixel, and Atlas contribute directly to this file and specialized files.

---

*"The foundation holds. The patterns scale."* — Sentinel
