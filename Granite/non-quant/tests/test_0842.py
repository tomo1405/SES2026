import json
import re
from collections import defaultdict
import string
from src_0842 import task_func
def test_task_func():
    json_string = '{"text": "Hello, world!"}'
    expected_result = {'hello': 1, 'world': 1}
    result = task_func(json_string)
    assert result == expected_result
def test_task_func_with_invalid_json():
    json_string = '{"text": "Invalid JSON"}'
    expected_result = {}
    result = task_func(json_string)
    assert result == expected_result
def test_task_func_with_empty_text():
    json_string = '{"text": ""}'
    expected_result = {}
    result = task_func(json_string)
    assert result == expected_result
def test_task_func_with_no_text_key():
    json_string = '{}'
    expected_result = {}
    result = task_func(json_string)
    assert result == expected_result