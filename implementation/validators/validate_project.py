#!/usr/bin/env python3

"""
OSEF Runtime

01-validate-project.py

Validates the basic structure of an OSEF project.

Checks

- Required folders exist
- osef.yaml exists
- schemas exist
- templates exist
- examples exist
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [

    "config/osef.yaml",

    "schemas",

    "templates",

    "examples"

]


def validate():

    errors = []

    for item in REQUIRED:

        path = PROJECT_ROOT / item

        if not path.exists():

            errors.append(f"Missing: {item}")

    return errors


def main():

    errors = validate()

    if errors:

        print("\nProject validation failed\n")

        for error in errors:

            print(error)

        sys.exit(1)

    print("Project validation passed.")


if __name__ == "__main__":
    main()
