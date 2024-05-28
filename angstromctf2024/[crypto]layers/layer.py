import itertools

def xor(key, data):
    return bytes([k^d for k, d in zip(itertools.cycle(key),data)])

xor(fb7fdbf9, 6db78706159d22)


