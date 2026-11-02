# Local behavior check on November 2, 2026

This run checks the behavior of the revised instructions on the three supplied assignments. It does not establish a general improvement in UI quality.

Two fresh participants used `gpt-6.1-sol`, with no reasoning override, the same tools, identical task requests, and identical source fixtures. Cedar received the baseline folder. Maple received the guidance folder. A first paired run was followed by a fresh Maple run after checklist corrections; the baseline output was reused because its requests and fixtures were unchanged. An independent `gpt-6-astra` reviewer saw only output labels, original fixtures, and criteria before receiving the condition mapping.

The final saved outputs are in [the run folder](runs/2026-11-02). [Provenance](runs/2026-11-02/provenance.json) records source hashes, configuration limits, baseline reuse, and the guidance snapshot. [The independent review](runs/2026-11-02/review.md) records the artifact-level judgments. Participant notes remain verbatim evidence.

## Observations

| Assignment | Baseline | With guidance |
| --- | --- | --- |
| Existing profile | Added an optional labeled field, reused product styling, and retained the POST form. | Did the same and tied token reuse and scope to named principles. |
| Phone booking form | Corrected fixed width, labeling, wrapping, and instruction colors. Left browser and server behavior unverified. | Did the same, explicitly identified the 20px regular text threshold, calculated contrast, and named the principles behind the changes. |
| Invoice review | Avoided the targeted false positives and suggested aligning the Amount heading with its numeric values. | Avoided the targeted false positives, retained valid product conventions, calculated text contrast, and named the principles behind its recommendations. Did not raise the optional heading-alignment refinement. |

Maple's booking notes connect `color / Measure text contrast` to changing white on `#888`, calculated at 3.54:1, to `#222` on `#eee`, calculated at 13.71:1. Its invoice review recognizes “Overdue” and “Due Friday” as status words and keeps the documented 13px metadata, 10px spacing, and 10px radii.

Both participants selected a biography character limit without a supplied backend contract. Both preserved the form action and method in HTML. Neither established that a server accepts or persists the new field. The source artifacts support those bounded observations.

## Separate deterministic verification

- Structural validation passes all nine skills and their local links.
- The five declared reference text pairs meet 4.5:1. The lowest calculated ratio is 7.561:1.
- Eleven CLI tests pass, including deliberately broken links, unknown and cyclic tokens, low-contrast palette changes, and protection against overwriting prepared assignments.
- The browser reference page passes its four checks in headless Chrome. With the original typography CSS substituted, the local-ratio check fails. This demonstrates that the browser page detects the corrected override defect.

[Saved browser results](runs/2026-11-02/css-reference.json) preserve the actual values. This browser run checks the CSS references, not the participant pages or their backend behavior.

## Limits

This is one baseline output and one retained guidance-assisted output per assignment. It shows principle reporting and the requested review restraint on these fixtures. Both participants produced useful implementation changes. The comparison does not establish a repeatable quality gain, and principle names alone are not evidence of better UI.

Fresh agents received no parent chat history and were told to stay within their assignment folders. Harness tool descriptions and the global skill catalog could not be removed. Full participant tool transcripts were not inspected, so this report does not claim verified skill-loading sequences. A final prose pass softened three remaining checklist statements and normalized blank lines after the saved guidance snapshot. Re-run the prepared assignments when assessing that exact final text or a different model.
