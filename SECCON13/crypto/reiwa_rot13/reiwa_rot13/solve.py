
from Crypto.Util.number import long_to_bytes, bytes_to_long
import codecs
import hashlib
from Crypto.Cipher import AES
import itertools
import string
from concurrent.futures import ProcessPoolExecutor
import os

# 与えられた値
n = 105270965659728963158005445847489568338624133794432049687688451306125971661031124713900002127418051522303660944175125387034394970179832138699578691141567745433869339567075081508781037210053642143165403433797282755555668756795483577896703080883972479419729546081868838801222887486792028810888791562604036658927
e = 137
c1 = 16725879353360743225730316963034204726319861040005120594887234855326369831320755783193769090051590949825166249781272646922803585636193915974651774390260491016720214140633640783231543045598365485211028668510203305809438787364463227009966174262553328694926283315238194084123468757122106412580182773221207234679
c2 = 54707765286024193032187360617061494734604811486186903189763791054142827180860557148652470696909890077875431762633703093692649645204708548602818564932535214931099060428833400560189627416590019522535730804324469881327808667775412214400027813470331712844449900828912439270590227229668374597433444897899112329233
encrypted_flag = b"\xdb'\x0bL\x0f\xca\x16\xf5\x17>\xad\xfc\xe2\x10$(DVsDS~\xd3v\xe2\x86T\xb1{xL\xe53s\x90\x14\xfd\xe7\xdb\xddf\x1fx\xa3\xfc3\xcb\xb5~\x01\x9c\x91w\xa6\x03\x80&\xdb\x19xu\xedh\xe4"

# ROT13の変換辞書を作成
alphabet = string.ascii_lowercase
rot13_map = {char: alphabet[(i + 13) % 26] for i, char in enumerate(alphabet)}

def rot13(text):
    return ''.join(rot13_map[c] for c in text)

def process_chunk(chunk, chunk_index, total_chunks):
    print(f"[プロセス {os.getpid()}] チャンク {chunk_index}/{total_chunks} 開始")
    for i, key_tuple in enumerate(chunk):
        key_candidate = ''.join(key_tuple)
        rot13_key_candidate = rot13(key_candidate)
        
        # RSA暗号化を試行
        key_long = bytes_to_long(key_candidate.encode())
        rot13_key_long = bytes_to_long(rot13_key_candidate.encode())
        
        c1_candidate = pow(key_long, e, n)
        if c1_candidate != c1:
            continue  # c1が不一致ならc2計算を省略

        c2_candidate = pow(rot13_key_long, e, n)
        if c2_candidate != c2:
            continue  # c2も不一致ならスキップ

        # 一致する場合、フラグを復号
        aes_key = hashlib.sha256(key_candidate.encode()).digest()
        cipher = AES.new(aes_key, AES.MODE_ECB)
        decrypted_flag = cipher.decrypt(encrypted_flag)
        print(f"[プロセス {os.getpid()}] 一致するキー発見: {key_candidate}")
        return key_candidate, decrypted_flag
        break

    if chunk_index % 10 == 0:
        print(f"[プロセス {os.getpid()}] チャンク {chunk_index}/{total_chunks} 処理中...")
    return None

def main():
    key_space = itertools.product(alphabet, repeat=10)
    chunk_size = 100000  # チャンクサイズを調整
    chunks = []
    chunk = []
    
    for key in key_space:
        chunk.append(key)
        if len(chunk) >= chunk_size:
            chunks.append(chunk)
            chunk = []
    if chunk:
        chunks.append(chunk)

    total_chunks = len(chunks)

    with ProcessPoolExecutor() as executor:
        futures = []
        for i, chunk in enumerate(chunks):
            futures.append(executor.submit(process_chunk, chunk, i + 1, total_chunks))

        for future in futures:
            result = future.result()
            if result:
                key, flag = result
                print(f"キー: {key}")
                print(f"復号フラグ: {flag}")
                return

if __name__ == "__main__":
    main()

