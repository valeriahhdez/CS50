import sys
import csv
from tabulate import tabulate

def main():
    """
    Calls is_csv_file, if Tru, reads CSV file and 
    creates an ASCII table with the data inside of it
    Args: 
      - None
    Returns: 
      - Nothing
    """
    if is_csv_file():
        menu_items = []
        header_dict = []
        try: 
            with open (sys.argv[1]) as csv_file:
                reader = csv.reader(csv_file)
                header = next(reader)
                header_dict = header
                for line in csv_file:
                    name, small, large = line.rstrip().split(',')
                    menu_items.append([name, small, large])
            print(tabulate(menu_items, header_dict, tablefmt = "grid"))
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

def is_csv_file():
    """
    Validates if the user input contains a CSV file
    Args: 
    - command_line_input: list of command-line args entered by the user
    Returns: 
    - True if a CSV file are contained in command-line_input
    - sys.exit() if it does not contain a CSV file or more than 2 args are entered
    """
    if len(sys.argv) == 2:
        return True
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if '.csv'not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()