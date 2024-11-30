def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or not s[0:2].isalpha():
        return False

    if not (2 <= len(s) <= 6):
        return False

    number_started = False
    for char in s:
        if char.isdigit() and not number_started:
            number_started = True
            if char == '0':
                return False
        elif number_started:
            return False

    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()