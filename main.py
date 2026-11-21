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
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1_048_576


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
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    with open(target, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        print("written copy does not match the source", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(written)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
