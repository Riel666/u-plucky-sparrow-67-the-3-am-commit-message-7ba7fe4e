"""One commit message an AI agent would write after breaking production at 3 AM, under 200 characters.
"""

import os

TEXT = "fix: revert my 3 AM 'improvement' — prod is down, the tests passed, and I have no further comment at this time"


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
