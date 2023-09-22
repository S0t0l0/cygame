f = open('Message.txt', 'r')
ciphertext = f.read()
lines = ciphertext.split('\n')[:-1]
binary = [character.replace(' ', '0').replace('\t', '1') for character in lines]
plaintext = ''.join([chr(int(b, 2)) for b in binary])
print(plaintext)
input('\nFinished')
