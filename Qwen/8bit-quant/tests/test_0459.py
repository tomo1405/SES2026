import pytest
from src_0459 import task_func
import pandas as pd

def test_task_func_empty_json():
    input_json = "{}"
    expected_output = pd.DataFrame()
    assert task_func(input_json).equals(expected_output)

def test_task_func_single_int():
    input_json = '{"a": 1}'
    expected_output = pd.DataFrame({"a": [2]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_single_float():
    input_json = '{"a": 1.5}'
    expected_output = pd.DataFrame({"a": [3.0]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_single_string_number():
    input_json = '{"a": "2"}'
    expected_output = pd.DataFrame({"a": [4]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_single_string_non_number():
    input_json = '{"a": "abc"}'
    expected_output = pd.DataFrame({"a": ["abc"]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_list_of_ints():
    input_json = '{"a": [1, 2, 3]}'
    expected_output = pd.DataFrame({"a": [2, 4, 6]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_list_of_floats():
    input_json = '{"a": [1.1, 2.2, 3.3]}'
    expected_output = pd.DataFrame({"a": [2.2, 4.4, 6.6]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_list_of_mixed_types():
    input_json = '{"a": [1, "2", 3.0, "abc"]}'
    expected_output = pd.DataFrame({"a": [2, 4, 6.0, "abc"]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_multiple_keys():
    input_json = '{"a": 1, "b": 2.5, "c": "3"}'
    expected_output = pd.DataFrame({"a": [2], "b": [5.0], "c": [6]})
    assert task_func(input_json).equals(expected_output)

def test_task_func_dataframe_conversion():
    input_json = '{"a": [1, 2], "b": ["3", "4"]}'
    expected_output = pd.DataFrame({"a": [2, 4], "b": [6, 8]})
    assert task_func(input_json).equals(expected_output)