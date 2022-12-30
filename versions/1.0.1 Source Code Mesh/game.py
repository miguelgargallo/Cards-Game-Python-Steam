# 2022 © All rights reserved. Pylar AI creative ML License. [License](https://huggingface.co/spaces/superdatas/LICENSE)

import random

from turns import *

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


def cards_in_turn_1():
    """Print cards in turn 1."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
    # Paint table 1 with 22x11 pixels in the terminal
        print('┌' + '─' * 11 + '┐')
        print('│' + (f"{player_deck[turn-1]}") + 'Vs' + (f"{computer_deck[turn-1]}") + ' ' *
              1 + '│')
        print('│' + ' ' *
              10 + '│')
        print('└' + '─' * 11 + '┘')

# Define table 22x22 in the terminal


def table():
    """Display 22 x 22 pixels table in the terminal."""
    print('┌' + '─' * 22 + '┐')
    for i in range(1):
        # Print table and cards used by myself and rival
        print('│' + (f"{player_deck[turn-1]}") + 'Vs' + (f"{computer_deck[turn-1]}") + ' ' *
              22 + '│')
    print('└' + '─' * 22 + '┘')


def cards_used_by_myself():
    """Display cards used by myself in the terminal one by one nearby the table axys y"""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")


def cards_used_by_rival():
    """Display cards used by rival in the terminal one by one nearby the table axys y"""
    for i in range(1):
        print(f"Computer's card: {computer_deck[turn-1]}")


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

        # Play the game 11 turns from turns.py
        for turn in range(1, 12):
            print(f"\nTurn {turn}:")
            print(f"table: {table()}")
            print(f"cards_in_turn_1: {cards_in_turn_1()}")
            print()

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

        # On final round, show the card table
        print("\nCard table:")
        print("Player's cards:", end=' ')
        for card in player_deck:
            print(card, end=' ')
        print()
        print("Computer's cards:", end=' ')
        for card in computer_deck:
            print(card, end=' ')
        print()

        # Wait for the user to press enter before continuing
        input("Press enter to continue...")

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
