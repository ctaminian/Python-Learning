def main():
    inventory = {
        "apple": {"price": 1.0, "stock": 10},
        "banana": {"price": 0.5, "stock": 20},
        "orange": {"price": 0.8, "stock": 15}
    }

    try:
        operation = input("Operation (lookup/buy/add): ").strip().lower()
        item = get_item(inventory)

        if operation == "lookup":
            print(f"Price: ${inventory[item]['price']}")
            print(f"Stock: {inventory[item]['stock']}")

        elif operation == "buy":
            quantity = get_quantity()
            if quantity > inventory[item]['stock']:
                print("Not enough stock available!")
            else:
                total_cost = inventory[item]['price'] * quantity
                inventory[item]['stock'] -= quantity
                print(f"You bought {quantity} {item}(s) for ${total_cost:.2f}.")

        elif operation == "add":
            quantity = get_quantity()
            inventory[item]["stock"] += quantity
            print(f"Added {quantity} to {item}'s stock. (New stock: {inventory[item]['stock']})")

        else:
            print("Not a valid operation.")

    except KeyError:
        print("Item not found in inventory.")
    except ValueError:
        print("Invalid input.")
    finally:
        print("Operation complete")


def get_quantity():
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Please enter a positive number.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid number.")


def get_item(inventory):
    while True:
        item = input("Item name: ").strip().lower()
        if item in inventory:
            return item
        print("Item not found in inventory. Please try again.")