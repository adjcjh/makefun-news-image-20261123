#!/usr/bin/env python3
"""make.fun entry: Sum up 23 November's world news in one image.

Deterministic, network-free: copies the pre-made collage held in this
repository to /output/entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit(f"missing source image: {SRC}")
    os.makedirs(DST_DIR, exist_ok=True)
    # Copy via a temp file in the destination dir, then atomically rename,
    # so a failed run can never leave a partial /output/entry.png behind.
    tmp = os.path.join(DST_DIR, ".entry.png.tmp")
    shutil.copyfile(SRC, tmp)
    os.replace(tmp, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
