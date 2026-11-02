import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/prepare-evaluation.py'


class PreparationTests(unittest.TestCase):
    def test_prepares_identical_assignments_with_separate_guidance(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'assignments'
            result = subprocess.run([sys.executable, str(SCRIPT), str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((output / 'conditions.json').read_text())
            folders = {condition: output / label for label, condition in manifest['conditions'].items()}
            self.assertEqual((folders['baseline'] / 'assignment.md').read_bytes(), (folders['skills'] / 'assignment.md').read_bytes())
            for folder in folders.values():
                for name in ['profile', 'invoices', 'booking']:
                    self.assertEqual((folder / name / 'index.html').read_bytes(), (ROOT / f'evals/fixtures/{name}.html').read_bytes())
            self.assertTrue((folders['skills'] / 'guidance/design-mode/SKILL.md').is_file())
            self.assertFalse((folders['baseline'] / 'guidance').exists())
            self.assertIn('evals/fixtures/booking.html', manifest['sources'])

    def test_refuses_to_overwrite_an_existing_assignment(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            marker = output / 'keep.txt'
            marker.write_text('existing work')
            result = subprocess.run([sys.executable, str(SCRIPT), str(output)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), 'existing work')
            self.assertEqual([path.name for path in output.iterdir()], ['keep.txt'])
