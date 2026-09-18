#!/usr/bin/env python3
"""
Production Completeness Gate — deterministic checker.

Implements the current Finding My Wei visual-production authority.

For current Tao weekly production, the core visual roles are:
    FEED       1080x1350
    LANDSCAPE  1200x628
    STORY      1080x1920 (sequence count declared by the manifest)

LANDSCAPE is the single canonical horizontal master and may serve blog/OG,
social-link, LinkedIn, email, and other approved horizontal derivatives.
A separate EMAILHEADER is not a core daily role. It is conditional only when
Founder-approved email creative materially differs from the landscape master.

The checker supports both current issue-level APPROVED_ASSETS layouts and
historical per-day APPROVED_ASSETS/<DAY>/ layouts. It preserves established
filenames rather than requiring approved historical/current binaries to be
renamed for tooling.

Every manifested asset must complete the persistence chain:
    Produced -> Founder Approved -> Canonically Named -> Manifested
             -> Hash Verified -> Committed -> Pushed -> Remote Verified

Usage:
    python3 verify_production_completeness.py <ISSUE_DIR> [--remote-ref origin/main]

Exit codes:
    0 gate CLOSED
    1 gate OPEN
    2 usage/environment error
"""

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

DAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

CORE_ROLES = {
    "FEED": "1080x1350",
    "STORY": "1080x1920",
    "LANDSCAPE": "1200x628",
}

# Historical aliases remain readable. They are normalized to current roles for
# completeness evaluation without renaming approved assets.
ROLE_ALIASES = {
    "BLOGOG": "LANDSCAPE",
}

SEQUENCE_ROLES = {"STORY", "CAROUSEL"}
CONDITIONAL_ROLES = {"EMAILHEADER", "CAROUSEL"}
FUTURE_CHANNELS = ["REELS", "TIKTOK", "THREADS"]

ASSET_ROW = re.compile(
    r"^\s*[-*]\s*`(?P<file>[^`]+\.(?:png|jpg|jpeg))`"
    r"(?P<mid>.*?)"
    r"SHA-256\s*`(?P<sha>[0-9a-fA-F]{64})`",
    re.IGNORECASE,
)
DIMS = re.compile(r"(?<!\d)(\d{3,5})x(\d{3,5})(?!\d)")
EXPECTED_ROW = re.compile(
    r"^\s*\|\s*(?P<role>[A-Z_]+)\s*\|\s*(?P<dims>\d+x\d+|-)\s*\|\s*(?P<count>\d+)\s*\|"
)
# Accept established STORY-01, STORY_01, STORY_FRAME01 and equivalents.
SEQ_IN_NAME = re.compile(
    r"(?:^|[_-])(?:STORY|CAROUSEL|SLIDE)(?:[_-]?(?:FRAME|SLIDE))?[_-]?(\d{1,2})(?=[_.-]|$)",
    re.IGNORECASE,
)


class Result:
    def __init__(self):
        self.failures = []
        self.notes = []

    def fail(self, day, check, detail):
        self.failures.append((day, check, detail))

    def note(self, msg):
        self.notes.append(msg)

    @property
    def ok(self):
        return not self.failures


def git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def normalize_role(role):
    if not role:
        return None
    role = role.upper()
    return ROLE_ALIASES.get(role, role)


def role_from_filename(name):
    upper = name.upper()
    for token in ("EMAILHEADER", "LANDSCAPE", "BLOGOG", "CAROUSEL", "SLIDE", "STORY", "FEED"):
        if token in upper:
            if token == "SLIDE":
                return "CAROUSEL"
            return normalize_role(token)
    return None


