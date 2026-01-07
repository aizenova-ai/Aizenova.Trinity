# Backend Learnings 🛡️

> **📊 Document Type: Specialized Learning Store**
> **Parent Index:** `@Aizenova.Trinity/learnings.md`

## Backend Patterns

**0. THE "NO DYNAMIC" PROTOCOL (Type Safety Absolute)**
- **Pattern:** The use of `dynamic`, `object` (as a catch-all), or `ExpandoObject` is strictly forbidden in business logic.
- **Rationale:** In an AI-augmented workflow, type blindness allows models to "hallucinate" properties. Strict C# types (records, classes, interfaces) are the only way to ensure the AI remains grounded in reality.
- **Contractual Standard:** Every field in a DTO must be explicitly typed. Avoid `Dictionary<string, object>`.

**1. Semantic RBAC Scopes**
- **Pattern:** Use clear suffixes (e.g., `-self`) to distinguish between personal and administrative/organizational permissions.
- **Rationale:** Eliminates ambiguity in scope names and provides a self-documenting security model.

**2. Attribute-Driven Authorization**
- **Pattern:** Use declarative attributes on controllers/actions that map to resource-based or action-based scopes.
- **Rationale:** Centralizes security logic and makes it "secure by default."

**3. ORM Best Practices**
- **Pattern:** Leverage automatic change tracking; avoid manual update calls on tracked entities.
- **Pattern:** Explicitly configure complex or self-referencing relationships that ORMs may fail to infer.
- **Rationale:** Ensures data integrity and minimizes side effects during persistence.

**4. Multi-Tenancy Identity vs. Routing**
- **Pattern:** Always distinguish between **Internal Identity** (immutable, optimized for storage) and **Public Routing** (human-readable, used for URLs).
- **Rationale:** Prevents collation issues and join failures while maintaining SEO/user-friendly URLs.

**5. OpenAPI & Contract-Driven Development**
- **Pattern:** Ensure all API responses include explicit type information in metadata.
- **Rationale:** Necessary for high-fidelity client code generation and maintaining type safety end-to-end.

**6. Identity Federation Principles**
- **Pattern:** Trust the identity provider (IdP) for UI-level changes (e.g., adding social logins) when possible.
- **Pattern:** Design for multi-audience validation when supporting both corporate and consumer user flows.

**7. Idempotent Data Seeding**
- **Pattern:** Use a "check-then-insert" strategy for all initialization data.
- **Rationale:** Ensures the system can be restarted or redeployed without data duplication or errors.

**8. Pipeline Behaviors (Cross-Cutting Concerns)**
- **Pattern:** Centralize logging, validation, and auditing using pipeline/middleware patterns.
- **Rationale:** Keeps business logic clean and ensures consistent enforcement of system-wide rules.

**9. Strict Constructor Injection**
- **Pattern:** ALWAYS use Constructor Injection for all dependencies. NEVER use Parameter Injection (passing infra types into interface methods).
- **Rationale:** Ensures all dependencies are managed by the DI container and maintains high-integrity abstraction boundaries.

**10. Interface Purity**
- **Pattern:** Abstractions must not reference implementation-specific types (e.g., specific database contexts).
- **Rationale:** Prevents circular dependencies and "leaky abstractions."

**11. Performance: Binary Comparison for Keys**
- **Pattern:** Use binary-optimized comparisons (e.g., specific collations) for high-frequency string-based keys.
- **Rationale:** Significantly faster than standard linguistic comparisons which involve complex cultural rules.

**12. Performance: Clustered Index Strategy**
- **Pattern:** Use sequential keys for physical storage (clustering) even when using non-sequential logical IDs (like GUIDs).
- **Rationale:** Prevents database index fragmentation and maximizes write throughput.

**13. Contract Ownership & DTO Locality**
- **Pattern:** The Application Layer owns the Contract. DTOs live next to the logic that uses them.
- **Locality Standard:**
    - **Single-Use:** Nest within the specific Command/Query folder.
    - **Domain-Shared:** Place in `{Domain}/Common/`.
    - **System-Wide:** Place in `Common/Models/{Domain}/`.
- **Rationale:** Decouples business logic from transport layers (API, CLI, Workers) and maintains high locality.

**14. Metadata Hardening (2025/2026 Standards)**
- **Pattern:** ALWAYS provide a unique `Name` property to Http attributes (e.g., `[HttpGet(Name = "...")]`) to lock the Operation ID.
- **Pattern:** Use C# `required` + `init` properties for mandatory fields instead of `[Required]` attributes.
- **Rationale:** Enforces contracts at compile-time and ensures stable, high-fidelity client SDK generation without metadata drift.

**15. Context Bridging (The Async Boundary)**
- **Pattern:** When standard context propagation (like `AsyncLocal`) fails across execution boundaries (e.g., Middleware -> Function), use a persistent dictionary/items collection to pass metadata.
- **Rationale:** Ensures tenant/user context remains stable across asynchronous handoffs in isolated worker environments.

**16. CQRS-Lite Segregation (Read-Only Paths)**
- **Pattern:** Use a specific read-only abstraction for query handlers that omits mutation methods (Add/Update/Save).
- **Inheritance:** The primary data context interface should inherit from the read-only interface. This allows for polymorphic usage where the full context can fulfill read-only requirements (e.g., in unit tests or shared services).
- **Rationale:** Enforces "Secure by Intent," prevents accidental writes in read paths, and allows for seamless integration of read replicas.

**17. Semantic Enum Serialization**
- **Pattern:** ALWAYS serialize enums as strings in API/Contract layers.
- **Rationale:** Prevents logic drift across platforms (where integer values may differ or be opaque) and maintains human-readable contracts.

---

## Backend Pitfalls

1. **Confusing Routing IDs with Database IDs** → Causes query failures and collation mismatches.
2. **Ambiguous Security Scopes** → Leads to "over-permissioning" or confused users.
3. **Leaky Abstractions** → Passing implementation details through domain interfaces creates brittle, hard-to-test systems.
4. **Real-time Aggregation on Massive Sets** → Avoid expensive "Total Count" queries on large tables; use projections or caching.
5. **Ignoring Build Warnings in Tests** → Leads to "warning rot" and masks logic errors.
6. **Transport-Owned Contracts** → Defining DTOs in the API layer makes them inaccessible to non-web consumers and leads to "Metadata Erosion."
