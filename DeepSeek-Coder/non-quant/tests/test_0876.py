import pytest
from src_0876 import task_func
import pandas as pd
import random

# Test cases for task_func

def test_task_func_basic():
    data = [['Alice', 30, 'Engineer'], ['Bob', 25, 'Doctor']]
    columns = ['Name', 'Age', 'Occupation']
    result = task_func(data, columns=columns)
    expected_df = pd.DataFrame(data, columns=columns)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_with_missing_values():
    data = [['Alice', None, 'Engineer'], ['Bob', 25, None]]
    columns = ['Name', 'Age', 'Occupation']
    result = task_func(data, columns=columns, fill_missing=True)
    expected_data = [['Alice', 0, 'Engineer'], ['Bob', 25, '']]
    expected_df = pd.DataFrame(expected_data, columns=columns)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_with_seed():
    data = [['Alice', 30, 'Engineer'], ['Bob', 25, 'Doctor']]
    columns = ['Name', 'Age', 'Occupation']
    result = task_func(data, columns=columns, seed=42)
    expected_df = pd.DataFrame(data, columns=columns)
    pd.testing.assert_frame_equal(result, expected_df)