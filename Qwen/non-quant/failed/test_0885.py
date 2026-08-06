import pytest
from src_0885 import task_func
import pandas as pd
from scipy.stats import chi2_contingency

def test_task_func_with_valid_data():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 60, 70, 80, 90],
        'C': [400, 500, 600, 700, 800]
    }
    df = pd.DataFrame(data)
    p_value = task_func(df)
    assert isinstance(p_value, float)

def test_task_func_with_invalid_column_count():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 60, 70, 80, 90],
        'C': [400, 500, 600, 700, 800]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Exactly three columns should be specified."):
        task_func(df, columns=['A', 'B'])

def test_task_func_with_nonexistent_column():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 60, 70, 80, 90],
        'C': [400, 500, 600, 700, 800]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="The specified columns should exist in the DataFrame."):
        task_func(df, columns=['A', 'B', 'D'])

def test_task_func_with_no_matching_data():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 60, 70, 80, 90],
        'C': [400, 500, 600, 700, 800]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Insufficient data - no matching data for the applied conditions."):
        task_func(df, larger=100, equal=800)