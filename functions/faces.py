def main():
    input_str = input("")
    emoji_str = convert(input_str)
    print(emoji_str)

def convert(s):
    h = "Hello 🙂"
    g = "Goodbye 🙁"
    if "Hello :)" == s:
        return h
    elif "Goodbye :(" == s:
        return g
    elif (":)" and ":(") in s: 
        return h + " " + g
    else: 
        return s
    
main()