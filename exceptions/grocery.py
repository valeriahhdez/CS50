grocery_list = []
while True:

    try:
         
        grocery_item = input("")
        grocery_list.append(grocery_item)
        
           
    except EOFError:
        exit()
        ... 

    print(grocery_list)