# 1. Create a dictionary that maps numbers from 1 to 5 to their squares.
# Example Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squares = {x: x * x for x in range(1, 6)}

# 2. Create a dictionary where the keys are characters in the string 'abcde' and the values are their ASCII values.
# Example Output: {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}

ascii_values = {letter: ord(letter) for letter in "abcde"}

# 3. Given the list ['apple', 'banana', 'cherry'], create a dictionary where the keys are the fruits and the values are their lengths.
# Example Output: {'apple': 5, 'banana': 6, 'cherry': 6}

fruits = {fruit: len(fruit) for fruit in ["apple", "banana", "cherry"]}

# 4. Generate a dictionary where keys are numbers from 1 to 10, and the values are 'even' if the number is even and 'odd' otherwise.
# Example Output: {1: 'odd', 2: 'even', 3: 'odd', ..., 10: 'even'}

even_odd = {num: "even" if num % 2 == 0 else "odd" for num in range(1, 11)}

# 5. Given the nested dictionary:
# nested_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Create a dictionary where the keys are the same, but the values are doubled only if they are even numbers.
# Example Output: {'a': 1, 'b': 4, 'c': 3, 'd': 8}

nested_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
doubled_even = {item: nested_dict[item] * 2 if nested_dict[item] % 2 == 0 else nested_dict[item] for item in nested_dict}

# 6. Given two lists:
# keys = ['name', 'age', 'city']
# values = ['Alice', 30, 'New York']
# Create a dictionary that maps keys to values.
# Example Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

key_value = {key: value for key, value in zip(keys, values)}
print(key_value)

# 7. Given the dictionary:
# word_counts = {'hello': 5, 'world': 8, 'python': 3, 'comprehension': 7}
# Create a new dictionary where the keys are the same, but the values are only included if they are greater than 5.
# Example Output: {'world': 8, 'comprehension': 7}

# 8. Given a string 'aabbccdd', create a dictionary where the keys are the unique characters, and the values are the count of each character in the string.
# Example Output: {'a': 2, 'b': 2, 'c': 2, 'd': 2}

# 9. Generate a dictionary from 1 to 10 where the keys are the numbers, and the values are lists of their factors.
# Example Output: {1: [1], 2: [1, 2], 3: [1, 3], ..., 10: [1, 2, 5, 10]}