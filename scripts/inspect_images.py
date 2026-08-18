import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow is required. Run:  pip install Pillow", file=sys.stderr)
    sys.exit(1)

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".tiff", ".bmp", ".tga"}

def inspect(path):
    try:
        with Image.open(path) as img:
            print(f"- {path}:  size={img.size}  format={img.format}  mode={img.mode}")
    except Exception as e:
        print(f"- {path}: ERROR  {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Print size, format, and colour-mode of image files."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help=(
            "One or more image file paths or directories. "
            "Directories are scanned for common image extensions."
        ),
    )
    args = parser.parse_args()

    if not args.paths:
        parser.print_help()
        sys.exit(0)

    print("Image Inspection:")
    for p in args.paths:
        if os.path.isdir(p):
            for f in sorted(os.listdir(p)):
                if os.path.splitext(f)[1].lower() in IMAGE_EXTENSIONS:
                    inspect(os.path.join(p, f))
        else:
            inspect(p)

if __name__ == "__main__":
    main()
