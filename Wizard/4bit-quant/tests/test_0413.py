python
import json
import base64
import unicodedata
import pytest

def task_func(json_file: str) -> dict:
    ENCODING = 'utf-8'
    
    with open(json_file, 'r') as f:
        data = json.load(f)

    decoded_data = {k: unicodedata.normalize('NFC', base64.b64decode(v).decode(ENCODING)) for k, v in data.items()}

    return decoded_data

def test_task_func():
    # Test case 1
    json_file = 'test_data.json'
    expected_output = {'key1': 'value1', 'key2': 'value2'}
    with open(json_file, 'w') as f:
        json.dump({'key1': 'dmFsdWUx', 'key2': 'dmFsdWUy'}, f)
    output = task_func(json_file)
    assert output == expected_output
    # Test case 2
    json_file = 'test_data.json'
    expected_output = {'key1': 'value1', 'key2': 'value2'}
    with open(json_file, 'w') as f:
        json.dump({'key1': 'dmFsdWUx', 'key2': 'dmFsdWUy'}, f)
    output = task_func(json_file)
    assert output == expected_output
    # Test case 3
    json_file = 'test_data.json'
    expected_output = {'key1': 'value1', 'key2': 'value2'}
    with open(json_file, 'w') as f:
        json.dump({'key1': 'dmFsdWUx', 'key2': 'dmFsdWUy'}, f)
    output = task_func(json_file)
    assert output == expected_output