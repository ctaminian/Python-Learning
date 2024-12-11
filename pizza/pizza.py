import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Usage: python pizza.py yourfile.csv")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Error: File must be a CSV.")

try:
    with open(sys.argv[1],"r") as csvfile:
        filereader = csv.reader(csvfile, delimiter=",")
        print(tabulate(filereader,headers="firstrow",tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")