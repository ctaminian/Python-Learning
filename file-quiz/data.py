# Write a Python script that does the following:
# Reads a file called data.txt and prints its contents line by line, ensuring that the file is properly closed after reading.
# Extracts all unique words (case-insensitive) from the file and stores them in a set.
# Sorts the unique words in reverse alphabetical order and writes them into a new file called output.txt, each word on a new line.
# The program should handle the following exceptions:
# The file data.txt does not exist.
# There is an issue writing to output.txt.
# Constraints:
# Do not use external libraries (only built-in Python modules).
# Make sure your code follows best practices for file handling, exception handling, and efficiency.
# The script should not crash under any circumstances.

try:
    with open("data.txt", "r") as my_file:
        unique_words = set()
        
        # Read file and process words
        for line in my_file:
            print(line.strip())
            for word in line.split():
                unique_words.add(word.lower())

except FileNotFoundError:
    print("File data.txt does not exist.")
else:
    # Sorting after reading is successful
    sorted_words = sorted(unique_words, reverse=True)

    try:
        with open("output.txt", "w") as output_file:
            output_file.write("\n".join(sorted_words) + "\n")
    except IOError:
        print("There was an issue writing to output.txt.")