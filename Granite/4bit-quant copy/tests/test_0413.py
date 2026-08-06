import json
import base64
import unicodedata
from src_0413 import task_func
import pytest

def test_task_func():
    json_file = 'test_data.json'
    data = {
        'key1': 'c29tZS12YWx1ZQ==',
        'key2': 'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo='
    }

    with open(json_file, 'w') as f:
        json.dump(data, f)

    decoded_data = task_func(json_file)

    assert decoded_data == {
        'key1': 'some-value',
        'key2': 'abcdefghijklmnopqrstuvwxyz'
    }

def test_task_func_invalid_json():
    json_file = 'invalid_json.json'
    with open(json_file, 'w') as f:
        f.write('invalid json data')

    with pytest.raises(ValueError) as excinfo:
        task_func(json_file)

    assert 'Invalid JSON' in str(excinfo.value)