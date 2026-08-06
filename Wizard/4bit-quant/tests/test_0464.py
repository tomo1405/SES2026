python
import numpy as np
import pandas as pd
import pytest

def task_func(data_str, separator=",", bins=20):

    data = np.fromstring(data_str, sep=separator)
    if data.size == 0:
        raise ValueError("Failed to find valid data")

    data = pd.Series(data, dtype='int64')
    ax = data.plot.hist(grid=True, bins=bins, rwidth=0.9, color="#607c8e")
    return data, ax

def test_task_func():
    # Test case 1: valid input
    data_str = "1,2,3,4,5,6,7,8,9,10"
    separator = ","
    bins = 20
    expected_data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='int64')
    expected_ax = None
    data, ax = task_func(data_str, separator, bins)
    assert data.equals(expected_data)
    assert ax == expected_ax

    # Test case 2: invalid input (empty string)
    data_str = ""
    separator = ","
    bins = 20
    with pytest.raises(ValueError):
        task_func(data_str, separator, bins)

    # Test case 3: invalid input (non-numeric string)
    data_str = "1,2,3,4,5,6,7,8,9,a"
    separator = ","
    bins = 20
    with pytest.raises(ValueError):
        task_func(data_str, separator, bins)