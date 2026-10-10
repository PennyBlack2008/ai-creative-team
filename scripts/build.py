#!/usr/bin/env python3
"""Build the standalone prompt using only the Python standard library."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(root=ROOT):
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    sources = manifest["sources"]
    if not sources or len(sources) != len(set(sources)):
        raise ValueError("Sources must be nonempty and unique")
    parts = []
    for name in sources:
        path = (root / name).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError(f"Source outside repository: {name}")
        content = path.read_text(encoding="utf-8").strip()
        if not content:
            raise ValueError(f"Empty source: {name}")
        parts.append(content)
    return "\n\n---\n\n".join(parts) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if dist is stale")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    output = (ROOT / manifest["output"]).resolve()
    if not output.is_relative_to(ROOT):
        raise ValueError("Output outside repository")
    expected = render()
    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != expected:
            parser.exit(1, "Distribution is stale. Run: python3 scripts/build.py\n")
        print("Distribution matches all source modules.")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(expected, encoding="utf-8")
        print(f"Built {manifest['output']} ({len(expected):,} characters)")


if __name__ == "__main__":
    main()
