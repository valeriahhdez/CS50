# Bread Recipe Calculator

#### Video Demo:  <URL HERE>

## Overview
This is my capstone project for [Harvard's CS50 Introduction to Python](https://cs50.harvard.edu/python/2022/). The Bread Recipe Calculator is designed to assist you creating bread recipes based on either grams or percentages of ingredients. It's an interactive command-line application that guides you through the process of recipe creation and modification.

## Project dependencies

To run this program, you will need the following installed on your system: 
- Python 3
- pandas library  
  
If you do not have pandas installed, you can install it using pip:

```bash
pip install pandas
````

## Features
- **Calculate Recipes by Grams**: Input the weight of each ingredient in grams to calculate their relative percentages in the recipe.
- **Calculate Recipes by Percentages**: Input the percentage of each ingredient to calculate their weight in grams.
- **Interactive Prompts**: The program prompts the user for inputs and provides feedback for invalid entries.
- **Recipe Modification**: Users can modify the recipe after initial calculation, either by changing ingredient weights or percentages.
- **Pandas DataFrame Display**: Recipes are displayed in a table format for easy reading and interpretation.

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the program using the following command:


````bash
python3 bread_recipe.py
````

4. Follow the on-screen prompts to create and modify your bread recipe.
   - Choose between calculating by grams or percentages.
   - Enter ingredient names and measurements.
   - Review the calculated recipe.
   - Modify the recipe if needed.

## Example

Suppose you want to create a simple bread recipe using grams. Here’s how you can use the program:

1. Select option 1 (Calculate percentages).
2. Enter the ingredient names and their weights in grams.
3. Review the calculated percentages.
4. If you want to adjust any ingredient, choose option 1 (Make changes) and update the weights.
5. The modified recipe will be displayed.

