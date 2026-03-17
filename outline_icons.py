from pathlib import Path
import re

ICON_DIR = Path("assets/icons")

# Add/override these attributes on every <path ...> tag
ATTRS = {
    "fill": "#000000",
    "stroke": "#FFFFFF",
    "stroke-width": "1.2",
    "stroke-linejoin": "miter",
    "stroke-linecap": "square",
    "paint-order": "stroke fill",
}

PATH_TAG_RE = re.compile(r"<path\b[^>]*?>")

def upsert_attr(tag: str, key: str, value: str) -> str:
    # If attribute exists, replace it; otherwise insert it before the closing >
    attr_re = re.compile(rf'(\s{re.escape(key)}=)(["\']).*?\2')
    if attr_re.search(tag):
        return attr_re.sub(rf' {key}="{value}"', tag)
    # Insert before final '>' (or '/>')
    return tag[:-1] + f' {key}="{value}">'

def main():
    if not ICON_DIR.exists():
        raise SystemExit(f"Missing directory: {ICON_DIR}")

    svgs = sorted(ICON_DIR.glob("*.svg"))
    if not svgs:
        raise SystemExit(f"No SVGs found in {ICON_DIR}")

    for svg_path in svgs:
        text = svg_path.read_text(encoding="utf-8")

        def repl(match):
            tag = match.group(0)
            # Don’t touch clipPath, etc. (we only match <path>)
            for k, v in ATTRS.items():
                tag = upsert_attr(tag, k, v)
            return tag

        new_text = PATH_TAG_RE.sub(repl, text)

        if new_text != text:
            svg_path.write_text(new_text, encoding="utf-8")
            print(f"updated: {svg_path}")
        else:
            print(f"no change: {svg_path}")

if __name__ == "__main__":
    main()