'''
This program prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
It ignores whitespaces and is case-insensitive
'''

# Prompt the user to greet
grtng = input("Greeting: ")

# Make the greeting lowercase
def lwr_grtng(nswr):
    wrd = nswr.lower()
    return wrd

# Store lowercase greeting in variable
greeting = lwr_grtng(grtng)

# Check if the greeting contains "Hello" or if it starts with "h"
if "hello" in greeting:
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")