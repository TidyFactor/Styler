import argparse
import os
import sys

try:
    from rembg import remove
    from PIL import Image
except ImportError:
    print("Required packages not installed. Run:  pip install rembg pillow", file=sys.stderr)
    sys.exit(1)

from _utils import split_spec

def remove_bg(src, dest):
    if not os.path.exists(src):
        print(f"[skip] {src} not found")
        return
    try:
        print(f"[work] {src} -> {dest}")
        img = Image.open(src)
        out = remove(img)
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        out.save(dest)
        print(f"[ok]   {dest}")
    except Exception as e:
        print(f"[error] {src}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Remove backgrounds from images using rembg. "
                    "Accepts src:dest pairs or a single file with --output.",
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        help="Image paths. Use  src:dest  syntax for explicit output names, "
             "or plain paths (output appends '_cut' before the extension).",
    )
    parser.add_argument("--output", "-o", help="Output path (valid only with a single input)")
    args = parser.parse_args()

    if not args.inputs:
        parser.print_help()
        sys.exit(0)

    if args.output and len(args.inputs) > 1:
        parser.error("--output can only be used with a single input file")

    for spec in args.inputs:
        if ":" in spec:
            parts = split_spec(spec)
            src, dest = parts[0], parts[1] if len(parts) > 1 else parts[0]
        elif args.output:
            src, dest = spec, args.output
        else:
            root, ext = os.path.splitext(spec)
            src, dest = spec, f"{root}_cut{ext}"
        remove_bg(src.strip(), dest.strip())

if __name__ == "__main__":
    main()
