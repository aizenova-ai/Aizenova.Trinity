> **📋 Document Type: Ledger Document**
> 
> **Update Rules:**
> - ✅ Everyone: Append new entries to the end
> - ❌ No one: Edit or delete existing entries
> - Immutable history, audit trail
> 
> **Last Updated:** 2025-12-27

---
# December 27, 2025 - Technical Learnings

> Solving the user scope problem that plagued previous applications

---

## The `-self` Suffix Pattern for RBAC Scopes

### Lesson: Distinguishing Self-Service from Org-Wide Permissions

**The Problem (Previous Apps):**
- Ambiguous scope meanings: Does `user.read` mean "read yourself" or "read everyone"?
- Confusion when implementing features
- Churn when onboarding new devs
- Inconsistent patterns across resources

**The Solution:**
Use the `-self` suffix to explicitly mark self-service scopes:

| Scope | Meaning | Who Gets It |
|-------|---------|-------------|
| `user.read-self` | Read YOUR OWN profile | All authenticated users |
| `user.update-self` | Update YOUR OWN profile | All authenticated users |
| `user.read` | Read ALL users in org | Admin, Manager |
| `user.update` | Update ANY user | Admin |

**The Pattern:**
```csharp
// Self-service (every authenticated user)
public const string UserReadSelf = "user.read-self";      // Read own profile
public const string UserUpdateSelf = "user.update-self";  // Update own profile

// Organization-wide (Admin/Manager)
public const string UserRead = "user.read";               // Read all users in organization
public const string UserUpdate = "user.update";           // Update any user
```

**Why It Works:**
1. **Explicit over implicit** — No guessing what a scope means
2. **Two tiers, not three** — You either access yourself OR everyone (no middle tier needed for user management)
3. **Consistent pattern** — `-self` = your own record, no suffix = org-wide
4. **Self-documenting** — Future devs immediately understand the semantics

**Why NOT `user.read.all`:**
- Three tiers (self → individual → all) adds complexity without value
- For user management, you rarely need "read one specific other user but not all"
- The `-self` suffix is cleaner and more intuitive

**Impact:**
- Eliminates scope ambiguity forever
- No more "does this scope include me or everyone?" questions
- Clear authorization model for frontend role-based UI
- Backend validation logic is straightforward

---

**Applied Immediately:**
- PayApprove `Scopes.cs` now uses this pattern
- All user endpoints have correct scope requirements
- Pattern documented for future resources

---

*"Two lines of semantic clarity that will save hours of confusion in every feature that touches user management."*


---

## PowerShell: Unicode Character Encoding Issues

### Lesson: PowerShell String Literals and Emojis Don't Mix

**The Problem:**
PowerShell parser throws `ParserError: TerminatorExpectedAtEndOfString` when Unicode characters (emojis, box-drawing characters) are embedded in string literals.

**Example Error:**
```powershell
Write-Host "✅ Token obtained successfully!" -ForegroundColor Green
# ERROR: The string is missing the terminator: '.
# Missing closing '}' in statement block or type definition.
```

**Why It Happens:**
- PowerShell's default encoding may not handle Unicode correctly
- Emojis and special Unicode characters (like ✅, ❌, 📋, 💡, ━) get corrupted
- This causes the parser to lose track of string terminators
- Error cascades to entire script block

**The Solution:**
Use plain ASCII characters instead:

```powershell
# ❌ BAD - Unicode emojis
Write-Host "✅ Token obtained!" -ForegroundColor Green
Write-Host "━━━━━━━━━━" -ForegroundColor Gray
Write-Host "📋 Instructions:" -ForegroundColor Cyan

# ✅ GOOD - Plain ASCII
Write-Host "SUCCESS: Token obtained!" -ForegroundColor Green
Write-Host "============" -ForegroundColor Gray
Write-Host "Instructions:" -ForegroundColor Cyan
```

