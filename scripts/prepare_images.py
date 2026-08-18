import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Required package not installed. Run:  pip install Pillow", file=sys.stderr)
    sys.exit(1)

PNG_EXTS = {".png", ".webp", ".tga", ".bmp", ".tiff"}

def convert_to_jpg(src, dest, quality=87):
    if not os.path.exists(src):
        print(f"[skip] {src} not found")
        return
    try:
        img = Image.open(src)
        rgb_img = img.convert("RGB")
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        rgb_img.save(dest, "JPEG", quality=quality)
        print(f"[ok]   {src} -> {dest}  (q={quality})")
    except Exception as e:
        print(f"[error] {src}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert PNG/WEBP images to optimised JPEG. "
                    "Accepts explicit src:dest pairs or an input/output directory pair.",
    )
    parser.add_argument(
        "pairs",
        nargs="*",
        help="src:dest pairs  e.g.  assets/hero.png:assets/hero.jpg",
    )
    parser.add_argument(
        "--input-dir",
        help="Scan a directory for PNG/WEBP files (alternative to positional pairs)",
    )
    parser.add_argument("--output-dir", help="Directory for converted JPEGs (default: same as input)")
    parser.add_argument("--quality", "-q", type=int, default=87, help="JPEG quality 1-100 (default: 87)")
    args = parser.parse_args()

    if args.input_dir and args.pairs:
        parser.error("Use either --input-dir OR positional pairs, not both.")

    if args.input_dir:
        out_dir = args.output_dir or args.input_dir
        os.makedirs(out_dir, exist_ok=True)
        for f in sorted(os.listdir(args.input_dir)):
            if os.path.splitext(f)[1].lower() in PNG_EXTS:
                src = os.path.join(args.input_dir, f)
                dest = os.path.join(out_dir, os.path.splitext(f)[0] + ".jpg")
                convert_to_jpg(src, dest, args.quality)
    elif args.pairs:
        for pair in args.pairs:
            if ":" not in pair:
                print(f"[skip] '{pair}' — expected format  src:dest", file=sys.stderr)
                continue
            src, dest = pair.split(":", 1)
            convert_to_jpg(src.strip(), dest.strip(), args.quality)
    else:
        parser.print_help()
        sys.exit(0)

if __name__ == "__main__":
    main()
