import pytest
from src_0762 import task_func

def test_task_func():
    json_str = '{"name": "John", "age": 30, "email": "john@example.com"}'
    expected_data = {"name": "John", "age": 30, "email": "None"}
    expected_value_counts = {"None": 1, "John": 1, 30: 1}

    result = task_func(json_str)

    assert result["data"] == expected_data
    assert result["value_counts"] == expected_value_counts