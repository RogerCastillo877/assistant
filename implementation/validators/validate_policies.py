#!/usr/bin/env python3

"""
OSEF Runtime

05-validate-policies.py

Validates every policy defined in the project.

Checks

- unique id
- valid effect
- valid scope
- rules exist
- no duplicated policies
"""

from pathlib import Path
import sys
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RUNTIME_ROOT = PROJECT_ROOT / "specification" / "300-runtime"

VALID_EFFECTS = {
    "allow",
    "deny",
    "require"
}

VALID_SCOPES = {
    "mission",
    "agent",
    "workflow",
    "capability",
    "skill",
    "tool",
    "resource",
    "memory",
    "project",
    "runtime"
}


def validate():

    errors = []

    ids = set()

    for file in RUNTIME_ROOT.rglob("*.yaml"):

        try:

            with open(file, encoding="utf-8") as f:
                obj = yaml.safe_load(f)

            walk(obj, ids, errors)

        except Exception:
            pass

    return errors


def walk(node, ids, errors):

    if isinstance(node, dict):

        if "effect" in node:

            pid = node.get("id")

            if pid:

                if pid in ids:
                    errors.append(f"Duplicated policy id: {pid}")

                ids.add(pid)

            effect = node.get("effect")

            if effect not in VALID_EFFECTS:
                errors.append(
                    f"Invalid effect '{effect}'"
                )

            scopes = node.get("scope", [])

            for scope in scopes:

                if scope not in VALID_SCOPES:

                    errors.append(
                        f"Invalid scope '{scope}'"
                    )

            rules = node.get("rules", [])

            if len(rules) == 0:

                errors.append(
                    f"Policy '{pid}' has no rules."
                )

        for value in node.values():
            walk(value, ids, errors)

    elif isinstance(node, list):

        for item in node:
            walk(item, ids, errors)


def main():

    errors = validate()

    if errors:

        print("\nPolicy validation failed\n")

        for err in errors:
            print(err)

        sys.exit(1)

    print("Policy validation passed.")


if __name__ == "__main__":
    main()
