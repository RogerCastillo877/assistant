#!/usr/bin/env python3

"""
OSEF Runtime

06-validate-runtime.py

Performs a complete runtime validation by executing all
runtime validators in sequence.

Validators

01 Project
02 Schemas
03 References
04 Traceability
05 Policies

Execution stops immediately if any validator fails.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

VALIDATORS = [

    "01-validate-project.py",
    "02-validate-schema.py",
    "03-validate-references.py",
    "04-validate-traceability.py",
    "05-validate-policies.py",
    "06-validate-document-references.py"

]


def run_validator(script):

    print(f"\nRunning {script}")

    result = subprocess.run(
        [sys.executable, str(ROOT / script)]
    )

    return result.returncode == 0


def main():

    for validator in VALIDATORS:

        ok = run_validator(validator)

        if not ok:

            print("\nRuntime validation failed.")

            sys.exit(1)

    print("\nAll runtime validations passed.")


if __name__ == "__main__":
    main()
