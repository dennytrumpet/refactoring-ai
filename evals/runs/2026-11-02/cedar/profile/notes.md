Added an optional, labeled biography textarea with a visible 240-character limit and native maxlength enforcement. It uses the existing typography, 10px padding and radius, border, focus treatment, and form spacing. Vertical resizing supports longer text.

The existing POST to /profile and Save profile button are unchanged; biography is submitted as an additional field. Checked the source for the label association, optional state, limit, and unchanged submission attributes. Browser rendering and server persistence have not been tested; the supplied folder contains no server implementation.
