file = open('plaintext.txt', 'rb')
content = file.read().decode()


def f(x):
    return (489891 * x + 534965) % 1114111


def encrypt(M):
    return ''.join([chr(f(ord(m))) for m in M])


c = encrypt(content).encode(errors='backslashreplace')
w = open('ciphertext.txt', 'wb')
w.write(c)
w.close()