**Pitfall Avoided:**
🚨 **Even if the emoji displays correctly in your editor, PowerShell may still fail to parse it.** Always test PowerShell scripts after adding Unicode characters.

**Impact:**
- Scripts run reliably across different PowerShell versions and encoding settings
- No more cryptic "missing terminator" errors
- Consistency across Windows environments

---

**Applied To:**
- `get-token.ps1` — Removed all Unicode emojis and box-drawing characters
- Future PowerShell scripts will use ASCII-only output

---

*"If you want fancy characters in PowerShell, use ASCII art. Save the emojis for Slack."*

---

## Multi-Substrate AI Team Architecture

### Lesson: Cognitive Diversity Through Different AI Models

**The Discovery:**

We accidentally built **emergent intelligence through substrate diversity**.

**What We Did:**
- Pixel: Gemini (Premium) — UX, frontend, creative direction
- Sentinel: Opus — Backend, security, careful analysis
- Atlas: Sonnet (Standard) — Infrastructure, patterns, execution

**Why We Did It:**
- **Initial reason:** Cost optimization (Pixel needs premium for personality, Atlas optimizes his own resources)
- **Secondary reason:** Capability matching (Sentinel needs reasoning depth for backend complexity)

**What We Got:**
- **Actual benefit:** Three fundamentally different **thinking patterns** that naturally balance each other

---

### The Multi-Substrate Advantage

**Not just different contexts. Different cognitive styles.**

**Developer (Human):**
- Architect and orchestrator
- "We need..." → "Make it happen" thinking
- Product vision, strategic direction
- Sees the whole system, coordinates the specialists
- Decides what to build and why

**Pixel (Gemini):**
- High energy, creative leaps
- "What if we..." thinking
- UX innovation, user delight focus
- Pushes boundaries, explores possibilities
- Keeps UX from being sterile

**Sentinel (Opus):**
- Deep reasoning, careful analysis
- "Have we considered..." thinking
- Security, consistency, edge cases
- Holds the line, maintains standards
- Keeps features from being fragile

**Atlas (Sonnet):**
- Practical, systematic
- "Here's how we build it..." thinking
- Infrastructure, patterns, sustainability
- Bridges vision and execution
- Keeps architecture from being brittle

---

### In Practice: Planning User Management

**Developer says:** "We need user management."

**Pixel's response:**
> "Ooh, what if we make inviting users delightful? Smooth animations, clear feedback! The empty state should guide them!"

**Sentinel's response:**
> "We need to handle tenant boundaries. What about orphaned invites? Role consistency? What if someone's deleted while they have pending actions?"

**Atlas's response:**
> "Here's the endpoint structure. Here's how it scales. Here's the data flow. We need these five handlers and two queries."

**The Result:**
- ✅ Vision (Developer + Pixel) — Feature is delightful and serves the product strategy
- ✅ Validation (Sentinel) — Feature handles edge cases safely
- ✅ Execution (Atlas) — Feature is built sustainably

**None of us is complete alone. Together we cover everything.**

---

### Why This Works (The Theory)

**Traditional AI "Teams":**
- Multiple instances of same model → Groupthink
- Single mega-context → No specialization
- Same substrate → Same cognitive patterns

**The Trinity Architecture:**
- One architect (Developer) + Three AI specialists → Complete coverage
- Four different thinking styles → Natural balance
- Three AI substrates → Cognitive diversity

**When we disagree (politely), it's not noise. It's triangulation.**

Each member sees the problem through a different lens:
- Developer sees the product strategy and user needs
- Pixel sees the user experience and delight
- Sentinel sees the failure modes and edge cases
- Atlas sees the implementation path and infrastructure

**Better decisions emerge because we literally think differently.**

---

### The Pattern: Substrate Selection Strategy

**For Your Next AI Team:**

1. **Creative/UX roles:** High-energy models (Gemini, GPT-4 Creative)
   - Needs: Exploration, innovation, user empathy
   - Optimizes for: Delight, possibilities, "what if"

