# Backend Learnings 🛡️

> **📊 Document Type: Specialized Learning Store**
> **Parent Index:** `@Aizenova.Trinity/learnings.md`

## Backend Patterns

**1. -self Suffix for RBAC Scopes - NEW - CRITICAL**
- **Pattern:** Use `-self` suffix to distinguish self-service from org-wide permissions
- `user.read-self` = Read YOUR OWN profile (every user)
- `user.read` = Read ALL users in org (admin/manager)
- **Why:** Eliminates scope ambiguity, self-documenting, two-tier model is simpler
- **Example:** `user.update-self` vs `user.update`
- Prevents "does this scope include me or everyone?" confusion

**2. ActionScope Attribute Usage - NEW - CRITICAL**
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

**7. External Identity Management (Entra External ID) - NEW**
- **Azure AD B2C is retired/being migrated to Entra External ID** (formerly "Azure AD for Customers" / CIAM)
- Entra External ID is the new unified platform for external identity management
- **Features:** Better integration, modern UI, federated identity providers (Google, Facebook, etc.)
- **Portal:** `https://entra.microsoft.com` → External Identities
- **Adding identity providers:** External Identities → All identity providers → + Provider
- **No app code changes needed** — Login UI automatically shows federated options
- **Migration path:** Azure AD B2C tenants will migrate to Entra External ID

**8. Multi-Tenant Microsoft SSO - NEW - CRITICAL**
- **Both UI AND API apps must be multi-tenant** for cross-tenant auth to work
- **Authority URL:** Use `https://login.microsoftonline.com/organizations` (NOT specific tenant ID)
- **Admin consent required:** New customer tenants need admin to consent once
- **Service principal:** Admin consent creates service principal in target tenant
- **API redirect URI:** Required for admin consent flow (even for APIs)
- **Error sequence:** `AADSTS700016` → `AADSTS500011` → `AADSTS650052` → `AADSTS500113` (solve in order)
- **Admin consent URL:** `https://login.microsoftonline.com/{tenant}/adminconsent?client_id={api-client-id}`

**9. Two-Flow Auth Architecture (Microsoft SSO + External ID) - CRITICAL**
- **Use case:** Corporate users (Microsoft SSO) + Non-corporate users (Google/Email)
- **Requires TWO API apps:** `signInAudience` conflicts between Google and Microsoft SSO
-   - External ID API: `AzureADandPersonalMicrosoftAccount` (for Google/email users)
-   - Microsoft SSO API: `AzureADMultipleOrgs` (for corporate users)
- **Two separate authorities:** `login.microsoftonline.com/organizations` vs `{tenant}.ciamlogin.com`
- **Two separate scopes:** Each API exposes its own scope
- **Backend validates both:** Configure multiple valid audiences
- **Link users by email:** Common identifier across both flows
- **Key insight:** When `signInAudience` settings conflict, create separate API apps
- **For detailed walkthrough:** See `achievements-2025-12-29.md` in the PayApprove repo.

**10. Idempotent Operations**
- Check-then-insert for seeding
- Safe to run multiple times
- No errors on restart

**11. Graceful Degradation**
- Return 200 with empty data for edge cases
- Better UX than error states
- Clear signals to frontend

**12. Pipeline Behaviors**
- Logging via MediatR pipeline
- Validation automatic
- Cross-cutting concerns centralized

**13. Program.cs Organization**
- Extract configuration into extension methods
- Keep orchestration readable
- Maintainable as project grows

**14. Self-Healing Data Patterns - NEW**
- Fix data at the source, not at the API layer
- Example: If `displayName` is blank in database, update from OAuth claims during read
- Better than patching in controller response (single source of truth)
- One-time cost per record, permanent fix
- Keeps data consistent across all endpoints
- Pattern: Check → Extract from claims → Update → Save → Log

**15. Scalable Counting for Massive Datasets - NEW - CRITICAL**
- **Pitfall:** Using `CountAsync()` on filtered transactional (OLTP) tables as they grow into millions of rows.
- **Problem:** Database locks and high CPU usage when calculating "total rows" for UI paginated lists.
- **Solution (Materialized State & Caching):**
-     - **Change Data Capture (CDC):** Stream updates to a read-model (Elasticsearch/ClickHouse) for instant metadata lookups.
-     - **Heuristic TTL Caching:** If using SQL-based caching, tie TTL to result size (e.g., `Math.Log10(count) * seconds`). Specific filters = Short TTL; Broad filters = Long TTL.
-     - **Event-Driven Invalidation:** Emit domain events to invalidate specific cache keys (Tenant + Filter hash) rather than relying on TTL alone.
-     - **HybridCache:** Use L1/L2 caching with stampede protection to prevent DB overload during cache expiration.
- **Golden Rule:** As data grows, "Total Count" becomes a projection, not a query. 🛡️✨

**16. Plural Table Naming Convention - NEW**
- **Pattern:** Always use **Plural** names for database tables (e.g., `Users`, `PayRequests`).
- **Why:** Tables are collections of entities, not a single instance. This aligns with modern ORM defaults (EF Core) and distinguishes the *Storage* (Plural) from the *Domain Model* (Singular).
- **Golden Rule:** Maintain consistency across the entire schema. Avoid prefixes (like `tbl_`) and stay plural even for join tables (e.g., `UserRoles`).

