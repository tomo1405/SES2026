python
import json
import re
from collections import Counter

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
    expected_result = {"data": {"name": "John", "email": REPLACE_NONE, "city": "New York"}, "value_counts": {"John": 1, REPLACE_NONE: 1}}
    assert task_func(json_str) == expected_result

    # Test case 2
    json_str = '{"name": "John", "email": "john@example.com", "age": null, "city": "New York", "phone": null}'
    expected_result = {"data": {"name": "John", "email": REPLACE_NONE, "city": "New York"}, "value_counts": {"John": 1, REPLACE_NONE: 1}}
    assert task_func(json_str) == expected_result

    # Test case 3
    json_str = '{"name": "John", "email": "john@example.com", "age": null, "city": "New York", "phone": "123-456-7890"}'
    expected_result = {"data": {"name": "John", "email": REPLACE_NONE, "city": "New York", "phone": REPLACE_NONE}, "value_counts": {"John": 1, REPLACE_NONE: 2}}
    assert task_func(json_str) == expected_result

    # Test case 4
    json_str = '{"name": "John", "email": "john@example.com", "age": null, "city": "New York", "phone": "123-456-7890", "email": null}'
    expected_result = {"data": {"name": "John", "email": REPLACE_NONE, "city": "New York", "phone": REPLACE_NONE}, "value_counts": {"John": 1, REPLACE_NONE: 2}}
    assert task_func(json_str) == expected_result

    # Test case 5
    json_str = '{"name": "John", "email": "john@example.com", "age": null, "city": "New York", "phone": "123-456-7890", "email": "jane@example.com"}'
    expected_result = {"data": {"name": "John", "email": REPLACE_NONE, "city": "New York", "phone": REPLACE_NONE}, "value_counts": {"John": 1, REPLACE_NONE: 2}}
    assert task_func(json_str) == expected_result

    # Test case 6
    json_str = '{"name": "John", "email": "john@example.com", "age": null, "city": "New York", "phone": "123-456-7890", "email": "jane@example.com", "age": 30}'
    expected_result = {"data": {"name": "John", "email": REPLACE_NONE, "city": "New York", "phone": REPLACE_NONE, "age": 30}, "value_counts": {"John": 1, REPLACE_NONE: 2, 30: 1}}
    assert task_func(json_str) == expected_result