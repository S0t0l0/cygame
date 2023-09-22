import random

choices = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'l': 'lizard', 'k': 'spock'}

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!", ""

    if player_choice == 'r':
        if computer_choice == 's':
            return 'You win!', 'Rock smashes Scissors'
        elif computer_choice == 'l':
            return 'You win!', 'Rock crushes Lizard'
        else:
            return 'Computer wins!', f"{choices[computer_choice].capitalize()} covers Rock"
    elif player_choice == 'p':
        if computer_choice == 'r':
            return 'You win!', 'Paper covers Rock'
        elif computer_choice == 'k':
            return 'You win!', 'Paper disproves Spock'
        else:
            return 'Computer wins!', f"{choices[computer_choice].capitalize()} cuts Paper"
    elif player_choice == 's':
        if computer_choice == 'p':
            return 'You win!', 'Scissors cuts Paper'
        elif computer_choice == 'l':
            return 'You win!', 'Scissors decapitates Lizard'
        else:
            return 'Computer wins!', f"{choices[computer_choice].capitalize()} smashes Scissors"
    elif player_choice == 'l':
        if computer_choice == 'p':
            return 'You win!', 'Lizard eats Paper'
        elif computer_choice == 'k':
            return 'You win!', 'Lizard poisons Spock'
        else:
            return 'Computer wins!', f"{choices[computer_choice].capitalize()} crushes Lizard"
    elif player_choice == 'k':
        if computer_choice == 'r':
            return 'You win!', 'Spock vaporizes Rock'
        elif computer_choice == 's':
            return 'You win!', 'Spock smashes Scissors'
        else:
            return 'Computer wins!', f"{choices[computer_choice].capitalize()} disproves Spock"
    else:
        return 'Invalid choice. Game over.', ""

def display_ascii(choice):
    if choice == 'r':
        return [
            "    _______           ",
            "---'   ____)          ",
            "      (_____)         ",
            "      (_____)         ",
            "      (____)          ",
            "---.__(___)           "
        ]
    elif choice == 'p':
        return [
            "    _______           ",
            "---'   ____)____      ",
            "          ______)     ",
            "       __________)    ",
            "       _________)     ",
            "---.__________)       "
        ]
    elif choice == 's':
        return [
            "    _______           ",
            "---'   ____)____      ",
            "          ______)     ",
            "       __________)    ",
            "      (____)          ",
            "---.__(___)           "
        ]
    elif choice == 'l':
        return [
            "    _______           ",
            "---'   ____)____      ",
            "          ______)     ",
            "       ____)          ",
            "      (____)          ",
            "---.__(___)           "
        ]
    elif choice == 'k':
        return [
            "    _______           ",
            "---'   ____)____      ",
            "          ______)     ",
            "       ____)____      ",
            "      (__________)    ",
            "---.____________)     "
        ]
    else:
        return []
f14g = [11, 79, 44, 83, 3, 37, 66, 63, 19, 114, 85, 112, 122, 6, 60, 117, 69, 67, 105, 46, 80, 5, 122, 11, 32, 113, 119, 74, 124, 5, 34, 108, 114, 6, 60, 110, 1, 61, 126, 63, 88, 98, 20, 70, 93, 8, 102, 64, 109, 113, 25]
def mirror_ascii(ascii_art):
    mirrored_art = []
    for line in ascii_art:
        mirrored_line = line.replace("(", ")").replace(")", "(")[::-1]
        mirrored_art.append(mirrored_line)
    return mirrored_art

def xor_decrypt(ciphertext, key):
    """Decrypt ciphertext using XOR with the given key"""
    decrypted = []
    key_index = 0

    for char in ciphertext:
        decrypted_char = chr(char ^ ord(key[key_index]))
        decrypted.append(decrypted_char)

        key_index = (key_index + 1) % len(key)

    return ''.join(decrypted)
key1 = r"h6K2"
def combine_ascii(ascii_art1, ascii_art2):
    combined_art = []
    for line1, line2 in zip(ascii_art1, ascii_art2):
        combined_line = line1 + "    " + line2
        combined_art.append(combined_line)
    return combined_art

def play_game():
    print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
    print("Choices: r - rock, p - paper, s - scissors, l - lizard, k - spock")
    key3 = r"3%7f*1p!q"
    player_wins = 0

    while player_wins < 15:
        player_choice = input("Enter your choice: ").lower()
        if player_choice not in choices:
            print('Invalid choice. Game over.')
            return

        computer_choice = random.choice(list(choices.keys()))
        player_art = display_ascii(player_choice)
        computer_art = mirror_ascii(display_ascii(computer_choice))
        key2 = r"n@9s#5d"
        # Combine player's and computer's ASCII art
        combined_art = combine_ascii(player_art, computer_art)

        # Find the maximum line length
        max_length = max(len(line) for line in combined_art)

        print("Player's Choice:             Computer's Choice:")
        for line in combined_art:
            print(line.ljust(max_length))

        result, explanation = determine_winner(player_choice, computer_choice)
        print("\n" + result)
        if explanation:
            print(explanation)

        if result == 'You win!':
            player_wins += 1
            print("Your choices: " + ", ".join(choices.values()))
        elif result == 'Computer wins!':
            print("\nToo bad, so sad!")
            break

        print(f"Win Counter: {player_wins}\n")
        print("Lets play again, make your choice.")
        print("Choices: r - rock, p - paper, s - scissors, l - lizard, k - spock\n")

    if player_wins == 15:
        print("Congratulations! You beat the computer 15 times in a row!")
        print(f"Your Flag is {xor_decrypt(f14g, key1+key2+key3)}")

play_game()
