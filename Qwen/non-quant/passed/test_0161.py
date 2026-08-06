import pytest
from src_0161 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_correct_number_of_columns():
    data = np.random.rand(10, 8)
    df, ax, p = task_func(data)
    assert df.shape == (10, 9)  # 10 rows and 9 columns (original 8 + 'Average')

def test_task_func_incorrect_number_of_columns():
    data = np.random.rand(10, 7)
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert str(excinfo.value) == "Data must contain exactly eight columns."

def test_task_func_average_column_exists():
    data = np.random.rand(10, 8)
    df, ax, p = task_func(data)
    assert 'Average' in df.columns

def test_task_func_average_column_values():
    data = np.array([[1, 2, 3, 4, 5, 6, 7, 8]])
    df, ax, p = task_func(data)
    assert df['Average'].iloc[0] == np.mean([1, 2, 3, 4, 5, 6, 7, 8])

def test_task_func_kdeplot():
    data = np.random.rand(10, 8)
    df, ax, p = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_normaltest_with_enough_samples():
    data = np.random.rand(25, 8)
    df, ax, p = task_func(data)
    assert p is not None

def test_task_func_normaltest_without_enough_samples():
    data = np.random.rand(15, 8)
    df, ax, p = task_func(data)
    assert p is None