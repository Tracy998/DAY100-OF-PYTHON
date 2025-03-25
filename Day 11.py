import random
def deal_card():
    """Returns a random card from a standard deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =random.choice(cards)  # Returns one card instead of a list
    return card



def calculate_score(cards):
    """Calculates the sum of the cards and checks for blackjack or bust."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert Ace to 1 if necessary

    return sum(cards)


def compare(u_score, c_score):
    """Compares user and computer scores to determine the winner."""
    if u_score == c_score:
        return "It's a Draw!"
    elif c_score == 0:
        return "Lose, the opponent has blackjack!"
    elif u_score == 0:
        return "Win with a blackjack!"
    elif u_score > 21:
        return "You lose!"
    elif c_score > 21:
        return "The opponent went over, you win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    # Deal two cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if continue_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer draws cards until score is 17 or more
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))  # Call the function without `print()`


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)  # Clears the screen for a fresh start
    play_game()














