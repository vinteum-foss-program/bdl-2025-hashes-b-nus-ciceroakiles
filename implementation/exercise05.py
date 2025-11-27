import sys
from pathlib import Path

# Add functions directory to path
sys.path.insert(0, 'functions')

from hash1 import simple_hash
import string, itertools

ascii_chars = string.printable[:-6]
all_ascii_len8_strings = itertools.product(ascii_chars, repeat=8)
all_ascii_len4_strings = itertools.product(ascii_chars, repeat=4)


# 2-step attack on simple_hash function
def simple_hash_attack(target: str) -> str:
    # Attack the first half of the hash
    word = ""
    for s in all_ascii_len8_strings:
        word = ''.join(reversed(s))
        #print(simple_hash(word), word)

        if target[:4] == simple_hash(word)[:4]:
            break

    #print(word[:4])

    # Get the first half of the preimage to resume attack on the second half
    for s in all_ascii_len4_strings:
        word = word[:4] + ''.join(s)
        #print(simple_hash(word), word)

        if target == simple_hash(word):
            break

    return word


def main():
    inp = "cicero"
    target = simple_hash(inp)
    #print(target)

    preimage = simple_hash_attack(target)
    print(inp + "," + preimage)


if __name__ == '__main__':
    main()
