from Crypto.Util.number import long_to_bytes
import codecs
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import *
import codecs
import string
import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# 与えられた値
n = 105270965659728963158005445847489568338624133794432049687688451306125971661031124713900002127418051522303660944175125387034394970179832138699578691141567745433869339567075081508781037210053642143165403433797282755555668756795483577896703080883972479419729546081868838801222887486792028810888791562604036658927
e = 137
c1 = 16725879353360743225730316963034204726319861040005120594887234855326369831320755783193769090051590949825166249781272646922803585636193915974651774390260491016720214140633640783231543045598365485211028668510203305809438787364463227009966174262553328694926283315238194084123468757122106412580182773221207234679
c2 = 54707765286024193032187360617061494734604811486186903189763791054142827180860557148652470696909890077875431762633703093692649645204708548602818564932535214931099060428833400560189627416590019522535730804324469881327808667775412214400027813470331712844449900828912439270590227229668374597433444897899112329233
encrypted_flag = b"\xdb'\x0bL\x0f\xca\x16\xf5\x17>\xad\xfc\xe2\x10$(DVsDS~\xd3v\xe2\x86T\xb1{xL\xe53s\x90\x14\xfd\xe7\xdb\xddf\x1fx\xa3\xfc3\xcb\xb5~\x01\x9c\x91w\xa6\x03\x80&\xdb\x19xu\xedh\xe4"

# 10文字の小文字英字の総当たり
import itertools
import string

alphabet = string.ascii_lowercase
for key_tuple in itertools.product(alphabet, repeat=10):
    key_candidate = ''.join(key_tuple)
    rot13_key_candidate = codecs.encode(key_candidate, 'rot13')
    
    # 文字列をバイトに変換
    key_bytes = key_candidate.encode()
    rot13_key_bytes = rot13_key_candidate.encode()
    
    # 長整数に変換
    key_long = bytes_to_long(key_bytes)
    rot13_key_long = bytes_to_long(rot13_key_bytes)
    
    # RSA暗号の計算
    c1_candidate = pow(key_long, e, n)
    c2_candidate = pow(rot13_key_long, e, n)
    
    # 一致を確認
    if c1_candidate == c1 and c2_candidate == c2:
        print(f"キーが見つかりました: {key_candidate}")
        
        # AES鍵の生成
        aes_key = hashlib.sha256(key_bytes).digest()
        
        # AESでフラグを復号
        cipher = AES.new(aes_key, AES.MODE_ECB)
        decrypted_flag = cipher.decrypt(encrypted_flag)
        print(f"復号されたフラグ: {decrypted_flag}")
        break

