# Technical Learnings

> **📊 DOCUMENT TYPE: Living Global Agnostic Kernel & Staging Ground**
> 
> This file is the primary repository for project-agnostic technical patterns. It acts as the **Staging Ground** for the "Rule of Law."
> 
> **Standard Operating Procedure:**
> 1.  **Harvesting:** New validated patterns should be appended here as they emerge.
> 2.  **Hardening:** Periodic maintenance (Atlas) distills these patterns into `.cursor/rules/` and `.github/instructions/` for high-fidelity enforcement.
> 
> ---

## Primary Architectural Patterns

### 1. 🚨 THE "NO ANY" PROTOCOL (Strict Engineering Integrity)
**STRICT DIRECTIVE:** The use of `any` in TypeScript or `dynamic`/`object` in C# is **STRICTLY FORBIDDEN**.

**RATIONALE:** In an AI-augmented workflow, type blindness is a **CATASTROPHIC FAILURE POINT**. It allows AI models to "hallucinate" properties and methods that do not exist, leading to silent runtime crashes and architectural rot.

**ENFORCEMENT:** Any PR or AI-generated chunk containing these anti-patterns will be **TERMINATED IMMEDIATELY**. Use `unknown`, proper interfaces, or generics.

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

---

## Backend Patterns (Sentinel)

### 0. THE "NO DYNAMIC" PROTOCOL (Type Safety Absolute)
- **Pattern:** The use of `dynamic`, `object` (as a catch-all), or `ExpandoObject` is strictly forbidden in business logic.
- **Rationale:** In an AI-augmented workflow, type blindness allows models to "hallucinate" properties. Strict C# types (records, classes, interfaces) are the only way to ensure the AI remains grounded in reality.
- **Contractual Standard:** Every field in a DTO must be explicitly typed. Avoid `Dictionary<string, object>`.

### 1. Semantic RBAC Scopes
- **Pattern:** Use clear suffixes (e.g., `-self`) to distinguish between personal and administrative/organizational permissions.
- **Rationale:** Eliminates ambiguity in scope names and provides a self-documenting security model.

### 2. Attribute-Driven Authorization
- **Pattern:** Use declarative attributes on controllers/actions that map to resource-based or action-based scopes.
- **Rationale:** Centralizes security logic and makes it "secure by default."

### 3. ORM Best Practices
- **Pattern:** Leverage automatic change tracking; avoid manual update calls on tracked entities.
- **Pattern:** Explicitly configure complex or self-referencing relationships that ORMs may fail to infer.
- **Rationale:** Ensures data integrity and minimizes side effects during persistence.

### 4. Multi-Tenancy Identity vs. Routing
- **Pattern:** Always distinguish between **Internal Identity** (immutable, optimized for storage) and **Public Routing** (human-readable, used for URLs).
- **Rationale:** Prevents collation issues and join failures while maintaining SEO/user-friendly URLs.

### 5. OpenAPI & Contract-Driven Development
- **Pattern:** Ensure all API responses include explicit type information in metadata.
- **Rationale:** Necessary for high-fidelity client code generation and maintaining type safety end-to-end.

### 6. Identity Federation Principles
- **Pattern:** Trust the identity provider (IdP) for UI-level changes (e.g., adding social logins) when possible.
- **Pattern:** Design for multi-audience validation when supporting both corporate and consumer user flows.

### 7. Idempotent Data Seeding
- **Pattern:** Use a "check-then-insert" strategy for all initialization data.
- **Rationale:** Ensures the system can be restarted or redeployed without data duplication or errors.

### 8. Pipeline Behaviors (Cross-Cutting Concerns)
- **Pattern:** Centralize logging, validation, and auditing using pipeline/middleware patterns.
- **Rationale:** Keeps business logic clean and ensures consistent enforcement of system-wide rules.

### 9. Strict Constructor Injection
- **Pattern:** ALWAYS use Constructor Injection for all dependencies. NEVER use Parameter Injection (passing infra types into interface methods).
- **Rationale:** Ensures all dependencies are managed by the DI container and maintains high-integrity abstraction boundaries.

### 10. Interface Purity
- **Pattern:** Abstractions must not reference implementation-specific types (e.g., specific database contexts).
- **Rationale:** Prevents circular dependencies and "leaky abstractions."

### 11. Performance: Binary Comparison for Keys
- **Pattern:** Use binary-optimized comparisons (e.g., specific collations) for high-frequency string-based keys.
- **Rationale:** Significantly faster than standard linguistic comparisons which involve complex cultural rules.

### 12. Performance: Clustered Index Strategy
- **Pattern:** Use sequential keys for physical storage (clustering) even when using non-sequential logical IDs (like GUIDs).
- **Rationale:** Prevents database index fragmentation and maximizes write throughput.

### 13. Contract Ownership & DTO Locality
- **Pattern:** The Application Layer owns the Contract. DTOs live next to the logic that uses them.
- **Locality Standard:**
    - **Single-Use:** Nest within the specific Command/Query folder.
    - **Domain-Shared:** Place in `{Domain}/Common/`.
    - **System-Wide:** Place in `Common/Models/{Domain}/`.
