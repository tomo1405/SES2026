import json
import re
from collections import defaultdict
import string

from src_0842 import task_func

def test_task_func():
    json_string = '{"text": "Hello, world!"}'
    expected_result = {'hello': 1, 'world': 1}
    assert task_func(json_string) == expected_result

def test_task_func_with_invalid_json():
    json_string = '{"text": "Invalid JSON"}'
    expected_result = {}
    assert task_func(json_string) == expected_result

def test_task_func_with_empty_text():
    json_string = '{"text": ""}'
    expected_result = {}
    assert task_func(json_string) == expected_result

def test_task_func_with_punctuation():
    json_string = '{"text": "Hello, world!"}'
    expected_result = {'hello': 1, 'world': 1}
    assert task_func(json_string) == expected_result

def test_task_func_with_uppercase():
    json_string = '{"text": "HELLO, WORLD!"}'
    expected_result = {'hello': 1, 'world': 1}
    assert task_func(json_string) == expected_result