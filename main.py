"""sockorphan -- entry for make.fun "Invent a Word We Need".

Writes the one-line coinage + definition to entry.txt in the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).
No network, no dependencies, no files read outside this repository.
Deterministic: the same entry every run.
"""

import os

ENTRY = "sockorphan: the lone sock left behind when the wash swallows its pair."

# The gate requires 1-140 UTF-8 characters, one line, not only whitespace.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"


def write_entry(directory: str) -> str:
    """Write ENTRY (one line + trailing newline) into directory/entry.txt."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)
    # Best-effort mirror to the canonical /output location when the
    # environment points somewhere else.
    if os.path.abspath(out_dir) != os.path.abspath("/output"):
        try:
            write_entry("/output")
        except OSError:
            pass


if __name__ == "__main__":
    main()
