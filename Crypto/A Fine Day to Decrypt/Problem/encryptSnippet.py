plaintext = 'secret'


def encrypt(x):
    return chr((21 * ord(x) + 73) % 128)


ciphertext = ''
for character in plaintext:
    ciphertext += encrypt(character)
print(ciphertext) # 8↕h#↕M