def parse_manifest(path):
    text = path.read_text(encoding="utf-8")
    assets, expected = [], {}

    in_expected = False
    for line in text.splitlines():
        if line.strip().lower().startswith("## expected production set"):
            in_expected = True
            continue
        if in_expected and (line.strip().startswith("## ") or ASSET_ROW.match(line)):
            in_expected = False
        if in_expected:
            m = EXPECTED_ROW.match(line)
            if m and m.group("role") != "ROLE":
                role = normalize_role(m.group("role"))
                spec = {
                    "count": int(m.group("count")),
                    "dims": None if m.group("dims") == "-" else m.group("dims"),
                }
                # If a historical manifest declares BLOGOG, normalize it to
                # LANDSCAPE. Do not silently merge contradictory declarations.
                if role in expected and expected[role] != spec:
                    raise ValueError(f"conflicting expected declarations for {role}")
                expected[role] = spec
            continue

        m = ASSET_ROW.match(line)
        if not m:
            continue
        fname = m.group("file")
        mid = m.group("mid")
        d = DIMS.search(mid) or DIMS.search(fname)
        dims = f"{d.group(1)}x{d.group(2)}" if d else None
        role = None
        for token in re.findall(r"[A-Z_]{4,}", mid.upper()):
            if token == "SHA":
                continue
            cand = "CAROUSEL" if token.startswith("SLIDE") else token
            base = re.sub(r"_?\d+$", "", cand)
            base = normalize_role(base)
            if base in CORE_ROLES or base in CONDITIONAL_ROLES:
                role = base
                break
        if role is None:
            role = role_from_filename(fname)
        sm = SEQ_IN_NAME.search(fname)
        seq = int(sm.group(1)) if sm else None
        assets.append({
            "file": fname,
            "sha": m.group("sha").lower(),
            "dims": dims,
            "role": role,
            "seq": seq,
        })

    mode = "DECLARED" if expected else "DERIVED"
    if not expected:
        for a in assets:
            if not a["role"]:
                continue
            e = expected.setdefault(a["role"], {"count": 0, "dims": a["dims"]})
            e["count"] += 1
    return assets, expected, mode


