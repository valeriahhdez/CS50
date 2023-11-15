menu_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Open tab to add menu items' cost
tab = 0

while True:

    try:
        # Check if case insensitive menu_item is in menu_dict 
        menu_item = input("Item: ").lower()
        menu_lower = {k.lower():v for k,v in menu_dict.items()}  
        
        if menu_item in menu_lower:
            tab = tab + menu_lower[menu_item]
            two_decimals = "%.2f" % tab
            print(f"Total: ${two_decimals}")
        
    except KeyError:
        continue    
    except EOFError:
        exit()
        ... 



