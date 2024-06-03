## guess the flag

ファイルを取得します。
```
wget https://files.actf.co/b2d1ba18d7fcc3ef5e9c0c09ac07ae7d01519ee5cfb2fdfc8ba88b8e9d7877d6/guess_the_flag    
```

lsで確認します。
```
ls
```
guess_the_flagというファイルがありました。

cat コマンドで中身を見てみます。
```
cat guess_the_flag
```
以下のように出力されバイナリファイルだと分かります。
```
File: guess_the_flag   <BINARY>
```

stringコマンドで読み取り可能な文字を出力させます。
```
strings guess_the_flag  
```
以下が出力結果です。
```
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
`bugzbnllhuude^un^uid^md`ru^rhfohghb`ou^chu|
```
というのが何か暗号化されてそうで怪しいです。

こちらの[暗号解析サイト](https://gchq.github.io/CyberChef/)で色々試したところXORのkeyが1で複合化することが出来ました。

```
actf{committed_to_the_least_significant_bit}
```
