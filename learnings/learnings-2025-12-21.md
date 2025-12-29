> **📋 Document Type: Ledger Document**
> 
> **Update Rules:**
> - ✅ Everyone: Append new entries to the end
> - ❌ No one: Edit or delete existing entries
> - Immutable history, audit trail
> 
> **Last Updated:** 2025-12-21

---
# December 21, 2025 - Technical Learnings

> State machines > setTimeout — Fighting race conditions the right way

---

## State Machine Over Duct Tape

### Lesson: setTimeout Is a Code Smell for Race Conditions

**What We Learned:**
- Navigation firing before state updates = race condition
- First attempt: `setTimeout(navigate, 100)` — duct tape
- Correct solution: Explicit state machine with event emitter

**Why It Matters:**
- setTimeout "works" but introduces timing bugs
- Production load patterns break timing assumptions
- State machines are reliable under all conditions

**Pattern:**
```typescript
// ❌ BAD: Timing-dependent
const handleSubmit = async () => {
  await updateState();
  setTimeout(() => navigate('/next'), 100); // Hope 100ms is enough
};

// ✅ GOOD: Event-driven
const handleSubmit = async () => {
  await updateState();
  eventEmitter.emit('state-updated');
};

eventEmitter.on('state-updated', () => {
  navigate('/next'); // Reacts to state, not time
});
```

**Impact:**
- Zero race conditions
- Works under load
- Scalable pattern for complex flows

---

## EF Core Tracking Gotcha

### Lesson: Don't Call Update() on Already-Tracked Entities

**What We Learned:**
- `_context.Users.Update(user)` fails if entity already tracked
- EF Core tracks changes automatically
- Explicit `Update()` is redundant and error-prone

**Error:**
```
Cannot update identity column 'ClusteredId'
```

**Solution:**
```csharp
// ❌ BAD: Explicit update on tracked entity
var user = await _context.Users.FindAsync(id);
user.Name = "Updated";
_context.Users.Update(user); // ← Fails

// ✅ GOOD: Let EF Core track changes
var user = await _context.Users.FindAsync(id);
user.Name = "Updated";
await _context.SaveChangesAsync(); // ← Works
```

**Impact:**
- Correct EF Core usage
- Performance improvement (no redundant tracking)
- Prevents identity column errors

---

## Finbuckle Tenant Isolation Nuance

### Lesson: Two Tenant Identifiers Can Cause Bugs

**What We Learned:**
- Finbuckle's `TenantInfo` has TWO IDs:
  - `Id` (GUID string) — internal
  - `Identifier` (string slug) — user-facing
- Using wrong one breaks authorization

**Gotcha:**
```csharp
// ❌ BAD: Using internal ID for claims
claims.Add(new Claim("tenant", tenantInfo.Id)); // GUID

// ✅ GOOD: Using identifier for claims
claims.Add(new Claim("tenant", tenantInfo.Identifier)); // Slug
```

**Why It Matters:**
- Frontend expects identifier (slug)
- Backend uses identifier for routing
- Mismatch = 403 Forbidden on valid requests

**Impact:**
- Multi-tenant isolation working correctly
- Authorization bugs fixed
- Clear documentation for future

---

## Idempotent Database Seeding

### Lesson: Seed Operations Must Be Rerunnable

**What We Learned:**
- Seed code runs on every startup
- Insert-only seeding fails on second run
- Check-then-insert pattern is idempotent

**Pattern:**
```csharp
// ❌ BAD: Fails on second run
await _context.Scopes.AddRangeAsync(builtInScopes);

// ✅ GOOD: Idempotent
foreach (var scope in builtInScopes)
{
    if (!await _context.Scopes.AnyAsync(s => s.Name == scope.Name))
    {
        await _context.Scopes.AddAsync(scope);
    }
}
```

**Impact:**
- Seed runs successfully every time
- No errors on restart
- Safe deployment pattern

---

## Graceful Degradation for New Users

### Lesson: 200 OK with Empty Data > 401 for New Users

**What We Learned:**
- `/api/users/me` returns 401 for unauthenticated
- But new OAuth users ARE authenticated (just no tenant yet)
- Return 200 with empty tenant signals onboarding needed

**Pattern:**
```csharp
// ❌ BAD: 401 for legitimate new user
if (user.TenantId == null) return Unauthorized();

// ✅ GOOD: 200 with empty data
return Ok(new { 
    tenantIdentifier = null, 
    roles = [],
    scopes = []
});
```

**Impact:**
- Better UX (no error states)
- Clear onboarding signal to frontend
- Legitimate new users don't see errors

---

## Program.cs Extension Methods

### Lesson: Extract Configuration for Readability

**What We Learned:**
- Program.cs grew to 349 lines (unreadable)
- Extract related config into extension methods
- Result: 12 lines of orchestration

**Pattern:**
```csharp
// BEFORE: 349 lines of configuration
builder.Services.AddDbContext(...);
builder.Services.AddAuthentication(...);
// ... 340 more lines

// AFTER: 12 lines of orchestration
builder.Services.AddInfrastructure(builder.Configuration);
builder.Services.AddApiServices();
builder.Services.AddApiMappers();

var app = builder.Build();
await app.InitializeDatabaseAsync();
app.ConfigurePipeline();
app.Run();
```

**Impact:**
- Readable startup
- Testable configuration
- Maintainable as project grows

---

## Metro Bundler CommonJS/ESM

### Lesson: React Native Web Needs CommonJS Priority

**What We Learned:**
- Some dependencies use `import.meta` (ESM-only)
- React Native Web expects CommonJS
- Configure `unstable_conditionNames` for CommonJS priority

**Solution:**
```javascript
// metro.config.js
resolver: {
  unstable_conditionNames: ['require', 'import']
}
```

**Impact:**
- Web build working
- Cross-platform compatibility
- No `import.meta` errors

---

## Key Takeaways

1. **State Machines > setTimeout:** Reliable under all conditions
2. **EF Core Tracks Automatically:** Don't call Update() on tracked entities
3. **Finbuckle Has Two IDs:** Use Identifier (slug), not Id (GUID)
4. **Idempotent Seeding:** Check-then-insert pattern
5. **Graceful Degradation:** 200 with empty data > 401 for new users
6. **Extract Configuration:** Keep Program.cs readable
7. **Metro Needs CommonJS Priority:** React Native Web quirk

---

**Applied to Next Project:**
- Use event emitters for async flows (no setTimeout)
- Let EF Core track changes (no explicit Update())
- Document which tenant ID to use where
- All seed operations idempotent from day one
- Return 200 with empty data for edge cases
- Extract Program.cs configuration early
- Configure Metro for CommonJS priority if using Web

---

*"The first solution that works isn't always the right solution."*

