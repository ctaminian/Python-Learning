my_dictionary = {
    "file1.txt": 1.0,
    "file2.txt": 0.88,
    "file3.txt": 1.5,
    "file4.txt": 2.6,
    "file5.txt": 55.5,
}

def main():
    add_file("charlie.txt", 20)
    print("Updated dictionary after adding a file:")
    print(my_dictionary)
    filtered_dict = remove_file(5)
    print("Dictionary after removing files larger than 5 MB:")
    print(filtered_dict)

def add_file(filename, size):
    if filename in my_dictionary or size <= 0:
        print("Please enter a unique name and file size must be greater than 0.0MB.")
        return
    my_dictionary[filename] = size

def remove_file(size):
    return {n:s for n, s in my_dictionary.items() if s < size}

if __name__ == "__main__":
    main()