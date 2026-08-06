python
import pytest
from src_0464 import task_func

def test_task_func():
    # Test case 1: Valid input
    data_str = "1,2,3,4,5"
    separator = ","
    bins = 20
    expected_data = [1, 2, 3, 4, 5]
    expected_ax = None
    data, ax = task_func(data_str, separator, bins)
    assert data.tolist() == expected_data
    assert ax == expected_ax

    # Test case 2: Invalid input (empty string)
    data_str = ""
    separator = ","
    bins = 20
    with pytest.raises(ValueError):
        task_func(data_str, separator, bins)

    # Test case 3: Invalid input (non-numeric data)
    data_str = "1,2,3,4,foo"
    separator = ","
    bins = 20
    with pytest.raises(ValueError):
        task_func(data_str, separator, bins)