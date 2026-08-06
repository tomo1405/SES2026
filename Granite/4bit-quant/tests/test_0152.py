import matplotlib
import pandas as pd
import pytest
from src_0152 import task_func


def test_task_func():
    data_dict = {'key1': [1, 2, 3], 'key2': [4, 5, 6], 'key3': [7, 8, 9]}
    data_keys = ['key1', 'key2']

    # Test if the function raises a ValueError when no matching keys are found
    with pytest.raises(ValueError):
        task_func({}, [])

    # Test if the function raises a ValueError when the keys list is empty
    with pytest.raises(ValueError):
        task_func(data_dict, [])

    # Test if the function returns the expected output for valid input
    output = task_func(data_dict, data_keys)
    assert isinstance(output, tuple) and len(output) == 2
    assert isinstance(output[0], pd.DataFrame)
    assert isinstance(output[1], matplotlib.axes.Axes)