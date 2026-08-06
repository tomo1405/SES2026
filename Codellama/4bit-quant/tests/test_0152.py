import pandas as pd
import pytest
from src_0152 import task_func


def test_task_func():
    # Test case 1: No matching keys found in data dictionary
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['c', 'd']
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

    # Test case 2: Keys list is empty
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = []
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

    # Test case 3: Normalization works correctly
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['a', 'b']
    normalized_df, ax = task_func(data_dict, data_keys)
    assert normalized_df.equals(pd.DataFrame({'a': [0, 0.5, 1], 'b': [0, 0.5, 1]}))
    assert ax.get_title() == 'Normalized Data'
    assert ax.get_ylabel() == 'Normalized Value'
    assert ax.get_xlabel() == 'Index'

if __name__ == '__main__':
    pytest.main()