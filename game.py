import random

while True:
    try:
        max_num = int(input("Level: "))
        if max_num > 0:
            break
    except ValueError:
        continue

random_num = random.randint(1, max_num)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > random_num:
            print("Too large!")
        elif guess < random_num:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass