import random
words_list = ['Mrabd', 'virat', 'smith']

#Randomly choose a word from words_list
choosen_word = random.choice(words_list)


lives = 6
#generating '_' for each letter in the choosen word
display = []
for letter in range(len(choosen_word)):
    display += "_"
# print(display)

#Ask the user to guess the letter and assign
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check the letter user gussed
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")