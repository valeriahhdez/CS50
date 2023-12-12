import emoji

def main():
    """
    Takes a string and converts it to an emoji
    ARGS:
    - str_emoji: a string entered by the user
    CHANGES:
    - str_emoji -> output_emoji
    RETURNS:
    - output_emoji
    """

    str_emoji = input("Input: ")
    output_emoji = emoji.emojize(str_emoji, language='alias')
    print('Output: ' + output_emoji)

if __name__ == "__main__":
    main()