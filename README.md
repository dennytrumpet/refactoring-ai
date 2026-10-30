# UI design skills

Agent-agnostic skills for designing and reviewing interfaces. Any coding agent that reads [Agent Skills](https://agentskills.io) can load them: Cursor, Claude Code, and others that point at a `skills/` directory.

The advice is original writing. It is not a reproduction of *Refactoring UI*, and this plugin is not affiliated with that book. See [NOTICE](NOTICE).

## Skills

| Skill | Use it when |
| --- | --- |
| `design-mode` | Starting or scoping a UI change. Loads the topic skills as the decisions come up. |
| `hierarchy` | Ranking what stands out: emphasis, labels, headings, and actions. |
| `layout-spacing` | Widths, columns, padding, and gaps. |
| `typography` | Fonts, sizes, measure, line height, alignment, and links. |
| `color` | OKLCH palettes, the 11-step shade scale, contrast, and status that is not color-only. |
| `depth` | Elevation, shadows, inset surfaces, and overlapping layers. |
| `images` | Photos, icons, screenshots, and user uploads. |

Later skills in this plugin cover finishing touches and a full-screen review. Start with `design-mode` so the agent does not jump straight to decoration.

## Layout

```text
.cursor-plugin/plugin.json   Cursor plugin manifest
.claude-plugin/plugin.json   Claude Code plugin manifest
skills/<name>/SKILL.md       shared skills, one folder each
scripts/validate-skills.py   frontmatter check
```

Both manifests set `skills` to `./skills/`. There is one copy of each skill.

## Install

### Cursor

Copy the repo into the local plugin folder (a symlink that points outside that folder is skipped):

```bash
mkdir -p ~/.cursor/plugins/local
cp -R /path/to/refactoring-ai ~/.cursor/plugins/local/ui-design-skills
```

Reload the window. Confirm **UI design skills** under Customize. On Enterprise, an admin must allow local plugin imports.

### Claude Code

Load this directory for one session:

```bash
claude --plugin-dir /path/to/refactoring-ai
```

To keep it across sessions, copy the repo to `~/.claude/skills/ui-design-skills` (the folder that contains `.claude-plugin/plugin.json`) or the project's `.claude/skills/ui-design-skills`. Claude Code treats that as a skills-directory plugin.

From a marketplace you already added:

```text
/plugin install ui-design-skills@<marketplace>
```

### Other agents

Install the folders under `skills/` wherever that agent reads Agent Skills. Common locations:

- project: `.agents/skills/`
- Codex: `~/.codex/skills/`
- a generic user skills dir the product documents

Copy each `skills/<name>` directory as-is so `SKILL.md` stays one level down. The `name` in the frontmatter must keep matching the folder.

## Check the skills

```bash
python3 scripts/validate-skills.py
```

The script fails if a skill is missing frontmatter, if `name` does not match the folder, or if `description` is empty.
