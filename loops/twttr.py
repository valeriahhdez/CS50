
input_str = (input("Input: "))
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def main():
    rmv_vowels(input_str)

def rmv_vowels(c):
    no_vowels =''.join([l for l in c if l not in vowels])
    print(no_vowels)

main()

             