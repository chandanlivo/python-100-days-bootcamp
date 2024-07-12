import random

randomInteger = random.randint(1, 10)
print(randomInteger)

randomFloat = random.random() * 5 # Prints a random floating number bw 0 and 5
print(randomFloat)

loveScore = random.randint(1, 100)
print(f"Your love score is {loveScore}")


# HEADS / TAILS

randomSide = random.randint(0, 1)
if randomSide == 1:
    print('HEADS')
else:
    print('TAILS')
