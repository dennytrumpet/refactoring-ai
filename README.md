# UI design skills

Agent-agnostic skills for designing and reviewing interfaces. Any coding agent that reads [Agent Skills](https://agentskills.io) can load them: Cursor, Claude Code, and others that point at a `skills/` directory.

Inspired by Refactoring UI by Adam Wathan and Steve Schoger. This plugin is an unofficial paraphrase, not a copy of that book, and it is not affiliated with its authors. See [NOTICE](NOTICE).

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
| `finishing-touches` | Empty states, accents, backgrounds, and fewer borders. |
| `ui-review` | Review visual evidence, report prioritized fixes, and identify separate functional accessibility checks. |

Start with `design-mode` on a new feature. Use `ui-review` for the visual pass, then complete the project's functional accessibility checks before calling a screen done.

The user's requirements and the existing product design system take precedence over the suggested defaults. A different type scale, palette, or radius is not a defect by itself.

Each skill names its principles and asks the agent to report which ones changed a material decision. The output connects a principle to a concrete choice. For example, "layout-spacing / Space explains grouping. I used the existing small gap inside each field and a larger gap between fields." Agents cite only skills they read and omit principles that did not affect the work.

## Layout

```text
.cursor-plugin/plugin.json      Cursor plugin manifest
.claude-plugin/plugin.json      Claude Code plugin manifest
.claude-plugin/marketplace.json Claude Code marketplace catalog
skills/<name>/SKILL.md          shared skills, one folder each
scripts/validate-skills.py      frontmatter and local-link checks
scripts/check-contrast.py       declared reference text-pair checks
scripts/prepare-evaluation.py   isolated paired assignments
tests/                         checker and CSS reference tests
evals/                         behavioral scenarios and run procedure
```

The Cursor manifest points `skills` at `./skills/`. Claude Code scans that directory by default, so its manifest does not set `skills` again. There is one copy of each skill.

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

Install from GitHub:

```text
/plugin marketplace add dennytrumpet/refactoring-ai
/plugin install ui-design-skills@refactoring-ai
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
python3 scripts/check-contrast.py
python3 -m unittest discover -s tests -v
```

The structural validator checks frontmatter, folder names, descriptions, and local Markdown link targets. The contrast checker calculates the explicit reference text pairs in `color`. It supports opaque hex, white, black, literal OKLCH, and simple token aliases. It rejects unsupported syntax and out-of-sRGB values instead of guessing browser behavior.

Open [the CSS reference page](tests/css-reference.html) in a browser to verify the fluid scale's container sizing and local overrides. It displays each result and an overall pass or fail.

These checks validate declared artifacts. They do not establish that an agent produces better UI. Use [the paired evaluation procedure](evals/README.md) to compare real outputs with and without the suite.

## License

The skill text, manifests, and scripts are under the MIT License. See [LICENSE](LICENSE). The book credit and the limit on what this repo may contain are in [NOTICE](NOTICE).
