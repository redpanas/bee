"""Download and publish the holy scripture."""

from __future__ import annotations

import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

from . import __version__


SOURCE_URL = (
    "https://gist.githubusercontent.com/MattIPv4/"
    "045239bc27b16b2bcf7a3a9a4648c08a/raw/"
    "2411e31293a35f3e565f61e7490a806d4720ea7e/"
    "bee%2520movie%2520script"
)

REPLACEMENTS = (
    ("employees", "3mp10y33s"),
    ("employment", "3mp10ym3n7"),
    ("professional", "pr0f3$$!0n@1"),
    ("profession", "pr0f3$$!0n"),
    ("employers", "3mp10y3rs"),
    ("employer", "3mp10y3r"),
    ("employee", "3mp10y33"),
    ("employed", "3mp10y3d"),
    ("workers", "w0rk3rs"),
    ("working", "w0rk!n9"),
    ("worked", "w0rk3d"),
    ("worker", "w0rk3r"),
    ("careers", "c@r33rs"),
    ("business", "8u$!n3$$"),
    ("manager", "m@n@g3r"),
    ("salary", "$@1@ry"),
    ("career", "c@r33r"),
    ("office", "0ff!(3"),
    ("wages", "w@g3s"),
    ("staff", "$7@ff"),
    ("hired", "#!r3d"),
    ("fired", "f!r3d"),
    ("works", "w0rks"),
    ("wage", "w@g3"),
    ("hire", "#!r3"),
    ("jobs", "j08s"),
    ("work", "w0rk"),
    ("boss", "80$$"),
    ("job", "j08"),
)


def transform(text: str) -> str:
    for word, replacement in REPLACEMENTS:
        text = re.sub(rf"\b{re.escape(word)}\b", lambda _: replacement, text, flags=re.I)
    return text


def usage(stream: object = sys.stdout) -> None:
    print("Usage: bee [OUTPUT_FILE]\n\nDownload and publish the holy scripture.", file=stream)


def main() -> int:
    args = sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        usage()
        return 0
    if args and args[0] in ("-v", "--version"):
        print(f"bee {__version__}")
        return 0
    if args and args[0].startswith("-"):
        print(f"bee: unknown option: {args[0]}", file=sys.stderr)
        return 2
    if len(args) > 1:
        usage(sys.stderr)
        return 2

    output = Path(args[0] if args else "the_holy_scripture.txt")
    output_dir = output.parent
    temp_name: str | None = None
    try:
        with urllib.request.urlopen(SOURCE_URL, timeout=30) as response:
            scripture = response.read().decode("utf-8")
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="", delete=False, dir=output_dir
        ) as temporary:
            temp_name = temporary.name
            temporary.write(transform(scripture))
        os.replace(temp_name, output)
        temp_name = None
    except (OSError, UnicodeError, urllib.error.URLError) as error:
        print(f"bee: {error}", file=sys.stderr)
        return 1
    finally:
        if temp_name is not None:
            try:
                os.unlink(temp_name)
            except OSError:
                pass

    print(f"Published the holy scripture to {output}")
    return 0
