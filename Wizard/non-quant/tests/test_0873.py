python
import numpy as np
import itertools
import pytest

def task_func(data_list):
    # Unzip the data while handling uneven tuple lengths by filling missing values with NaN
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))

    # Calculate the mean of numeric values, ignoring non-numeric ones
    mean_values = [np.nanmean([val for val in column if isinstance(val, (int, float))]) for column in unzipped_data]

    return mean_values

def test_task_func():
    # Test case 1: data_list with numeric values only
    data_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_result = [3.0, 5.0, 7.0]
    assert task_func(data_list) == expected_result

    # Test case 2: data_list with non-numeric values
    data_list = [(1, 2, 3), (4, 'a', 6), (7, 8, 9)]
    expected_result = [3.0, np.nan, 7.0]
    assert task_func(data_list) == expected_result

    # Test case 3: data_list with empty tuples
    data_list = [(1, 2, 3), (), (7, 8, 9)]
    expected_result = [3.0, np.nan, 7.0]
    assert task_func(data_list) == expected_result

    # Test case 4: data_list with all tuples empty
    data_list = [(), (), ()]
    expected_result = [np.nan, np.nan, np.nan]
    assert task_func(data_list) == expected_result