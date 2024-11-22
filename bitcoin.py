import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:    
    bitcoin_amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
    bitcoin_data = response.json()

    bitcoin_price = float(bitcoin_data["bpi"]["USD"]["rate_float"])
    total_price = bitcoin_price * bitcoin_amount
    print(f"The total cost to buy {bitcoin_amount} Bitcoin(s), is ${total_price:,.4f}.")

except requests.RequestException as e:
    sys.exit(f"HTTP request fialed: {e}")