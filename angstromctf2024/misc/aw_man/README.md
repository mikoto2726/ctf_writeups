## aw man 50pt, 290solves
```
Man? Is that you?
```
こちらも写真が与えられる問題でした。
```
CTF 画像
```
と検索して出てきた以下のサイトを参考に解いてみましたがflagが見つからず断念しました。

[Forensics入門（CTF）](https://qiita.com/knqyf263/items/6ebf06e27be7c48aab2e)
[4-Girls Petit CTF WriteUp（in SECCON 2023 電脳会議）](https://tech.dentsusoken.com/entry/2024/01/17/4-Girls_Petit_CTF_WriteUp)

## CTF終了後
[こちらのwriteupを参考にしました](https://momrulhasan.medium.com/angstrom-ctf-2024-writeups-5482332ad537)

画像ファイルを取得する
```
wget https://files.actf.co/5b9ef628dbf56fedc1ad1861b0ccb96569cd6a97fe49d50cb8f099155adf66b3/mann.jpg
```
画像の確認(flagには関係ないです)
```
eog mann.jpg &
```

画像や音声ファイルに埋め込まれたデータを抽出する
```
steghide extract -sf mann.jpg
```
出力結果がこちら
```
Enter passphrase: 
wrote extracted data to "enc.txt".
```
lsでファイルを確認
```
enc.txt  mann.jpg
```
enc.txtの中身を確認
```
cat enc.txt
```
出力結果
```
5RRjnsi3Hb3yT3jWgFRcPWUg5gYXe81WPeX3vmXS
```
これはbase58なのでdecodeするとfalgを取得できます
```
actf{crazy?_i_was_crazy_once}
```
