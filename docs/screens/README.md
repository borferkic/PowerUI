# Screens

Reference layouts for the screen types of a Klipper display, built from the PowerUI components. This section is a work in
progress: each screen will get a page with its structure, measurements and states, and a reference image.

All screens use the same [frame](../foundations/layout.md#frame): a top bar, a sidebar and a content area of 712 × 416 px.

| Screen | Structure |
|---|---|
| Home | A large print card on the left; three temperature cards, a status chip and four quick buttons on the right |
| Menu (Calibrations, Settings) | A grid of menu cards, four columns by two rows |
| Files | Left: a Local / USB selector, a toolbar and a list of rows. Right: a detail card with preview, data and actions |
| Print status | Left: job card with Pause and Cancel and a large progress. Right: temperature and motion cards. Bottom: Tune, Objects and Stop |
| Filament | Left rail (Manual color, Load, Unload, Cooldown), three segmented groups in the center, right rail (Extrude, Retract) |
| Movement | An XY cross with a Z column and an actions column; a distance selector and an emergency stop below |
| Settings / System | Cards with preference rows (label and control) |
| Tools (Input shaper, Limits, Belts) | Tool cards with a chart or sliders, a switch and action buttons |
| Dialogs | A centered card over a 60 % overlay |

Pages and images will be added here as each screen is documented.
