> **📋 Document Type: Ledger Document**
> 
> **Update Rules:**
> - ✅ Everyone: Append new entries to the end
> - ❌ No one: Edit or delete existing entries
> - Immutable history, audit trail
> 
> **Last Updated:** 2025-12-20

---
# December 20, 2025 - Technical Learnings

> POC vs MVP — Understanding what you've actually built

---

## POC vs MVP Reality Check

### Lesson: Foundation ≠ Product

**What We Learned:**
- Built: Multi-tenant auth, database schema, API contracts, deployment pipeline
- Didn't build: User value features, approval workflow, notifications
- **Built the plumbing, not the business**

**Why It Matters:**
- Customers pay for features, not architecture
- Investors want user metrics, not clean code
- Foundation enables MVP, but isn't MVP

**Pattern:**
- POC validates architecture
- MVP validates product-market fit
- Don't confuse the two

**Impact:**
- Clear expectations (6 more weeks of work ahead)
- Honest assessment prevents false confidence
- Foundation work was necessary, not sufficient

---

## Foundation-First Trade-Off

### Lesson: Build Right vs Build Fast

**What We Learned:**
- Most startups: Features on duct tape, rewrite later
- This project: Solid foundation, features slower initially
- Trade-off: Slower launch, confident scaling

**Why It Matters:**
- Duct tape startups: 6 months in, hiring engineers for refactoring
- Foundation-first: 6 months in, still shipping solo
- Different strategies for different goals

**Pattern:**
- Duct tape: Speed to market, technical debt later
- Foundation-first: Slower start, scale without rewrite

**When to Choose Foundation-First:**
- Solo dev (no team to parallelize rewrites)
- Long-term play (not flipping in 12 months)
- Enterprise customers (they audit your code)

---

## Infrastructure Pitfalls Documented

### Lesson: Azure App Service + SSL Termination Changes CORS

**What We Learned:**
- Azure terminates SSL at load balancer
- App sees HTTP, but requests came as HTTPS
- CORS origin checks fail if not configured correctly

**Solution:**
- Configure forwarded headers middleware
- Trust Azure's SSL termination
- Test CORS in deployed environment, not just local

**Pattern:**
```csharp
app.UseForwardedHeaders();
app.UseCors();
```

**Impact:**
- CORS working in production
- Documented for future Azure deployments
- Saved hours of debugging for next project

---

## HTTPS Redirection Pitfall

### Lesson: Don't Force HTTPS When Azure Already Did It

**What We Learned:**
- Azure enforces HTTPS at load balancer
- App forcing HTTPS again = redirect loop
- Health checks fail (can't complete handshake)

**Solution:**
- Trust Azure's HTTPS enforcement
- Don't add `app.UseHttpsRedirection()` when behind load balancer
- Configure properly for environment

**Pattern:**
```csharp
if (!app.Environment.IsDevelopment())
{
    // Don't force HTTPS - Azure already did it
}
```

**Impact:**
- Health checks working
- No redirect loops
- Deployment succeeds

---

## Multi-Repo Build Complexity

### Lesson: Path Handling in Azure DevOps Requires Care

**What We Learned:**
- Multiple repos in pipeline = complex paths
- Checkout path affects restore commands
- Working directory must be explicit

**Solution:**
- Use absolute paths in pipeline YAML
- Test pipeline changes in branch first
- Document working directory expectations

**Impact:**
- Reliable builds
- Predictable deployments
- Future devs understand path structure

---

## Three-Specialist Coverage

### Lesson: Backend + Frontend + Infrastructure = Complete Solo Dev Team

**What We Learned:**
- Backend (Sentinel): APIs, auth, database
- Frontend (Pixel): UI, UX, mobile
- Infrastructure (Atlas): Deployment, monitoring, operations

**Why It Matters:**
- Complete domain expertise coverage
- No knowledge gaps
- Solo dev has full-team capabilities

**Pattern:**
- Specialize AI personas by domain
- Let each own their domain completely
- Coordinate via documentation + contracts

**Impact:**
- Solo dev with team-level velocity
- No bottlenecks (each specialist works independently)
- Foundation for scaling (add specialists as needed)

---

## Key Takeaways

1. **Be Honest About Progress:** POC ≠ MVP, foundation ≠ features
2. **Foundation-First Has Trade-Offs:** Slower start, confident scale
3. **Cloud Platforms Have Quirks:** Document Azure-specific patterns
4. **HTTPS Termination Changes Behavior:** Don't double-enforce
5. **Multi-Repo Complexity Is Real:** Use absolute paths, test carefully
6. **Three Specialists = Complete Coverage:** Backend, Frontend, Infrastructure

---

## Pitfalls to Avoid Next Time

1. **Don't celebrate POC as MVP** — Set honest expectations
2. **Trust cloud HTTPS termination** — Don't force it in app
3. **Test CORS in deployed environment** — Local doesn't match prod
4. **Document multi-repo path handling** — Future self will thank you
5. **Add Infrastructure specialist early** — Don't wait for deployment problems

---

**Applied to Next Project:**
- Separate POC and MVP milestones clearly
- Choose foundation-first or duct-tape strategy explicitly
- Document cloud-specific configurations immediately
- Test in deployed environment, not just local
- Establish three-specialist coverage from start

---

*"We built the plumbing. Now let's build the business."*

