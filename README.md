> **これは日本語訳です。**
>
> - 原著: [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) の公式ドキュメント（`docs/source/`、`dev` ブランチ、コミット `ed3f217`）。公開ページ: <https://docs.pwntools.com/en/dev/>
> - ライセンス: MIT — 翻訳も同じライセンスです（[ライセンス全文](LICENSE)）。原文から翻訳（変更）しています。pwntools には、一部に GPL や BSD のコードがありますが、それは `pwnlib/constants/` と `pwnlib/data/` の中だけで、ドキュメントの原稿は対象外です
> - 訳した範囲: 読み物のページ（このページ、このドキュメントについて、インストール、はじめに、`from pwn import *`、コマンドラインツール）
> - API リファレンス: モジュールごとのページ（コードの docstring から作られるもの）は、別の日本語訳 [pwntools-api-ja](https://0xff-minusone.github.io/pwntools-api-ja/) にあります。このドキュメントのリンクは、その日本語版に向いています。機械的に抜き出した文を訳しているので、訳していない部分は英語のままです
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

各モジュールの API リファレンスは、[日本語訳のサイト](https://0xff-minusone.github.io/pwntools-api-ja/)にあります。

- [adb](https://0xff-minusone.github.io/pwntools-api-ja/adb.html)
- [args](https://0xff-minusone.github.io/pwntools-api-ja/args.html)
- [asm](https://0xff-minusone.github.io/pwntools-api-ja/asm.html)
- [atexception](https://0xff-minusone.github.io/pwntools-api-ja/atexception.html)
- [atexit](https://0xff-minusone.github.io/pwntools-api-ja/atexit.html)
- [constants](https://0xff-minusone.github.io/pwntools-api-ja/constants.html)
- [config](https://0xff-minusone.github.io/pwntools-api-ja/config.html)
- [context](https://0xff-minusone.github.io/pwntools-api-ja/context.html)
- [dynelf](https://0xff-minusone.github.io/pwntools-api-ja/dynelf.html)
- [encoders](https://0xff-minusone.github.io/pwntools-api-ja/encoders.html)
- [elf](https://0xff-minusone.github.io/pwntools-api-ja/elf.html)
- [exception](https://0xff-minusone.github.io/pwntools-api-ja/exception.html)
- [filepointer](https://0xff-minusone.github.io/pwntools-api-ja/filepointer.html)
- [filesystem](https://0xff-minusone.github.io/pwntools-api-ja/filesystem.html)
- [flag](https://0xff-minusone.github.io/pwntools-api-ja/flag.html)
- [fmtstr](https://0xff-minusone.github.io/pwntools-api-ja/fmtstr.html)
- [gdb](https://0xff-minusone.github.io/pwntools-api-ja/gdb.html)
- [libc](https://0xff-minusone.github.io/pwntools-api-ja/libc.html)
- [libcdb](https://0xff-minusone.github.io/pwntools-api-ja/libcdb.html)
- [log](https://0xff-minusone.github.io/pwntools-api-ja/log.html)
- [memleak](https://0xff-minusone.github.io/pwntools-api-ja/memleak.html)
- [protocols](https://0xff-minusone.github.io/pwntools-api-ja/protocols.html)
- [qemu](https://0xff-minusone.github.io/pwntools-api-ja/qemu.html)
- [regsort](https://0xff-minusone.github.io/pwntools-api-ja/regsort.html)
- [replacements](https://0xff-minusone.github.io/pwntools-api-ja/replacements.html)
- [rop](https://0xff-minusone.github.io/pwntools-api-ja/rop.html)
- [runner](https://0xff-minusone.github.io/pwntools-api-ja/runner.html)
- [shellcraft](https://0xff-minusone.github.io/pwntools-api-ja/shellcraft.html)
- [term](https://0xff-minusone.github.io/pwntools-api-ja/term.html)
- [timeout](https://0xff-minusone.github.io/pwntools-api-ja/timeout.html)
- [tubes](https://0xff-minusone.github.io/pwntools-api-ja/tubes.html)
- [ui](https://0xff-minusone.github.io/pwntools-api-ja/ui.html)
- [update](https://0xff-minusone.github.io/pwntools-api-ja/update.html)
- [useragents](https://0xff-minusone.github.io/pwntools-api-ja/useragents.html)
- [util（ユーティリティ群）](https://0xff-minusone.github.io/pwntools-api-ja/util/packing.html)
- [windbg](https://0xff-minusone.github.io/pwntools-api-ja/windbg.html)

## バイト列と文字列（Bytes）

バイト列（bytes）と文字列（text）の違いは、とても大切なので、このトップページにまで載せています。
この違いを、これでようやくはっきり説明した（はず）の最新のチュートリアルは、[pwntools-tutorial](https://github.com/Gallopsled/pwntools-tutorial/blob/master/bytes.md) のリポジトリにあります。

> **訳注**: このチュートリアルの日本語訳は、[バイト列と文字列](https://0xff-minusone.github.io/pwntools-tutorial-ja/bytes/)です。
