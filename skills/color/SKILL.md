---
name: color
description: Use when choosing a palette, building an OKLCH shade ramp, or checking contrast and status colors. Use when colors are one-off hex values, washed-out ramps, or the only signal for meaning.
---

# Color

**Trigger:** Load when introducing or changing color, including grays, status, and text on a colored surface.

## Principles

- Author UI color in OKLCH. L is perceptual lightness, so equal steps in L look evenly spaced. C is chroma, how colorful the step is. H is the hue in degrees. Hex and RGB hide those relationships, so do not build a ramp by nudging hex.
- A five-swatch brand sheet is not a product palette. You need a gray ramp for text and surfaces, one or two primaries for actions, and accent ramps for success, warning, and danger. A complex product can need on the order of ten hues.
- Define every shade before you use it. Do not call `lighten()`, `darken()`, or `color-mix()` at the component to invent a new step. That manufactures near-duplicates. Use the fixed 11-step scale: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950. Pick the button step and one alert pair first, then fill only the missing steps on that scale. Do not insert a 450 because two neighbors feel close.
- Lightness is L. Lighten and darken by changing L, not by rotating hue. Hold H nearly constant on a ramp. A small deliberate drift is enough (the reference blue moves from about 255 toward 268 as it gets darker). A jump that reads as a different color belongs on another ramp.
- Keep chroma up for as long as the gamut allows, so the light and dark steps do not collapse to gray. C peaks through the middle, where displays can actually show it. Very high L and very low L cannot hold that chroma in sRGB, so lower C on 50, 100, 900, and 950 instead of letting the browser clip the color into a muddy neighbor. The reference blue peaks near 0.25 at 600, and is about 0.01 at 50 and 0.09 at 950.
- Grays are not zero chroma. Give them a little C at a cool hue, around 250–265 in the reference, with C staying under about 0.04. The darkest ink is gray-950, not pure black.
- Contrast is measured on the painted pixels. L is not a contrast ratio. Normal text under about 18px needs at least 4.5:1. Larger text needs at least 3:1. White text on a 600 or 700 fill often makes the block dominate the page. Prefer dark text on a 50 or 100 tint when the message should stay quiet. On a colored surface, secondary text is another step of the same ramp, not a neutral gray.
- Color supports a message the interface already states. Add an icon, a word, or a lighter-versus-darker pair. Never use hue as the only channel.

## Defaults

Eleven steps, named `--color-<hue>-<step>`. This is the reference palette: cool gray, blue, green, and red. Copy these tokens. Do not re-mix them.

