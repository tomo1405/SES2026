import json
from datetime import datetime
from src_0173 import task_func
import pytest

def test_task_func_with_valid_input():
    json_data = '{"utc_datetime": "2023-03-14T12:34:56"}'
    expected_output = True
    actual_output = task_func(json_data)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    json_data = '{"utc_datetime": "2023-03-14T12:34:56'
    with pytest.raises(Exception):
        task_func(json_data)

def test_task_func_with_invalid_json():
    json_data = '{"utc_datetime": "2023-03-14T12:34:56'
    with pytest.raises(json.decoder.JSONDecodeError):
        task_func(json_data)