#!/usr/bin/env python3
"""
Validate that markdown-related document references use OSEF document IDs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

DOCUMENT_ID_PATTERN = re.compile(r"^OSEF-[A-Z]{3}-\d{3}$")
LIST_ITEM_PATTERN = re.compile(r"^-\s+.+")


def _iter_markdown_files(paths: Iterable[Path] | None = None) -> list[Path]:
    if paths is None:
        repo_root = Path(__file__).resolve().parents[2]
        return sorted(repo_root.rglob("*.md"))

    return sorted(paths)


def validate_related_documents(paths: Iterable[Path] | None = None) -> list[str]:
    errors: list[str] = []

    for path in _iter_markdown_files(paths):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue

        lines = text.splitlines()
        in_related_section = False

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("Related Documents:"):
                in_related_section = True
                continue

            if in_related_section and not stripped:
                continue

            if in_related_section and stripped.startswith("#"):
                break

            if in_related_section and LIST_ITEM_PATTERN.match(stripped):
                item = stripped[1:].strip()
                item = item.lstrip()
                if not DOCUMENT_ID_PATTERN.match(item):
                    errors.append(
                        f"{path}: related document '{item}' must use a document ID such as OSEF-SPE-101"
                    )
                continue

            if in_related_section and not LIST_ITEM_PATTERN.match(stripped):
                in_related_section = False

    return errors


def main() -> None:
    errors = validate_related_documents()

    if errors:
        print("\nDocument reference validation failed\n")
        for err in errors:
            print(err)
        sys.exit(1)

    print("Document reference validation passed.")


if __name__ == "__main__":
    main()
