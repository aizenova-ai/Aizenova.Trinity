# Frontend Learnings ✨

> **📊 Document Type: Specialized Learning Store**
> **Parent Index:** `@Aizenova.Trinity/learnings.md`

## Frontend Patterns

**0. THE "NO ANY" PROTOCOL (Strict Engineering Integrity)**
- **Pattern:** Use of `any` or casting to `any` is a critical architectural failure.
- **Rationale:** AI-driven development requires strict type boundaries. `any` allows the model to "hallucinate" properties, leading to avoidable runtime crashes.
- **TVA Standard:** Use `VariantProps<typeof style>` or proper generics for UI library props.

**1. State Machine Navigation**
- **Pattern:** Use event-driven state updates for complex navigation flows.
- **Rationale:** More reliable than manual delays or implicit sequencing.

**2. State Management Persistence**
- **Pattern:** Persist global app-wide state (user session, theme) to local storage.
- **Rationale:** Essential for mobile-first experiences and surviving application restarts.

**3. Role-Based UI (Defense in Depth)**
- **Pattern:** Dynamically hide or disable actions based on current user permissions.
- **Rationale:** Matches backend security and improves UX by reducing cognitive noise.

**4. Optimistic Updates**
- **Pattern:** Update local UI state immediately, then rollback if the API request fails.
- **Rationale:** Improves perceived performance and provides an "instant" feel.

**5. Location-Based Navigation**
- **Pattern:** Use semantic location objects or enums instead of complex boolean logic for redirects.
- **Rationale:** Prevents infinite redirect loops and makes navigation code readable like natural language.

**6. State Management Boundaries**
- **Pattern:** Global stores for stable data; direct API calls for frequently changing transactional data.
- **Rationale:** Prevents stale data and simplifies cache invalidation. "Fetch fresh" is the default for list views.

**7. Semantic UI Props**
- **Pattern:** Use semantic tokens (e.g., `action="primary"`) instead of raw styling overrides.
- **Rationale:** Leverages design system scalability and ensures visual consistency.

**8. Visual Hierarchy: Action vs Navigation**
- **Pattern:** Use distinct visual styles to separate state-changing actions (Primary) from navigation-only actions (Secondary/Outline).
- **Rationale:** Provides clear affordances for user intention.

**9. Deep Link Support**
- **Pattern:** Ensure security guards respect the current deep-link destination during authentication checks.
- **Rationale:** Prevents "ghost" redirects and context loss on page refreshes.

**10. Accessibility as a Quality Signal**
- **Pattern:** Maintain high-contrast ratios and adequate target sizes (WCAG baseline).
- **Rationale:** Users perceive accessibility and legibility as indicators of professional, high-quality software.

**11. Variant-Based Component Styling**
- **Pattern:** Decouple interaction logic from styling by using a "Variant" name or "Role" to drive visual updates.
- **Rationale:** Framework-agnostic. Whether using CSS-in-JS, Tailwind, or Stylesheets, the component remains clean and stable.

**12. Interaction Context (Agnostic ARIA)**
- **Pattern:** Build components around interaction states (Focus, Press, Hover) using semantic triggers.
- **Rationale:** Ensures accessibility is baked into the component lifecycle regardless of the styling library.

**13. Notification Lifecycle Management**
- **Pattern:** Use stable identifiers for real-time notifications to ensure safe manual dismissal and race-condition handling.
- **Rationale:** Prevents "Zombie Toasts" and ensures the UI remains responsive to user interaction even during high-velocity updates.

---

## Frontend Pitfalls

1. **Caching Transactional Data in Global Stores** → Leads to stale data and complex synchronization bugs.
2. **Boolean Soup in Redirect Logic** → Hard to debug and prone to infinite loops.
3. **Ergonomic Reach Fatigue** → Avoid placing primary actions in hard-to-reach areas (e.g., top-right on large mobile screens).
4. **Ignoring Dependency Arrays in Hooks** → Causes stale closures and unpredictable rendering behavior.
5. **Sacrificing Legibility for Aesthetics** → Low-contrast designs hurt usability and professional credibility.
