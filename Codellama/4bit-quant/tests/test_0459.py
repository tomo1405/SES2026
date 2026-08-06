import pandas as pd
from src_0459 import task_func


def test_task_func():
    json_str = '{"a": 1, "b": [2, 3], "c": "4"}'
    expected_df = pd.DataFrame({"a": [2], "b": [4, 6], "c": [8]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_empty_json():
    json_str = ''
    expected_df = pd.DataFrame()
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_invalid_json():
    json_str = '{"a": 1, "b": [2, 3], "c": "4"'
    expected_df = pd.DataFrame()
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_invalid_value():
    json_str = '{"a": 1, "b": [2, 3], "c": "4", "d": "invalid"}'
    expected_df = pd.DataFrame({"a": [2], "b": [4, 6], "c": [8]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)

def test_task_func_nested_list():
    json_str = '{"a": 1, "b": [2, 3], "c": "4", "d": [{"e": 5}]}'
    expected_df = pd.DataFrame({"a": [2], "b": [4, 6], "c": [8], "d": [{"e": 10}]})
    actual_df = task_func(json_str)
    assert actual_df.equals(expected_df)