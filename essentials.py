# Write a map function to square all numbers in a list
numbers = [2, 4, 6, 8]

def square(n):
    return n * n

squared_numbers = map(square, numbers)
print(*squared_numbers)

# Write a map function to capitalize strings in a list
fruits = ["apple", "banana", "cherry"]

def capitalize(w):
    return w.upper()

capital_words = map(capitalize, fruits)
print(*capital_words)

# Write a filter function to find all even numbers in the list [1, 2, 3, 4, 5, 6].
nums = [1, 2, 3, 4, 5, 6]

def find_even_nums(n):
    return n % 2 == 0

even_numbers = filter(find_even_nums, nums)
print(*even_numbers)

# Given the list of names ["Anna", "Bob", "Alice", "Eve", "Charlie"], use filter to extract all names that start with the letter "A".
names = ["Anna", "Bob", "Alice", "Eve", "Charlie"]

def names_with_a(s):
    return s.startswith("A")

names_that_start_with_a = filter(names_with_a, names)
print(*names_that_start_with_a)

# Write a loop using enumerate to print the index and value of each item in the list ["red", "green", "blue"].
colors = ["red", "green", "blue"]

for i, color in enumerate(colors, 1):
    print(i, color)

# Given the list [10, 20, 30, 40], use enumerate to create a new list of tuples where each tuple contains (index, value * index).
nums = [10, 20, 30, 40]
result = []

for i, num in enumerate(nums, 1):
    result.append((i, num * i))

print(result)

# Write a single line of code using list comprehension and unpacking to create a list of strings in the format:
# Item <index>: <name> costs $<price>

data = [(1, "apple", 3.5), (2, "banana", 2.8), (3, "cherry", 4.2)]

unpacked_list = [f"Item {index}: {name} costs ${price}" for index, name, price in data]
print(unpacked_list)

#Write a single line of code using list comprehension and unpacking to create a list of strings in the format:
#<item_name>: <quantity> items with dimensions <length>x<width>x<height>

items = [("Box", 3, (10, 5, 8)), ("Crate", 2, (15, 10, 12)), ("Package", 5, (8, 4, 6))]

unpacked_items = [f"{item}: {quantity} items with dimensions {length}x{width}x{height}" for item, quantity, (length, width, height) in items]
print(unpacked_items)

# Write a single line of code to print all the keys in the dictionary.
fruit_prices = {"apple": 1.2, "banana": 0.8, "cherry": 2.5}
print(*fruit_prices.keys())

# Write a single line of code to create a list of all the values.
list_of_fruit_values = list(fruit_prices.values())
print(list_of_fruit_values)
num1, num2, num3 = list_of_fruit_values
print(num1, num2, num3)

# Write a loop using .items() to print each key-value pair in the format:
# apple costs $1.2
for name, cost in fruit_prices.items():
    print(f"{name} costs ${cost}")

# Unpack the dictionary into three variables, length, width, and height, and print their values.
dimensions = {"length": 10, "width": 5, "height": 8}
length, width, height = dimensions.values()
print(length, width, height)

# Write a loop using .items() to print the following:
# apple: 10
# banana: 8
# carrot: 15
# broccoli: 5
inventory = {
    "fruits": {"apple": 10, "banana": 8},
    "vegetables": {"carrot": 15, "broccoli": 5}
}

for item in inventory.values():
    for frt, price in item.items():
        print(f"{frt}: {price}")

# Write code to create a new dictionary where each key is a subject ("math", "science") and the value is a list of all students' scores for that subject.
# {
#     "math": [90, 78, 92],
#     "science": [85, 88, 79]
# }

students = {
    "Alice": {"math": 90, "science": 85},
    "Bob": {"math": 78, "science": 88},
    "Charlie": {"math": 92, "science": 79},
}

new_dictionary = {}

for courses in students.values():
    for subject, score in courses.items():
        if subject not in new_dictionary:
            new_dictionary[subject] = []
        new_dictionary[subject].append(score)

print(new_dictionary)