try:
    num = int(input("Enter a number: "))
    print(num*num)
except ValueError:
    print("Invalid input, please enter a number")