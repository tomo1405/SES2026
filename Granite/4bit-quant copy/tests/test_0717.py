import pytest
from src_0717 import task_func
import sys
import json
from datetime import datetime

PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'

def test_task_func():
    sys.path.append(PATH_TO_APPEND)

    with open(JSON_FILE, 'r+') as file:
        json_data = json.load(file)
        json_data['last_updated'] = str(datetime.now())
        file.seek(0)
        json.dump(json_data, file, indent=4)
        file.truncate()

    assert task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE) == json_data