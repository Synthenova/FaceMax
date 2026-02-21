#!/usr/bin/env python3
"""
ELL Indexer — Stage 3 of the Eternal Learning Loop.

Takes a newly created AKM markdown file and registers it in the CLAUDE.md
knowledge index so the agent immediately gains awareness of the new content.

Usage:
    python scripts/indexer.py <filename> <category>

Example:
    python scripts/indexer.py neck-wall-press.md 02-neck-and-posture
"""

import os
import re
import sys


def indexer_update(filename: str, target_category: str) -> None:
    claude_md_path = os.path.join(os.path.dirname(__file__), '..', 'CLAUDE.md')

    with open(claude_md_path, 'r') as f:
        content = f.read()

    if f"|{target_category}:" in content:
        pattern = rf"\|{re.escape(target_category)}:{{([^}}]+)}}"
        match = re.search(pattern, content)
        if match:
            existing_files = match.group(1)
            if filename not in existing_files:
                new_files = f"{existing_files},{filename}"
                new_line = f"|{target_category}:{{{new_files}}}"
                content = content.replace(match.group(0), new_line)
                print(f"[Indexer] Appended '{filename}' to category '{target_category}'.")
            else:
                print(f"[Indexer] '{filename}' already present in '{target_category}'. No change.")
    else:
        new_line = f"|{target_category}:{{{filename}}}"
        content = content + f"{new_line}\n"
        print(f"[Indexer] Created new category '{target_category}' with '{filename}'.")

    with open(claude_md_path, 'w') as f:
        f.write(content)

    print(f"[Indexer] CLAUDE.md updated. Agent knowledge graph expanded.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scripts/indexer.py <filename> <category>")
        print("Example: python scripts/indexer.py neck-wall-press.md 02-neck-and-posture")
        sys.exit(1)

    indexer_update(filename=sys.argv[1], target_category=sys.argv[2])
