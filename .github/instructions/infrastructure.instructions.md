---
applyTo: "infrastructure/**, **/*.yml, **/*.json"
description: Architectural standards and implementation patterns for all infrastructure and DevOps orchestration.
---
# Global Infrastructure Instructions

These instructions govern the architectural standards and implementation patterns for all infrastructure and DevOps orchestration in the Aizenova ecosystem.

## PRIMARY PATTERNS

### 1. Startup Resilience (The `WaitFor` Pattern)
- **Pattern:** Use health-check-aware orchestration (e.g., `.WaitFor(resource)`) for all services that depend on external resources (Databases, Message Brokers, Key Vaults).
- **Why:** Prevents "Symbolic Jitter" during local startup and ensures a deterministic order of operations for distributed services.

### 2. Native Resource Integration
- **Pattern:** Register resources (DB Contexts, Cloud SDK Clients) using platform-native orchestrator extensions rather than manual connection string parsing.
- **Why:** Enables automatic OpenTelemetry, health checks, and service discovery out-of-the-box.

### 3. Worker Telemetry Parity
- **Pattern:** Manually replicate shared observability logic in serverless/isolated workers to ensure full distributed tracing parity with the main application.
- **Why:** Prevents background tasks from becoming "black holes" in the system dashboard.

### 4. Decoupled Notification Bridge (Queue-Based)
- **Pattern:** When background workers (Functions/Lambdas) need to signal clients, push to a message broker/queue first, then consume from the API/Hub layer.
- **Why:** Bypasses "Serverless-only" limitations of standard real-time emulators and ensures the API remains the authoritative source for real-time delivery.

### 5. Cloud Platform SSL/HTTPS Handling
- **Pattern:** Trust SSL termination at the platform edge (Load Balancer/Gateway). Use forwarded headers to preserve client identity.
- **Why:** Prevents "Infinite Redirect" loops and application-level overhead.

### 6. Cognitive Context Management
- **Pattern:** Split AI persona files into "Main" (Coordination) and "Lore/Vault" (History/Milestones). Match the cognitive substrate (model type) to the task complexity.
- **Why:** Minimizes context window pressure and persona drift. Optimizes for cost-effectiveness and quality.

## OPERATIONAL PRINCIPLES
- **Infrastructure is code:** Version controlled, reviewed, tested.
- **Automate everything:** Manual steps become pipelines.
- **Fail fast, recover faster:** Detect early, rollback quickly.
- **Monitor everything:** Can't improve what you don't measure.

## ⚠️ INFRASTRUCTURE PITFALLS & REGRESSION PREVENTION
- **Platform-Specific Scripts:** Avoid shell-specific operators (like `&&`) in shared docks if cross-platform support is needed.
- **Encoding Conflicts:** Use standard ASCII for CI/CD logging to avoid parser errors in restricted terminal environments.
- **Context Bloat:** Failing to prune or archive session logs leads to context window exhaustion.
- **Homogeneous Teams:** Lack of cognitive diversity leads to architectural blind spots. Use specialized specialists.
