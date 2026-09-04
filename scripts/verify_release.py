from __future__ import annotations

import os
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    with (ROOT / "pyproject.toml").open("rb") as file:
        version = tomllib.load(file)["project"]["version"]
    tag = os.environ.get("GITHUB_REF_NAME") or next((arg for arg in sys.argv[1:] if arg != "--"), None)
    expected = f"v{version}"
    if tag is None:
        raise RuntimeError("release tag is required")
    if tag != expected:
        raise RuntimeError(f"release tag {tag} does not match {expected}")
    sys.stdout.write(f"release tag {tag} matches package version\n")


if __name__ == "__main__":
    main()
