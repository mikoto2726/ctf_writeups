ダウンロードしたファイルを調べます。   
```
file nothin_but_stringz.c.o       
```
出力結果   
```
nothin_but_stringz.c.o: LLVM bitcode, wrapper
```   
以下のコマンドでLLVMのバイトコードを読める形式に変換します。   
llm-disについては[こちら](https://llvm.org/docs/CommandGuide/llvm-dis.html)   
```
llvm-dis nothin_but_stringz.c.o -o nothin_but_stringz.ll
```
変換後のファイルを開くと、以下のようなコードが表示されます。   
```
; ModuleID = 'nothin_but_stringz.c.o'
source_filename = "nothin_but_stringz.c"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-ios7.0.0"

@.str = private unnamed_addr constant [40 x i8] c"flag{al1_th3_h0miez_l0v3_llvm_643e5f4a}\00", align 1
@flag = global ptr @.str, align 8
@.str.1 = private unnamed_addr constant [25 x i8] c"The flag begins with %c\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable(sync)
define i32 @main() #0 {
  %1 = alloca i32, align 4
  store i32 0, ptr %1, align 4
  %2 = load ptr, ptr @flag, align 8
  %3 = getelementptr inbounds i8, ptr %2, i64 0
  %4 = load volatile i8, ptr %3, align 1
  %5 = sext i8 %4 to i32
  %6 = call i32 (ptr, ...) @printf(ptr noundef @.str.1, i32 noundef %5)
  ret i32 0
}

declare i32 @printf(ptr noundef, ...) #1

attributes #0 = { noinline nounwind optnone ssp uwtable(sync) "frame-pointer"="non-leaf" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-a7" "target-features"="+aes,+crypto,+fp-armv8,+neon,+sha2,+v8a,+zcm,+zcz" }
attributes #1 = { "frame-pointer"="non-leaf" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-a7" "target-features"="+aes,+crypto,+fp-armv8,+neon,+sha2,+v8a,+zcm,+zcz" }

!llvm.module.flags = !{!0, !1, !2, !3, !4}
!llvm.ident = !{!5}

!0 = !{i32 2, !"SDK Version", [2 x i32] [i32 14, i32 4]}
!1 = !{i32 1, !"wchar_size", i32 4}
!2 = !{i32 8, !"PIC Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 1}
!4 = !{i32 7, !"frame-pointer", i32 1}
!5 = !{!"Apple clang version 15.0.0 (clang-1500.3.9.4)"}
```
このコードを読むと、`@.str`にフラグが格納されていることがわかります。   
```
flag{al1_th3_h0miez_l0v3_llvm_643e5f4a}
```


