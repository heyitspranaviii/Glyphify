import numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter

def extract_style(style_img: Image.Image, bins: int = 16) -> dict:
    """
    Extract style as brightness histogram + texture statistics.
    This tells us how 'dark', 'busy', or 'swirly' the style image is.
    """
    gray = np.array(style_img.convert("L"), dtype=np.float32) / 255.0

    hist, _ = np.histogram(gray, bins=bins, range=(0.0, 1.0), density=True)
    hist = hist / hist.sum()  # normalize to probability distribution

    mean_brightness = float(gray.mean())
    std_brightness = float(gray.std())
    local_mean = uniform_filter(gray, size=5)
    local_contrast = float(np.abs(gray - local_mean).mean())

    return {
        "histogram": hist,          #shape of brightness distribution
        "mean": mean_brightness,    #overall darkness/lightness
        "std": std_brightness,      #contrast range
        "texture": local_contrast,  #busyness / detail density
    }


def style_bias(brightness: float, style: dict) -> float:
    """
    Remap brightness based on style histogram.
    Only applies remapping if the style has strong texture/contrast.
    """
    # If style is flat/low contrast, don't remap much
    if style["texture"] < 0.05:
        return brightness

    bins = len(style["histogram"])
    bin_idx = min(int(brightness * bins), bins - 1)

    cdf = np.cumsum(style["histogram"])
    cdf = cdf / cdf[-1]

    remapped = float(cdf[bin_idx])

    # Subtle blend(never more than 40% remapping)
    blend = min(style["texture"] * 1.5, 0.25)
    return brightness * (1 - blend) + remapped * blend
