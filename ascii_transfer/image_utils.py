import numpy as np
from PIL import Image, ImageFilter


def load_image(path: str, width: int, height: int) -> Image.Image:
    """Load and resize image to target character grid dimensions."""
    img = Image.open(path).convert("RGB")
    img = img.resize((width, height), Image.LANCZOS)
    return img


def get_brightness(img: Image.Image) -> np.ndarray:
    """Return brightness map normalized 0.0 (dark) to 1.0 (light)."""
    gray = img.convert("L")
    arr = np.array(gray, dtype=np.float32) / 255.0
    return arr


def get_edges(img: Image.Image) -> tuple[np.ndarray, np.ndarray]:
    """Return edge magnitude and angle maps using Sobel filters."""
    gray = np.array(img.convert("L"), dtype=np.float32)

    #Simple Sobel kernels applied via convolution
    from scipy.ndimage import convolve
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

    gx = convolve(gray, kx)
    gy = convolve(gray, ky)

    magnitude = np.hypot(gx, gy)
    magnitude = magnitude / magnitude.max() if magnitude.max() > 0 else magnitude
    angle = np.degrees(np.arctan2(gy, gx))

    return magnitude, angle


def get_colors(img: Image.Image) -> np.ndarray:
    """Return RGB array normalized to 0-1."""
    return np.array(img, dtype=np.float32) / 255.0
