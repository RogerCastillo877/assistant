#!/usr/bin/env python3
"""Validate OSEF markdown-related document references."""

from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from implementation.validators.validate_document_references import main


if __name__ == "__main__":
    main()
