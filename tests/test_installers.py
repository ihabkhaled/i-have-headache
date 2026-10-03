"""install.sh / install.ps1: always-on artifacts, and uninstall leaves nothing behind.

Everything runs against a temp home (HEADACHE_USER_HOME, CODEX_HOME) with the
Claude CLI disabled (HEADACHE_CLAUDE_BIN=none): no real user config is touched.
"""
import os
import shutil
import subprocess
import unittest
from pathlib import Path

from helpers import ROOT, SH, TempCase, git, loud_problems

POWERSHELL = shutil.which("pwsh") or shutil.which("powershell")


def listing(home):
    return sorted(str(p.relative_to(home)) for p in Path(home).rglob("*"))


class Base(TempCase):
    def env(self, home, source_repo=None):
        e = dict(os.environ, HEADACHE_USER_HOME=str(home), CODEX_HOME=str(Path(home) / ".codex"),
                 HEADACHE_CLAUDE_BIN="none")
        e.pop("HEADACHE_SOURCE", None)
        if source_repo:
            e["HEADACHE_REPO_URL"] = str(source_repo)
        return e

    def served_copy(self):
        """A git repo (branch main) holding this checkout: what a download would fetch."""
        d = self.tmp() / "src"
        files = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard"],
                               capture_output=True, text=True).stdout.splitlines()
        for f in files:
            if (ROOT / f).is_file():
                (d / f).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / f, d / f)
        git(d, "init", "-q", "-b", "main")
        git(d, "config", "user.email", "t@example.invalid")
        git(d, "config", "user.name", "t")
        git(d, "config", "commit.gpgsign", "false")
        git(d, "add", "-A")
        git(d, "commit", "-q", "-m", "served")
        return d

    def assert_always_on(self, home):
        agents = (Path(home) / ".codex" / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("i-have-headache:begin", agents)
        self.assertIn("no command needed", agents)
        self.assertIn("I have a headache.", agents)
        rule = (Path(home) / ".cursor" / "rules" / "i-have-headache.mdc").read_text(encoding="utf-8")
        self.assertIn("alwaysApply: true", rule)
        self.assertIn("no command needed", rule)
        self.assertNotIn("Concise mode on.", agents + rule)
        for name, text in (("AGENTS block", agents), ("Cursor rule", rule)):
            self.assertEqual(loud_problems(text), [], name)


@unittest.skipUnless(SH, "sh not available")
class ShellInstaller(Base):
    def sh(self, home, *args, piped=False, source=None):
        if piped:  # like `curl ... | sh`: $0 is not install.sh, so it downloads
            cmd = [SH, "-s", "--", *args]
            stdin = (ROOT / "install.sh").read_text(encoding="utf-8")
        else:
            cmd, stdin = [SH, str(ROOT / "install.sh"), *args], None
        p = subprocess.run(cmd, input=stdin, capture_output=True, text=True, env=self.env(home, source))
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        return p.stdout

    def test_install_is_always_on_and_says_so(self):
        home = self.tmp()
        out = self.sh(home, "--codex", "--cursor")
        self.assertIn("no command needed", out)
        self.assert_always_on(home)

    def test_uninstall_from_checkout_leaves_nothing(self):
        home = self.tmp()
        self.sh(home, "--codex", "--cursor")
        self.sh(home, "--codex", "--cursor", "--uninstall")
        self.assertEqual(listing(home), [])

    def test_uninstall_after_download_install_removes_the_cache(self):
        home, served = self.tmp(), self.served_copy()
        self.sh(home, "--codex", "--cursor", piped=True, source=served)
        self.assertTrue((home / ".i-have-headache" / "src").is_dir())  # the cache exists
        self.assertTrue(listing(home))
        self.sh(home, "--codex", "--cursor", "--uninstall", piped=True, source=served)
        self.assertEqual(listing(home), [])  # fires if the cache is left behind


@unittest.skipUnless(POWERSHELL, "PowerShell not available")
class PowerShellInstaller(Base):
    def ps(self, home, *args, piped=False, source=None):
        script = ROOT / "install.ps1"
        if piped:  # like `irm ... | iex`: no $PSScriptRoot
            call = f"& ([scriptblock]::Create([IO.File]::ReadAllText('{script}'))) {' '.join(args)}"
        else:
            call = f"& '{script}' {' '.join(args)}"
        p = subprocess.run([POWERSHELL, "-NoProfile", "-NonInteractive", "-Command", call],
                           capture_output=True, text=True, env=self.env(home, source))
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        return p.stdout

    def test_install_is_always_on_and_says_so(self):
        home = self.tmp()
        self.assertIn("no command needed", self.ps(home, "-Codex", "-Cursor"))
        self.assert_always_on(home)

    def test_uninstall_after_download_install_removes_the_cache(self):
        home, served = self.tmp(), self.served_copy()
        self.ps(home, "-Codex", "-Cursor", piped=True, source=served)
        self.assertTrue((home / ".i-have-headache" / "src").is_dir())
        self.ps(home, "-Codex", "-Cursor", "-Uninstall", piped=True, source=served)
        self.assertEqual(listing(home), [])


if __name__ == "__main__":
    unittest.main()
