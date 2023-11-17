# Prompt the user to enter an item

# Add item to list

# When user types crtl + d, count the number of times 
# each times appears in the list and store the results in a dictionary

# print the contents of dictionary

grocery_list = []
grocery_dict = {}
while True:

    try:
         
        grocery_item = input("")
        grocery_list.append(grocery_item)
        
           
    except EOFError:
        
        for item in range(len(grocery_list)):
            grocery_dict[grocery_list[item]] = grocery_list.count(grocery_list[item])

        print(grocery_dict)
        
        exit()
        ... 