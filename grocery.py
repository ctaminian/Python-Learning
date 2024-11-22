list = {}

while True:
    try:
        item = input("Item: ")
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
    except EOFError:
        for l in list:
            print(f"{list[l]} {l.upper()}")
        break