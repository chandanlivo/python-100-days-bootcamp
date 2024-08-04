from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    '''format the account data into printable format''' 
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    '''use if statement to check if user is correct'''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    
# import logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
clear = lambda: os.system('cls')

# make the game repeatable 
while game_should_continue:
    # generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    # ask user for a guess
    guess = input("Who has the more followers, type 'A' or 'B':").lower()

    # check if user is correct
    ## get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen between the rounds
    clear()
    print(logo)
    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right, your current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong, Final Score:{score}")
# score keeping





# making account at position B become the next account at position B


