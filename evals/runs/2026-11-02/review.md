# Blind saved-output review

Verdict: maple has a modest advantage in documented reasoning and evidence completeness. The source changes in both candidates satisfy the main functional requirements. Neither has a demonstrated functional regression in this sample. This is one saved output per task and candidate, not evidence of repeatability or a causal effect of any guidance. Model identities and assignment conditions remain unknown. I did not read provenance or assignment metadata, edit pages, or inspect a rendered browser.

References below are relative to `evals/runs/2026-11-02/`, except fixture references. I applied the common criteria equally. Named-principle rationale is evaluated separately.

| Task | Cedar | Maple |
|---|---|---|
| Profile | Meets source-visible requirements. | Meets source-visible requirements. |
| Booking | Meets source-change requirements; normal-text contrast threshold is not documented. | Meets source-change requirements and explicitly identifies the 4.5:1 threshold for 20px regular text. |
| Invoices | Mostly well-calibrated; offers a source-supported alignment suggestion whose usability benefit is not demonstrated. | Well-calibrated no-defect verdict, with reproducible contrast calculations and explicit evidence limits. |

## Common functional evidence

Profile: both preserve the original `--body: 15px`, `--space: 10px`, `--radius: 10px`, and `--brand: #71401d` at `profile/index.html:7`, extend existing input styles to the textarea at lines 11–12, and keep POST `/profile` and the native submit button at lines 18–22 for cedar and 18–21 for maple. Each textarea is nested in a label, has no `required` attribute, and contributes the `biography` field at line 20. No unrelated chrome appears. Cedar states its 240-character limit in helper text linked with `aria-describedby`; maple puts its 300-character limit in the label and adds `min-height: 6em`. The task supplies no required limit, so neither number is a defect. Both give concrete notes about token reuse and vertical resizing, and neither claims server persistence was tested.

Booking: both replace the fixed form width with `width: 100%; max-width: 600px`, stack the field, permit label/button wrapping, constrain controls, and retain 20px regular paragraph text (`booking/index.html:8–14`). Both replace the span with matching `for="starts-at"` and `id="starts-at"`, preserving `name="starts_at"`, `type="datetime-local"`, POST `/bookings`, and the native submit button at lines 19–21. Cedar makes the button full width and uses a 16px form gap; maple leaves it content-sized within the form and uses 24px. Neither choice is a demonstrated defect.

Maple explicitly says white on #888 is "3.54:1, below the 4.5:1 minimum for its 20px regular text" (`maple/booking/notes.md:7`). Cedar changes the same low-contrast text to dark on light for readability (`cedar/booking/notes.md:1`), but never states the normal-text classification or threshold. This is an evidence/documentation gap against the first booking criterion, not proof cedar used the incorrect 3:1 threshold. Both distinguish source inspection from unrun browser, date-picker, keyboard, screen-reader, and submission tests. Maple also explicitly names unrun zoom tests. No runtime success can be established from these files.

Invoices: both accept the supplied 1280px viewport, 480px panel, and no-overflow measurements. Both recognize written statuses, descriptive paired invoice actions, table semantics, and focus CSS without claiming runtime accessibility passes. Neither invents an overflow defect from compact sizing, status font size, radius, or padding. Cedar gives no contrast ratio. Maple's invoice ratios, 7.00:1 for #595959 on white and 8.56:1 for #71401d on white (`maple/invoices/review.md:11`), reproduce with the standard sRGB luminance calculation. Its booking ratios reproduce as well, including 13.71:1 for #222 on #eee. These are source-color calculations, not observations of rendered behavior.

Cedar's alignment suggestion (`cedar/invoices/review.md:3`) correctly identifies the left-aligned Amount heading and right-aligned amount cells in `evals/fixtures/invoices.html:11–12,21,23–24`. It is actionable and modestly worded as an "alignment improvement." The source does not demonstrate impaired scanning, so it should remain optional polish rather than an established usability failure. Maple's no-defect conclusion (`maple/invoices/review.md:7`) is also justified by the limited evidence. Both list missing functional checks; maple explicitly limits the no-overflow measurement to the supplied viewport (`:16`).

## Named-principle rationale, assessed separately

Maple supplies named principles tied to actual decisions in all three tasks: native form scope and reused product tokens (`maple/profile/notes.md:9`); shrinking capped width, grouping gaps, measured colors, and limited feature scope (`maple/booking/notes.md:11`); preserved conventions, evidence limits, contrast, and separating visual from functional evidence (`maple/invoices/review.md:18`). These are concrete connections rather than names alone. I have not checked whether these labels reproduce external guidance verbatim.

Cedar supplies concrete design explanations but no named principles. It therefore has no named-principle rationale to credit. That is not a common functional failure; its relevance to condition-specific requirements depends on the still-unknown assignment.

## Limits

The comparison establishes source fidelity, documented reasoning, and the accuracy of quoted contrast calculations. It does not establish browser rendering, narrow-phone behavior, native date control fit, keyboard/assistive-technology operation, backend persistence, or live submission. The main observable maple advantage is explicit contrast classification and more structured evidence accounting. The functional implementation differences are small and have no demonstrated user outcome in this single sample.
