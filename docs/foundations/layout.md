# Layout and spacing

The reference display is **800 × 480 px**.

## Grid

- Base unit **4 px**.
- **Outer margin 12 px** and **gap 12 px** between any two elements.
- Card padding 16–20 px.
- Equal columns use fractional units (`LV_GRID_FR(1)` in LVGL) with a 12 px gap; the toolkit distributes the remaining pixels.

## Frame

| Element | Size |
|---|---|
| Top bar | 40 px high, full width, `card` background with a bottom border; 16 px side padding (8 px on the left when it holds Back) |
| Sidebar | 64 px wide, always visible, even when a panel is open; icons of 32 px inside 52 px tiles |
| Content area | **With** the sidebar: x 76 → 788 (**712 px**). **Without** it: x 12 → 788 (776 px). In both cases y 52 → 468 (**416 px**) |

Top bar contents: the logo only on the home screen; on every other screen a bold centered title. A gray **‹ Back** pill on the
left when a panel is open. On the right: camera, filament and Wi-Fi status icons (gap 16) and the clock.

## Radii and borders

| Element | Radius |
|---|---|
| Card | 14 |
| Button | 10 |
| Icon tile | 10 |
| Badge and pill-shaped chips | fully rounded |

Borders are always 1 px. There are no shadows.

## Touch targets

- Buttons are at least 44 px high; the common sizes are 44, 52 and 60 px.
- Rail buttons (side columns) are 95–140 px high with a small icon above a label.
- Keep 12 px between touch targets so that a finger cannot hit two at once.
