# `from pwn import *`

pwntools の使われ方として、最もよく見るのは、次の形です。

```python
>>> from pwn import *
```

これは、楽をするために、膨大な数のものを、グローバルの名前空間に import します。

以下は、import されるオブジェクトとルーチンの、ほとんどの一覧です。重要さと、使う頻度の、おおよその順に並べています。

- [`pwnlib.context`](https://0xff-minusone.github.io/pwntools-api-ja/context.html)
    - [`pwnlib.context.context`](https://0xff-minusone.github.io/pwntools-api-ja/context.html#pwnlib.context.context)
    - pwntools の便利な設定の、ほとんどを担っています
    - エクスプロイトの調子が悪いときは、`context.log_level = 'debug'` に設定します
    - スコープを意識するので、[`ContextType.local`](https://0xff-minusone.github.io/pwntools-api-ja/context.html#pwnlib.context.ContextType.local) で、コードの一部だけ、ログを無効にできます
- `remote`、`listen`、`ssh`、`process`
    - [`pwnlib.tubes`](https://0xff-minusone.github.io/pwntools-api-ja/tubes.html)
    - CTF のチャレンジで使う、よくある機能のすべてを、とても便利に包んでいます
    - どこにあるものにでも接続でき、思いどおりに動きます
    - `recvline`、`recvuntil`、`clean` などの、よくある作業の補助機能があります
    - `.interactive()` で、アプリケーションと直接やり取りできます
- `p32` と `u32`
    - [`pwnlib.util.packing`](https://0xff-minusone.github.io/pwntools-api-ja/util/packing.html)
    - `struct.pack` で `'>'` が、符号つきか、符号なしか、を覚えておく必要も、末尾の見苦しい `[0]` のインデックスも、なくなる便利な関数です
    - `signed` と `endian` を、分かりやすい形で設定します（これらは、`context` に一度設定すれば、もう気にしなくて済みます）
    - よく使うサイズは、あらかじめ定義されています（`u8`、`u64` など）。[`pwnlib.util.packing.pack`](https://0xff-minusone.github.io/pwntools-api-ja/util/packing.html#pwnlib.util.packing.pack) で、自分でサイズを決めることもできます
- `log`
    - [`pwnlib.log`](https://0xff-minusone.github.io/pwntools-api-ja/log.html)
    - 出力をきれいにします
- `cyclic` と `cyclic_func`
    - [`pwnlib.util.cyclic`](https://0xff-minusone.github.io/pwntools-api-ja/util/cyclic.html)
    - N バイト（たいてい 4 バイト）だけから、部分文字列のオフセットを見つけられるような文字列を作る道具です。単純なバッファオーバーフローで、とても役に立ちます。0x41414141 を見る代わりに、0x61616171 なら、バッファのオフセット 64 で EIP を制御できている、と分かります
- `asm` と `disasm`
    - [`pwnlib.asm`](https://0xff-minusone.github.io/pwntools-api-ja/asm.html)
    - 面倒なことなしに、アセンブリをバイト列に、またはその逆に、すばやく変換します
    - binutils を入れてある、どのアーキテクチャにも対応しています
    - 20 を超えるアーキテクチャ向けの、ビルド済みのバイナリが、[ppa:pwntools/binutils](https://launchpad.net/~pwntools/+archive/ubuntu/binutils) にあります
- `shellcraft`
    - [`pwnlib.shellcraft`](https://0xff-minusone.github.io/pwntools-api-ja/shellcraft.html)
    - すぐ使えるシェルコードのライブラリです
    - `asm(shellcraft.sh())` で、シェルが手に入ります
    - シェルコードの断片を再利用するための、テンプレートのライブラリです
- `ELF`
    - [`pwnlib.elf`](https://0xff-minusone.github.io/pwntools-api-ja/elf.html)
    - ELF バイナリを操作する道具です。シンボルの検索、仮想メモリからファイルオフセットへの変換の補助、バイナリを書き換えてディスクに保存する機能が入っています
- `DynELF`
    - [`pwnlib.dynelf`](https://0xff-minusone.github.io/pwntools-api-ja/dynelf.html)
    - 読み込まれているモジュールの、どれか 1 つへのポインタと、任意のアドレスのデータを漏洩（リーク）できる関数だけから、関数を動的に解決します
- `ROP`
    - [`pwnlib.rop`](https://0xff-minusone.github.io/pwntools-api-ja/rop.html)
    - 生のアドレスではなく、やりたいことを書く DSL（専用言語）を使って、ROP チェーンを自動で作ります
- `gdb.debug` と `gdb.attach`
    - [`pwnlib.gdb`](https://0xff-minusone.github.io/pwntools-api-ja/gdb.html)
    - バイナリを GDB の下で起動して、操作するための新しいターミナルを開きます。ブレークポイントの設定を自動化し、エクスプロイトの試行錯誤を、ずっと速くします
    - あるいは、PID、[`pwnlib.tubes`](https://0xff-minusone.github.io/pwntools-api-ja/tubes.html) のオブジェクト、さらには、それに接続しているソケットだけを渡して、実行中のプロセスにアタッチ（接続）できます
- `args`
    - すべて大文字のコマンドライン引数を、すばやく取り出すための辞書です
    - `python foo.py REMOTE=1` で実行すると、`args['REMOTE'] == '1'` になります
    - ログの詳細度や、ターミナルの派手さも、制御できます
        - `NOTERM`
        - `SILENT`
        - `DEBUG`
- `randoms`、`rol`、`ror`、`xor`、`bits`
    - [`pwnlib.util.fiddling`](https://0xff-minusone.github.io/pwntools-api-ja/util/fiddling.html)
    - 指定した文字の集合から、ランダムなデータを作る、あるいは、ふつうは `0xffffffff` でマスクしたり、`ord` と `chr` を、うんざりするほど呼んだりが必要な数値演算を、簡単にするための便利な道具です
- `net`
    - [`pwnlib.util.net`](https://0xff-minusone.github.io/pwntools-api-ja/util/net.html)
    - ネットワークインターフェースを調べるルーチンです
- `proc`
    - [`pwnlib.util.proc`](https://0xff-minusone.github.io/pwntools-api-ja/util/proc.html)
    - プロセスを調べるルーチンです
- `pause`
    - 新しい `getch`（1 文字入力を待つ関数）です
- `safeeval`
    - [`pwnlib.util.safeeval`](https://0xff-minusone.github.io/pwntools-api-ja/util/safeeval.html)
    - 嫌な副作用なしに、Python のコードを安全に評価するための関数です

これらは、どれも、名前から分かりやすいものですが、グローバルの名前空間にあると便利です。

- `hexdump`
- `read` と `write`
- `enhex` と `unhex`
- `more`
- `group`
- `align` と `align_down`
- `urlencode` と `urldecode`
- `which`
- `wget`

さらに、次のモジュールは、すべて自動で import されます。どうせ自分で import するつもりだったでしょう。

- `os`
- `sys`
- `time`
- `requests`
- `re`
- `random`
