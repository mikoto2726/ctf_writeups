## erm what the enigma[crypto] 20pt, 530solves
```
In the dimly lit, smoke-filled war room, the Enigma M3 machine sat at the center of the table like a cryptographic sentinel.
Its reflector, UKW B, gleamed ominously in the low light. 
The three rotors, I, II, and III, stood proudly in their respective slots, each at position 1 with their rings set to 1. 
The plugboard, conspicuously vacant, indicated a reliance on the rotor settings alone to encode the day's crucial messages. 
As the operator's fingers hovered over the keys, the silence was heavy with anticipation. 
Each clack of the keys transformed plaintext into an unbreakable cipher, the resulting ciphertext, brht{d_imhw_cexhrmwyy_lbvkvqcf_ldcz}, a guardian of wartime secrets.
```
日本語訳
```
薄暗く、煙が充満した戦場では、エニグマM3マシンが暗号の歩哨のようにテーブルの中央に置かれていた。
その反射鏡UKW Bは暗い光の中で不吉に輝いていた。
I、II、IIIの3つのローターがそれぞれのスロットに誇らしげに立っており、それぞれのリングは1の位置にセットされていた。
オペレーターの指がキーの上に置かれると、期待に満ちた静寂が訪れた。
キーを叩くたびに、平文が解読不可能な暗号に変換され、その結果の暗号文、brht{d_imhw_cexhrmwyy_lbvkvqcf_ldcz}は、戦時中の秘密の守護者となった。
```
エニグマの暗号問題ということが分かります。
enigma m3などと検索し色々と仕組みを調べました。

最初[このサイト](https://cryptii.com/pipes/enigma-machine)でやりましたが、上手く出来ませんでした。

次にenigma ctfで検索して出てきた[このサイト](https://www.dcode.fr/enigma-machine-cipher)で問題文に合うよう、以下の写真のように設定

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3794748/b3510627-d5b0-2e38-7beb-c136717b26a8.png)

Decryptoしたところflagを取得できました。

```
actf{i_love_enigmatic_machines_mwah}
```
