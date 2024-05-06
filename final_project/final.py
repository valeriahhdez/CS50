import pandas as pd


def main():
    """
    Main function to start the recipe calculation program.
    It prompts the user to select the type of calculation they want to perform.
    """
    while True:
        try:
            type_of_recipe = input("What do you want to do?\n(1) Calculate percentages\n(2) Calculate grams\nEnter option (or 'q' to quit): ")
            if type_of_recipe == "1":
                create_recipe_from_grams()
            elif type_of_recipe == "2":
                create_recipe_from_percentage()
            elif type_of_recipe.lower() == 'q':
                break
            else:
                print("Invalid input. Please enter '1', '2', or 'q'.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def collect_ingredient_data():
    """
    Collects ingredient data from the user.
    Returns a dictionary with ingredients and their measurements.
    """
    ingredients = {}
    while True:
        ingredient = input("Enter the name of an ingredient or 'q' to finish: ")
        if ingredient.lower() == 'q':
            break
        try:
            measurement = float(input(f"Enter the measurement for {ingredient}: "))
            ingredients[ingredient] = measurement
        except ValueError:
            print("Please enter a valid number for the measurement.")
    return ingredients

def create_recipe_from_grams():
    """
    Creates a recipe table using grams as input values to calculate percentages.
    """
    ingredients = collect_ingredient_data()
    flour_weight = ingredients.get('flour', 0)
    if flour_weight <= 0:
        print("Flour weight must be greater than zero. Please start over.")
        return

    recipe_data = calculate_percentages(ingredients, flour_weight)
    display_recipe_table(recipe_data)

    if prompt_for_changes():
        recipe_data = modify_ingredient_weights(ingredients, flour_weight)
        display_recipe_table(recipe_data)

def calculate_percentages(ingredients, flour_weight):
    """
    Calculates the percentage of each ingredient relative to the flour weight.
    Returns a dictionary with the calculated data.
    """
    recipe_data = {}
    for ingredient, weight in ingredients.items():
        percentage = (weight / flour_weight) * 100
        recipe_data[ingredient] = {
            'Weight (g)': weight,
            'Percent (%)': f"{percentage:.2f}"
        }
    return recipe_data

def prompt_for_changes():
    """
    Prompts the user to decide if they want to make changes to the recipe.
    Returns True if changes are to be made, False otherwise.
    """
    while True:
        make_changes = input("Would you like to make any changes?\n(1) Yes\n(2) No\nEnter number: ")
        if make_changes == "1":
            return True
        elif make_changes == "2":
            return False
        else:
            print("Invalid input. Please enter '1' or '2'.")

def modify_ingredient_weights(ingredient_list, flour_weight):
    """
    Allows the user to modify the weights of ingredients and recalculates percentages.
    Returns the updated recipe data.
    """
    while True:
        ingredient = input("Enter the ingredient you want to change or 'q' to finish recipe: ")
        if ingredient.lower() == 'q':
            break
        if ingredient == 'flour':
            print("Flour weight cannot be changed.")
            continue
        try:
            weight = float(input(f"Enter the new weight in grams for {ingredient}: "))
            ingredient_list[ingredient] = weight
        except ValueError:
            print("Please enter a valid number for the weight.")
    return calculate_percentages(ingredient_list, flour_weight)

def create_recipe_from_percentage():
    """
    Creates a recipe table using percentages as input values to calculate grams.
    """
    ingredients = collect_ingredient_data()
    flour_weight = ingredients.get('flour', 0)
    if flour_weight <= 0:
        print("Flour weight must be greater than zero. Please start over.")
        return

    ingredients_percent = convert_percentages_to_decimals(ingredients)
    recipe_data = calculate_weights(ingredients_percent, flour_weight)
    display_recipe_table(recipe_data)

    if prompt_for_changes():
        recipe_data = modify_ingredient_percentages(ingredients, flour_weight)
        display_recipe_table(recipe_data)

def calculate_weights(ingredients_percent, flour_weight):
    """
    Calculates the weight in grams of each ingredient based on percentages.
    Returns a dictionary with the calculated data.
    """
    recipe_data = {}
    for ingredient, percent in ingredients_percent.items():
        if ingredient != 'flour':
            ingredient_grams = percent * flour_weight
            recipe_data[ingredient] = {
                'Percent (%)': percent * 100,
                'Grams': f"{ingredient_grams:.2f}"
            }
    recipe_data['flour'] = {
        'Percent (%)': '-',
        'Grams': flour_weight
    }
    return recipe_data

def modify_ingredient_percentages(ingredient_list, flour_weight):
    """
    Allows the user to modify the percentages of ingredients and recalculates weights.
    Returns the updated recipe data.
    """
    while True:
        ingredient = input("Enter the ingredient you want to change or 'q' to finish recipe: ")
        if ingredient.lower() == 'q':
            break
        try:
            percentage = float(input(f"Enter the new percentage for {ingredient}: "))
            ingredient_list[ingredient] = percentage
        except ValueError:
            print("Please enter a valid number for the percentage.")
    return calculate_weights(convert_percentages_to_decimals(ingredient_list), flour_weight)

def display_recipe_table(recipe_data):
    """
    Displays the recipe table from the recipe data.
    """
    recipe_table = pd.DataFrame.from_dict(recipe_data, orient='index')
    print(recipe_table)

def convert_percentages_to_decimals(ingredients_dict):
    """
    Converts percentages to decimal format for all ingredients except flour.
    Returns the updated ingredients dictionary.
    """
    for key, value in ingredients_dict.items():
        if key != 'flour':
            ingredients_dict[key] = value / 100
    return ingredients_dict

if __name__ == "__main__":
    main()
