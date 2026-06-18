# Glyphify

Convert any image into ASCII art using brightness mapping, edge detection, and optional histogram-based style transfer.

Feed it a photo and a style photo(optional) and Glyphify reconstructs the content's structure in characters, tone, and texture. Optionally pass a second image to influence how characters are distributed across the output. 

---

## Project Structure

```
glyphify/
│
├── ascii_transfer/
│   ├── charmap.py       →  brightness and edge angle → character mappings
│   ├── image_utils.py   →  image loading, grayscale, Sobel edge detection
│   ├── style.py         →  histogram extraction and brightness remapping
│   ├── converter.py     →  main pipeline: ties all modules together
│   └── renderer.py      →  saves output as .txt and colored .html
│
├── main.py              →  CLI entry point
└── requirements.txt
```

| File | What it does |
|---|---|
| `charmap.py` | Maps brightness values to characters (`@#MWod+;:,. `). Maps edge angles to directional characters (`\|/-`) |
| `image_utils.py` | Loads and resizes image. Extracts per-pixel brightness and runs Sobel filter for edge magnitude and angle |
| `style.py` | Extracts brightness histogram and texture density from style image. Remaps content brightness toward the style distribution |
| `converter.py` | Iterates every pixel — picks edge char or brightness char, applies style bias, collects RGB for coloring |
| `renderer.py` | Writes the character grid to `.txt` and a styled `.html` file with per-character color spans |

---

## Requirements

- Python 3.10 or higher
- Pillow
- NumPy
- SciPy

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

**Step 1: Clone the repo**

```bash
git clone https://github.com/pranaviii29/Glyphify.git
cd glyphify
```

**Step 2: Run**

Without a style image:

```bash
python main.py path/to/image.jpg(or jpeg/png)
```

With a style image:

```bash
python main.py path/to/image.jpg(or jpeg/png) --style path/to/style.jpg(or jpeg/png)
```

Output is saved to the `output/` folder as `.txt` and `.html`. Open the `.html` in any browser — that is the colored version.

---

## All Flags

| Flag | Default | Description |
|---|---|---|
| `--style` | None | Style image to influence character distribution |
| `--width` | 120 | Output width in characters |
| `--height` | 60 | Output height in characters |
| `--edge-threshold` | 0.45 | Edge sensitivity 0.0–1.0 |
| `--no-color` | False | Disable color in HTML output |
| `--output` | `output/` | Directory to save results |

---

## How It Works

**Brightness mapping**
Each pixel is converted to a brightness value between 0 and 1. That value indexes into a character ramp ordered by visual density — `@` is darkest, space is lightest.

**Edge detection**
A Sobel filter runs over the grayscale image producing an edge magnitude and angle at every pixel. Where the magnitude crosses the threshold, the brightness character is replaced with a directional one — `|` for vertical edges, `/` and `\` for diagonals, `-` for horizontal. This preserves outlines, glasses frames, hair boundaries.

**Style transfer**
The style image's brightness histogram is extracted along with its texture density (local contrast). The content image's brightness values are remapped using cumulative histogram matching toward the style's distribution. A dark busy painting pushes character weight up. A minimal image opens the output up. The blend strength is capped so the content structure is never lost.

---

## Tips

- Portrait photos work best with `height ≈ width × 0.55`-characters are taller than wide
- Zoom out in the browser to around 50% — ASCII art resolves at a distance
- High contrast photos (strong lighting, glasses, hair) produce the sharpest results
- Always open the `.html` output(the `.txt` has no color).

---

## Future Work

- `--invert` flag to flip the brightness ramp for light-background output
- Automatic aspect ratio correction based on detected image orientation
- Unicode block character mode as an alternative to ASCII
- Web UI-drag and drop image,download HTML output directly in browser

---

## License

MIT
