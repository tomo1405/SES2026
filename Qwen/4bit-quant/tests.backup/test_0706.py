import pytest
from src_0706 import task_func
import pandas as pd
import numpy as np

def test_task_func_column_not_exists():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df, 'C', 0.05)

def test_task_func_shapiro_test_pass():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    alpha = 0.05
    result = task_func(df, 'A', alpha)
    assert isinstance(result, bool)

def test_task_func_shapiro_test_fail():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    alpha = 1.0  # Set alpha to 1.0 to ensure the test always fails
    result = task_func(df, 'A', alpha)
    assert result == False

def test_task_func_mean_subtraction():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    original_df = df.copy()
    task_func(df, 'A', 0.05)
    assert not (df['A'] == original_df['A']).all(), "Mean subtraction did not occur"

def test_task_func_with_zero_variance():
    df = pd.DataFrame({'A': [1, 1, 1, 1, 1]})
    alpha = 0.05
    result = task_func(df, 'A', alpha)
    assert result == True, "Shapiro test should pass for zero variance data"