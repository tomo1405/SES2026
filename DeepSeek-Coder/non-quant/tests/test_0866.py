import pytest
from src_0866 import task_func
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test data
    data = [
        ('Item1', 10, 0.5),
        ('Item2', 20, 0.3),
        ('Item3', 30, 0.7)
    ]
    
    # Expected output
    expected_df = pd.DataFrame({
        'Item': ['Item1', 'Item2', 'Item3'],
        'Normalized Count': zscore([10, 20, 30]),
        'Normalized Weight': MinMaxScaler().fit_transform([[0.5], [0.3], [0.7]]).flatten()
    })
    
    # Call the function
    result_df = task_func(data)
    
    # Compare the result with the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)