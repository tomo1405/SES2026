import pytest
from src_0459 import task_func
import pandas as pd

def test_task_func_empty_json():
    result = task_func("{}")
    assert result.empty

def test_task_func_single_integer():
    result = task_func('{"a": 1}')
    expected_df = pd.DataFrame({"a": [2]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_single_float():
    result = task_func('{"b": 3.5}')
    expected_df = pd.DataFrame({"b": [7.0]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_single_string_number():
    result = task_func('{"c": "4"}')
    expected_df = pd.DataFrame({"c": [8]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_string_not_number():
    result = task_func('{"d": "hello"}')
    expected_df = pd.DataFrame({"d": ["hello"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_list_of_numbers():
    result = task_func('{"e": [1, 2.5, "3", "not_a_number"]}')
    expected_df = pd.DataFrame({"e": [2, 5.0, 6, "not_a_number"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_mixed_values():
    result = task_func('{"f": 1, "g": [2, "3"], "h": "4.5"}')
    expected_df = pd.DataFrame({"f": [2], "g": [4, 6], "h": [9.0]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_non_numeric_values():
    result = task_func('{"i": "world", "j": [True, False, None]}')
    expected_df = pd.DataFrame({"i": ["world"], "j": [True, False, None]})
    pd.testing.assert_frame_equal(result, expected_df)