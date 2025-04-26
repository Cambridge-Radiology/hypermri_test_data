#!/usr/bin/env python3
import subprocess
import sys

"""
Pre-commit script: ensure all binary files are tracked by Git LFS.
When an error is found, prints suggestions on how to fix.
"""


def is_lfs_tracked(path):
    out = subprocess.check_output(["git", "check-attr", "-z", "filter", "--", path])
    return b"filter\x00lfs" in out


def is_probably_text(path, blocksize=1024):
    try:
        with open(path, "rb") as f:
            chunk = f.read(blocksize)
            # Allow UTF-8 BOM
            chunk = chunk.lstrip(b"\xef\xbb\xbf")
            # Try decoding as UTF-8
            chunk.decode("utf-8")
            return True
    except (UnicodeDecodeError, OSError):
        return False


errors = []
tracked_files = subprocess.check_output(["git", "ls-files"]).decode().splitlines()

for path in tracked_files:
    if path in (
        ".gitattributes",
        ".gitignore",
        ".pre-commit-config.yaml",
    ) or path.startswith(".github/"):
        continue
    if is_lfs_tracked(path):
        continue
    if is_probably_text(path):
        continue
    errors.append(path)

if errors:
    print("❌ ERROR: Found binary files not tracked by LFS:", file=sys.stderr)
    for p in errors:
        print(f"  • {p}", file=sys.stderr)

    # User suggestions
    print("\n👉 To fix each file individually, run:", file=sys.stderr)
    print('    git lfs track "<file>"', file=sys.stderr)
    print('    git add .gitattributes "<file>"', file=sys.stderr)
    print('    git commit -m "Track <file> with Git LFS"', file=sys.stderr)

    print("\n👉 To track all files by extension (e.g. PNG), run:", file=sys.stderr)
    print('    git lfs track "*.png"', file=sys.stderr)

    sys.exit(1)
else:
    print("✅ All committed files are either plain text or tracked by LFS.")
    sys.exit(0)
