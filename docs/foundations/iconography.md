# Iconography

## Style

- **Line icons**, single color, rounded caps and joins. The general set is [Lucide](https://lucide.dev/) (ISC).
- Icons are **masks**: white shapes on a transparent background that the code tints with the text or accent color. They
  are never delivered in color.
- Typical sizes: 18 px in the status bar, 20–24 px inside buttons, 32 px in the sidebar, 38–44 px above a label in rail
  buttons, 40 px inside an icon tile.

## Icon tile

An icon tile is a 40–64 px square with the `secondary` background and a 10 px radius, with the icon centered and tinted.
Menus use a 60 px tile with a 40 px icon.

## Meaning of colors

| Tint | Meaning |
|---|---|
| `foreground` | Normal action |
| `accent` | Active or primary action |
| `destructive` | Destructive action (stop, delete) |
| `muted` | Status or disabled |
| Series colors | The measured value they identify (extruder, bed, chamber) |

## Choosing an icon

1. The icon must say **what the action does**, not which screen it opens (Home All is a crosshair, not a house).
2. Two buttons on the same screen must never share the same icon.
3. A slash over an icon means *off* (Motor off).
4. When no icon exists, draw one with the same stroke width as Lucide (2 px at 24 px).

## Printer-specific icons

The reference implementation uses a separate set for printer symbols (nozzle, bed, filament spool). Those files belong to
their own project and are not part of PowerUI; use any set with the same single-color mask format.

## Generating LVGL assets

1. Draw the icon as an SVG on a 24 × 24 grid with a 2 px stroke.
2. Render it at 4× and scale it down to 32 or 64 px with a smoothing filter.
3. Export a white-on-transparent image in the format of your LVGL version (for example true color with alpha).
4. Tint it at runtime with `img_recolor` and `img_recolor_opa`.
