---
applyTo: "ui/**, **/*.tsx, **/*.ts"
description: Architectural standards and implementation patterns for all frontend development.
---
# Global Frontend Instructions

These instructions govern the architectural standards and implementation patterns for all frontend development in the Aizenova ecosystem.

## CRITICAL ARCHITECTURAL CONSTRAINTS

### 1. THE "NO ANY" PROTOCOL (Strict Engineering Integrity)
- **STRICT RULE:** Use of `any` or casting to `any` is a critical failure. All TypeScript must be strictly typed.
- **RATIONALE:** In an AI-driven workflow, `any` allows the model to "hallucinate" properties that don't exist, leading to 100% avoidable production crashes.
- **TVA PATTERN:** Use `VariantProps<typeof style>` or proper generics for UI library props.

## PRIMARY PATTERNS

### 1. Architectural Pillars
- **Standalone Components:** Use standalone function exports instead of library compound defaults.
- **TanStack Query V5:** Use **Strict Object Syntax** for all hooks (`useMutation`, `useQuery`, `invalidateQueries`). Positional arguments are forbidden and cause runtime failures.
- **Form Power Tuple:** Use React Hook Form (RHF) + Zod with appropriate resolvers for type-safe validation.

### 2. State Management Boundaries
- **Pattern:** Use global stores for stable app-wide data (session, theme); use direct API calls or specialized cache (TanStack Query) for transactional data.
- **Why:** Prevents stale data and simplifies cache invalidation. "Fetch fresh" is the default for list views.

### 2. Role-Based UI (Defense in Depth)
- **Pattern:** Dynamically hide or disable actions based on current user permissions.
- **Why:** Matches backend security and improves UX by reducing cognitive noise.

### 3. Optimistic Updates
- **Pattern:** Update local UI state immediately, then rollback if the API request fails.
- **Why:** Improves perceived performance and provides an "instant" feel.

### 4. Deep Link Support
- **Pattern:** Ensure security guards and navigation logic respect the current deep-link destination during authentication checks.
- **Why:** Prevents "ghost" redirects and context loss on page refreshes.

### 5. Accessibility as a Quality Signal
- **Pattern:** Maintain high-contrast ratios and adequate target sizes (WCAG baseline).
- **Why:** Users perceive accessibility and legibility as indicators of professional, high-quality software.

### 6. Variant-Based Component Styling
- **Pattern:** Decouple interaction logic from styling by using a "Variant" name or "Role" to drive visual updates.
- **Why:** Framework-agnostic stability. Keeps the interaction logic clean and stable regardless of styling changes.

## ⚠️ FRONTEND PITFALLS & REGRESSION PREVENTION
- **Transactional Caching:** Caching transactional data in global stores leads to stale data and complex synchronization bugs.
- **Boolean Soup:** Using complex boolean logic for redirects is hard to debug and prone to infinite loops. Use semantic location objects or enums.
- **Ergonomic reach:** Avoid placing primary actions in hard-to-reach areas (e.g., top-right on large mobile screens).
- **Dependency Arrays:** Ignoring dependency arrays in hooks causes stale closures and unpredictable rendering behavior.
- **Legibility vs. Aesthetics:** Never sacrifice legibility for aesthetics. Low-contrast designs hurt usability and professional credibility.
