import json
import re
from collections import Counter
from src_0762 import task_func

def test_task_func():
    json_str = '{"name": "John", "email": "john@example.com", "age": 30, "location": null}'
    expected_output = {"data": {"name": "John", "email": REPLACE_NONE, "age": 30, "location": REPLACE_NONE}, 
                       "value_counts": Counter({"John": 1, 30: 1, REPLACE_NONE: 2})}
    actual_output = task_func(json_str)
    assert actual_output == expected_output

def test_task_func_with_empty_input():
    json_str = '{}'
    expected_output = {"data": {}, "value_counts": Counter()}
    actual_output = task_func(json_str)
    assert actual_output == expected_output

def test_task_func_with_no_none_values():
    json_str = '{"name": "John", "email": "john@example.com", "age": 30, "location": "New York"}'
    expected_output = {"data": {"name": "John", "email": "john@example.com", "age": 30, "location": "New York"}, 
                       "value_counts": Counter({"John": 1, "john@example.com": 1, 30: 1, "New York": 1})}
    actual_output = task_func(json_str)
    assert actual_output == expected_output