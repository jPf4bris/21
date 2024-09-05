import random

cards = ["11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]

def draw_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(int(card) for card in hand)
    return score

def user_turn(user_cards):
    while True:
        choice = input("Do you want to take another card? Type 'yes' or 'no': ")
        if choice.lower() == 'yes':
            new_card = draw_card()
            if new_card == "11":
                ace_choice = input("You drew an Ace! Do you want to count it as 1 or 11? Type '1' or '11': ")
                if ace_choice == '1':
                    new_card = "1"
            user_cards.append(new_card)
            user_score = calculate_score(user_cards)
            print(f"Your cards are now: {user_cards} and your score is: {user_score}")
            if user_score > 21:
                break
        elif choice.lower() == 'no':
            break
    return user_cards

def computer_turn(computer_cards):
    while calculate_score(computer_cards) < 17:
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)
        if computer_score > 21:
            print("You win! Computer scored more than 21!")
            break
    return computer_cards

def print_final_scores(user_cards, computer_cards):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final score is: {user_score}")
    print(f"Computer's final score is: {computer_score}")
    if user_score <= 21 and computer_score <= 21:
        if user_score > computer_score:
            print("You win!")
        elif user_score < computer_score:
            print("You lose!")
        else:
            print("It's a tie!")
    elif user_score > 21:
        print("You went over 21! You lose!")
    elif computer_score > 21:
        print("Computer went over 21! You win!")

def play_blackjack():
    print("Welcome to the BlackJack game.\n")

    user_cards = [draw_card(), draw_card()]
    computer_cards = [draw_card(), draw_card()]

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards are: {user_cards}")
    print(f"Computer's cards are: {computer_cards}")

    if user_score == 21:
        print(f"You win scoring {user_score}!")
    elif computer_score == 21:
        print(f"You lose scoring {user_score}\nComputer scored {computer_score}!")

    user_cards = user_turn(user_cards)
    computer_cards = computer_turn(computer_cards)
    print_final_scores(user_cards, computer_cards)

play_blackjack()

   

