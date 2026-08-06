import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from src_0886 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'A': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'B': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
        'C': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900]
    })

def test_invalid_input(input_df):
    invalid_df = input_df.copy()
    invalid_df['D'] = ['x', 'y', 'z']
    result = task_func(invalid_df)
    assert result is None

def test_non_numeric_data(input_df):
    non_numeric_df = input_df.copy()
    non_numeric_df['A'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    result = task_func(non_numeric_df)
    assert result is None

def test_valid_input(input_df):
    result = task_func(input_df)
    assert result is not None
    assert len(result) == 2
    assert isinstance(result[0], list)
    assert isinstance(result[1], LinearRegression)