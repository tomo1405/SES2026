import pytest
from src_0055 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_single_sentence():
    text = "Hello world."
    expected_columns = ['hello', 'world']
    expected_data = [[1, 1]]
    result_df = task_func(text)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.values.tolist() == expected_data

def test_task_func_with_multiple_sentences():
    text = "Hello world. This is a test. Another sentence here."
    expected_columns = ['a', 'another', 'here', 'hello', 'is', 'sentence', 'test', 'this', 'world']
    expected_data = [
        [0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0]
    ]
    result_df = task_func(text)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.values.tolist() == expected_data

def test_task_func_with_empty_text():
    text = ""
    expected_columns = []
    expected_data = []
    result_df = task_func(text)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.values.tolist() == expected_data

def test_task_func_with_only_periods():
    text = ". . ."
    expected_columns = []
    expected_data = []
    result_df = task_func(text)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.values.tolist() == expected_data

def test_task_func_with_special_characters():
    text = "Hello, world! This is a test."
    expected_columns = ['a', 'hello', 'is', 'test', 'this', 'world']
    expected_data = [
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0]
    ]
    result_df = task_func(text)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.values.tolist() == expected_data