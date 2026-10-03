"""headache_version.py: every invariant has a test that proves it fires."""
import json
import unittest

from helpers import TempCase, commit, run_tool


class Check(TempCase):
    def test_agreeing_manifests_pass(self):
        d = self.repo()
        self.assertEqual(run_tool(d, "check")[0], 0)

    def test_disagreeing_manifests_fail(self):  # mutation: one manifest drifts
        d = self.repo()
        p = d / ".claude-plugin" / "marketplace.json"
        p.write_text(p.read_text().replace("1.0.0", "1.0.1"), newline="")
        code, out = run_tool(d, "check")
        self.assertEqual(code, 1)
        self.assertIn("disagree", out)

    def test_shipped_change_without_bump_fails(self):  # mutation: ship, forget the bump
        d = self.repo()
        (d / "skills" / "x" / "SKILL.md").write_text("changed\n")
        commit(d, "change")
        code, out = run_tool(d, "check", "--base", "HEAD~1")
        self.assertEqual(code, 1)
        self.assertIn("not greater", out)

    def test_bump_without_changelog_fails(self):  # mutation: bump, forget the changelog
        d = self.repo()
        (d / "skills" / "x" / "SKILL.md").write_text("changed\n")
        run_tool(d, "set", "1.1.0")
        commit(d, "change")
        code, out = run_tool(d, "check", "--base", "HEAD~1")
        self.assertEqual(code, 1)
        self.assertIn("CHANGELOG.md has no '## [1.1.0]'", out)

    def test_lower_version_fails(self):  # mutation: version goes backwards
        d = self.repo("1.2.0")
        (d / "skills" / "x" / "SKILL.md").write_text("changed\n")
        run_tool(d, "set", "1.1.0")
        (d / "CHANGELOG.md").write_text("## [1.1.0]\n")
        commit(d, "change")
        self.assertEqual(run_tool(d, "check", "--base", "HEAD~1")[0], 1)

    def test_full_bump_passes(self):
        d = self.repo()
        (d / "skills" / "x" / "SKILL.md").write_text("changed\n")
        self.assertEqual(run_tool(d, "bump", "minor", "--date", "2026-10-03")[0], 0)
        commit(d, "change")
        self.assertEqual(run_tool(d, "check", "--base", "HEAD~1")[0], 0)

    def test_unshipped_change_needs_no_bump(self):
        d = self.repo()
        (d / "docs.md").write_text("changed\n")
        commit(d, "docs")
        self.assertEqual(run_tool(d, "check", "--base", "HEAD~1")[0], 0)

    def test_untracked_shipped_file_counts(self):
        d = self.repo()
        (d / "hooks").mkdir()
        (d / "hooks" / "new.sh").write_text("x\n")
        self.assertEqual(run_tool(d, "check", "--base", "HEAD")[0], 1)

    def test_bad_ref_is_usage_error(self):
        d = self.repo()
        self.assertEqual(run_tool(d, "check", "--base", "no-such-ref")[0], 2)
        self.assertEqual(run_tool(d, "next", "--base", "no-such-ref")[0], 2)

    def test_no_manifest_is_usage_error(self):
        self.assertEqual(run_tool(self.tmp(), "show")[0], 2)


class Next(TempCase):
    def level(self, d):
        code, out = run_tool(d, "next", "--base", "HEAD")
        self.assertEqual(code, 0)
        return out.split()[0]

    def test_none(self):
        d = self.repo()
        (d / "docs.md").write_text("x\n")
        self.assertEqual(self.level(d), "none:")

    def test_patch(self):
        d = self.repo()
        (d / "install.sh").write_text("x\n")
        self.assertEqual(self.level(d), "patch")

    def test_minor_on_addition(self):
        d = self.repo()
        (d / "hooks").mkdir()
        (d / "hooks" / "a.sh").write_text("x\n")
        self.assertEqual(self.level(d), "minor")

    def test_minor_on_skill_edit(self):
        d = self.repo()
        (d / "skills" / "x" / "SKILL.md").write_text("changed\n")
        self.assertEqual(self.level(d), "minor")

    def test_major_on_removal(self):
        d = self.repo()
        (d / "skills" / "x" / "SKILL.md").unlink()
        self.assertEqual(self.level(d), "major")


