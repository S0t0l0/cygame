class Word:
    def __init__(self, word):
        self.left = word >> 8
        self.right = word & 0xff

    def splice(self):
        return self.left << 8 | self.right

    def hex(self):
        return hex(self.left << 8 | self.right)


def round_function(x):
    y = -x % 256
    return (y << 4) & 0xff | (y >> 4)


R = [round_function(x) for x in range(256)]

P1 = Word(0x0041)
E_P1 = Word(0x7e0a)
E_P1x8080 = Word(0x4732)
E_P1x0080 = Word(0x0884)
E_P1x0008 = Word(0xd6dc)

P2 = Word(0x0079)
E_P2 = Word(0xd522)
E_P2x8080 = Word(0xce3a)
E_P2x0080 = Word(0xa3ac)
E_P2x0008 = Word(0x9d14)

P3 = Word(0x9f5e)
E_P3 = Word(0xcea3)
E_P3x8080 = Word(0xd6b4)
E_P3x0080 = Word(0x4623)
E_P3x0008 = Word(0xba5b)


def crack_K5(C: Word, dC: Word):
    S = set()
    for key in range(256):
        if (R[C.right ^ C.left ^ key] ^ C.right) ^ (R[dC.right ^ dC.left ^ key] ^ dC.right) == 0x08:
            S.add(key)
    return S


S1 = crack_K5(E_P1, E_P1x8080)
S2 = crack_K5(E_P2, E_P2x8080)
S3 = crack_K5(E_P3, E_P3x8080)
S = set.intersection(S1, S2, S3)
print(S)


def R5_inv(C: Word, k5):
    D = Word(0x0000)
    D.left = C.left ^ C.right
    D.right = R[C.right ^ C.left ^ k5] ^ C.right
    return Word(D.splice())


def crack_K4(C: Word, dC: Word, k5):
    S = set()
    C = R5_inv(C, k5)
    dC = R5_inv(dC, k5)
    for key in range(256):
        if (R[C.right ^ key] ^ C.left) ^ (R[dC.right ^ key] ^ dC.left) == 0x80:
            S.add(key)
    return S

F = []
for s in S:
    T1 = crack_K4(E_P1, E_P1x8080, s)
    T2 = crack_K4(E_P2, E_P2x8080, s)
    T3 = crack_K4(E_P3, E_P3x8080, s)
    Ti_cap = set.intersection(T1, T2, T3)
    if Ti_cap:
        F.append(Ti_cap)
T = set.union(*F)
print(T)

def R4_inv(C: Word, k5, k4):
    C = R5_inv(C, k5)
    D = Word(0x0000)
    D.left = R[C.right ^ k4] ^ C.left
    D.right = C.right
    return Word(D.splice())

def crack_K3(C: Word, dC: Word, k5, k4):
    S = set()
    C = R4_inv(C, k5, k4)
    dC = R4_inv(dC, k5, k4)
    for key in range(256):
        if (R[C.left ^ key] ^ C.right) ^ (R[dC.left ^ key] ^ dC.right) == 0x80:
            S.add(key)
    return S

from itertools import product
possible_keys = product(S, T)
F = []
for key in possible_keys:
    U1 = crack_K3(E_P1, E_P1x0080, *key)
    U2 = crack_K3(E_P2, E_P2x0080, *key)
    U3 = crack_K3(E_P3, E_P3x0080, *key)
    Ui_cap = set.intersection(U1, U2, U3)
    if Ui_cap:
        F.append(Ui_cap)
U = set.union(*F)
print(U)

def R3_inv(C:Word, k5, k4, k3):
    C = R4_inv(C, k5, k4)
    D = Word(0)
    D.left = C.left
    D.right = R[C.left ^ k3] ^ C.right
    return Word(D.splice())

