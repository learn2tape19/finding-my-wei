#!/usr/bin/env python3
"""Check this audit's backlog and local Markdown targets; no external IO."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def check(data):
    errors = []
    ids = set()
    required = {"id", "project", "finding", "state", "evidence", "next_action",
                "suggested_owner", "review_trigger", "closure_test", "closure_evidence"}
    for item in data["items"]:
        name = item.get("id", "<missing>")
        if required - item.keys():
            errors.append(f"{name}: missing {sorted(required - item.keys())}")
        if name in ids:
            errors.append(f"{name}: duplicate ID")
        ids.add(name)
        if item.get("state") not in {"OPEN", "HOLD", "CLOSED"}:
            errors.append(f"{name}: invalid state")
        for key in required - {"closure_evidence"}:
            if not item.get(key):
                errors.append(f"{name}: empty {key}")
        if item.get("state") == "CLOSED" and not item.get("closure_evidence"):
            errors.append(f"{name}: closure needs evidence")
    return errors


def main():
    data = json.loads((HERE / "BACKLOG.json").read_text())
    errors = check(data)
    for item in data["items"]:
        for target in item["evidence"]:
            if ":" not in target:
                resolved = (HERE / target).resolve()
                if not resolved.is_relative_to(ROOT) or not resolved.exists():
                    errors.append(f"{item['id']}: invalid local evidence target: {target}")
    files = list(HERE.glob("*.md"))
    for path in files:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if ":" in target or target.startswith("#"):
                continue
            resolved = (path.parent / unquote(target.split("#")[0])).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"{path.name}: target leaves repository: {target}")
            elif not resolved.exists():
                errors.append(f"{path.name}: missing target: {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(data['items'])} backlog records; {len(files)} Markdown files checked.")
    print("External links, approvals, rights, remote persistence and delivery were not checked.")


if __name__ == "__main__":
    main()
