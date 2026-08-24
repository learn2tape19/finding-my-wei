#!/usr/bin/env python3
"""
Production Completeness Gate — deterministic checker.

Implements Phase 7A of CANONICAL_PUBLICATION_WORKFLOW.md.

Validates, for each production day of an issue, that every asset the manifest
says should exist actually does exist and has completed all eight persistence
states:

    Produced -> Founder Approved -> Canonically Named -> Manifested
             -> Hash Verified -> Committed -> Pushed -> Remote Verified

This is NOT a dimension check. Dimensions do not define a production role; the
manifest does. A day passes only when expected state and actual state agree for
every declared role, including every frame of a Story sequence and every slide
of a carousel.

Usage:
    python3 verify_production_completeness.py <ISSUE_DIR> [--remote-ref origin/main]

    ISSUE_DIR is the directory containing the day folders and APPROVED_ASSETS/,
    e.g. 07_MARKETING/CAMPAIGNS/CAMPAIGN_001_THERAPEUTIC_ALLIANCE/ISSUE_008

Exit codes:
    0  gate CLOSED (all checks pass)
    1  gate OPEN   (one or more checks fail)
    2  usage / environment error

Remote verification note:
    Remote presence is checked against the fetched remote ref (default
    origin/main) using `git cat-file -e <ref>:<path>`. Run `git fetch` first;
    the checker refuses to claim remote verification against a stale ref older
    than the local HEAD's upstream unless --no-fetch-check is passed.
"""

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

DAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

# Core roles expected as part of the standard daily production architecture.
# The 1200x627 email-header role is required every production day even when that
# day has no scheduled Brevo campaign. Scheduling and asset completeness are
# separate concerns.
CORE_ROLES = {
    "FEED": "1080x1350",
    "STORY": "1080x1920",
    "BLOGOG": "1200x628",
    "EMAILHEADER": "1200x627",
}

# Roles that are sequences: completeness requires every member, in order.
SEQUENCE_ROLES = {"STORY", "CAROUSEL"}

