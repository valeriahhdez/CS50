from tabulate import tabulate
import pandas as pd
import sys

def main():
    # prompt the user to select type of calculation
    type_of_recipe = input("What do you want to do with your ingredients?\n(1) Calculate percentages\n(2) Calculate gr\nEnter option: ")
    if type_of_recipe == "1":
        create_recipe_from_grams()
    elif "2" in type_of_recipe:
        create_recipe_from_percentage()

def create_recipe_from_grams():
    ingredients = {}
    while True:
        # Prompt the user to ingredients one at a time and their weights
        ingredient = input("Enter the name of an ingredient or 'q' to finish recipe: ")
        if ingredient.lower() == 'q':
            break
        weight = float(input(f"Enter the weight in grams for {ingredient}: "))
        ingredients[ingredient] = weight
    # Ensure flour has been entered and has a non-zero weight
    flour_weight = ingredients.get('flour')
    if flour_weight == 0:
        print("Flour weight is zero or not provided, cannot create recipe.")
        return 
    # Calculate and store percentages inside list
    recipe_data = {}
    for ingredient, weight in ingredients.items():
        percentage = calculate_percentage(weight, flour_weight)
        recipe_data[ingredient] = {
            'Weight (g)': weight,
            '% of flour weight': f"{percentage:.2f} %"
        }
        
        # Create table using the data from list
        recipe_table = pd.DataFrame.from_dict(recipe_data, orient='index')
    print(recipe_table)
    # Ask if user wants to make any changes
    make_changes = input("Would you like to change anything?\n(1) Yes\n(2) No\nEnter number: ")
    if make_changes == "1":
        print(change_recipe(ingredients, flour_weight))
    elif make_changes == "2":
        sys.exit()
    
def create_table(recipe_dict):
    table = tabulate(recipe_dict)
    return table

def change_recipe(ingredient_list, flour_weight):
    while True:
        # Prompt the user to enter the ingredient to be changed
        ingredient = input("\nEnter the ingredient you want to change or 'q' to finish recipe: ")
        if ingredient.lower() == 'q':
            break
        weight = float(input(f"Enter the new weight in grams for {ingredient}: "))
        ingredient_list[ingredient] = weight
    new_recipe_data = {}
    for ingredient, weight in ingredient_list.items():
        percentage = calculate_percentage(weight, flour_weight)
        new_recipe_data[ingredient] = {
            'Weight (g)': weight,
            '% of flour weight': f"{percentage:.2f} %"
        }
        new_recipe_table = pd.DataFrame.from_dict(new_recipe_data, orient='index')
    return new_recipe_table

def calculate_percentage(x_weight, y_weight):
    return (x_weight/y_weight) *100

def create_recipe_from_percentage():
    ingredient_dict = {
    'starter': 0,
    'starter hydration': 0,
    'white flour': 0,
    'whole wheat': 0,
    'salt': 0,
    'oil': 0
}

    for item in ingredient_dict:
        try:
            percentage = float(input(f"Enter the percentage for '{item}': "))
            ingredient_dict[item] = percentage
        except ValueError:
            print(f"Invalid input for '{item}'. Please enter a valid percentage.")

    print("Updated ingredient_dict:")
    return ingredient_dict
   
# # ----- Functions to calculate grams of ingredients ------
# def calculate_grams_of_water():
#     ...


main()