""" This code prompts the user to enter an item

Adds the item to a list

When user types crtl + d, it counts the number of times 
each item was entered stores the information in a dictionary

Finally, it prints the contents of dictionary"""

grocery_list = []
grocery_dict = {}
while True:
    try: 
        grocery_item = input("")
        grocery_list.append(grocery_item)
              
    except EOFError:
        
        for item in range(len(grocery_list)):
            grocery_dict[grocery_list[item]] = grocery_list.count(grocery_list[item])


        for key, value in grocery_dict.items():
            print(value, key.upper())
        
        exit()
        ... 