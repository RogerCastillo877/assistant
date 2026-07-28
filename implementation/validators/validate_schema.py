#!/usr/bin/env python3

"""
OSEF Runtime

02-validate-schema.py

Validates every JSON Schema inside the project.

Checks

- valid JSON
- required fields
- $schema
- $id
- title
- type
"""

from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RUNTIME_ROOT = PROJECT_ROOT / "specification" / "300-runtime"

SCHEMA_FOLDER = RUNTIME_ROOT / "schemas"


def validate_schema(file):

    errors = []

    try:

        with open(file, encoding="utf-8") as f:

            schema = json.load(f)

    except Exception as ex:

        return [f"{file}: invalid JSON ({ex})"]

    required = [

        "$schema",

        "$id",

        "title",

        "type"

    ]

    for field in required:

        if field not in schema:

            errors.append(f"{file}: missing '{field}'")

    return errors


def validate():

    errors = []

    for file in SCHEMA_FOLDER.rglob("*.json"):

        errors.extend(validate_schema(file))

    return errors


def main():

    errors = validate()

    if errors:

        print("\nSchema validation failed\n")

        for error in errors:

            print(error)

        sys.exit(1)

    print("Schema validation passed.")


if __name__ == "__main__":
    main()
