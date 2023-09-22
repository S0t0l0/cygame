'''
Notice, with our modulus, hex(1114111) = 0x10ffff, the maximum number supported by Unicode.  This likely means our
ciphertext is encoded with Unicode, so we can take advantage of str.encode(), bytes.decode(), chr(int), and ord(str).
Technically, the max 0x10ffff means Unicode can support 1114112 characters; however, 1114111 is more desirable as it
is prime.  Consequently, the coefficient for x can be any integer strictly between 0 and 1114111
(integers mod prime form a finite field). As such, it is significantly harder to brute force a solution. In this case,
we will notate the integers mod 1114111 as GF(1114111).
'''

file = open('ciphertext.txt', 'rb')
content = file.read().decode()

a = 489891 #coefficient of x in our affine cipher
b = 534965 #constant in our affine cipher

#A naive way to find the multiplicative inverse of a = 489891 in GF(1114111) but is still fairly quick
a_mult_inv = 1
while (a_mult_inv * a) % 1114111 != 1:
    a_mult_inv += 1

b_add_inv = 1114111 - b #Additive inverse of b = 534965 in GF(1114111)


def f_inv(x):
    return (a_mult_inv * x + a_mult_inv * b_add_inv) % 1114111


def decrypt(M):
    return ''.join([chr(f_inv(ord(m))) for m in M])


sol = open('plaintext.txt', 'wb')
sol.write(decrypt(content).encode())
print(decrypt(content))
