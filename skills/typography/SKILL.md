---
name: typography
description: Use when choosing fonts or setting size, line height, measure, alignment, links, letter-spacing, or fluid type. Use when text is hard to read, awkwardly aligned, using one-off font sizes, or a bare font-family.
---

# Typography

**Trigger:** Load when setting type, pairing sizes on one line, or fixing text that is hard to scan.

## Principles

- Most interfaces collect too many font sizes. A linear ramp from 10px to 24px creates inconsistency and slow decisions. App UI and data tables use the fixed scale below, in px or rem, and only those steps. A modular scale is too coarse there, and em sizes leave the scale when nested. Marketing pages, articles, and their headings use the fluid scale instead. See Fluid typography.
- For product UI, a neutral sans is the safe default. A system stack is enough when personality comes from elsewhere. If you pick a custom family, prefer one with many weights and a tall x-height made for small sizes. Condensed display faces belong in short headlines, not in body or labels. Popular, well-hinted families beat novelty. A serif can carry a formal personality. See `design-mode`.
- Paragraphs should be about 45–75 characters per line. Wider than that is a last resort. A width of 20–35em, or about 65ch, lands in range. If the section also holds images, keep the paragraph at that measure anyway. Do not stretch the words to match the figure.
- When two sizes share a row, align their baselines, not their vertical centers. Center alignment of mixed sizes looks fine until the sizes sit close together, then the baselines fight.
- Line-height is not a single 1.5 everywhere. It exists so the eye can find the next line. Narrow columns can sit near 1.5. Very wide columns may need closer to 2. Larger type needs less relative leading. Small text needs more. Headlines can sit at 1–1.15.
- Color every link only when the link is inside running text and must be distinguishable. In a nav, list, or menu where almost everything is a link, brand-colored underlines are noise. Use weight or a darker ink, or show the underline only on hover for minor links.
- Align for reading. For left-to-right languages, left-align almost everything. Center is for headlines and blocks of two or three lines. If one centered block runs long, shorten the copy. Right-align numbers so digits and decimals line up. Justified text needs hyphenation, and it is optional even then. Left alignment is a fine default.
- Leave the type designer's tracking alone except in two cases. Wide-tracking families used as headlines can be tightened slightly. All-caps text, where every letter is the same height, needs a little extra tracking to stay legible. Do not take a headline face, add tracking, and use it at 12px.

## Defaults

Type scale, in px. Use these exact steps as px or the matching rem (`px / 16`):

`12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72`

| Size | Line-height | Tracking |
| --- | --- | --- |
| 12–14 | 1.5–1.6 | 0, or `0.04em`–`0.08em` if uppercase |
| 16–18 | 1.5 | 0 |
| 20–24 | 1.3–1.4 | 0 |
| 30–36 | 1.15–1.25 | 0 to `-0.01em` |
| 48–72 | 1.0–1.1 | `-0.02em` if the face looks loose |

- Body size: 16. Secondary UI: 14. Captions: 12.
- Weights: 400 or 500, plus 600 or 700. See `hierarchy`.
- Measure: `max-width: 65ch`.
- Numbers in tables: `text-align: right` and `font-variant-numeric: tabular-nums`.
- Custom families should offer at least five weights before you adopt them. Otherwise use System UI, `system-ui, sans-serif`.

## Font stacks

