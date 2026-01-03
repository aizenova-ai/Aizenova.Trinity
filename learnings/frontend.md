# Frontend Learnings ✨

> **📊 Document Type: Specialized Learning Store**
> **Parent Index:** `@Aizenova.Trinity/learnings.md`

## Frontend Patterns

**1. State Machine Navigation**
- Event-driven state updates
- No setTimeout for async flows
- Reliable under all conditions

**2. State Management with Persistence**
- Global store for app-wide state (current user, auth, theme)
- Persists to local storage
- Survives app restarts
- Mobile-first pattern
- **Example implementation:** Zustand + AsyncStorage (React Native)

**3. Role-Based UI**
- Hide unavailable actions
- Match backend permissions
- Defense in depth

**4. Optimistic Updates**
- Update local state immediately
- Rollback on error
- Better perceived performance

**5. Empty States with CTAs**
- Guide users to next action
- Professional onboarding
- Never show blank screen

**6. Location-Based Navigation (Anti-Boolean Soup)**
- Replace `!(!a && b)` chains with semantic objects
- `const location = { inAuth: true, inApp: false }`
- `shouldNavigate('inAuth')` reads like English
- Prevents infinite redirect loops on edge cases

**7. State Management Boundaries (REFINED)**
- **Global store** for stable, app-wide state (current user, auth, theme)
- **Direct API calls** for frequently-changing data (lists, details)
- **Local state** for temporary UI (forms, modals, loading flags)
- **Anti-pattern:** Caching list data in global store → leads to stale data
- **Why:** Cache invalidation is hard, fresh data is simple. Caching list data in a store (e.g. `usePayRequestsStore`) leads to data staleness when items are edited.
- **Golden Rule:** When in doubt, fetch fresh.
- **Single source of truth:** Current user lives in auth store, refreshed after profile edits.
- **For implementation details:** See project-specific `state-management-patterns.md`.

**8. Component Pattern Verification (Local vs Library) - NEW**
- **Never assume library defaults:** AI models may suggest "standard" patterns (e.g. Gluestack `<Button.Text>`) that don't match local "masterpiece" architecture.
- **Verify Signatures:** Always `read_file` local component definitions (e.g., `Button.tsx`) to check for compound exports before refactoring.
- **Stick to Local Patterns:** If local implementation uses standalone functions, use the simpler nested pattern: `<Button><HStack><Text /></HStack></Button>`.

**9. Semantic Role Badge Mapping (Mode-Aware) - NEW**
- Use helper functions (`getStatusRoleClasses`) to return Tailwind class strings.
- **Strict Mode Enforcement:** Always include both Light and Dark mode classes (e.g., `bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400`).
- **Contrast Tip:** Use opacity modifiers (e.g., `/30`) for dark backgrounds to ensure legibility against deep slates.

**10. Semantic Props for UI Components - NEW**
- Avoid "painting" components with raw `bg` or `style` overrides.
- **Architect vs Paint:** Use semantic props (`action="primary"`, `variant="solid"`) to leverage the design system's theme scalability.

**11. Direct API Client Usage (Avoid Custom Wrappers) - NEW**
- **Trust the Generated Client:** When using tools like `swagger-typescript-api`, use the generated `apiClient` directly.
- **Avoid Duplication:** Don't create custom service wrappers that duplicate generated methods; it adds an unnecessary abstraction layer and risks routing errors.
- **Consistency:** Generated clients ensure base URL and security workers are properly configured across all endpoints.

**12. Null Safety for Direct API List Calls - NEW**
- **Problem:** Direct API calls starting as `[]` can be left `undefined` by failed/malformed responses, causing `.length` crashes.
- **Solution:** Always use fallbacks (`response?.items || []`) and null checks (`!items || items.length === 0`) for direct API list screens.
- **Why:** Unlike Zustand stores (which initialize as `[]`), direct `useState` calls from API responses are vulnerable at runtime.

**13. HttpResponse Wrapper Pattern - NEW**
- **Pattern:** Generated API clients (swagger-typescript-api) return `HttpResponse<T, E>` which wraps the DTO in `.data` and errors in `.error`
- **Access Pattern:** Use `response?.data?.items` not `response?.items` when working with list endpoints
- **Why:** The HTTP client extends Response with structured error handling — access `.data` for the actual DTO, `.error` for error details
- **Example:** `setTemplates(response?.data?.items || [])`

