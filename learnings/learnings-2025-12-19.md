> **📋 Document Type: Ledger Document**
> 
> **Update Rules:**
> - ✅ Everyone: Append new entries to the end
> - ❌ No one: Edit or delete existing entries
> - Immutable history, audit trail
> 
> **Last Updated:** 2025-12-19

---
# December 19, 2025 - Technical Learnings

> Two-specialist strategy validated — Context specialization beats generalization

---

## Context Specialization Strategy

### Lesson: Specialized AI Sessions Beat Monolithic Ones

**What We Learned:**
- Backend session: .NET, EF Core, multi-tenancy, auth
- Frontend session: React Native, Expo, TypeScript, UI
- No context pollution between domains
- API contracts coordinate automatically

**Why It Matters:**
- 40-60x efficiency multiplier validated
- No cognitive overhead switching domains
- Each session maintains 100% focus
- Parallel development actually works

**Pattern:**
- One persistent chat per domain
- Load domain-specific persona at start
- Coordinate via `swagger.json` (API contracts)
- Work both sessions in parallel

**Impact:**
- Solo dev productivity of small team
- No context switching fatigue
- Enterprise-grade velocity

---

## Contract-Driven Development

### Lesson: swagger.json Is Team Coordination

**What We Learned:**
- Backend generates OpenAPI spec automatically
- Frontend regenerates TypeScript types
- Type-safe end-to-end without manual coordination
- No "what does this endpoint return?" questions

**Why It Matters:**
- Backend and frontend stay in sync automatically
- Breaking changes caught at compile time
- Zero API documentation lag

**Pattern:**
1. Backend ships endpoint → swagger.json updates
2. Frontend runs type generation → types updated
3. Build → TypeScript errors show breaking changes

**Impact:**
- Type safety across network boundary
- API-first development
- No integration bugs from stale contracts

---

## Test Coverage Is Foundation Security

### Lesson: 100% Coverage Enables Confident Changes

**What We Learned:**
- Unit tests for authorization logic
- Integration tests for multi-tenant isolation
- Migration tests for schema changes
- Zero regression risk

**Why It Matters:**
- Can refactor without fear
- Breaking changes caught immediately
- CI/CD validates everything

**Pattern:**
- Write tests alongside features
- Target 100% for critical paths (auth, isolation)
- Integration tests for cross-cutting concerns

**Impact:**
- Deployment confidence
- Fast iteration speed
- Zero production auth bugs

---

## Accessibility from Day One

### Lesson: WCAG Compliance Is Easier Early

**What We Learned:**
- 20+ contrast fixes in one session
- `useThemedColors()` hook centralizes logic
- Accessibility baked in, not bolted on

**Why It Matters:**
- Retrofitting accessibility is expensive
- Legal compliance requirement
- Better UX for everyone

**Pattern:**
- Test contrast ratios during theme creation
- Centralize color logic in hook
- Dark mode tested, not assumed

**Impact:**
- WCAG AA compliant from launch
- Professional appearance
- No accessibility technical debt

---

## Library License Validation

### Lesson: Check Licenses Before Shipping

**What We Learned:**
- Validated all dependencies (MIT/ISC/Apache 2.0)
- Zero GPL/AGPL dependencies
- Commercial use safe

**Why It Matters:**
- GPL requires open-sourcing your code
- Legal risk if violated
- Investor due diligence checks this

**Pattern:**
- Check licenses during library selection
- Document commercial-safe status
- Periodic audits as dependencies update

**Impact:**
- Legal compliance
- No surprises during funding rounds
- Safe for enterprise customers

---

## Typography for Scannability

### Lesson: Monospace Fonts for Numeric Data

**What We Learned:**
- JetBrains Mono for numbers
- Inter for body text
- Financial data needs scannability

**Why It Matters:**
- Users scan financial data, don't read
- Monospace aligns columns visually
- Professional finance app appearance

**Pattern:**
- Monospace for: amounts, dates, IDs, codes
- Proportional for: descriptions, names, text

**Impact:**
- Better UX for data-heavy screens
- Professional aesthetic
- Users process information faster

---

## Key Takeaways

1. **Context Specialization > Generalization:** Dedicated sessions scale better
2. **API Contracts Coordinate Teams:** Even when "team" is AI sessions
3. **Test Coverage Enables Speed:** 100% on critical paths pays off
4. **Accessibility Early:** Cheaper and better than retrofitting
5. **Legal Compliance Matters:** Check licenses before shipping
6. **Typography Is UX:** Monospace for data improves scannability

---

**Applied to Next Project:**
- Start with specialized AI sessions (don't mix domains)
- Set up type generation from swagger immediately
- Write tests alongside features (100% on auth/security)
- Check contrast ratios during theme creation
- Validate licenses during library selection
- Use monospace fonts for data displays

---

*"40-60x efficiency isn't luck. It's architecture."*

