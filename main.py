"""Entry for make.fun bounty u-po-pu-say-what-actually-broke-a2c153b5.

Writes one line of brutally honest error copy to /output/entry.txt.
Standard library only; deterministic: the same line every run.
"""

import os

LINE = (
    "Deploy #482 deleted the production database. "
    "Our last backup is from 2021 and has never been restored. "
    "Your data is in a better place now. Please start over."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
