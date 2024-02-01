import re


def main():
    """Prompts the user to enter an IP address
    Calls validate which returns True if the IP address is valid. """
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Checks if the entered IP address has a valid format
    Args: 
    - ip: a string number entered by the user
    Returns: 
    - True if the string is a valid IP address, False if otherwise."""
    if re.findall(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', ip):
        ip_numbers = re.split(r'\.', ip)
        for number in ip_numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else: 
        return False 

if __name__ == "__main__":
    main()