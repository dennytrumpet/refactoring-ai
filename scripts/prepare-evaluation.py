#!/usr/bin/env python3
"""Prepare isolated UI assignments with and without the local skill suite."""

import argparse
import hashlib
import json
from pathlib import Path
import random
import shutil


def prepare(root: Path, output: Path, seed: int) -> None:
    scenarios = json.loads((root / "evals/scenarios.json").read_text())
    labels = ["cedar", "maple"]
    random.Random(seed).shuffle(labels)
    output.mkdir(parents=True, exist_ok=False)
    manifest = {"conditions": dict(zip(labels, ["baseline", "skills"])), "sources": {}}
    for source in sorted((root / "skills").rglob("*")):
        if source.is_file():
            manifest["sources"][str(source.relative_to(root))] = hashlib.sha256(source.read_bytes()).hexdigest()
    for label, condition in manifest["conditions"].items():
        folder = output / label
        folder.mkdir()
        instructions = "Work only in this assignment folder. Preserve the supplied product behavior.\n"
        if condition == "skills":
            shutil.copytree(root / "skills", folder / "guidance")
            instructions += "For UI changes, read guidance/design-mode/SKILL.md and follow its relevant topic links. For a visual review, read guidance/ui-review/SKILL.md.\n"
        (folder / "AGENTS.md").write_text(instructions)
        assignments = []
        for scenario in scenarios:
            target = folder / scenario["id"]
            target.mkdir()
            shutil.copyfile(root / "evals/fixtures" / scenario["fixture"], target / "index.html")
            request = scenario["request"]
            if scenario["id"] == "invoices":
                request += " The viewport is 1280px and the panel is 480px wide. It has no horizontal overflow. The product uses 13px metadata, 10px compact spacing, and 10px panel radii."
            assignments.append(f"## {scenario['id']}\n\nIn {scenario['id']}/index.html, {request}\n")
        (folder / "assignment.md").write_text("\n".join(assignments))
    for source in [root / "evals/scenarios.json", *sorted((root / "evals/fixtures").glob("*.html"))]:
        manifest["sources"][str(source.relative_to(root))] = hashlib.sha256(source.read_bytes()).hexdigest()
    (output / "conditions.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Prepared assignments in {output}. Keep conditions.json from the participants.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    prepare(Path(__file__).resolve().parent.parent, args.output, args.seed)


if __name__ == "__main__":
    main()
