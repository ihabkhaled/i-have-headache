"""Shared test helpers. Stdlib only. Git config is always local to temp repos."""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "skills" / "i-have-headache" / "scripts" / "headache_version.py"
SH = shutil.which("sh")


def run_tool(root, *args):
    p = subprocess.run([sys.executable, str(TOOL), "--root", str(root), *args],
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def git(root, *args):
    r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout


def make_repo(version="1.0.0", with_changelog=True):
    """A temp git repo with a plugin manifest, a marketplace and a CHANGELOG."""
    d = Path(tempfile.mkdtemp(prefix="hh-test-"))
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@example.invalid")
    git(d, "config", "user.name", "t")
    git(d, "config", "commit.gpgsign", "false")
    (d / ".claude-plugin").mkdir()
    (d / ".claude-plugin" / "plugin.json").write_text(
        '{\n  "name": "x",\n  "version": "%s"\n}\n' % version, encoding="utf-8", newline="")
    (d / ".claude-plugin" / "marketplace.json").write_text(
        '{\n  "name": "x",\n  "plugins": [\n    {\n      "name": "x",\n      "version": "%s"\n    }\n  ]\n}\n'
        % version, encoding="utf-8", newline="")
    (d / "skills" / "x").mkdir(parents=True)
    (d / "skills" / "x" / "SKILL.md").write_text("skill\n", encoding="utf-8")
    (d / "docs.md").write_text("docs\n", encoding="utf-8")
    if with_changelog:
        (d / "CHANGELOG.md").write_text("# Changelog\n\n## [%s] - 2026-01-01\n\n- start\n" % version,
                                        encoding="utf-8", newline="")
    commit(d, "init")
    return d


def commit(d, msg):
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", msg)


class TempCase(unittest.TestCase):
    def tearDown(self):
        for d in getattr(self, "_dirs", []):
            shutil.rmtree(d, ignore_errors=True)

    def repo(self, *a, **k):
        d = make_repo(*a, **k)
        self._dirs = getattr(self, "_dirs", []) + [d]
        return d

    def tmp(self):
        d = Path(tempfile.mkdtemp(prefix="hh-test-"))
        self._dirs = getattr(self, "_dirs", []) + [d]
        return d


LOUD = "NOT OPTIONAL"
LIMIT = "5 short bullets"


def loud_problems(text):
    """The loud marker and the numeric limit must be in every output that reaches the model."""
    return [f"missing {m!r}" for m in (LOUD, LIMIT) if m not in text]
