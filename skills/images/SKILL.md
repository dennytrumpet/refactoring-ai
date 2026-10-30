---
name: images
description: Use when placing photos, illustrations, icons, screenshots, avatars, or user uploads. Use when text sits on an image, artwork is scaled to the wrong size, or uploads can blow up the layout.
---

# Images

**Trigger:** Load when adding or reviewing any image, icon, screenshot, or user upload.

## Principles

- A weak photo sinks an otherwise careful layout. If the picture has to be specific, use a real photographer. If it can be generic, use a strong stock source. Do not design around a placeholder and plan to swap in a phone snapshot later. The lighting and crop will not match.
- Text on a photo fails when the photo is both very light and very dark. White type dies in the highlights. Dark type dies in the shadows. Calm the image before you restyle the type. A translucent black scrim helps light type. A white scrim helps dark type. Lowering the photo's own contrast, then correcting brightness, targets the problem areas more carefully than a full-bleed wash. A single color overlay (reduce contrast, remove saturation, then a solid multiply) ties the photo to the product hue. If you need to keep more of the photo's range, add a wide, unoffset text shadow that reads as a soft halo, and reduce contrast a little less.
- Every asset has a size it was drawn for. Blowing a bitmap past its pixels looks soft. Blowing a 16–24px icon up to hero size stays crisp and still looks crude, because the drawing has no detail. Put that small icon inside a shape that fills the space, and keep the glyph near its native size. Shrinking a full-app screenshot until body text is a few pixels tall invites squinting. Capture a narrower viewport, crop to the relevant part, or redraw a simplified frame where text becomes bars. The same problem hits tiny marks: a logo drawn at 128px turns to mud at 16px. Redraw a simpler mark at the target size.
- User uploads will not match your crop, contrast, or background. Lock them in a fixed frame and cover-crop. Do not let intrinsic aspect ratios reflow a gallery. When the upload's background matches the page, the edge disappears. Prefer a soft inner shadow or a translucent inner border over a solid stroke that clashes with the picture.

## Defaults

| Asset | Intended size | Treatment |
| --- | --- | --- |
| UI icon | 16, 20, or 24 | Do not render above 32 without a surrounding shape |
| Icon in a feature tile | glyph 24 inside a 48 or 64 shape | Shape uses a ramp step from `color` |
| Avatar | fixed square, 32–96 | `object-fit: cover` |
| Hero photo with text | full bleed of its region | scrim or contrast reduction under the type |
| Product screenshot | captured near display size | shrink by less than half, or crop |
| Favicon / 16px mark | drawn at 16 | not a scaled wordmark |

Scrim for light text, using `--color-gray-900`: `linear-gradient(oklch(21% 0.034 264.665 / 0.55), oklch(21% 0.034 264.665 / 0.25))`.
Halo, only if you must keep the photo lively: `text-shadow: 0 0 16px oklch(21% 0.034 264.665 / 0.8)` with no offset.
User frame: fixed aspect ratio, `object-fit: cover`, `box-shadow: inset 0 0 0 1px oklch(21% 0.034 264.665 / 0.12)`.

## Checklist

- [ ] The shipped photo is a real, high-quality image, not a stand-in you hope to replace with a casual snapshot.
- [ ] Text over a photo stays readable across the light and dark parts of that photo. A scrim, reduced contrast, color overlay, or soft halo does the work.
- [ ] Icons are near the size they were drawn. Enlarged spots use a containing shape.
- [ ] Screenshots are not scaled so far that UI text becomes illegible. Crop, recapture, or simplify instead.
- [ ] Tiny marks are redrawn for that size.
- [ ] User images sit in a fixed frame with cover cropping.
- [ ] Uploads that could blend into the page have an inner shadow or translucent inner edge, not a heavy clashing border.

## Example

Before: a 24px icon stretched to a hero, and an upload that dictates the row height.

```html
<img class="icon" src="/icons/lock.svg" width="160" height="160" alt="" />
<img class="upload" src="{{ user.photo }}" alt="" />
```

```css
.upload { max-width: 100%; height: auto; }
```

After: the glyph stays small inside a tile, and the upload is cover-cropped with a quiet inner edge.

```html
<div class="tile" aria-hidden="true"><img src="/icons/lock.svg" width="24" height="24" alt="" /></div>
<div class="frame"><img src="{{ user.photo }}" alt="" /></div>
```

```css
.tile {
  width: 64px;
  height: 64px;
  display: grid;
  place-items: center;
  border-radius: 16px;
  background: var(--color-blue-100);
}
.frame {
  width: 96px;
  aspect-ratio: 1;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: inset 0 0 0 1px oklch(21% 0.034 264.665 / 0.12);
}
.frame img { width: 100%; height: 100%; object-fit: cover; }
```
