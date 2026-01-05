# Infrastructure Learnings 🌍

> **📊 Document Type: Specialized Learning Store**
> **Parent Index:** `@Aizenova.Trinity/learnings.md`

## Infrastructure Patterns

**1. Cloud Platform SSL/HTTPS Handling**
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
