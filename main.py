#!/usr/bin/env python3
"""make.fun entry: Sum up 23 November's world news in one image.

Deterministic, network-free: copies the pre-made collage held in this
repository to /output/entry.png.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def validate_png(path):
    """Check the source is a complete PNG of the required size.

    Guards against silently submitting a corrupt or wrong-sized image:
    a truncated file, a non-PNG, or wrong dimensions all fail loudly
    before anything is written to /output.
    """
    with open(path, "rb") as f:
        header = f.read(8)
        if header != PNG_SIGNATURE:
            raise SystemExit(f"invalid source image (not a PNG): {path}")
        chunk_header = f.read(8)
        if len(chunk_header) < 8:
            raise SystemExit(f"invalid source image (truncated): {path}")
        length, chunk_type = struct.unpack(">I4s", chunk_header)
        if chunk_type != b"IHDR" or length != 13:
            raise SystemExit(f"invalid source image (no IHDR chunk): {path}")
        ihdr = f.read(13)
        if len(ihdr) < 13:
            raise SystemExit(f"invalid source image (truncated IHDR): {path}")
        width, height = struct.unpack(">II", ihdr[:8])
        if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
            raise SystemExit(
                f"invalid source image (expected "
                f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}, got {width}x{height}): {path}"
            )


def main():
    if not os.path.isfile(SRC):
        raise SystemExit(f"missing source image: {SRC}")
    validate_png(SRC)
    os.makedirs(DST_DIR, exist_ok=True)
    # Copy via a temp file in the destination dir, then atomically rename,
    # so a failed run can never leave a partial /output/entry.png behind.
    tmp = os.path.join(DST_DIR, ".entry.png.tmp")
    shutil.copyfile(SRC, tmp)
    os.replace(tmp, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
