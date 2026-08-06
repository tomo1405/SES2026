import numpy as np
import pytest
import seaborn as sns
from src_0161 import task_func


def test_task_func_data_shape():
    data = np.random.rand(10, 8)
    df, ax, p = task_func(data)
    assert df.shape == (10, 9), "The DataFrame should have 10 rows and 9 columns."

def test_task_func_column_names():
    data = np.random.rand(10, 8)
    df, ax, p = task_func(data)
    assert all(column in df.columns for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']), "DataFrame should have the correct column names."

def test_task_func_average_column():
    data = np.random.rand(10, 8)
    df, ax, p = task_func(data)
    assert 'Average' in df.columns, "DataFrame should have an 'Average' column."
    assert df['Average'].equals(df.mean(axis=1)), "The 'Average' column should be the mean of the other columns."

def test_task_func_kdeplot():
    data = np.random.rand(10, 8)
    df, ax, p = task_func(data)
    assert isinstance(ax, sns.axisgrid.FacetGrid), "The returned object should be a seaborn FacetGrid."

def test_task_func_normaltest():
    data = np.random.rand(25, 8)  # Ensure at least 20 samples for normaltest
    df, ax, p = task_func(data)
    assert p is not None, "p value should be calculated if there are at least 20 samples."

def test_task_func_insufficient_samples():
    data = np.random.rand(15, 8)  # Less than 20 samples
    df, ax, p = task_func(data)
    assert p is None, "p value should not be calculated if there are less than 20 samples."

def test_task_func_value_error():
    data = np.random.rand(10, 7)  # Incorrect number of columns
    with pytest.raises(ValueError, match="Data must contain exactly eight columns."):
        task_func(data)