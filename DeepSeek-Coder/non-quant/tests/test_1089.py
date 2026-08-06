import pytest
from src_1089 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test with default data
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (100, 5), "The shape of the DataFrame is incorrect"
    assert np.all(result.iloc[:, 0] >= -3) and np.all(result.iloc[:, 0] <= 3), "The data is not standardized correctly"

    # Test with custom data
    custom_data = np.random.rand(100, 5)
    result_custom = task_func(custom_data)
    assert isinstance(result_custom, pd.DataFrame), "The result should be a DataFrame"
    assert result_custom.shape == (100, 5), "The shape of the DataFrame is incorrect"
    assert np.all(result_custom.iloc[:, 0] >= -3) and np.all(result_custom.iloc[:, 0] <= 3), "The data is not standardized correctly"