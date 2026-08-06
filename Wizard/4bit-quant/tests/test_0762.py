python
import json
import re
from collections import Counter
import pytest

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    data = json.loads(json_str)
    
    # Remove None values and replace emails
    processed_data = {}
    for key, value in data.items():
        if value is None:
            continue
        if isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value):
            value = REPLACE_NONE
        processed_data[key] = value

    # Count frequency of each unique value
    value_counts = Counter(processed_data.values())

    return {"data": processed_data, "value_counts": value_counts}

def test_task_func():
    # Test case 1
    json_str = '{"name": "John", "email": "john@example.com", "age": null, "city": "New York"}'
    expected_output = {"data": {"name": "John", "email": REPLACE_NONE, "city": "New York"}, "value_counts": {"John": 1, "New York": 1}}
    assert task_func(json_str) == expected_output

    # Test case 2
    json_str = '{"name": "John", "email": "john@example.com", "age": 30, "city": "New York"}'
    expected_output = {"data": {"name": "John", "email": REPLACE_NONE, "age": 30, "city": "New York"}, "value_counts": {"John": 1, "New York": 1, 30: 1}}
    assert task_func(json_str) == expected_output

    # Test case 3
    json_str = '{"name": "John", "email": "john@example.com", "age": 30, "city": "New York", "country": "USA"}'
    expected_output = {"data": {"name": "John", "email": REPLACE_NONE, "age": 30, "city": "New York", "country": "USA"}, "value_counts": {"John": 1, "New York": 1, 30: 1, "USA": 1}}
    assert task_func(json_str) == expected_output