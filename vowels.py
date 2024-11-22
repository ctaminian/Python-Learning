string = "Hello World"
vowels = "aeiou"
count = 0

for letter in string.lower():
    if letter in vowels:
        count += 1

print(count)