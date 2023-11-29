import requests
import sys
import json
import decimal


# Deskcoin API URL
api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def is_float(string):
    """
    Checks if input can't be converted to float
    args: an input string
    returns: False if string can be converted to float, True if the string can't be converted to float
    """
    try:
        float(string)
        return False
    except ValueError:
        return True

# Check if user entered a digit
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif is_float(sys.argv[1]):
    sys.exit("Command-line argument is not a number")
else:
#     # Store the number of bitcoins in variable
    n_bitcoins = float(sys.argv[1])
#     # Make a Get request and store the JSON data in variable
    response = requests.get(api_url).json()
#     # Extract USD rate per bitcoin and store it in variable
    bitcoin_rate = float(response['bpi']['USD']['rate_float'])
#     # Obtain the total price of bitcoins
    price_bitcoins = n_bitcoins * bitcoin_rate
#     # format the price to four decimal places
    four_d_price = float("{:.4f}".format(price_bitcoins))
#     # Separate thousand with a comma and print price
    four_d_price = f'{four_d_price:,}'

print('$' + four_d_price)

