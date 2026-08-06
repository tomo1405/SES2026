import pandas as pd
import pytest
from statsmodels.tsa.stattools import adfuller
from src_0884 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'column_a': [1, 2, 3, 4, 5],
        'column_b': [50, 60, 70, 80, 90],
        'column_c': [900, 900, 900, 900, 900]
    })

def test_task_func_with_unique_values(df):
    assert task_func(df, 'column_a', 'column_b', 'column_c') is True

def test_task_func_with_no_values(df):
    df = df[(df['column_b'] <= 50) & (df['column_c'] != 900)]
    assert task_func(df, 'column_a', 'column_b', 'column_c') is True

def test_task_func_with_empty_dataframe(df):
    df = df[(df['column_b'] > 50) & (df['column_c'] == 100)]
    assert task_func(df, 'column_a', 'column_b', 'column_c') is True

def test_task_func_with_adf_p_value_less_than_05(df):
    adf_result = adfuller(df['column_a'])
    df = df[(df['column_b'] > 50) & (df['column_c'] == 900)]
    df['column_a'] = [1, 2, 3, 4, 5]
    adf_result = adfuller(df['column_a'])
    assert task_func(df, 'column_a', 'column_b', 'column_c') is True

def test_task_func_with_adf_p_value_greater_than_05(df):
    adf_result = adfuller(df['column_a'])
    df = df[(df['column_b'] > 50) & (df['column_c'] == 900)]
    df['column_a'] = [1, 2, 3, 4, 5]
    adf_result = adfuller(df['column_a'])
    df['column_a'] = [1, 2, 3, 4, 5]
    adf_result = adfuller(df['column_a'])
    assert task_func(df, 'column_a', 'column_b', 'column_c') is False