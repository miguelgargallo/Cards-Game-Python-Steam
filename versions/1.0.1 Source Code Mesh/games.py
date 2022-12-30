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

# Shuffle the cards
random.shuffle(cards)

# Deal the cards
for i in range(5):
    player_deck.append(cards.pop())
    computer_deck.append(cards.pop())

# Start the game
turn = 1


def get_player_move():
    """Get the player's move."""
    player_move = input(
        "Do you want to (1) compare cards or (2) draw a new card? ")
    while player_move not in ['1', '2']:
        player_move = input(
            "Do you want to (1) compare cards or (2) draw a new card? ")
    return player_move


def draw_card(deck):
    """Draw a card from the deck."""
    if len(cards) > 0:
        deck.append(cards.pop())
    else:
        print("There are no more cards left in the deck.")


def compare_cards(player_card, computer_card):
    """Compare the player's and computer's cards."""
    if card_effects[player_card] == card_effects[computer_card]:
        print("It's a tie!")
    elif card_effects[player_card] == 'soak' and card_effects[computer_card] == 'burn':
        print("You win!")
        computer_deck.pop()
    elif card_effects[player_card] == 'burn' and card_effects[computer_card] == 'soak':
        print("You lose!")
        player_deck.pop()
    elif card_effects[player_card] == 'dig' and card_effects[computer_card] == 'blow':
        print("You win!")
        computer_deck.pop()
    elif card_effects[player_card] == 'blow' and card_effects[computer_card] == 'dig':
        print("You lose!")
        player_deck.pop()
    elif card_effects[player_card] == 'grow' and card_effects[computer_card] == 'soak':
        print("You win!")
        computer_deck.pop()
    elif card_effects[player_card] == 'soak' and card_effects[computer_card] == 'grow':
        print("You lose!")
        player_deck.pop()
    else:
        print("Invalid card combination.")


player_card = player_deck[turn-1]
computer_card = computer_deck[turn-1]
while len(player_deck) > 0 and len(computer_deck) > 0:
    print(f"Turn {turn}")
    player_move = get_player_move()
    if player_move == '1':
        compare_cards(player_card, computer_card)
    elif player_move == '2':
        draw_card(player_deck)
        player_card = player_deck[turn-1]
    draw_card(computer_deck)
    computer_card = computer_deck[turn-1]
    turn += 1

print("The game is over!")
if len(player_deck) == 0:
    print("You ran out of cards!")
if len(computer_deck) == 0:
    print("The computer ran out of cards!")
