---
name: design-mode
description: Use when starting a screen, feature, or visual redesign, before picking chrome, colors, or decoration. Sets feature-first scope, grayscale structure, personality, and constrained tokens, then tells you which topic skill to load.
---

# Design mode

**Trigger:** Load this before building a new view or restyling one, and stay here until the feature, fidelity, and personality are decided.

## Principles

- Design the next feature, not the application shell. Navigation, page width, and logo placement fall out of real screens. A share-file task needs a recipient, a note, an expiry, and a send action long before it needs a sidebar.
- Stay low-fidelity until the structure works. Ignore typefaces, shadows, and icons at the start. If the tool keeps pulling you into detail, sketch with a fat marker or block boxes in grayscale. Color comes after spacing, size, and contrast already explain the screen.
- Treat mockups as disposable. Ship a working slice instead of specifying every edge case up front. Design the smallest useful version, build it, then design the next feature. Drop anything you are not ready to implement. A notes field without attachments is shippable; a paperclip that implies attachments you will not build blocks the whole feature.
- Pick a personality on purpose and keep it. The concrete levers are type genre, color temperature, corner radius, and voice. A serious tool can use a neutral or serif face, near-zero radius, and plain language. A playful tool can use a rounded face, large radius, and casual labels. Do not mix sharp and very round corners in one product. Look at products your users already trust, and do not clone a direct competitor.
- Decide from a short list. Predefine type size, weight, line height, color, space, size, radius, border width, shadow, and opacity. When choosing, try the scale step you guess and its two neighbors. Two of the three are usually wrong. Add a new system the second time you hesitate over the same kind of value. Do not invent a one-off pixel.

## Defaults

Pick one personality and only its tokens:

| Personality | Type | Radius | Hue feel | Voice |
| --- | --- | --- | --- | --- |
| Plain product | Neutral system sans | 6px | Familiar blue or teal | Direct, no jokes |
| Formal | Serif for titles, neutral sans for UI | 0 | Ink, stone, a restrained gold or green | Complete sentences |
| Playful | Rounded sans | 16px | A clear non-corporate hue | Short, friendly |

Shared constraints until a topic skill replaces them:

- Spacing and size steps stay at least ~25% apart. Start from 16.
- Two weights only for UI text: 400–500 for body, 600–700 for emphasis. No weight under 400 below 20px.
- One radius for the product.
- Grayscale first: near-black, mid gray, light gray on an off-white canvas.

## Checklist

Apply this to the diff or the screenshot before any polish.

- [ ] The change is one feature a user can finish, not a new app frame.
- [ ] Controls that imply unbuilt behavior are gone.
- [ ] With color removed, size, weight, and space still show what matters.
- [ ] Personality is named, and radius, type genre, and tone match that one choice.
- [ ] New sizes, colors, and shadows are scale steps, not fresh arbitrary values.
- [ ] The next skill below is loaded only for a decision this change actually makes.

## Load a topic skill

| You are deciding | Load |
| --- | --- |
| What should stand out, labels, actions | `hierarchy` |
| Space, width, columns, grouping | `layout-spacing` |
| Font, measure, line height, alignment | `typography` |
| Palette, shades, contrast, status | `color` |
| Shadows, inset, overlap | `depth` |
| Photos, icons, avatars, uploads | `images` |
| Empty states, borders, accents, defaults | `finishing-touches` |
| Whether the screen is ready | `ui-review` |

For a pass over a whole screen, load `ui-review` and let it run the other checklists. Do not load every topic skill "just in case" on a one-line copy change.

## Example

A team is adding "schedule a workshop." The first mock is a full app: sidebar, top search, settings gear, and a calendar with drag-and-drop, waitlists, and file attachments. None of that is in this milestone.

After, the only UI is the feature, in grayscale, plain personality, 6px radius:

```html
<form style="max-width: 28rem; display: grid; gap: 1.5rem; font-family: system-ui, sans-serif; color: #1c2430">
  <header>
    <h1 style="font-size: 1.25rem; font-weight: 600; margin: 0">Schedule a workshop</h1>
    <p style="margin: 0.25rem 0 0; color: #5c6b7a">People get a calendar invite when you publish.</p>
  </header>
  <label>Title <input name="title" /></label>
  <label>When <input type="datetime-local" name="when" /></label>
  <label>Seats <input type="number" name="seats" min="1" /></label>
  <button type="submit" style="justify-self: start; background: #2a3340; color: white; border: 0; border-radius: 6px; padding: 0.5rem 0.75rem">
    Publish workshop
  </button>
</form>
```

Load `hierarchy` if the submit action is competing with secondary links, `layout-spacing` before tuning the gaps, and `color` only after the grayscale version reads clearly. Waitlist and attachments stay out until a later cycle.
