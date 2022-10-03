import json
from typing import Dict

def get_json_dict(json_path:str)->Dict:
    with open(json_path, 'r') as jsonFile:
        return json.load(jsonFile)