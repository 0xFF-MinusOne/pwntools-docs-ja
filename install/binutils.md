# Binutils

他のアーキテクチャのアセンブル（たとえば、Mac OS X で Sparc のシェルコードをアセンブルする）には、クロスコンパイル版の `binutils` が必要です。この手順は、できるだけ簡単にしてあります。

以下の例では、`$ARCH` を、対象のアーキテクチャ（たとえば arm、aarch64、mips64、vax など）に置き換えてください。

`binutils` をソースからビルドするのに、最近の 8 コアのマシンで 60 秒ほどかかります。

## Ubuntu

Ubuntu 12.04 から 15.10 では、先に pwntools の [Personal Package Archive リポジトリ](https://launchpad.net/~pwntools/+archive/ubuntu/binutils)を追加する必要があります。

Ubuntu Xenial（16.04）には、ほとんどのアーキテクチャの公式パッケージがあるので、この手順は要りません。

```bash
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:pwntools/binutils
$ sudo apt-get update
```

そのあと、対象のアーキテクチャの binutils を入れます。

```bash
$ sudo apt-get install binutils-$ARCH-linux-gnu
```

## Mac OS X

Mac OS X も同じくらい簡単ですが、binutils をソースからビルドする必要があります。ただ、2 つのコマンドで済むように、`homebrew` のレシピを用意しています。[brew](https://brew.sh) を入れたら、[binutils のリポジトリ](https://github.com/Gallopsled/pwntools-binutils/)から、適切なレシピを取ってきます。

```bash
$ wget https://raw.githubusercontent.com/Gallopsled/pwntools-binutils/master/macos/binutils-$ARCH.rb
$ brew install ./binutils-$ARCH.rb
```

注: pwntools/pwntools の Homebrew tap は、現在（2026 年 8 月）、移行の最中です。Mac OS で問題が起きたら、`brew install ...` の前に、`export HOMEBREW_DEVELOPER="true"` を実行してみてください。tap の移行の最終的な解決は、まだ決まっていません。

## Windows

Windows のサポートは、実験的なものです。目的のアーキテクチャ向けに、ビルド済みの binutils を、[GNU Toolchains](https://gnutoolchains.com/) のプロジェクトから入れてみてください。

注: x86 と x86_64 では、コマンドラインの扱いの違いのため、MinGW のツールチェーンではなく、[ubuntu のツールチェーン](https://gnutoolchains.com/ubuntu/)を使ってください。

## そのほかの OS

すべて手でビルドしたい場合や、上のどの OS も使っていない場合は、`binutils` は、手でビルドするのも簡単です。

```bash
#!/usr/bin/env bash

V=2.38   # Binutils Version
ARCH=arm # Target architecture

cd ${TMPDIR:-/tmp}
wget -nc https://ftp.gnu.org/gnu/binutils/binutils-$V.tar.gz
wget -nc https://ftp.gnu.org/gnu/binutils/binutils-$V.tar.gz.sig

gpg --keyserver keys.gnupg.net --recv-keys 4AE55E93
gpg --verify binutils-$V.tar.gz.sig

tar xf binutils-$V.tar.gz

mkdir binutils-build
cd binutils-build

export AR=ar
export AS=as

../binutils-$V/configure \
    --prefix=${PREFIX:-/usr/local} \
    --target=$ARCH-unknown-linux-gnu \
    --disable-static \
    --disable-multilib \
    --disable-werror \
    --disable-nls

MAKE=gmake
hash gmake || MAKE=make

$MAKE -j clean all
sudo $MAKE install
```
