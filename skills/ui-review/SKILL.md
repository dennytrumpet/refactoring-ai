---
name: ui-review
description: Use when auditing a screen, component, diff, or screenshot before shipping or after a visual change. Runs every other skill checklist and returns prioritized fixes.
---

# UI review

**Trigger:** Load to audit a finished or in-progress interface. Do not load it to invent a new feature. For that, start at `design-mode`.

## How to review

1. Read the code and, when one is available, the screenshot. Note the viewport width you are judging.
2. Open each skill and apply its checklist to what you can actually see. Skills, in order:
   - `hierarchy`
   - `layout-spacing`
   - `typography`
   - `color`
   - `depth`
   - `images`
   - `finishing-touches`
   - `design-mode`, only when the change is a new feature or a restyle
3. Use that skill's defaults as the fix, not a new one-off value.
4. Skip items you cannot verify. Say so. Do not guess a contrast ratio you did not compute, and do not claim a photo is low quality without seeing it.
5. Report findings first, highest priority first. Cap the list at every P0 plus the strongest P1 and P2 items, about eight findings unless the screen is large.

## Priority

| Level | File it when |
| --- | --- |
| P0 | The primary action is unclear, body text is under 4.5:1 (or large text under 3:1), status is color-only, text on a photo fails in places, uploads can break the frame, or a first-run empty state has no next step. |
| P1 | Hierarchy is tied, spacing or type leaves the scale, groups are ambiguous, the layout stretches to fill a wide viewport, or gray text sits on a saturated fill. |
| P2 | Elevation is arbitrary, images are the wrong native size but still readable, borders are noisy, or polish and empty-state craft are thin. |

## Output

Use this shape. Every finding names the skill and a concrete fix.

```markdown
## UI review
Target: <component or route>
Evidence: <files, screenshot, viewport>

## P0
- **hierarchy** — Two solid buttons compete. Make "Publish" the only solid button. Render "Discard" as text until the confirm step.

## P1
- **layout-spacing** — Label and field share the same 16px gap as the next group. Use 8px inside the field and 24px between groups.

## P2
- **finishing-touches** — The panel is separated only by a 1px border. Drop the border and use `--gray-100` against the white page.

## Clear
- typography: sizes are on the scale, measure is capped at 65ch.

## Not checked
- images: no photos or uploads in this diff.
```

If nothing fails, say so and list what you checked. Do not invent polish work to fill the page.

## Example

Before, a card an agent might be asked to review:

```html
<div style="border: 1px solid #ccc; padding: 10px; width: 100%">
  <h1 style="font-size: 42px; color: #9ca3af">Invoice</h1>
  <p style="font-size: 13px">Status: overdue</p>
  <button style="background: #2563eb; color: #fff">Send</button>
  <button style="background: #dc2626; color: #fff">Void</button>
</div>
```

Review:

```markdown
## UI review
Target: invoice card
Evidence: snippet above, desktop width assumed

## P0
- **hierarchy** — "Send" and "Void" are both solid, and void is red on the parent screen. Keep "Send" solid. Make "Void" a text button until a confirm dialog, where it becomes the primary destructive action.
- **color** — "overdue" is color-less gray text and the only status signal. State it in words (already done) and add an icon or a dark-on-tint alert from the danger ramp. Do not rely on red alone.

## P1
- **hierarchy** — The title is 42px and gray, so the heading level is doing the styling. Drop it to 20px or 24px, near-black, weight 600. The title is a label. The status and amount should lead.
- **layout-spacing** — Padding is 10px, off the scale, and the card is width 100%. Use 24px padding and a max-width of 512px.
- **typography** — 42px and 13px are off the type scale. Use 24px and 14px.

## P2
- **finishing-touches** — Replace the gray border with a `--gray-100` background or an elevation-1 shadow.

## Not checked
- images, depth beyond the border note: no assets or layered surfaces in the snippet.
```

After the P0 and P1 fixes:

```html
<article style="max-width: 512px; padding: 24px; background: hsl(210 40% 98%); border-radius: 6px; font-family: system-ui, sans-serif">
  <p style="margin: 0; font-size: 14px; color: hsl(215 16% 34%)">Invoice 1842</p>
  <h1 style="margin: 4px 0 0; font-size: 24px; line-height: 1.25; font-weight: 600; color: hsl(222 47% 11%)">$2,400 overdue</h1>
  <p style="margin: 8px 0 0; font-size: 14px; color: hsl(0 63% 28%); background: hsl(0 86% 97%); display: inline-block; padding: 4px 8px">Payment is 12 days late</p>
  <div style="margin-top: 24px; display: flex; gap: 16px; align-items: center">
    <button style="background: hsl(222 47% 11%); color: white; border: 0; border-radius: 6px; padding: 8px 12px">Send reminder</button>
    <button style="background: none; border: 0; color: hsl(215 16% 34%); text-decoration: underline">Void</button>
  </div>
</article>
```