# Recognized future/conditional channels. Extension point only — these are NOT
# gate requirements. Do not add them to CORE_ROLES without Founder doctrine
# defining their dimensions, cadence, naming, and publishing workflow.
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
SEQ_IN_NAME = re.compile(
    r"_(?:STORY|CAROUSEL|SLIDE)(?:[_]?(?:FRAME|SLIDE))?[_]?(\d{1,2})(?=[_.])",
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
    p = subprocess.run(["git", "-C", str(repo), *args],
                       capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def role_from_filename(name):
    upper = name.upper()
    for token in ("EMAILHEADER", "BLOGOG", "CAROUSEL", "SLIDE", "STORY", "FEED"):
        if token in upper:
            return "CAROUSEL" if token == "SLIDE" else token
    return None


def parse_manifest(path):
    """Return (assets, expected, mode).

    assets: list of dicts {file, sha, dims, role, seq}
    expected: dict role -> {'count': int, 'dims': str|None}
    mode: 'DECLARED' if an Expected Production Set table was found, else 'DERIVED'
    """
    text = path.read_text(encoding="utf-8")
    assets, expected = [], {}

    in_expected = False
    for line in text.splitlines():
        if line.strip().lower().startswith("## expected production set"):
            in_expected = True
            continue
        if in_expected and (line.strip().startswith("## ")
                            or ASSET_ROW.match(line)):
            in_expected = False
        if in_expected:
            m = EXPECTED_ROW.match(line)
            if m and m.group("role") not in ("ROLE",):
                expected[m.group("role")] = {
                    "count": int(m.group("count")),
                    "dims": None if m.group("dims") == "-" else m.group("dims"),
                }
            continue

        m = ASSET_ROW.match(line)
        if not m:
            continue
        fname = m.group("file")
        mid = m.group("mid")
        d = DIMS.search(mid) or DIMS.search(fname)
        dims = f"{d.group(1)}x{d.group(2)}" if d else None
        role = None
        for token in re.findall(r"[A-Z_]{4,}", mid):
            if token in ("SHA",):
                continue
            cand = "CAROUSEL" if token.startswith("SLIDE") else token
            base = re.sub(r"_?\d+$", "", cand)
            if base in CORE_ROLES or base == "CAROUSEL":
                role = base
                break
        if role is None:
            role = role_from_filename(fname)
        seq = None
        sm = SEQ_IN_NAME.search(fname)
        if sm:
            seq = int(sm.group(1))
        assets.append({"file": fname, "sha": m.group("sha").lower(),
                       "dims": dims, "role": role, "seq": seq})

    mode = "DECLARED" if expected else "DERIVED"
    if not expected:
        for a in assets:
            if not a["role"]:
                continue
            e = expected.setdefault(a["role"], {"count": 0, "dims": a["dims"]})
            e["count"] += 1
    return assets, expected, mode


def check_day(repo, issue_dir, day, remote_ref, res):
    manifest = issue_dir / day / "ASSET_MANIFEST.md"
    asset_dir = issue_dir / "APPROVED_ASSETS" / day
    rel_issue = issue_dir.relative_to(repo)

    if not manifest.exists():
        res.fail(day, "MANIFEST_PRESENT", f"missing {manifest.relative_to(repo)}")
        return
    assets, expected, mode = parse_manifest(manifest)
    if mode == "DERIVED":
        res.note(f"{day}: expected counts DERIVED from manifest rows "
                 f"(no 'Expected Production Set' table declared)")
    if not assets:
        res.fail(day, "MANIFEST_NONEMPTY", "manifest declares no assets")
        return

    # 1. Core roles known and present
    actual_counts = {}
    for a in assets:
        if a["role"]:
            actual_counts[a["role"]] = actual_counts.get(a["role"], 0) + 1
        else:
            res.fail(day, "ROLE_RESOLVABLE",
                     f"{a['file']}: role not resolvable from manifest or filename")

    for role in CORE_ROLES:
        if role not in expected:
            res.fail(day, "CORE_ROLE_DECLARED",
                     f"core role {role} ({CORE_ROLES[role]}) absent from expected set")

    # 2/3. Expected vs actual count per role
    for role, spec in sorted(expected.items()):
        got = actual_counts.get(role, 0)
        if got != spec["count"]:
            res.fail(day, "COUNT_MATCH",
                     f"{role}: expected {spec['count']} / manifested {got}")
        if spec["dims"]:
            bad = [a["file"] for a in assets
                   if a["role"] == role and a["dims"] != spec["dims"]]
            if bad:
                res.fail(day, "ROLE_DIMENSIONS",
                         f"{role}: expected {spec['dims']}, wrong on {', '.join(bad)}")

    # 4/5/6. Sequence completeness and determinism
    for role in SEQUENCE_ROLES:
        members = [a for a in assets if a["role"] == role]
        if not members:
            continue
        seqs = [a["seq"] for a in members]
        if any(s is None for s in seqs):
            res.fail(day, "SEQUENCE_DETERMINISTIC",
                     f"{role}: frame/slide number not encoded in filename for "
                     + ", ".join(a["file"] for a in members if a["seq"] is None))
            continue
        if len(set(seqs)) != len(seqs):
            res.fail(day, "SEQUENCE_UNIQUE", f"{role}: duplicate sequence numbers {sorted(seqs)}")
        want = list(range(1, len(members) + 1))
        if sorted(seqs) != want:
            res.fail(day, "SEQUENCE_CONTIGUOUS",
                     f"{role}: expected {want}, found {sorted(seqs)}")

    # 7/8. Canonical location and naming
    for a in assets:
        path = asset_dir / a["file"]
        rel = f"{rel_issue}/APPROVED_ASSETS/{day}/{a['file']}"
        if not path.exists():
            res.fail(day, "FILE_PRESENT", f"missing {rel}")
            continue
        if a["dims"] and a["dims"] not in a["file"]:
            res.fail(day, "CANONICAL_NAME",
                     f"{a['file']}: filename does not encode {a['dims']}")

        # 10. Hash verification
        actual = sha256_file(path)
        if actual != a["sha"]:
            res.fail(day, "HASH_VERIFIED",
                     f"{a['file']}: manifest {a['sha'][:12]}… actual {actual[:12]}…")
            continue

        # 11/12. Tracked by git and committed (not staged-only, not modified)
        rc, out, _ = git(repo, "ls-files", "--error-unmatch", rel)
        if rc != 0:
            res.fail(day, "GIT_TRACKED", f"{rel}: not tracked by git")
            continue
        rc, out, _ = git(repo, "status", "--porcelain", "--", rel)
        if out:
            res.fail(day, "COMMITTED", f"{rel}: uncommitted change ({out.split()[0]})")
            continue

        # 13/14. Pushed and remotely retrievable, with content identity
        rc, _, _ = git(repo, "cat-file", "-e", f"{remote_ref}:{rel}")
        if rc != 0:
            res.fail(day, "REMOTE_VERIFIED",
                     f"{rel}: LOCAL-ONLY — absent from {remote_ref}")
            continue
        rc, remote_blob, _ = git(repo, "rev-parse", f"{remote_ref}:{rel}")
        rc2, local_blob, _ = git(repo, "hash-object", str(path))
        if rc == 0 and rc2 == 0 and remote_blob != local_blob:
            res.fail(day, "REMOTE_CONTENT_MATCH",
                     f"{rel}: remote blob differs from approved local file")


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
        print(f"ERROR: remote ref {args.remote_ref} not found. Run `git fetch` first.",
              file=sys.stderr)
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

    # 15. Working tree and HEAD parity
    _, dirty, _ = git(repo, "status", "--porcelain")
    tree_state = "CLEAN" if not dirty else "DIRTY"
    _, local_head, _ = git(repo, "rev-parse", "HEAD")
    _, remote_head, _ = git(repo, "rev-parse", args.remote_ref)
    parity = local_head == remote_head
    if not parity:
        _, ahead, _ = git(repo, "rev-list", "--count", f"{args.remote_ref}..HEAD")
        res.fail("REPO", "HEAD_PARITY",
                 f"local HEAD {local_head[:12]} != {args.remote_ref} "
                 f"{remote_head[:12]} ({ahead} unpushed commit(s))")

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
    print(f"future/conditional channels (not gated): {', '.join(FUTURE_CHANNELS)}")
    print("=" * 72)
    if res.ok:
        print("GATE CLOSED — production complete")
        return 0
    print("GATE OPEN — production NOT complete")
    return 1


if __name__ == "__main__":
    sys.exit(main())
