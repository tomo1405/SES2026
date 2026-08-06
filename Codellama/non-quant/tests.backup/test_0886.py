import pytest
from src_0886 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def test_task_func_valid_input():
    # Test with valid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is not None
    assert model is not None


def test_task_func_invalid_input():
    # Test with invalid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C', seed=None)
    assert predictions is None
    assert model is None


def test_task_func_non_numeric_data():
    # Test with non-numeric data
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    df['A'] = df['A'].astype(str)
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is None
    assert model is None


def test_task_func_empty_data():
    # Test with empty data
    df = pd.DataFrame({'A': [], 'B': [], 'C': []})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is None
    assert model is None


def test_task_func_filtered_data():
    # Test with filtered data
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is not None
    assert model is not None


def test_task_func_train_test_split():
    # Test with train-test split
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is not None
    assert model is not None


def test_task_func_linear_regression():
    # Test with linear regression
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C')
    assert predictions is not None
    assert model is not None