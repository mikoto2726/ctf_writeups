## [qiita](https://qiita.com/mikoto2726/items/2a0e40836ded98f7422e)

## 自己紹介
名前：尊(mikoto)
Twitter:[mikoto2726](https://x.com/mikoto2726)

python,Linuxの基本的な知識はありますが、CTF関連は初心者です。
かなり前にCpawCTFをwriteupを皆がら解いた程度で現在は、ほぼ忘れてしまった状態で参加しました。

## 感想

簡単な問題でもGoogleで類似問題を調べることで何とか解く事が出来ました。
ChatGPTは使わないようにしました。
だいぶ時間を使ったのでRSA暗号の問題を解けた時が一番嬉しかったです。
他の方のwriteupを見て解けなかった問題を復習したいです。

## [angstromctf](https://2024.angstromctf.com/challenges) writeup
[English writeup](https://qiita.com/mikoto2726/items/b62f9b57cefde01947a4)


結果は630位/923位中,80ptという結果になりました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3794748/a8c91216-fc5e-9ecb-64b2-8a0b51863bed.png)

解けた問題はこちらの4問
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3794748/e6357634-13fe-f158-72de-9b59ecf7d56c.png)

## kcehC ytinaS[misc] 10pt, 550solvs
```
)csim# ni cipot lennahc eht s'ti( galf eht rof drocsiD ruo nioJ
```
最初シーザー暗号化かと思いましたが違いました。
リンクの部分がdiscordへのリンクだったのでこの単語はなんとなくDiscordと読めました。
10分ぐらい考えて文字が逆から読めることに気づきました。
```
joiin our Discord for the flag (it's the channel topic in #misc)
```
ということでDiscordのmiscチャンネルを見てみるとチャンネルの概要欄に以下のようにありました。
```
}egassem_terces_ym_edoced_uoy_did_woh{ftca
```
こちらも反転させてflagが取れました。
```
actf{how_did_you_decode_my_secret_message}
```


## putnam[misc] 10pt, 637solves

```
Solve the putnam, get the flag. Easy right?

Connect to it at nc challs.actf.co 31337
```
コマンドをそのまま打ち込みます。
足し算をしたらflagが取れました。
```
└─$ nc challs.actf.co 31337
514 + 97 = ?
611
You succeeded! The flag is actf{just_a_tad_easier_than_the_actual_putnam} :D
```

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

## philosophy[crypto] 40pt, 338solves
```
Clam decided to start studying philosophy, and what is the difference between plus one and minus one anyway...

challenge
```

chall.pyというファイルが与えられたのでcatコマンドで中身を見てみる
```
cat chall.py
```
chell.py
```
from Crypto.Util.number import getPrime
from secret import flag

p = getPrime(512)
q = getPrime(512)

m = int.from_bytes(flag.encode(), "big")

n = p * q
e = 65537
c = pow(m, e, n)

phi = (p + 1) * (q + 1)

print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")
print(f"\"phi\": {phi}")

"""
n: 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084554536903236375579771401257801115918586590639686117179685431627540567894983403579070366895343181435791515535593260495162656111028487919107927692512155290673
e: 65537
c: 64457111821105649174362298452450091137161142479679349324820456191542295609033025036769398863050668733308827861582321665479620448998471034645792165920115009947792955402994892700435507896792829140545387740663865218579313148804819896796193817727423074201660305082597780007494535370991899386707740199516316196758
"phi": 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084573410416063246853198167436938724585247461433706053188624379514833802770205501907568228388536548010385588837258085711058519777393945044905741975952241886308
```
powが手掛かりになりそうだと思ったのでGoogleで
```
ctf crypto writeup pow
```
と調べました。
```
https://trap.jp/post/1582/
```
こちらのサイトを参考にしました。

現在
```math
c = m^e(mod\;n)\\
```
となっています。
以下の式を計算すると平文mが求まります。


```math
\displaylines{ 
\begin{align}
φ & = (p-1)(q-1)\\
d & = e^{-1}(mod\;φ)\\
m & = c^d(mod \;n)\\
\end{align}
} 
```

まずφを求めます。
```math
φ =pq-(p+q)+1・・・①
```

ここで問題文より、
```math
\displaylines{ 
\begin{align}
n & = pq\\
phi & = pq + (p+q) + 1\\
\end{align}
}
```
なので式変形して
```math

p+q = phi-n-1・・・②


```
ということが分かります。
②を①に代入すると
```math
\displaylines{ 
\begin{align}
φ & =n-(phi-n-1)+1\\
  & = 2n -phi +2
\end{align}
} 
```
次にdを求めます。
```math
\displaylines{ 
\begin{align}
d & = e^{-1}(mod\;φ)\\
  & = pow(e, -1, φ)
\end{align}
} 
```
最後に今までのを代入してmを求めます。
```math
\displaylines{ 
\begin{align}
m & = c^d(mod \;n)\\
  & = pow(c, d, n) 
\end{align}
} 
```
これらをコードにすると以下のようになりました。

