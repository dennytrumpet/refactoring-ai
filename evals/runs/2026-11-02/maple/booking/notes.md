# Booking notes

Replaced the fixed 600px width with a fluid width capped at 600px. The label and date control now stack with an 8px internal gap, and the submit action is separated by 24px. Labels and button text can wrap, including long unbroken translations; controls use border-box sizing and stay within the form width.

Replaced the unassociated span with a visible label linked to the date control. Preserved `starts_at`, `datetime-local`, the POST to `/bookings`, the submit button, and the existing copy. Added a visible keyboard-focus outline.

The instruction paragraph now uses #222 on #eee (calculated 13.71:1), replacing white on #888 (3.54:1, below the 4.5:1 minimum for its 20px regular text).

Checked source structure, label association, submission attributes, wrapping rules, and calculated sRGB contrast. No rendered phone, translation, zoom, native date-picker, keyboard, screen-reader, or server submission tests were run; these still need verification in supported browsers.

Principles applied: `layout-spacing / Match sizing to the region` changed the fixed width to a shrinking capped form; `layout-spacing / Space explains grouping` separated the field from its action; `color / Measure text contrast` changed the instruction colors; `design-mode / Feature before shell` kept the work within the existing booking form.
