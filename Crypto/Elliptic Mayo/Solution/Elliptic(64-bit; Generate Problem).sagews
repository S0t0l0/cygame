p = 0xdb8f1e4884c47bfb
a = 0xdb8f1e4884c47bf8
b = 0xba0adf33491811a8
E = EllipticCurve(GF(p), (a, b))
G = (0x18c87d6cc12ee703, 0x869a10ce9f08ed34)
n = E.order()
n 
# 15820897315794384701
prime_factors(n) 
# [15820897315794384701]
G = E.gen(0)
# G = (0x18c87d6cc12ee703 : 0x869a10ce9f08ed34 : 1)

# SUPER SECRET #
d_A = 0x9835ed3d021d65dc
d_B = 0x9ea444b75dee6ac6
d_Ad_BG = (0x78f8ed91e33f2b9d, 0x6df58cf7920a9513)
# SUPER SECRET #

# SHOW IN Instructions #
d_AG = (0x28aa430008a24715, 0x537c24c86f3f17a4)
d_BG = (0x1ce10c7c5989866e, 0x176acbd73cf15bc8)

# New Curve Function#
def NewCurve():
    bi = randint(0, 2**64)
    print('b_i = ' + hex(bi))
    Ei = EllipticCurve(GF(p), (a, bi))
    ni = Ei.order()
    return prime_factors(ni)

### Discrete Log Function ###
def DL(curve, prime):
    Q = curve.gen(0) * int(curve.order() / prime)
    print (f'Q = ({hex(Q.xy()[0])}, {hex(Q.xy()[1])})')
    d_AQ = (d_A * Q).xy()
    print(f'd_AQ = ({hex(d_AQ[0])}, {hex(d_AQ[1])})')
    return Q.discrete_log(curve(d_AQ))

# Invalid Curve 1 #
b1 = 0xed0e0818000417c8
E1 = EllipticCurve(GF(p), (a, b1))
n1 = E1.order()
prime_factors(n1)
# [2, 3, 41, 320821, 66820844767]
DL(E1, 66820844767)
# Q = (0x6a71de4cf2c7bc02, 0x552e50cbc80691a7)
# d_AQ = (0x7fe76431e04a0aaa, 0x8b99f0d205e1aa6)
# 13087305027

# Invalid Curve 2 #
b2 = 0xd33e7fc2ba39f952
E2 = EllipticCurve(GF(p), (a, b2))
n2 = E2.order()
prime_factors(n2)
# [2, 3, 19, 3141389, 44177846483]
DL(E2, 44177846483)
# Q = (0x20b95fb49c0abba3, 0x86a9d9e1156788e4)
# d_AQ = (0xc37fca91993c3e76, 0xcf780d75c662fa11)
# 4614858334

### THE SHARED KEY (DO NOT SHOW) ###
crt(13087305027, 4614858334, 66820844767, 44177846483)*d_B*E(G)
# (8716978289614203805 : 7923394114363233555 : 1)

### x-coord of Secret Key (DO NOT SHOW) ###
hex(8716978289614203805)
# 0x78f8ed91e33f2b9d
### y-coord of Secret Key (DO NOT SHOW) ###
hex(7923394114363233555)
# 0x6df58cf7920a9513









