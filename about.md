# pwntools について

pwntools を、エクスプロイトを書くために使うのか、別のソフトウェアプロジェクトの一部として使うのかで、使い方が変わります。

以前の pwntools は、エクスプロイトを書くための一種の DSL（専用言語）として使われていました。以前のバージョンでは、`from pwn import *` と書くだけで、いろいろな便利な副作用が起きました。

pwntools を 2.0 に作り直すとき、相反する 2 つの目標があることに気づきました。

- 「ふつうの」Python モジュールの構造にして、ほかの人が pwntools にすばやく慣れられるようにしたい。
- さらに多くの副作用を持たせたい。とくに、ターミナルを raw モード（入力を 1 文字ずつ、加工せずに受け取る状態）にしたい。

これを両立させるために、モジュールを 2 つに分けることにしました。[`pwnlib`](https://0xff-minusone.github.io/pwntools-api-ja/about.html#module-pwnlib) は、きれいな Python モジュールです。[`pwn`](https://0xff-minusone.github.io/pwntools-api-ja/about.html#module-pwn) は、CTF の最中に使うものです。

## `pwn` — CTF 向けに最適化した道具箱

先に述べたように、これらの副作用の多くを、最初から使えるようにもしたい、というのがこのモジュールの目的です。このモジュールは、次のことをします。

- トップレベルの `pwnlib` のすべてと、多くのサブモジュールの関数を import する。つまり、`import pwn` や `from pwn import *` と書けば、エクスプロイトを書くのに必要なものがすべて使えます。
- [`pwnlib.term.init`](https://0xff-minusone.github.io/pwntools-api-ja/term.html) を呼んで、ターミナルを raw モードにし、そうなっていないように見せる機能を実装する。
- [`pwnlib.context.log_level`](https://0xff-minusone.github.io/pwntools-api-ja/context.html) を `"info"` にする。
- [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) の値のうち、解釈できるものを解釈し、解釈できたものは取り除く。

## `pwnlib` — ふつうの Python ライブラリ

このモジュールは、「きれいな」Python コードです。原則として、`pwnlib` やそのサブモジュールを import しても、（キャッシュなどを除いて）目立った副作用があってはいけない、と考えています。

また、ほとんどの場合、import したものだけが手に入ります。たとえば、`import pwnlib.util` と書くだけでは、`pwnlib.util.packing` は使えません。

いくつか例外があります（たとえば `pwnlib.shellcraft`）。これは、「単純できれい」という目標に、あまり合いません。ただ、それらも、暗黙の副作用なしに import できます。
