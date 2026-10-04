# Components

Specifications of the PowerUI components. Colors refer to the [tokens](../foundations/tokens.md) and sizes to the
[layout](../foundations/layout.md).

## Card

Background `card`, radius 14, 1 px `border`, no shadow, padding 16–20. A card groups one topic; do not nest cards.

## Buttons

| Variant | Background | Border | Text | Use |
|---|---|---|---|---|
| Outline | `card` | `border` | `foreground` | Normal action |
| Secondary | `secondary` | none | `foreground` | Back pill, neutral action |
| Soft | `accent` 14 % | `accent` 50 % | `accent` | Selected, or a positive action that is not the main one |
| Primary | `accent` | none | `#052E16` | The main action of the screen (one per screen) |
| Destructive | `card` | `destructive` 35 % | `destructive` | Stop, delete, emergency stop |

- Radius 10, height 44, 52 or 60 px. An optional icon of 20–24 px goes before the label with an 8 px gap.
- Disabled buttons use 45 % opacity. Pressed buttons darken their own background.
- **Rail button:** a taller button in a side column, with a 38–44 px icon above a title-case label.

## Segmented group

A row of equal buttons with 6–8 px gaps for choosing one option. The selected item uses the *soft* style; the others use the
`secondary` background without border. Each item has a 8 px radius, so the items read as separated cells.

## Switch

46 × 26 px. On: `accent` track with a `#052E16` knob. Off: `secondary` track with a `foreground` knob.

## Slider and progress bar

Track `secondary`, indicator `accent`, 8 px high (4–6 px inside small cards). Sliders add a round knob and, optionally, a
text *Reset* button on the right.

## Badge

A pill 24 px high with a 1 px border, a 7 px colored dot and a 12 px label. Used for states (Active, Offline, New, Archived).

## Select

A 40 px high outline button with a chevron on the right that opens a list.

## Icon tile

40–64 px square, `secondary` background, radius 10, tinted icon centered.

## List row

56 px high. A 40 px thumbnail or icon, a bold 14 px title and a 12 px `muted` detail. The selected row uses the
`secondary` background and an `accent` border.

## Dialog

A centered card over a 60 % black overlay, with a title, a short text and two buttons (Cancel on the left as outline, the
action on the right as primary or destructive). Tapping outside never confirms.

## Empty state

A 56 px icon tile, a 16 px title and a 12 px `muted` description, centered in the area that would hold the content.

## Menu card

Used in menu grids: a 60 px icon tile at the top left, an optional badge at the top right, and a bold 16 px title with a
12 px description at the bottom left. Four columns, two rows, 12 px gap.

## Status bar icons

Camera, filament and Wi-Fi, 18 px. Green means active and gray with a diagonal slash means inactive.
