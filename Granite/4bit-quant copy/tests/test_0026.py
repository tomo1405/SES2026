import base64
import json
import zlib

def task_func(data_dict):
    json_str = json.dumps(data_dict)
    compressed = zlib.compress(json_str.encode())
    return base64.b64encode(compressed).decode()

def test_task_func():
    data_dict = {"key": "value"}
    expected_output = "expected_output"  # Replace with the expected output for the given input
    actual_output = task_func(data_dict)
    assert actual_output == expected_output