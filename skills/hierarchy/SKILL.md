---
name: hierarchy
description: Use when deciding what should stand out on a screen or component, or when a UI feels noisy, flat, or like every action is equal. Covers emphasis, labels, headings, icons, and primary versus secondary actions.
---

# Hierarchy

**Trigger:** Load when ranking elements, styling buttons, pairing icons with text, or reviewing a screen where everything shouts.

## Principles

- Rank items before you style them. A screen feels designed when secondary information recedes and one thing is obviously first. Same type, same color, and the same layout can still look noisy if every element competes.
- Do not put hierarchy on font size alone. Size jumps make titles huge and supporting text unreadably small. Prefer weight and color. Two weights are enough: a regular weight for most copy, a heavier weight for emphasis. Do not drop below 400 to quiet small text. Use a softer color or one step down the type scale instead.
- On a light surface, three inks are enough: near-black for primary content, a mid gray for support, a lighter gray for metadata.
- Gray text on a colored surface is the wrong tool. The useful effect is lower contrast against that surface, not grayness. Translucent white looks washed out and disabled, and it lets photos or patterns show through the letters. Pick a solid color in the same hue and adjust saturation and lightness until the contrast drops without looking faded.
- If the important item still will not pop, quiet its neighbors. An active nav item needs the inactive ones to be softer, not a louder fill. A sidebar that competes with the main pane should sit on the page background instead of gaining its own strong color.
- For displayed data, add a separate label only when the value cannot speak for itself. This is not a rule about form fields. Skip the label when the format or the surrounding words already identify the value. Otherwise fold the label into the phrase. When you truly need a separate label, treat it as support: smaller, lighter, or both. Emphasize the label instead only when the user is scanning for the label, as on a spec sheet, and still keep the value readable.
- Heading level and visual size are different jobs. Use `h1`–`h3` for the outline, then size the text for its role on this screen. Section titles are often labels. The content under them is the focus. Hide a heading visually only when the content is self-explanatory and the name still exists for assistive tech.
- Bold type and solid icons carry more ink, so they feel louder. Balance a heavy icon by softening its color. Balance a faint thin border by making it slightly thicker before you darken it.
- Semantics do not set the rank. Most views have one primary action, a few secondary ones, and some rare tertiary ones. Primary actions are solid and high contrast. Secondary actions are outline or a quiet fill. Tertiary actions look like links. Destructive does not mean giant and red unless that destruction is the primary action. Keep it quiet on the parent screen, then make it the obvious action on the confirm step.

## Defaults

- Ink on an off-white surface: primary `var(--color-gray-900)`, secondary `var(--color-gray-600)`, tertiary `var(--color-gray-400)`.
- Weights: 400 or 500 for body, 600 or 700 for emphasis. Never 300 for text under 20px.
- On a saturated fill, secondary text keeps the fill's hue. Move lightness about 15–25 points toward the background and keep saturation high enough that it is not gray.
- One solid high-contrast button per view. A second solid button means the first one is no longer primary.

## Checklist

- [ ] Name the single primary element. Anything else that matches its size, weight, and contrast is a competitor. Remove the tie.
- [ ] In grayscale, or with color filters off, that primary element is still obvious.
- [ ] Supporting text is secondary because of color or weight, not because it is tiny.
- [ ] No gray text on a saturated background. No white text below full opacity on a photo or pattern.
- [ ] Data is not a wall of "Label: value" unless the user is hunting those labels.
- [ ] Heading size matches importance on this screen, not the tag's default size.
- [ ] Icons next to text are not heavier than the words they support, unless the icon is the signal.
- [ ] There is one primary button. Destructive styling shows up where destruction is the decision, not on every screen that mentions it.

## Example

Before: equal lines, and three solid buttons.

```html
<div class="text-sm text-gray-500 space-y-1">
  <div>Name: Ada Cole</div>
  <div>Role: Producer</div>
  <div>Desk: Studio B</div>
  <div class="flex gap-2 pt-2">
    <button class="bg-blue-600 text-white px-3 py-1.5">Edit</button>
    <button class="bg-blue-600 text-white px-3 py-1.5">Copy link</button>
    <button class="bg-red-600 text-white px-3 py-1.5">Remove</button>
  </div>
</div>
```

After: the person is primary, the rest is support, and only one action is solid. Removal waits for a confirm step.

```html
<div class="font-sans">
  <p class="text-base font-semibold text-slate-900">Ada Cole</p>
  <p class="text-sm text-slate-500">Producer · Studio B</p>
  <div class="mt-4 flex items-center gap-3">
    <button class="rounded-md bg-slate-900 px-3 py-1.5 text-sm font-semibold text-white">Edit</button>
    <button class="rounded-md border border-slate-300 px-3 py-1.5 text-sm text-slate-800">Copy link</button>
    <button class="text-sm text-slate-600 underline-offset-2 hover:underline">Remove</button>
  </div>
</div>
```
