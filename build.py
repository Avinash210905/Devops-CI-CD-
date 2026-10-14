"""Build the static site into dist/ for GitHub Pages."""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "index.html"
OUTPUT = ROOT / "dist"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit("Build failed: index.html is missing")
    OUTPUT.mkdir(exist_ok=True)
    shutil.copy2(SOURCE, OUTPUT / "index.html")
    print("Built site: dist/index.html")


if __name__ == "__main__":
    main()
