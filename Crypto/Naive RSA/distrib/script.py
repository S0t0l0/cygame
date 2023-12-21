from Crypto.Util.number import bytes_to_long, getPrime
from math import gcd, lcm


message = b'flag{REDACTED}'

e = 17
key_size = 512

p = getPrime(key_size)
q = getPrime(key_size)

n = p * q

Carmichael_n = lcm(p - 1, q - 1)

while gcd(e, Carmichael_n) != 1:
    p = getPrime(key_size)
    q = getPrime(key_size)
    Carmichael_n = lcm(p - 1, q - 1)


c = (bytes_to_long(message) ** e) % n
