import pytest
from src_0886 import task_func
import pandas as pd


def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is not None
    assert model is not None


def test_task_func_invalid_input():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C', seed=42)
    assert predictions is None
    assert model is None


def test_task_func_non_numeric_data():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    df['A'] = df['A'].astype(str)
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is None
    assert model is None


def test_task_func_empty_data():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    df = df.iloc[0:0]
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is None
    assert model is None