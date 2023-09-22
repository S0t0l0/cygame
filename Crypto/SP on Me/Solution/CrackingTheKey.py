from BuildingTheNetwork import WordBlock

S_inv = [0xe, 0x3, 0x4, 0x8, 0x1, 0xc, 0xa, 0xf, 0x7, 0xd, 0x9, 0x6, 0xb, 0x2, 0x0, 0x5]
P_inv = [0xa, 0xd, 0x1, 0x8, 0x7, 0x2, 0x0, 0x5, 0x3, 0xf, 0xc, 0x9, 0x6, 0x4, 0xb, 0xe]


def decrypt(cipherhex, key):
    words = [int(cipherhex[i:i+4], 16) for i in range(0, len(cipherhex), 4)]
    plainhex = ''
    for word in words:
        state = WordBlock(word)
        state = state.xor(key).substitute(S_inv)
        for i in range(2):
            state = state.xor(key).permutate(P_inv).substitute(S_inv)
        state = state.xor(key)
        plainhex += state.tohex()
    plaintext = bytes.fromhex(plainhex).decode()
    if plaintext[-1] == '\x00':
        return plaintext[:-1]
    return plaintext


cipherhex = 'ff29803a1dc0ae1ac892ee0f6a9c88da6f2c408ec1ff5715245cfd7a9055a4301d85'

for i in range(0x10000):
    try:
        if decrypt('ff29', i) == 'cy':
            key = i
    except:
        continue

print(decrypt(cipherhex, key))
#cygame{N07h1n6_7iK3_13rU72_F0RC3}
