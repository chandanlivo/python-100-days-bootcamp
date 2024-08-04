import random

def deal_card():
    '''returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Take the list of cards and  return the score calculated from the cards'''
    if sum == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "LOSE, computer has a blackjack"
    elif user_score == 0:
        return "WIN with a blackjack"
    elif user_score > 21:
        return "You went over, you LOSE"
    elif computer_score > 21:
        return "Opponent went over, you WIN"
    elif user_score > computer_score:
        return "you WIN"
    else:
        return "yoou LOSE"
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    # new_card = deal_card()
    # user_cards.append(new_card) SAME AS BELOW LINE
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
while not is_game_over:
# call the calculate_score . if the computer or user has a blackjack(0) , or if the user_score is over 21 then the game ends
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score = {user_score}")
    print(f"Computer's first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, 'n' to pass ")
        if user_should_deal == 'y':
            user_cards.append(deal_card)
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card)
    computer_score = calculate_score(computer_cards)

print(f"Your final hand is {user_cards} and your final score is {user_score}")
print(f"Computer's final hand is {computer_cards} and your final score is {computer_score}")
print(compare(user_score, computer_score))

