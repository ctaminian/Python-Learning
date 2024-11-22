import random

def main():

    current_level = get_level()

    score = 0

    for _ in range(10):

        x = generate_integer(current_level)
        y = generate_integer(current_level)

        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            attempts += 1
        if attempts == 3:
            print(f"The correct answer is {x + y}")
    print(f"Score: {score}/10")
        
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError("Level must be 1, 2, or 3")
    lower = 10**(level-1)
    upper = 10**level - 1
    return random.randint(lower, upper)

if __name__ == "__main__":
    main()