def crack_K2(C: Word, dC: Word, k5, k4, k3):
    S = set()
    C = R3_inv(C, k5, k4, k3)
    dC = R3_inv(dC, k5, k4, k3)
    for key in range(256):
        if (R[C.right ^ key] ^ C.left) ^ (R[dC.right ^ key] ^ dC.left) == 0x00:
            S.add(key)
    return S

possible_keys = product(S, T, U)
F = []
for key in possible_keys:
    V1 = crack_K2(E_P1, E_P1x0008, *key)
    V2 = crack_K2(E_P2, E_P2x0008, *key)
    V3 = crack_K2(E_P3, E_P3x0008, *key)
    Vi_cap = set.intersection(V1, V2, V3)
    if Vi_cap:
        F.append(Vi_cap)
V = set.union(*F)
print(V)

def R2_inv(C: Word, k5, k4, k3, k2):
    C = R3_inv(C, k5, k4, k3)
    D = Word(0x0000)
    D.left = R[C.right ^ k2] ^ C.left
    D.right = C.right
    return Word(D.splice())

def crack_K1(C: Word, P: Word, k5, k4, k3, k2):
    S = set()
    C = R2_inv(C, k5, k4, k3, k2)
    for key in range(256):
        if C.right ^ C.left ^ key == P.right:
            S.add(key)
    return S

possible_keys = product(S, T, U, V)
F = []
for key in possible_keys:
    W1 = crack_K1(E_P1, P1, *key)
    W2 = crack_K1(E_P2, P2, *key)
    W3 = crack_K1(E_P3, P3, *key)
    Wi_cap = set.intersection(W1, W2, W3)
    if Wi_cap:
        F.append(Wi_cap)
W = set.union(*F)
print(W)

def crack_K0(C: Word, P:Word, k5, k4, k3, k2):
    S = set()
    C = R2_inv(C, k5, k4, k3, k2)
    for key in range(256):
        if C.left ^ key == P.left:
            S.add(key)
    return S

possible_keys = product(S, T, U, V)
F = []
for key in possible_keys:
    X1 = crack_K0(E_P1, P1, *key)
    X2 = crack_K0(E_P2, P2, *key)
    X3 = crack_K0(E_P3, P3, *key)
    Xi_cap = set.intersection(X1, X2, X3)
    if Xi_cap:
        F.append(Xi_cap)
X = set.union(*F)
print(X)

def R1_inv(C: Word, k5, k4, k3, k2, k1, k0):
    C = R2_inv(C, k5, k4, k3, k2)
    D = Word(0x0000)
    D.left = C.left ^ k0
    D.right = C.right ^ C.left ^ k1
    return Word(D.splice())

possible_keys = product(S, T, U, V, W, X)

P4 = Word(0x6379)
E_P4 = Word(0x7a47)
P5 = Word(0x455f)
E_P5 = Word(0x8223)
P6 = Word(0x366f)
E_P6 = Word(0x1a2f)

ciphertext = '7a47857bcbd5a8c5bed41936ad897f463543b35a31bba9a335a97ff6ae0aced65a3182231a2f813ab5b532a8933cd448eaf0'
CBlocks = []
h = len(ciphertext)
for i in range(0, h, 4):
    CBlocks.append(int(ciphertext[i:i+4], 16))
for key in possible_keys:
    check1 = R1_inv(E_P1, *key).splice() == P1.splice()
    check2 = R1_inv(E_P2, *key).splice() == P2.splice()
    check3 = R1_inv(E_P3, *key).splice() == P3.splice()
    check4 = R1_inv(E_P4, *key).splice() == P4.splice()
    check5 = R1_inv(E_P5, *key).splice() == P5.splice()
    check6 = R1_inv(E_P6, *key).splice() == P6.splice()
    if check1 and check2 and check3 and check4 and check5 and check6:
        PBlocks = [R1_inv(Word(CBlock), *key).hex()[2:] for CBlock in CBlocks]
        print(b''.fromhex(''.join(PBlocks)))


