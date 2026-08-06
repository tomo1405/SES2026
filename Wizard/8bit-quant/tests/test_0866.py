python
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(data):
    # Extracting items, counts, and weights from the input data
    items, counts, weights = zip(*data)
    
    # Normalizing the counts and weights
    counts_normalized = zscore(counts)
    scaler = MinMaxScaler()
    weights_normalized = scaler.fit_transform(np.array(weights).reshape(-1, 1)).flatten()

    # Creating a DataFrame with the normalized data
    report_df = pd.DataFrame({
        'Item': items,
        'Normalized Count': counts_normalized,
        'Normalized Weight': weights_normalized
    })

    return report_df

def test_task_func():
    # Test case 1: Normal input data
    data = [('item1', 10, 2), ('item2', 20, 3), ('item3', 30, 4)]
    expected_df = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [-1.3416407864998738, 0.0, 1.3416407864998738],
        'Normalized Weight': [0.0, 0.5, 1.0]
    })
    assert task_func(data).equals(expected_df)

    # Test case 2: Input data with negative counts
    data = [('item1', -10, 2), ('item2', 20, 3), ('item3', 30, 4)]
    expected_df = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [-1.3416407864998738, 0.0, 1.3416407864998738],
        'Normalized Weight': [0.0, 0.5, 1.0]
    })
    assert task_func(data).equals(expected_df)

    # Test case 3: Input data with all zero counts
    data = [('item1', 0, 2), ('item2', 0, 3), ('item3', 0, 4)]
    expected_df = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.5, 1.0]
    })
    assert task_func(data).equals(expected_df)

    # Test case 4: Input data with all zero weights
    data = [('item1', 10, 0), ('item2', 20, 0), ('item3', 30, 0)]
    expected_df = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [-1.3416407864998738, 0.0, 1.3416407864998738],
        'Normalized Weight': [0.0, 0.5, 1.0]
    })
    assert task_func(data).equals(expected_df)

    # Test case 5: Input data with all zero counts and weights
    data = [('item1', 0, 0), ('item2', 0, 0), ('item3', 0, 0)]
    expected_df = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.5, 1.0]
    })
    assert task_func(data).equals(expected_df)