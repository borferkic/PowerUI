# Color tokens

PowerUI is dark only. All colors are fixed constants (there are no user themes), which keeps every screen consistent.

## Base tokens

| Token | Value | Use |
|---|---|---|
| `background` | `#0A0A0A` | Screen background |
| `card` | `#171717` | Cards and the top bar |
| `secondary` | `#262626` | Secondary buttons, active tab, bar track, icon tile |
| `foreground` | `#FAFAFA` | Primary text |
| `muted` | `#A1A1A1` | Labels and status icons |
| `border` | white at 10 % | 1 px border on cards and buttons |
| `accent` (`primary`) | `#4ADE80` | Progress, active state, primary button |
| `destructive` | `#FF6467` | Stop, emergency stop, errors, delete |
| `warning` | `#FBBF24` | Warnings (for example a missing camera or filament) |

## Data series

Colors that identify a measured value, used on bars and icons:

| Series | Value |
|---|---|
| Extruder | `#F87171` |
| Bed | `#C084FC` |
| Chamber / camera | `#60A5FA` |

These are the only colors, besides the accent, that may appear next to each other in the same card.

## States

| State | Rule |
|---|---|
| Active / selected | Soft accent: background `accent` at 14 %, border `accent` at 50 %, text `accent` |
| Primary button | Background `accent`, text `#052E16` |
| Pressed | Slightly darker background of the same variant |
| Disabled | Opacity 45 % |
| Destructive | Text and border in `destructive`, card background |

## Rules of use

- One accent per screen area: do not mix several accent colors.
- Red is reserved for destructive actions and errors.
- Text on the accent background is always the dark green `#052E16`, never white.
- Colors that come from the printer (for example the color of a filament spool) are the only exception to the palette.
