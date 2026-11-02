Replaced the fixed 600px form width with a fluid width capped at 600px. Stacked the date label above its input, removed forced no-wrap text, and allowed the long submit label to wrap. Border-box sizing and constrained controls keep padding inside the available form width. Replaced the white-on-gray instruction text with dark text on a light gray background for readability, and added a visible keyboard focus outline.

Associated the date label with its control using for/id. Kept the datetime-local input, starts_at field name, POST to /bookings, and submit button behavior.

Checked source attributes and responsive CSS. No browser/device rendering, translated-content rendering, native date-picker sizing, keyboard/screen-reader interaction, or server submission checks were run. Those remain necessary to confirm the result on narrow phones.
