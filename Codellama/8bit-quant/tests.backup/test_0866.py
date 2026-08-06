import pytest
from src_0866 import task_func
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Normal input
    data = [('item1', 10, 100), ('item2', 20, 200), ('item3', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.0, 0.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 2: Input with negative values
    data = [('item1', -10, 100), ('item2', 20, -200), ('item3', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [-1.0, 0.0, 1.0],
        'Normalized Weight': [0.0, -1.0, 1.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 3: Input with zero values
    data = [('item1', 0, 100), ('item2', 20, 0), ('item3', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [0.0, 0.0, 1.0],
        'Normalized Weight': [0.0, 0.0, 1.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 4: Input with missing values
    data = [('item1', 10, 100), ('item2', 20, None), ('item3', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [0.0, 0.0, 1.0],
        'Normalized Weight': [0.0, 0.0, 1.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 5: Input with duplicate items
    data = [('item1', 10, 100), ('item2', 20, 200), ('item1', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item1'],
        'Normalized Count': [0.0, 0.0, 1.0],
        'Normalized Weight': [0.0, 0.0, 1.0]
    })
    assert task_func(data).equals(expected_output)