import json
import cases
def save_cases(path, items):
    if cases.valid_cases(items) is False:
        return False
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False
def load_cases(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if cases.valid_cases(data) is True:
            return data
        else:
            return None
    except FileNotFoundError:
        return []
    except:
        return None
