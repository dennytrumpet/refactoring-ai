from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/validate-skills.py'


class ValidationTests(unittest.TestCase):
    def run_validator(self, body='', name='sample'):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / 'skills/sample'
            skill.mkdir(parents=True)
            (skill / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: Test\n---\n{body}')
            (skill / 'reference.md').write_text('# Reference')
            if body == 'nested broken reference':
                (skill / 'reference.md').write_text('[broken][target]\n[target]: absent.css')
            return subprocess.run([sys.executable, str(SCRIPT), '--root', str(root)], capture_output=True, text=True)

    def test_local_external_fragment_and_fenced_links(self):
        result = self.run_validator('[reference](reference.md#anything)\n[web](https://example.org)\n[self](#anchor)\n```md\n[example](missing.md)\n```')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_broken_local_link(self):
        result = self.run_validator('[broken](missing.md)')
        self.assertEqual(result.returncode, 1)
        self.assertIn('missing.md', result.stderr)

    def test_name_mismatch(self):
        result = self.run_validator(name='other')
        self.assertEqual(result.returncode, 1)
        self.assertIn('does not match folder', result.stderr)

    def test_reference_documents_are_checked(self):
        result = self.run_validator('nested broken reference')
        self.assertEqual(result.returncode, 1)
        self.assertIn('reference.md', result.stderr)
        self.assertIn('absent.css', result.stderr)
