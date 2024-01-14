import sys

def main():
    """
    Calls is_python_file, if True, reads python file and 
    cunts the number of lines that contain code. It checks for 
    and excludes all whitespace lines and comment lines. 
    Args: 
      - None
    Returns: 
      - Nothing
    """
    is_python_file()
    lines_of_code = 0
    try: 
        with open (sys.argv[1]) as file:
            lines = file.readlines()
            total_lines = len(lines)
            no_code_lines = sum(line.isspace() or line.lstrip().startswith("#") for line in lines)
            lines_of_code = total_lines - no_code_lines
        print(lines_of_code)
    except FileNotFoundError:
        sys.exit("File does not exist")

def is_python_file():
    """
    Validates if the user input contains a python file
    Args: 
    - command_line_input: list of command-line args entered by the user
    Returns: 
    - sys.exit() if input does not contain a python file, the input does not contain only two args
    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    
    

if __name__ == "__main__":
    main()