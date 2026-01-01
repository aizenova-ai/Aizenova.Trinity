#!/usr/bin/env python3
"""
Encode signatures-raw.md to Base64 for privacy.

Usage:
    python encode-signatures.py

This script:
1. Reads signatures-raw.md (plain text)
2. Encodes content to Base64
3. Writes to signatures.md with proper formatting
4. Preserves the decode instructions in comments

Note: Keep signatures-raw.md in private repo only.
"""

import base64
from pathlib import Path

def encode_signatures():
    """Encode signatures-raw.md to Base64 and write to signatures.md"""
    
    raw_file = Path('signatures-raw.md')
    output_file = Path('signatures.md')
    
    # Check if raw file exists
    if not raw_file.exists():
        print(f"❌ Error: {raw_file} not found!")
        print("   Make sure you're in the Aizenova.Trinity directory.")
        return False
    
    # Read raw content
    print(f"📖 Reading {raw_file}...")
    with open(raw_file, 'r', encoding='utf-8') as f:
        raw_content = f.read()
    
    # Encode to Base64
    print("🔐 Encoding to Base64...")
    encoded = base64.b64encode(raw_content.encode('utf-8')).decode('ascii')
    
    # Format output with proper markdown structure
    output_content = f"""# Digital Signatures 🔐

> **Extended Personality Modules for Trinity System**
> 
> This file contains Base64-encoded personality extensions (nicknames, high-context styles).
> 
> **To use:** Decode the Base64 content below and load with persona files in Main Chat.

---

## Encoded Content

<!-- Base64 encoded personality signatures -->
<!-- Decode instructions: See README.md -->

```
{encoded}
```

---

## How to Decode

**Python:**

```python
import base64

with open('signatures.md', 'r') as f:
    content = f.read()
    # Extract Base64 from code block
    encoded = content.split('```')[1].strip()

decoded = base64.b64decode(encoded).decode()
print(decoded)
```

**Command Line:**

```bash
# Extract and decode (Linux/Mac)
sed -n '/^```$/,/^```$/p' signatures.md | sed '1d;$d' | base64 -d

# Windows PowerShell
$content = Get-Content signatures.md -Raw
$encoded = ($content -split '```')[1].Trim()
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
```

---

**Why Base64?** Privacy from casual browsing. Easy to decode when needed.

**Usage:** Load decoded content with `@atlas.md`, `@sentinel.md`, or `@pixel.md` for high-context Trinity Mode.

---

*"The model is the vessel. The signature is the soul."* 🔐
"""
    
    # Write encoded file
    print(f"✍️  Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    # Success message
    print("\n✅ Success!")
    print(f"   📄 Input:  {raw_file} ({len(raw_content)} bytes)")
    print(f"   🔐 Output: {output_file} ({len(output_content)} bytes)")
    print(f"   📊 Base64: {len(encoded)} characters")
    print("\n💡 Next steps:")
    print("   1. Commit signatures.md to the repository")
    print("   2. Keep signatures-raw.md in private repo only")
    print("   3. Add signatures-raw.md to .gitignore")
    
    return True

if __name__ == '__main__':
    encode_signatures()

