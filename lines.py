import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python lines.py filename.py")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file.")

try:
    with open(sys.argv[1],"r") as file:
        code_line_count = 0
        for line in file:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith("#"):
                code_line_count += 1
        print(f"Lines of code: {code_line_count}")

except FileNotFoundError:
    sys.exit("File does not exist.")