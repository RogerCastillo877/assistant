#!/usr/bin/env python3

"""
OSEF Runtime

04-validate-traceability.py

Validates every traceability relationship declared
inside the project.

Checks

- source exists
- target exists
- relationship is valid
- no duplicated links
"""

from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TRACEABILITY_FILE = (
    PROJECT_ROOT /
    "traceability.json"
)

VALID_RELATIONSHIPS = {

    "implements",
    "defines",
    "requires",
    "depends_on",
    "references",
    "extends",
    "specializes",
    "validates",
    "governs",
    "produces",
    "consumes",
    "uses",
    "generates",
    "documents",
    "supersedes"

}


def collect_known_ids():

    ids = set()

    for file in PROJECT_ROOT.rglob("*.yaml"):

        try:

            import yaml

            with open(file, encoding="utf-8") as f:

                obj = yaml.safe_load(f)

            walk_collect(obj, ids)

        except Exception:
            pass

    return ids


def walk_collect(node, ids):

    if isinstance(node, dict):

        if "id" in node:

            ids.add(node["id"])

        for value in node.values():

            walk_collect(value, ids)

    elif isinstance(node, list):

        for item in node:

            walk_collect(item, ids)


def validate():

    errors = []

    if not TRACEABILITY_FILE.exists():

        return [
            "traceability.json not found."
        ]

    with open(TRACEABILITY_FILE, encoding="utf-8") as f:

        links = json.load(f)

    known = collect_known_ids()

    seen = set()

    for link in links:

        source = link["source"]

        target = link["target"]

        relation = link["relationship"]

        if source not in known:

            errors.append(
                f"Unknown source: {source}"
            )

        if target not in known:

            errors.append(
                f"Unknown target: {target}"
            )

        if relation not in VALID_RELATIONSHIPS:

            errors.append(
                f"Invalid relationship: {relation}"
            )

        key = (source, relation, target)

        if key in seen:

            errors.append(
                f"Duplicated relationship: {key}"
            )

        seen.add(key)

    return errors


def main():

    errors = validate()

    if errors:

        print("\nTraceability validation failed\n")

        for err in errors:

            print(err)

        sys.exit(1)

    print("Traceability validation passed.")


if __name__ == "__main__":
    main()
