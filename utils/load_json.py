
from ast import Dict
from pathlib import Path
import json

def load_json_file(file_path:str) -> Dict:
    path:Path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path.resolve()}")

    if not path.read_text(encoding="utf-8").strip():
        raise ValueError(f"JSON file is empty: {path.resolve()}")

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in {path.resolve()} "
            f"at line {error.lineno}, column {error.colno}"
        ) from error