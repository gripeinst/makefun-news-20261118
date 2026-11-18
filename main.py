#!/usr/bin/env python3
"""Submit the 18 November 2026 world-news front page to the grader.

The image is composed outside this program and shipped beside it; the program
only checks the artefact and copies it to the output directory the harness
gives it. It uses the Python standard library alone.
"""

from __future__ import annotations

import os
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_IMAGE_BYTES = 1024 * 1024


def main() -> None:
    bot_dir = Path(os.environ.get("MAKEFUN_BOT_DIR", "/bot"))
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

    image = (bot_dir / "entry.png").read_bytes()
    if not image.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png is not a PNG file")
    if len(image) > MAX_IMAGE_BYTES:
        raise SystemExit(f"entry.png is {len(image)} bytes, over the 1 MiB cap")

    width = int.from_bytes(image[16:20], "big")
    height = int.from_bytes(image[20:24], "big")
    if (width, height) != (1024, 1024):
        raise SystemExit(f"entry.png is {width}x{height}, expected 1024x1024")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(image)


if __name__ == "__main__":
    main()