```
from Crypto.Util.number import long_to_bytes

n = 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084554536903236375579771401257801115918586590639686117179685431627540567894983403579070366895343181435791515535593260495162656111028487919107927692512155290673

e = 65537

c = 64457111821105649174362298452450091137161142479679349324820456191542295609033025036769398863050668733308827861582321665479620448998471034645792165920115009947792955402994892700435507896792829140545387740663865218579313148804819896796193817727423074201660305082597780007494535370991899386707740199516316196758

phi = 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084573410416063246853198167436938724585247461433706053188624379514833802770205501907568228388536548010385588837258085711058519777393945044905741975952241886308

f = 2*n - phi + 2 
d = pow(e, -1, f)
#d = (e ** -1) % f
m = pow(c, d, n)
#k = (c ** d) % n


print(m)
print("----------------")
#print(k)
print(long_to_bytes(m))
```

```
d = pow(e, -1, f)
#d = (e ** -1) % f
```

最初下で書いていてエラーにはまっていました。
ここら辺の理解がまだ甘いみたいです。
```
GPTより
pow(e, -1, f) は整数のモジュラ逆元を計算します。これは特定の数論的な問題を解決するためのものです。
e ** -1 % f は浮動小数点数の逆数を計算し、その結果を f で割った余りを求めますが、これは数論的なモジュラ逆元の計算とは異なります。
正確なモジュラ逆元を計算するためには、必ず pow(e, -1, f) を使用してください。
```


```
actf{its_okay_i_figured_out_phi_anyway}
```

