import numpy as np
import pandas as pd
from src_0293 import task_func


def test_task_func():
    # Test case 1: Test that the function returns a tuple with two elements
    df = pd.DataFrame({'id': [1, 2, 3], 'age': [20, 30, 40], 'income': [100, 200, 300]})
    result = task_func(df)
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test case 2: Test that the function returns a DataFrame with the correct columns
    df_grouped, (hist, bins) = result
    assert isinstance(df_grouped, pd.DataFrame)
    assert 'age' in df_grouped.columns
    assert 'income' in df_grouped.columns

    # Test case 3: Test that the function returns a histogram with the correct number of bins
    assert isinstance(hist, np.ndarray)
    assert len(hist) == 10

    # Test case 4: Test that the function returns a histogram with the correct bin edges
    assert isinstance(bins, np.ndarray)
    assert len(bins) == 11
    assert bins[0] == 0
    assert bins[-1] == 1

    # Test case 5: Test that the function returns a DataFrame with the correct values
    expected_df = pd.DataFrame({'id': [1, 2, 3], 'age': [0.2, 0.3, 0.4], 'income': [0.1, 0.2, 0.3]})
    pd.testing.assert_frame_equal(df_grouped, expected_df)