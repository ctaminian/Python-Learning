def main():
    num = get_int("What's x? ")
    print(f"x is {num}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()