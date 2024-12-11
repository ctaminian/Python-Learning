import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py youroldfile.csv yournewfile.csv")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Error: File must be a CSV.")

try:
    with open(sys.argv[1],"r") as oldcsvfile:
        reader = csv.DictReader(oldcsvfile)
  
        with open(sys.argv[2],"w", newline="") as newcsvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                splitname = row["name"].split(",")
                writer.writerow({
                    "first": splitname[1].strip(),
                    "last": splitname[0].strip(),
                    "house": row["house"]
                })
except FileNotFoundError:
    sys.exit("File does not exist")