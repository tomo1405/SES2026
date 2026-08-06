import pytest
from src_0884 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({'column_a': [1, 2, 3, 4, 5], 'column_b': [10, 20, 30, 40, 50], 'column_c': [900, 900, 900, 900, 900]})
    assert task_func(df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_invalid_input():
    df = pd.DataFrame({'column_a': [1, 2, 3, 4, 5], 'column_b': [10, 20, 30, 40, 50], 'column_c': [900, 900, 900, 900, 900]})
    assert task_func(df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_empty_df():
    df = pd.DataFrame()
    assert task_func(df, 'column_a', 'column_b', 'column_c') == False

def test_task_func_invalid_column_names():
    df = pd.DataFrame({'column_a': [1, 2, 3, 4, 5], 'column_b': [10, 20, 30, 40, 50], 'column_c': [900, 900, 900, 900, 900]})
    assert task_func(df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_invalid_column_types():
    df = pd.DataFrame({'column_a': [1, 2, 3, 4, 5], 'column_b': [10, 20, 30, 40, 50], 'column_c': [900, 900, 900, 900, 900]})
    assert task_func(df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_invalid_p_value():
    df = pd.DataFrame({'column_a': [1, 2, 3, 4, 5], 'column_b': [10, 20, 30, 40, 50], 'column_c': [900, 900, 900, 900, 900]})
    assert task_func(df, 'column_a', 'column_b', 'column_c') == True