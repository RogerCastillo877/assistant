#!/usr/bin/env python3

"""
OSEF Runtime

07-validate-release.py

Validates an OSEF release before publication.

Checks

- Project validation
- Schema validation
- Reference validation
- Traceability validation
- Policy validation

If any validation fails, the release cannot be generated.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

REQUIRED_VALIDATORS = [

    "01-validate-project.py",
    "02-validate-schema.py",
    "03-validate-references.py",
    "04-validate-traceability.py",
    "05-validate-policies.py"

]


def execute(script):

    result = subprocess.run(
        [sys.executable, str(ROOT / script)]
    )

    return result.returncode == 0


def main():

    print("OSEF Release Validation")
    print("-----------------------")

    for validator in REQUIRED_VALIDATORS:

        print(f"Checking {validator}")

        if not execute(validator):

            print("\nRelease validation failed.")
            sys.exit(1)

    print("\nRelease validation passed.")
    print("The project is ready for release.")


if __name__ == "__main__":
    main()
