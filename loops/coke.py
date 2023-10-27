""" 
This codes simulates a selling machine that dispatches cokes. 
The user can only input coins of 25, 10, and 5 cents. 

The program prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, 
the program outputs how many cents in change the user is owed.
"""

print("Amount Due: 50")
consumer_input = int(input("Insert Coin: "))

amount_due = 50

while consumer_input != amount_due:
    x = amount_due - consumer_input
    print("Amount Due: "+ x)
    n = int(input("Insert Coin: "))
