#!/usr/bin/env python3
"""Entrypoint for the news-image-20261121 front page.

Copies the bundled front-page image to the output directory as
entry.png. The copy is byte-identical to the source every run, and the
program refuses to write anything that is not a complete JPEG under
the 1 MiB limit.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def jpeg_dimensions(data):
    """Read width and height from a JPEG's first SOF marker."""
    pos = 2
    while pos + 9 < len(data):
        if data[pos] != 0xFF:
            return None
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        size = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        pos += 2 + size
    return None


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SOURCE):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        print("entry.png exceeds the 1 MiB limit", file=sys.stderr)
        return 1
    if not data.startswith(b"\xff\xd8\xff") or not data.endswith(b"\xff\xd9"):
        print("entry.png is not a complete JPEG", file=sys.stderr)
        return 1
    dims = jpeg_dimensions(data)
    if dims is None:
        print("entry.png has no readable JPEG frame header", file=sys.stderr)
        return 1
    if dims[0] > MAX_SIDE or dims[1] > MAX_SIDE:
        print(f"entry.png is {dims[0]}x{dims[1]}, over the 1024x1024 cap",
              file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    with open(target, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        print("written copy does not match the source", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(written)} bytes, {dims[0]}x{dims[1]}, "
          f"sha256 {hashlib.sha256(written).hexdigest()[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
