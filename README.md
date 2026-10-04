<p align="center">
  <img src="assets/logo/powerui-logo-horizontal-dark.svg#gh-dark-mode-only" alt="PowerUI" height="64" />
  <img src="assets/logo/powerui-logo-horizontal-light.svg#gh-light-mode-only" alt="PowerUI" height="64" />
</p>

# PowerUI

PowerUI is a dark, card-based design system for touch displays that control 3D printers running **Klipper**. It was
structured, created and standardized for 3D printing by **Boris Fernández (Boris SdK)**, and it is based on the design
principles of [shadcn/ui](https://github.com/shadcn-ui/ui).

This repository contains **instructions only**: the design tokens, the layout grid, the component specifications and a
step-by-step guide to implement them in your own project. It does not contain application code. The reference
implementation is [PowerScreen](https://github.com/borferkic/K1C-CFS-POWER-SCREEN), a touch screen UI for the Creality K1C
built with [LVGL](https://github.com/lvgl/lvgl).

> PowerUI is intended for Creality K1 series printers with root access, but the guidelines apply to any small Klipper
> display (the reference layout is 800 × 480 px).

## What is inside

| Folder | Content |
|---|---|
| [`docs/foundations`](docs/foundations) | Color tokens, typography, spacing and layout grid, iconography |
| [`docs/components`](docs/components) | Cards, buttons, segmented groups, switches, badges, lists, dialogs and their states |
| [`docs/implementation`](docs/implementation) | How to build the components with LVGL, and the pitfalls found along the way |
| [`docs/screens`](docs/screens) | Reference layout of each screen type (work in progress) |
| [`assets/logo`](assets/logo) | PowerUI logo in SVG (horizontal, stacked and symbol; dark and light) |

## Design principles

1. **Dark first.** Near-black background, slightly lighter cards, a single green accent.
2. **Cards on a grid.** A 4 px base unit, 12 px outer margin and 12 px gap between any two elements.
3. **One accent.** Green means active, selected or primary. Red is only for destructive actions.
4. **Line icons, tinted by code.** Icons are single-color masks tinted with the text or accent color.
5. **Touch first.** Targets are large (usually 44–60 px high) and states are visible without hover.

## Status

Work in progress. The foundations and the component list are written; the screen references and the LVGL guide are being
completed while PowerScreen is finished.

## License and credits

PowerUI is licensed under [CC BY-NC 4.0](LICENSE.md): free to use by people and not for commercial purposes. Use by
companies for commercial purposes requires the permission of the author. Keep the credit when you reuse it.

PowerUI builds on [shadcn/ui](https://github.com/shadcn-ui/ui) by [shadcn](https://github.com/shadcn) (MIT); thank you for
its UI guidelines, which made it possible to build PowerUI. See [NOTICE.md](NOTICE.md) for all the credits.
