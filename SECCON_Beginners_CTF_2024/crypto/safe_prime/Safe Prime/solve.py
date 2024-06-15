from Crypto.Util.number import long_to_bytes, inverse, isPrime

# 与えられた n, e, c
n = 292927367433510948901751902057717800692038691293351366163009654796102787183601223853665784238601655926920628800436003079044921928983307813012149143680956641439800408783429996002829316421340550469318295239640149707659994033143360850517185860496309968947622345912323183329662031340775767654881876683235701491291
e = 65537
c = 40791470236110804733312817275921324892019927976655404478966109115157033048751614414177683787333122984170869148886461684367352872341935843163852393126653174874958667177632653833127408726094823976937236033974500273341920433616691535827765625224845089258529412235827313525710616060854484132337663369013424587861

# 整数の平方根を計算する関数
def integer_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# nを素因数分解する関数
def find_p_and_q(n):
    sqrt_n = integer_sqrt(n)
    print("find_p_and_q")
    for p in range(2, sqrt_n + 1):
        if p % 4 == 3:
            q_candidate = 2*p+1
            if (2**p-1)%q_candidate == 0:
                q = (2**p-1)//q_candidate
                if p*q == n and isPrime(p) and isPrime(q):
                    return p, q
    return None, None

# ソフィー・ジェルマン素数を利用して n を素因数分解
p, q = find_p_and_q(n)
if p is None or q is None:
    print("Failed to factorize n with given method.")
else:
    print(f"p = {p}")
    print(f"q = {q}")
    
    # φ(n)の計算
    phi = (p - 1) * (q - 1)
    
    # 秘密鍵 d の計算
    d = inverse(e, phi)
    
    # 復号化
    m = pow(c, d, n)
    
    # メッセージをバイト列に変換
    message = long_to_bytes(m)
    print("Decrypted message:", message.decode())

