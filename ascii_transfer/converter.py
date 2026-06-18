import numpy as np
from PIL import Image

from .charmap import brightness_to_char, edge_to_char
from .image_utils import load_image, get_brightness, get_edges, get_colors
from .style import extract_style, style_bias


def convert(
    content_path: str,
    style_path: str | None = None,
    width: int = 120,
    height: int = 60,
    edge_threshold: float = 0.45,
    colored: bool = True,
) -> tuple[list[list[str]], list[list[tuple]] | None]:
    content_img = load_image(content_path, width, height)
    brightness = get_brightness(content_img)
    edge_mag, edge_angle = get_edges(content_img)
    colors = get_colors(content_img) if colored else None

    style = None
    if style_path:
        style_img = load_image(style_path, width, height)
        style = extract_style(style_img)

    chars = []
    color_grid = []

    for row in range(height):
        char_row = []
        color_row = []

        for col in range(width):
            b = float(brightness[row, col])
            if style:
                b = style_bias(b, style)
            if edge_mag[row, col] > edge_threshold:
                ch = edge_to_char(float(edge_angle[row, col]))
            else:
                ch = brightness_to_char(b)

            char_row.append(ch)

            if colored and colors is not None:
                r, g, b_val = colors[row, col]
                color_row.append((int(r * 255), int(g * 255), int(b_val * 255)))

        chars.append(char_row)
        if colored:
            color_grid.append(color_row)

    return chars, (color_grid if colored else None)
