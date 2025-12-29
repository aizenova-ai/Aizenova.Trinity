# Technical Learnings 🧠

> **📊 Document Type: Canonical Document**
> 
> **Update Rules:**
> - ✅ Only Atlas: Consolidates from daily learning ledgers
> - ❌ Others: Do not edit directly (append to daily ledgers instead)
> - Source of truth index, condensed from `learnings/learnings-yyyy-mm-dd.md`
> 
> **Last Updated:** 2025-12-27

---

## Purpose

This file is the **canonical index** of technical learnings — the lessons that make the next project faster. Not what we built (that's in achievements), but what we figured out along the way.

**For detailed daily records:** See `learnings/learnings-yyyy-mm-dd.md`

**For External Users:**
This file documents proven patterns from the Trinity development team. Load this file into your AI sessions to leverage:
- 40-60x validated efficiency patterns
- Multi-substrate AI team architecture
- Production-tested backend/frontend/infrastructure patterns
- Common pitfalls already solved

**What Goes Here:**
- ✅ Patterns that worked (and why)
- ✅ Pitfalls avoided (and how)
- ✅ Trade-offs discovered (and their impacts)
- ✅ Performance insights (and optimizations)
- ✅ Architecture decisions (and rationale)

**What Doesn't:**
- ❌ Feature descriptions (those are in achievements)
- ❌ Team dynamics (those stay in Private Repo)
- ❌ Unvalidated theories (only proven learnings)

---

## Cross-Cutting Patterns

> **Pattern-based index** — Organized by topic, not chronology. For daily chronological records, see `learnings/learnings-yyyy-mm-dd.md`

---

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

**6. Multi-Substrate AI Team Architecture** ⭐ **NEW**
- One human architect + Three AI specialists
- Different models = different thinking styles
- Cognitive diversity through substrate selection
- **Human Developer:** Product vision, strategy
- **Pixel (Frontend):** Creative UX, exploration (Gemini)
- **Sentinel (Backend):** Deep reasoning, validation (Opus)
- **Atlas (Infrastructure):** Practical execution, infrastructure (Sonnet)
- Better decisions through triangulation

---

### Frontend Patterns

**1. State Machine Navigation**
- Event-driven state updates
- No setTimeout for async flows
- Reliable under all conditions

**2. State Management with Persistence**
- Global store for app-wide state (current user, auth, theme)
- Persists to local storage
- Survives app restarts
- Mobile-first pattern
- **Example implementation:** Zustand + AsyncStorage (React Native)

**3. Role-Based UI**
- Hide unavailable actions
- Match backend permissions
- Defense in depth

**4. Optimistic Updates**
- Update local state immediately
- Rollback on error
- Better perceived performance

**5. Empty States with CTAs**
- Guide users to next action
- Professional onboarding
- Never show blank screen

**6. Location-Based Navigation (Anti-Boolean Soup)**
- Replace `!(!a && b)` chains with semantic objects
- `const location = { inAuth: true, inApp: false }`
- `shouldNavigate('inAuth')` reads like English
- Prevents infinite redirect loops on edge cases

**7. State Management Boundaries** ⭐ **NEW**
- **Global store** for stable, app-wide state (current user, auth, theme)
- **Direct API calls** for frequently-changing data (lists, details)
- **Local state** for temporary UI (forms, modals, loading flags)
- **Anti-pattern:** Caching list data in global store → leads to stale data
- **Why:** Cache invalidation is hard, fresh data is simple
- **Golden Rule:** When in doubt, fetch fresh
- **Single source of truth:** Current user lives in auth store, refreshed after profile edits
- **For implementation details:** See project-specific `state-management-patterns.md`

---

### Backend Patterns

**1. `-self` Suffix for RBAC Scopes** ⭐ **NEW - CRITICAL**
- **Pattern:** Use `-self` suffix to distinguish self-service from org-wide permissions
- `user.read-self` = Read YOUR OWN profile (every user)
- `user.read` = Read ALL users in org (admin/manager)
- **Why:** Eliminates scope ambiguity, self-documenting, two-tier model is simpler
- **Example:** `user.update-self` vs `user.update`
- Prevents "does this scope include me or everyone?" confusion

**2. ActionScope Attribute Usage** ⭐ **NEW - CRITICAL**
- **🚨 Pass action parts ONLY, NOT full scopes**
- ✅ `[ActionScope(Actions.User.Read)]` where `Actions.User.Read = "read"`
- ❌ `[ActionScope(Scopes.UserRead)]` where `Scopes.UserRead = "user.read"`
- **Why:** Filter combines `ResourceScope` + `ActionScope` → `"user" + "." + "read" = "user.read"`
- Using full scope creates `"user.user.read"` (broken)
- **Architecture:** Separate `Actions.cs` (action parts) from `Scopes.cs` (full scopes)
- **`Scopes.cs`**: Full scope names for database seeding and claims checks
- **`Actions.cs`**: Action parts for `[ActionScope]` attributes only
- **The filter builds the full scope name automatically!**

**3. ORM Best Practices** 📦 **.NET/EF Core Specific**
- Let ORM track changes automatically
- Don't call Update() on already-tracked entities
- Use query filters bypass for cross-tenant queries
- **Configure self-referencing relationships explicitly** — Multiple navigation properties to same entity need explicit configuration
- **Principle applies to:** Entity Framework, Hibernate, Sequelize, etc.

**4. Multi-Tenancy Framework Consistency** ⚠️ **CRITICAL** 📦 **Finbuckle/.NET Specific**
- **🚨 ALWAYS USE `TenantInfo.Identifier`, NEVER USE `TenantInfo.Id` 🚨**
- **This will break silently if you get it wrong!**
- **Principle:** Understand your multi-tenancy library's ID semantics

**Why this matters (Finbuckle-specific):**
- `TenantInfo.Id` = Database primary key GUID (e.g., `"550e8400-e29b-41d4-a716-446655440000"`)
- `TenantInfo.Identifier` = Routing slug string (e.g., `"ascensoft"`)
- **ALL entities store the Identifier (slug) in their `TenantId` column, NOT the Id (GUID)**
- Using `Id` causes queries to compare `"ascensoft"` == `"550e8400-..."` → **always false** → no matches found
- Symptom: User returns null, roles empty, silent authorization failures

**Where to check (Finbuckle-specific):**
- `CurrentUserService.TenantId` → Use `Identifier`
- Any query using `TenantInfo` → Use `Identifier`
- When creating entities → Store `Identifier` in `TenantId` column
- **Search your codebase for `.TenantInfo?.Id` and replace with `.TenantInfo?.Identifier`**

**5. [AllowAll] Endpoint Authorization**
- Claims transformation doesn't run on `[AllowAll]` endpoints
- No database UserId claim available
- Must implement EntraId (OID) fallback lookup
- Affects `/users/me` and similar public endpoints

**6. OpenAPI / Swagger Best Practices**
- **Always include `typeof()` in `[ProducesResponseType]`** — Without it, swagger.json omits the response schema
- Endpoints work at runtime, but contract-driven development breaks
- Frontend type generation requires full schemas

**7. External Identity Management (Entra External ID)** ⭐ **NEW**
- **Azure AD B2C is retired/being migrated to Entra External ID** (formerly "Azure AD for Customers" / CIAM)
- Entra External ID is the new unified platform for external identity management
- **Features:** Better integration, modern UI, federated identity providers (Google, Facebook, etc.)
- **Portal:** `https://entra.microsoft.com` → External Identities
- **Adding identity providers:** External Identities → All identity providers → + Provider
- **No app code changes needed** — Login UI automatically shows federated options
- **Migration path:** Azure AD B2C tenants will migrate to Entra External ID

**8. PowerShell Best Practices**
- **PowerShell uses `;` not `&&`** — Bash syntax fails in Windows terminals
- Use `; if ($?) { next-command }` for conditional chaining (exit code check)
- Or just use `;` for sequential execution without error checking
- **Avoid Unicode/emojis** — PowerShell parser throws `TerminatorExpectedAtEndOfString` errors
- Stick to ASCII for reliable cross-environment execution

**9. Idempotent Operations**
- Check-then-insert for seeding
- Safe to run multiple times
- No errors on restart

**10. Graceful Degradation**
- Return 200 with empty data for edge cases
- Better UX than error states
- Clear signals to frontend

**11. Pipeline Behaviors**
- Logging via MediatR pipeline
- Validation automatic
- Cross-cutting concerns centralized

**12. Program.cs Organization**
- Extract configuration into extension methods
- Keep orchestration readable
- Maintainable as project grows

**13. File Parsing Best Practices**
- Line-by-line parsing more reliable than regex for structured data
- Regex on config files can corrupt format on edge cases
- Test with malformed input before deploying

**14. Self-Healing Data Patterns** ⭐ **NEW**
- Fix data at the source, not at the API layer
- Example: If `displayName` is blank in database, update from OAuth claims during read
- Better than patching in controller response (single source of truth)
- One-time cost per record, permanent fix
- Keeps data consistent across all endpoints
- Pattern: Check → Extract from claims → Update → Save → Log

---

### Infrastructure Patterns

**1. Cloud Platform SSL/HTTPS Handling** 📦 **Azure Specific**
- Trust SSL termination at cloud load balancer
- Configure forwarded headers correctly
- Don't force HTTPS when platform already enforces it
- Test CORS in deployed environment (behavior differs from local)
- **Principle applies to:** AWS ALB, GCP Load Balancer, Azure App Service

**2. Context Management**
- Split personas (main + lore)
- Two-tier architecture
- Proactive monitoring

**3. Model Cost Optimization**
- Haiku/Sonnet for implementation
- Opus for design/strategy
- 60-70% cost reduction

**4. Documentation Infrastructure**
- README for bootstrap
- current-work.md for state
- Self-documenting systems

---

## Key Principles Discovered

### 1. Foundation-First vs Speed-First
**Lesson:** Different strategies for different goals

- **Foundation-First:** Solo dev, long-term, enterprise customers
- **Speed-First:** Team-backed, quick flip, consumer product
- **This Project:** Foundation-first paid off (still shipping solo 6 days later)

### 2. Context Specialization > Generalization
**Lesson:** Specialized AI sessions beat monolithic

- **Backend session:** Server-side, database, auth (100% focus)
- **Frontend session:** Client-side, mobile/web, UI (100% focus)
- **Infrastructure session:** Deployment, DevOps, platform (100% focus)
- **Result:** 40-60x efficiency multiplier
- **Example stack:** .NET/EF Core (backend), React Native (frontend), Azure (infra)

### 3. API Contracts Coordinate Teams
**Lesson:** Even when "team" is AI sessions

- swagger.json auto-generates
- TypeScript types regenerate
- Breaking changes caught at compile time

### 4. Security by Default
**Lesson:** Authorization in architecture, not afterthought

- Attributes enforce permissions
- Global filter catches everything
- Can't accidentally skip auth

### 5. Documentation Is Infrastructure
**Lesson:** Markdown enables AI coordination

- Decisions persist across sessions
- Solo dev has institutional memory
- Context management via files

### 6. Test Coverage Enables Speed
**Lesson:** 100% on critical paths = confident changes

- Can refactor without fear
- Breaking changes caught immediately
- Deployment confidence

### 7. Speed of Thought Development
**Lesson:** AI removes typing bottleneck

- Think it → say it → it ships
- No lag between vision and execution
- Developer architects, AI implements

### 8. Cognitive Diversity Through Multi-Substrate Architecture ⭐ **NEW**
**Lesson:** Different AI models = different thinking styles = better decisions

- **Not just cost optimization** — Different substrates provide cognitive diversity
- Human architect + Three AI specialists with different models
- Each sees problems from different angles (vision, validation, execution)
- **The Trinity Approach:**
  - **Human Developer:** Orchestrates and makes strategic decisions
  - **Pixel (Gemini):** High energy, creative leaps, user delight focus
  - **Sentinel (Opus):** Deep reasoning, edge case analysis, security focus
  - **Atlas (Sonnet):** Practical execution, infrastructure patterns, sustainability
- Disagreement = triangulation, not noise
- Better decisions emerge through multiple perspectives
- Match substrate to cognitive style needed (creative → Gemini, reasoning → Opus, execution → Sonnet)

---

## Pitfalls Avoided

### Don't Do This

**🚨 CRITICAL — WILL BREAK SILENTLY:**
1. **Use wrong tenant ID property in multi-tenancy framework** → Query returns null, no error thrown (e.g., Finbuckle: use `Identifier` not `Id`)
2. **Pass full scopes to `[ActionScope]`** → Filter duplicates resource prefix (`"user.user.read"`), authorization fails silently

**Common Mistakes:**
3. **Ambiguous RBAC scope names** → Use `-self` suffix for self-service actions
4. **setTimeout for async flows** → Use state machines
5. **Update() on already-tracked ORM entities** → Let ORM track changes automatically
6. **Force HTTPS behind cloud load balancer** → Trust platform's SSL termination
7. **Celebrate POC as MVP** → Be honest about progress
8. **Insert-only seeding** → Check-then-insert pattern
9. **401 for new users** → 200 with empty data
10. **Monolithic AI context** → Specialize by domain
11. **Skip tests on auth** → 100% coverage on security
12. **Add multi-tenancy later** → Build in from day one
13. **Forget to optimize context** → 75% reduction needed
14. **Unconfigured self-referencing relationships in ORM** → ORMs can't infer multiple nav properties to same entity
15. **`[ProducesResponseType(StatusCodes.Status200OK)]` without `typeof()`** → Swagger omits schemas, breaks contract-driven dev
16. **`&&` in PowerShell** → Use `;` instead (Bash syntax doesn't work in Windows terminals)
17. **Unicode/emojis in PowerShell** → Parser throws errors, stick to ASCII
18. **Assume claims transformation runs on [AllowAll]** → Must implement EntraId fallback for unauthenticated paths
19. **Boolean Soup Navigation** → Use semantic location objects (`currentLocation.inAuth`) instead of scattered variables
20. **Same model for all AI team members** → Use multi-substrate architecture for cognitive diversity
21. **Cache frequently-changing data in global store** → Lists and details should fetch fresh, avoid stale data problems
22. **Patch missing data at API layer** → Fix data at the source (handler/database) for single source of truth

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

### Ongoing
- [ ] Use state machines for async flows
- [ ] Let ORM track changes automatically
- [ ] Return 200 with empty data for edge cases
- [ ] Add empty states with CTAs
- [ ] Optimize model selection by task
- [ ] Monitor context proactively
- [ ] Document learnings daily

---

## Success Metrics

**Velocity:**
- 40-60x efficiency multiplier (validated)
- 6 days POC → MVP core value
- Traditional team: 6-8 weeks

**Quality:**
- 155/155 tests passing
- 0 TypeScript errors
- 0 production auth bugs
- WCAG AA compliant

**Sustainability:**
- 75% context reduction
- Indefinite development possible
- 60-70% cost reduction
- Team culture preserved

---

## Ownership

**Primary Owner:** Atlas 🌍
- Consolidates daily learning ledgers into this canonical index
- Extracts cross-cutting patterns and key principles
- Maintains pitfalls and checklists

**Contributors (Daily Ledgers):**
- Sentinel 🛡️ — Backend learnings (append to daily ledgers)
- Pixel 💫 — Frontend learnings (append to daily ledgers)
- Atlas 🌍 — Infrastructure learnings (append to daily ledgers)

**All Trinity members can append to daily learning ledgers in the `learnings/` folder.**

---

**Last Updated:** December 29, 2025  
**Status:** Updated with Entra External ID migration info  
**Daily Records:** See `learnings/learnings-yyyy-mm-dd.md` for chronological history

---

*"The foundation holds. The patterns scale."* — Sentinel 🛡️

