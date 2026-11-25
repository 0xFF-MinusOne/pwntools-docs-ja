# インストール

pwntools は、64 ビットの Ubuntu LTS（22.04 と 24.04）で、最もよくサポートされています。ほとんどの機能は、Posix 系のどのディストリビューション（Debian、Arch、FreeBSD、OSX など）でも動くはずです。

## 前提

`pwntools` を最大限に活用するために、次のシステムライブラリを入れておくと良いです。

- [Binutils](install/binutils.md)
- [Python の開発用ヘッダー](install/headers.md)

注: Mac OS X では、cmake（`brew install cmake`）と pkg-config（`brew install pkg-config`）が必要です。

```bash
brew install pwntools
```

## リリース版

pwntools は、Python 3 用の `pip` パッケージとして配布されています。バージョン v5.0.0 は、Python 3.10 以降に対応しています。それより古い Python を使う場合は、v4 を使ってください。

### Python 3

pwntools のインストールに必要な Python のバージョンは、できる範囲で低く保たれています。ただし、新しい機能は、Python 3.10 以降を対象にしています。

```bash
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade pwntools
```

### Python 2（非推奨）

Python 2 のサポートは、Pwntools v5.0.0 で削除されました。Python 2 に対応した最後のバージョンは v4.15.0 です。

注: Pwntools のメンテナーは、今後の Pwntools を使うスクリプトやプロジェクトでは、すべて Python 3 を使うことを、強く推奨します。

また、`pip` が Python 2 のサポートをやめたので、特定のバージョンの `pip` を入れる必要があります。

```bash
$ sudo apt-get update
$ sudo apt-get install python python-pip python-dev git libssl-dev libffi-dev build-essential
$ python2 -m pip install --upgrade pip==20.3.4
$ python2 -m pip install --upgrade pwntools
```

## コマンドラインツール

上のコマンドを `sudo` つきで実行すると、Pwntools のコマンドラインツールが、`/usr/bin` のような場所に入ります。

ただし、特権のないユーザーで実行すると、次のような警告が出ることがあります。

```
WARNING: The scripts asm, checksec, common, constgrep, cyclic, debug, disablenx, disasm, 
elfdiff, elfpatch, errno, hex, main, phd, pwn, pwnstrip, scramble, shellcraft, template, 
unhex, update and version are installed in '/home/user/.local/bin' which is not on PATH.
```

表示された指示に従って、`~/.local/bin` を、環境変数 `$PATH` に追加してください。

## 開発する場合

手元で Pwntools を開発する場合は、次のようにします。

```bash
$ git clone https://github.com/Gallopsled/pwntools
$ pip install --upgrade --editable ./pwntools
```