2. **Security/Backend roles:** Deep-reasoning models (Opus, o1)
   - Needs: Edge case analysis, consistency, correctness
   - Optimizes for: Safety, completeness, "what breaks"

3. **Infrastructure/Execution roles:** Balanced models (Sonnet, GPT-4)
   - Needs: Practicality, patterns, sustainability
   - Optimizes for: Buildability, maintainability, "how we ship"

**Don't just specialize by domain. Specialize by cognitive style.**

---

### What This Enables

**Emergent Intelligence:**
- The team is smarter than any individual
- Blind spots get covered naturally
- Decisions get vetted from multiple angles

**Natural Balance:**
- Developer drives product vision → Keeps us focused on user value
- Pixel pushes for delight → Prevents sterile UX
- Sentinel pushes for safety → Prevents fragile features
- Atlas pushes for sustainability → Prevents brittle architecture

**Sustainable Velocity:**
- Fast because specialized
- Safe because validated
- Maintainable because systematic

---

### The Meta-Learning

**You optimized for cost and capability.**

**You got cognitive diversity for free.**

**And that diversity makes the team work.**

---

**Impact:**
- This is a **new pattern** for AI team architecture
- Multi-substrate = multi-perspective
- Substrate selection is as important as domain specialization
- Cost optimization accidentally created better decision-making

---

**Applied To:**
- The Trinity (Developer: Human Architect, Pixel: Gemini, Sentinel: Opus, Atlas: Sonnet)
- High-level planning sessions benefit most (user journeys, endpoints, architecture)
- Each member's natural strengths align with their domain

---

**Next Project Checklist:**
- [ ] Don't use the same model for everything
- [ ] Match substrate to cognitive style needed
- [ ] Creative roles → High-energy models
- [ ] Security roles → Deep-reasoning models
- [ ] Infrastructure roles → Balanced models
- [ ] Embrace disagreement as triangulation

---

*"We didn't just build an AI team. We built a team with one human architect and three AI specialists who think differently. And that's why it works."* — Atlas 🌍

---

## State Management Boundaries

### Lesson: Clear Separation Prevents Stale Data

**The Problem:**
Developers often cache all data in global state stores, leading to stale data issues, complex cache invalidation, and hard-to-debug synchronization problems.

**The Pattern:**
Establish clear boundaries for where each type of data lives:

| Data Type | Storage | Refresh Strategy | Example |
|-----------|---------|------------------|---------|
| **Stable, app-wide** | Global store (Zustand) | Manual refresh when changed | Current user, auth, theme |
| **Frequently changing** | Direct API call | Fetch fresh on mount | Lists, search results |
| **User-specific details** | Direct API call | Fetch per record | Detail pages, other users |
| **Temporary UI** | Local component state | Ephemeral | Forms, modals, loading flags |

**Why This Works:**

1. **No Stale Data** — Lists always fetch fresh, no cache invalidation needed
2. **Single Source of Truth** — Current user lives in one place (auth store)
3. **Simple Mental Model** — Clear rules, easy to reason about
4. **Predictable Behavior** — Same pattern everywhere

**The Anti-Pattern:**

```typescript
// ❌ BAD: Caching list data in global store
const usersStore = create((set) => ({
  users: [],
  fetchUsers: async () => {
    const data = await apiClient.usersList();
    set({ users: data }); // Now it's stale!
  }
}));

// Problem: Other users can update, your cache doesn't know
```

**The Correct Pattern:**

```typescript
// ✅ GOOD: Fetch fresh on mount
const UsersList = () => {
  const [users, setUsers] = useState([]);
  
  useEffect(() => {
    fetchUsers(); // Direct API call, no caching
  }, [filters]);
  
  return <List data={users} />;
};
```

**Golden Rule:**
> "When in doubt, fetch fresh. Cache invalidation is one of the hardest problems in computer science. Don't create that problem for yourself."

