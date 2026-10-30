#!/usr/bin/env python3
"""Check Agent Skills frontmatter: present, name matches folder, description set."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
FOLD_MARKERS = {">", "|", ">-", "|-", ">+", "|+"}


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, "missing opening frontmatter"
    try:
        close = lines[1:].index("---") + 1
    except ValueError:
        return None, "missing closing frontmatter"

    data: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal key, buf
        if key is None:
            return
        parts = list(buf)
        if parts and parts[0] in FOLD_MARKERS:
            parts = parts[1:]
        value = " ".join(part.strip() for part in parts).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        data[key] = value
        key = None
        buf = []

    for line in lines[1:close]:
        if not line.strip():
            if key is not None:
                buf.append("")
            continue
        if line[0] not in " \t" and ":" in line:
            flush()
            raw_key, _, raw_value = line.partition(":")
            key = raw_key.strip()
            buf = [raw_value.strip()]
        elif key is not None:
            buf.append(line.strip())
        else:
            return None, "frontmatter line is outside a key"
    flush()
    return data, None


def main() -> int:
    errors: list[str] = []
    if not SKILLS.is_dir():
        print("skills/ directory is missing", file=sys.stderr)
        return 1

    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("no skills/*/SKILL.md files")

    for child in sorted(SKILLS.iterdir()):
        if child.is_dir() and not (child / "SKILL.md").is_file():
            errors.append(f"{child.relative_to(ROOT)}: directory has no SKILL.md")

    for skill_md in skill_files:
        folder = skill_md.parent.name
        rel = skill_md.relative_to(ROOT)
        data, err = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        if err:
            errors.append(f"{rel}: {err}")
            continue
        assert data is not None
        name = data.get("name", "").strip()
        description = data.get("description", "").strip()
        if not name:
            errors.append(f"{rel}: name is missing")
        elif name != folder:
            errors.append(f"{rel}: name {name!r} does not match folder {folder!r}")
        if not description:
            errors.append(f"{rel}: description is empty")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    names = ", ".join(path.parent.name for path in skill_files)
    print(f"ok: {len(skill_files)} skill(s): {names}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
