# Profile notes

Added a labeled, optional biography textarea, limited to 300 characters with the limit stated in its label. It uses the existing font, 10px spacing, radius, border, and focus treatment, and supports vertical resizing.

The existing POST to `/profile`, display-name field, and Save profile button remain. The textarea submits as `biography` in that form. Server storage is not supplied, so persistence has not been verified.

Source checks verified the optional field, native label association, character limit, and unchanged submission attributes. No browser, keyboard, screen-reader, or backend tests were run.

Principles applied: `design-mode / Ship the useful slice` kept this to a native field in the existing form. `design-mode / Constrain repeated decisions` reused the product tokens rather than introducing a new style.
