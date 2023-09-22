import random
import sys

def xor_decrypt(ciphertext, key):
    """Decrypt ciphertext using XOR with the given key"""
    decrypted = []
    key_index = 0

    for char in ciphertext:
        decrypted_char = chr(char ^ ord(key[key_index]))
        decrypted.append(decrypted_char)

        key_index = (key_index + 1) % len(key)

    return ''.join(decrypted)

def calculate_score(cards):
    """Calculate the total value of a list of cards"""
    score = 0
    num_aces = 0

    for card in cards:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            score += 11
            num_aces += 1
        else:
            score += card

    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1

    return score

def play_blackjack():
    """Play a game of blackjack"""
    print("Let's play Blackjack!")

    # Deal initial cards to the player
    player_cards = []
    for _ in range(2):
        player_cards.append(random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']))

    player_score = calculate_score(player_cards)

    print(f"\nYour cards: {player_cards}, current score: {player_score}")

    if player_score == 21:
        print("Blackjack! You win!")
        return 1
    else:
        print("You lose!")
        return 0

def main():
    key2 = "GPAWJRMSADGH"
    consecutive_blackjacks = 0
    total_hands = 0

    flag = [34, 53, 44, 43, 62, 33, 55, 8, 122, 41, 36, 30, 100, 36, 54, 18, 99, 47, 27, 115, 23, 13, 124, 126, 127, 46]
    key1 = "ALKJSDLKN"

    while total_hands < 3:
        input("Press any key to deal a hand...")
        blackjack_count = play_blackjack()
        if blackjack_count == 1:
            consecutive_blackjacks += 1
            if consecutive_blackjacks == 3:
                print("\nCongratulations! You are really cool or have too much time on your hands!")
                print("Here is your decrypted flag:")
                print(xor_decrypt(flag, (key1+key2)))
                input("Press Enter to exit...")
        else:
            consecutive_blackjacks = 0

        total_hands += 1
        print()  # Add a new line between each hand

    else:
        print(f"\nToo bad! You only got dealt {consecutive_blackjacks} blackjacks.")
        input("Press Enter to exit...")
if __name__ == "__main__":
    main()


