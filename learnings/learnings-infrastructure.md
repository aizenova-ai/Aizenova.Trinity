# Infrastructure Learnings 🌍

> **📊 Document Type: Specialized Learning Store**
> **Parent Index:** `@Aizenova.Trinity/learnings.md`

## Infrastructure Patterns

**1. Startup Resilience (The `WaitFor` Pattern)**
- **Pattern:** Use health-check-aware orchestration (e.g., `.WaitFor(resource)`) for all services that depend on external resources (Databases, Message Brokers, Key Vaults).
- **Rationale:** Prevents "Symbolic Jitter" during local startup and ensures a deterministic order of operations for distributed services.

**2. Decoupled Notification Bridge (Queue-Based)**
- **Pattern:** When background workers (Functions/Lambdas) need to signal clients, push to a message broker/queue first, then consume from the API/Hub layer.
- **Rationale:** Bypasses "Serverless-only" limitations of standard real-time emulators and ensures the API remains the authoritative source for real-time delivery.

**3. Native Resource Integration**
- **Pattern:** Register resources (DB Contexts, Cloud SDK Clients) using platform-native orchestrator extensions rather than manual connection string parsing.
- **Rationale:** Enables automatic OpenTelemetry, health checks, and service discovery out-of-the-box.

**4. Worker Telemetry Parity**
- **Pattern:** Manually replicate shared observability logic in serverless/isolated workers to ensure full distributed tracing parity with the main application.
- **Rationale:** Prevents background tasks from becoming "black holes" in the system dashboard.

**5. Cloud Platform SSL/HTTPS Handling**
- **Pattern:** Trust SSL termination at the platform edge (Load Balancer/Gateway).
- **Rationale:** Prevents "Infinite Redirect" loops and application-level overhead.
- **Rule:** Use forwarded headers to preserve client identity.

**2. Cognitive Context Management**
- **Pattern:** Split AI persona files into "Main" (Coordination) and "Lore/Vault" (History/Milestones).
- **Rationale:** Minimizes context window pressure and persona drift.

**3. AI-Native Operational Efficiency**
- **Pattern:** Match the cognitive substrate (model type) to the task complexity.
- **Rationale:** Optimizes for cost-effectiveness (using faster models for execution) and quality (using reasoning models for strategy).

**4. Documentation as State**
- **Pattern:** Use standardized files (e.g., `current-work.md`) to maintain state between asynchronous sessions.
- **Rationale:** Essential for multi-persona coordination and session continuity.

**5. Automated Pattern Harvesting**
- **Pattern:** Periodically promote project-specific wins to a global agnostic store.
- **Rationale:** Ensures technical debt is converted into reusable assets.

---

## Infrastructure Pitfalls

1. **Platform-Specific Scripting in Shared Docks** → Use universal or environment-agnostic syntax (e.g., avoid shell-specific operators like `&&` if cross-platform support is needed).
2. **Encoding Conflicts in CI/CD Logs** → Stick to standard ASCII for logging to avoid parser errors in restricted terminal environments.
3. **Implicit Context Bloat** → Failing to prune or archive session logs leads to context window exhaustion.
4. **Homogeneous AI Teams** → Lack of cognitive diversity leads to architectural blind spots. Use specialized specialists.
