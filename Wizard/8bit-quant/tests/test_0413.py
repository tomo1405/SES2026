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
    # Test case 1: Valid input
    input_json = '{"key1": "aGVsbG8gd29ybGQ=", "key2": "d29ybGQ="}'
    expected_output = {'key1': 'hello world', 'key2': 'world'}
    assert task_func(input_json) == expected_output

    # Test case 2: Invalid input (not a JSON string)
    input_json = 'not a JSON string'
    with pytest.raises(json.JSONDecodeError):
        task_func(input_json)

    # Test case 3: Invalid input (not a base64 string)
    input_json = '{"key1": "not a base64 string", "key2": "d29ybGQ="}'
    with pytest.raises(base64.binascii.Error):
        task_func(input_json)

    # Test case 4: Invalid input (not a valid UTF-8 string)
    input_json = '{"key1": "aGVsbG8gd29ybGQ=", "key2": "d29ybGQ=\xff"}'
    with pytest.raises(UnicodeDecodeError):
        task_func(input_json)