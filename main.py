"""The 3 AM Excuse — make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes one line (<200 chars) to /output/entry.txt: the excuse a hardware
wallet gives for refusing to sign a transaction at 3 AM.

Standard library only (Python 3.13 grading sandbox installs nothing).
"""

import os

# The angle: the wallet runs a 3 AM sobriety test on its owner — its USB
# port doubles as a breathalyzer. The hour is the joke (it could not be
# pasted onto a 3 PM transaction), the voice is the device's own, and the
# punchline lands in one breath: the owner cannot even spell "sleep".
# No trailing newline: the gate counts every character in entry.txt.

ENTRY = (
    "Blow into my USB port. If you can spell 'seed phrase' backwards "
    "at 3 AM, I'll sign. You can't even spell 'sleep'."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
