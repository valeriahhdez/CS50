def main():
    """
    Takes user input, passes it to the shorten function, and prints the result.
    Args:
        None
    Returns:
        None
    Example Usage:
        Input: "Hello World"
        shorten("Hello World") -> "Hll Wrld"
    """
    input_str = (input("Input: "))
    print(shorten(input_str))

def shorten(word):
    """
    Removes all vowels from a given string.
    Args:
        input_str: The input string from the user.
    Returns:
        no_vowels_str: The modified string with all the vowels removed.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    no_vowels_str =''.join([l for l in word if l not in vowels])
    return no_vowels_str



if __name__ == "__main__":
    main()
