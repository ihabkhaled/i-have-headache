#!/usr/bin/env python3
"""Version discipline for i-have-headache: one version, every manifest, a changelog.

    headache_version.py [--root .] show
    headache_version.py [--root .] check [--base REF]
    headache_version.py [--root .] next  [--base REF]
    headache_version.py [--root .] bump major|minor|patch --date YYYY-MM-DD
    headache_version.py [--root .] set X.Y.Z

Manifests (whichever exist): .claude-plugin/plugin.json,
.claude-plugin/marketplace.json (plugins[].version), .codex-plugin/plugin.json,
.cursor-plugin/plugin.json,
package.json, pyproject.toml, VERSION.

Exit codes: 0 ok, 1 check failed, 2 usage error or bad ref.
No clock is read: bump takes its date from --date.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

MANIFESTS = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    "package.json",
    "pyproject.toml",
    "VERSION",
]
SHIPPED = [
    "skills/**", "hooks/**", "install.sh", "install.ps1", ".claude-plugin/**",
    ".codex-plugin/**", ".cursor-plugin/**", ".agents/**", "agents/**", "templates/**",
]
SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
JSON_VERSION = re.compile(r'("version"\s*:\s*")([^"]*)(")')
TOML_SECTION = re.compile(r"^\s*\[([^\]]+)\]\s*$")
TOML_VERSION = re.compile(r'^(\s*version\s*=\s*")([^"]*)(")', re.M)
TOML_PROJECT_SECTIONS = {"project", "tool.poetry"}


class Usage(Exception):
    """Bad arguments or a bad ref: exit 2."""


def parse(version: str) -> tuple[int, int, int]:
    m = SEMVER.match(version)
    if not m:
        raise Usage(f"not a version X.Y.Z: {version!r}")
    return int(m[1]), int(m[2]), int(m[3])


def glob_re(pattern: str) -> re.Pattern:
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out += ".*"
            i += 2
        elif pattern[i] == "*":
            out += "[^/]*"
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile("^" + out + "$")


def is_shipped(path: str) -> bool:
    return any(glob_re(p).match(path) for p in SHIPPED)


# --- reading versions --------------------------------------------------------

def toml_span(text: str):
    """Return the match of `version = "..."` inside [project] or [tool.poetry]."""
    section, offset = None, 0
    for line in text.splitlines(keepends=True):
        s = TOML_SECTION.match(line.rstrip("\r\n"))
        if s:
            section = s[1].strip()
        elif section in TOML_PROJECT_SECTIONS:
            m = TOML_VERSION.match(line)
            if m:
                return offset + m.start(2), offset + m.end(2), m[2]
        offset += len(line)
    return None


def depth_at(text: str, pos: int) -> int:
    """JSON nesting depth at pos (root object is 1), ignoring braces in strings."""
    depth, in_str, esc = 0, False, False
    for ch in text[:pos]:
        if in_str:
            esc = (ch == "\\") and not esc
            if ch == '"' and not esc:
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
    return depth


def versions_in(rel: str, text: str) -> list[str]:
    """Every version string the manifest declares (marketplace may hold several)."""
    if rel == "VERSION":
        return [text.strip()] if text.strip() else []
    if rel == "pyproject.toml":
        span = toml_span(text)
        return [span[2]] if span else []
    try:
        data = json.loads(text)
    except ValueError as e:
        raise Usage(f"{rel} is not valid JSON: {e}")
    if rel.endswith("marketplace.json"):
        return [str(p["version"]) for p in data.get("plugins", []) if "version" in p]
    return [str(data["version"])] if "version" in data else []


def read_text(path: Path) -> str:
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def write_text(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def collect(root: Path) -> dict[str, list[str]]:
    found = {}
    for rel in MANIFESTS:
        p = root / rel
        if p.is_file():
            vs = versions_in(rel, read_text(p))
            if vs:
                found[rel] = vs
    return found


def current(root: Path) -> tuple[dict[str, list[str]], list[str]]:
    found = collect(root)
    if not found:
        raise Usage(f"no manifest with a version under {root}")
    return found, sorted({v for vs in found.values() for v in vs})


# --- git ---------------------------------------------------------------------

def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)


def resolve_base(root: Path, ref: str) -> str:
    r = git(root, "rev-parse", "--verify", "--quiet", ref + "^{commit}")
    if r.returncode != 0:
        raise Usage(f"bad ref: {ref}")
    return r.stdout.strip()


def base_versions(root: Path, sha: str) -> list[str]:
    out = []
    for rel in MANIFESTS:
        r = git(root, "show", f"{sha}:{rel}")
        if r.returncode == 0:
            out += versions_in(rel, r.stdout)
    return sorted(set(out))


def changed(root: Path, sha: str) -> list[tuple[str, str]]:
    """(status, path) for tracked changes since sha, plus untracked files as A."""
    out = []
    r = git(root, "diff", "--name-status", "--no-renames", sha)
    for line in r.stdout.splitlines():
        status, _, path = line.partition("\t")
        out.append((status[:1], path))
    r = git(root, "ls-files", "--others", "--exclude-standard")
    out += [("A", p) for p in r.stdout.splitlines() if p]
    return out


# --- changelog ---------------------------------------------------------------

def changelog_has(root: Path, version: str) -> bool:
    p = root / "CHANGELOG.md"
    if not p.is_file():
        return False
    return re.search(rf"^## \[{re.escape(version)}\]", read_text(p), re.M) is not None


def changelog_insert(root: Path, version: str, date: str) -> bool:
    """Add a skeleton section above the newest entry. False if already present."""
    if changelog_has(root, version):
        return False
    p = root / "CHANGELOG.md"
    text = read_text(p) if p.is_file() else "# Changelog\n"
    nl = "\r\n" if "\r\n" in text else "\n"
    skeleton = nl.join([f"## [{version}] - {date}", "", "### Changed", "- ", "", ""])
    m = re.search(r"^## \[", text, re.M)
    if m:
        text = text[: m.start()] + skeleton + text[m.start():]
    else:
        text = text.rstrip("\r\n") + nl + nl + skeleton.rstrip("\r\n") + nl
    write_text(p, text)
    return True


# --- writing versions --------------------------------------------------------

def rewrite(root: Path, version: str) -> list[str]:
    touched = []
    for rel in MANIFESTS:
        p = root / rel
        if not p.is_file():
            continue
        text = read_text(p)
        old = versions_in(rel, text)
        if not old:
            continue
        if rel == "VERSION":
            lead = text[: len(text) - len(text.lstrip())]
            tail = text[len(text.rstrip()):]
            new = lead + version + tail
        elif rel == "pyproject.toml":
            a, b, _ = toml_span(text)
            new = text[:a] + version + text[b:]
        else:
            depth = 3 if rel.endswith("marketplace.json") else 1
            spans = [m for m in JSON_VERSION.finditer(text) if depth_at(text, m.start()) == depth]
            if len(spans) != len(old):
                raise Usage(f"{rel}: found {len(spans)} version strings, expected {len(old)}; edit by hand")
            new = text
            for m in reversed(spans):
                new = new[: m.start(2)] + version + new[m.end(2):]
        if new != text:
            write_text(p, new)
        touched.append(rel)
    return touched


# --- commands ----------------------------------------------------------------

def cmd_show(root: Path, a) -> int:
    found, vs = current(root)
    for rel, v in found.items():
        print(f"{rel}: {', '.join(v)}")
    print(f"version: {vs[0]}" if len(vs) == 1 else f"DISAGREE: {', '.join(vs)}")
    return 0


def cmd_check(root: Path, a) -> int:
    found, vs = current(root)
    bad = []
    if len(vs) != 1:
        bad.append("manifests disagree: " + "; ".join(f"{r}={','.join(v)}" for r, v in found.items()))
    version = vs[0]
    parse(version)
    if a.base:
        sha = resolve_base(root, a.base)
        files = [p for _, p in changed(root, sha) if is_shipped(p)]
        if files:
            before = base_versions(root, sha)
            if before and parse(version) <= max(parse(v) for v in before):
                bad.append(f"shipped paths changed since {a.base} ({files[0]}...) but version {version} "
                           f"is not greater than {max(before, key=parse)}")
            if not changelog_has(root, version):
                bad.append(f"CHANGELOG.md has no '## [{version}]' section")
    for b in bad:
        print("FAIL:", b)
    if not bad:
        print(f"ok: {version}")
    return 1 if bad else 0


def cmd_next(root: Path, a) -> int:
    _, vs = current(root)
    sha = resolve_base(root, a.base or "HEAD")
    ch = [(s, p) for s, p in changed(root, sha) if is_shipped(p)]
    if not ch:
        print("none: no shipped path changed")
        return 0
    surface = ("skills/", "hooks/", "agents/", ".agents/")
    removed = [p for s, p in ch if s == "D" and p.startswith(surface)]
    added = [p for s, p in ch if s == "A" and p.startswith(surface + ("templates/",))]
    behaviour = [p for s, p in ch if p.endswith("SKILL.md") or p == "hooks/hooks.json"]
    if removed:
        level, why = "major", f"removed {removed[0]}"
    elif added:
        level, why = "minor", f"added {added[0]}"
    elif behaviour:
        level, why = "minor", f"changed {behaviour[0]}"
    else:
        level, why = "patch", f"changed {ch[0][1]}"
    print(f"{level} -> {bump_version(max(vs, key=parse), level)}: {why}")
    return 0


def bump_version(v: str, level: str) -> str:
    major, minor, patch = parse(v)
    if level == "major":
        return f"{major + 1}.0.0"
    if level == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def cmd_bump(root: Path, a) -> int:
    if not a.date or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        raise Usage("bump needs --date YYYY-MM-DD (no clock is read)")
    found, vs = current(root)
    if len(vs) != 1:
        raise Usage("manifests disagree; run `set X.Y.Z` first")
    new = bump_version(vs[0], a.level)
    touched = rewrite(root, new)
    added = changelog_insert(root, new, a.date)
    print(f"{vs[0]} -> {new}: {', '.join(touched)}")
    print("CHANGELOG.md: " + ("section added, fill it in" if added else "section already present"))
    return 0


def cmd_set(root: Path, a) -> int:
    parse(a.version)
    touched = rewrite(root, a.version)
    print(f"{a.version}: {', '.join(touched)}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=".")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("show")
    for name in ("check", "next"):
        sub.add_parser(name).add_argument("--base")
    b = sub.add_parser("bump")
    b.add_argument("level", choices=["major", "minor", "patch"])
    b.add_argument("--date")
    sub.add_parser("set").add_argument("version")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code else 0
    root = Path(a.root)
    try:
        if not root.is_dir():
            raise Usage(f"not a directory: {a.root}")
        return {"show": cmd_show, "check": cmd_check, "next": cmd_next,
                "bump": cmd_bump, "set": cmd_set}[a.cmd](root, a)
    except Usage as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
