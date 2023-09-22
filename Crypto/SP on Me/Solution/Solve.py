ciphertext = 0xff29803a1dc0ae1ac892ee0f6a9c88da6f2c408ec1ff5715245cfd7a9055a4301d85

S = [0xe, 0x4, 0xD, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7]
P = [0x6, 0x2, 0x5, 0x8, 0xd, 0x7, 0xc, 0x4, 0x3, 0xb, 0x0, 0xe, 0xa, 0x1, 0xf, 0x9]

S_inv = [0xe, 0x3, 0x4, 0x8, 0x1, 0xc, 0xa, 0xf, 0x7, 0xd, 0x9, 0x6, 0xb, 0x2, 0x0, 0x5]
P_inv = [0xa, 0xd, 0x1, 0x8, 0x7, 0x2, 0x0, 0x5, 0x3, 0xf, 0xc, 0x9, 0x6, 0x4, 0xb, 0xe]


class SP_Block:
    def __init__(self, word):
        self.word = word
        self.nibbles = [(self.word & 0xf000) >> 4*3,
                        (self.word & 0x0f00) >> 4*2,
                        (self.word & 0x00f0) >> 4*1,
                        (self.word & 0x000f) >> 4*0,
                        ]
        self.bits = [(self.word & 2 ** i) >> i for i in range(15, -1, -1)]

    def hex(self):
        return hex(self.word)[2:]

    def sub(self, Sbox):
        new_nibbles = [Sbox[n] for n in self.nibbles]
        new_word = sum([n*16**i for n, i in zip(new_nibbles, range(3, -1, -1))])
        return SP_Block(new_word)

    def perm(self, Pbox):
        perm_bits = [self.bits[Pbox[i]] for i in range(16)]
        new_word = sum([n*2**i for n, i in zip(perm_bits, range(15, -1, -1))])
        return SP_Block(new_word)

    def xor(self, key):
        new_word = key ^ self.word
        return SP_Block(new_word)


possible_keys = []
B = SP_Block(0xff29)
for key in range(0x10000):
    if B.xor(key).sub(S_inv).xor(key).perm(P_inv).sub(S_inv).xor(key).perm(P_inv).sub(S_inv).xor(key).hex() == '6379':
        possible_keys.append(key)

print(possible_keys) # [55738]

key = possible_keys[-1]


def decrypt(block: SP_Block, key):
    return block.xor(key).sub(S_inv).xor(key).perm(P_inv).sub(S_inv).xor(key).perm(P_inv).sub(S_inv).xor(key).hex()


h = hex(ciphertext)[2:]
cipher_blocks = []
for i in range(0, len(h), 4):
    block = h[i: i + 4]
    cipher_blocks.append(int(block, 16))
decipher_blocks = [decrypt(SP_Block(block), key) for block in cipher_blocks]
print(b''.fromhex(''.join(decipher_blocks))) # b'cygame{N07h1n6_7iK3_13rU72_F0RC3}\x00'
