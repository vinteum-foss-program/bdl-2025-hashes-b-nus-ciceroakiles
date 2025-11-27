import sys
from pathlib import Path

# Add functions directory to path
sys.path.insert(0, 'functions')

from hash0 import xor32_hash
import string

ascii_chars = string.printable[:-6]


# Basic single char attack on an interval
def xor32_hash_single_char_attack(target: str, shift: int, begin: int, end: int) -> str:
    for c in ascii_chars:
        # Get the char and envelop it with 0's (before and after) to satisfy length conditions.
        # zfill() and ljust() cannot be used with characters "+" and "-"
        tmpstr = "0"*(7-shift) + str(c) + "0"*shift

        #print(xor32_hash(tmpstr), tmpstr)

        # Stop if the results match
        if target[begin:end] == xor32_hash(tmpstr)[begin:end]:
            return c
        else:
            tmpstr = []
    return ""


def get_output(target: str) -> str:
    result = []
    for i in range(4):
        char = xor32_hash_single_char_attack(target, i, i*2, (i*2)+2)
        result.append(char)

    out = ''.join(reversed(result)).zfill(8)
    return out


def main():
    target = "1b575451"
    output = get_output(target)
    print(output)


if __name__ == '__main__':
    main()
