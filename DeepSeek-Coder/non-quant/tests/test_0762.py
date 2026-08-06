import pytest
from src_0762 import task_func
import json

def test_task_func():
    # Test case 1: Basic functionality
    json_str = '{"key1": "email@example.com", "key2": "value2", "key3": None}'
    expected_output = {
        "data": {"key2": "value2"},
        "value_counts": {"value2": 1}
    }
    assert task_func(json_str) == expected_output

    # Add more test cases as needed

# Add more test cases as needed