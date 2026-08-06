import json
import base64
import unicodedata
from src_0413 import task_func
import pytest

def test_task_func():
    json_file = 'test_data.json'
    data = {
        "key1": "SGVsbG8gV29ybGQ=",
        "key2": "QSBjb3VudCBpbiBiYXNlNjQgY29kZS4gQSBzZWN1cmUgdmFsdWUu",
        "key3": "SGVsbG8gV29ybGQ="
    }

    with open(json_file, 'w') as f:
        json.dump(data, f)

    decoded_data = task_func(json_file)

    assert decoded_data == {
        "key1": "Hello World",
        "key2": "A customer in base64 code. A secret value.",
        "key3": "Hello World"
    }

def test_task_func_invalid_json():
    json_file = 'invalid_json.json'
    with open(json_file, 'w') as f:
        f.write("Invalid JSON data")

    with pytest.raises(ValueError) as excinfo:
        task_func(json_file)

    assert "Invalid JSON" in str(excinfo.value)