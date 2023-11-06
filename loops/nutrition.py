fruit_item = input("Item: ")
# Make the string case insensitive for convenience
case_insensitive_item = fruit_item.lower()

fruit_dict = {
    "apple": 130,
    "sweet cherries": 100,
    "pear": 100,
    "avocado": 50,
    "cantaloupe": 50,
    "honeydew melon": 50,
    "pineapple": 50,
    "strawberries": 50,
    "tangerine": 50,
    "banana": 110,
    "grapefruit": 60,
    "nectarine": 60,
    "peach": 60,
    "plums": 70,
    "grapes": 90,
    "kiwifruit": 90,
    "orange": 80,
    "watermelon": 80,
    "lemon": 15,
    "lime": 20 
    }

# If fruit_item is in fruit_dict print its calorie value
if case_insensitive_item in fruit_dict: 
    
    print(f"Calories: {fruit_dict[case_insensitive_item]}")
else: 
    print("")