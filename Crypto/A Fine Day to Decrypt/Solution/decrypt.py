'''
The modulus 128 of our affine cipher hints that we are likely dealing with ASCII.  Fortunately, ASCII and Unicode
coincide with their mappings under the domain of integers between 0 and 127.
Check details.docx for a more mathematical explanation on how to find an inverse for function f.
Also notice the plaintext mentions Unicode offering larger character support (this is an important hint to the
sequential challenge, A Finer Day to Decrypt.
'''

file = open('ciphertext.txt', 'rb')
ciphertext = file.read()
file.close()

a = 21 #coefficient of x in our affine cipher
b = 73 #constant in our affine cipher

# We can find the multiplicative inverse of 21 (mod 128) using the native pow function (Python 3.8 and later)
a_inv = pow(a, -1, 128) # 21^-1 (mod 128)
b_inv = -b % 128


def decrypt(x):
    return chr(a_inv * (x + b_inv) % 128)


plaintext = ''
for character in ciphertext:
    plaintext += decrypt(character)
print(plaintext)
