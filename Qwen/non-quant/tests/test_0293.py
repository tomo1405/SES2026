import pytest
from src_0293 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Create a sample DataFrame
    data = {
        'id': [1, 1, 2, 2],
        'age': [25, 30, 45, 50],
        'income': [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)

    # Expected output after scaling
    expected_scaled_data = {
        'id': [1, 1, 2, 2],
        'age': [0.0, 1.0, 0.0, 1.0],
        'income': [0.0, 1.0, 0.0, 1.0]
    }
    expected_df = pd.DataFrame(expected_scaled_data).set_index(df.index)

    # Expected histogram of the 'income' column
    expected_hist, expected_bins = np.histogram([0.0, 1.0, 0.0, 1.0], bins=10)

    # Call the function
    result_df, result_hist_bins = task_func(df)

    # Check if the scaled DataFrame is correct
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))

    # Check if the histogram is correct
    assert np.array_equal(result_hist_bins[0], expected_hist)
    assert np.array_equal(result_hist_bins[1], expected_bins)