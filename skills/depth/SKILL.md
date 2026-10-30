---
name: depth
description: Use when adding shadows, borders that should feel raised or inset, or overlap between layers. Use when elevation is random, shadows are decorative only, or a flat UI feels paper-thin.
---

# Depth

**Trigger:** Load when something should feel raised, pressed, inset, or layered above another region.

## Principles

- Light comes from above. A raised edge that faces the light is lighter. An edge that faces away is darker, and the surface below the object loses a little light. People look slightly down at a screen, so a raised control shows a hint of its top lip and hides the bottom lip. An inset well shows the opposite: a lighter bottom lip, and a small shadow just inside the top where the rim blocks the light. Pick the lighter edge color by hand. A translucent white overlay dulls the hue underneath.
- Keep it short of photoreal. A couple of pixels of shadow and a subtle edge are enough. Real outlet and window-frame shadows are sharp and close, not a huge blur on a button.
- Shadow distance is elevation, not decoration. A tight, small shadow sits just off the page. A broader, softer shadow feels closer to the viewer and pulls focus. Use the small step for buttons, a middle step for menus and popovers, and the largest for modal dialogs. Define about five shadows and reuse them. On press or drag, move the element up or down that scale: a dragged row jumps forward, a pressed button drops to a smaller shadow or none.
- A convincing shadow is often two shadows. The larger, softer, more offset one is the cast shadow from a direct light. The tighter, darker one is the contact shadow where ambient light cannot reach. As elevation increases, the contact shadow fades. At the highest step it can disappear.
- Flat UIs can still have depth. Lighter than the background reads as raised. Darker reads as inset. A solid shadow with offset and zero blur lifts a card without a soft glow.
- Overlap makes layers obvious. Let a card cross a section boundary, or let a control hang past its parent. When images overlap, give each a gap in the page color, like a thick border or padding that matches the background, so the photos do not collide.

## Defaults

Five elevations. The first shadow in each pair is the contact shadow. It fades as the element rises. The second is the cast shadow. Light is a soft top edge, not a white wash. Shadow ink is `--color-gray-900`. The lit edge is `--color-gray-50`. Alpha is written on the OKLCH value.

```css
:root {
  --edge-light: oklch(98.5% 0.002 247.839 / 0.35);
  --elev-1:
    0 1px 1px oklch(21% 0.034 264.665 / 0.08),
    0 1px 2px oklch(21% 0.034 264.665 / 0.06);
  --elev-2:
    0 1px 2px oklch(21% 0.034 264.665 / 0.08),
    0 6px 12px oklch(21% 0.034 264.665 / 0.08);
  --elev-3:
    0 1px 3px oklch(21% 0.034 264.665 / 0.06),
    0 12px 24px oklch(21% 0.034 264.665 / 0.10);
  --elev-4:
    0 2px 4px oklch(21% 0.034 264.665 / 0.05),
    0 24px 40px oklch(21% 0.034 264.665 / 0.14);
  --elev-5: 0 32px 64px oklch(21% 0.034 264.665 / 0.18);
}
.raised {
  box-shadow: var(--elev-1), inset 0 1px 0 var(--edge-light);
}
.inset {
  box-shadow:
    inset 0 1px 2px oklch(21% 0.034 264.665 / 0.12),
    inset 0 -1px 0 oklch(98.5% 0.002 247.839 / 0.65);
}
.flat-lift { box-shadow: 0 4px 0 oklch(21% 0.034 264.665 / 0.12); }
```

| Level | Use |
| --- | --- |
| 1 | Buttons, low cards |
| 2 | Dragged rows, hover cards |
| 3 | Dropdowns, popovers |
| 4 | Drawers |
| 5 | Modal dialogs |

Pressed buttons use no shadow, or drop from 2 to 1.

## Checklist

- [ ] Raised surfaces are lighter on the top edge and shadow only below, not a glow on all sides.
- [ ] Inset fields and wells are darker along the top inner edge and lighter along the bottom.
- [ ] The shadow is one of the five elevation tokens, chosen by z-order, not by taste.
- [ ] Low elevations include a tighter contact shadow. The top elevation does not rely on one.
- [ ] Interaction moves elevation: drag forward, press down.
- [ ] If the design is flat, depth still comes from a lighter or darker fill, or a hard offset shadow.
- [ ] Overlapping images have a page-colored gap between them.

## Example

Before: a blur in every direction and a white sheen.

```css
.menu { box-shadow: 0 0 24px rgb(0 0 0 / 0.35); }
.btn { box-shadow: inset 0 0 0 1px rgb(255 255 255 / 0.5); }
```

After: a menu at elevation 3, and a button that shows a top lip plus a short downward shadow.

```css
.menu { box-shadow: var(--elev-3); }
.btn { box-shadow: var(--elev-1), inset 0 1px 0 var(--edge-light); }
.btn:active { box-shadow: inset 0 1px 2px oklch(21% 0.034 264.665 / 0.2); }
```
