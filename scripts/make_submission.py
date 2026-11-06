"""Bundle the code submission into dist/ and copy the compiled report next to it.

Usage (from repo root):  python scripts/make_submission.py

Per the guidelines, the zip holds all programming files (source, scripts, helpers,
dataset) and must NOT contain the report PDF.
"""

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
ZIP_NAME = "MTE544_A2_code.zip"
REPORT_PDF = ROOT / "report" / "main.pdf"

INCLUDE_DIRS = ["code", "scripts"]
INCLUDE_FILES = ["requirements.txt"]
EXCLUDE_PARTS = {"__pycache__", ".ipynb_checkpoints"}
EXCLUDE_SUFFIXES = {".pyc", ".pdf"}


def main():
    DIST.mkdir(exist_ok=True)
    zip_path = DIST / ZIP_NAME

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for d in INCLUDE_DIRS:
            for f in sorted((ROOT / d).rglob("*")):
                if not f.is_file() or f.name == ".gitkeep":
                    continue
                if EXCLUDE_PARTS & set(f.parts) or f.suffix in EXCLUDE_SUFFIXES:
                    continue
                zf.write(f, f.relative_to(ROOT))
        for name in INCLUDE_FILES:
            zf.write(ROOT / name, name)

    print(f"Wrote {zip_path}")
    with zipfile.ZipFile(zip_path) as zf:
        for n in zf.namelist():
            print("  ", n)

    if REPORT_PDF.exists():
        shutil.copy(REPORT_PDF, DIST / "MTE544_A2_report.pdf")
        print(f"Copied report to {DIST / 'MTE544_A2_report.pdf'}")
    else:
        print("Report PDF not found - build it with: cd report && latexmk -pdf main.tex")


if __name__ == "__main__":
    main()
