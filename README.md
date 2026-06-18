# ASCII Style Transfer

Convert any image into ASCII art — optionally styled by a second image.

No deep learning required. Built with Pillow, NumPy, and SciPy.

---

## How It Works

**Without a style image:**  
Each pixel's brightness maps to a character (`@`, `#`, `+`, `.`, ` `, etc.).  
Strong edges are replaced with directional characters (`|`, `/`, `\`, `-`).

**With a style image:**  
The style image's brightness histogram and texture density are extracted.  
The content image's brightness values are remapped to match the style's character distribution — dark/busy styles push the output denser, light/minimal styles open it up.

---

## Project Structure

```
ascii_style_transfer/
├── ascii_transfer/
│   ├── charmap.py       # brightness/edge → character mappings
│   ├── image_utils.py   # image loading, brightness, edge detection
│   ├── style.py         # style extraction and brightness remapping
│   ├── converter.py     # main conversion pipeline
│   └── renderer.py      # save as .txt and .html
├── samples/             # sample content and style images
├── output/              # generated outputs go here
├── main.py              # CLI entry point
└── requirements.txt
```

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/ascii-style-transfer.git
cd ascii-style-transfer
pip install -r requirements.txt
```

---

## Usage

**Basic (no style):**
```bash
python main.py samples/portrait.jpg
```

**With a style image:**
```bash
python main.py samples/portrait.jpg --style samples/vangogh_style.jpg
```

**Custom size:**
```bash
python main.py samples/portrait.jpg --width 160 --height 80
```

**All options:**
```
positional arguments:
  content               Path to the content image

optional arguments:
  --style               Path to style image
  --width               Output width in characters (default: 120)
  --height              Output height in characters (default: 60)
  --edge-threshold      Edge sensitivity 0.0–1.0 (default: 0.3)
  --no-color            Disable color in HTML output
  --output              Output directory (default: output/)
```

Outputs are saved to the `output/` folder as:
- `name.txt` — plain text, printable anywhere
- `name.html` — colored version, open in any browser

---

## Style Tips

| Style image type | Effect on output |
|---|---|
| Dark, high-contrast | Dense characters, heavy shadows |
| Light, minimal | Sparse characters, airy output |
| Swirly/textured | Redistributed brightness, more character variety |
| Flat/uniform | Minimal remapping, close to original |

---

## Example

```
python main.py samples/portrait.jpg --style samples/vangogh_style.jpg --width 120 --height 60
```

Open `output/portrait_styled_vangogh_style.html` in your browser.