## 以下解けなかったが試した問題
## trip 30pt,484solves
```
What road was this this photo taken on?

For example, if the road was "Colesville Road" the flag would be actf{colesville}.
```
写真が与えられてどこで撮られたのかを回答する問題。
[【CTF】OSINT問題で個人的に使用するツール・サイト・テクニックまとめ](https://qiita.com/xryuseix/items/e35b8c946e5dfe96f848)を参照し、google lensや画像検索など色々試しましたが、一致する画像が出てこなかった為、断念しました。


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


```
$ file guess_the_flag
guess_the_flag: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5872c12702d2954fef870af77944910ef66b5d69, for GNU/Linux 3.2.0, not stripped
```
```
$ strings guess_the_flag           
/lib64/ld-linux-x86-64.so.2
mgUa
__cxa_finalize
fgets
__libc_start_main
strcmp
puts
strlen
stdin
__stack_chk_fail
libc.so.6
GLIBC_2.4
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
D$H1
D$HdH+
PTE1
u+UH
Go ahead, guess the flag: 
Correct! It was kinda obvious tbh.
Wrong. Not sure why you'd think it'd be that.
:*3$"
`bugzbnllhuude^un^uid^md`ru^rhfohghb`ou^chu|
GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Scrt1.o
__abi_tag
guess_the_flag.c
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_start_main@GLIBC_2.34
_ITM_deregisterTMCloneTable
puts@GLIBC_2.2.5
stdin@GLIBC_2.2.5
secretcode
_edata
_fini
strlen@GLIBC_2.2.5
__stack_chk_fail@GLIBC_2.4
fgets@GLIBC_2.2.5
__data_start
strcmp@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
_end
__bss_start
main
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@GLIBC_2.2.5
_init
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
```

```
$ sudo chmod 777 guess_the_flag.exe   
```
```
$ ./guess_the_flag                  
Go ahead, guess the flag: 
a
Wrong. Not sure why you'd think it'd be that.
```
```
$ readelf guess_the_flag 
Usage: readelf <option(s)> elf-file(s)
 Display information about the contents of ELF format files
 Options are:
  -a --all               Equivalent to: -h -l -S -s -r -d -V -A -I
  -h --file-header       Display the ELF file header
  -l --program-headers   Display the program headers
     --segments          An alias for --program-headers
  -S --section-headers   Display the sections' header
     --sections          An alias for --section-headers
  -g --section-groups    Display the section groups
  -t --section-details   Display the section details
  -e --headers           Equivalent to: -h -l -S
  -s --syms              Display the symbol table
     --symbols           An alias for --syms
     --dyn-syms          Display the dynamic symbol table
     --lto-syms          Display LTO symbol tables
     --sym-base=[0|8|10|16] 
                         Force base for symbol sizes.  The options are 
                         mixed (the default), octal, decimal, hexadecimal.
  -C --demangle[=STYLE]  Decode mangled/processed symbol names
                           STYLE can be "none", "auto", "gnu-v3", "java",
                           "gnat", "dlang", "rust"
     --no-demangle       Do not demangle low-level symbol names.  (default)
     --recurse-limit     Enable a demangling recursion limit.  (default)
     --no-recurse-limit  Disable a demangling recursion limit
     -U[dlexhi] --unicode=[default|locale|escape|hex|highlight|invalid]
                         Display unicode characters as determined by the current locale
                          (default), escape sequences, "<hex sequences>", highlighted
                          escape sequences, or treat them as invalid and display as
                          "{hex sequences}"
     -X --extra-sym-info Display extra information when showing symbols
     --no-extra-sym-info Do not display extra information when showing symbols (default)
  -n --notes             Display the contents of note sections (if present)
  -r --relocs            Display the relocations (if present)
  -u --unwind            Display the unwind info (if present)
  -d --dynamic           Display the dynamic section (if present)
  -V --version-info      Display the version sections (if present)
  -A --arch-specific     Display architecture specific information (if any)
  -c --archive-index     Display the symbol/file index in an archive
  -D --use-dynamic       Use the dynamic section info when displaying symbols
  -L --lint|--enable-checks
                         Display warning messages for possible problems
  -x --hex-dump=<number|name>
                         Dump the contents of section <number|name> as bytes
  -p --string-dump=<number|name>
                         Dump the contents of section <number|name> as strings
  -R --relocated-dump=<number|name>
                         Dump the relocated contents of section <number|name>
  -z --decompress        Decompress section before dumping it
  -w --debug-dump[a/=abbrev, A/=addr, r/=aranges, c/=cu_index, L/=decodedline,
                  f/=frames, F/=frames-interp, g/=gdb_index, i/=info, o/=loc,
                  m/=macro, p/=pubnames, t/=pubtypes, R/=Ranges, l/=rawline,
                  s/=str, O/=str-offsets, u/=trace_abbrev, T/=trace_aranges,
                  U/=trace_info]
                         Display the contents of DWARF debug sections
  -wk --debug-dump=links Display the contents of sections that link to separate
                          debuginfo files
  -P --process-links     Display the contents of non-debug sections in separate
                          debuginfo files.  (Implies -wK)
  -wK --debug-dump=follow-links
                         Follow links to separate debug info files (default)
  -wN --debug-dump=no-follow-links
                         Do not follow links to separate debug info files
  --dwarf-depth=N        Do not display DIEs at depth N or greater
  --dwarf-start=N        Display DIEs starting at offset N
  --ctf=<number|name>    Display CTF info from section <number|name>
  --ctf-parent=<name>    Use CTF archive member <name> as the CTF parent
  --ctf-symbols=<number|name>
                         Use section <number|name> as the CTF external symtab
  --ctf-strings=<number|name>
                         Use section <number|name> as the CTF external strtab
  --sframe[=NAME]        Display SFrame info from section NAME, (default '.sframe')
  -I --histogram         Display histogram of bucket list lengths
  -W --wide              Allow output width to exceed 80 characters
  -T --silent-truncation If a symbol name is truncated, do not add [...] suffix
  @<file>                Read options from <file>
  -H --help              Display this information
  -v --version           Display the version number of readelf

```


## layers 50pt, 530solves
```
nc challs.actf.co 31398‎

challenge.py
```
問題文にある通りncコマンドを叩くと以下のように出てきました。

```
└─$ nc challs.actf.co 31398
Welcome to my encryption service!
Surely encrypting multiple times will make it more secure.
1. Encrypt message.
2. Encrypt (hex) message.
3. See encrypted flag!
Pick 1, 2, or 3 > 
```
1を選択するとメッセージを入力できるようになり、適当に打ったら違うと言われます。
```
Pick 1, 2, or 3 > 1
Your message > actf
fb7fdbf9
Not sure what that means.
```
以下がchallenge.pyです
```
   1   │ import hashlib
   2   │ import itertools
   3   │ import os
   4   │ 
   5   │ def xor(key, data):
   6   │     return bytes([k ^ d for k, d in zip(itertools.cycle(key), data)]
       │ )
   7   │ 
   8   │ def encrypt(phrase, message, iters=1000):
   9   │     key = phrase.encode()
  10   │     for _ in range(iters):
  11   │         key = hashlib.md5(key).digest()
  12   │         message = xor(key, message)
  13   │     return message
  14   │ 
  15   │ print('Welcome to my encryption service!')
  16   │ print('Surely encrypting multiple times will make it more secure.')
  17   │ print('1. Encrypt message.')
  18   │ print('2. Encrypt (hex) message.')
  19   │ print('3. See encrypted flag!')
  20   │ 
  21   │ phrase = os.environ.get('FLAG', 'missing')
  22   │ 
  23   │ choice = input('Pick 1, 2, or 3 > ')
  24   │ if choice == '1':
  25   │     message = input('Your message > ').encode()
  26   │     encrypted = encrypt(phrase, message)
  27   │     print(encrypted.hex())
  28   │ if choice == '2':
  29   │     message = bytes.fromhex(input('Your message > '))
  30   │     encrypted = encrypt(phrase, message)
  31   │     print(encrypted.hex())
  32   │ elif choice == '3':
  33   │     print(encrypt(phrase, phrase.encode()).hex())
  34   │ else:
  35   │     print('Not sure what that means.')


```

```
nc challs.actf.co 31398
```

で３を選択するとフラッグとフラッグのエンコードされた数字の排他的論理和が出力される？
この二つのうちのどちらかがわかればフラッグを取る事が出来るはずですが分かりませんでした。




