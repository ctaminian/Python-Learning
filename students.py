students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

try:
    name = input("Enter a student's name: ")
    print(students[name])
except KeyError:
    print("Student not found")
except ValueError:
    print("Please enter a valid student's name")
finally:
    print("Lookup process complete")