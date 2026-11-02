---
name: design-mode
description: Use when starting a screen, feature, or visual redesign, before picking chrome, colors, or decoration. Sets feature-first scope, grayscale structure, personality, and constrained tokens, then tells you which topic skill to load.
---

# Design mode

**Trigger:** Load this before building a new view or restyling one, and stay here until the feature, fidelity, and personality are decided.

## Apply this skill

Follow the user's requirements and the project's existing design system first. Use these defaults where the project leaves a choice open. Treat a departure as a finding only when you can show a usability, accessibility, or consistency problem.

## Principles

- **Feature before shell.** Design the next feature, not the application shell. Navigation, page width, and logo placement fall out of real screens. A share-file task needs a recipient, a note, an expiry, and a send action long before it needs a sidebar.
- **Structure before decoration.** Stay low-fidelity until the structure works. Ignore typefaces, shadows, and icons at the start. If the tool keeps pulling you into detail, sketch with a fat marker or block boxes in grayscale. Color comes after spacing, size, and contrast already explain the screen.
- **Ship the useful slice.** Treat mockups as disposable. Ship a working slice instead of specifying every edge case up front. Design the smallest useful version, build it, then design the next feature. Drop anything you are not ready to implement. A notes field without attachments is shippable; a paperclip that implies attachments you will not build blocks the whole feature.
- **Choose a coherent personality.** Pick a personality on purpose and keep it. The concrete levers are type genre, color temperature, corner radius, and voice. A serious tool can use a neutral or serif face, near-zero radius, and plain language. A playful tool can use a rounded face, large radius, and casual labels. Use the project's radius roles consistently. Different roles can use different radii, such as a pill badge and a rectangular panel. Look at products your users already trust, and do not clone a direct competitor. When you name a family, paste the matching `font-family` from [typography](../typography/SKILL.md) after it.
- **Constrain repeated decisions.** Decide from a short list. Predefine type size, weight, line height, color, space, size, radius, border width, shadow, and opacity. When choosing, try the scale step you guess and its two neighbors. Two of the three are usually wrong. Add a new system the second time you hesitate over the same kind of value. Prefer an existing token. Add a value when the content, optical alignment, or a documented product requirement earns the exception.

## Defaults

When the project has no established direction, use one of these starting points:

| Personality | Type | Radius | Hue feel | Voice |
| --- | --- | --- | --- | --- |
| Plain product | System UI | 6px | Familiar blue or teal | Direct, no jokes |
| Formal | Transitional for titles, System UI for UI | 0 | Ink, stone, a restrained gold or green | Complete sentences |
| Playful | Rounded Sans | 16px | A clear non-corporate hue | Short, friendly |

Shared constraints until a topic skill replaces them:

- Spacing and size steps stay at least ~25% apart. Start from 16.
- Two weights only for UI text: 400–500 for body, 600–700 for emphasis. No weight under 400 below 20px.
- A small set of radius roles, reused consistently.
- Grayscale first: near-black, mid gray, light gray on an off-white canvas.

## Checklist

Apply this to the diff or the screenshot before any polish.

- [ ] The scope serves the requested task. New application chrome has a concrete purpose in that task.
- [ ] Controls that imply unbuilt behavior are gone.
- [ ] With color removed, size, weight, and space still show what matters.
- [ ] Type, radius roles, and tone fit the established product or a named direction for a new product.
- [ ] Repeated sizes, colors, and shadows use project tokens. Any additions have a concrete purpose.
- [ ] The next skill below is loaded only for a decision this change actually makes.

## Load a topic skill

| You are deciding | Load |
| --- | --- |
| What should stand out, labels, actions | [hierarchy](../hierarchy/SKILL.md) |
| Space, width, columns, grouping | [layout-spacing](../layout-spacing/SKILL.md) |
| Font, measure, line height, alignment | [typography](../typography/SKILL.md) |
| Palette, shades, contrast, status | [color](../color/SKILL.md) |
| Shadows, inset, overlap | [depth](../depth/SKILL.md) |
| Photos, icons, avatars, uploads | [images](../images/SKILL.md) |
| Empty states, borders, accents, defaults | [finishing-touches](../finishing-touches/SKILL.md) |
| Whether the screen is ready | [ui-review](../ui-review/SKILL.md) |

For a pass over a whole screen, load [ui-review](../ui-review/SKILL.md) and let it run the other checklists. Do not load every topic skill "just in case" on a one-line copy change.

## Output

In your final response, name the principles from this skill that changed a material choice and state the choice each changed. Use `skill / Principle name` with a short explanation. Cite only skills you read, and omit principles that did not affect the work.

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

Load [hierarchy](../hierarchy/SKILL.md) if the submit action is competing with secondary links, [layout-spacing](../layout-spacing/SKILL.md) before tuning the gaps, and [color](../color/SKILL.md) only after the grayscale version reads clearly. Waitlist and attachments stay out until a later cycle.
