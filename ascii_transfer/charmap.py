# Characters ordered from darkest to lightest visual weight
CHARS = list('@#S%?*+;:,. ')

def brightness_to_char(value: float) -> str:
    """Map a brightness value (0.0=dark to 1.0=light) to a character."""
    index = int(value * (len(CHARS) - 1))
    return CHARS[index]

def edge_to_char(angle_deg: float) -> str:
    """Map an edge gradient angle to a directional character."""
    if angle_deg is None:
        return ' '
    angle_deg = angle_deg % 180
    if angle_deg < 22.5 or angle_deg >= 157.5:
        return '-'
    elif angle_deg < 67.5:
        return '/'
    elif angle_deg < 112.5:
        return '|'
    else:
        return '\\'
