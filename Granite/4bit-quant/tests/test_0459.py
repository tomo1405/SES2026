import json
import re
import pandas as pd
from src_0459 import task_func

def test_task_func():
    json_str = '{"a": 1, "b": 2, "c": [3, 4]}'
    expected_df = pd.DataFrame({"a": [2], "b": [4], "c": [6, 8]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_empty_dict():
    json_str = '{}'
    expected_df = pd.DataFrame()
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_non_numeric_values():
    json_str = '{"a": "1", "b": "2", "c": ["3", "4"]}'
    expected_df = pd.DataFrame({"a": [2], "b": [4], "c": [6, 8]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_numeric_column():
    json_str = '{"a": 1, "b": 2.5, "c": [3, 4.5]}'
    expected_df = pd.DataFrame({"a": [2], "b": [5], "c": [6, 9]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)