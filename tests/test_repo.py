"""The repo's own invariants: one skill, one command, one version, small Codex skill."""
import json
import unittest

from helpers import ROOT, run_tool


class Repo(unittest.TestCase):
    def test_exactly_one_skill_and_no_commands(self):
        skills = [p.name for p in (ROOT / "skills").iterdir() if p.is_dir()]
        self.assertEqual(skills, ["i-have-headache"])
        self.assertFalse((ROOT / "commands").exists())
        self.assertFalse((ROOT / ".codex" / "prompts").exists())

    def test_skill_name_matches_folder_and_stays_small(self):
        skill = ROOT / "skills" / "i-have-headache" / "SKILL.md"
        self.assertIn("name: i-have-headache\n", skill.read_text(encoding="utf-8"))
        self.assertLess(skill.stat().st_size, 8000)  # Codex limit, also for the installed copy

    def test_always_on_cut_line_exists(self):
        text = (ROOT / "skills" / "i-have-headache" / "SKILL.md").read_text(encoding="utf-8")
        self.assertEqual(sum(l.startswith("Concise mode is always on") for l in text.splitlines()), 1)

    def test_manifests_agree_and_changelog_has_the_version(self):
        code, out = run_tool(ROOT, "check")
        self.assertEqual(code, 0, out)
        version = out.split()[-1]
        self.assertIn(f"## [{version}]", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_marketplace_lists_the_plugin_once(self):
        m = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual([p["name"] for p in m["plugins"]], ["i-have-headache"])


if __name__ == "__main__":
    unittest.main()
