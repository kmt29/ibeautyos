import os
from pathlib import Path
import json

def get_KEY(keyname):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    KEYS_PATH = os.path.join(BASE_DIR,"KEYS.json")
    if os.path.exists(KEYS_PATH):
        with open("KEYS.json") as raw_json:
            data = json.load(raw_json)
            return data[keyname]
    else:
        return os.environ[keyname]

