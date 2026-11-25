# はじめの一歩

pwntools に慣れるために、まず、いくつかの例を見ていきましょう。

エクスプロイトを書くとき、pwntools は、基本的に「キッチンシンク」方式（全部入り）の方針をとります。

```python
>>> from pwn import *
```

これで、多くの機能がグローバルの名前空間に import されます。アセンブル、逆アセンブル、パック、アンパックなど、多くのことを、1 つの関数で行えるようになります。

import されるもの全部の一覧は、[`from pwn import *`](globals.md) にあります。

## チュートリアル

Pwntools のチュートリアルが、オンラインにあります。
<https://github.com/Gallopsled/pwntools-tutorial#readme>

> **訳注**: このチュートリアルの日本語訳は、[Pwntools チュートリアル（日本語訳）](https://0xff-minusone.github.io/pwntools-tutorial-ja/)です。ただし、原著のチュートリアルは 2021 年ごろから更新されておらず、古い記述が残っています。最新の情報は、このドキュメントを優先してください。

## 接続する

チャレンジのバイナリを pwn するには、そのバイナリと話す必要がありますよね。
pwntools の [`pwnlib.tubes`](https://docs.pwntools.com/en/dev/tubes.html) モジュールを使えば、これがとても簡単です。

このモジュールは、プロセス、ソケット、シリアルポートなど、あらゆるものと話すための標準のインターフェースと、よくある作業のための便利な補助機能を提供します。たとえば、[`pwnlib.tubes.remote`](https://docs.pwntools.com/en/dev/tubes/sockets.html) を使ったリモート接続です。

```python
>>> conn = remote('ftp.ubuntu.com',21)
>>> conn.recvline()
b'220 ...'
>>> conn.send(b'USER anonymous\r\n')
>>> conn.recvuntil(b' ', drop=True)
b'331'
>>> conn.recvline()
b'Please specify the password.\r\n'
>>> conn.close()
```

待ち受け側（リスナー）を立てるのも簡単です。

```python
>>> l = listen()
>>> r = remote('localhost', l.lport)
>>> c = l.wait_for_connection()
>>> r.send(b'hello')
>>> c.recv()
b'hello'
```

プロセスとのやり取りも、[`pwnlib.tubes.process`](https://docs.pwntools.com/en/dev/tubes/processes.html) のおかげで簡単です。

```python
>>> sh = process('/bin/sh')
>>> sh.sendline(b'sleep 3; echo hello world;')
>>> sh.recvline(timeout=1)
b''
>>> sh.recvline(timeout=5)
b'hello world\n'
>>> sh.close()
```

プロセスと、プログラムからやり取りできるだけでなく、プロセスと実際に**対話**することもできます。

```python
>>> sh.interactive()
$ whoami
user
```

ローカルや setuid のエクスプロイトを実行するために、ボックスへ SSH で入る必要があるとき用の、SSH モジュールもあります（[`pwnlib.tubes.ssh`](https://docs.pwntools.com/en/dev/tubes/ssh.html)）。プロセスをすばやく起動して出力を取ったり、プロセスを起動して、`process` の tube のように、それと対話したりできます。

```python
>>> shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)
>>> shell['whoami']
b'bandit0'
>>> shell.download_file('/etc/motd')
>>> sh = shell.run('sh')
>>> sh.sendline(b'sleep 3; echo hello world;')
>>> sh.recvline(timeout=1)
b''
>>> sh.recvline(timeout=5)
b'hello world\n'
>>> shell.close()
```

## 整数のパック

エクスプロイトを書くときによくある作業は、Python が扱う整数と、バイト列としての表現とを、相互に変換することです。
たいていは、組み込みの `struct` モジュールを使います。

pwntools は、[`pwnlib.util.packing`](https://docs.pwntools.com/en/dev/util/packing.html) で、これを簡単にします。アンパックのコードを覚える必要も、補助ルーチンでコードを散らかす必要も、もうありません。

```python
>>> import struct
>>> p32(0xdeadbeef) == struct.pack('I', 0xdeadbeef)
True
>>> leet = unhex('37130000')
>>> u32(b'abcd') == struct.unpack('I', b'abcd')[0]
True
```

パックとアンパックの操作は、よく使われる多くのビット幅に対して、定義されています。

```python
>>> u8(b'A') == 0x41
True
```

## 対象のアーキテクチャと OS の設定

対象のアーキテクチャは、たいてい、それを必要とするルーチンの引数として指定できます。

```python
>>> asm('nop')
b'\x90'
>>> asm('nop', arch='arm')
b'\x00\xf0 \xe3'
```

ただし、グローバルの `context` に、一度だけ設定することもできます。オペレーティングシステム、ワードサイズ、エンディアンも、ここで設定できます。

```python
>>> context.arch      = 'i386'
>>> context.os        = 'linux'
>>> context.endian    = 'little'
>>> context.word_size = 32
```

さらに、すべての値を一度に設定する近道もあります。

```python
>>> asm('nop')
b'\x90'
>>> context(arch='arm', os='linux', endian='big', word_size=32)
>>> asm('nop')
b'\xe3 \xf0\x00'
```

## ログの詳細度の設定

標準の pwntools のログの詳細度は、`context` で制御できます。

たとえば、次のように設定すると、

```python
>>> context.log_level = 'debug'
```

`tube` が送受信するデータのすべてが、画面に表示されます。

## アセンブルと逆アセンブル

出どころの分からない、アセンブル済みのシェルコードのかたまりを、もう実行する必要はありません。[`pwnlib.asm`](https://docs.pwntools.com/en/dev/asm.html) モジュールは、すごい機能でいっぱいです。

```python
>>> enhex(asm('mov eax, 0'))
'b800000000'
```

それでも実行してしまった場合でも、中身を調べるのは簡単です。

```python
>>> print(disasm(unhex('6a0258cd80ebf9')))
   0:   6a 02                   push   0x2
   2:   58                      pop    eax
   3:   cd 80                   int    0x80
   5:   eb f9                   jmp    0x0
```

しかも、たいていの場合、自分でシェルコードを書く必要すらありません。pwntools には、時間を節約できるシェルコードがたくさん入った [`pwnlib.shellcraft`](https://docs.pwntools.com/en/dev/shellcraft.html) モジュールが付いています。

たとえば、`setreuid(getuid(), getuid())` を行い、続いてファイルディスクリプタ 4 を `stdin`、`stdout`、`stderr` に `dup`（複製）して、シェルを起動したい、としましょう。

```python
>>> enhex(asm(shellcraft.setreuid() + shellcraft.dupsh(4)))
'6a3158cd80...'
```

## そのほかの道具

[`pwnlib.util.fiddling`](https://docs.pwntools.com/en/dev/util/fiddling.html) のおかげで、hexdump を、もう自分で書く必要はありません。

[`pwnlib.cyclic`](https://docs.pwntools.com/en/dev/util/cyclic.html) のおかげで、バッファの中の、クラッシュを引き起こすオフセットを、見つけられます。

```python
>>> cyclic(20)
b'aaaabaaacaaadaaaeaaa'
>>> # クラッシュ時に EIP = 0x62616166 (b'faab'、つまり pack(0x62616166) の結果) だったとする
>>> cyclic_find(b'faab')
120
```

## ELF の操作

値を決め打ちするのは、もうやめましょう。[`pwnlib.elf`](https://docs.pwntools.com/en/dev/elf.html) で、実行時に調べます。

```python
>>> e = ELF('/bin/cat')
>>> print(hex(e.address))
0x400000
>>> print(hex(e.symbols['write']))
0x401680
>>> print(hex(e.got['write']))
0x60b070
>>> print(hex(e.plt['write']))
0x401680
```

ファイルにパッチを当てて、保存することもできます。

```python
>>> e = ELF('/bin/cat')
>>> e.read(e.address, 4)
b'\x7fELF'
>>> e.asm(e.address, 'ret')
>>> e.save('/tmp/quiet-cat')
>>> disasm(open('/tmp/quiet-cat','rb').read(1))
'   0:   c3                      ret'
```
