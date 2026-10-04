# Typography

## Sizes (px)

| Size | Use |
|---|---|
| 88 | The large progress number |
| 40 | Version numbers |
| 24–26 | Values (temperatures, positions) |
| 16 | Titles and button labels |
| 14 | Body text |
| 13 and 12 | Secondary text, hints and badges |

## Typeface

- The reference mockups use a neutral sans-serif (Segoe UI). The reference implementation uses **Montserrat**, which is wider:
  check for clipped text in long names and use an ellipsis (`…`).
- The logo wordmark uses **Orbitron Bold** (OFL). It is only used in the logo, never in the interface.
- Numbers use tabular figures so that values do not jump while they change.

## Rules

- Titles are bold, body text is regular, secondary text uses the `muted` color.
- Labels of buttons use title case (`Manual color`, `Load`, `Cooldown`), not all caps.
- Very large sizes (88 and 40 px) must come from a font generated with `lv_font_conv`, limited to the characters that are
  needed, so that the binary does not grow.
