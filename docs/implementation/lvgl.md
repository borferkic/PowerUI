# Implementing PowerUI with LVGL

This guide maps the PowerUI components to LVGL 8 objects and lists the problems found while building the reference
implementation, [PowerScreen](https://github.com/borferkic/K1C-CFS-POWER-SCREEN).

## 1. Define the tokens once

Declare the colors as constants (`COLOR_BG`, `COLOR_CARD`, `COLOR_SECONDARY`, `COLOR_FG`, `COLOR_MUTED`, `COLOR_ACCENT`,
`COLOR_DESTRUCTIVE`, `COLOR_WARNING`) and the sizes as helpers. Never write a color literal inside a screen file.

If the display can run at different resolutions, wrap every pixel value in a scaling helper (`px(12)`) so the layout follows
the screen size.

## 2. Components → LVGL

| Component | LVGL construction |
|---|---|
| Card | `lv_obj` with background `#171717`, radius 14, 1 px border (white 10 %), no shadow, padding 16–20 |
| Button | `lv_btn` (or a styled `lv_obj`) with radius 10, one shared style per variant, an icon image and a label |
| Icon tile | `lv_obj` 40–64 px, `secondary` background, radius 10, an image centered |
| Badge | `lv_obj` pill 24 px high with a border, a 7 px dot and a 12 px label |
| Progress | `lv_bar` 8 px high, track `secondary`, indicator `accent` |
| Segmented group | `lv_btnmatrix` with `LV_BTNMATRIX_CTRL_CHECKABLE` and `lv_btnmatrix_set_one_checked`, styled on the items part |
| Switch | `lv_switch` 46 × 26 |
| Select | `lv_dropdown` 40 px high |
| List row | `lv_obj` 56 px high with an image and two labels |
| Dialog | an overlay on the top layer (`lv_layer_top`) with a 60 % black background and a centered card |

## 3. Layout

- Use `LV_GRID_FR(1)` columns and rows with a 12 px gap for menus and card grids.
- Reserve the frame once (top bar and sidebar) and make every panel a child of the content area, so panels never need to know
  about the bars.
- Panels that open on top of another keep a small stack so that Back returns to the previous panel.

## 4. Icons

- Export icons as white masks with alpha and tint them with `lv_obj_set_style_img_recolor` and
  `lv_obj_set_style_img_recolor_opa(…, LV_OPA_COVER, …)`.
- `lv_imgbtn` cannot be zoomed. To show a small icon in a button built from an image button, hide the image button and add a
  separate `lv_img` with `lv_img_set_zoom(256 * target / natural)`.
- Generate assets at 4× and scale them down: a direct 32 px render looks jagged.

## 5. Pitfalls found

| Problem | Cause | Fix |
|---|---|---|
| Segmented options show as one dark band with square corners | The widget that wraps the button matrix keeps the default theme background and shows between the cells | Make that container transparent (`bg_opa`, border, shadow and outline to 0); the card behind provides the background |
| Large numbers make the binary grow | A full-size font includes every glyph | Generate a font with `lv_font_conv` limited to the characters you need |
| Text is clipped in long names | The final font is wider than the mockup font | Use ellipsis and test with the longest names |
| A button looks fine in the emulator but a faint shape is invisible on the printer | Very low opacity values on real panels are crushed by the display's black level | Keep decorative elements at 10 % or more and check them on the real display |
| A panel opens behind the sidebar | The panel was created as a child of the screen, not of the content area | Create every panel inside the content area |

## 6. Verification

- Build an emulator or simulator and compare each screen with the reference image at 1:1.
- Check the longest names, the disabled states and the pressed states of every component.
- Always check on the real display before calling a screen finished: colors and contrast differ from a monitor.