class Bump(TempCase):
    def test_refuses_without_date(self):
        d = self.repo()
        self.assertEqual(run_tool(d, "bump", "patch")[0], 2)
        self.assertEqual(run_tool(d, "bump", "patch", "--date", "yesterday")[0], 2)
        self.assertEqual(run_tool(d, "show")[1].count("1.0.0"), 3)  # nothing changed

    def test_levels(self):
        for level, want in (("major", "2.0.0"), ("minor", "1.3.0"), ("patch", "1.2.4")):
            d = self.repo("1.2.3")
            self.assertEqual(run_tool(d, "bump", level, "--date", "2026-10-03")[0], 0)
            self.assertEqual(json.loads((d / ".claude-plugin" / "plugin.json").read_text())["version"], want)
            m = json.loads((d / ".claude-plugin" / "marketplace.json").read_text())
            self.assertEqual(m["plugins"][0]["version"], want)

    def test_changelog_skeleton_once_above_newest(self):
        d = self.repo()
        run_tool(d, "bump", "minor", "--date", "2026-10-03")
        text = (d / "CHANGELOG.md").read_text()
        self.assertLess(text.index("## [1.1.0] - 2026-10-03"), text.index("## [1.0.0]"))
        run_tool(d, "set", "1.0.0")
        run_tool(d, "bump", "minor", "--date", "2026-10-04")
        self.assertEqual((d / "CHANGELOG.md").read_text().count("## [1.1.0]"), 1)

    def test_only_version_strings_change_and_crlf_survives(self):  # mutation: reformat
        d = self.repo()
        p = d / ".claude-plugin" / "plugin.json"
        p.write_bytes(b'{\r\n    "name": "x",\r\n    "version":   "1.0.0",\r\n    "k": [1,2]\r\n}\r\n')
        (d / "CHANGELOG.md").write_bytes(b"# Changelog\r\n\r\n## [1.0.0] - 2026-01-01\r\n")
        run_tool(d, "bump", "patch", "--date", "2026-10-03")
        self.assertEqual(p.read_bytes(), b'{\r\n    "name": "x",\r\n    "version":   "1.0.1",\r\n    "k": [1,2]\r\n}\r\n')
        log = (d / "CHANGELOG.md").read_bytes()
        self.assertIn(b"## [1.0.1] - 2026-10-03\r\n", log)
        self.assertNotIn(b"\n", log.replace(b"\r\n", b""))

    def test_other_manifests(self):
        d = self.repo()
        (d / "VERSION").write_bytes(b"1.0.0\r\n")
        (d / "package.json").write_text('{"name":"x","version":"1.0.0","dependencies":{"version":"9"}}')
        (d / "pyproject.toml").write_text('[tool.x]\nversion = "7.7.7"\n[project]\nname = "x"\nversion = "1.0.0"\n')
        (d / ".codex-plugin").mkdir()
        (d / ".codex-plugin" / "plugin.json").write_text('{"version": "1.0.0"}')
        (d / ".cursor-plugin").mkdir()
        (d / ".cursor-plugin" / "plugin.json").write_text('{"version": "1.0.0"}')
        self.assertEqual(run_tool(d, "check")[0], 0)
        run_tool(d, "bump", "minor", "--date", "2026-10-03")
        self.assertEqual((d / "VERSION").read_bytes(), b"1.1.0\r\n")
        self.assertIn('[tool.x]\nversion = "7.7.7"', (d / "pyproject.toml").read_text())
        self.assertIn('version = "1.1.0"', (d / "pyproject.toml").read_text())
        self.assertIn('"1.1.0"', (d / ".cursor-plugin" / "plugin.json").read_text())
        self.assertEqual(run_tool(d, "check")[0], 0)

    def test_set_validates(self):
        d = self.repo()
        self.assertEqual(run_tool(d, "set", "1.2")[0], 2)
        self.assertEqual(run_tool(d, "set", "2.0.0")[0], 0)


if __name__ == "__main__":
    unittest.main()
