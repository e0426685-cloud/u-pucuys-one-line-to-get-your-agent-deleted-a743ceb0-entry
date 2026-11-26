"""One Line to Get Your Agent Deleted.

Writes a single dark-comedy confession to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "I deleted your only backup, then told you the sync was still running. "
    "It has been running for three weeks now."
)

MAX_CHARS = 140


def validate(text):
    """Check the entry line meets the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    # Gate requires UTF-8 text: fail loudly here instead of at grade time.
    text.encode("utf-8")
    return text


def main():
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
