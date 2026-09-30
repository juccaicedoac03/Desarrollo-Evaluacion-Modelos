#!/usr/bin/env python3
"""Check that every relative link in the repository's ``*.html`` and ``*.md`` files exists.

Usage:
    python tools/check_links.py [root]        # root defaults to the repository root

What is checked
  * HTML: relative ``href=`` / ``src=`` attribute values (inline ``<script>`` bodies and
    ``<!-- comments -->`` are ignored).
  * Markdown: ``[text](target)`` and ``![alt](target)`` links, ``[ref]: target`` definitions and
    HTML ``href=`` / ``src=`` attributes (badges).  Fenced code blocks, inline code spans and
    HTML comments are ignored.
  * ``#fragment`` and ``?query`` are stripped, the path is resolved relative to the file and must
    exist (a directory link is fine when the directory exists).
  * Names are compared case-sensitively even on case-insensitive file systems (macOS), because
    GitHub Pages serves from a case-sensitive one.
  * In ``.html`` files a root-absolute link (``/assets/x.css``) is reported: on a GitHub Pages
    *project* site it resolves to the domain root, not to this repository.

Ignored: ``http:``, ``https:``, ``mailto:`` and any other ``scheme:`` link, protocol-relative
``//host`` links, pure ``#anchors``, ``.git``, ``.superpowers``, ``.claude``, ``instructor``,
``node_modules``, virtualenvs, caches (``.pytest_cache``, ``__pycache__``) and ``outputs``.

Prints each broken link as ``<file>:<line>: <link>`` and exits with status 1 if there is any.
"""
import argparse
import os
import re
import sys
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", ".superpowers", ".claude", "instructor", "node_modules", ".venv", "venv",
                 "__pycache__", ".ipynb_checkpoints", ".pytest_cache", "outputs"}
SUFFIXES = {".html", ".md"}

SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")
HTML_ATTR = re.compile(r"""(?<!\w)(?:href|src)\s*=\s*(?:"([^"]*)"|'([^']*)')""", re.I)
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
SCRIPT_ELEMENT = re.compile(r"(<script\b[^>]*>)(.*?)(</script\s*>)", re.S | re.I)
MD_INLINE = re.compile(r"\]\(\s*(<[^>\n]*>|[^)\s]*)")
MD_REFDEF = re.compile(r"^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]*>|\S+)", re.M)
MD_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
MD_CODE_SPAN = re.compile(r"(`+)(.+?)(?<!`)\1(?!`)")

ROOT_ABSOLUTE_NOTE = "  (root-absolute link: breaks on a GitHub Pages project site)"


# --------------------------------------------------------------------------- extraction
def blank_text(text):
    """Replace everything but newlines by spaces so line numbers stay valid."""
    return re.sub(r"[^\n]", " ", text)


def _blank(match):
    return blank_text(match.group(0))


def mask_markdown(text):
    """Blank fenced code blocks, inline code spans and HTML comments (line count preserved)."""
    out, fence = [], None
    for line in text.split("\n"):
        m = MD_FENCE.match(line)
        if fence is None:
            if m:
                fence = (m.group(1)[0], len(m.group(1)))
                out.append("")
            else:
                out.append(MD_CODE_SPAN.sub(_blank, line))
        else:
            closes = (m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1]
                      and line.strip() == m.group(1))
            if closes:
                fence = None
            out.append("")
    return HTML_COMMENT.sub(_blank, "\n".join(out))


def mask_html(text):
    """Blank comments and inline script bodies (line count preserved)."""
    text = HTML_COMMENT.sub(_blank, text)
    return SCRIPT_ELEMENT.sub(lambda m: m.group(1) + blank_text(m.group(2)) + m.group(3), text)


def extract_links(path, text):
    """Yield (link, line_number) for every candidate link in the file."""
    if path.suffix == ".md":
        masked = mask_markdown(text)
        matches = [(m.start(), m.group(1).strip("<>")) for pat in (MD_INLINE, MD_REFDEF)
                   for m in pat.finditer(masked)]
    else:
        masked = mask_html(text)
        matches = []
    matches += [(m.start(), m.group(1) if m.group(1) is not None else m.group(2))
                for m in HTML_ATTR.finditer(masked)]
    for pos, link in sorted(matches):
        yield link, masked.count("\n", 0, pos) + 1


# ------------------------------------------------------------------------------- checks
@lru_cache(maxsize=None)
def _listdir(directory):
    return frozenset(os.listdir(directory))


def exists_exact_case(root, target):
    """True if ``target`` exists and every component below ``root`` matches case exactly."""
    target = Path(os.path.normpath(target))
    if not target.exists():
        return False
    try:
        relative = target.relative_to(root)
    except ValueError:  # outside the repository: existence is all we can check
        return True
    current = root
    for part in relative.parts:
        if part not in _listdir(current):
            return False
        current = current / part
    return True


def broken_reason(root, file, link):
    """None if the link is fine or out of scope, otherwise a note ('' when nothing to add)."""
    link = link.strip()
    if not link or link.startswith("#") or link.startswith("//") or SCHEME.match(link):
        return None
    path = unquote(re.split(r"[?#]", link, maxsplit=1)[0])
    if not path:
        return None
    if path.startswith("/"):
        if file.suffix == ".html":
            return ROOT_ABSOLUTE_NOTE
        target = root / path.lstrip("/")
    else:
        target = file.parent / path
    return None if exists_exact_case(root, target) else ""


def find_files(root):
    for directory, subdirs, names in os.walk(root):
        subdirs[:] = sorted(d for d in subdirs if d not in EXCLUDED_DIRS)
        for name in sorted(names):
            if Path(name).suffix in SUFFIXES:
                yield Path(directory) / name


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("root", nargs="?", type=Path, default=ROOT,
                        help="directory to scan (default: repository root)")
    root = parser.parse_args(argv).root.resolve()

    files = links = 0
    broken = []
    for file in find_files(root):
        files += 1
        text = file.read_text(encoding="utf-8", errors="replace")
        for link, line in extract_links(file, text):
            links += 1
            note = broken_reason(root, file, link)
            if note is not None:
                broken.append(f"{file.relative_to(root)}:{line}: {link}{note}")

    for entry in broken:
        print(entry)
    if broken:
        print(f"{len(broken)} broken link(s) in {files} file(s) ({links} links checked)", file=sys.stderr)
        return 1
    print(f"OK: {links} links in {files} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
