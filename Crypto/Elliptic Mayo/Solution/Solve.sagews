p = 0xdb8f1e4884c47bfb
a = 0xdb8f1e4884c47bf8
b = 0xba0adf33491811a8
E = EllipticCurve(GF(p), (a, b))
G = E(0x18c87d6cc12ee703, 0x869a10ce9f08ed34)
n = E.order()
prime_factors(n)

# [15820897315794384701]

b1 = 0xed0e0818000417c8
E1 = EllipticCurve(GF(p), (a, b1))
G1 = E1(0x6a71de4cf2c7bc02, 0x552e50cbc80691a7)
d_AG1 = E1(0x7fe76431e04a0aaa, 0x8b99f0d205e1aa6)
modulus1 = G1.order()
remainder1 = G1.discrete_log(d_AG1)
remainder1, modulus1

# (13087305027, 66820844767)

b2 = 0xd33e7fc2ba39f952
E2 = EllipticCurve(GF(p), (a, b2))
G2 = E2(0x20b95fb49c0abba3, 0x86a9d9e1156788e4)
d_AG2 = E2(0xc37fca91993c3e76, 0xcf780d75c662fa11)
modulus2 = G2.order()
remainder2 = G2.discrete_log(d_AG2)
remainder2, modulus2

# (4614858334, 44177846483)

d_A = crt(remainder1, remainder2, modulus1, modulus2)
hex(d_A)

# 0x9835ed3d021d65dc

d_BG = E(0x1ce10c7c5989866e, 0x176acbd73cf15bc8)
S = d_A * d_BG
S.xy()

# (8716978289614203805, 7923394114363233555)

from Crypto.Cipher import AES

x = int(S.xy()[0])
y = int(S.xy()[1])
K = int((x << 64) ^^ y).to_bytes(16, 'big')
V = int((y << 64) ^^ x).to_bytes(16, 'big')
cipher = AES.new(K, 2, V)
ciphertext = int(0x01c62e810475ee812688c2ef10bdd5cfe3bceb68d6ffbb2ee1d1d5d1b2653274).to_bytes(32, 'big')
cipher.decrypt(ciphertext)

# b'cygame{7H13r_CuRv3_G4m3_W3ak}\x03\x03\x03'