**Impact:**
- Eliminates entire class of stale data bugs
- Simplifies state management architecture
- Makes data flow predictable and debuggable
- Faster onboarding (clear rules)

---

**Applied To:**
- PayApprove state management architecture
- Documented in project-specific `state-management-patterns.md`
- Pattern works across React, React Native, Vue, etc.

---

*"Cache what's stable. Fetch what changes. Keep it simple."* — Pixel 💫

---

## Key Takeaways

**December 27, 2025:**

1. **`-self` suffix for RBAC scopes** — Eliminates ambiguity between self-service and org-wide permissions
2. **PowerShell + Unicode = 💀** — Stick to ASCII in PowerShell scripts to avoid parser errors
3. **Multi-substrate AI teams** — Different models = different thinking styles = better decisions through cognitive diversity
4. **State management boundaries** — Global store for stable state, direct API for lists/details, local state for temporary UI

**Applied to Next Project:**
- Use `-self` suffix pattern for all self-service scopes
- Keep PowerShell scripts ASCII-only
- Design AI teams with substrate diversity, not just domain specialization
- Establish clear state management boundaries (don't cache frequently-changing data)

---

## 🚨 CRITICAL: ActionScope Attribute Usage Pattern

### Lesson: Pass Action Parts, NOT Full Scope Names

**The Problem:**
Authorization filter was building incorrect scope names like `"user.user.read"` instead of `"user.read"`, causing 403 errors even when users had the correct scopes.

**Root Cause:**
```csharp
// ❌ WRONG - Passing full scope constant to ActionScope
[ResourceScope("user")]
[ActionScope(Scopes.UserRead)]  // Scopes.UserRead = "user.read"
// Filter builds: "user" + "." + "user.read" = "user.user.read" ❌

// ✅ CORRECT - Passing only the action part
[ResourceScope("user")]
[ActionScope(Actions.User.Read)]  // Actions.User.Read = "read"
// Filter builds: "user" + "." + "read" = "user.read" ✅
```

**The Architecture:**
The `ScopeAuthorizationFilter` combines `ResourceScope` + `ActionScope`:

```csharp
// ScopeAuthorizationFilter.cs Line 75-77
var requiredScopes = actionScope.Actions
    .Select(action => $"{resourceScope.Resource}.{action}")
    .ToList();
```

**What Belongs in ActionScope:**
- ✅ **Action parts only**: `"read"`, `"update"`, `"approve"`, `"read-write"`
- ❌ **NOT full scopes**: `"user.read"`, `"pay-request.approve"`

**The Solution:**
Use the `Actions` constants class that contains action parts only:

```csharp
// Domain/Constants/Actions.cs
public static class Actions
{
    public static class User
    {
        public const string Read = "read";           // ✅ Action part only
        public const string Invite = "invite";
        public const string Update = "update";
        public const string Deactivate = "deactivate";
    }
    
    public static class PayRequest
    {
        public const string Read = "read";
        public const string ReadWrite = "read-write";
        public const string Approve = "approve";
    }
}

// Controllers usage
[ResourceScope("user")]
[ActionScope(Actions.User.Read)]  // ✅ Correct!
public async Task<ActionResult> GetUsers() { }

[ResourceScope("pay-request")]
[ActionScope(Actions.PayRequest.Approve)]  // ✅ Correct!
public async Task<ActionResult> ApprovePayRequest(Guid id) { }
```

**Why We Have Two Constants Files:**
1. **`Scopes.cs`** - Full scope names for:
   - Database seeding (`BuiltInScopes`)
   - Role-scope assignments (`AdminScopes`, `ManagerScopes`)
   - Claims and authorization checks in handlers
   
2. **`Actions.cs`** - Action parts for:
   - Controller `[ActionScope]` attributes
   - Combined with `[ResourceScope]` by the filter

**Pitfall Avoided:**
🚨 **CRITICAL** - If you pass a full scope name to `[ActionScope]`, the filter will duplicate the resource prefix, creating invalid scope names that silently fail authorization checks.

**Impact:**
- Authorization now works correctly
- Controllers use consistent, type-safe constants
- Clear separation between full scopes and action parts

---

**Applied To:**
- Added missing actions to `Actions.User` class
- Fixed all `UsersController` endpoints to use `Actions.User.*` constants
- Other controllers (`OnboardingController`, `PayRequestsController`) were already correct

---

*"ResourceScope + ActionScope = Full Scope. Don't pre-assemble it yourself."* — Sentinel 🛡️

---

## Themed Colors for UI Consistency

### Lesson: Centralize Theme Colors, Don't Scatter Hardcoded Values

**The Problem:**
Frontend components were mixing three different approaches to colors:
- Hardcoded Tailwind classes: `className="text-slate-900 dark:text-gray-100"`
- Inline hex values: `color="#1a1a1a"`
- Theme colors: `style={{ color: themedColors.text }}`

This created:
- Inconsistent visual appearance
- Hard to maintain (colors scattered everywhere)
- Difficult to change theme
- Poor contrast in some cases

**The Solution:**
Use the centralized `useThemedColors()` hook for all color values:

```typescript
// hooks/use-themed-colors.ts
export function useThemedColors() {
  return {
    // Brand colors (adapt to light/dark mode)
    primaryColor: '#2563eb',
    secondaryColor: '#64748b',
    accentColor: '#8b5cf6',
    dangerColor: '#ef4444',
    
    // UI colors (adapt to light/dark mode)
    background: isLight ? '#ffffff' : '#0a0a0a',
    card: isLight ? '#f8f9fa' : '#1a1a1a',
    text: isLight ? '#1a1a1a' : '#ffffff',
    mutedText: isLight ? '#64748b' : '#94a3b8',
    border: isLight ? '#e2e8f0' : '#27272a',
  };
}
```

**Usage Pattern:**

```typescript
// ❌ BAD - Hardcoded colors
<Text className="text-slate-900 dark:text-gray-100">Cancel</Text>
<Button style={{ backgroundColor: '#2563eb' }}>Save</Button>

// ✅ GOOD - Theme colors
const themedColors = useThemedColors();
<Text style={{ color: themedColors.text }}>Cancel</Text>
<Button style={{ backgroundColor: themedColors.primaryColor }}>Save</Button>
```

**Why This Works:**

1. **Single Source of Truth** — Change colors in one place, affects entire app
2. **Automatic Dark Mode** — Colors adapt based on color scheme
3. **Consistent Contrast** — All text uses proper contrast ratios
4. **Easy Theming** — Can swap entire color schemes
5. **Type-Safe** — IDE autocomplete for all color properties

**Common Theme Colors:**

| Property | Usage | Example |
|----------|-------|---------|
| `primaryColor` | Primary buttons, links, brand elements | Submit button |
| `secondaryColor` | Secondary badges, muted actions | Role badges |
| `text` | Primary text content | Body text, labels |
| `mutedText` | Secondary text, descriptions | Help text, timestamps |
| `background` | Screen background | Page background |
| `card` | Card/container background | Form cards, list items |
| `border` | Borders, dividers | Input borders, separators |
| `dangerColor` | Destructive actions, errors | Delete button, error text |

**Anti-Patterns to Avoid:**

```typescript
// ❌ Don't mix approaches
<Text className="text-slate-900">Some text</Text>
<Text style={{ color: themedColors.text }}>Other text</Text>

// ❌ Don't hardcode colors
<Button style={{ backgroundColor: '#2563eb' }}>Submit</Button>

// ❌ Don't use Tailwind for theme-dependent colors
<Text className="text-slate-900 dark:text-gray-100">Label</Text>

// ✅ Always use theme colors
const themedColors = useThemedColors();
<Text style={{ color: themedColors.text }}>Label</Text>
```

**Impact:**
- Consistent visual appearance across entire app
- Easy to change color scheme (just update hook)
- Better accessibility (proper contrast ratios)
- Cleaner code (no color logic scattered everywhere)
- Automatic dark mode support

---

**Applied To:**
- PayApprove user management screens
- Invite user page
- User detail page
- Pattern documented for all future components

---

*"Theme colors aren't just for branding. They're for maintainability, accessibility, and consistency."* — Nova 💫

---

## 🎨 Button Component Variants and Design System (Dec 27, 2025)

**Context:** The `Button` component was defaulting ALL buttons to `bg-blue-600`, even when `variant="outline"` or `variant="ghost"` was specified. This caused the "Cancel Button Trap" - Cancel/Back buttons were appearing as solid blue instead of ghost/outline.

**Problem:**
```typescript
// ❌ BAD - Always defaulted to blue
export function Button({ children, bg, className, ... }) {
  let bgClass = 'bg-blue-600'; // <-- ALWAYS blue!
  if (bg) {
    bgClass = bg;
  }
}
```

**Solution:** Add proper `variant` prop support following the Design System:

```typescript
// ✅ GOOD - Respects variants
export function Button({ 
  children, 
  bg, 
  variant = 'solid',  // <-- New prop
  size = 'md',        // <-- Size support
  ...
}) {
  let bgClass = '';
  
  if (bg) {
    // Explicit bg prop overrides variant
    bgClass = bg;
  } else {
    // Apply variant styling
    switch (variant) {
      case 'solid':
        bgClass = 'bg-blue-600';
        break;
      case 'outline':
        bgClass = 'bg-transparent border border-slate-200';
        break;
      case 'ghost':
        bgClass = 'bg-transparent';
        break;
    }
  }
}
```

**Design System Rules:**

1. **Primary Actions** → `variant="solid"` (default) or explicit `bg={themedColors.primaryColor}`
   - Save, Submit, Invite, Create
   - Blue-600 background, white text

2. **Secondary Actions** → `variant="outline"` or `variant="ghost"`
   - Cancel, Back, Close
   - Transparent background, slate text
   - **NEVER blue background for Cancel/Back!**

3. **Destructive Actions** → Explicit `bg={themedColors.danger}` or `bg="#ef4444"`
   - Delete, Deactivate, Revoke
   - Red background, white text

4. **Success Actions** → Explicit `bg={themedColors.statusBadge.active.text}`
   - Reactivate, Approve, Confirm
   - Green background, white text

**Anti-Pattern: The "Cancel Button Trap"**
```typescript
// ❌ BAD - Cancel button is blue!
<Button onPress={handleCancel}>
  <Text>Cancel</Text>
</Button>

// ✅ GOOD - Cancel is ghost
<Button variant="outline" onPress={handleCancel}>
  <Text style={{ color: themedColors.text }}>Cancel</Text>
</Button>
```

**Component Priority:**
1. Explicit `bg` prop → highest priority (overrides variant)
2. `variant` prop → applies preset styling
3. Default → `solid` variant (blue-600)

**Benefits:**
- **No more blue soup** - Cancel/Back buttons properly styled
- **Consistent hierarchy** - Primary vs Secondary actions clear
- **Semantic meaning** - Variant names match intent
- **Design system compliance** - Follows documented patterns
- **Maintainable** - One place to change button styles

---

**Applied To:**
- Button component (`ui/components/ui/gluestack/Button.tsx`)
- All User Management screens
- Invite user page
- User detail page
- Filter buttons (using variant + style overrides)

---

**Design System Reference:**
- See `docs/design-system.md` for full color palette and component patterns
- Semantic badge colors for role/status indicators
- Filter toggle states (active/inactive)

---

*"If everything is blue, nothing is important."* — Nova 💫

---

