"""hooks.json and the two hook scripts: both events, exec form, instant, quiet exit 0."""
import copy
import json
import subprocess
import time
import unittest

from helpers import ROOT, SH

EXPECTED = {"SessionStart": "session-start.sh", "UserPromptSubmit": "prompt-reminder.sh"}


def problems(cfg):
    """Everything wrong with a hooks.json dict; empty means it is right."""
    out = []
    hooks = cfg.get("hooks", {})
    for event, script in EXPECTED.items():
        groups = hooks.get(event)
        if not groups:
            out.append(f"{event} missing")
            continue
        if any("matcher" in g for g in groups):
            out.append(f"{event} must have no matcher")
        for g in groups:
            for h in g.get("hooks", []):
                if h.get("command") != "sh" or h.get("args") != ["${CLAUDE_PLUGIN_ROOT}/hooks/" + script]:
                    out.append(f"{event} must use exec form: command sh, args [hooks/{script}]")
    return out


@unittest.skipUnless(SH, "sh not available")
class Hooks(unittest.TestCase):
    cfg = json.loads((ROOT / "hooks" / "hooks.json").read_text(encoding="utf-8"))

    def test_hooks_json_is_right(self):
        self.assertEqual(problems(self.cfg), [])

    def test_mutations_are_caught(self):
        for mutate in (
            lambda c: c["hooks"].pop("UserPromptSubmit"),
            lambda c: c["hooks"].pop("SessionStart"),
            lambda c: c["hooks"]["SessionStart"][0].update(matcher="startup"),
            lambda c: c["hooks"]["UserPromptSubmit"][0]["hooks"][0].update(command="${CLAUDE_PLUGIN_ROOT}/hooks/prompt-reminder.sh", args=[]),
        ):
            c = copy.deepcopy(self.cfg)
            mutate(c)
            self.assertNotEqual(problems(c), [])

    def run_script(self, name):
        t = time.perf_counter()
        p = subprocess.run([SH, str(ROOT / "hooks" / name)], capture_output=True, text=True, input="{}")
        return p, time.perf_counter() - t

    def test_scripts_exit_zero_non_empty(self):
        for name in EXPECTED.values():
            p, _ = self.run_script(name)
            self.assertEqual(p.returncode, 0, name)
            self.assertTrue(p.stdout.strip(), name)

    def test_prompt_reminder_is_three_short_instant_lines(self):
        p, _ = self.run_script("prompt-reminder.sh")
        self.assertLessEqual(len(p.stdout.splitlines()), 3)
        self.assertLess(len(p.stdout), 300)
        best = min(self.run_script("prompt-reminder.sh")[1] for _ in range(5))
        # 50 ms is the budget for the script itself; process spawn on Windows
        # (Git Bash) is the noise floor, so this checks the best of five.
        self.assertLess(best, 0.5)

    def test_session_start_prints_the_skill_rules(self):
        p, _ = self.run_script("session-start.sh")
        self.assertIn("I have a headache.", p.stdout)
        self.assertNotIn("Concise mode on.", p.stdout)  # the acknowledgement stays out
        self.assertNotIn("Avoid being:", p.stdout)  # nor the acknowledgement's word list
        self.assertLess(len(p.stdout), 8000)  # rules incl. clean-code section, under the Codex limit


if __name__ == "__main__":
    unittest.main()
