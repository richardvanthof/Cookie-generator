from typing import TypedDict, Literal

class Ingredient(TypedDict):
    name: str
    amount: float
    unit: str
    flavour: Literal[
        'acidity', 'salt', 'spice', 'bitter', 
        'creamy', 'sweet', 'none', 'aromatic'
        ]
    type: Literal[
        'starches', 'sugars', 'salts', 'fats', 
        'seeds_nuts_dried_fruits', 'binders', 
        'produce', 'spices', 'sugars', 'liquids'
        ]
    ingredients: list[Ingredient]
    cons: Literal["SOLID", "LIQUID"]

class Recipe(TypedDict):
    name: str
    servings: int
    ingredients: list[Ingredient]
    source: str