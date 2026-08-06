import pytest
from src_0885 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [100, 200, 300, 400, 500],
        'C': [900, 900, 900, 900, 900]
    }
    df = pd.DataFrame(data)
    p_value = task_func(df, columns=['A', 'B', 'C'])
    assert isinstance(p_value, float)

def test_task_func_with_insufficient_data():
    data = {
        'A': ['X', 'Y', 'X'],
        'B': [100, 200, 300],
        'C': [900, 900, 900]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Insufficient data - no matching data for the applied conditions."):
        task_func(df, columns=['A', 'B', 'C'])

def test_task_func_with_invalid_column_number():
    data = {
        'A': ['X', 'Y', 'X'],
        'B': [100, 200, 300],
        'C': [900, 900, 900]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Exactly three columns should be specified."):
        task_func(df, columns=['A', 'B'])

def test_task_func_with_non_existent_column():
    data = {
        'A': ['X', 'Y', 'X'],
        'B': [100, 200, 300],
        'C': [900, 900, 900]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match='The specified columns should exist in the DataFrame.'):
        task_func(df, columns=['A', 'B', 'D'])

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match='The specified columns should exist in the DataFrame.'):
        task_func(df, columns=['A', 'B', 'C'])

def test_task_func_with_all_conditions_met():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [100, 200, 300, 400, 500],
        'C': [900, 900, 900, 900, 900]
    }
    df = pd.DataFrame(data)
    p_value = task_func(df, columns=['A', 'B', 'C'])
    assert isinstance(p_value, float)

def test_task_func_with_no_matching_data():
    data = {
        'A': ['X', 'Y', 'X'],
        'B': [10, 20, 30],
        'C': [900, 900, 900]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Insufficient data - no matching data for the applied conditions."):
        task_func(df, columns=['A', 'B', 'C'])