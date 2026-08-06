import pytest
from src_0459 import task_func
import pandas as pd

def test_empty_json_string():
    result = task_func("{}")
    assert result.empty

def test_single_integer():
    result = task_func('{"a": 1}')
    expected_df = pd.DataFrame({"a": [2]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_single_float():
    result = task_func('{"a": 1.5}')
    expected_df = pd.DataFrame({"a": [3.0]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_single_number_string():
    result = task_func('{"a": "1"}')
    expected_df = pd.DataFrame({"a": [2]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_single_non_number_string():
    result = task_func('{"a": "hello"}')
    expected_df = pd.DataFrame({"a": ["hello"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_list_of_integers():
    result = task_func('{"a": [1, 2, 3]}')
    expected_df = pd.DataFrame({"a": [2, 4, 6]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_list_of_floats():
    result = task_func('{"a": [1.5, 2.5, 3.5]}')
    expected_df = pd.DataFrame({"a": [3.0, 5.0, 7.0]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_list_of_mixed_types():
    result = task_func('{"a": [1, "2", 3.0, "four"]}')
    expected_df = pd.DataFrame({"a": [2, 4, 6.0, "four"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_multiple_keys():
    result = task_func('{"a": 1, "b": "2", "c": [3, 4.0]}')
    expected_df = pd.DataFrame({"a": [2], "b": [4], "c": [[6, 8.0]]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_conversion_to_numeric():
    result = task_func('{"a": "1", "b": "2.5", "c": "three"}')
    expected_df = pd.DataFrame({"a": [2], "b": [5.0], "c": [pd.NA]})
    pd.testing.assert_frame_equal(result, expected_df)