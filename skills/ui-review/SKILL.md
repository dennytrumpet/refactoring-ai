---
name: ui-review
description: Review visual hierarchy, layout, type, color, depth, images, and polish using observed evidence. Report prioritized visual findings and identify functional accessibility checks that remain separate.
---

# UI review

**Trigger:** Load to review a finished or in-progress interface. Start with [design-mode](../design-mode/SKILL.md) when inventing a new feature.

## Principles

- **Respect product conventions.** Follow the user's requirements and the project's design system first. Use this suite's defaults where a choice is open. A different type scale, palette, radius, or spacing value is not a defect by itself.
- **Evidence before conclusions.** Report what you observed and how it affects a user. Check the rendered result when available. A percentage width does not prove stretching, a heading tag does not explain its visual size, and a written status already communicates beyond hue.
- **Severity follows user impact.** Prioritize blocked tasks, unreadable information, and misleading controls over visual preference. Do not turn a polish suggestion into a release blocker.
- **Separate visual and functional evidence.** This is a visual review. A screenshot cannot prove keyboard operation, accessible names, announcements, or error recovery. Report those checks separately before calling an interface ready.

## How to review

1. Identify the component or route, the requested scope, and the project's tokens and patterns. Read the code. Inspect the rendered interface when available and record the viewport.
2. Open the relevant topic skills and apply their checklists. For a whole-screen review, consider each topic. Skip topics the change does not affect, and explain any missing evidence.
   - [hierarchy](../hierarchy/SKILL.md)
   - [layout-spacing](../layout-spacing/SKILL.md)
   - [typography](../typography/SKILL.md)
   - [color](../color/SKILL.md)
   - [depth](../depth/SKILL.md)
   - [images](../images/SKILL.md)
   - [finishing-touches](../finishing-touches/SKILL.md)
   - [design-mode](../design-mode/SKILL.md), for a new feature or restyle
3. For each finding, state the observation, its user consequence, and the smallest fix that fits the product. Distinguish a demonstrated failure from a suggestion.
4. Calculate contrast before reporting a ratio. Inspect images before judging their quality. If the viewport, container, image, or runtime state is unknown, report that limit instead of inventing a failure.
5. Report findings in priority order. Keep the strongest actionable findings, usually no more than eight. If nothing fails, say so and list what you checked.

## Priority

| Level | File it when |
| --- | --- |
| P0 | The reviewed interface blocks the main task for affected users or makes essential information unreadable, and the evidence establishes that impact. |
| P1 | A demonstrated accessibility, readability, hierarchy, grouping, or responsive-layout problem harms use but does not meet P0. Text contrast below the applicable minimum is at least P1. |
| P2 | A supported consistency or polish issue adds friction. A style preference without a user consequence is an optional suggestion, not a defect. |

State why a finding has its priority. Do not assign priority from a token mismatch alone.

## Readiness beyond this review

Before calling the interface ready, use the project's functional accessibility checks or drive it directly to verify the following items. Record anything not checked.

- Keyboard access, logical focus order, visible focus, and focus return after dialogs close.
- Accessible names, input labels, image alternatives, and appropriate announcements for status changes.
- Loading, validation errors, failure recovery, and empty states, including active filters with no matches.
- Narrow viewports, 200% zoom, long translated labels, right-to-left content when supported, and missing or unusually long data.
- Supported themes and forced colors where the product requires them.

Passing the visual checks does not establish these behaviors or WCAG conformance.

## Output

Report the target and evidence, then findings in priority order. Each finding names the topic, observation, user consequence, and concrete fix. Separate optional suggestions and checks that lack evidence.

Finish with the principles from the skills you read that changed a material recommendation. Use `skill / Principle name` and state the choice it changed. Omit principles that did not affect the review.

## Example

The project uses 13px metadata, 10px compact spacing, and 8px panel radii. An invoice card sits in a 480px parent at a 1280px viewport. Its status is written as text.

```html
<article style="width: 100%; padding: 10px; border-radius: 8px; box-sizing: border-box; background: #fff">
  <h2 style="font-size: 24px; color: #111">Invoice 1842</h2>
  <p style="font-size: 13px; color: #aaa">Status: overdue</p>
  <button>Send reminder</button>
</article>
```

A review based on the supplied code and container dimensions can say the following.

- P1, color. The status uses `#aaa` against white, which calculates to 2.32:1. At 13px it needs at least 4.5:1. Use the project's darker supporting-text token. The current status text is hard to read.
- Clear. The word "overdue" communicates the status without color. The 100% width fits the known parent. The metadata size, compact spacing, and radius follow project tokens.
- Not checked. Keyboard behavior, focus, accessible announcements, rendered overflow, and other runtime states need direct verification.
- Principles applied. `color / Measure text contrast` led to a darker status ink. `ui-review / Respect product conventions` kept the established sizes and radius. `ui-review / Evidence before conclusions` prevented an unsupported width or color-only finding.

After the fix, the status can use a verified product token. This example uses `#595959`, which calculates to 7.00:1 against white.

```css
:root { --text-supporting: #595959; }
.invoice-status { color: var(--text-supporting); }
```
