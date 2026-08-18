import argparse
import os
import shutil
import sys

try:
    from PIL import Image
except ImportError:
    print("Required package not installed. Run:  pip install Pillow", file=sys.stderr)
    sys.exit(1)

def resize_image_max_dim(path, max_dim, output=None):
    if not os.path.exists(path):
        print(f"[skip] {path} not found")
        return
    try:
        img = Image.open(path)
        w, h = img.size
        if w <= max_dim and h <= max_dim:
            print(f"[ok]   {path} already within {max_dim}px ({w}x{h})")
            return
        if w > h:
            new_w = max_dim
            new_h = int(h * (max_dim / w))
        else:
            new_h = max_dim
            new_w = int(w * (max_dim / h))
        print(f"[resize] {path}  {w}x{h} -> {new_w}x{new_h}")
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        dest = output or path
        img.save(dest)
        print(f"[saved] {dest}")
    except Exception as e:
        print(f"[error] {path}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Resize images so their largest dimension does not exceed a given pixel limit. "
                    "Overwrites in place unless --output is specified.",
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        help="Image file paths. Each can be followed by a colon and a max-dim value "
             "(e.g. assets/logo.png:240). The colon suffix is only recognised when the "
             "trailing segment is purely numeric, so Windows paths like C:\\images\\photo.png "
             "work without ambiguity. If no colon value is given, --max-dim is used.",
    )
    parser.add_argument(
        "--max-dim",
        type=int,
        default=1200,
        help="Default max dimension in pixels (default: 1200)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Optional output path (only valid when a single input is given)",
    )
    args = parser.parse_args()

    if not args.inputs:
        parser.print_help()
        sys.exit(0)

    if args.output and len(args.inputs) > 1:
        parser.error("--output can only be used with a single input file")

    output_for_single = args.output if len(args.inputs) == 1 else None
    for spec in args.inputs:
        # Split spec into path + optional max-dim ONLY when the trailing segment
        # after the last colon is purely numeric.  This avoids corrupting
        # Windows absolute paths like  C:\images\photo.png  (which contain a
        # drive-letter colon that is NOT a dimension modifier).
        path = spec
        dim = args.max_dim
        if ":" in spec:
            left, right = spec.rsplit(":", 1)
            if right.isdigit():
                path, dim = left, int(right)

        dest = output_for_single or path
        if not output_for_single and os.path.exists(path):
            backup = path + ".bak"
            print(f"[warn] overwriting in-place: {path}  (backup -> {backup})")
            shutil.copy2(path, backup)

        resize_image_max_dim(path, dim, output=dest)

if __name__ == "__main__":
    main()
