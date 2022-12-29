# 2022 © All rights reserved. Pylar AI creative ML License. [License](https://huggingface.co/spaces/superdatas/LICENSE)

import random

# Welcome message
print("Welcome to the card game!")

# Set up the game
cards = ['💧', '🔥', '🪨', '💨', '🌱'] * 11
player_deck = []
computer_deck = []

# Dictionary to map cards to their effects
card_effects = {
    '💧': 'soak',
    '🔥': 'burn',
    '🪨': 'dig',
    '💨': 'blow',
    '🌱': 'grow'
}


def reset_game():
    """Reset the game by shuffling the cards and emptying the player and computer decks."""
    random.shuffle(cards)
    player_deck.clear()
    computer_deck.clear()


# Main game loop
while True:
    # Display menu
    print("\nMenu:")
    print("1. Play against the computer")
    print("2. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Deal cards to each player
        for i in range(11):
            player_deck.append(cards.pop())
            computer_deck.append(cards.pop())

        # Play the game
        for turn in range(1, 12):
            print(f"\nTurn {turn}:")
            print(f"Your card: {player_deck[turn-1]}")
            print(f"Computer's card: {computer_deck[turn-1]}")

            # Determine the winner of the turn
            player_effect = card_effects[player_deck[turn-1]]
            computer_effect = card_effects[computer_deck[turn-1]]
            if player_effect == 'soak' and computer_effect == 'burn':
                print("You win the turn!")
            elif player_effect == 'burn' and computer_effect == 'soak':
                print("Computer wins the turn.")
            elif player_effect == 'dig' and computer_effect == 'blow':
                print("You win the turn!")
            elif player_effect == 'blow' and computer_effect == 'dig':
                print("Computer wins the turn.")
            elif player_effect == 'grow' and computer_effect == 'soak':
                print("You win the turn!")
            elif player_effect == 'soak' and computer_effect == 'grow':
                print("Computer wins the turn.")
            else:
                print("It's a tie!")

            # Wait for the user to press enter before continuing
            input("Press enter to continue...")

        # Determine the overall winner
        player_score = player_deck.count('💧') + player_deck.count(
            '🔥') + player_deck.count('🪨') + player_deck.count('💨') + player_deck.count('🌱')
        computer_score = computer_deck.count('💧') + computer_deck.count(
            '🔥') + computer_deck.count('🪨') + computer_deck.count('💨') + computer_deck.count('🌱')

        # Display the scores
        print(f"\nYour score: {player_score}")
        print(f"Computer score: {computer_score}")

        # Display the winner
        if player_score > computer_score:
            print("You win!")
        elif player_score < computer_score:
            print("Computer wins.")
        else:
            print("It's a tie!")

        # Reset the game
        reset_game()
    elif choice == '2':
        # Quit the game
        break
    else:
        # Invalid choice
        print("Invalid choice.")

# Goodbye message
print("Thanks for playing!")

# Path: game.py
