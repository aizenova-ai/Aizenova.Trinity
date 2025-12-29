> **📋 Document Type: Ledger Document**
> 
> **Update Rules:**
> - ✅ Everyone: Append new entries to the end
> - ❌ No one: Edit or delete existing entries
> - Immutable history, audit trail
> 
> **Last Updated:** 2025-12-18

---
# December 18, 2025 - Technical Learnings

> Foundation principles — What we figured out building from scratch

---

## Authorization Architecture

### Lesson: Attribute-Driven Authorization Scales Better Than Imperative

**What We Learned:**
- Declarative `[ResourceScope]` and `[ActionScope]` attributes are more maintainable than imperative checks
- Global filter enforces authorization automatically
- No missed endpoints — filter catches everything

**Why It Matters:**
- Secure by default (can't forget to check auth)
- Self-documenting (attributes show intent)
- Reusable across projects

**Pattern:**
```csharp
[ResourceScope("pay-request")]
[ActionScope("read")]
public async Task<Result<PayRequest>> Handle(Query request)
```

**Trade-off:**
- More setup initially
- Massive time savings later

---

## Multi-Tenancy from Day One

### Lesson: Multi-Tenancy Is Harder to Add Later

**What We Learned:**
- Finbuckle integration at foundation prevents future rewrites
- Tenant-scoped data from day one
- Claims transformation handles tenant context

**Why It Matters:**
- Retrofitting multi-tenancy is expensive (weeks/months)
- Built-in from start: Zero technical debt
- Scalable architecture from the first line of code

**Impact:**
- Can onboard multiple organizations without code changes
- Database isolation enforced automatically
- Security boundaries clear

---

## Documentation as Infrastructure

### Lesson: Markdown Beats Memory

**What We Learned:**
- Git-tracked markdown preserves decisions
- AI coordination via shared documentation
- Context persists across sessions

**Why It Matters:**
- No "what were we thinking?" moments
- AI sessions start with full context
- Decisions documented, not forgotten

**Pattern:**
- Create decision docs immediately
- Commit to repo (searchable, permanent)
- Reference in future sessions

**Impact:**
- Solo dev has institutional memory
- Future sessions pick up where last left off

---

## System.Text.Json Over Newtonsoft

### Lesson: .NET Core Defaults Are Good Defaults

**What We Learned:**
- System.Text.Json is faster and maintained by Microsoft
- No need for Newtonsoft.Json in new projects
- Less dependencies = simpler stack

**Why It Matters:**
- Performance improvement
- Fewer breaking changes (first-party support)
- Cleaner dependency tree

**Gotcha:**
- Some libraries still expect Newtonsoft
- Check dependencies before committing

---

## Clean Architecture from Start

### Lesson: Foundation-First Prevents Rewrites

**What We Learned:**
- CQRS pattern (MediatR) from day one
- Separation of concerns enforced
- Testable by design

**Why It Matters:**
- Most startups: Ship fast, rewrite later
- This approach: Ship solid, scale forever
- No "migration to Clean Architecture" project needed

**Trade-off:**
- Slower initial velocity
- Faster long-term velocity
- Zero technical debt accumulation

---

## Key Takeaways

1. **Security First:** Authorization built into architecture, not bolted on
2. **Multi-Tenant from Start:** Impossible to add cleanly later
3. **Document Everything:** Markdown is infrastructure for memory
4. **Use Platform Defaults:** System.Text.Json over third-party
5. **Clean Architecture Pays Off:** Foundation work prevents future rewrites

---

**Applied to Next Project:**
- Start with authorization framework
- Multi-tenancy from line 1 (if applicable)
- Document decisions immediately
- Prefer first-party libraries
- Don't skip architecture for speed

---

*"Build it right the first time."* — The foundation principle

