import pytest
from src_0939 import task_func
import pandas as pd

def test_task_func_with_empty_string():
    input_df = pd.DataFrame({'text': ['']})
    expected_output = pd.DataFrame({'clean_text': [''], 'text_length': [0]})
    assert task_func(input_df).equals(expected_output)

def test_task_func_with_null_value():
    input_df = pd.DataFrame({'text': [None]})
    expected_output = pd.DataFrame({'clean_text': [''], 'text_length': [0]})
    assert task_func(input_df).equals(expected_output)

def test_task_func_with_special_characters():
    input_df = pd.DataFrame({'text': ['Hello, World!']})
    expected_output = pd.DataFrame({'clean_text': ['HelloWorld'], 'text_length': [10]})
    assert task_func(input_df).equals(expected_output)

def test_task_func_with_numbers():
    input_df = pd.DataFrame({'text': ['12345']})
    expected_output = pd.DataFrame({'clean_text': ['12345'], 'text_length': [5]})
    assert task_func(input_df).equals(expected_output)

def test_task_func_with_mixed_content():
    input_df = pd.DataFrame({'text': ['Python3.8 is awesome!']})
    expected_output = pd.DataFrame({'clean_text': ['Python38isawesome'], 'text_length': [17]})
    assert task_func(input_df).equals(expected_output)

def test_task_func_with_multiple_rows():
    input_df = pd.DataFrame({'text': ['Hello, World!', None, '12345', 'Python3.8 is awesome!']})
    expected_output = pd.DataFrame({
        'clean_text': ['HelloWorld', '', '12345', 'Python38isawesome'],
        'text_length': [10, 0, 5, 17]
    })
    assert task_func(input_df).equals(expected_output)