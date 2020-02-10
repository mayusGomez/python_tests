
alpha_index = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}

index_alpha = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: 'A',
    28: 'B',
    29: 'C',
    30: 'D',
    31: 'E',
    32: 'F',
    33: 'G',
    34: 'H',
    35: 'I',
    36: 'J',
    37: 'K',
    38: 'L',
    39: 'M',
    40: 'N',
    41: 'O',
    42: 'P',
    43: 'Q',
    44: 'R',
    45: 'S',
    46: 'T',
    47: 'U',
    48: 'V',
    49: 'W',
    50: 'X',
    51: 'Y',
    52: 'Z'
}

last_idx = 52


def decrypt_letter(letter, position):
    """
    Decrypt a letter and return the correct letter to read the message

    This function use two dictionaries for accessing O(1) to data of alphabet and transform the letter
    :param letter: encrypted letter
    :param position: letter's position in encrypted message
    :return: correct letter
    """

    # Get the index of letter
    idx = alpha_index[letter]

    # Fix the position if the result is negative
    while idx <= position:
        position = position - idx
        idx = last_idx

    new_idx = idx - position
    return index_alpha[new_idx]  # return the correct letter, O(1)


def puzzle(encoded_message: str):
    """
    Call decrypt_letter for each letter in the encoded_message
    :param encoded_message: message encrypted
    :return: message decrypted
    """
    message = ''
    for i, letter in enumerate(encoded_message):
        if letter.isalpha():
            message += decrypt_letter(letter, i)
        else:
            message += letter
    return message


# Tests
secret_messages = (
    "Ig Bsz swEo IrpHEtCxNN xLC ELDRLU, OSYP ocTiWp Bkauhn.",
    "Rfcg fhvCC DAzs MrQL OK GLPSQYI eVca eMYYh Rl yheiw MpthltAzm'C nyCv.",
    "Fftqesjv YoCqM HJrJM xKKRQICWWMSM bX TBlhWee gcia wdasu elu.",
    "Lbvh fz vrqsF WCuJ fIIPxLH ICFOX HeJi aa iefdl ako Zrukimhoht syFrzAyxwGwz.",
    "Ig Bsz DiwD FB vuK LNvNQCC JP QFIOQWO XROgdZfZ, pecqe kv f iwxu IEwIJvF vT pyQAI jYNJV fYcfU gURVbhb.",
    "Wjvk ynl ykypnG FIGCyxP, BRFCWII Ig GPe ARAZfgYt, wnu edr qlmy JAHF trLt DJ ANLVOQW.",
    "BfcxxnlBt sD osIJvJ NCwK TGMa.",
    "EyromhoA rC nrHIuI MBvJ GLPMKFMY.",
    "Sjospj pA lpFGsG KztH yLKOLFZ.",
    "CpospjD qB mqGHtH LAuI zMLPMKFEYKK.",
    "Fmcw ny jnDEqE IxrF HzOQCC.",
    "Sqcuwj pA lpFGsG KztH zBLRE.",
    "RfcgegosqCI oBICJJ.",
)


if __name__ == "__main__":
    for message in secret_messages:
        print(puzzle(message))
