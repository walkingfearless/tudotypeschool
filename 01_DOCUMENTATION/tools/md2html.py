#!/usr/bin/env python3
"""
md2html.py — Convert Markdown files to styled HTML documentation.

Usage:
    python3 md2html.py                        # convert all .md files in current dir
    python3 md2html.py notes.md               # convert a single file
    python3 md2html.py docs/*.md              # convert specific files
    python3 md2html.py --css custom.css *.md  # use a different stylesheet

Output HTML files are written next to the source .md files.
"""

import argparse
import glob
import os
import sys
import textwrap

try:
    import markdown
except ImportError:
    print("Installing 'markdown' package…")
    import subprocess
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "markdown", "--break-system-packages", "-q"]
    )
    import markdown


FOOTER_HTML = textwrap.dedent("""\
<footer class="doc-footer">
  <span class="footer-left">
    Type Design Workshop
    <span class="separator">|</span>
    UAlg 2026
  </span>
  <span>
    By <a href="https://www.linkedin.com/in/walkingfearless/" target="_blank" rel="noopener">João Miranda</a>
    <span class="separator">|</span>
    <a href="https://tudotype.com" target="_blank" rel="noopener">tudotype</a>
  </span>
</footer>
""")

HTML_TEMPLATE = textwrap.dedent("""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="{css_path}">
</head>
<body>
{body}
{footer}
</body>
</html>
""")


def md_to_html(md_path: str, css_path: str = "style.css") -> str:
    """Read a Markdown file and return a complete HTML string."""
    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    # Extract a title from the first H1, falling back to the filename
    title = os.path.splitext(os.path.basename(md_path))[0].replace("-", " ").replace("_", " ")
    for line in md_text.splitlines():
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            break

    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "codehilite", "toc", "smarty"],
        extension_configs={
            "codehilite": {"css_class": "highlight", "guess_lang": False},
        },
    )

    # Compute relative path from the HTML file to the CSS file
    return HTML_TEMPLATE.format(title=title, css_path=css_path, body=body, footer=FOOTER_HTML)


def convert_file(md_path: str, css_path: str = "style.css") -> str:
    """Convert a single .md file → .html and return the output path."""
    html_content = md_to_html(md_path, css_path)
    out_path = os.path.splitext(md_path)[0] + ".html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return out_path


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to styled HTML documentation."
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Markdown files to convert. If none given, converts all .md in the current directory.",
    )
    parser.add_argument(
        "--css",
        default="style.css",
        help="Path to the CSS stylesheet (default: style.css).",
    )
    args = parser.parse_args()

    md_files = args.files if args.files else sorted(glob.glob("*.md"))

    if not md_files:
        print("No .md files found.")
        sys.exit(0)

    for md_path in md_files:
        if not os.path.isfile(md_path):
            print(f"  ⚠  Skipping (not found): {md_path}")
            continue
        out = convert_file(md_path, css_path=args.css)
        print(f"  ✓  {md_path} → {out}")

    print(f"\nDone — {len(md_files)} file(s) processed.")


if __name__ == "__main__":
    main()
