import json

def save_history(history, filename):
    with open(filename, 'w') as file:
        json.dump(history, file, indent=4)

def load_history(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []