import hashlib
import sys
import threading

def solve_pow(prefix, difficulty):
    """
    Solves the Proof of Work challenge by finding an input that, when concatenated
    with the prefix and hashed using SHA-256, results in a hash that starts with
    a certain number of zero bits.

    :param prefix: The prefix string provided in the challenge.
    :param difficulty: The number of leading zero bits required in the hash.
    :return: The input string that solves the challenge.
    """
    nonce = 0
    target = 1 << (256 - difficulty)
    prefix_bytes = prefix.encode('utf-8')

    while True:
        input_str = f"{nonce}"
        hash_result = hashlib.sha256(prefix_bytes + input_str.encode('utf-8')).hexdigest()
        if int(hash_result, 16) < target:
            return input_str
        nonce += 1

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 solve.py [prefix] [difficulty]")
        sys.exit(1)

    prefix = sys.argv[1]
    difficulty = int(sys.argv[2])

    print(f"Solving PoW for prefix: {prefix}, difficulty: {difficulty} bits...")

    solution = solve_pow(prefix, difficulty)

    hash_result = hashlib.sha256((prefix + solution).encode('utf-8')).hexdigest()
    print(f"YOUR_INPUT = {solution}\n")
    print(f"sha256(\"{prefix}\" + \"{solution}\") = {hash_result}")
    print("correct")

if __name__ == "__main__":
    main()


