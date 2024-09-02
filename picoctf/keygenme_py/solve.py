import hashlib

username_trial = "MORTON"
hash_value = hashlib.sha256(username_trial.encode()).hexdigest()
print(hash_value)

dynamic_key = hash_value[4] + hash_value[5] + hash_value[3] + hash_value[6] + \
              hash_value[2] + hash_value[7] + hash_value[1] + hash_value[8]

print(dynamic_key)


key_full = "picoCTF{1n_7h3_|<3y_of_" + dynamic_key + "}"
print(key_full)

