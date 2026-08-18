import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow is required. Run:  pip install Pillow", file=sys.stderr)
    sys.exit(1)

def check_alpha(path):
    if not os.path.exists(path):
        print(f"- {path}: file not found")
        return
    try:
        with Image.open(path) as img:
            if img.mode == 'RGBA':
                alpha = img.split()[3]
                extrema = alpha.getextrema()
                has_transparency = extrema[0] < 255
                print(f"- {path}: RGBA  alpha_range={extrema}  transparent={has_transparency}")
            else:
                print(f"- {path}: {img.mode}  no alpha channel")
    except Exception as e:
        print(f"- {path}: ERROR  {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Check whether images have an alpha (transparency) channel."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="One or more image file paths. If a path is a directory, all PNG/WEBP files inside it are checked.",
    )
    args = parser.parse_args()

    if not args.paths:
        parser.print_help()
        sys.exit(0)

    print("Alpha Channel Check:")
    for p in args.paths:
        if os.path.isdir(p):
            for f in sorted(os.listdir(p)):
                if f.lower().endswith((".png", ".webp", ".tga")):
                    check_alpha(os.path.join(p, f))
        else:
            check_alpha(p)

if __name__ == "__main__":
    main()
