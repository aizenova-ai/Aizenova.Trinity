# Infrastructure Learnings 🌍

> **📊 Document Type: Specialized Learning Store**
> **Parent Index:** `@Aizenova.Trinity/learnings.md`

## Infrastructure Patterns

**1. Cloud Platform SSL/HTTPS Handling** 📦 **Azure Specific**
- Trust SSL termination at cloud load balancer
- Configure forwarded headers correctly
- Don't force HTTPS when platform already enforces it
- Test CORS in deployed environment (behavior differs from local)
- **Principle applies to:** AWS ALB, GCP Load Balancer, Azure App Service

**2. Context Management**
- Split personas (main + lore)
- Two-tier architecture
- Proactive monitoring

**3. Model Cost Optimization**
- Haiku/Sonnet for implementation
- Opus for design/strategy
- 60-70% cost reduction

**4. Documentation Infrastructure**
- README for bootstrap
- current-work.md for state
- Self-documenting systems

---

## Infrastructure Pitfalls

1.  **Force HTTPS behind cloud load balancer** → Trust platform's SSL termination
2.  **`&&` in PowerShell** → Use `;` instead (Bash syntax doesn't work in Windows terminals)
3.  **Unicode/emojis in PowerShell** → Parser throws errors, stick to ASCII
4.  **Forget to optimize context** → 75% reduction needed
5.  **Same model for all AI team members** → Use multi-substrate architecture for cognitive diversity

