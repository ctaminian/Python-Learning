# Create a list of squares for numbers 1 to 10.
# Expected result: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = range(10)
squares = [num * num for num in nums]

# Filter even numbers from a list numbers = [5, 8, 12, 15, 18].
# Expected result: [8, 12, 18]

numbers = [5, 8, 12, 15, 18]
even_numbers = [n for n in numbers if n % 2 == 0]

# Convert a list of strings words = ["hello", "world", "python"] to uppercase.
# Expected result: ['HELLO', 'WORLD', 'PYTHON']

words = ["hello", "world", "python"]
upper_case_words = [word.upper() for word in words]

# Create a list of tuples (number, square) for numbers 1 to 5.
# Expected result: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

nums = range(1, 6)
squared_tuples = [(num, num * num) for num in nums]

# Create a list of numbers from 1 to 20 that are divisible by both 2 and 3.
# Expected result: [6, 12, 18]

nums = range(1, 21)
divisible_nums = [n for n in nums if n % 2 == 0 and n % 3 == 0]

# Flatten the list nested = [[1, 2], [3, 4], [5, 6]].
# Expected result: [1, 2, 3, 4, 5, 6]

nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]

# Given two lists, list1 = [1, 2, 3] and list2 = ['a', 'b', 'c'], create a list of dictionaries where each dictionary maps the number to the corresponding letter.
# Expected result: [{'1': 'a'}, {'2': 'b'}, {'3': 'c'}]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = [{str(x): y} for x, y in zip(list1, list2)]

# Create a new list from words = ["apple", "banana", "cherry", "date"] that includes the word and its length as tuples only if the word has more than 5 letters.
# Expected result: [('banana', 6), ('cherry', 6)]

words = ["apple", "banana", "cherry", "date"]
word_lengths = [(word, len(word)) for word in words if len(word) > 5]

# From the list numbers = [2, 3, 5, 7, 11, 13, 17], create a list of squares if the number is prime and greater than 10.
# Expected result: [121, 169, 289]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 5, 7, 11, 13, 17]
prime_squares = [num * num for num in numbers if num > 10 and is_prime(num)]