## dou you wanna build a snowman
[こちらのwriteupを参照](https://momrulhasan.medium.com/angstrom-ctf-2024-writeups-5482332ad537)

```
wget https://files.actf.co/67ad046a16c81593ac82fdc7975dd8713a9c364774b69e2a8a3632e639c7fc66/snowman.jpg
```
```
ls
```
lsでディレクトを確認するとsnowman.jpgが作成されています。

```
eog snowman.jpg &
```

.jpgなのでeogコマンドで表示させようとしましたが中身が壊れていて表示できませんでした。

中身を見ていきます。

バイナリモードでVimを起動:
```
vim -b snowman.jpg
```
バイナリ表示モードを有効にする:
バイナリファイルを16進数で表示するには、以下のコマンドをVim内で入力します。
```
:%! xxd
```
ファイルの内容が16進数とASCIIコードで表示されました。
```
00000000: fdd8 ffe0 0010 4a46 4946 0001 0100 0001  ......JFIF......
00000010: 0001 0000 ffe2 01d8 4943 435f 5052 4f46  ........ICC_PROF
00000020: 494c 4500 0101 0000 01c8 0000 0000 0430  ILE............0
00000030: 0000 6d6e 7472 5247 4220 5859 5a20 07e0  ..mntrRGB XYZ ..
```
「jpg バイナリ」と検索して出てきた[こちらのサイト](https://qiita.com/spc_ehara/items/87d383a59a37a2c82531#jpg%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E6%A7%8B%E9%80%A0)によると先頭は(FFD8)となるそうです。
```
i
```
でINSERTモードにして、先頭のfdd8をffd8にします。
```
00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0001  ......JFIF......
00000010: 0001 0000 ffe2 01d8 4943 435f 5052 4f46  ........ICC_PROF
00000020: 494c 4500 0101 0000 01c8 0000 0000 0430  ILE............0
00000030: 0000 6d6e 7472 5247 4220 5859 5a20 07e0  ..mntrRGB XYZ ..
```
16進数表示を元に戻すには、以下のコマンドを使用します。
```
:%! xxd -r
```
変更を保存します。
```
:wq
```
eogで画像を開いてみます。
```
eog snowman.jpg &
```

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3794748/84ab940d-1995-1e43-6e74-9d05d48568a3.png)

flagを獲得できました。
```
actf{built_the_snowman}
````


