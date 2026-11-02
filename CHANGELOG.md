# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Named principles and decision notes in the output of every skill.
- Local-link validation, calculated reference contrast checks, and checker tests in CI.
- Paired UI assignments for product consistency, review restraint, and mobile form fixes.
- A browser page that checks the fluid typography reference.

### Changed

- Existing product tokens and user requirements take precedence over suggested defaults.
- Visual reviews require observed user impact and list functional accessibility checks separately.
- Empty-state guidance distinguishes first use from filtered results with no matches.

### Fixed

- Low-contrast metadata defaults and the WCAG large-text threshold.
- Unsupported findings in the invoice review example.
- The sRGB fallback example, undefined gray token names, and claims about derived gamut safety.
- Local fluid type overrides now recalculate dependent scale steps.

## [1.1.0] - 2026-10-30

### Added

- Modern Font Stacks fallbacks. A named family is followed by a copied stack from modernfontstacks.com.
- Fluid typography for marketing pages, articles, and headings. Dense app UI and data tables stay on the fixed scale.
- Derived OKLCH color ramps with semantic names, plus `color-mix` guidance for tint, hover, active, and overlay.

## [1.0.0] - 2026-10-30

### Added

- The initial nine skills, including `design-mode` and the topic skills for hierarchy, layout and spacing, typography, color, depth, images, finishing touches, and UI review.
