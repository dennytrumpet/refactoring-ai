#!/usr/bin/env python3
"""Measure the explicit text pairs in skills/color/SKILL.md, without CSS cascade inference."""

import argparse
import math
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)"


def color(value, tokens, trail=()):
    value = value.strip().lower()
    variable = re.fullmatch(r"var\((--[\w-]+)\)", value)
    if variable:
        name = variable[1]
        if name in trail:
            raise ValueError(f"variable cycle: {' -> '.join((*trail, name))}")
        if name not in tokens:
            raise ValueError(f"unknown token {name}")
        return color(tokens[name], tokens, (*trail, name))
    value = {"white": "#ffffff", "black": "#000000"}.get(value, value)
    if re.fullmatch(r"#(?:[0-9a-f]{3}|[0-9a-f]{6})", value):
        digits = value[1:]
        if len(digits) == 3:
            digits = ''.join(c * 2 for c in digits)
        channels = [int(digits[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        return tuple(c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels)
    match = re.fullmatch(rf"oklch\(({NUMBER})(%?)\s+({NUMBER})\s+({NUMBER})(?:deg)?\)", value)
    if not match:
        raise ValueError(f"unsupported color {value!r}")
    lightness, chroma, hue = float(match[1]), float(match[3]), math.radians(float(match[4]))
    lightness /= 100 if match[2] else 1
    if not 0 <= lightness <= 1 or chroma < 0:
        raise ValueError(f"invalid OKLCH color {value!r}")
    a, b = chroma * math.cos(hue), chroma * math.sin(hue)
    l = (lightness + .3963377774 * a + .2158037573 * b) ** 3
    m = (lightness - .1055613458 * a - .0638541728 * b) ** 3
    s = (lightness - .0894841775 * a - 1.2914855480 * b) ** 3
    rgb = (4.0767416621*l - 3.3077115913*m + .2309699292*s,
           -1.2684380046*l + 2.6097574011*m - .3413193965*s,
           -.0041960863*l - .7034186147*m + 1.7076147010*s)
    if any(not math.isfinite(c) or c < -1e-6 or c > 1 + 1e-6 for c in rgb):
        raise ValueError(f"out-of-sRGB color {value!r}")
    return tuple(min(1, max(0, c)) for c in rgb)


def load(text):
    css = '\n'.join(re.findall(r"(?ms)^```css\s*\n(.*?)^```\s*$", text))
    tokens = dict(re.findall(r"(--[\w-]+)\s*:\s*([^;{}]+);", css))
    section = re.search(r"(?m)^## Verified text pairs\s*$", text)
    if not section:
        raise ValueError("missing '## Verified text pairs' table")
    section = re.split(r"(?m)^## ", text[section.end():], maxsplit=1)[0]
    lines = [line.strip() for line in section.splitlines() if line.strip().startswith('|')]
    if len(lines) < 3 or [c.strip() for c in lines[0].strip('|').split('|')] != ['Foreground', 'Background', 'Minimum']:
        raise ValueError("verified text pairs needs Foreground | Background | Minimum and rows")
    rows = []
    for line in lines[2:]:
        cells = [c.strip().strip('`') for c in line.strip('|').split('|')]
        if len(cells) != 3:
            raise ValueError(f"invalid contrast row {line!r}")
        foreground, background, minimum = cells
        minimum = float(minimum)
        if not math.isfinite(minimum) or not 1 <= minimum <= 21:
            raise ValueError(f"invalid minimum {minimum}")
        rows.append((foreground, background, minimum))
    return tokens, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = []
    try:
        tokens, rows = load((args.root / 'skills/color/SKILL.md').read_text(encoding='utf-8'))
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    for foreground, background, minimum in rows:
        try:
            luminances = [sum(c*w for c, w in zip(color(v, tokens), (.2126, .7152, .0722))) for v in (foreground, background)]
            ratio = (max(luminances) + .05) / (min(luminances) + .05)
            print(f'{foreground} on {background}: {ratio:.3f}:1 (minimum {minimum:g}:1)')
            if ratio < minimum:
                errors.append(f'{foreground} on {background}: contrast below {minimum:g}:1')
        except ValueError as error:
            errors.append(f'{foreground} on {background}: {error}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
    return int(bool(errors))


if __name__ == '__main__':
    sys.exit(main())
