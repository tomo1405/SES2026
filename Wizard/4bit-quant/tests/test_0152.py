python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0152 import task_func

def test_task_func():
    # Test case 1: Valid data keys and dictionary
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    data_keys = ['A', 'B']
    expected_normalized_df = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]}, index=[0, 1, 2])
    expected_ax = None
    actual_normalized_df, actual_ax = task_func(data_dict, data_keys)
    assert actual_normalized_df.equals(expected_normalized_df)
    assert actual_ax == expected_ax

    # Test case 2: Invalid data keys and dictionary
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    data_keys = ['D', 'E']
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

    # Test case 3: Empty data keys and dictionary
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    data_keys = []
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

    # Test case 4: Empty data dictionary
    data_dict = {}
    data_keys = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)