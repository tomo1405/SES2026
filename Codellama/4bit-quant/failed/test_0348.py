import pytest
from src_0348 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    df = pd.DataFrame({'A': ['abc123', 'def456', 'ghi789'],
                       'B': ['jkl012', 'mno345', 'pqr678']})
    column = 'A'
    expected_output = pd.Series({'abc123': 1, 'def456': 1, 'ghi789': 1,
                                'jkl012': 1, 'mno345': 1, 'pqr678': 1})
    output = task_func(df, column)
    pd.testing.assert_series_equal(output, expected_output)

def test_task_func_invalid_column():
    df = pd.DataFrame({'A': ['abc123', 'def456', 'ghi789'],
                       'B': ['jkl012', 'mno345', 'pqr678']})
    column = 'C'
    with pytest.raises(KeyError):
        task_func(df, column)

def test_task_func_empty_column():
    df = pd.DataFrame({'A': ['abc123', 'def456', 'ghi789'],
                       'B': ['jkl012', 'mno345', 'pqr678']})
    column = 'A'
    df[column] = ''
    expected_output = pd.Series({})
    output = task_func(df, column)
    pd.testing.assert_series_equal(output, expected_output)

def test_task_func_invalid_data():
    df = pd.DataFrame({'A': ['abc123', 'def456', 'ghi789'],
                       'B': ['jkl012', 'mno345', 'pqr678']})
    column = 'A'
    df[column] = 'invalid data'
    with pytest.raises(ValueError):
        task_func(df, column)