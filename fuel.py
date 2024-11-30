def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError:
            print("Invalid input. Please enter a proper fraction in the format 'X/Y'.")
        except ZeroDivisionError:
            print("The denominator cannot be zero.")

def convert(fraction):
    try:
        parts = fraction.split("/")
        if len(parts) != 2:
            raise ValueError("Invalid fraction format.")

        x = int(parts[0])
        y = int(parts[1])

        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than the denominator.")
        
        return round(x / y * 100)
    
    except (ValueError, ZeroDivisionError) as e:
        raise e

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()