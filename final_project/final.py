from tabulate import tabulate
# while True:
#     options = input("What do you want to do with your recipe?\n (1) Get %\n (2) Get gr \n Enter number:")
#     if "1" in options:
#         print("Let's calculate percentage")
#     elif "2" in options:
#         print("Let's calculate the grams")
#     elif "3" in options:
#         break
    


# Prompt the user to select whether he wants to calculate % or gr
# After the user selects an option, the program will follow these steps:
    # Enter the name of an ingredient
    # Enter a float (percentage or grams)
    # Enter 3 when all ingredients are entered
    # The program prints a table with all the ingredients of the recipe and their calculated percentages of grams

def main():
    # prompts the user to select type of calculation
    type_of_recipe = input("(1) to calculate percentages\n (2) to calculate gr\n Enter option: ")
    if type_of_recipe == "1":
        print(percentage_recipe())
    # elif "2" in type_of_recipe:
    #     ingredient = input("Enter ingredient and gr: ")
    #     calculate_grams(ingredient)

def percentage_recipe():
    ingredients = {}
    while True:
        # Prompt user to enter ingredients and weights one by one until he/she completes list
        ingredient = input("Enter an ingredient (or 'q' to quit): ")
        if ingredient.lower() == 'q':
            break
        weight = float(input(f"Enter the weight in grams of {ingredient}: "))
        ingredients[ingredient] = weight
    # Ensure flour has been entered and has a non-zero weight
    flour_weight = ingredients.get('flour')
    if flour_weight == 0:
        print("Flour weight is zero or not provided, cannot calculate percentages.")
        return 
    # Calculate and store percentages inside a list
    recipe_data = {}
    for ingredient, weight in ingredients.items():
        percentage = calculate_percentage(weight, flour_weight)
        recipe_data[ingredient] = {
            'Weight (g)': weight,
            '% of flour weight': f"{percentage:.2f} %"
        }
        # Create table using the data from list
        print(tabulate(recipe_data, headers=['Ingredient', 'Weight (g)', '% of flour weight']))
        # Ask if user wants to make changes to the recipe
        make_changes = input("Would you like to change anything?\n (1) Yes\n (2) No\n Enter number: ")
        if make_changes == "1":
            print("Updated recipe")
            change_recipe()

def change_recipe(ingredient_list, flour_weight):
    while True:
        ingredient_to_change = input("\nEnter the ingredient you want to change (or 'q' to quit): ")
        if ingredient_to_change.lower() == 'q':
            break
        new_weight = float(input(f"Enter the new weight in grams for {ingredient_to_change}: "))
        ingredient_list[ingredient_to_change] = new_weight
        new_recipe_data = {}
    for ingredient, weight in ingredient_list.items():
        percentage = calculate_percentage(new_weight, flour_weight)
        new_recipe_data[ingredient] = {
            'Weight (g)': weight,
            '% of flour weight': f"{percentage:.2f} %"
        }
    return tabulate(new_recipe_data.items(), headers=['Ingredient', 'Weight (g)', '% of flour weight'])

def calculate_percentage(x_weight, y_weight):
    return (x_weight/y_weight) *100

# def calculate_grams():
    # ingredients = {}
    # while True:
    #     ingredient = input("Enter an ingredient (or 'q' to quit): ")
    #     if ingredient.lower() == 'q':
    #         break
    #     percentage = float(input(f"Enter the % of {ingredient}: "))
    #     ingredients[ingredient] = percentage

    # flour_weight = ingredients.get('flour', 0)
    # if flour_weight == 0:
    #     print("Flour weight is zero or not provided, cannot calculate percentages.")
        

    # data = []
    # for ingredient, weight in ingredients.items():
    #     percentage = (weight / flour_weight) * 100
    #     data.append([ingredient, weight, f"{percentage:.2f} %"])

    # return tabulate(data, headers=['Ingredient', 'Weight (g)', 'Percentage of Flour Weight'])
   

main()