```css
:root {
  --color-gray-50: oklch(98.5% 0.002 247.839);
  --color-gray-100: oklch(96.7% 0.003 264.542);
  --color-gray-200: oklch(92.8% 0.006 264.531);
  --color-gray-300: oklch(87.2% 0.01 258.338);
  --color-gray-400: oklch(70.7% 0.022 261.325);
  --color-gray-500: oklch(55.1% 0.027 264.364);
  --color-gray-600: oklch(44.6% 0.03 256.802);
  --color-gray-700: oklch(37.3% 0.034 259.733);
  --color-gray-800: oklch(27.8% 0.033 256.848);
  --color-gray-900: oklch(21% 0.034 264.665);
  --color-gray-950: oklch(13% 0.028 261.692);

  --color-blue-50: oklch(97% 0.014 254.604);
  --color-blue-100: oklch(93.2% 0.032 255.585);
  --color-blue-200: oklch(88.2% 0.059 254.128);
  --color-blue-300: oklch(80.9% 0.105 251.813);
  --color-blue-400: oklch(70.7% 0.165 254.624);
  --color-blue-500: oklch(62.3% 0.214 259.815);
  --color-blue-600: oklch(54.6% 0.245 262.881);
  --color-blue-700: oklch(48.8% 0.243 264.376);
  --color-blue-800: oklch(42.4% 0.199 265.638);
  --color-blue-900: oklch(37.9% 0.146 265.522);
  --color-blue-950: oklch(28.2% 0.091 267.935);

  --color-green-50: oklch(98.2% 0.018 155.826);
  --color-green-100: oklch(96.2% 0.044 156.743);
  --color-green-200: oklch(92.5% 0.084 155.995);
  --color-green-300: oklch(87.1% 0.15 154.449);
  --color-green-400: oklch(79.2% 0.209 151.711);
  --color-green-500: oklch(72.3% 0.219 149.579);
  --color-green-600: oklch(62.7% 0.194 149.214);
  --color-green-700: oklch(52.7% 0.154 150.069);
  --color-green-800: oklch(44.8% 0.119 151.328);
  --color-green-900: oklch(39.3% 0.095 152.535);
  --color-green-950: oklch(26.6% 0.065 152.934);

  --color-red-50: oklch(97.1% 0.013 17.38);
  --color-red-100: oklch(93.6% 0.032 17.717);
  --color-red-200: oklch(88.5% 0.062 18.334);
  --color-red-300: oklch(80.8% 0.114 19.571);
  --color-red-400: oklch(70.4% 0.191 22.216);
  --color-red-500: oklch(63.7% 0.237 25.331);
  --color-red-600: oklch(57.7% 0.245 27.325);
  --color-red-700: oklch(50.5% 0.213 27.518);
  --color-red-800: oklch(44.4% 0.177 26.899);
  --color-red-900: oklch(39.6% 0.141 25.723);
  --color-red-950: oklch(25.8% 0.092 26.042);

  --ink: var(--color-gray-900);
  --ink-secondary: var(--color-gray-600);
  --canvas: white;
  --surface-sunken: var(--color-gray-100);
}
```

| Steps | Use |
| --- | --- |
| 50–100 | Tinted backgrounds, quiet alerts |
| 200–300 | Borders, hover washes |
| 400–500 | Icons, illustrations, bright fills |
| 600–700 | Buttons and text that must meet contrast |
| 800–950 | Text on tints, near-black ink |

Button fill: `--color-blue-600`. Alert background: `--color-red-50`. Alert text: `--color-red-800`. Check that pair against 4.5:1 before shipping. Add warning the same way, on this scale, and use accents sparingly.

`oklch()` is ignored by browsers that do not understand it, and a C that is past the display gamut gets mapped to a duller color. Put the sRGB rendering of the same step first, then the OKLCH value. The ends of the ramp already use less chroma so that mapping has less to do.

```css
.button {
  background: #2563eb; /* sRGB rendering of --color-blue-600 */
  background: var(--color-blue-600);
}
```

## Checklist

- [ ] New colors are the named 11-step tokens, not a fresh hex and not a runtime mix or lighten.
- [ ] Each ramp is OKLCH. L is what changes from 50 to 950, and the steps look even in lightness.
- [ ] C stays high through the middle and drops at the light and dark ends only as far as the gamut requires.
- [ ] H on one ramp drifts a little. It does not jump to a different color.
- [ ] Grays use a cool hue and a small chroma. The darkest ink is gray-950, not `#000`.
- [ ] Where older browsers matter, an sRGB fallback is declared before `oklch()`.
- [ ] Body text meets 4.5:1. Large text meets 3:1. Quiet colored messages are dark text on a 50 or 100 tint.
- [ ] Status and chart series still communicate with an icon, a word, or a lightness difference when hue is removed.

## Example

Before: a one-off red, gray text on that red, and a generated lighter red.

```css
.alert { background: #ef4444; color: #d1d5db; }
.alert button { background: #fca5a5; } /* mixed lighter at the call site */
```

After: both colors are ramp steps, the message is dark-on-tint, and the words carry the meaning too.

```css
.alert {
  background: var(--color-red-50);
  color: var(--color-red-800);
  border-left: 4px solid var(--color-red-600);
}
```

```html
<div class="alert" role="status">
  <strong>Payment failed.</strong> Check the card and try again.
</div>
```
