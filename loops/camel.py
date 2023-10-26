#prompt the user to enter a camel case variable and store it
camel_case = input("Camel Case: ")

## My code
snake =[]

# Check which letter in the string provided is uppercase
for i in camelCase:
  if i.isupper():
    # add and '_', make it lowercase, and append it to the empty list
    s = '_' + i.lower()
    snake.append(s)
  else:
    snake.append(i)

snake_case = ''.join(snake)
print(snake_case)



## Pythonic version
# def camel_to_snake(camel_case):
#   snake_case = ''
#   for i in camel_case:
#     if i.isupper():
#       snake_case += '_' + i.lower()
#     else:
#       snake_case += i
#   return snake_case


# snake_case = camel_to_snake(camel_case)
# print(snake_case)

 
  


