import pytest
from src_0127 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_values():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 5)
    assert all(df.columns == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'])
    assert all(df['Animal'].isin(['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']))

def test_task_func_custom_animals():
    custom_animals = ['Dog', 'Cat', 'Mouse']
    df = task_func(custom_animals)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 5)
    assert all(df.columns == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'])
    assert all(df['Animal'].isin(custom_animals))

def test_task_func_randomness():
    df1 = task_func(seed=42)
    df2 = task_func(seed=42)
    assert df1.equals(df2)

def test_task_func_different_seed():
    df1 = task_func(seed=1)
    df2 = task_func(seed=2)
    assert not df1.equals(df2)

def test_task_func_statistics():
    df = task_func()
    for index, row in df.iterrows():
        counts = [randint(1, 100) for _ in range(10)]
        mean = statistics.mean(counts)
        median = statistics.median(counts)
        mode = statistics.mode(counts)
        std_dev = np.std(counts)
        assert np.isclose(row['Mean'], mean)
        assert np.isclose(row['Median'], median)
        assert row['Mode'] == mode
        assert np.isclose(row['Standard Deviation'], std_dev)