"""Render the PowerUI reference images (components and screens) with Microsoft Edge in headless mode.

Self-contained: it only uses Lucide line icons (ISC) and plain HTML/CSS, so the images contain no third-party artwork.
Usage:  python tools/render_reference.py            (needs Microsoft Edge; set EDGE if it is installed elsewhere)
Output: docs/components/img/*.png and docs/screens/img/*.png
"""
import os
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
EDGE = os.environ.get('EDGE', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
TMP = os.path.join(ROOT, 'tools', '_tmp')

# ------------------------------------------------------------------ Lucide icons (24 x 24, stroke 2)
L = {
    'house': '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    'sliders': '<path d="M21 4h-7M10 4H3M21 12h-9M8 12H3M21 20h-5M12 20H3M14 2v4M8 10v4M16 18v4"/>',
    'folder': '<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>',
    'settings': '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
    'wifi': '<path d="M12 20h.01M2 8.82a15 15 0 0 1 20 0M5 12.859a10 10 0 0 1 14 0M8.5 16.429a5 5 0 0 1 7 0"/>',
    'camera': '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
    'chev-l': '<path d="m15 18-6-6 6-6"/>', 'chev-d': '<path d="m6 9 6 6 6-6"/>',
    'arrow-up': '<path d="m5 12 7-7 7 7M12 19V5"/>', 'arrow-down': '<path d="M12 5v14M19 12l-7 7-7-7"/>',
    'arrow-left': '<path d="m12 19-7-7 7-7M19 12H5"/>', 'arrow-right': '<path d="M5 12h14M12 5l7 7-7 7"/>',
    'crosshair': '<circle cx="12" cy="12" r="10"/><path d="M22 12h-4M6 12H2M12 6V2M12 22v-4"/>',
    'play': '<polygon points="6 3 20 12 6 21 6 3"/>', 'pause': '<rect x="14" y="4" width="4" height="16" rx="1"/><rect x="6" y="4" width="4" height="16" rx="1"/>',
    'square': '<rect x="3" y="3" width="18" height="18" rx="2"/>',
    'shield-alert': '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="M12 8v4"/><path d="M12 16h.01"/>',
    'thermo': '<path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/>',
    'fan': '<path d="M10.827 16.379a6.082 6.082 0 0 1-8.618-7.002l5.412 1.45a6.082 6.082 0 0 1 7.002-8.618l-1.45 5.412a6.082 6.082 0 0 1 8.618 7.002l-5.412-1.45a6.082 6.082 0 0 1-7.002 8.618l1.45-5.412Z"/><path d="M12 12v.01"/>',
    'check': '<path d="M20 6 9 17l-5-5"/>', 'x': '<path d="M18 6 6 18M6 6l12 12"/>',
    'refresh': '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    'trash': '<path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>',
    'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>',
    'layers': '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    'circle-dot': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="1"/>', 'hand': '<path d="M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2"/><path d="M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/>',
    'snow': '<path d="M2 12h20M12 2v20m-7-5 14-10M5 7l14 10"/>', 'download': '<path d="M12 15V3M7 10l5 5 5-5M5 21h14"/>', 'upload': '<path d="M12 3v12M7 8l5-5 5 5M5 21h14"/>',
    'power-off': '<path d="M18.36 6.64A9 9 0 0 1 20.77 15"/><path d="M6.16 6.16a9 9 0 1 0 12.68 12.68"/><path d="M12 2v4"/><path d="m2 2 20 20"/>',
    'slash': '<path d="m3 3 18 18"/>', 'info': '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>', 'refresh-cw': '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/>',
    'cpu': '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/>',
}

CSS = """:root{--bg:#0a0a0a;--card:#171717;--border:rgba(255,255,255,.1);--fg:#fafafa;--muted:#a1a1a1;--sec:#262626;--ok:#4ade80;--bad:#ff6467;--warn:#fbbf24}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Inter,Arial,sans-serif;background:var(--bg);color:var(--fg);position:relative;overflow:hidden;font-variant-numeric:tabular-nums}
.abs{position:absolute}.row{display:flex;align-items:center}.col{display:flex;flex-direction:column}.nw{white-space:nowrap}.muted{color:var(--muted)}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px}
.btn{display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid var(--border);font-weight:500}
.out{background:var(--card)}.sec{background:var(--sec);border-color:transparent}
.primary{background:var(--ok);color:#052e16;border-color:transparent;font-weight:600}
.soft{background:rgba(74,222,128,.14);border-color:rgba(74,222,128,.5);color:var(--ok)}
.destr{background:var(--card);color:var(--bad);border-color:rgba(255,100,103,.35)}
.dis{opacity:.45}
.badge{height:24px;padding:0 10px;border:1px solid var(--border);border-radius:999px;font-size:12px;font-weight:500;gap:6px;display:flex;align-items:center}
.prog{height:8px;border-radius:4px;background:var(--sec);overflow:hidden}.prog>i{display:block;height:100%;border-radius:4px;background:var(--ok)}
.tab{width:52px;height:52px;border-radius:10px;display:flex;align-items:center;justify-content:center;color:var(--muted)}.tab.on{background:var(--sec);color:var(--fg)}
.lbl{font-size:12px;font-weight:600;letter-spacing:.6px;color:var(--muted)}
.dim{position:absolute;font:11px Consolas,monospace;color:#7dd3fc}
"""

# ------------------------------------------------------------------ helpers
def ic(name, size=20, color='currentColor', sw=2):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" style="flex:none">{L[name]}</svg>')

def btn(label='', icon=None, kind='out', h=44, w=None, fs=15, gap=8, isz=20, col=False, style=''):
    st = f'height:{h}px;' + (f'width:{w}px;' if w else 'padding:0 18px;') + f'font-size:{fs}px;gap:{gap}px;' + ('flex-direction:column;' if col else '') + style
    return f'<div class="btn {kind}" style="{st}">{ic(icon, isz) if icon else ""}{("<span class=nw>" + label + "</span>") if label else ""}</div>'

def seg(options, active, h=44, fs=15, gap=8):
    items = ''.join(
        f'<div class="btn {"soft" if str(o) == str(active) else "sec"}" style="flex:1;height:{h}px;font-size:{fs}px;border-radius:8px;'
        f'font-weight:{600 if str(o) == str(active) else 500}">{o}</div>' for o in options)
    return f'<div class="row" style="gap:{gap}px;width:100%">{items}</div>'

def switch(on):
    return (f'<div style="width:46px;height:26px;border-radius:13px;background:{"var(--ok)" if on else "var(--sec)"};position:relative;border:1px solid var(--border);flex:none">'
            f'<div style="position:absolute;top:2px;left:{22 if on else 2}px;width:20px;height:20px;border-radius:50%;background:{"#052e16" if on else "#fafafa"}"></div></div>')

def badge(text, dot=None, color=None):
    d = f'<span style="width:7px;height:7px;border-radius:50%;background:{dot}"></span>' if dot else ''
    return f'<div class="badge nw" style="{f"color:{color};" if color else ""}">{d}{text}</div>'

def prog(pct, h=8):
    return f'<div class="prog" style="height:{h}px"><i style="width:{pct}%"></i></div>'

def tile(icon, size=40, isz=24, color='#fafafa'):
    return f'<div class="row" style="width:{size}px;height:{size}px;border-radius:10px;background:var(--sec);justify-content:center;flex:none">{ic(icon, isz, color)}</div>'

def model(size=56):
    return (f'<div style="width:{size}px;height:{size}px;border-radius:8px;background:#0a0a0a;border:1px solid var(--border);flex:none;padding:6px">'
            '<svg width="100%" height="100%" viewBox="0 0 100 100"><path d="M50 18 82 34v34L50 84 18 68V34z" fill="#d4d4d4"/><path d="M50 18 82 34 50 50 18 34z" fill="#fafafa"/><path d="M50 50 82 34v34L50 84z" fill="#a3a3a3"/></svg></div>')

def pos(x, y, w, h, inner, cls='card', style=''):
    return f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{inner}</div>'

def render(path, name, html, size=(800, 480)):
    out = os.path.join(ROOT, path)
    os.makedirs(out, exist_ok=True)
    os.makedirs(TMP, exist_ok=True)
    page = os.path.join(TMP, name + '.html')
    with open(page, 'w', encoding='utf-8') as f:
        f.write(f'<!doctype html><meta charset=utf-8><style>{CSS}html,body{{width:{size[0]}px;height:{size[1]}px}}</style><body>{html}</body>')
    subprocess.run([EDGE, '--headless', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    f'--screenshot={os.path.join(out, name + ".png")}', f'--window-size={size[0]},{size[1]}',
                    'file:///' + page.replace('\\', '/')], check=True, capture_output=True)
    os.remove(page)
    print('ok', path, name)

# ------------------------------------------------------------------ frame
M, G, SIDE, HEAD = 12, 12, 64, 40
X0, X1, Y0, Y1 = SIDE + M, 800 - M, HEAD + M, 480 - M     # 76, 788, 52, 468
CW, CH = X1 - X0, Y1 - Y0                                  # 712 x 416

def top_bar(title, back=False):
    left = f'<span class="nw" style="font-size:14px;font-weight:600">{title}</span>'
    if back:
        left = (f'<div class="row" style="gap:12px"><div class="btn sec" style="height:32px;padding:0 12px 0 8px;gap:4px;font-size:13px">{ic("chev-l", 18)}Back</div>'
                f'<span style="width:1px;height:16px;background:var(--border)"></span>{left}</div>')
    right = (f'<span class="row nw" style="gap:16px;font-size:13px"><span style="color:var(--ok);display:flex">{ic("camera", 18)}</span>'
             f'<span style="color:var(--ok);display:flex">{ic("circle-dot", 18)}</span><span style="color:var(--ok);display:flex">{ic("wifi", 18)}</span>'
             f'<span class="muted">22:59</span></span>')
    return (f'<div class="abs row" style="left:0;top:0;width:800px;height:{HEAD}px;background:var(--card);border-bottom:1px solid var(--border);'
            f'padding:0 16px {"0 8px" if back else ""};justify-content:space-between">{left}{right}</div>')

def sidebar(active):
    tabs = ''.join(f'<div class="tab {"on" if i == active else ""}">{ic(n, 32)}</div>' for i, n in enumerate(['house', 'sliders', 'folder', 'settings']))
    return (f'<div class="abs" style="left:0;top:{HEAD}px;bottom:0;width:{SIDE}px;border-right:1px solid var(--border);display:flex;flex-direction:column;'
            f'justify-content:space-around;align-items:center;padding:8px 0">{tabs}</div>')

def frame(title, active, body, back=False):
    return top_bar(title, back) + sidebar(active) + body

# ------------------------------------------------------------------ component images
def components():
    path = 'docs/components/img'
    W = 760
    # card
    render(path, 'card', pos(24, 24, 360, 150, f'<div class="col" style="padding:18px;gap:8px"><span style="font-size:16px;font-weight:600">Card title</span>'
           f'<span class="muted" style="font-size:14px">One topic per card. Background card, radius 14, 1 px border, no shadow.</span></div>')
           + pos(400, 24, 336, 150, f'<div class="col" style="padding:18px;gap:12px"><span class="lbl">TEMPERATURE</span><span style="font-size:24px;font-weight:600">220° <span class="muted" style="font-size:14px">/ 220°</span></span>{prog(72)}</div>'),
           (W, 200))
    # buttons
    row1 = '<div class="row" style="gap:12px">' + btn('Outline', 'play', 'out') + btn('Secondary', None, 'sec') + btn('Soft', 'check', 'soft') + btn('Primary', 'play', 'primary') + btn('Destructive', 'square', 'destr') + '</div>'
    row2 = '<div class="row" style="gap:12px">' + btn('Disabled', None, 'out dis') + btn('', 'trash', 'destr', w=44) + btn('', 'refresh', 'out', w=44) + btn('Back', 'chev-l', 'sec', h=32, fs=13, isz=18) + '</div>'
    rail = '<div class="row" style="gap:12px">' + ''.join(btn(t, i, 'out', h=95, w=140, col=True, gap=8, isz=38, fs=15) for t, i in (('Load', 'download'), ('Unload', 'upload'))) + btn('Cooldown', 'snow', 'out', h=95, w=140, col=True, gap=8, isz=38, fs=15, style='color:#60a5fa') + '</div>'
    render(path, 'buttons', f'<div class="col abs" style="left:24px;top:24px;gap:22px"><span class="lbl">VARIANTS</span>{row1}<span class="lbl">SIZES AND STATES</span>{row2}<span class="lbl">RAIL BUTTONS</span>{rail}</div>', (W, 380))
    # segmented
    render(path, 'segmented', f'<div class="col abs" style="left:24px;top:24px;gap:18px;width:{W - 48}px"><span class="lbl">SELECT ONE OPTION</span>{seg([1, 2, 5, 10, 25, 35, 50], 5, h=52)}'
           f'<span class="lbl">COMPACT</span>{seg(["Local", "USB"], "Local", h=40, fs=14)}</div>', (W, 220))
    # controls
    ctrl = (f'<div class="col abs" style="left:24px;top:24px;gap:22px;width:{W - 48}px"><span class="lbl">SWITCH</span><div class="row" style="gap:24px">{switch(True)}<span>On</span>{switch(False)}<span>Off</span></div>'
            f'<span class="lbl">PROGRESS BAR</span><div class="row" style="gap:14px"><div style="width:420px">{prog(60)}</div><span class="muted" style="font-size:13px">60 %</span></div>'
            f'<span class="lbl">SLIDER WITH RESET</span><div class="row" style="gap:14px"><div class="row" style="width:420px;height:20px;position:relative"><div style="width:100%">{prog(45, 6)}</div>'
            f'<div style="position:absolute;left:45%;width:20px;height:20px;border-radius:50%;background:#fafafa;margin-left:-10px"></div></div>{btn("Reset", None, "out", h=32, fs=13)}</div></div>')
    render(path, 'controls', ctrl, (W, 300))
    # badges, tiles, select
    bt = (f'<div class="col abs" style="left:24px;top:24px;gap:22px"><span class="lbl">BADGES</span><div class="row" style="gap:12px">{badge("Active", "var(--ok)", "var(--ok)")}{badge("Offline", "var(--bad)")}{badge("New", "var(--ok)")}{badge("Archived")}</div>'
          f'<span class="lbl">ICON TILES</span><div class="row" style="gap:12px">{tile("house")}{tile("sliders")}{tile("fan", 40, 24, "#60a5fa")}{tile("thermo", 40, 24, "#f87171")}{tile("wifi", 60, 40)}</div>'
          f'<span class="lbl">SELECT</span>{btn("Creality", None, "out", h=40, w=220, fs=14, style="justify-content:space-between;padding:0 12px")}</div>')
    render(path, 'badges-tiles-select', bt, (W, 330))
    # list row
    rows = ''.join(f'<div class="row" style="height:56px;padding:0 12px;gap:12px;border-radius:10px;{"background:var(--sec);border:1px solid rgba(74,222,128,.5);" if i == 1 else ""}">{model(40)}'
                   f'<div class="col" style="flex:1;gap:1px"><span style="font-size:14px;font-weight:600">{n}</span><span class="muted" style="font-size:12px">{d}</span></div>{badge(b, c, c) if b else ""}</div>'
                   for i, (n, d, b, c) in enumerate((('Benchy.gcode', '1 h 12 min · 14 g', '', None), ('Calibration cube.gcode', '38 min · 6 g', 'Printed', 'var(--ok)'), ('Bracket.gcode', '2 h 05 min · 31 g', '', None))))
    render(path, 'list-row', pos(24, 24, 480, 190, f'<div class="col" style="padding:8px;gap:2px">{rows}</div>'), (528, 240))
    # menu card + empty state
    mc = lambda ico, t, d, pill='': (f'<div class="card col" style="width:180px;height:200px;padding:14px;justify-content:space-between;position:relative">'
                                     f'<div class="abs" style="right:12px;top:12px">{pill}</div>{tile(ico, 60, 40)}<div class="col" style="gap:3px"><span style="font-size:16px;font-weight:600">{t}</span><span class="muted" style="font-size:12px">{d}</span></div></div>')
    es = (f'<div class="col" style="align-items:center;gap:8px;width:300px;padding-top:30px">{tile("file", 56, 32, "#a1a1a1")}<span style="font-size:16px;font-weight:600;margin-top:6px">No print history</span>'
          f'<span class="muted" style="font-size:12px;text-align:center">Finished prints appear here once Moonraker has recorded them.</span></div>')
    render(path, 'menu-card-empty-state', f'<div class="abs row" style="left:24px;top:24px;gap:12px;align-items:flex-start">{mc("wifi", "Wi-Fi", "Network")}{mc("info", "System", "Preferences and info", badge("New", "var(--ok)"))}{es}</div>', (W, 250))
    # dialog
    dlg = ('<div class="abs" style="inset:0;background:rgba(0,0,0,.6)"></div>'
           + pos(150, 130, 500, 220, f'<div class="col" style="padding:24px;height:100%;justify-content:space-between"><div class="col" style="gap:8px"><span style="font-size:20px;font-weight:600">Restart Klipper?</span>'
                 f'<span class="muted" style="font-size:14px">Klipper will restart. A running print is not affected until it pauses.</span></div>'
                 f'<div class="row" style="gap:12px">{btn("Cancel", None, "out", h=50, w=200)}{btn("Restart", None, "destr", h=50, w=240)}</div></div>', style='border-color:rgba(255,255,255,.18)'))
    render(path, 'dialog', f'<div class="abs" style="inset:0;background:#0a0a0a"></div>{dlg}', (800, 480))

# ------------------------------------------------------------------ screen images
def temp_card(y, name, ico, color, cur, tgt):
    return pos(496, y, 292, 60, f'<div class="row" style="height:100%;padding:0 12px;gap:12px">{tile(ico, 40, 24, color)}<div class="col" style="flex:1"><span class="muted" style="font-size:12px">{name}</span>'
               f'<span style="font-size:20px;font-weight:600">{cur}° <span class="muted" style="font-size:13px">/ {tgt}°</span></span></div></div>')

def screens():
    path = 'docs/screens/img'
    # frame with dimensions
    guides = (f'<div class="abs" style="left:{X0}px;top:{Y0}px;width:{CW}px;height:{CH}px;border:1px dashed #7dd3fc;border-radius:4px"></div>'
              f'<div class="dim" style="left:{X0 + 8}px;top:{Y0 + 6}px">content area {CW} x {CH} px (x {X0}..{X1}, y {Y0}..{Y1})</div>'
              f'<div class="dim" style="left:6px;top:{HEAD + 4}px;color:#a1a1a1">sidebar<br>64 px</div><div class="dim" style="left:340px;top:12px;color:#a1a1a1">top bar 40 px</div>')
    render(path, 'frame', frame('Title', 0, guides, back=True))
    # home
    left = pos(X0, Y0, 408, CH, f'<div class="col" style="padding:16px;height:100%;gap:12px"><div class="row" style="justify-content:space-between"><span style="font-size:16px;font-weight:600">Benchy.gcode</span>{badge("Printing", "var(--ok)")}</div>'
               f'<div class="row" style="gap:16px">{model(120)}<div class="col" style="gap:4px"><span style="font-size:64px;font-weight:700;line-height:1">59<span style="font-size:28px" class="muted">%</span></span><span class="muted" style="font-size:13px">Layer 118 / 200</span></div></div>'
               f'{prog(59)}<div class="row" style="justify-content:space-between" ><span class="muted" style="font-size:13px">Elapsed 00:42</span><span class="muted" style="font-size:13px">ETA 22:14</span></div>'
               f'<div class="row" style="gap:12px;margin-top:auto">{btn("Pause", "pause", "sec", h=52, w=186)}{btn("Stop", "square", "destr", h=52, w=186)}</div></div>')
    cfs = pos(496, Y0 + 3 * 72, 292, 56, f'<div class="row" style="height:100%;padding:0 14px;gap:10px;justify-content:space-between"><span class="lbl">CFS</span><div class="row" style="gap:8px">'
              + ''.join(f'<span style="width:22px;height:22px;border-radius:50%;background:{c};border:1px solid rgba(255,255,255,.25)"></span>' for c in ('#f5f5f5', '#2b2b2b', '#f97316', '#3b82f6')) + '</div></div>')
    quick = ''.join(pos(496 + (i % 2) * 152, Y0 + 3 * 72 + 68 + (i // 2) * 72, 140, 60, f'<div class="row" style="height:100%;gap:10px;justify-content:center">{ic(ico, 22)}<span style="font-size:14px;font-weight:500">{t}</span></div>')
                    for i, (t, ico) in enumerate((('Homing', 'crosshair'), ('Filament', 'circle-dot'), ('Fans', 'fan'), ('Fine tune', 'sliders'))))
    render(path, 'home', frame('', 0, left + temp_card(Y0, 'Extruder', 'thermo', '#f87171', 220, 220) + temp_card(Y0 + 72, 'Bed', 'layers', '#c084fc', 60, 60) + temp_card(Y0 + 144, 'Chamber', 'fan', '#60a5fa', 36, '--') + cfs + quick)
           .replace('<span class="nw" style="font-size:14px;font-weight:600"></span>', '<span class="nw" style="font-size:15px;font-weight:700;letter-spacing:1px">POWER<span style="color:var(--ok)">UI</span></span>'))
    # menu
    items = (('wifi', 'Wi-Fi', 'Network', ''), ('info', 'System', 'Preferences and info', ''), ('refresh', 'Power Update', 'Software and script', badge('New', 'var(--ok)')), ('settings', 'Settings', 'Display and behavior', ''),
             ('refresh-cw', 'Restart', 'Reload this interface', ''), ('fan', 'Fans', 'Speeds and targets', ''), ('thermo', 'Temperatures', 'Presets', ''), ('sliders', 'Limits', 'Velocity and acceleration', ''))
    cells = ''.join(f'<div class="card col" style="padding:14px;justify-content:space-between;position:relative"><div class="abs" style="right:12px;top:12px">{p}</div>{tile(i, 60, 40)}'
                    f'<div class="col" style="gap:3px"><span style="font-size:16px;font-weight:600">{t}</span><span class="muted" style="font-size:12px">{d}</span></div></div>' for i, t, d, p in items)
    render(path, 'menu', frame('Settings', 3, f'<div class="abs" style="left:{X0}px;top:{Y0}px;width:{CW}px;height:{CH}px;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(2,1fr);gap:{G}px">{cells}</div>'))
    # files
    rows = ''.join(f'<div class="row" style="height:56px;padding:0 12px;gap:12px;border-radius:10px;{"background:var(--sec);border:1px solid rgba(74,222,128,.5);" if i == 0 else ""}">{model(40)}<div class="col" style="flex:1"><span style="font-size:14px;font-weight:600">{n}</span><span class="muted" style="font-size:12px">{d}</span></div></div>'
                   for i, (n, d) in enumerate((('Benchy.gcode', '1 h 12 min · 14 g'), ('Calibration cube.gcode', '38 min · 6 g'), ('Bracket.gcode', '2 h 05 min · 31 g'), ('Vase.gcode', '3 h 40 min · 52 g'), ('Gear.gcode', '55 min · 9 g'))))
    lw = 472
    list_card = pos(X0, Y0, lw, CH, f'<div class="col" style="padding:12px;gap:10px;height:100%"><div class="row" style="gap:10px"><div style="width:180px">{seg(["Local", "USB"], "Local", h=40, fs=14)}</div><span style="flex:1"></span>{btn("A-Z", "sliders", "sec", h=40, fs=13, isz=16)}{btn("", "refresh", "out", h=40, w=40)}</div><div class="col" style="gap:2px">{rows}</div></div>')
    dx = X0 + lw + G
    det = pos(dx, Y0, CW - lw - G, CH, f'<div class="col" style="padding:16px;gap:10px;height:100%"><div style="height:130px">{model(130)}</div><span style="font-size:16px;font-weight:600">Benchy.gcode</span>'
              f'<div class="col" style="gap:6px"><div class="row" style="justify-content:space-between"><span class="muted" style="font-size:13px">Duration</span><span style="font-size:13px;font-weight:600">1 h 12 min</span></div>'
              f'<div class="row" style="justify-content:space-between"><span class="muted" style="font-size:13px">Filament</span><span style="font-size:13px;font-weight:600">14 g</span></div></div>'
              f'<div class="row" style="gap:10px;margin-top:auto">{btn("Print", "play", "primary", h=52, w=198)}{btn("", "trash", "destr", h=52, w=52)}</div></div>')
    render(path, 'files', frame('Files', 2, list_card + det))
    # filament
    left_rail = ''.join(pos(X0, Y0 + i * 107, 140, 95, f'<div class="col" style="align-items:center;justify-content:center;height:100%;gap:6px;{"color:#60a5fa;" if i == 3 else ""}">{ic(ico, 38)}<span style="font-size:15px;font-weight:500">{t}</span></div>')
                        for i, (t, ico) in enumerate((('Manual color', 'hand'), ('Load', 'download'), ('Unload', 'upload'), ('Cooldown', 'thermo'))))
    right_rail = ''.join(pos(X1 - 140, Y0 + i * 142, 140, 130 if i < 2 else 132, f'<div class="col" style="align-items:center;justify-content:center;height:100%;gap:8px">{ic(ico, 44)}<span style="font-size:15px;font-weight:500">{t}</span></div>',
                             cls='card' if i != 1 else 'card soft')
                         for i, (t, ico) in enumerate((('CFS', 'layers'), ('Extrude', 'arrow-down'), ('Retract', 'arrow-up'))))
    cards = ''.join(pos(X0 + 152, Y0 + [0, 142, 284][i], 408, [130, 130, 132][i], f'<div class="col" style="padding:14px 16px;height:100%;justify-content:space-between"><span class="muted" style="font-size:14px">{t}</span>{seg(o, a, h=52, fs=15, gap=6)}</div>')
                    for i, (t, o, a) in enumerate((('Extrude speed (mm/s)', [1, 2, 5, 10, 25], 5), ('Extrude length (mm)', [5, 10, 15, 20, 25], 10), ('Extruder temperature (°C)', [180, 200, 220, 240], 220))))
    render(path, 'filament', frame('Filament', 1, left_rail + cards + right_rail, back=True))
    # movement
    cell = lambda ico, t, kind='out': f'<div class="btn col {kind}" style="height:100px;width:96px;gap:4px;font-size:13px">{ic(ico, 30)}{t}</div>'
    xy = pos(X0, Y0, 332, 344, f'<div class="abs" style="left:13px;top:13px">{cell("arrow-up", "Y+")}</div><div class="abs" style="left:13px;top:121px;display:flex;gap:8px">{cell("arrow-left", "X-")}{cell("crosshair", "Home XY", "soft")}{cell("arrow-right", "X+")}</div><div class="abs" style="left:13px;top:229px">{cell("arrow-down", "Y-")}</div>'.replace('left:13px;top:13px', 'left:117px;top:13px').replace('left:13px;top:229px', 'left:117px;top:229px'))
    zc = pos(X0 + 344, Y0, 128, 344, f'<div class="abs" style="left:12px;top:12px">{btn("Z+", "arrow-up", "out", h=100, w=102, col=True, isz=30, fs=13)}</div><div class="abs" style="left:12px;top:120px">{btn("Home Z", "arrow-down", "soft", h=100, w=102, col=True, isz=30, fs=13)}</div><div class="abs" style="left:12px;top:228px">{btn("Z-", "arrow-down", "out", h=100, w=102, col=True, isz=30, fs=13)}</div>')
    ac = pos(X0 + 484, Y0, 228, 344, f'<div class="abs" style="left:12px;top:12px">{btn("Home All", "crosshair", "soft", h=100, w=202, isz=30, fs=15, gap=12)}</div><div class="abs" style="left:12px;top:120px">{btn("Motor Off", "power-off", "out", h=100, w=202, isz=30, fs=15, gap=12)}</div><div class="abs" style="left:12px;top:228px">{btn("Emergency Stop", "shield-alert", "destr", h=100, w=202, isz=30, fs=15, gap=12)}</div>')
    dist = pos(X0, Y0 + 356, CW, 60, f'<div class="row" style="height:100%;padding:0 12px;gap:14px"><span class="muted nw" style="font-size:13px;width:100px">Distance (mm)</span>{seg([".1", ".5", "1", "5", "10", "25", "50"], "1", h=44, fs=14, gap=6)}</div>')
    render(path, 'movement', frame('Movement', 0, xy + zc + ac + dist, back=True))
    # print status
    ps_left = pos(X0, Y0, 348, 296, f'<div class="col" style="padding:16px;gap:12px;height:100%"><div class="row" style="gap:12px">{model(96)}<div class="col" style="gap:6px"><span style="font-size:16px;font-weight:600">Benchy.gcode</span>{badge("Printing", "var(--ok)")}</div></div>'
                  f'<span style="font-size:48px;font-weight:700;line-height:1">59<span class="muted" style="font-size:22px">%</span></span>{prog(59)}<div class="row" style="gap:12px;margin-top:auto">{btn("Pause", "pause", "sec", h=44, w=150)}{btn("Cancel", "x", "out", h=44, w=150)}</div></div>')
    ps_t = pos(X0 + 360, Y0, 352, 144, f'<div class="col" style="padding:14px 16px;gap:10px"><span class="lbl">TEMPERATURE</span>' + ''.join(f'<div class="row" style="justify-content:space-between"><span class="muted" style="font-size:14px">{n}</span><span style="font-size:15px;font-weight:600">{c}° / {t}°</span></div>' for n, c, t in (('Extruder', 220, 220), ('Bed', 60, 60), ('Chamber', 36, 40))) + '</div>')
    ps_m = pos(X0 + 360, Y0 + 152, 352, 144, f'<div class="col" style="padding:14px 16px;gap:10px"><span class="lbl">MOTION</span>' + ''.join(f'<div class="row" style="justify-content:space-between"><span class="muted" style="font-size:14px">{n}</span><span style="font-size:15px;font-weight:600">{v}</span></div>' for n, v in (('Speed', '100 %'), ('Flow', '100 %'), ('Z offset', '+0.040'))) + '</div>')
    ps_b = f'<div class="abs row" style="left:{X0}px;top:{Y0 + 308}px;width:{CW}px;gap:12px">{btn("Tune", "sliders", "sec", h=56, w=230)}{btn("Objects", "layers", "out", h=56, w=230)}{btn("Stop", "square", "destr", h=56, w=230)}</div>'
    render(path, 'print-status', frame('Print status', 0, ps_left + ps_t + ps_m + ps_b, back=True))

if __name__ == '__main__':
    components()
    screens()
