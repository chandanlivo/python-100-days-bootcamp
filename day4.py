import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# 
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, Scissors]
user_choice = int(input("What do you choose? rock 0, paper 1, scissor 2\n"))
if user_choice >=3 or user_choice < 0:
    print("You entered an invalid input, you lose...!")

else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer choice")
    print(game_images[computer_choice])


    if user_choice == 2 and computer_choice == 0:
        print("You lose...")
    elif user_choice == 0 and computer_choice == 2:
        print("You win...")
    elif user_choice < computer_choice:
        print("You lose..")
    elif user_choice > computer_choice:
        print("You win..")
    elif user_choice == computer_choice:
        print("Its a draw..")