
while True:
    try:
        user_string = input("Fraction: ").split("/")
        num1 = int(user_string[0])
        num2 = int(user_string[1])
        if num1 > num2:
            continue
        percentage = round(num1 / num2 * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")