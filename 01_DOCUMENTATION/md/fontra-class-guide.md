# Fontra Pak — Class Guide

> **Before this guide:** install Fontra Pak and read the interface overview in [**Fontra — Getting Started**](fontra-getting-started.html). This document assumes Fontra Pak is already running on your machine.

---

## 1 — Open the Class Variable Font Project

### About ZalandoSans

The class demo font is **ZalandoSans-VariableFont.fontra**, located in the `02_DEMO` folder of the class drive. It is the open-source [Zalando Sans](https://github.com/zalando/sans) typeface, released by Zalando SE under the SIL Open Font Licence — a contemporary sans-serif with two variable axes:

| Axis | Tag | Range | Default |
|---|---|---|---|
| Weight | `wght` | 200 – 900 | 400 (Regular) |
| Width | `wdth` | 75 – 125 | 100 (Normal) |

### Opening the file

1. Launch **Fontra Pak** — the launcher window appears.
2. In Finder / Explorer, navigate to `02_DEMO/` on the class drive.
3. **Drag `ZalandoSans-VariableFont.fontra` onto the Fontra Pak launcher window**.
4. Your browser opens automatically and lands on the **Font Overview** — a grid of every glyph in the font.

### Exploring the variable axes

1. Double-click any glyph — try **H**, **O**, or **n** — to enter the **Editor View**.
2. In the right-hand panel, open the **Design Space** panel (compass icon).
3. Drag the **Weight** and **Width** sliders — the glyph updates live.
4. Click any position in the 2-D axis map to jump to that location instantly.

### Using ZalandoSans as a Reference Font while editing your own work

1. Open your own project in a Fontra Pak session.
2. In the right panel, open the **Reference Fonts** panel.
3. Click **+** and navigate to `ZalandoSans-VariableFont.fontra`.
4. The reference glyph appears in grey behind your drawings — use it for proportion comparison, not tracing.

---

## 2 — Start a New Project from Scratch

### Create the font file

1. In the Fontra Pak launcher, click **New Font…**
2. A new, empty font opens in the browser.
3. When prompted, choose a save location inside your project folder and name the file (e.g. `MyFamily.fontra`).
   Fontra saves automatically from this point on — there is no manual *Save* step.

### Set up Font Info

Open the **Font Info** panel (ⓘ icon in the top toolbar) and fill in at minimum:

| Field | Recommended value |
|---|---|
| Family Name | Your typeface name |
| Units Per Em (UPM) | `1000` (PostScript standard) |
| Ascender | `800` |
| Cap Height | `700` |
| x-Height | `500` |
| Descender | `-200` |

### Add a variable axis (optional — for variable fonts only)

1. In Font Info, scroll to the **Axes** section and click **+**.
2. A standard starting axis: `wght` Weight — min `100`, default `400`, max `900`.
3. Click **Add source** to place masters — e.g. Regular at 400, Bold at 700.
4. Fontra creates separate source layers for each master location.

> For a first project in class, **work with a single master**. Add a second only once the first is solid.

### Draw your first glyphs

Follow the drawing order established in the typography sessions:

- **Uppercase:** `H` then `O` — all other uppercase letters derive from these proportions.
- **Lowercase:** `n` then `o` then `y` — together they define the arch, the bowl, and the descender.

To add a glyph:

1. In the Font Overview, click **+** (or right-click an empty cell → **Add glyph**).
2. Type the glyph name (e.g. `H`) — Fontra fills the Unicode value automatically for standard characters.
3. Double-click the new cell to open the **Editor View** and start drawing.

### Import a scanned sketch as background

1. In the Editor View, open the **Layers** panel on the right.
2. Click **+** and name the new layer (e.g. `sketch`).
3. Drag a PNG or JPEG scan onto the glyph canvas — it lands in the active layer.
4. Lower the opacity in the layer settings so it doesn't compete with your contours.

---

## 3 — Export Font Files

### Native autosave — .fontra (always on)

Your `.fontra` folder on disk is always current. No export is needed for ongoing work.

### Export to UFO + DesignSpace

The standard interchange format — compatible with RoboFont, Glyphs, and the Google Fonts build pipeline.

1. **File → Export as…**
2. Choose **UFO + DesignSpace**.
3. Select a destination **outside** your `.fontra` source folder.
4. Click **Export** — Fontra writes one `.ufo` per master plus a `.designspace` file.

### Export to Variable TTF / OTF

To produce a binary font for testing in applications or browsers:

1. **File → Export as…** → **Variable TTF** (or Variable OTF).
2. Choose a destination and click **Export** — Fontra compiles the font directly, no external tools required.

### Export to Static instances

To produce individual style files (Regular.ttf, Bold.ttf, etc.):

1. **File → Export as…** → **Static TTF instances**.
2. Fontra generates one binary per defined master location.

> **Quick proof:** install the exported `.ttf` system-wide, or drop it on [wakamaifondue.com](https://wakamaifondue.com) to inspect all variable axes and OpenType features directly in the browser.

---

## Useful Links

| Resource | URL |
|---|---|
| Fontra — Getting Started (general) | [fontra-getting-started.html](fontra-getting-started.html) |
| Fontra documentation | [docs.fontra.xyz](https://docs.fontra.xyz/) |
| Zalando Sans source (open-source reference) | [github.com/zalando/sans](https://github.com/zalando/sans) |
| Font proofing | [wakamaifondue.com](https://wakamaifondue.com) |

---

*Sources: [Fontra Docs – Export as](https://docs.fontra.xyz/reference/menu/file/export-as) · [Zalando Sans](https://github.com/zalando/sans)*
