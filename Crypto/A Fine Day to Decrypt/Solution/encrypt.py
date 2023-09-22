file = open('plaintext.txt', 'rb')
content = file.read().decode()


def f(x):
    return (21 * x + 73) % 128


def encrypt(M):
    return ''.join([chr(f(ord(m))) for m in M])


c = encrypt(content).encode()
w = open('ciphertext.txt', 'wb')
w.write(c)
w.close()
