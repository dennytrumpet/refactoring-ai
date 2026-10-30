---
name: layout-spacing
description: Use when setting widths, columns, padding, or gaps, or when a layout feels cramped, stretched, or ambiguously grouped. Applies a spacing scale and keeps each region only as wide as its content needs.
---

# Layout and spacing

**Trigger:** Load when placing elements, choosing widths, or fixing a layout that feels either cramped or stretched across the viewport.

## Principles

- Start with too much space, then remove it. Adding the smallest margin that "doesn't look broken" leaves the UI at the edge of cramped. Extra room that feels slightly generous on one component usually looks right in the full screen. Dense layouts are allowed when a lot of data must stay on one screen. Make that a choice, not the default.
- Use a scale whose steps are far enough apart to matter. A 4px grid still makes you pick between 120 and 124. Small sizes need closer steps because a few pixels are a large percentage. Large sizes need bigger jumps because 20px on a 500px card is noise. Keep adjacent steps at least about 25% apart. Build the scale from a 16px base instead of inventing values per component.
- You do not have to fill the window. If a form only needs about 600px, give it 600px. Full-bleed navigation does not force full-bleed content. When a narrow block looks lonely on a wide page, add a second column of supporting content instead of stretching the form. If a large canvas makes you over-spread a small UI, design at about 400px first, then relax only the parts that were compromises.
- A column grid is a tool, not a rule. Percentage columns are right when regions should grow together. They are wrong when a region has a natural size. A sidebar at 25% becomes too wide on a large monitor and too narrow on a small one. Fix the sidebar, and let the main region flex. Give cards and dialogs a max-width and let them shrink only once the viewport is smaller than that max. Do not jump them between column counts in a way that makes the medium layout wider than the large one.
- Do not lock every measurement to one ratio. A headline that is 2.5 times the body size on a desktop is often too big once the body drops to 14px. Large elements should shrink faster than small ones. Inside a component, padding should not be a fixed em of the font size. Small controls want tighter padding. Large controls want more generous padding, chosen from the scale on their own.
- Space explains grouping when there is no box. The gap around a group must be clearly larger than the gap inside it. Equal space between a label and its field, and between that field and the next label, makes the pairs ambiguous. The same trap shows up above headings, between list items that wrap, and between horizontal clusters.

## Defaults

Spacing and sizing scale, in px. No ad-hoc values between steps:

`4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768`

| Job | Step |
| --- | --- |
| Icon in a compact control | 16 or 24 |
| Tight padding inside a small button | 8 by 12 |
| Label to its control | 4 or 8 |
| Between stacked groups | 24 or 32 |
| Section break | 48 or 64 |
| Reading measure | 65ch, from `typography` |
| Form or narrow card | max-width 384 or 512 |
| Sidebar | fixed 256, main region flexes |
| Starting canvas | about 400px wide, then expand |

Group gap should be about twice the inner gap. If the inner gap is 8, the next group starts at 16 only when that is unmistakably larger, otherwise 24.

## Checklist

- [ ] Every new margin, padding, width, and height is a scale step.
- [ ] The first pass had more space than the shipped pass. Density, if any, is intentional.
- [ ] Nothing is stretched to the viewport just because the viewport is wide.
- [ ] Sidebars and other fixed-content regions use a fixed width. Percentage widths are reserved for regions that should actually flex.
- [ ] Cards and dialogs use max-width and shrink only below that cap.
- [ ] Headings and padding are not a constant em multiple of body size across breakpoints.
- [ ] Space inside a group is visibly smaller than space around it, in both axes.
- [ ] A screenshot still shows which label belongs to which control with the borders removed.

## Example

Before: one cramped column, ambiguous gaps, and a form stretched to the page.

```css
.page { padding: 10px; }
.field { margin-bottom: 10px; }
.field label { display: block; margin-bottom: 10px; }
.field input { width: 100%; }
```

After: scale steps, a cap on the form, and a larger gap between groups than inside them.

```css
.page { padding: 32px; }
form { max-width: 384px; display: grid; gap: 24px; }
.field { display: grid; gap: 8px; }
.field input { width: 100%; }
```

```html
<form>
  <div class="field"><label for="room">Room</label><input id="room" /></div>
  <div class="field"><label for="when">When</label><input id="when" type="datetime-local" /></div>
</form>
```
