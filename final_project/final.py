import pandas as pd
import sys

def main():
    # prompt the user to select type of calculation
    try: 
        type_of_recipe = input("What do you want to do with your ingredients?\n(1) Calculate percentages\n(2) Calculate gr\nEnter option: ")
        if type_of_recipe == "1":
            create_recipe_from_grams()
        elif "2" in type_of_recipe:
            create_recipe_from_percentage()
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")


def collect_ingredient_weights():
    ingredients = {}
    while True:
        ingredient = input("Enter the name of an ingredient or 'q' to finish: ")
        if ingredient.lower() == 'q':
            break
        weight = get_user_input(f"Enter the weight in grams of {ingredient}: ")
        ingredients[ingredient] = weight
    return ingredients
def create_recipe_from_grams():
    ingredients = collect_ingredient_weights()

    # Ensure flour weight is provided
    flour_weight = ingredients.get('flour', 0)
    if flour_weight == 0:
        print("Flour weight is zero or not provided. Cannot create recipe.")
        return

    recipe_data = {}
    for ingredient, weight in ingredients.items():
        percentage = calculate_percentage(weight, flour_weight)
        recipe_data[ingredient] = {
            'Weight (g)': weight,
            '% of flour weight': f"{percentage:.2f} %"
        }

    recipe_table = pd.DataFrame.from_dict(recipe_data, orient='index')
    print(recipe_table)

    make_changes = input("Would you like to make any changes?\n(1) Yes\n(2) No\nEnter number: ")
    if make_changes == "1":
        print(change_recipe(ingredients, flour_weight))
    elif make_changes == "2":
        sys.exit()

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
   
# # ----- Formula functions ------
def calculate_percentage(x_weight, y_weight):
    return (x_weight/y_weight) *100

def calculate_grams_of_water(total_flour, hydration_percent, starter_percent, starter_hydration, butter_percent, milk_percent, cream_water_percent, cream_percent):
    """
    Calculate the grams of water needed based on ingredient percentages.

    Args:
        total_flour (float): Total flour weight in grams.
        hydration_percent (float): Desired hydration percentage.
        starter_percent (float): Percentage of starter in the recipe.
        starter_hydration (float): Hydration percentage of the starter.
        butter_percent (float): Percentage of butter in the recipe.
        milk_percent (float): Percentage of milk in the recipe.
        cream_water_percent (float): Percentage of water in cream.
        cream_percent (float): Percentage of cream in the recipe.

    Returns:
        float: Grams of water needed.
    """
    starter_hydration_factor = 1 + 1 / starter_hydration
    water_grams = total_flour * (
        hydration_percent
        - starter_percent / starter_hydration_factor
        - 0.15 * butter_percent
        - 0.87 * milk_percent
        - cream_water_percent * cream_percent
    )
    return water_grams

def calculate_grams_of_white_flour(total_flour, starter_percent, starter_hydration_percent, wholeness_percent):
    """
    Calculate the grams of white flour needed based on ingredient percentages.

    Args:
        total_flour (float): Total flour weight in grams.
        starter_percent (float): Percentage of starter in the recipe.
        starter_hydration_percent (float): Hydration percentage of the starter.
        wholeness_percent (float): Percentage of whole grains (non-white flour).

    Returns:
        float: Grams of white flour needed.
    """
    starter_hydration_factor = 1 + 1 / starter_hydration_percent

    white_flour_grams = total_flour * (
        1 - starter_percent / starter_hydration_factor - wholeness_percent
    )

    return white_flour_grams



main()