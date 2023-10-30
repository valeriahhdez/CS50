# To check if the plate number contains a punctuation character, import punctuation
# from string import punctuation
plate = input("Plate: ")

# def main():
#     plate = input("Plate: ")
#     # if is_valid(plate):
#     #     print("Valid")
#     # else:
#     #     print("Invalid")

# def is_valid(conditions):
#     for condition in conditions:
#         if not condition:
#             return False
#     return True


# def valid_length(x):
#     if 2 <=len(x) <=6:
#         return True

# conditions = [
    # not(any(char.isdigit() for char in inputString[0:2])),
#     2 <= len(plate) <=6,
#     not(p in my_text for p in punctuation),
#     i ,
# ]

# main()



# my_text = 'What?'

# if not(p in my_text for p in punctuation):
#     print("True")
# else:
#     print("False")

def has_numbers(inputString):
    return not(any(char.isdigit() for char in inputString[0:2]))


print(has_numbers(plate))