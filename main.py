import random
from art import logo,outcomes

score_board = {
    "dealer": 0,
    "player": 0
}

def get_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1  # Convert an Ace from 11 to 1 if needed
        score = sum(hand)
    return score

def winning_conditions(score_dealer, score_player):
    if score_player > 21:
        print(outcomes[1])
        return "dealer"
    if score_dealer > 21 or score_player > score_dealer:
        print(outcomes[0])
        return "player"
    if score_dealer > score_player:
        print(outcomes[1])
        return "dealer"
    print(outcomes[2])
    return "draw"

def display_score_board():
    print("\nScoreboard:")
    for key, value in score_board.items():
        print(f"{key.capitalize()} Wins: {value}")
    print()

def display_decks(dealer_deck, player_deck, reveal_dealer=False):
    print("\nDealer's Hand:")
    if reveal_dealer:
        for card in dealer_deck:
            print(card, end=", ")
    else:
        print("_, ", end="")
        for card in dealer_deck[1:]:
            print(card, end=", ")
    print()  # Move to the next line

    print("\nYour Hand:")
    for card in player_deck:
        print(card, end=", ")
    print("\n")  # Move to the next line

def simple_black_jack():
    dealer_hand = [get_random_card(), get_random_card()]
    player_hand = [get_random_card(), get_random_card()]

    dealer_value = calculate_score(dealer_hand)
    player_value = calculate_score(player_hand)

    while True:
        display_decks(dealer_hand, player_hand)
        user_choice = input("Type 'h' to hit, type 's' to stand: ").lower()

        if user_choice == "h":
            player_hand.append(get_random_card())
            player_value = calculate_score(player_hand)

            if player_value > 21:
                print("Bust! You went over 21.")
                break
        elif user_choice == "s":
            break

    # Dealer's turn (hits until reaching at least 17)
    while dealer_value < 17:
        dealer_hand.append(get_random_card())
        dealer_value = calculate_score(dealer_hand)

    display_decks(dealer_hand, player_hand, reveal_dealer=True)

    winner = winning_conditions(dealer_value, player_value)

    if winner in score_board:
        score_board[winner] += 1

def main():
    print(logo)
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        display_score_board()
        simple_black_jack()

if __name__ == "__main__":
    main()
