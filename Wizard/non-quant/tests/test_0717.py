python
import sys
import json
from datetime import datetime
import pytest

# Constants
PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'

def task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE):
    sys.path.append(path_to_append)

    with open(json_file, 'r+') as file:
        json_data = json.load(file)
        json_data['last_updated'] = str(datetime.now())
        file.seek(0)
        json.dump(json_data, file, indent=4)
        file.truncate()

    return json_data

def test_task_func():
    # Test with default arguments
    assert task_func() == {'last_updated': '2022-07-17 15:22:22.123456'}

    # Test with custom arguments
    assert task_func(path_to_append='/path/to/custom/whatever', json_file='/path/to/custom/json_file.json') == {'last_updated': '2022-07-17 15:22:22.123456'}