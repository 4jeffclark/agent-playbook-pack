#!/usr/bin/env python3
"""Validate APP YAML manifests against JSON Schemas in this directory."""

from __future__ import annotations

import json
import sys
from pathlib import Path

STANDARD_DIR = Path(__file__).resolve().parent
REPO_ROOT = STANDARD_DIR.parent
EXAMPLES_DIR = REPO_ROOT / "examples"

PACK_SCHEMA = STANDARD_DIR / "pack.manifest.schema.json"
PLAYBOOK_SCHEMA = STANDARD_DIR / "playbook.manifest.schema.json"


def _load_deps():
    try:
        import yaml  # type: ignore
        from jsonschema import Draft202012Validator  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Missing dependencies. Install with: pip install pyyaml jsonschema"
        ) from exc
    return yaml, Draft202012Validator


def _load_schema(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _validate_file(path: Path, validator, label: str) -> list[str]:
    yaml = _load_deps()[0]
    errors: list[str] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: YAML parse error: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: manifest root must be a mapping"]

    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in error.path) or "(root)"
        errors.append(f"{path}: [{label}] {loc}: {error.message}")
    return errors


def _discover_manifests(root: Path) -> tuple[list[Path], list[Path]]:
    packs = sorted(root.glob("**/*.app/pack.app.yaml"))
    playbooks = sorted(root.glob("**/*.app/layer3-playbooks/*/playbook.app.yaml"))
    return packs, playbooks


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    yaml, Draft202012Validator = _load_deps()

    pack_validator = Draft202012Validator(_load_schema(PACK_SCHEMA))
    playbook_validator = Draft202012Validator(_load_schema(PLAYBOOK_SCHEMA))

    if argv:
        paths = [Path(p).resolve() for p in argv]
        pack_paths = [p for p in paths if p.name == "pack.app.yaml"]
        playbook_paths = [p for p in paths if p.name == "playbook.app.yaml"]
        unknown = [p for p in paths if p not in pack_paths and p not in playbook_paths]
        if unknown:
            print("Unknown manifest paths (expected pack.app.yaml or playbook.app.yaml):")
            for path in unknown:
                print(f"  {path}")
            return 2
    else:
        pack_paths, playbook_paths = _discover_manifests(EXAMPLES_DIR)

    all_errors: list[str] = []
    for path in pack_paths:
        all_errors.extend(_validate_file(path, pack_validator, "pack"))
    for path in playbook_paths:
        all_errors.extend(_validate_file(path, playbook_validator, "playbook"))

    if all_errors:
        print("Manifest validation failed:")
        for line in all_errors:
            print(line)
        return 1

    print(
        f"OK: {len(pack_paths)} pack manifest(s), {len(playbook_paths)} playbook manifest(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
