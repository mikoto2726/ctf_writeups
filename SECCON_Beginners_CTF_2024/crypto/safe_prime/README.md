## safe prime
問題文

Using a [safe prime](https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes) makes RSA secure, doesn't it?

tar.gzファイルがあるのでダウンロードします。
```
wget https://score.beginners.seccon.jp/api/download?key=beginners2024%2FSafe_Prime.tar.gz
```
zipファイルを解凍します。
```
unzip download\?key=beginners2024%2FSafe_Prime.tar.gz 
```
Safe Primeというフォルダが出てきたのでこのディレクトリに移動します。
```
cd Safe\ Prime/  
```
lsコマンドでフォルダの中身を確認します。
```
ls
```
chall.pyとoutput.txtの二つのファイルがありました。
catコマンドで中身を確認します。
```
cat chall.py
```
↓出力結果
```
import os
from Crypto.Util.number import getPrime, isPrime

FLAG = os.getenv("FLAG", "ctf4b{*** REDACTED ***}").encode()
m = int.from_bytes(FLAG, 'big')

while True:
    p = getPrime(512)
    q = 2 * p + 1
    if isPrime(q):
        break


n = p * q
e = 65537
c = pow(m, e, n)

print(f"{n = }")
print(f"{c = }")
```

```
cat output.txt
```
↓出力結果
```
n = 292927367433510948901751902057717800692038691293351366163009654796102787183601223853665784238601655926920628800436003079044921928983307813012149143680956641439800408783429996002829316421340550469318295239640149707659994033143360850517185860496309968947622345912323183329662031340775767654881876683235701491291
c = 40791470236110804733312817275921324892019927976655404478966109115157033048751614414177683787333122984170869148886461684367352872341935843163852393126653174874958667177632653833127408726094823976937236033974500273341920433616691535827765625224845089258529412235827313525710616060854484132337663369013424587861
```
私は問題文にあるwikipediaをよみ、Googleでsafe primeと検索し、こちらの[wikipedia](https://ja.wikipedia.org/wiki/%E5%AE%89%E5%85%A8%E7%B4%A0%E6%95%B0)を読みました。




