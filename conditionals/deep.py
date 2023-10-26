"""
This program returns 'Yes' whenever the user answers 42 either with number or letters. 
It is case- and space-insensitive. It demonstrates the use of the match case statement
"""

# Prompt the user to answer the question
grt_q = input("What is the answer to the great question of life, the universe, and everything? ")

# Remove all whitespaces and dashes from input
def new_word(nswr):
    wrd = nswr.replace(" ", "").replace("-", "").lower()
    return wrd

# Store the answer in a new variable
clean_wrd = new_word(grt_q)
#print(clean_wrd)

# Check answer, if it's 42 or forty two (case- and space-sensitive), print 'Yes'
# Otherwise, print 'No'
match clean_wrd:
    case "fortytwo" | "42":
        print("Yes!")
    case _:
        print("No")