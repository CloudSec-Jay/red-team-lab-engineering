#!/usr/bin/env python3
"""Validate the red-team lab catalog without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "labs" / "catalog.json"
ALLOWED_TRACKS = {"web", "api", "cloud", "transport"}
ALLOWED_STATUSES = {"planned", "source-notes", "source-lab", "executed", "retired"}
ID_PATTERN = re.compile(r"^[A-Z]+(?:-[A-Z]+)*-\d{3}$")


def validate() -> list[str]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    seen: set[str] = set()
    for index, lab in enumerate(data.get("labs", []), start=1):
        prefix = f"lab {index}"
        lab_id = lab.get("id", "")
        if not ID_PATTERN.fullmatch(lab_id):
            errors.append(f"{prefix}: invalid id {lab_id!r}")
        if lab_id in seen:
            errors.append(f"{prefix}: duplicate id {lab_id}")
        seen.add(lab_id)
        if lab.get("track") not in ALLOWED_TRACKS:
            errors.append(f"{lab_id}: invalid track")
        if lab.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{lab_id}: invalid status")
        for field in ("title", "source"):
            if not lab.get(field):
                errors.append(f"{lab_id}: missing {field}")
        if lab.get("status") == "executed" and not lab.get("evidence"):
            errors.append(f"{lab_id}: executed labs require evidence")

    if not seen:
        errors.append("catalog must contain at least one lab")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("Lab catalog validation passed.")
