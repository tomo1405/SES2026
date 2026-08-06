import pytest
from src_0550 import task_func

def test_task_func_with_empty_dataframe():
    input_data = {}
    expected_output = ''
    assert task_func(input_data) == expected_output

def test_task_func_with_single_row():
    input_data = {'A': [1], 'B': [2]}
    expected_output = 'QU46QkAKMSwy'
    assert task_func(input_data) == expected_output

def test_task_func_with_multiple_rows():
    input_data = {'A': [1, 3], 'B': [2, 4]}
    expected_output = 'QU46QkAKMSwyAzMsNA=='
    assert task_func(input_data) == expected_output

def test_task_func_with_non_numeric_data():
    input_data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    expected_output = 'TmFtZTpBZ2UKQWxpY2UyNQpCb2IzMA=='
    assert task_func(input_data) == expected_output

def test_task_func_with_special_characters():
    input_data = {'Symbol': ['@', '#'], 'Value': [10, 20]}
    expected_output = 'U3ltdWJseTpWYWx1ZQAKQCExMAojMjA='
    assert task_func(input_data) == expected_output