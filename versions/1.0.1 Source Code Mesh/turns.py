# This python script is used to define turns, it will copy paste the last card from terminal to terminal

from game import cards, player_deck, computer_deck, card_effects, table, cards_used_by_myself, cards_used_by_rival

# Define turn


def turn():
    """Define turn."""
    turn = 1
    for i in range(1):
        print(f"Turn {turn}")
        turn += 1
    return turn


def card():
    """Define card."""
    card = 1
    for i in range(1):
        print(f"Turn {turn}")
        turn += 1
    return turn

# Print cards in turn 1


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


# Print card in turn 2 and previous cards in turn 1


def cards_in_turn_2():
    """Print cards in turn 2."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        table()

# Print card in turn 3 and previous cards in turn 2 and turn 1


def cards_in_turn_3():
    """Print cards in turn 3."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        table()

# Print card in turn 4 and previous cards in turn 3, turn 2 and turn 1


def cards_in_turn_4():
    """Print cards in turn 4."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        table()

# Print card in turn 5 and previous cards in turn 4, turn 3, turn 2 and turn 1


def cards_in_turn_5():
    """Print cards in turn 5."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        print(f"Your previous card: {player_deck[turn-5]}")
        print(f"Computer's previous card: {computer_deck[turn-5]}")
        table()

# Print card in turn 6 and previous cards in turn 5, turn 4, turn 3, turn 2 and turn 1


def cards_in_turn_6():
    """Print cards in turn 6."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        print(f"Your previous card: {player_deck[turn-5]}")
        print(f"Computer's previous card: {computer_deck[turn-5]}")
        print(f"Your previous card: {player_deck[turn-6]}")
        print(f"Computer's previous card: {computer_deck[turn-6]}")
        table()

# Print card in turn 7 and previous cards in turn 6, turn 5, turn 4, turn 3, turn 2 and turn 1


def cards_in_turn_7():
    """Print cards in turn 7."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        print(f"Your previous card: {player_deck[turn-5]}")
        print(f"Computer's previous card: {computer_deck[turn-5]}")
        print(f"Your previous card: {player_deck[turn-6]}")
        print(f"Computer's previous card: {computer_deck[turn-6]}")
        print(f"Your previous card: {player_deck[turn-7]}")
        print(f"Computer's previous card: {computer_deck[turn-7]}")
        table()

# Print card in turn 8 and previous cards in turn 7, turn 6, turn 5, turn 4, turn 3, turn 2 and turn 1


def cards_in_turn_8():
    """Print cards in turn 8."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        print(f"Your previous card: {player_deck[turn-5]}")
        print(f"Computer's previous card: {computer_deck[turn-5]}")
        print(f"Your previous card: {player_deck[turn-6]}")
        print(f"Computer's previous card: {computer_deck[turn-6]}")
        print(f"Your previous card: {player_deck[turn-7]}")
        print(f"Computer's previous card: {computer_deck[turn-7]}")
        print(f"Your previous card: {player_deck[turn-8]}")
        print(f"Computer's previous card: {computer_deck[turn-8]}")
        table()

# Print card in turn 9 and previous cards in turn 8, turn 7, turn 6, turn 5, turn 4, turn 3, turn 2 and turn 1


def cards_in_turn_8():
    """Print cards in turn 8."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        print(f"Your previous card: {player_deck[turn-5]}")
        print(f"Computer's previous card: {computer_deck[turn-5]}")
        print(f"Your previous card: {player_deck[turn-6]}")
        print(f"Computer's previous card: {computer_deck[turn-6]}")
        print(f"Your previous card: {player_deck[turn-7]}")
        print(f"Computer's previous card: {computer_deck[turn-7]}")
        print(f"Your previous card: {player_deck[turn-8]}")
        print(f"Computer's previous card: {computer_deck[turn-8]}")
        table()

# Print card in turn 10 and previous cards in turn 9, turn 8, turn 7, turn 6, turn 5, turn 4, turn 3, turn 2 and turn 1


def cards_in_turn_10():
    """Print cards in turn 10."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        print(f"Your previous card: {player_deck[turn-5]}")
        print(f"Computer's previous card: {computer_deck[turn-5]}")
        print(f"Your previous card: {player_deck[turn-6]}")
        print(f"Computer's previous card: {computer_deck[turn-6]}")
        print(f"Your previous card: {player_deck[turn-7]}")
        print(f"Computer's previous card: {computer_deck[turn-7]}")
        print(f"Your previous card: {player_deck[turn-8]}")
        print(f"Computer's previous card: {computer_deck[turn-8]}")
        print(f"Your previous card: {player_deck[turn-9]}")
        print(f"Computer's previous card: {computer_deck[turn-9]}")
        table()

# Print card in turn 11 and previous cards in turn 10, turn 9, turn 8, turn 7, turn 6, turn 5, turn 4, turn 3, turn 2 and turn 1


def cards_in_turn_11():
    """Print cards in turn 11."""
    for i in range(1):
        print(f"Your card: {player_deck[turn-1]}")
        print(f"Computer's card: {computer_deck[turn-1]}")
        print(f"Your previous card: {player_deck[turn-2]}")
        print(f"Computer's previous card: {computer_deck[turn-2]}")
        print(f"Your previous card: {player_deck[turn-3]}")
        print(f"Computer's previous card: {computer_deck[turn-3]}")
        print(f"Your previous card: {player_deck[turn-4]}")
        print(f"Computer's previous card: {computer_deck[turn-4]}")
        print(f"Your previous card: {player_deck[turn-5]}")
        print(f"Computer's previous card: {computer_deck[turn-5]}")
        print(f"Your previous card: {player_deck[turn-6]}")
        print(f"Computer's previous card: {computer_deck[turn-6]}")
        print(f"Your previous card: {player_deck[turn-7]}")
        print(f"Computer's previous card: {computer_deck[turn-7]}")
        print(f"Your previous card: {player_deck[turn-8]}")
        print(f"Computer's previous card: {computer_deck[turn-8]}")
        print(f"Your previous card: {player_deck[turn-9]}")
        print(f"Computer's previous card: {computer_deck[turn-9]}")
        print(f"Your previous card: {player_deck[turn-10]}")
        print(f"Computer's previous card: {computer_deck[turn-10]}")
        table()
