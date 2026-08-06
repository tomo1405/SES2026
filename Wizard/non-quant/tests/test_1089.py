python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(data=None):
    if data is None:
        data = np.random.rand(100, 5)

    df = pd.DataFrame(data)
    df[df < 0.5] = 0

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    standardized_df = pd.DataFrame(scaled_data, columns=df.columns)

    return standardized_df

def test_task_func():
    # Test case 1: Test with default data
    data = None
    expected_result = pd.DataFrame(np.zeros((100, 5)))
    result = task_func(data)
    assert result.equals(expected_result)

    # Test case 2: Test with custom data
    data = np.random.rand(100, 5)
    expected_result = pd.DataFrame(np.zeros((100, 5)))
    result = task_func(data)
    assert result.equals(expected_result)