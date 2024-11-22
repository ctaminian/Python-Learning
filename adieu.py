import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Enter a name (ctrl + Z to finish): ").strip()
        if name:
            names.append(name)
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(names)}")
        break