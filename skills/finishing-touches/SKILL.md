---
name: finishing-touches
description: Use when a layout already works and needs polish, or when empty states, borders, bullets, form controls, or section backgrounds still look like browser defaults. Use before calling a screen finished.
---

# Finishing touches

**Trigger:** Load when structure, type, and color are already in place and the screen still feels plain, boxed-in, or unfinished. Also load for empty states.

## Principles

- Polish what is already on the screen before adding new chrome. Bullets can become icons that match the content, not generic dots. A quotation can be a large mark in the accent hue. Links can carry a thick underline that overlaps the descenders. Checkboxes and radios can use the product color for the selected state instead of the browser's.
- A flat rectangle of color is enough decoration when you are not illustrating. Put a short accent on the top of a card, beside an alert, under a heading, on the active nav item, or across the top of the layout. One consistent accent beats a new illustration on every panel.
- Backgrounds can do more than stay white. Shift a section or a panel to another ramp step so regions separate. A gradient should use two hues no more than about 30° apart. Repeating patterns and simple geometric shapes work if their contrast stays low enough that text is untouched. A pattern can run along one edge instead of covering the whole page.
- The empty state is the first run, not an edge case. Design it with the feature: an image or a simple mark, a sentence about what is missing, and one primary action. Hide tabs, filters, and bulk actions that do nothing until content exists. Do not ship a bare "no results" line.
- Reach for a border last. A shadow, two neighboring background colors, or a larger gap often separates regions with less noise. If a border and a background change are both present, try deleting the border. Shadows that replace borders work best when the element is not the same color as the page behind it.
- Components are not stuck in their textbook shape. A menu can be more than a single column of links: groups, a second column, short descriptions, icons. A table can merge related fields into one cell and include a thumbnail when that helps scanning. A set of radios that is the point of the screen can be selectable cards. Break the familiar pattern when it makes the choice clearer, not just to be novel.

## Defaults

- Accent thickness: 3px or 4px, in the primary 500 step.
- Active nav: 3px bar on the start or bottom edge, not a second filled button style. See `hierarchy`.
- Section bands alternate `--canvas` and `--gray-100`.
- Gradient stops stay within 30° of hue and use neighboring lightness steps.
- Pattern or shape on a background: contrast against the background under about 1.2:1 so it cannot be mistaken for content.
- Empty state: one icon or illustration, one sentence, one primary button. No disabled toolbars.
- Border substitute order: more space, then a background shift, then an elevation-1 shadow, then a 1px border in `--gray-200`.

## Checklist

- [ ] Visible lists, quotes, and selection controls are styled for this product where the user will notice the browser default.
- [ ] Any accent border is a ramp color, a scale width, and used for meaning or emphasis, not on every edge.
- [ ] Large empty regions are not all the same white. Decoration does not compete with text.
- [ ] The empty state explains what is missing and offers the next action. Useless chrome is hidden.
- [ ] Boxes are not outlined by default. Separation is space, background, or shadow first.
- [ ] Menus, tables, and choice controls that carry the task are not the generic widget if a richer layout would be clearer.

## Example

Before: a boxed list and a blank first run.

```html
<section style="border: 1px solid #ccc; padding: 12px">
  <p>No projects yet.</p>
  <div>
    <button disabled>Filter</button>
    <button disabled>Export</button>
  </div>
</section>
```

After: no outer border, a tinted empty state, one action, accent reserved for the card that needs it.

```html
<section style="background: var(--color-gray-50); border-radius: 12px; padding: 32px; max-width: 32rem">
  <div style="width: 4px; height: 24px; background: var(--color-blue-600); border-radius: 999px"></div>
  <h2 style="font-size: 20px; margin: 12px 0 4px">No projects yet</h2>
  <p style="margin: 0 0 16px; color: var(--color-gray-600)">Create one to invite your team and track work.</p>
  <button style="background: var(--color-gray-900); color: white; border: 0; border-radius: 6px; padding: 8px 12px">
    Create a project
  </button>
</section>
```
