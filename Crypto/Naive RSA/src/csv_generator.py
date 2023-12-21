from Crypto.Util.number import bytes_to_long, getPrime
from math import gcd, lcm


def encrypt(message, e):
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
    
    return c, n, e


message = b'flag{M1gH7_W4N7_50M3_P4DD1nG_Nex7_t1m3}'

file = open('ciphertexts.csv', 'w')
file.write('Message,c,n,e\n')
for i in range(1, 101):
    c, n, e = encrypt(message, 17)
    file.write(f'{i},{c},{n},{e}\n')
file.close()
