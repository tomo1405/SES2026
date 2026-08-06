python
import base64
import json
import zlib
import pytest

def task_func(data_dict):
    json_str = json.dumps(data_dict)
    compressed = zlib.compress(json_str.encode())
    return base64.b64encode(compressed).decode()

def test_task_func():
    data_dict = {'key1': 'value1', 'key2': 'value2'}
    result = task_func(data_dict)
    assert isinstance(result, str)
    assert len(result) > 0