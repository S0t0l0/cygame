from Crypto.Util.number import long_to_bytes
from math import gcd, lcm


def crt(Remainders, Moduli):
    sum = 0
    N = 1
    for n in Moduli:
        N *= n
    for r_i, n_i in zip(Remainders, Moduli):
        p = N // n_i
        sum += r_i * pow(p, -1, n_i) * p
    return sum % N


def find_invpow(x,n):
    '''Uses binary search to find the integral n_th root of x'''
    high = 1
    while high ** n <= x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


content = open('ciphertexts.csv', 'r').read()
rows = content.split('\n')
Ciphers = []
Moduli = []

if gcd(*Moduli) == 1:
    print(gcd(*Moduli))
    null = input()
    exit()

for row in rows[1:18]:
    id_, c, n, e = row.split(',')
    Ciphers.append(int(c))
    Moduli.append(int(n))

Chinese_remainder = crt(Ciphers, Moduli)
message_bytes = find_invpow(Chinese_remainder, 17)
message = long_to_bytes(message_bytes)
print(message)
null = input()

