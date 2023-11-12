def main():
    input_str = input("")
    emoji_str = convert(input_str)
    print(emoji_str)

def convert(s):
    if ":)" in s:
        return "🙂"
    elif ":(" in s:
        return "🙁"
    else: 
        return s
    
main()