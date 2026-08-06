import json
import base64
from datetime import datetime
from src_0028 import task_func
import pytest

def test_task_func():
    data = {"key": "value"}
    expected_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_json_data = json.dumps({"key": "value", "timestamp": expected_timestamp})
    expected_encoded_data = base64.b64encode(expected_json_data.encode('ascii')).decode('ascii')

    actual_encoded_data = task_func(data)

    assert actual_encoded_data == expected_encoded_data

def test_task_func_with_empty_dict():
    data = {}
    expected_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_json_data = json.dumps({"timestamp": expected_timestamp})
    expected_encoded_data = base64.b64encode(expected_json_data.encode('ascii')).decode('ascii')

    actual_encoded_data = task_func(data)

    assert actual_encoded_data == expected_encoded_data

def test_task_func_with_none_data():
    with pytest.raises(TypeError):
        task_func(None)