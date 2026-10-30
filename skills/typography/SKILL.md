---
name: typography
description: Use when choosing fonts or setting size, line height, measure, alignment, links, or letter-spacing. Use when text is hard to read, awkwardly aligned, or using one-off font sizes.
---

# Typography

**Trigger:** Load when setting type, pairing sizes on one line, or fixing text that is hard to scan.

## Principles

- Most interfaces collect too many font sizes. A linear ramp from 10px to 24px creates inconsistency and slow decisions. A mathematical modular scale looks tidy and then fails UI work: you get fractional pixels, and you miss the in-between sizes product screens need. Hand a fixed scale, in px or rem, and only use those steps. Do not define the scale in em. Nested ems compute to sizes that are not on the scale.
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
- Custom families should offer at least five weights before you adopt them. Otherwise stay on a neutral system sans: `system-ui, "Segoe UI", Roboto, sans-serif`.

## Checklist

- [ ] Every `font-size` is on the scale. None are computed with em.
- [ ] Paragraphs are capped around 45–75 characters even when the section is wider.
- [ ] Line-height drops as size rises, and rises if the line is very long.
- [ ] Mixed sizes in one row align on the baseline.
- [ ] Links in chrome are not all brand-colored. In-prose links still look clickable.
- [ ] Centered text is three lines or fewer. Long copy is left-aligned.
- [ ] Numeric columns are right-aligned with tabular figures.
- [ ] Uppercase labels have extra tracking. Body copy does not.
- [ ] UI text under 20px is not a light or hairline weight.
- [ ] The face is readable at 14–16px, or it is only used for short large titles.

## Example

Before: a nested em size, centered paragraph, and a centered price next to a title.

```css
.card h2 { font-size: 2.4em; text-align: center; letter-spacing: 0; }
.card p { font-size: 0.9em; line-height: 1.5; text-align: center; width: 100%; }
.price { font-size: 14px; vertical-align: middle; }
```

After: scale steps, a reading measure, baseline alignment, tighter display leading.

```css
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
