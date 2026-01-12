---
applyTo: "backend/**, **/*.cs"
description: Architectural standards and implementation patterns for all backend development.
---
# Global Backend Instructions

These instructions govern the architectural standards and implementation patterns for all backend development in the Aizenova ecosystem.

## CRITICAL ARCHITECTURAL CONSTRAINTS

### 1. THE "NO DYNAMIC" PROTOCOL (Type Safety Absolute)
- **STRICT RULE:** Use of `dynamic`, `object` (as a catch-all), or `ExpandoObject` is strictly forbidden in business logic and DTOs.
- **RATIONALE:** AI models require strict type definitions to function without hallucination. Explicit types (C# records/classes) provide the "Gravity" that keeps AI-generated code safe and predictable.
- **CRITICAL PITFALL:** Avoid `Dictionary<string, object>`. Every field in a DTO must be explicitly typed.

### 2. XML DOCUMENTATION PROTOCOL
- **STRICT RULE:** Every public member (Classes, Interfaces, Methods, Properties, DTOs) MUST have XML comments (`/// <summary>`, etc.).
- **RATIONALE:** High-fidelity AI collaboration requires documented intent. Undocumented members lead to architectural drift and increased review latency.
- **ENFORCEMENT:** Do not submit code that generates `CS1591` warnings.

## PRIMARY PATTERNS

### 1. Semantic RBAC Scopes
- **Pattern:** Use clear suffixes (e.g., `-self`) to distinguish between personal and administrative/organizational permissions.
- **Why:** Eliminates ambiguity in scope names and provides a self-documenting security model.

### 2. Attribute-Driven Authorization
- **Pattern:** Use declarative attributes on controllers/actions that map to resource-based or action-based scopes.
- **Why:** Centralizes security logic and makes it "secure by default."

### 3. ORM Best Practices
- **Pattern:** Leverage automatic change tracking; avoid manual update calls on tracked entities. Explicitly configure complex or self-referencing relationships that ORMs may fail to infer.
- **UNIT OF WORK:** Command Handlers MUST perform all operations in memory and call `await SaveChangesAsync()` exactly ONCE at the end. Multiple saves per command are strictly forbidden.
- **Guid Determinism:** Manually assign Guid IDs upon instantiation. Do not call `SaveChangesAsync` just to retrieve a generated ID; this allows building complex object graphs atomically.
- **Why:** Ensures data integrity, atomicity, and minimizes side effects during persistence.

### 4. OpenAPI & Contract-Driven Development
- **Pattern:** Ensure all API responses include explicit type information in metadata. ALWAYS provide a unique `Name` property to Http attributes (e.g., `[HttpGet(Name = "GetX")]`).
- **Why:** Lock the Operation ID for stable client SDK generation and prevent metadata drift.

### 5. Strict Constructor Injection
- **Pattern:** ALWAYS use Constructor Injection for all dependencies. NEVER use Parameter Injection (passing infra types into interface methods).
- **Why:** Ensures managed dependencies and maintains high-integrity abstraction boundaries.

### 6. CQRS-Lite Segregation (Read-Only Paths)
- **Pattern:** Use a specific read-only abstraction for query handlers that omits mutation methods (Add/Update/Save).
- **Inheritance:** The primary data context interface should inherit from the read-only interface.
- **Why:** Enforces "Secure by Intent," prevents accidental writes in read paths, and allows for read replicas.

## ⚠️ BACKEND PITFALLS & REGRESSION PREVENTION
- **Routing vs. Database IDs:** Confusing Routing IDs (slugs) with Database IDs (GUIDs) causes query failures and collation mismatches.
- **Leaky Abstractions:** Passing implementation details through domain interfaces creates brittle, hard-to-test systems.
- **Transport-Owned Contracts:** Defining DTOs in the API layer makes them inaccessible to non-web consumers and leads to "Metadata Erosion."
- **Massive Sets:** Avoid expensive "Total Count" queries on large tables; use projections or caching.