def locate_manifest(issue_dir, day):
    candidates = [
        issue_dir / day / "ASSET_MANIFEST.md",
        issue_dir / f"{day}_ASSET_MANIFEST.md",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def locate_asset(issue_dir, day, filename):
    candidates = [
        issue_dir / "APPROVED_ASSETS" / day / filename,
        issue_dir / "APPROVED_ASSETS" / filename,
        # Issue 013 canonical architecture: approved assets live directly in the
        # issue root. Founder-locked; assets are not moved to satisfy the older
        # APPROVED_ASSETS/ convention.
        issue_dir / filename,
    ]
    for p in candidates:
        if p.exists():
            return p
    return candidates[0]


def check_day(repo, issue_dir, day, remote_ref, res):
    manifest = locate_manifest(issue_dir, day)
    if manifest is None:
        res.fail(day, "MANIFEST_PRESENT", "missing day asset manifest")
        return

    try:
        assets, expected, mode = parse_manifest(manifest)
    except ValueError as exc:
        res.fail(day, "MANIFEST_VALID", str(exc))
        return

    if mode == "DERIVED":
        res.note(f"{day}: expected counts DERIVED from manifest rows")
    if not assets:
        res.fail(day, "MANIFEST_NONEMPTY", "manifest declares no assets")
        return

    actual_counts = {}
    for a in assets:
        if a["role"]:
            actual_counts[a["role"]] = actual_counts.get(a["role"], 0) + 1
        else:
            res.fail(day, "ROLE_RESOLVABLE", f"{a['file']}: role not resolvable")

    for role, dims in CORE_ROLES.items():
        if role not in expected:
            res.fail(day, "CORE_ROLE_DECLARED", f"core role {role} ({dims}) absent from expected set")

    for role, spec in sorted(expected.items()):
        got = actual_counts.get(role, 0)
        if got != spec["count"]:
            res.fail(day, "COUNT_MATCH", f"{role}: expected {spec['count']} / manifested {got}")
        if spec["dims"]:
            bad = [a["file"] for a in assets if a["role"] == role and a["dims"] != spec["dims"]]
            if bad:
                res.fail(day, "ROLE_DIMENSIONS", f"{role}: expected {spec['dims']}, wrong on {', '.join(bad)}")

    for role in SEQUENCE_ROLES:
        members = [a for a in assets if a["role"] == role]
        if not members:
            continue
        seqs = [a["seq"] for a in members]
        if any(s is None for s in seqs):
            res.fail(day, "SEQUENCE_DETERMINISTIC", f"{role}: sequence number missing on " + ", ".join(a["file"] for a in members if a["seq"] is None))
            continue
        if len(set(seqs)) != len(seqs):
            res.fail(day, "SEQUENCE_UNIQUE", f"{role}: duplicate sequence numbers {sorted(seqs)}")
        want = list(range(1, len(members) + 1))
        if sorted(seqs) != want:
            res.fail(day, "SEQUENCE_CONTIGUOUS", f"{role}: expected {want}, found {sorted(seqs)}")

    rel_issue = issue_dir.relative_to(repo)
    for a in assets:
        path = locate_asset(issue_dir, day, a["file"])
        if not path.exists():
            res.fail(day, "FILE_PRESENT", f"missing {a['file']} from approved asset locations")
            continue
        rel = str(path.relative_to(repo))

        if a["dims"] and a["dims"] not in a["file"]:
            res.fail(day, "CANONICAL_NAME", f"{a['file']}: filename does not encode {a['dims']}")

        actual = sha256_file(path)
        if actual != a["sha"]:
            res.fail(day, "HASH_VERIFIED", f"{a['file']}: manifest {a['sha'][:12]}… actual {actual[:12]}…")
            continue

        rc, _, _ = git(repo, "ls-files", "--error-unmatch", rel)
        if rc != 0:
            res.fail(day, "GIT_TRACKED", f"{rel}: not tracked by git")
            continue
        _, out, _ = git(repo, "status", "--porcelain", "--", rel)
        if out:
            res.fail(day, "COMMITTED", f"{rel}: uncommitted change ({out.split()[0]})")
            continue

        rc, _, _ = git(repo, "cat-file", "-e", f"{remote_ref}:{rel}")
        if rc != 0:
            res.fail(day, "REMOTE_VERIFIED", f"{rel}: LOCAL-ONLY — absent from {remote_ref}")
            continue
        rc, remote_blob, _ = git(repo, "rev-parse", f"{remote_ref}:{rel}")
        rc2, local_blob, _ = git(repo, "hash-object", str(path))
        if rc == 0 and rc2 == 0 and remote_blob != local_blob:
            res.fail(day, "REMOTE_CONTENT_MATCH", f"{rel}: remote blob differs from approved local file")


def main():
    ap = argparse.ArgumentParser(description="Production Completeness Gate")
    ap.add_argument("issue_dir")
    ap.add_argument("--remote-ref", default="origin/main")
    ap.add_argument("--days", default=",".join(DAYS))
    args = ap.parse_args()

    issue_dir = Path(args.issue_dir).resolve()
    if not issue_dir.is_dir():
        print(f"ERROR: not a directory: {issue_dir}", file=sys.stderr)
        return 2
    rc, repo_root, _ = git(issue_dir, "rev-parse", "--show-toplevel")
    if rc != 0:
        print("ERROR: not inside a git repository", file=sys.stderr)
        return 2
    repo = Path(repo_root)

    rc, _, _ = git(repo, "rev-parse", "--verify", args.remote_ref)
    if rc != 0:
        print(f"ERROR: remote ref {args.remote_ref} not found. Run `git fetch` first.", file=sys.stderr)
        return 2

    res = Result()
    days = [d.strip().upper() for d in args.days.split(",") if d.strip()]

    print("=" * 72)
    print(f"PRODUCTION COMPLETENESS GATE — {issue_dir.name}")
    print(f"repo: {repo}")
    print(f"remote ref: {args.remote_ref}")
    print("=" * 72)

    for day in days:
        check_day(repo, issue_dir, day, args.remote_ref, res)

    _, dirty, _ = git(repo, "status", "--porcelain")
    tree_state = "CLEAN" if not dirty else "DIRTY"
    _, local_head, _ = git(repo, "rev-parse", "HEAD")
    _, remote_head, _ = git(repo, "rev-parse", args.remote_ref)
    parity = local_head == remote_head
    if not parity:
        _, ahead, _ = git(repo, "rev-list", "--count", f"{args.remote_ref}..HEAD")
        res.fail("REPO", "HEAD_PARITY", f"local HEAD {local_head[:12]} != {args.remote_ref} {remote_head[:12]} ({ahead} unpushed commit(s))")

    for n in res.notes:
        print(f"NOTE  {n}")
    print()
    for day, check, detail in res.failures:
        print(f"FAIL  [{day}] {check}: {detail}")

    print()
    print(f"working tree: {tree_state}")
    print(f"local HEAD:   {local_head}")
    print(f"{args.remote_ref}:  {remote_head}")
    print(f"HEAD parity:  {'PASS' if parity else 'FAIL'}")
    print(f"failures:     {len(res.failures)}")
    print()
    print(f"core roles: {', '.join(CORE_ROLES)}")
    print(f"conditional roles: {', '.join(sorted(CONDITIONAL_ROLES))}")
    print(f"future/conditional channels (not gated): {', '.join(FUTURE_CHANNELS)}")
    print("=" * 72)
    if res.ok:
        print("GATE CLOSED — production complete")
        return 0
    print("GATE OPEN — production NOT complete")
    return 1


if __name__ == "__main__":
    sys.exit(main())
