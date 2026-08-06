import pandas as pd
from src_0459 import task_func


def test_task_func_empty_json():
    json_str = ""
    expected_df = pd.DataFrame()
    assert task_func(json_str).equals(expected_df)

def test_task_func_non_empty_json():
    json_str = '{"a": 1, "b": [2, 3], "c": "4"}'
    expected_df = pd.DataFrame({"a": [2], "b": [4, 6], "c": [8]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_non_numeric_values():
    json_str = '{"a": "1", "b": ["2", "3"], "c": "4"}'
    expected_df = pd.DataFrame({"a": [2], "b": [4, 6], "c": [8]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_nested_lists():
    json_str = '{"a": [1, [2, 3]], "b": [4, 5], "c": [6, 7]}'
    expected_df = pd.DataFrame({"a": [2, [4, 6]], "b": [8, 10], "c": [12, 14]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_nested_dicts():
    json_str = '{"a": {"b": 1, "c": 2}, "d": {"e": 3, "f": 4}}'
    expected_df = pd.DataFrame({"a": {"b": 2, "c": 4}, "d": {"e": 6, "f": 8}})
    assert task_func(json_str).equals(expected_df)

def test_task_func_mixed_types():
    json_str = '{"a": 1, "b": [2, 3], "c": "4"}'
    expected_df = pd.DataFrame({"a": [2], "b": [4, 6], "c": [8]})
    assert task_func(json_str).equals(expected_df)

def test_task_func_invalid_json():
    json_str = '{"a": 1, "b": [2, 3], "c": "4"'
    expected_df = pd.DataFrame()
    assert task_func(json_str).equals(expected_df)