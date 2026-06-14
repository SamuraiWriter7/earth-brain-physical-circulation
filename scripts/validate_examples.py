#!/usr/bin/env python3
"""
Validate example YAML files against their JSON Schemas.

This script validates the Physical Circulation examples for
Earth Brain OS.

Current validation targets:
- examples/wind-node.example.yaml
  -> schemas/wind-node.schema.json
- examples/optical-node.example.yaml
  -> schemas/optical-node.schema.json
- examples/hybrid-node.example.yaml
  -> schemas/hybrid-node.schema.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Wind Node",
        "schema": REPOSITORY_ROOT / "schemas" / "wind-node.schema.json",
        "example": REPOSITORY_ROOT / "examples" / "wind-node.example.yaml",
    },
    {
        "name": "Optical Node",
        "schema": REPOSITORY_ROOT / "schemas" / "optical-node.schema.json",
        "example": REPOSITORY_ROOT / "examples" / "optical-node.example.yaml",
    },
    {
        "name": "Hybrid Node",
        "schema": REPOSITORY_ROOT / "schemas" / "hybrid-node.schema.json",
        "example": REPOSITORY_ROOT / "examples" / "hybrid-node.example.yaml",
    },
]


def load_json(path: Path) -> Any:
    """Load a JSON file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {path}") from None
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {path}: {error}") from None


def load_yaml(path: Path) -> Any:
    """Load a YAML file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found: {path}") from None
    except yaml.YAMLError as error:
        raise ValueError(f"Invalid YAML in {path}: {error}") from None


def format_error_path(error_path: Any) -> str:
    """Format a jsonschema error path for human-readable output."""
    path_parts = list(error_path)

    if not path_parts:
        return "<root>"

    return ".".join(str(part) for part in path_parts)


def validate_example(name: str, schema_path: Path, example_path: Path) -> bool:
    """Validate one example file against one schema file."""
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(REPOSITORY_ROOT)}")
    print(f"  example: {example_path.relative_to(REPOSITORY_ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))

    if errors:
        print(f"[error] {name} validation failed")

        for error in errors:
            error_path = format_error_path(error.path)
            print(f"  - path: {error_path}")
            print(f"    message: {error.message}")

        return False

    print(f"[ok] {name} example is valid")
    return True


def main() -> int:
    """Run all configured validations."""
    all_valid = True

    for target in VALIDATION_TARGETS:
        try:
            is_valid = validate_example(
                name=target["name"],
                schema_path=target["schema"],
                example_path=target["example"],
            )
        except Exception as error:
            print(f"[error] {target['name']} validation could not run")
            print(f"  {error}")
            is_valid = False

        all_valid = all_valid and is_valid

    if not all_valid:
        print("[result] Validation failed")
        return 1

    print("[result] All examples are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())


