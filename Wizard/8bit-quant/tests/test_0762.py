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
    json_str = '{"name": "John Doe", "email": "johndoe@example.com", "age": null, "city": "New York"}'
    expected_result = {"data": {"name": "John Doe", "email": REPLACE_NONE, "city": "New York"}, "value_counts": {"New York": 1}}
    assert task_func(json_str) == expected_result

    # Test case 2
    json_str = '{"name": "Jane Doe", "email": null, "age": 30, "city": "Los Angeles"}'
    expected_result = {"data": {"name": "Jane Doe", "age": 30, "city": "Los Angeles"}, "value_counts": {"Los Angeles": 1}}
    assert task_func(json_str) == expected_result

    # Test case 3
    json_str = '{"name": "Bob Smith", "email": "bob@example.com", "age": 40, "city": "Chicago"}'
    expected_result = {"data": {"name": "Bob Smith", "email": REPLACE_NONE, "age": 40, "city": "Chicago"}, "value_counts": {"Chicago": 1}}
    assert task_func(json_str) == expected_result