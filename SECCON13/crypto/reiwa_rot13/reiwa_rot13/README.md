# reiwa_rot13

### ChatGPTとの会話のまとめです
---

## 会話の流れ
1. **問題の概要**
   - CTFのCrypto問題に取り組んでおり、RSAとAES暗号を解く必要がある。
   - RSAのパラメータ \( n \), \( e \), 暗号化された値 \( c1 \), \( c2 \)、およびAESで暗号化されたフラグが与えられている。

2. **最初のアプローチ**
   - \( n \) の因数分解を試みたが、大きすぎて通常の手法では解けなかった。

3. **Wiener攻撃の導入**
   - \( d \)（秘密鍵）が小さい可能性を想定し、Wiener攻撃を実装。
   - しかし、実装中にいくつかのエラーが発生。

4. **エラー対応**
   - **`ModuleNotFoundError: No module named 'Crypto'`**  
     → `pycryptodome` をインストールして解決。

   - **`ZeroDivisionError: Modulus cannot be zero`**  
     → \( n \) の因数分解が必要だと判明。

   - **`TypeError: continued_fraction_convergents() takes 1 positional argument but 2 were given`**  
     → `sympy` の連分数関数に誤った引数を渡していたため、修正。

5. **Wiener攻撃の修正**
   - 修正版では、RSAの公開鍵パラメータを正しく処理するよう調整。
   - `Rational(e, n)` を使用して有理数形式で比率を処理し、連分数の収束値を取得する形に修正。

6. **現状**
   - エラーを修正し、Wiener攻撃の実行が可能になった。
   - 現在、秘密鍵 \( d \) を推定する試行中。

---

