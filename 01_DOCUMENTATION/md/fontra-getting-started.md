# Getting Started with Fontra

Fontra is a free, open-source, browser-based font editor built for variable fonts from the ground up. Developed by Black[Foundry] and Just van Rossum with support from Google Fonts, it originally targeted the design and production of large CJK character sets but has grown into a near-feature-complete editor suitable for any type project.

Because it runs in the browser, Fontra works on macOS, Windows, and Linux with the same interface. You can edit local files through the companion app **Fontra Pak**, or connect to a remote server for real-time collaboration with other designers.

---

## 1 — Installing Fontra Pak

Fontra Pak is a self-contained application that runs a local Fontra server and opens the editor in your default browser.

| Platform | How to install |
|---|---|
| **macOS** | Download the `.dmg` from [fontra.xyz](https://fontra.xyz/), open the package, and drag Fontra Pak into your Applications folder. |
| **Windows 10/11** | Download the `.zip` from [fontra.xyz](https://fontra.xyz/), extract it, and double-click the installer. |
| **Linux (Ubuntu)** | Search for *fontrapak* in Ubuntu Software, or install the snap: `sudo snap install fontrapak`. Flatpak is also available. |

> For detailed platform instructions see the [installation docs](https://docs.fontra.xyz/how-tos/installation/installing-fontra-pak/).

---

## 2 — Opening a Font

1. Double-click the **Fontra Pak** icon — a small start-up window appears.
2. **Drag** a `.ufo`, `.designspace`, `.fontra`, `.glyphs`, or `.glyphspackage` file onto that window.
3. Fontra opens in your browser. You land on the **Font Overview** — a grid of all glyphs in the font.
4. **Double-click** any glyph cell to enter the **Editor View** and start drawing.

You can also open compiled `.ttf` or `.otf` files for inspection (read-only).

---

## 3 — Supported File Formats

| Format | Read | Write |
|---|---|---|
| `.fontra` | Yes | Yes |
| `.ufo` / `.designspace` | Yes | Yes |
| `.glyphs` / `.glyphspackage` | Yes | Yes (partial — via plugin) |
| `.ttf` / `.otf` | Yes | — |
| `.rcjk` (RoboCJK) | Yes (via plugin) | Yes (via plugin) |

---

## 4 — Key Capabilities

### Variable-first design
Every glyph can have its own sources at any location in the design space. Variation axes are not forced to be global — you can define glyph-local axes and use **variable components** (similar to Smart Components in Glyphs) to build modular, parametric letterforms.

### Browser-based, cross-platform
The client is written in JavaScript and runs in any modern browser; the server is Python. Because it is browser-based, the interface is identical on macOS, Windows, and Linux.

### Real-time collaboration
When Fontra runs on a shared server, multiple designers can edit the same font simultaneously — each working on different glyphs without conflict. This was a core requirement for large CJK production teams.

### Background layers and images
You can create additional source layers per glyph for sketches, variations, or reference shapes. Background images (PNG or JPEG) can be placed inside a glyph with adjustable opacity, and are mostly compatible with the UFO background-image format.

### OpenType feature editing
A built-in code panel (powered by CodeMirror) lets you author and edit OpenType feature source code directly inside Fontra, without switching to an external text editor.

### Kerning
The Kerning tool lives alongside the new Sidebearing tool. Select a glyph pair and drag or use arrow keys to adjust values. Modifier keys constrain edits to 5, 10, or 50-unit increments. A context menu lets you create kerning exceptions for group pairs.

### Font Info and low-level tables
The Font Info panel exposes metadata (family name, version, UPM, etc.) as well as lower-level OpenType table settings (hhea, vhea, OS/2) so you can fine-tune the binary output.

### Large character-set support
Fontra was designed from the start to handle fonts with tens of thousands of glyphs — scrolling, searching, and editing remain smooth even in massive CJK projects.

---

## 5 — The Interface at a Glance

Fontra has two main views:

**Font Overview** — a grid of all glyphs. You can filter by glyph sets (predefined collections independent from the font), search by name or Unicode, and see placeholder cells for characters not yet drawn.

**Editor View** — where you draw and edit. The toolbar on the left gives you access to the drawing and editing tools. Panels on the right provide context: design-space navigation, glyph info, transformations, reference fonts, preview text, and more.

---

## 6 — Drawing and Editing Tools

| Tool | Purpose |
|---|---|
| **Pointer** | Select, move, and transform points and contours. |
| **Pen** | Draw new Bézier contours. A sub-tool switches to quadratic curves. |
| **Knife** | Cut contours. |
| **Shape** | Draw basic geometric shapes (rectangles, ellipses). |
| **Ruler** | Measure distances and angles. |
| **Hand** | Pan the canvas. |
| **Sidebearing** | Adjust left and right sidebearings visually. Hold Alt to move opposite bearings symmetrically. |
| **Kerning** | Adjust pair kerning by dragging or with arrow keys. Shift-click to multi-select pairs. |

---

## 7 — Quick-Reference Cheatsheet

### Navigation

| Action | Shortcut / Gesture |
|---|---|
| Pan canvas | Hand tool **or** Space + drag |
| Zoom in / out | Scroll wheel or pinch |
| Next / previous glyph | Arrow shortcuts (customisable) |
| Open glyph from overview | Double-click the glyph cell |
| Return to Font Overview | Close the editor tab or use the menu |

### Editing essentials

| Action | How |
|---|---|
| Switch to Pen tool | Select from toolbar (custom shortcut available) |
| Toggle cubic / quadratic | Use the Pen sub-tool toggle |
| Undo / Redo | Cmd/Ctrl + Z / Shift + Cmd/Ctrl + Z (per-glyph) |
| Constrain kerning to 10 units | Hold modifier key while dragging |
| Create kerning exception | Right-click with Kerning tool active |
| Add background layer | Layers panel — add a new source layer to the current glyph |
| Place background image | Drag a PNG/JPEG onto the glyph, or use the image panel |

### File formats at a glance

| I want to… | Use this format |
|---|---|
| Native round-trip editing | `.fontra` |
| Interop with other editors | `.ufo` / `.designspace` |
| Open a Glyphs file directly | `.glyphs` / `.glyphspackage` |
| Inspect a compiled font | `.ttf` / `.otf` (read-only) |

### Useful links

| Resource | URL |
|---|---|
| Fontra home | [fontra.xyz](https://fontra.xyz/) |
| Documentation | [docs.fontra.xyz](https://docs.fontra.xyz/) |
| Blog / updates | [blog.fontra.xyz](https://blog.fontra.xyz/) |
| Changelog | [fontra.xyz/changelog.html](https://fontra.xyz/changelog.html) |
| GitHub | [github.com/fontra](https://github.com/fontra) |

---

*Sources: [Fontra Documentation](https://docs.fontra.xyz/), [Fontra Blog](https://blog.fontra.xyz/), [Fontra GitHub](https://github.com/fontra/fontra).*
