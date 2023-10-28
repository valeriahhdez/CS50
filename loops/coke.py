"""
This codes simulates a selling machine that dispatches cokes.
The user can only input coins of 25, 10, and 5 cents.

The program prompts the user to insert a coin, one at a time,
each time informing the user of the amount due.
Once the user has inputted at least 50 cents,
the program outputs how many cents in change the user is owed.
"""

# Initialize the input of coins
consumer_input= 0
# Cost value
cost= 50

def main():
    # Call amount_due function and pass inputs
    amount_due(consumer_input, cost)

def amount_due(x, y):
    # While the value of coins is less than the cost:
    while x < y:
        # Print the amount due by customer
        print("Amount Due: ",y-x)
        # Prompt the user to insert coins
        x += int(input("Insert Coin: "))
    else:
        # Caclulate how much the machines owes to the customer
        change_owed = x - y
        print("Change Owed: ", change_owed)


main()
