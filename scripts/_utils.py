"""Shared utilities for the Cinematic Landing Kit asset pipeline."""

import re

try:
    from PIL import Image
except ImportError:
    Image = None


def crop_cover_16_9(img, target_w: int = 1280, target_h: int = 720):
    """Crop-resize an image to a target 16:9 frame (object-cover style)."""
    if Image is None:
        raise ImportError("Pillow is required for crop_cover_16_9. Run:  pip install Pillow")
    img = img.convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h
    if img_ratio > target_ratio:
        new_width = int(target_ratio * img.height)
        offset = (img.width - new_width) // 2
        img = img.crop((offset, 0, offset + new_width, img.height))
    else:
        new_height = int(img.width / target_ratio)
        offset = (img.height - new_height) // 2
        img = img.crop((0, offset, img.width, offset + new_height))
    return img.resize((target_w, target_h), Image.Resampling.LANCZOS)


_NATURAL_SORT_RE = re.compile(r"(\d+)")


def natural_sort_key(s: str):
    """Sort key for filenames with embedded numbers.

    'k2.jpg' sorts before 'k10.jpg', matching human expectations.
    """
    parts = _NATURAL_SORT_RE.split(s)
    return [int(p) if p.isdigit() else p.lower() for p in parts]


def split_spec(spec: str) -> list[str]:
    """Split 'src:dest[:opts]' with Windows drive-letter awareness.

    A single-alpha character immediately before ':' is treated as a drive-letter
    prefix (e.g. C:\\path) rather than a field separator.  All other colons are
    normal field delimiters.
    """
    parts: list[str] = []
    current = ""
    for ch in spec:
        if ch == ":":
            if len(current) == 1 and current[0].isalpha():
                current += ch
            else:
                parts.append(current)
                current = ""
        else:
            current += ch
    parts.append(current)
    return parts
