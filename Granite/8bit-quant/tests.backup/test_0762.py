import json
import re
from collections import Counter
from src_0762 import task_func

def test_task_func():
    json_str = '{"name": "John", "email": "john@example.com", "age": 30, "location": null}'
    expected_output = {
        "data": {
            "name": "John",
            "email": REPLACE_NONE,
            "age": 30
        },
        "value_counts": Counter({30: 1, "John": 1, REPLACE_NONE: 1})
    }
    output = task_func(json_str)
    assert output == expected_output

def test_task_func_with_no_data():
    json_str = '{}'
    expected_output = {
        "data": {},
        "value_counts": Counter()
    }
    output = task_func(json_str)
    assert output == expected_output

def test_task_func_with_null_and_email():
    json_str = '{"name": null, "email": "john@example.com", "age": null}'
    expected_output = {
        "data": {
            "email": REPLACE_NONE
        },
        "value_counts": Counter({REPLACE_NONE: 2})
    }
    output = task_func(json_str)
    assert output == expected_output