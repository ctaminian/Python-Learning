from datetime import date
import sys
import inflect

def main():
    
    p = inflect.engine()
    birthday = input("Enter your date of birth: ").strip().split("-")

    try:
        year, month, day = map(int, birthday)
        birthdate = date(year, month, day)

    except (ValueError, IndexError):
        sys.exit("Invalid date format. Please use YYY-MM-DD.")

    today = date.today()

    if birthdate > today:
        sys.exit("Birthdate cannot be in the future.")

    days_lived = today - birthdate
    minutes_lived = days_lived.days * 24 * 60
    print(f"You have lived {p.number_to_words(minutes_lived, andword='')} minutes.")

if __name__ == "__main__":
    main()