"""The contract is loud and has a number: it must reach the model in every channel.

Incident 2026-10-03: the model ignored a polite contract and wrote ~25 lines for
a summary request. If the loud marker or the numeric limit disappears from the
skill or either hook, these tests fail. (Codex block and Cursor rule: see
test_installers.py.)
"""
import subprocess
import unittest

from helpers import LIMIT, LOUD, ROOT, SH, loud_problems


class Loud(unittest.TestCase):
    def test_checker_fires(self):  # mutation: remove each marker
        good = f"X {LOUD} Y {LIMIT}"
        self.assertEqual(loud_problems(good), [])
        self.assertEqual(len(loud_problems(good.replace(LOUD, ""))), 1)
        self.assertEqual(len(loud_problems(good.replace(LIMIT, "5 bullets"))), 1)

    def test_skill_is_loud(self):
        text = (ROOT / "skills" / "i-have-headache" / "SKILL.md").read_text(encoding="utf-8")
        self.assertEqual(loud_problems(text), [])

    @unittest.skipUnless(SH, "sh not available")
    def test_hooks_are_loud(self):
        for name in ("session-start.sh", "prompt-reminder.sh"):
            out = subprocess.run([SH, str(ROOT / "hooks" / name)], capture_output=True, text=True).stdout
            self.assertEqual(loud_problems(out), [], name)


if __name__ == "__main__":
    unittest.main()
