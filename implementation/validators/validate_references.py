#!/usr/bin/env python3

"""
OSEF Runtime Validator

03-validate-references.py

Validates that every identifier referenced by an OSEF artifact
exists somewhere inside the project.

Examples

mission -> workflows
workflow -> capabilities
capability -> skills
skill -> tools
skill -> resources
agent -> capabilities

"""

from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RUNTIME_ROOT = PROJECT_ROOT / "specification" / "300-runtime"


def load_yaml(file):
    with open(file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_ids(root):

    ids = set()

    for file in root.rglob("*.yaml"):

        try:
            obj = load_yaml(file)

            if isinstance(obj, dict):

                if "id" in obj:
                    ids.add(obj["id"])

                for value in obj.values():
                    if isinstance(value, dict):
                        if "id" in value:
                            ids.add(value["id"])

        except Exception:
            pass

    return ids


def validate(root):

    known = collect_ids(root)

    errors = []

    for file in root.rglob("*.yaml"):

        try:
            obj = load_yaml(file)

            walk(obj, known, file, errors)

        except Exception as ex:

            errors.append(f"{file}: {ex}")

    return errors


REFERENCE_FIELDS = {

    "mission",
    "missions",

    "workflow",
    "workflows",

    "agent",
    "agents",

    "capability",
    "capabilities",

    "skill",
    "skills",

    "tool",
    "tools",

    "resource",
    "resources",

    "policy",
    "policies",

    "memory",

    "knowledge"

}


def walk(node, known, file, errors):

    if isinstance(node, dict):

        for key, value in node.items():

            if key in REFERENCE_FIELDS:

                if isinstance(value, str):

                    if value not in known:
                        errors.append(
                            f"{file}: Unknown reference '{value}'"
                        )

                elif isinstance(value, list):

                    for item in value:

                        if item not in known:

                            errors.append(
                                f"{file}: Unknown reference '{item}'"
                            )

            walk(value, known, file, errors)

    elif isinstance(node, list):

        for item in node:
            walk(item, known, file, errors)


def main():

    errors = validate(RUNTIME_ROOT)

    if errors:

        print("\nReference validation failed\n")

        for err in errors:
            print(err)

        raise SystemExit(1)

    print("Reference validation passed.")


if __name__ == "__main__":
    main()
