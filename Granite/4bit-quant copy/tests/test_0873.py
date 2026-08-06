import pytest
import numpy as np
import itertools

def task_func(data_list):
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean([val for val in column if isinstance(val, (int, float))]) for column in unzipped_data]
    return mean_values

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    expected_output = [5.5, 7.5, 9.5]
    output = task_func(data_list)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_non_numeric_values():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]
    expected_output = [5.5, 7.5, 9.5]
    output = task_func(data_list)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_uneven_tuple_lengths():
    data_list = [[1, 2, 3], [4, 5], [7, 8, 9, 10], [11, 12]]
    expected_output = [2, 5.5, 8.5, 11.5]
    output = task_func(data_list)
    assert output == expected_output, "Output does not match expected output"