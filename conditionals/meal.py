'''
This program prompts the user for a time 
and outputs whether it’s breakfast time, lunch time, or dinner time. 
If it’s not time for a meal, it doesn't output anything. 
It assumes that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
Each meal’s time range is inclusive. 
'''

def main():
    # Prompt the user to enter a time
    time = convert(input("What is it? "))   
    # check if it's time to eat and what to eat
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# Function to convert 24 h time to the corresponding number of hours as a float
def convert(time):
    # Split hours and minutes from string
    time_object = time.split(":")
    # Convert numbers to integers
    h, m = int(time_object[0]), int(time_object[1])
    # Calculate minutes in decimal values
    dec_m = m/60
    # Add number of hours and decimal minutes to get the total time
    t_time = h + dec_m
    return t_time

# Run main() when meal.py is used as a script
if __name__ == "__main__":
    main()