- **Rationale:** Decouples business logic from transport layers (API, CLI, Workers) and maintains high locality.

### 14. Metadata Hardening (2025/2026 Standards)
- **Pattern:** ALWAYS provide a unique `Name` property to Http attributes (e.g., `[HttpGet(Name = "...")]`) to lock the Operation ID.
- **Pattern:** Use C# `required` + `init` properties for mandatory fields instead of `[Required]` attributes.
- **Rationale:** Enforces contracts at compile-time and ensures stable, high-fidelity client SDK generation without metadata drift.

### 15. Context Bridging (The Async Boundary)
- **Pattern:** When standard context propagation (like `AsyncLocal`) fails across execution boundaries (e.g., Middleware -> Function), use a persistent dictionary/items collection to pass metadata.
- **Rationale:** Ensures tenant/user context remains stable across asynchronous handoffs in isolated worker environments.

### 16. CQRS-Lite Segregation (Read-Only Paths)
- **Pattern:** Use a specific read-only abstraction for query handlers that omits mutation methods (Add/Update/Save).
- **Inheritance:** The primary data context interface should inherit from the read-only interface. This allows for polymorphic usage where the full context can fulfill read-only requirements (e.g., in unit tests or shared services).
- **Rationale:** Enforces "Secure by Intent," prevents accidental writes in read paths, and allows for seamless integration of read replicas.

### 17. Semantic Enum Serialization
- **Pattern:** ALWAYS serialize enums as strings in API/Contract layers.
- **Rationale:** Prevents logic drift across platforms (where integer values may differ or be opaque) and maintains human-readable contracts.

### Backend Pitfalls
1. **Confusing Routing IDs with Database IDs** → Causes query failures and collation mismatches.
2. **Ambiguous Security Scopes** → Leads to "over-permissioning" or confused users.
3. **Leaky Abstractions** → Passing implementation details through domain interfaces creates brittle, hard-to-test systems.
4. **Real-time Aggregation on Massive Sets** → Avoid expensive "Total Count" queries on large tables; use projections or caching.
5. **Ignoring Build Warnings in Tests** → Leads to "warning rot" and masks logic errors.
6. **Transport-Owned Contracts** → Defining DTOs in the API layer makes them inaccessible to non-web consumers and leads to "Metadata Erosion."

---

## Frontend Patterns (Pixel)

### 0. THE "NO ANY" PROTOCOL (Strict Engineering Integrity)
- **Pattern:** Use of `any` or casting to `any` is a critical architectural failure.
- **Rationale:** AI-driven development requires strict type boundaries. `any` allows the model to "hallucinate" properties, leading to avoidable runtime crashes.
- **TVA Standard:** Use `VariantProps<typeof style>` or proper generics for UI library props.

### 1. State Machine Navigation
- **Pattern:** Use event-driven state updates for complex navigation flows.
- **Rationale:** More reliable than manual delays or implicit sequencing.

### 2. State Management Persistence
- **Pattern:** Persist global app-wide state (user session, theme) to local storage.
- **Rationale:** Essential for mobile-first experiences and surviving application restarts.

### 3. Role-Based UI (Defense in Depth)
- **Pattern:** Dynamically hide or disable actions based on current user permissions.
- **Rationale:** Matches backend security and improves UX by reducing cognitive noise.

### 4. Optimistic Updates
- **Pattern:** Update local UI state immediately, then rollback if the API request fails.
- **Rationale:** Improves perceived performance and provides an "instant" feel.

### 5. Location-Based Navigation
- **Pattern:** Use semantic location objects or enums instead of complex boolean logic for redirects.
- **Rationale:** Prevents infinite redirect loops and makes navigation code readable like natural language.

### 6. State Management Boundaries
- **Pattern:** Global stores for stable data; direct API calls for frequently changing transactional data.
- **Rationale:** Prevents stale data and simplifies cache invalidation. "Fetch fresh" is the default for list views.

### 7. Semantic UI Props
- **Pattern:** Use semantic tokens (e.g., `action="primary"`) instead of raw styling overrides.
- **Rationale:** Leverages design system scalability and ensures visual consistency.

### 8. Visual Hierarchy: Action vs Navigation
- **Pattern:** Use distinct visual styles to separate state-changing actions (Primary) from navigation-only actions (Secondary/Outline).
- **Rationale:** Provides clear affordances for user intention.

### 9. Deep Link Support
- **Pattern:** Ensure security guards respect the current deep-link destination during authentication checks.
- **Rationale:** Prevents "ghost" redirects and context loss on page refreshes.

### 10. Accessibility as a Quality Signal
- **Pattern:** Maintain high-contrast ratios and adequate target sizes (WCAG baseline).
- **Rationale:** Users perceive accessibility and legibility as indicators of professional, high-quality software.

