import pytest
from src_0866 import task_func
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Basic functionality with simple data
    data = [
        ('item1', 10, 20),
        ('item2', 20, 30),
        ('item3', 30, 40)
    ]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': zscore([10, 20, 30]),
        'Normalized Weight': MinMaxScaler().fit_transform(np.array([20, 30, 40]).reshape(-1, 1)).flatten()
    })
    assert task_func(data).equals(expected_output)

    # Test case 2: Single item data
    data = [
        ('item1', 5, 15)
    ]
    expected_output = pd.DataFrame({
        'Item': ['item1'],
        'Normalized Count': zscore([5]),
        'Normalized Weight': MinMaxScaler().fit_transform(np.array([15]).reshape(-1, 1)).flatten()
    })
    assert task_func(data).equals(expected_output)

    # Test case 3: All identical counts and weights
    data = [
        ('item1', 10, 20),
        ('item2', 10, 20),
        ('item3', 10, 20)
    ]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.0, 0.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 4: Negative counts and weights
    data = [
        ('item1', -10, -20),
        ('item2', -20, -30),
        ('item3', -30, -40)
    ]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': zscore([-10, -20, -30]),
        'Normalized Weight': MinMaxScaler().fit_transform(np.array([-20, -30, -40]).reshape(-1, 1)).flatten()
    })
    assert task_func(data).equals(expected_output)

    # Test case 5: Mixed positive and negative counts and weights
    data = [
        ('item1', 10, -20),
        ('item2', -20, 30),
        ('item3', 30, -40)
    ]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': zscore([10, -20, 30]),
        'Normalized Weight': MinMaxScaler().fit_transform(np.array([-20, 30, -40]).reshape(-1, 1)).flatten()
    })
    assert task_func(data).equals(expected_output)