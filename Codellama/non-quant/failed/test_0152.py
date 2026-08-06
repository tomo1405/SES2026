import pytest
from src_0152 import task_func

def test_task_func():
    # Test case 1: Empty data dictionary
    data_dict = {}
    data_keys = ['key1', 'key2']
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

    # Test case 2: No matching keys
    data_dict = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}
    data_keys = ['key3', 'key4']
    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

    # Test case 3: Valid data dictionary and keys
    data_dict = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}
    data_keys = ['key1', 'key2']
    normalized_df, ax = task_func(data_dict, data_keys)
    assert isinstance(normalized_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert normalized_df.shape == (3, 2)
    assert ax.get_title() == 'Normalized Data'
    assert ax.get_ylabel() == 'Normalized Value'
    assert ax.get_xlabel() == 'Index'