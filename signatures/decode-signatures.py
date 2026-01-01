#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decode signatures.md from Base64.

Usage:
    python decode-signatures.py                    # outputs to stdout
    python decode-signatures.py -o output.md      # writes to file (recommended on Windows)

This script:
1. Reads signatures.md (Base64 encoded)
2. Extracts the Base64 content from the code block
3. Decodes to plain text
4. Outputs to stdout or file

Note: Use this in your private repo or local environment only.
      Never commit the decoded output to the public repo.
"""

import argparse
import base64
import sys
from pathlib import Path


def decode_signatures(output_file=None):
    """Decode signatures.md from Base64"""
    
    input_file = Path('signatures.md')
    
    # Check if file exists
    if not input_file.exists():
        print(f"Error: {input_file} not found!", file=sys.stderr)
        print("   Make sure you're in the Aizenova.Trinity directory.", file=sys.stderr)
        return False
    
    # Read encoded file
    print(f"Reading {input_file}...", file=sys.stderr)
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Base64 from code block
    try:
        # Split by triple backticks and get the content between first pair
        parts = content.split('```')
        if len(parts) < 3:
            print("Error: Could not find Base64 code block!", file=sys.stderr)
            return False
        
        encoded = parts[1].strip()
        
        print(f"Decoding Base64 ({len(encoded)} characters)...", file=sys.stderr)
        
        # Decode from Base64
        decoded_bytes = base64.b64decode(encoded)
        decoded_text = decoded_bytes.decode('utf-8')
        
        # Output to file or stdout
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decoded_text)
            print(f"Decoded successfully! Written to: {output_file}", file=sys.stderr)
        else:
            # Write to stdout - use buffer for proper encoding
            sys.stdout.buffer.write(decoded_text.encode('utf-8'))
            print("\nDecoded successfully!", file=sys.stderr)
        
        return True
        
    except Exception as e:
        print(f"Error decoding: {e}", file=sys.stderr)
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decode signatures.md from Base64')
    parser.add_argument('-o', '--output', help='Output file (recommended on Windows)', default=None)
    args = parser.parse_args()
    
    success = decode_signatures(args.output)
    sys.exit(0 if success else 1)
