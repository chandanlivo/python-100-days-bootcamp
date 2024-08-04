#choosing a random number between 1 and 100
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's guess against actual answer 
def check_answer(guess, answer, turns):
    '''Checks answer against guess and returns the number of turns remaining'''
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it!!..The answer was {answer}")

#make a function to set the difficulty level
def set_difficulty():
    level = input("Choose the difficulty level 'easy' or 'hard' ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the number guessing game")
    print("I'm thinking between  1 and 100 ")

    answer = randint(1, 100)
    turns = set_difficulty()

    #repeat the guessing functionality if they get it wrong 
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        #let the user guess the number 
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you LOSE.....")
            return
        elif guess != answer:
            print("Guess again")
game()




