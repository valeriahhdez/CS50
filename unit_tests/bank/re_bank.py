def main():
    """ Prompts the user for a greeting and prints the amount of money the client receives"""
    user_greeting = input("Greeting: ")
    amount = value(user_greeting)
    print(f'${amount}')


def value(greeting: str) -> int:
    """
    Value takes a greeting from the user and returns a value of money
    Args:
    - greeting: the greeting of the bank
    Returns:
    - amount of money the user receives
    """
    greeting = greeting.lower().strip()

    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()