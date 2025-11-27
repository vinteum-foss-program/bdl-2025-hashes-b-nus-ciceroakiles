import sys
from pathlib import Path

# Add functions directory to path
sys.path.insert(0, 'functions')

from hash1 import simple_hash
import string

ascii_chars = string.printable[:-6]


# Basic single char hash generator
def generate_simple_hash_list_with_single_char(shift: int) -> list:
    hash_list = []
    for c in ascii_chars:
        # Get the char and envelop it with 0's (before and after) to satisfy length conditions.
        # zfill() and ljust() cannot be used with characters "+" and "-"
        tmpstr = "0"*(7-shift) + str(c) + "0"*shift

        # Avoid repeating inclusion of hashes of this 8-zero sequence
        if tmpstr != "00000000":
            hash_list.append(simple_hash(tmpstr))
        #print(simple_hash(tmpstr), tmpstr)

    return hash_list


# Check for duplicates in a list, comparing its size to a set of itself
def has_duplicates(lst) -> bool:
    return len(lst) != len(set(lst))


def run_simple_hash_analysis():
    allhashes = []
    i = 0

    # If there are still no collisions, inflate the list of hashes
    while not has_duplicates(allhashes):
       allhashes += generate_simple_hash_list_with_single_char(i)
       i += 1

    # Filter duplicates using sets to check them later
    seen = set()
    dupl = set()

    for h in allhashes:
        if h in seen:
            dupl.add(h)
        else:
            seen.add(h)

    # Reveal hash collisions
    #print(dupl)


def main():
    run_simple_hash_analysis()

    # Hash collision:
    # 0000000n -> ba07183e
    # 00000020 -> ba07183e
    print("0000000n,00000020")


if __name__ == '__main__':
    main()
