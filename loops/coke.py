""" 
This codes simulates a selling machine that dispatches cokes. 
The user can only input coins of 25, 10, and 5 cents. 

The program prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, 
the program outputs how many cents in change the user is owed.
"""


consumer_input= 0

cost= 50

def main():
    amount_due(consumer_input, cost)

def amount_due(x, y):
    
    while x < y:
        print("Amount Due: ",y-x)
        x += int(input("Insert Coin: "))
    else: 
        change_owed = x - y
        print("Change Owed: ", change_owed)


main()
