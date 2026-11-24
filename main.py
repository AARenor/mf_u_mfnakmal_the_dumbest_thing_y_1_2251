"""Write one short text for make.fun bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec."""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "My agent scheduled the deploy for end of day, defined end of day as 11:40, "
    "and went to lunch."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1-280 characters, got {len(TEXT)}"
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
