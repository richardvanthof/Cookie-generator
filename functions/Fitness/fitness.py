from typing import TypedDict, Literal
import json
from pathlib import Path
import sys

repository_root = Path(__file__).resolve().parents[2]
if str(repository_root) not in sys.path:
    sys.path.insert(0, str(repository_root))

from functions.Fitness.types import Recipe

def has_correct_ingredient_ratios(recipe: Recipe, ratios: list[tuple[str, float, float]], key: str) -> float:
    targets_reached: int = 0;

    for ingredient_type, min_ratio, max_ratio in ratios:
        
        # see the total amount of the ingredient per type
        total_amount = sum(
            ing["amount"] for ing in recipe["ingredients"] if ing[key] == ingredient_type
        )

        # total mass of the recipe
        total_recipe_amount = sum(ing["amount"] for ing in recipe["ingredients"])
        ratio = total_amount / total_recipe_amount if total_recipe_amount > 0 else 0

        if (min_ratio <= ratio <= max_ratio):
            targets_reached += 1
    ratio = targets_reached / len(ratios) if len(ratios) > 0 else 0
    print("Ratio:", ratio, "Targets reached:", targets_reached, "Total ratios:", len(ratios))
    return ratio  # Return the proportion of targets reached


# def evaluate_recipes(recipes: list[Recipe]) -> None:
texture_ratios: list[tuple[str, float, float]] = [
            ("starches", 0.2, 0.4),                 # Starches should be between 20% and 40%
            ("sugars", 0.2, 0.4),                   # Sugars should be between 20% and 40%
            ("salts", 0.01, 0.05),                  # Salts should be between 1% and 5%
            ("fats", 0.1, 0.3),                     # Fats should be between 10% and 30%
            ("liquids", 0.1, 0.3),                  # Liquids should be between 10% and 30%
            ("binders", 0.05, 0.15),                # Binders (like eggs) should be between 5% and 15%
            ("leavening_agents", 0.01, 0.05),       # Leavening agents should be between 1% and 5%
            ("spices", 0.01, 0.05),                 # Flavorings should be between 1% and 5%
            ("seeds_nuts_dried_fruits", 0.01, 0.1), # Seeds, nuts, and dried fruits should be between 1% and 10%
            ("produce", 0.01, 0.1)                  # Fresh produce should be between 1% and 10%
        ]
path: Path = Path(__file__).with_name("testData.json")
with path.open("r", encoding="utf-8") as f:
            test_data:list[Recipe] = json.load(f)

flavour_ratios: list[tuple[str, float, float]] = [
        ("acidity", 0.012610533234090978, 0.05),              
        ("salt", 0.0010696354325280442, 0.05),                   
        ("spice", 0.017011286527471157, 0.05),                  
        ("bitter", 0.006801153718857514, 0.05),                 
        ("creamy", 0.15454724806392225, 0.3),                   
        ("sweet", 0.20010430855331854, 0.4),                   
        ("aromatic", 0.020651303838833082, 0.05)                
]

flavour_ratio = has_correct_ingredient_ratios(test_data[0], flavour_ratios, "flavour")
flavour_ratio = has_correct_ingredient_ratios(test_data[0], texture_ratios, "texture")


print(flavour_ratio)

