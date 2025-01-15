# Question: Given the list numbers = [1, 2, 3, 4], write a single line of code using map() to convert each number to its square. Store the results in a new list called squares.
# Example answer format:
# numbers = [1, 2, 3, 4]
# squares = list(map( ... ))
# print(squares)  # Expected output: [1, 4, 9, 16]

numbers = [1, 2, 3, 4]
squares = list(map(lambda num: num * num, numbers))

# Question: You have a list of integers: values = [10, 15, 20, 25, 30]. Use filter() to create a new list that only contains the numbers greater than 20.
# Example answer format:
# values = [10, 15, 20, 25, 30]
# filtered_values = list(filter( ... ))
# print(filtered_values)  # Expected output: [25, 30]

values = [10, 15, 20, 25, 30]
filtered_values = list(filter(lambda value: value > 20, values))

# Question: Using the list animals = ["cat", "dog", "rabbit"], print each animal name alongside its index in this format:
# Index: 0 - Animal: cat
# Index: 1 - Animal: dog
# Index: 2 - Animal: rabbit

#using a loop
animals = ["cat", "dog", "rabbit"]
for i, animal in enumerate(animals):
    print(f"{i} - Animal: {animal}")

#using list comprehension
animal_list = [f"{i} - Animal: {animal}" for i, animal in enumerate(animals)]

# Question: You have the dictionary:
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# Print all the keys.
# Print all the values.
# Print each key–value pair on a new line in the format: key => value.

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(*person.keys())
print(*person.values())

for item in person:
    print(f"{item} => {person[item]}")

for key, value in person.items():
    print(f"{key} => {value}")

# Question: Using the same dictionary person from the previous question:
# Create a list called keys_list that contains all the keys from person.
# Create a list called values_list that contains all the values from person.

keys_list = [key for key in person]
value_list = [value for value in person.values()]

# Question: Write a list comprehension that takes a list of integers numbers = [1, 2, 3, 4, 5, 6] and produces a new list of their cubes only if the original number is even. Store the result in even_cubes.
# Hint: The expected output for numbers = [1, 2, 3, 4, 5, 6] would be [8, 64, 216].

numbers = [1, 2, 3, 4, 5, 6]
even_cubes = [num ** 3 for num in numbers if num % 2 == 0]

# Question: Create a dictionary comprehension that maps each word in the list words = ["python", "java", "c++"] to its length. For example, "python" should map to 6. Assign the resulting dictionary to word_lengths.
# Expected output: {"python": 6, "java": 4, "c++": 3}

words = ["python", "java", "c++"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# Question: Given numbers = [0, -1, 3, 5, -2, 10], use a combination of filter() and map() to accomplish the following in a single line of code:
# Filter out the negative numbers.
# Multiply the remaining numbers by 2.
# Store the final results in a list called processed_numbers.

#using filter and map
numbers = [0, -1, 3, 5, -2, 10]
processed_numbers = list(map(lambda x: x * 2, filter(lambda n: n > 0, numbers)))

#using comprehension
processed_numbers = [num * 2 for num in numbers if num > 0]

# Question: Assume you have a list of dictionaries representing books:
# books = [
#     {"title": "Book A", "pages": 200},
#     {"title": "Book B", "pages": 150},
#     {"title": "Book C", "pages": 300},
#     {"title": "Book D", "pages": 120}
# ]
# Write a list comprehension (or filter()) to get only books that have more than 150 pages.
# For each book in the resulting list, print its title using enumerate() so that the output shows the index of each book in the filtered list along with its title.

books = [
    {"title": "Book A", "pages": 200},
    {"title": "Book B", "pages": 150},
    {"title": "Book C", "pages": 300},
    {"title": "Book D", "pages": 120}
]

longer_books = [book for book in books if book["pages"] > 150]
for i, book in enumerate(longer_books):
    print(f"{i}. {book['title']}")

# Question: Given the list letters = ["a", "b", "a", "c", "b", "a"], write a dictionary comprehension that creates a frequency dictionary—mapping each distinct letter to the number of times it appears in the list.
# Expected output (order may vary):
# {
#   "a": 3,
#   "b": 2,
#   "c": 1
# }

letters = ["a", "b", "a", "c", "b", "a"]
letter_count = {letter: letters.count(letter) for letter in set(letters)}