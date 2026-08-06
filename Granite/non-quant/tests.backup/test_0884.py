import pandas as pd
import pytest
from statsmodels.tsa.stattools import adfuller
from src_0884 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'column_a': [1, 2, 3, 4, 5],
        'column_b': [100, 200, 300, 400, 500],
        'column_c': [800, 900, 1000, 1100, 1200]
    })

def test_task_func_with_unique_values(df):
    assert task_func(df, 'column_a', 'column_b', 'column_c') is True

def test_task_func_with_no_values(df):
    df = df[(df['column_b'] <= 50) & (df['column_c'] != 900)]
    assert task_func(df, 'column_a', 'column_b', 'column_c') is True

def test_task_func_with_empty_dataframe(df):
    df = df[(df['column_b'] > 50) & (df['column_c'] == 900)]
    df = df.drop(df.index)
    assert task_func(df, 'column_a', 'column_b', 'column_c') is True

def test_task_func_with_adf_p_value_less_than_0_05(df):
    assert task_func(df, 'column_a', 'column_b', 'column_c') is False