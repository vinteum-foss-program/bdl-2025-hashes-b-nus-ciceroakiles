import hashlib
import string, itertools

ascii_chars = string.printable[:-6]
all_ascii_len4_strings = itertools.product(ascii_chars, repeat=4)


def sha256_partial_collision(target: str, start: str) -> str:
    # Get size of the starting piece to be found
    l = len(target)
    for s in all_ascii_len4_strings:
        # Creates the string to be hashed
        word = start + ''.join(s)
        hashstr = hashlib.sha256(word.encode('utf-8')).hexdigest()

        if target == hashstr[:l]:
            #print(str(hashstr)[:l], word)
            break

    return word


def main():
    startswith = "bitcoin"

    target1 = "cafe"
    output1 = sha256_partial_collision(target1, startswith)
    #print(output1)

    target2 = "faded"
    output2 = sha256_partial_collision(target2, startswith)
    #print(output2)

    target3 = "decade"
    output3 = sha256_partial_collision(target3, startswith)
    #print(output3)

    print(output1 + "," + output2 + "," + output3)


if __name__ == '__main__':
    main()
