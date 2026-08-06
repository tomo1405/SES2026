python
import re
import json
import os
import pytest

def task_func(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
        text = ' '.join(data.values())
        matches = re.findall(regex_pattern, text)

    match_dict = {os.path.basename(file_path): matches}
    return match_dict

def test_task_func():
    # Test case 1: Valid input file
    file_path = 'data.json'
    with open(file_path, 'w') as file:
        json.dump({'name': 'John Doe', 'age': 30}, file)
    assert task_func(file_path) == {'data.json': ['John Doe', '30']}
    os.remove(file_path)

    # Test case 2: Invalid input file
    file_path = 'invalid.txt'
    with open(file_path, 'w') as file:
        file.write('This is not a JSON file')
    with pytest.raises(json.JSONDecodeError):
        task_func(file_path)
    os.remove(file_path)

    # Test case 3: Custom regex pattern
    file_path = 'data.json'
    with open(file_path, 'w') as file:
        json.dump({'name': 'John Doe', 'age': 30}, file)
    assert task_func(file_path, regex_pattern=r'\w+') == {'data.json': ['John', 'Doe', '30']}
    os.remove(file_path)