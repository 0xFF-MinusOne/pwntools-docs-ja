#!/usr/bin/env python3
"""ビルド用に Markdown を .site-src/ へコピーする。元のファイルは変更しない。
サイトに載せないファイルへの相対リンクは、GitHub 上のファイルへのリンクに書き換える。"""
import posixpath
import re
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent.parent
out = root / ".site-src"
REPO = "https://github.com/0xFF-MinusOne/" + root.name
if out.exists():
    shutil.rmtree(out)
out.mkdir()

files = sorted([*root.glob("*.md"), *root.glob("install/*.md")])
pages = {p.relative_to(root).as_posix() for p in files}
LINK = re.compile(r"(!?\[[^\]]*\])\(([^)\s]+)((?:\s+\"[^\"]*\")?)\)")


def make_rewrite(src):
    base = posixpath.dirname(src)

    def rewrite(m):
        label, target, title = m.group(1), m.group(2), m.group(3)
        if re.match(r"^([a-z][a-z0-9+.-]*:|#|/)", target, re.I):
            return m.group(0)
        path, _, frag = target.partition("#")
        rel = posixpath.normpath(posixpath.join(base, path))
        if rel in pages or not (root / rel).exists():
            return m.group(0)
        kind = "tree" if (root / rel).is_dir() else "blob"
        return f"{label}({REPO}/{kind}/main/{rel}" + (f"#{frag}" if frag else "") + f"{title})"

    return rewrite


for p in files:
    rel = p.relative_to(root).as_posix()
    dst = out / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(LINK.sub(make_rewrite(rel), p.read_text(encoding="utf-8")), encoding="utf-8")
print(f"prepared {sum(1 for _ in out.rglob('*') if _.is_file())} files in {out}")
