#!/usr/bin/env python3
"""Check skill frontmatter and local Markdown link targets."""

from __future__ import annotations

import argparse
import re
import sys
from urllib.parse import unquote, urlsplit
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
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


def validate_links(root: Path, source: Path) -> list[str]:
    text = source.read_text(encoding="utf-8")
    prose = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
        else:
            prose.append(line)
    text = "\n".join(prose)
    targets = re.findall(r"!?\[[^\]]*\]\((<[^>]*>|[^\s]+?)(?:\s+[\"'][^\n]*?[\"'])?\)", text)
    targets += re.findall(r"(?m)^ {0,3}\[[^\]]+\]:\s*(<[^>]*>|\S+)", text)
    errors = []
    for target in targets:
        target = target.strip("<>")
        url = urlsplit(target)
        if url.scheme or url.netloc:
            continue
        path = (source.parent / unquote(url.path)).resolve() if url.path else source
        if not path.is_relative_to(root) or not path.exists():
            errors.append(f"{source.relative_to(root)}: missing local link {target!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    root = parser.parse_args().root.resolve()
    skills = root / "skills"
    errors: list[str] = []
    if not skills.is_dir():
        print("skills/ directory is missing", file=sys.stderr)
        return 1

    skill_files = sorted(skills.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("no skills/*/SKILL.md files")

    for child in sorted(skills.iterdir()):
        if child.is_dir() and not (child / "SKILL.md").is_file():
            errors.append(f"{child.relative_to(root)}: directory has no SKILL.md")

    for skill_md in skill_files:
        folder = skill_md.parent.name
        rel = skill_md.relative_to(root)
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

    for source in sorted(skills.rglob("*.md")):
        errors.extend(validate_links(root, source))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    names = ", ".join(path.parent.name for path in skill_files)
    print(f"ok: {len(skill_files)} skill(s): {names}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
