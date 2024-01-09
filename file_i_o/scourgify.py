import sys
import csv

def main():
    """
    Calls is_valid_length
    If true, it creates a new csv file with first, last, and house rows
    """
    if is_valid_length(sys.argv):
        try:
            students = []
            with open (sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Split the first name, last name, and house
                    students.append({"first": row['name'].split(', ')[1], "last": row['name'].split(',')[0], "house": row['house']})
            with open(sys.argv[2], "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ['first', 'last', 'house'])
                writer.writeheader()
                for student in students:
                    writer.writerow(student)
        except:
            sys.exit(f"Could not read {sys.argv[1]}")
    
def is_valid_length(command_line_input):
    """
    Validates that user input contains a CSV file to read 
    and a CSV output file
    Args: 
    - command_line_input: list of command-line args entered by the user
    Return: 
    - True if both CSV file are contained in command-line_input
    - False if otherwise
    """
    if len(command_line_input) == 3:
        return True
    elif len(command_line_input) < 3:
        sys.exit("Too few command-line arguments")
    elif len(command_line_input) > 3:
        sys.exit("Too many command-line arguments")
 

if __name__ == "__main__":
    main()