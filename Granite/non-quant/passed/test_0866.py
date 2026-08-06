import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
def task_func(data):
    items, counts, weights = zip(*data)
    counts_normalized = zscore(counts)
    scaler = MinMaxScaler()
    weights_normalized = scaler.fit_transform(np.array(weights).reshape(-1, 1)).flatten()
    report_df = pd.DataFrame({
        'Item': items,
        'Normalized Count': counts_normalized,
        'Normalized Weight': weights_normalized
    })

    return report_df
import pytest
def test_task_func():
    data = [('Item1', 10, 20), ('Item2', 15, 25), ('Item3', 20, 30)]
    expected_df = pd.DataFrame({
        'Item': ['Item1', 'Item2', 'Item3'],
        'Normalized Count': zscore([10, 15, 20]),
        'Normalized Weight': MinMaxScaler().fit_transform(np.array([20, 25, 30]).reshape(-1, 1)).flatten()
    })
    actual_df = task_func(data)
    assert actual_df.equals(expected_df)