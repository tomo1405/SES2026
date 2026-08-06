import pandas as pd
from src_0459 import task_func


def test_task_func_empty_json():
    json_str = ""
    expected_df = pd.DataFrame()
    assert task_func(json_str).equals(expected_df)

def test_task_func_non_empty_json():
    json_str = '{"a": 1, "b": [2, 3], "c": "4.5"}'
    expected_df = pd.DataFrame({"a": [2], "b": [4, 6], "c": [9]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_non_numeric_values():
    json_str = '{"a": "hello", "b": [2, 3], "c": "world"}'
    expected_df = pd.DataFrame({"a": ["hello", "hello"], "b": [4, 6], "c": ["world", "world"]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_non_numeric_values_in_list():
    json_str = '{"a": [1, "hello"], "b": [2, 3], "c": "world"}'
    expected_df = pd.DataFrame({"a": [2, "hello"], "b": [4, 6], "c": ["world", "world"]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_non_numeric_values_in_nested_list():
    json_str = '{"a": [[1, "hello"], [2, 3]], "b": [4, 5], "c": "world"}'
    expected_df = pd.DataFrame({"a": [[2, "hello"], [4, 6]], "b": [8, 10], "c": ["world", "world"]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_non_numeric_values_in_nested_list_with_non_numeric_values():
    json_str = '{"a": [[1, "hello"], [2, "world"]], "b": [4, 5], "c": "world"}'
    expected_df = pd.DataFrame({"a": [[2, "hello"], [4, "world"]], "b": [8, 10], "c": ["world", "world"]})
    assert task_func(json_str).equals(expected_df)