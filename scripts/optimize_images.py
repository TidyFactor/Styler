#!/usr/bin/env python3
"""
Image Optimization Utility
Optimizes JPEGs, PNGs, and WebP images in a directory using Python's Pillow library.
Resolves paths relative to the project root.
"""

import os
import sys
import argparse
from pathlib import Path

# Project root is parent of scripts/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

try:
    from PIL import Image
except ImportError:
    print("Error: The 'Pillow' library is required to run this script.")
    print("Install it by running: pip install Pillow")
    sys.exit(1)


def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def optimize_image(file_path, quality=85, convert_to_webp=False, replace=True, backup=True):
    path = Path(file_path)
    ext = path.suffix.lower()

    if ext not in [".jpg", ".jpeg", ".png", ".webp"]:
        return None

    orig_size = path.stat().st_size
    
    try:
        # Determine destination path
        if convert_to_webp:
            dest_path = path.with_suffix(".webp")
        else:
            dest_path = path

        # Backup handling: Rename the original file BEFORE opening it
        # This prevents WinError 32 (file in use) on Windows
        backup_path = None
        source_path = path
        
        if replace and dest_path == path and backup:
            bp = path.with_name(f"{path.stem}_backup{ext}")
            if not bp.exists():
                os.rename(path, bp)
                backup_path = bp
                source_path = bp
            else:
                source_path = bp
        
        # Now process the image from source_path and write to dest_path
        with Image.open(source_path) as img:
            # Handle conversion for JPEG
            if (not convert_to_webp and ext in [".jpg", ".jpeg"]) or (convert_to_webp and ext in [".jpg", ".jpeg"]):
                if img.mode != "RGB":
                    img = img.convert("RGB")
                    
            if convert_to_webp:
                img.save(dest_path, "WEBP", quality=quality, method=6)
            elif ext in [".jpg", ".jpeg"]:
                img.save(dest_path, "JPEG", optimize=True, quality=quality, progressive=True)
            elif ext == ".png":
                if img.mode != "P" and img.mode in ("RGB", "RGBA"):
                    try:
                        quantized = img.quantize(colors=256)
                        quantized.save(dest_path, "PNG", optimize=True)
                    except Exception:
                        img.save(dest_path, "PNG", optimize=True, compress_level=9)
                else:
                    img.save(dest_path, "PNG", optimize=True, compress_level=9)
            elif ext == ".webp":
                img.save(dest_path, "WEBP", quality=quality, method=6)

        new_size = dest_path.stat().st_size
        saved_bytes = orig_size - new_size
        
        if saved_bytes > 0:
            saving_pct = (saved_bytes / orig_size) * 100
            print(f"[OPTIMIZED] {path.name} -> {dest_path.name}")
            print(f"  Size: {get_size_format(orig_size)} -> {get_size_format(new_size)} (-{saving_pct:.1f}%)")
            return orig_size, new_size
        else:
            # If the file didn't compress further (new size >= original), restore original
            if backup_path and backup_path.exists():
                if dest_path.exists():
                    os.remove(dest_path)
                os.rename(backup_path, dest_path)
            print(f"[SKIPPED]   {path.name} (Already optimized)")
            return orig_size, orig_size

    except Exception as e:
        print(f"[ERROR]     Could not optimize {path.name}: {e}")
        # Restore backup in case of half-saved/failed operations
        if 'backup_path' in locals() and backup_path and backup_path.exists():
            if path.exists():
                os.remove(path)
            os.rename(backup_path, path)
        return None


def main():
    parser = argparse.ArgumentParser(description="Optimize assets in a folder using Pillow.")
    parser.add_argument("directory", help="Path to the directory containing images (relative to project root)")
    parser.add_argument("--quality", type=int, default=85, help="JPEG/WebP quality setting (0-100, default: 85)")
    parser.add_argument("--webp", action="store_true", help="Convert JPEGs and PNGs to WebP format")
    parser.add_argument("--no-backup", action="store_true", help="Do not keep backups of replaced images")
    
    args = parser.parse_args()
    
    target_dir = PROJECT_ROOT / args.directory
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: '{target_dir}' is not a valid directory.")
        sys.exit(1)

    print(f"Scanning '{target_dir.relative_to(PROJECT_ROOT)}' for images...")
    
    supported_extensions = {".png", ".jpg", ".jpeg", ".webp"}
    image_files = []
    
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in supported_extensions and "_backup" not in file_path.name:
                image_files.append(file_path)

    if not image_files:
        print("No supported images found in the directory.")
        sys.exit(0)

    print(f"Found {len(image_files)} image files. Beginning optimization...\n")
    
    total_original = 0
    total_optimized = 0
    optimized_count = 0

    for file_path in image_files:
        result = optimize_image(
            file_path, 
            quality=args.quality, 
            convert_to_webp=args.webp,
            replace=True, 
            backup=not args.no_backup
        )
        if result:
            orig, new = result
            total_original += orig
            total_optimized += new
            optimized_count += 1

    print("\n" + "="*40)
    print("Optimization Summary:")
    print("="*40)
    print(f"Total Images Scanned:   {len(image_files)}")
    print(f"Total Optimized/Saved: {optimized_count}")
    if total_original > 0:
        saved = total_original - total_optimized
        pct = (saved / total_original) * 100
        print(f"Total Original Size:   {get_size_format(total_original)}")
        print(f"Total Optimized Size:  {get_size_format(total_optimized)}")
        print(f"Total Disk Space Saved: {get_size_format(saved)} (-{pct:.1f}%)")
    print("="*40)


if __name__ == "__main__":
    main()
