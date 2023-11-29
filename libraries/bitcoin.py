import requests
import sys
import json



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


# The following lines of code are an imporved version of my version made by Bard

# import requests
# import sys
# import json


# # Define the Deskcoin API URL
# api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"


# def validate_input(user_input):
#     try:
#         # Convert the user input to a float to check if it's a valid number
#         float(user_input)
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         sys.exit(1)


# # Check if the user provided a single command-line argument
# if len(sys.argv) != 2:
#     print("Missing command-line argument. Please enter the number of bitcoins.")
#     sys.exit(1)

# # Validate the user-provided number of bitcoins
# user_input = sys.argv[1]
# validate_input(user_input)

# # Convert the validated input to a float
# n_bitcoins = float(user_input)

# # Make a GET request to the Deskcoin API and store the JSON response
# response = requests.get(api_url).json()

# # Extract the USD rate per bitcoin from the API response
# bitcoin_rate = float(response['bpi']['USD']['rate_float'])

# # Calculate the total price of the bitcoins
# price_bitcoins = n_bitcoins * bitcoin_rate

# # Format the price to four decimal places
# four_d_price = float("{:.4f}".format(price_bitcoins))

# # Separate thousand with a comma and print the price
# four_d_price = f'{four_d_price:,}'

# print('$' + four_d_price)