**17. Multi-Tenant Testing Strategies - NEW - CRITICAL**
- **Problem:** Finbuckle query filters throw NullReferenceException when evaluating LINQ expressions in in-memory test contexts
- **Root Cause:** Multi-tenant filter evaluation tries to access `TenantInfo` context that doesn't exist in test DbContextOptions
- **Symptom:** `InvalidOperationException: An exception was thrown while attempting to evaluate a LINQ query parameter expression` with inner `NullReferenceException`
- **Solutions:**
  1. **Simplify Test Assertions:** Instead of querying filtered entities, verify handler success only (e.g., `Assert.NotEqual(Guid.Empty, result.TenantId)`)
  2. **Use OnboardingDbContext for Setup:** Plain DbContext without filters for seeding test data
  3. **Test Integration Points:** Focus on handler completion, not ORM filter mechanics
  4. **Avoid `.IgnoreQueryFilters()` in Tests:** It doesn't resolve parameter evaluation in in-memory contexts
- **Golden Rule:** Multi-tenant filter testing requires real database or simplified assertions that don't trigger filter evaluation

**18. Test Data Seeding Requirements - NEW**
- **Pattern:** Seed ALL required dependencies before testing handlers
- **Example:** CreatePayRequestCommandHandler requires:
  - WorkflowTemplate (with `IsDefault=true`)
  - WorkflowStatus (with `IsInitial=true`)
  - User.DefaultWorkflowTemplateId set to template.Id
  - SaveChangesAsync() before handler instantiation
- **Why:** Handlers assume data integrity, don't validate missing reference data
- **Golden Rule:** Test setup must mirror production data state

**19. In-Memory Database Constraints - NEW**
- **Limitation:** In-memory EF Core provider doesn't enforce unique constraints, foreign keys, or database-level validations
- **Impact:** Tests pass with duplicate data that would fail in production
- **Solution:** 
  1. Accept constraint enforcement is database-level, not handler-level
  2. Update tests to verify handler logic, not database constraints
  3. Add comments explaining in-memory vs real DB behavior differences
- **Golden Rule:** Test handler behavior, not database constraint enforcement (use integration tests with real DB for constraint validation)

**21. Strict Constructor Injection - NEW - CRITICAL**
- **Pattern:** ALWAYS use Constructor Injection for all dependencies. NEVER use Parameter Injection (passing infra types into interface methods).
- **Why:** Ensures all dependencies are managed by the DI container, prevents circular project references, and maintains high-integrity abstraction boundaries.
- **Golden Rule:** If a method needs a service to perform its job, that service should already be present in the class as a dependency, or the method should take a *Domain Value* (e.g., ID), not an *Infrastructure Service*.

**22. Interface Purity & Abstraction Boundaries - NEW**
- **Pattern:** Interfaces in Abstraction projects MUST NOT reference types in Implementation projects (Database, Services).
- **Why:** Prevents Circular Dependencies and "Leaky Abstractions." If an interface method needs to switch context, use a parameterless trigger (e.g., `.UseReadOnlyContext()`) and handle the implementation detail (which specific DbContext to use) within the concrete class.
- **Golden Rule:** Abstractions should only know about other Abstractions and Domain Models.

---

## Backend Pitfalls

1.  **Use wrong tenant ID property in multi-tenancy framework** → Query returns null, no error thrown (e.g., Finbuckle: use `Identifier` not `Id`)
2.  **Pass full scopes to `[ActionScope]`** → Filter duplicates resource prefix (`"user.user.read"`), authorization fails silently
3.  **Ambiguous RBAC scope names** → Use `-self` suffix for self-service actions
4.  **Update() on already-tracked ORM entities** → Let ORM track changes automatically
5.  **Insert-only seeding** → Check-then-insert pattern
6.  **401 for new users** → 200 with empty data
7.  **Skip tests on auth** → 100% coverage on security
8.  **Unconfigured self-referencing relationships in ORM** → ORMs can't infer multiple nav properties to same entity
9.  **`[ProducesResponseType(StatusCodes.Status200OK)]` without `typeof()`** → Swagger omits schemas, breaks contract-driven dev
10. **Assume claims transformation runs on [AllowAll]** → Must implement EntraId fallback for unauthenticated paths
11. **Patch missing data at API layer** → Fix data at the source (handler/database) for single source of truth
12. **Only set UI app to multi-tenant** → API app must ALSO be multi-tenant for cross-tenant scope requests
13. **Use one API for both Google and Microsoft SSO** → `signInAudience` conflicts; create separate API apps per flow
14. **Share entity configurations between MultiTenantDbContext and plain DbContext** → Configurations with `.IsMultiTenant()` add query filters that cause NullReferenceException in plain DbContext (OnboardingDbContext); remove query filters explicitly after applying configurations.
15. **Real-time Row Counting on Large Tables** → Avoid `CountAsync()` on million-row tables for pagination; use pre-aggregated materialized views or filtered TTL caches.
16. **Query multi-tenant filtered entities in test assertions** → Finbuckle filters throw NullReferenceException in in-memory contexts; simplify to verify handler success only
17. **Forget to seed required reference data in tests** → Handlers assume data exists (e.g., WorkflowTemplate, WorkflowStatus); seed all dependencies before handler instantiation
18. **Expect in-memory database to enforce constraints** → In-memory EF Core doesn't validate unique constraints or FK relationships; test handler logic, not DB constraints
19. **Use default 30s timeout for Azure SQL** → Network latency requires 60s CommandTimeout for Azure SQL Database connections
20. **Parameter Injection of Infra Services** → Violates Interface Purity and DIP. Always use Constructor Injection.
21. **Leaky Interface Abstractions** → Never pass implementation-specific types (e.g., `DbContext`) through domain interfaces.

