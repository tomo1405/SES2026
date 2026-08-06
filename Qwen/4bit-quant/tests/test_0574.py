import pytest
from src_0574 import task_func
import numpy as np
import pandas as pd

def test_task_func_default_length():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))  # Assuming no return value is expected for the plot
    assert df.shape == (3, 2)
    assert all(df.columns == ['Array1', 'Array2'])

def test_task_func_custom_length():
    length = 50
    df, ax = task_func(length)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, type(None))
    assert df.shape == (3, 2)
    assert all(df.columns == ['Array1', 'Array2'])

def test_task_func_statistics():
    df, ax = task_func(10)
    assert len(df['Array1']) == 3
    assert len(df['Array2']) == 3
    assert all(isinstance(stat, float) for stat in df['Array1'])
    assert all(isinstance(stat, float) for stat in df['Array2'])

def test_task_func_mean_values():
    df, ax = task_func(10)
    mean_array1 = np.mean(np.random.rand(10))
    mean_array2 = np.mean(np.random.rand(10))
    assert abs(df.loc['Mean', 'Array1'] - mean_array1) < 0.1
    assert abs(df.loc['Mean', 'Array2'] - mean_array2) < 0.1

def test_task_func_median_values():
    df, ax = task_func(10)
    median_array1 = np.median(np.random.rand(10))
    median_array2 = np.median(np.random.rand(10))
    assert abs(df.loc['Median', 'Array1'] - median_array1) < 0.1
    assert abs(df.loc['Median', 'Array2'] - median_array2) < 0.1

def test_task_func_std_values():
    df, ax = task_func(10)
    std_array1 = np.std(np.random.rand(10))
    std_array2 = np.std(np.random.rand(10))
    assert abs(df.loc['Standard Deviation', 'Array1'] - std_array1) < 0.1
    assert abs(df.loc['Standard Deviation', 'Array2'] - std_array2) < 0.1