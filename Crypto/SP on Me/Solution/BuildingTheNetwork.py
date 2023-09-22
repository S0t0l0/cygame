class WordBlock:
    def __init__(self, word):
        self.word = word
        self.nibbles = [(word >> 4 * i) & 0xf for i in range(4)][::-1]
        self.bits = [(word >> i) & 0x1 for i in range(16)][::-1]

    def tohex(self):
        return hex(self.word)[2:]

    def xor(self, word1):
        return WordBlock(self.word ^ word1)

    def substitute(self, sbox):
        return WordBlock(sum([sbox[nibble] * 16 ** i for nibble, i in zip(self.nibbles[::-1], range(4))]))

    def permutate(self, pbox):
        pbits = [self.bits[pbox[i]] for i in range(16)]
        return WordBlock(sum(pbits[::-1][i] * 2 ** i for i in range(16)))


if __name__=='__main__':
    S = [0xe, 0x4, 0xD, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7]
    P = [0x6, 0x2, 0x5, 0x8, 0xd, 0x7, 0xc, 0x4, 0x3, 0xb, 0x0, 0xe, 0xa, 0x1, 0xf, 0x9]

    def encrypt(plaintext, key):
        if len(plaintext.encode()) % 2:
            plaintext += '\x00'
        plainhex = plaintext.encode().hex()
        words = [int(plainhex[i:i+4], 16) for i in range(0, len(plainhex), 4)]
        cipherhex = ''
        for word in words:
            state = WordBlock(word)
            for i in range(2):
                state = state.xor(key).substitute(S).permutate(P)
            state = state.xor(key).substitute(S).xor(key)
            cipherhex += state.tohex()
        return cipherhex