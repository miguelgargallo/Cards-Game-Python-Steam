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

# Shuffle the cards
random.shuffle(cards)

# Deal the cards
for i in range(5):
    player_deck.append(cards.pop())
    computer_deck.append(cards.pop())

# Start the game
turn = 1
while len(player_deck) > 0 and len(computer_deck) > 0:
    print(f"Turn {turn}")

    # Print cards in turn 1
    if turn == 1:
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
    if turn >= 2:
        # Display 22 x 22 pixels table in the terminal
        print('┌' + '─' * 22 + '┐')
        for i in range(1):
            # Print table and cards used by myself and rival
            print('│' + (f"{player_deck[turn-1]}") + 'Vs' + (f"{computer_deck[turn-1]}") + ' ' *
                  22 + '│')
        print('└' + '─' * 22 + '┘')

    # Display cards used by myself in the terminal one by one nearby the table axys y
    if turn >= 2:
        for i in range(1):
            print(' ' * 22 + (f"{player_deck[turn-1]}"))

    # Display cards used by rival in the terminal one by one nearby the table axys y
    if turn >= 2:
        for i in range(1):
            print(' ' * 22 + (f"{computer_deck[turn-1]}"))

    # Define get_player_move function
    def get_player_move():
        """Get the player's move."""
        player_move = input(
            "Do you want to (1) compare cards or (2) draw a new card? ")
        while player_move not in ['1', '2']:
            player_move = input(
                "Do you want to (1) compare cards or (2) draw a new card? ")
        return player_move

    # Get the player's move
    player_move = get_player_move()

    # Define draw_card function
    def draw_card():
        """Draw a card from the deck."""
        return random.choice(list(card_effects.keys()))

    # Process the player's move
    if player_move == '1':
        # Compare cards
        if card_effects[player_deck[turn-1]] == card_effects[computer_deck[turn-1]]:
            print("It's a tie!")
        elif card_effects[player_deck[turn-1]] == 'soak' and card_effects[computer_deck[turn-1]] == 'burn':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'soak' and card_effects[computer_deck[turn-1]] == 'dig':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'soak' and card_effects[computer_deck[turn-1]] == 'blow':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'soak' and card_effects[computer_deck[turn-1]] == 'grow':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'burn' and card_effects[computer_deck[turn-1]] == 'soak':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'burn' and card_effects[computer_deck[turn-1]] == 'soak':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'burn' and card_effects[computer_deck[turn-1]] == 'dig':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'burn' and card_effects[computer_deck[turn-1]] == 'blow':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'burn' and card_effects[computer_deck[turn-1]] == 'grow':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'dig' and card_effects[computer_deck[turn-1]] == 'soak':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'dig' and card_effects[computer_deck[turn-1]] == 'burn':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'dig' and card_effects[computer_deck[turn-1]] == 'blow':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'dig' and card_effects[computer_deck[turn-1]] == 'grow':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'blow' and card_effects[computer_deck[turn-1]] == 'soak':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'blow' and card_effects[computer_deck[turn-1]] == 'burn':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'blow' and card_effects[computer_deck[turn-1]] == 'dig':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'blow' and card_effects[computer_deck[turn-1]] == 'grow':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'grow' and card_effects[computer_deck[turn-1]] == 'soak':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'grow' and card_effects[computer_deck[turn-1]] == 'soak':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'grow' and card_effects[computer_deck[turn-1]] == 'burn':
            print("You lose!")
            player_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'grow' and card_effects[computer_deck[turn-1]] == 'dig':
            print("You win!")
            computer_deck.pop()
        elif card_effects[player_deck[turn-1]] == 'grow' and card_effects[computer_deck[turn-1]] == 'blow':
            print("You lose!")
            player_deck.pop()
        else:
            print("You lose!")
            player_deck.pop()
    elif player_move == '2':
        # Draw a card
        player_deck.append(draw_card())
        computer_deck.append(draw_card())
        turn += 1

    # Display the player's deck
    print("Your deck: " + str(player_deck))

    # Display the computer's deck
    print("Computer's deck: " + str(computer_deck))

    # Display the player's score
    print("Your score: " + str(len(player_deck)))

    # Display the computer's score
    print("Computer's score: " + str(len(computer_deck)))

    # Check if the game is over
    if len(player_deck) == 0:
        print("You lose!")
        break
    elif len(computer_deck) == 0:
        print("You win!")
        break

    # Check if the game is a tie
    if turn == 10:
        print("Its a tie!")
        break

    # Display the turn number
    print("Turn " + str(turn))
