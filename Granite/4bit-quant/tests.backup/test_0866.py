import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
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
import pytest
def test_task_func():
    data = [('A', 10, 0.5), ('B', 20, 0.7), ('C', 30, 0.9)]
    expected_df = pd.DataFrame({
        'Item': ['A', 'B', 'C'],
        'Normalized Count': zscore([10, 20, 30]),
        'Normalized Weight': MinMaxScaler().fit_transform(np.array([0.5, 0.7, 0.9]).reshape(-1, 1)).flatten()
    })
    actual_df = task_func(data)
    assert actual_df.equals(expected_df)
def test_task_func_with_empty_data():
    data = []
    expected_df = pd.DataFrame(columns=['Item', 'Normalized Count', 'Normalized Weight'])
    actual_df = task_func(data)
    assert actual_df.equals(expected_df)