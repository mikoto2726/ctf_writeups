from sympy import isprime
from math import isqrt
from Crypto.Util.number import long_to_bytes, inverse

# ここに出力された n と c の値を入力します
n = 292927367433510948901751902057717800692038691293351366163009654796102787183601223853665784238601655926920628800436003079044921928983307813012149143680956641439800408783429996002829316421340550469318295239640149707659994033143360850517185860496309968947622345912323183329662031340775767654881876683235701491291
c = 40791470236110804733312817275921324892019927976655404478966109115157033048751614414177683787333122984170869148886461684367352872341935843163852393126653174874958667177632653833127408726094823976937236033974500273341920433616691535827765625224845089258529412235827313525710616060854484132337663369013424587861


# 2p + 1 の形で n の因数分解を行います
# ソフィー・ジェルマン素数の特徴を考慮します
n_sqrt = isqrt(n)
p = None

# 6n - 1 かつ一の位が 1, 3, 9 の素数を探索
for potential_p in range(6, n_sqrt + 1, 6):
    for offset in [-1, 1, 3, 5]:
        candidate_p = potential_p + offset
        if candidate_p % 10 in [1, 3, 9] and n % candidate_p == 0:
            potential_q = n // candidate_p
            if potential_q == 2 * candidate_p + 1 and isprime(candidate_p) and isprime(potential_q):
                p = candidate_p
                q = potential_q
                break
    if p is not None:
        break

if p is None:
    raise ValueError("Could not find p and q such that q = 2p + 1")

# 公開指数 e
e = 65537

# 秘密鍵 d を計算します
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# 復号化して FLAG を取得します
m = pow(c, d, n)
flag = long_to_bytes(m).decode()

print(f"FLAG = {flag}")