Never ship a bare `font-family`. Put the webfont first if you need one, then end the list with the closest stack below, copied unchanged. The lists are from [Modern Font Stacks](https://modernfontstacks.com), [CC0 1.0](https://github.com/system-fonts/modern-font-stacks/blob/main/LICENSE).

Match the face's class, not a similar name. A neutral product UI uses System UI. A grotesque like Helvetica or Inter uses Neo-Grotesque. A calligraphic sans uses Humanist. A geometric sans uses Geometric Humanist. Optima-like faces use Classical Humanist. A rounded face uses Rounded Sans. A condensed gothic uses Industrial. A Renaissance serif uses Old Style. A newspaper serif uses Transitional. A high-contrast Didot or Bodoni uses Didone. A slab uses Slab Serif. Clarendon, Bookman, or Georgia uses Antique. UI code uses Monospace Code. A typewriter mono uses Monospace Slab Serif. A script uses Handwritten.

| Stack | `font-family` |
| --- | --- |
| System UI | `system-ui, sans-serif` |
| Transitional | `Charter, 'Bitstream Charter', 'Sitka Text', Cambria, serif` |
| Old Style | `'Iowan Old Style', 'Palatino Linotype', 'URW Palladio L', P052, serif` |
| Humanist | `Seravek, 'Gill Sans Nova', Ubuntu, Calibri, 'DejaVu Sans', source-sans-pro, sans-serif` |
| Geometric Humanist | `Avenir, Montserrat, Corbel, 'URW Gothic', source-sans-pro, sans-serif` |
| Classical Humanist | `Optima, Candara, 'Noto Sans', source-sans-pro, sans-serif` |
| Neo-Grotesque | `Inter, Roboto, 'Helvetica Neue', 'Arial Nova', 'Nimbus Sans', Arial, sans-serif` |
| Monospace Slab Serif | `'Nimbus Mono PS', 'Courier New', monospace` |
| Monospace Code | `ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace` |
| Industrial | `Bahnschrift, 'DIN Alternate', 'Franklin Gothic Medium', 'Nimbus Sans Narrow', sans-serif-condensed, sans-serif` |
| Rounded Sans | `ui-rounded, 'Hiragino Maru Gothic ProN', Quicksand, Comfortaa, Manjari, 'Arial Rounded MT', 'Arial Rounded MT Bold', Calibri, source-sans-pro, sans-serif` |
| Slab Serif | `Rockwell, 'Rockwell Nova', 'Roboto Slab', 'DejaVu Serif', 'Sitka Small', serif` |
| Antique | `Superclarendon, 'Bookman Old Style', 'URW Bookman', 'URW Bookman L', 'Georgia Pro', Georgia, serif` |
| Didone | `Didot, 'Bodoni MT', 'Noto Serif Display', 'URW Palladio L', P052, Sylfaen, serif` |
| Handwritten | `'Segoe Print', 'Bradley Hand', Chilanka, TSCu_Comic, casual, cursive` |

## Fluid typography

Use fluid type where size should grow with the layout. That means marketing pages, articles, and headings. Do not use it for dense app UI or data tables. Those keep the fixed px scale.

The steps live in [references/fluid-type.css](references/fluid-type.css). Load that file, then set the parent and the family.

```css
.prose {
  container-type: inline-size;
}
.prose h1 {
  font-family: Charter, 'Bitstream Charter', 'Sitka Text', Cambria, serif;
  font-size: var(--text-4xl);
}
```

- The named ratios are how much contrast you want between steps. Minor second is nearly flat. Golden ratio is loud. Set `--text-ratio` to the ratio this page needs. The file starts at minor third.
- `--text-base` moves from `--text-min` to `--text-max` as the width moves from `--screen-min` to `--screen-max`.
- Each larger step multiplies the previous step by `--text-ratio`. `sm` and `xs` divide by it.
- `100cqw` is the container's inline size, so the parent needs `container-type: inline-size`. To follow the viewport instead, replace `100cqw` with `100vw`.
- `clamp` keeps a px floor and a px ceiling, so zoom still has a real size to scale. Check the page at 200% zoom.

## Checklist

- [ ] App UI `font-size` is on the fixed scale. None of those sizes are computed with em. Fluid headings use the named steps in `references/fluid-type.css`.
- [ ] Paragraphs are capped around 45–75 characters even when the section is wider.
- [ ] Line-height drops as size rises, and rises if the line is very long.
- [ ] Mixed sizes in one row align on the baseline.
- [ ] Links in chrome are not all brand-colored. In-prose links still look clickable.
- [ ] Centered text is three lines or fewer. Long copy is left-aligned.
- [ ] Numeric columns are right-aligned with tabular figures.
- [ ] Uppercase labels have extra tracking. Body copy does not.
- [ ] UI text under 20px is not a light or hairline weight.
- [ ] The face is readable at 14–16px, or it is only used for short large titles.
- [ ] `font-family` is a Modern Font Stacks list, or a webfont followed by that list copied unchanged. A single family name fails.
- [ ] Dense app UI and tables use the fixed px scale. Marketing pages, articles, and their headings may use the fluid steps.
- [ ] Fluid type sets `container-type: inline-size` on the parent, or replaces `100cqw` with `100vw` on purpose.
- [ ] Fluid text uses the `clamp` floor. Check the page at 200% zoom.

## Example

Before: a nested em size, centered paragraph, and a centered price next to a title.

```css
.card h2 { font-size: 2.4em; text-align: center; letter-spacing: 0; }
.card p { font-size: 0.9em; line-height: 1.5; text-align: center; width: 100%; }
.price { font-size: 14px; vertical-align: middle; }
```

After: scale steps, a reading measure, baseline alignment, tighter display leading.

```css
.card {
  font-family: system-ui, sans-serif;
}
.card h2 {
  font-size: 30px;
  line-height: 1.15;
  letter-spacing: -0.01em;
  font-weight: 600;
}
.card p {
  font-size: 16px;
  line-height: 1.5;
  max-width: 65ch;
  text-align: left;
}
.title-row { display: flex; align-items: baseline; justify-content: space-between; gap: 16px; }
.price { font-size: 14px; font-variant-numeric: tabular-nums; color: var(--color-gray-600); }
```
