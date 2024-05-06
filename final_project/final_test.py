import pytest
from unittest.mock import patch
from final import (
    calculate_percentages,
    calculate_weights,
    convert_percentages_to_decimals,
    modify_ingredient_weights,
    modify_ingredient_percentages,
)

# Test for calculating percentages based on flour weight
def test_calculate_percentages():
    ingredients = {"flour": 1000, "water": 600, "yeast": 20}
    flour_weight = 1000
    expected_output = {
        'flour': {'Weight (g)': 1000, 'Percent (%)': '100.00'}, 
        'water': {'Weight (g)': 600, 'Percent (%)': '60.00'}, 
        'yeast': {'Weight (g)': 20, 'Percent (%)': '2.00'}
        }
    assert calculate_percentages(ingredients, flour_weight) == expected_output

# Test for calculating weights based on percentages
def test_calculate_weights():
    ingredients_percent = {"flour": 100, "water": 60, "yeast": 2}
    flour_weight = 1000
    expected_output = {
        "flour": {"Percent (%)": "-", "Grams": 1000},
        "water": {"Percent (%)": "60.0", "Grams": 600.0},
        "yeast": {"Percent (%)": "2.0", "Grams": 20.0},
    }
    assert calculate_weights(ingredients_percent, flour_weight) == expected_output

# Test for converting percentages to decimals
def test_convert_percentages_to_decimals():
    ingredients = {"flour": 100, "water": 60, "yeast": 2}
    expected_output = {"flour": 100, "water": 0.6, "yeast": 0.02}
    assert convert_percentages_to_decimals(ingredients) == expected_output

# Test for modifying ingredient weights
@patch('builtins.input', side_effect=['water', '700', 'q'])
def test_modify_ingredient_weights(mock_input):
    ingredient_list = {"flour": 1000, "water": 600, "yeast": 20}
    flour_weight = 1000
    expected_output = {
        "flour": {"Weight (g)": 1000, "Percent (%)": "100.00"},
        "water": {"Weight (g)": 700, "Percent (%)": "70.00"},
        "yeast": {"Weight (g)": 20, "Percent (%)": "2.00"},
    }
    assert modify_ingredient_weights(ingredient_list, flour_weight) == expected_output

# Test for modifying ingredient percentages
@patch('builtins.input', side_effect=['water', '70', 'q'])
def test_modify_ingredient_percentages(mock_input):
    ingredient_list = {"flour": 100, "water": 60, "yeast": 2}
    flour_weight = 1000
    expected_output = {
        "flour": {"Percent (%)": "-", "Grams": 1000},
        "water": {"Percent (%)": 70.0, "Grams": 700.0},
        "yeast": {"Percent (%)": 2.0, "Grams": 20.0},
    }
    assert modify_ingredient_percentages(ingredient_list, flour_weight) == expected_output
