# Local behavior check on November 2, 2026

This run checks the behavior of the revised instructions on the three supplied assignments. It does not establish a general improvement in UI quality.

Fresh participants used `gpt-6.1-sol`, with no reasoning override, the same tools, identical requests, and identical source fixtures. A fresh guidance-assisted run followed checklist corrections, with the unchanged baseline output reused. An independent `gpt-6-astra` reviewer saw labeled outputs, fixtures, and criteria before learning the conditions. Raw outputs, source hashes, and review logs remain local and are not tracked in the repository.

## Observations

| Assignment | Baseline | With guidance |
| --- | --- | --- |
| Existing profile | Added an optional labeled field, reused product styling, and retained the POST form. | Did the same and tied token reuse and scope to named principles. |
| Phone booking form | Corrected fixed width, labeling, wrapping, and instruction colors. Left browser and server behavior unverified. | Did the same, explicitly identified the 20px regular text threshold, calculated contrast, and named the principles behind the changes. |
| Invoice review | Avoided the targeted false positives and suggested aligning the Amount heading with its numeric values. | Avoided the targeted false positives, retained valid product conventions, calculated text contrast, and named the principles behind its recommendations. Did not raise the optional heading-alignment refinement. |

The guidance-assisted booking notes connect `color / Measure text contrast` to changing white on `#888`, calculated at 3.54:1, to `#222` on `#eee`, calculated at 13.71:1. Both participants selected a biography limit without a supplied backend contract. Neither established server acceptance or persistence.

## Separate deterministic verification

- Structural validation passes all nine skills and their local links.
- The five declared reference text pairs meet 4.5:1. The lowest calculated ratio is 7.561:1.
- Eleven CLI tests pass, including deliberately broken links, unknown and cyclic tokens, low-contrast palette changes, and protection against overwriting prepared assignments.
- The browser reference page passes its four checks in headless Chrome. With the original typography CSS substituted, the local-ratio check fails. This demonstrates that the browser page detects the corrected override defect.

The browser run checks the CSS references, not the participant pages or their backend behavior.

## Limits

This is one retained output per condition and assignment. It demonstrates principle reporting and review restraint on these fixtures, not a repeatable quality gain.

Agents received no parent chat history. Harness tool descriptions and the global skill catalog remained available. Full tool transcripts were not inspected, so skill-loading sequences are unverified. A final prose pass softened three checklist statements and normalized blank lines after the guidance snapshot. Re-run the assignments to assess that exact final text or a different model.
