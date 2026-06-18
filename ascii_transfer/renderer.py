import os

def save_txt(chars: list[list[str]], output_path: str):
    """Save ASCII art as plain text file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    lines = [''.join(row) for row in chars]
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Saved text: {output_path}")


def save_html(
    chars: list[list[str]],
    colors: list[list[tuple]] | None,
    output_path: str,
    bg_color: str = "#0d0d0d",
    font_size: int = 10,
):
    """Save ASCII art as colored HTML file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    lines_html = []
    for row_idx, row in enumerate(chars):
        spans = []
        for col_idx, ch in enumerate(row):
            display = ch if ch != ' ' else '&nbsp;'
            if colors:
                r, g, b = colors[row_idx][col_idx]
                style = f'color:rgb({r},{g},{b})'
                spans.append(f'<span style="{style}">{display}</span>')
            else:
                spans.append(display)
        lines_html.append(''.join(spans))

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ASCII Style Transfer</title>
  <style>
    body {{
      background: {bg_color};
      margin: 0;
      padding: 20px;
    }}
    pre {{
      font-family: 'Courier New', monospace;
      font-size: {font_size}px;
      line-height: 1.1;
      letter-spacing: 0.05em;
    }}
  </style>
</head>
<body>
  <pre>{"<br>".join(lines_html)}</pre>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved HTML: {output_path}")
