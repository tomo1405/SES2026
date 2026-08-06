import pytest
from src_0762 import task_func

def test_task_func():
    # Test case 1: Empty input
    json_str = ""
    expected_output = {"data": {}, "value_counts": Counter()}
    assert task_func(json_str) == expected_output

    # Test case 2: Valid input with None values
    json_str = '{"key1": "value1", "key2": None, "key3": "value3"}'
    expected_output = {"data": {"key1": "value1", "key3": "value3"}, "value_counts": Counter({"value1": 1, "value3": 1})}
    assert task_func(json_str) == expected_output

    # Test case 3: Valid input with email values
    json_str = '{"key1": "value1", "key2": "email@example.com", "key3": "value3"}'
    expected_output = {"data": {"key1": "value1", "key2": REPLACE_NONE, "key3": "value3"}, "value_counts": Counter({"value1": 1, "value3": 1})}
    assert task_func(json_str) == expected_output

    # Test case 4: Invalid input
    json_str = "invalid_json"
    with pytest.raises(ValueError):
        task_func(json_str)