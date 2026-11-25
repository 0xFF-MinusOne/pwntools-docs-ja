# Python の開発用ヘッダー

pwntools が依存する Python のパッケージの一部は、ネイティブ拡張（C などで書かれた部分）を必要とします（たとえば、Paramiko は PyCrypto を必要とします）。

これらのネイティブ拡張をビルドするために、Python の開発用ヘッダーを入れておく必要があります。

## Ubuntu

```bash
$ sudo apt-get install python-dev
```

## Mac OS X

何もする必要はありません。
