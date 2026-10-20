import unittest
import json
from typing import TypedDict, Literal
from ast import Dict
from pathlib import Path
import sys

repository_root = Path(__file__).resolve().parents[2]
if str(repository_root) not in sys.path:
    sys.path.insert(0, str(repository_root))

from functions.Fitness.fitness import has_correct_ingredient_ratios
from functions.Fitness.types import Recipe
from utils.load_json import load_json_file

test_data: list[Recipe] = load_json_file(
    Path(__file__).with_name("testData.json")
)
print(test_data)


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

# def load_json_file(file_path:str) -> Dict:
#     path:Path = Path(file_path)

#     if not path.exists():
#         raise FileNotFoundError(f"File not found: {path.resolve()}")

#     if not path.read_text(encoding="utf-8").strip():
#         raise ValueError(f"JSON file is empty: {path.resolve()}")

#     try:
#         with path.open("r", encoding="utf-8") as f:
#             return json.load(f)
#     except json.JSONDecodeError as error:
#         raise ValueError(
#             f"Invalid JSON in {path.resolve()} "
#             f"at line {error.lineno}, column {error.colno}"
#         ) from error





# class TestAdd(unittest.TestCase):
#     def test_addition(self):
#         self.assertEqual(add(2, 3), 5)


# if __name__ == "__main__":
#     unittest.main()