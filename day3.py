print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')

print("Welcome to treasure island..")
print("Your mission is to find the treasure..")
choice1 = input("you are at the cross road, would you like to take 'left' or 'right' ").lower()
if choice1 == 'left':
    choice2 = input("There is lake, would you like to 'swim' or 'wait' for boat to reach the island ").lower()
    if choice2 == 'wait':
        choice3 = input("There are three doors 'blue', 'yellow' and 'red', which one you would like to choose ").lower()
        if choice3 == 'blue':
            print("You fell into the well and you lost the game")
        elif choice3 == 'yellow':
            print("You found the treasure.....!")
        elif choice3 == 'red':
            print("You fell into the fire, you lost the game")
        else:
            print("You have choosen that does not exist")
    else:
        print("The crocodile inside the lake harmed you and you lost the game")
else:
    print("You fell into a trap and you lost the game")