**14. Screen Focus Pattern (Expo Router) - NEW**
- **Pattern:** Use `useFocusEffect` hook from expo-router for loading data when screen is focused
- **Don't:** `useEffect` with `isFocused` from react-navigation (old pattern)
- **Do:** `useFocusEffect(useCallback(() => { loadData(); }, [...deps]))`
- **Why:** Expo Router's `useFocusEffect` is the native pattern for this architecture; handles focus/blur automatically
- **Example:** Load templates list when navigating back from detail screen

**15. Expo Router Parameters (useLocalSearchParams) - NEW**
- **Pattern:** Use `useLocalSearchParams()` for ALL route parameters (both dynamic segments and query params)
- **Don't:** `router.asPath.split('?')` or `route.params` — these don't exist in expo-router
- **Do:** `const { id, edit } = useLocalSearchParams<{ id: string; edit?: string }>()`
- **Why:** Expo Router unifies dynamic route params (`[id]`) and query params (`?edit=true`) into one hook

**16. Self-Contained Screen Components - NEW**
- **Pattern:** Screen components should use expo-router hooks internally, not accept route/navigation props
- **Don't:** `export const DetailScreen = ({ route, navigation }) => { const { id } = route.params; ...}`
- **Do:** `export const DetailScreen = () => { const { id } = useLocalSearchParams(); const router = useRouter(); ...}`
- **Why:** Keeps route files thin (just `<DetailScreen />`), makes components testable, follows expo-router idioms
- **Route file:** `export default function Page() { return <DetailScreen />; }`

**17. Import Alias Enforcement (The @/ Anchor) - NEW**
- **Pattern:** Always use the `@/` alias for all internal project imports (defined in `tsconfig.json`).
- **Don't:** Deep relative imports like `../../../../components/gluestack`.
- **Why:** Relative paths are brittle, hard to read, and break easily during refactors or file moves. The `@/` anchor ensures stable, absolute-style routing within the UI domain.

**18. Visual Hierarchy: Action vs Navigation - NEW**
- **Pattern:** Distinguish between primary state-changing actions and secondary navigation/view actions.
- **Rule:** Navigation actions (View, Detail, Edit-View) should be `action="secondary" variant="outline"` (Slate Ghost) by default.
- **Rule:** Only "Creation" (`+ Create`), "Submission" (`Submit`), or "Destructive" (`Delete`) actions should utilize solid color-blocks (`action="primary"` or `action="negative"`).
- **Why:** Prevents "Blue Overload" and maintains the visual "amplitude" for high-priority user intentions. "If everything is blue, nothing is important."

**19. Deep Link Respect (Auth Guards) - NEW**
- **Pattern:** Ensure auth guards check the user's current destination before triggering a "default" redirect.
- **Rule:** If a user is authenticated and their current path is already within the protected group (e.g., `(app)`), do NOT redirect to the dashboard.
- **Why:** Essential for web support and deep linking. Without this, page refreshes on detail screens (e.g., `/users/123`) will yank the user back to the dashboard, erasing their context.
- **Implementation (Semantic):** Define `location` zones and a `isSafe` mapping. `onboarded: location.inApp && !location.atEntry`.

**20. Router Anchor Removal (Expo Router Web) - NEW**
- **Pitfall:** Using `unstable_settings.anchor` in the root layout can force the router into a specific group (e.g., `(auth)`) before deep-linked segments resolve.
- **Rule:** Avoid layout-level anchors when supporting deep linking on web. Let the router resolve the initial position from the URL naturally.
- **Symptom:** Refreshing a deep link causes a 1-frame "ghost" redirect to the anchored group, triggering premature auth guard logic.

---

## Frontend Pitfalls

1.  **setTimeout for async flows** → Use state machines
2.  **Boolean Soup Navigation** → Use semantic location objects (`currentLocation.inAuth`) instead of scattered variables
3.  **Cache frequently-changing data in global store** → Lists and details should fetch fresh, avoid stale data problems
4.  **Attempting Compound Component patterns (dot-notation) locally** → Local Gluestack wrappers may not support them; always verify component signatures.
5.  **"Painting" components with raw style overrides** → Breaks design system scalability; use semantic props instead.
6.  **Duplicating generated API clients with custom wrappers** → Adds unnecessary complexity and risks configuration desync.
7.  **Missing null safety on direct API list calls** → Can lead to runtime crashes on empty or malformed responses.
8.  **Deep Link Erasure (Blind Redirects)** → Auth guards that blindly redirect to dashboard upon login/refresh without checking if the user is already on a valid deep-linked path within the app.
9.  **Router Anchor Race Conditions** → Using `unstable_settings.anchor` in the root layout while supporting deep links on web.