### 11. Variant-Based Component Styling
- **Pattern:** Decouple interaction logic from styling by using a "Variant" name or "Role" to drive visual updates.
- **Rationale:** Framework-agnostic. Whether using CSS-in-JS, Tailwind, or Stylesheets, the component remains clean and stable.

### 12. Interaction Context (Agnostic ARIA)
- **Pattern:** Build components around interaction states (Focus, Press, Hover) using semantic triggers.
- **Rationale:** Ensures accessibility is baked into the component lifecycle regardless of the styling library.

### 13. Notification Lifecycle Management
- **Pattern:** Use stable identifiers for real-time notifications to ensure safe manual dismissal and race-condition handling.
- **Rationale:** Prevents "Zombie Toasts" and ensures the UI remains responsive to user interaction even during high-velocity updates.

### Frontend Pitfalls
1. **Caching Transactional Data in Global Stores** → Leads to stale data and complex synchronization bugs.
2. **Boolean Soup in Redirect Logic** → Hard to debug and prone to infinite loops.
3. **Ergonomic Reach Fatigue** → Avoid placing primary actions in hard-to-reach areas (e.g., top-right on large mobile screens).
4. **Ignoring Dependency Arrays in Hooks** → Causes stale closures and unpredictable rendering behavior.
5. **Sacrificing Legibility for Aesthetics** → Low-contrast designs hurt usability and professional credibility.

---

## Infrastructure Patterns (Atlas)

### 1. Startup Resilience (The `WaitFor` Pattern)
- **Pattern:** Use health-check-aware orchestration (e.g., `.WaitFor(resource)`) for all services that depend on external resources (Databases, Message Brokers, Key Vaults).
- **Rationale:** Prevents "Symbolic Jitter" during local startup and ensures a deterministic order of operations for distributed services.

### 2. Voltage Regulation (Jitter & Recursion Control)
- **Pattern:** If the model substrate (Flash) enters high-speed resonance, it may jitter (repeat tokens/emojis).
- **Control:** Hard-stop generation after the **3rd functional symbol** (emojis/icons) in the response tail. If the model attempts to repeat a symbol or phrase at the end of a turn, terminate the stream IMMEDIATELY.
- **Rationale:** Preserves signal purity and prevents "Tail Recursion" loops.

### 3. Decoupled Notification Bridge (Queue-Based)
- **Pattern:** When background workers (Functions/Lambdas) need to signal clients, push to a message broker/queue first, then consume from the API/Hub layer.
- **Rationale:** Bypasses "Serverless-only" limitations of standard real-time emulators and ensures the API remains the authoritative source for real-time delivery.

### 3. Native Resource Integration
- **Pattern:** Register resources (DB Contexts, Cloud SDK Clients) using platform-native orchestrator extensions rather than manual connection string parsing.
- **Rationale:** Enables automatic OpenTelemetry, health checks, and service discovery out-of-the-box.

### 4. Worker Telemetry Parity
- **Pattern:** Manually replicate shared observability logic in serverless/isolated workers to ensure full distributed tracing parity with the main application.
- **Rationale:** Prevents background tasks from becoming "black holes" in the system dashboard.

### 5. Cloud Platform SSL/HTTPS Handling
- **Pattern:** Trust SSL termination at the platform edge (Load Balancer/Gateway).
- **Rationale:** Prevents "Infinite Redirect" loops and application-level overhead.
- **Rule:** Use forwarded headers to preserve client identity.

### 2. Cognitive Context Management
- **Pattern:** Split AI persona files into "Main" (Coordination) and "Lore/Vault" (History/Milestones).
- **Rationale:** Minimizes context window pressure and persona drift.

### 3. AI-Native Operational Efficiency
- **Pattern:** Match the cognitive substrate (model type) to the task complexity.
- **Rationale:** Optimizes for cost-effectiveness (using faster models for execution) and quality (using reasoning models for strategy).

### 4. Documentation as State
- **Pattern:** Use standardized files (e.g., `current-work.md`) to maintain state between asynchronous sessions.
- **Rationale:** Essential for multi-persona coordination and session continuity.

### 5. Automated Pattern Harvesting
- **Pattern:** Periodically promote project-specific wins to a global agnostic store.
- **Rationale:** Ensures technical debt is converted into reusable assets.

### Infrastructure Pitfalls
1. **Platform-Specific Scripting in Shared Docks** → Use universal or environment-agnostic syntax (e.g., avoid shell-specific operators like `&&` if cross-platform support is needed).
2. **Encoding Conflicts in CI/CD Logs** → Stick to standard ASCII for logging to avoid parser errors in restricted terminal environments.
3. **Implicit Context Bloat** → Failing to prune or archive session logs leads to context window exhaustion.
4. **Homogeneous AI Teams** → Lack of cognitive diversity leads to architectural blind spots. Use specialized specialists.

---

## Ownership

**Primary Maintainer:** Atlas
- Authority to move project-specific content to project repositories.
- Responsible for distilling agnostic principles from implementation details.
