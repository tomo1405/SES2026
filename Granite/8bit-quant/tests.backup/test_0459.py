import json
import re
import pandas as pd
from src_0459 import task_func

def test_task_func():
    json_str = '{"a": 1, "b": 2, "c": 3}'
    expected_df = pd.DataFrame({"a": [2], "b": [4], "c": [6]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_with_list():
    json_str = '{"a": [1, 2, 3], "b": 2, "c": 3}'
    expected_df = pd.DataFrame({"a": [1, 2, 3], "b": [4], "c": [6]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_with_string_number():
    json_str = '{"a": "1", "b": 2, "c": 3}'
    expected_df = pd.DataFrame({"a": [2], "b": [4], "c": [6]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_with_non_numeric_string():
    json_str = '{"a": "abc", "b": 2, "c": 3}'
    expected_df = pd.DataFrame({"a": ["abc"], "b": [4], "c": [6]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_with_empty_dict():
    json_str = '{}'
    expected_df = pd.DataFrame()
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)