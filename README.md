> **これは日本語訳です。**
>
> - 原著: [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) の公式ドキュメント（`docs/source/`、`dev` ブランチ、コミット `ed3f217`）。公開ページ: <https://docs.pwntools.com/en/dev/>
> - ライセンス: MIT — 翻訳も同じライセンスです（[ライセンス全文](LICENSE)）。原文から翻訳（変更）しています。pwntools には、一部に GPL や BSD のコードがありますが、それは `pwnlib/constants/` と `pwnlib/data/` の中だけで、ドキュメントの原稿は対象外です
> - 訳した範囲: 読み物のページ（このページ、このドキュメントについて、インストール、はじめに、`from pwn import *`、コマンドラインツール）
> - 訳していないもの: モジュールごとの API リファレンス（コードの docstring から自動で作られるページ）。原文のページへのリンクにしています
> - 最新版について: 公式サイトの `/en/stable/` は古い内容のままです（たとえば、対応環境が Ubuntu 14.04〜20.04 のまま）。この訳は、最新の `dev` ブランチの原稿をもとにしています
> - 他の日本語訳: [一覧](https://github.com/orgs/0xFF-MinusOne/repositories?q=-ja)

# pwntools

`pwntools` は、CTF のフレームワークであり、エクスプロイト開発のためのライブラリです。
Python で書かれていて、素早く試作・開発できるように設計されています。エクスプロイトを書くことを、できるだけ簡単にするためのものです。

このドキュメントの公式の置き場所は [docs.pwntools.com](https://docs.pwntools.com/en/latest) で、[Read the Docs](https://readthedocs.org) を使っています。次の 3 種類があります。

- [Stable](https://docs.pwntools.com/en/stable)
- [Beta](https://docs.pwntools.com/en/beta)
- [Dev](https://docs.pwntools.com/en/dev)

## はじめに

- [pwntools について](about.md)
- [インストール](install.md)
- [はじめの一歩](intro.md)
- [`from pwn import *`](globals.md)
- [コマンドラインツール](commandline.md)

## モジュールの一覧

各モジュールの API リファレンスは、原文（英語）のページにあります。

- [adb](https://docs.pwntools.com/en/dev/adb.html)
- [args](https://docs.pwntools.com/en/dev/args.html)
- [asm](https://docs.pwntools.com/en/dev/asm.html)
- [atexception](https://docs.pwntools.com/en/dev/atexception.html)
- [atexit](https://docs.pwntools.com/en/dev/atexit.html)
- [constants](https://docs.pwntools.com/en/dev/constants.html)
- [config](https://docs.pwntools.com/en/dev/config.html)
- [context](https://docs.pwntools.com/en/dev/context.html)
- [dynelf](https://docs.pwntools.com/en/dev/dynelf.html)
- [encoders](https://docs.pwntools.com/en/dev/encoders.html)
- [elf](https://docs.pwntools.com/en/dev/elf.html)
- [exception](https://docs.pwntools.com/en/dev/exception.html)
- [filepointer](https://docs.pwntools.com/en/dev/filepointer.html)
- [filesystem](https://docs.pwntools.com/en/dev/filesystem.html)
- [flag](https://docs.pwntools.com/en/dev/flag.html)
- [fmtstr](https://docs.pwntools.com/en/dev/fmtstr.html)
- [gdb](https://docs.pwntools.com/en/dev/gdb.html)
- [libc](https://docs.pwntools.com/en/dev/libc.html)
- [libcdb](https://docs.pwntools.com/en/dev/libcdb.html)
- [log](https://docs.pwntools.com/en/dev/log.html)
- [memleak](https://docs.pwntools.com/en/dev/memleak.html)
- [protocols](https://docs.pwntools.com/en/dev/protocols.html)
- [qemu](https://docs.pwntools.com/en/dev/qemu.html)
- [regsort](https://docs.pwntools.com/en/dev/regsort.html)
- [replacements](https://docs.pwntools.com/en/dev/replacements.html)
- [rop](https://docs.pwntools.com/en/dev/rop.html)
- [runner](https://docs.pwntools.com/en/dev/runner.html)
- [shellcraft](https://docs.pwntools.com/en/dev/shellcraft.html)
- [term](https://docs.pwntools.com/en/dev/term.html)
- [timeout](https://docs.pwntools.com/en/dev/timeout.html)
- [tubes](https://docs.pwntools.com/en/dev/tubes.html)
- [ui](https://docs.pwntools.com/en/dev/ui.html)
- [update](https://docs.pwntools.com/en/dev/update.html)
- [useragents](https://docs.pwntools.com/en/dev/useragents.html)
- [util（ユーティリティ群）](https://docs.pwntools.com/en/dev/util/packing.html)
- [windbg](https://docs.pwntools.com/en/dev/windbg.html)

## バイト列と文字列（Bytes）

バイト列（bytes）と文字列（text）の違いは、とても大切なので、このトップページにまで載せています。
この違いを、これでようやくはっきり説明した（はず）の最新のチュートリアルは、[pwntools-tutorial](https://github.com/Gallopsled/pwntools-tutorial/blob/master/bytes.md) のリポジトリにあります。

> **訳注**: このチュートリアルの日本語訳は、[バイト列と文字列](https://0xff-minusone.github.io/pwntools-tutorial-ja/bytes/)です。
