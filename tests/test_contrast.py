from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/check-contrast.py'


class ContrastTests(unittest.TestCase):
    def run_checker(self, text):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'skills/color/SKILL.md'
            source.parent.mkdir(parents=True)
            source.write_text(text)
            return subprocess.run([sys.executable, str(SCRIPT), '--root', str(root)], capture_output=True, text=True)

    def document(self, foreground='black', background='white', css=''):
        return f'```css\n:root {{ {css} }}\n```\n## Verified text pairs\n\n| Foreground | Background | Minimum |\n| --- | --- | --- |\n| `{foreground}` | `{background}` | 4.5 |\n'

    def test_black_white(self):
        result = self.run_checker(self.document())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('21.000:1', result.stdout)

    def test_low_contrast(self):
        result = self.run_checker(self.document('#aaa'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('2.323:1', result.stdout)

    def test_unknown_cycle_unsupported_and_gamut(self):
        for foreground, css, message in [('var(--missing)', '', 'unknown token'), ('var(--a)', '--a: var(--b); --b: var(--a);', 'cycle'), ('rgb(0 0 0)', '', 'unsupported'), ('oklch(50% 1 30)', '', 'out-of-sRGB')]:
            with self.subTest(foreground=foreground):
                result = self.run_checker(self.document(foreground, css=css))
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)

    def test_missing_table_and_rows(self):
        for text in ['', '## Verified text pairs\n| Foreground | Background | Minimum |\n| --- | --- | --- |']:
            self.assertEqual(self.run_checker(text).returncode, 1)

    def test_palette_mutation(self):
        text = self.document('var(--ink)', css='--ink: var(--gray); --gray: oklch(40% 0 0);')
        self.assertEqual(self.run_checker(text).returncode, 0)
        self.assertEqual(self.run_checker(text.replace('40%', '90%')).returncode, 1)
