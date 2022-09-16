import json
import requests
import sys

# Verifies and gets value from command line
if len(sys.argv) == 2:
    try:
        coins = float(sys.argv[1])
    except:
        sys.exit('Command-line argument is not a number')
else:
    sys.exit('Missing command-line argument')

# Gets the current value of a Bitcoin as a float
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = (o['bpi']['USD']['rate_float'])
except requests.RequestException:
    sys.exit("RequestException")

# Calculate the cost based on input and current price
amount = coins * rate

print(f"${amount:,.4f}")

