import re

def main():
    try:
        print(convert(input("Hours: ")))

    except ValueError as e:
        print(e)

def convert(s):
    match = re.search(r"^([0-9]|1[0-2]):?(0[0-9]|[1-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?(0[0-9]|[1-5][0-9])? (AM|PM)$", s)

    if match:
        start_hours = int(match.group(1))
        start_minutes = match.group(2) or "00"
        end_hours = int(match.group(4))
        end_minutes = match.group(5) or "00"

        start_period = match.group(3)
        end_period = match.group(6)

        if start_period == "PM" and start_hours != 12:
            start_hours += 12
        elif start_period == "AM" and start_hours == 12:
            start_hours = 0
        
        if end_period == "PM" and end_hours != 12:
            end_hours += 12
        elif end_period == "AM" and end_hours == 12:
            end_hours = 0

        return f"{start_hours:02}:{start_minutes} to {end_hours:02}:{end_minutes}"

    else:
        raise ValueError("Invalid input format")

if __name__ == "__main__":
    main()