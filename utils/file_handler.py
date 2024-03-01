import json
def read_json_file(file_path):


    """Reads data from a JSON file and returns it."""

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"No such file: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}")
        return None

def write_json_file(file_path, data):

    """Writes data to a JSON file."""

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        return False
