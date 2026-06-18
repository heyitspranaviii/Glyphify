import argparse
import os
from ascii_transfer import convert, save_txt, save_html

def parse_args():
    parser = argparse.ArgumentParser(
        description="ASCII Art Style Transfer:Convert images to styled ASCII art"
    )
    parser.add_argument("content", help="Path to the content image")
    parser.add_argument("--style", default=None, help="Path to the style image (optional)")
    parser.add_argument("--width", type=int, default=120, help="Output width in characters (default: 120)")
    parser.add_argument("--height", type=int, default=60, help="Output height in characters (default: 60)")
    parser.add_argument("--edge-threshold", type=float, default=0.3, help="Edge sensitivity 0.0-1.0 (default: 0.3)")
    parser.add_argument("--no-color", action="store_true", help="Disable color in HTML output")
    parser.add_argument("--output", default="output", help="Output directory (default: output/)")
    return parser.parse_args()


def main():
    args = parse_args()

    if not os.path.exists(args.content):
        print(f"Error: content image not found: {args.content}")
        return

    if args.style and not os.path.exists(args.style):
        print(f"Error: style image not found: {args.style}")
        return

    print(f"Converting: {args.content}")
    if args.style:
        print(f"Style:      {args.style}")
    print(f"Grid size:  {args.width} x {args.height}")

    chars, colors = convert(
        content_path=args.content,
        style_path=args.style,
        width=args.width,
        height=args.height,
        edge_threshold=args.edge_threshold,
        colored=not args.no_color,
    )
    base = os.path.splitext(os.path.basename(args.content))[0]
    if args.style:
        style_base = os.path.splitext(os.path.basename(args.style))[0]
        base = f"{base}_styled_{style_base}"

    save_txt(chars, os.path.join(args.output, f"{base}.txt"))
    save_html(chars, colors, os.path.join(args.output, f"{base}.html"))


if __name__ == "__main__":
    main()
