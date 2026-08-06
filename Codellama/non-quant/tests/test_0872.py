import pytest
from src_0872 import task_func

def test_task_func():
    # Test case 1: Empty data list
    data_list = []
    file_name = 'test_file.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == []

    # Test case 2: Data list with one tuple
    data_list = [('a', 1, 2, 3)]
    file_name = 'test_file.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1, 2, 3]

    # Test case 3: Data list with multiple tuples
    data_list = [('a', 1, 2, 3), ('b', 4, 5, 6), ('c', 7, 8, 9)]
    file_name = 'test_file.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case 4: Data list with non-numerical values
    data_list = [('a', 1, 2, 3), ('b', 'x', 'y', 'z'), ('c', 7, 8, 9)]
    file_name = 'test_file.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1, 2, 3, np.nan, np.nan, np.nan, 7, 8, 9]

    # Test case 5: Data list with empty tuples
    data_list = [('a', 1, 2, 3), ('b',), ('c', 7, 8, 9)]
    file_name = 'test_file.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1, 2, 3, np.nan, np.nan, np.nan, 7, 8, 9]

    # Test case 6: Data list with non-numerical values and empty tuples
    data_list = [('a', 1, 2, 3), ('b', 'x', 'y', 'z'), ('c',), ('d', 7, 8, 9)]
    file_name = 'test_file.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1, 2, 3, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 7, 8, 9]