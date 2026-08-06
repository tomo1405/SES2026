import pytest
from src_0872 import task_func

def test_task_func():
    # Test case 1: Empty data list
    data_list = []
    file_name = 'test_output.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == []
    with open(file_name, 'r') as f:
        assert f.read() == ''

    # Test case 2: Data list with one tuple
    data_list = [('a', 1, 2), ('b', 3, 4)]
    file_name = 'test_output.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1.5, 3.5]
    with open(file_name, 'r') as f:
        assert f.read() == 'Position 1: 1.5\nPosition 2: 3.5\n'

    # Test case 3: Data list with multiple tuples
    data_list = [('a', 1, 2), ('b', 3, 4), ('c', 5, 6)]
    file_name = 'test_output.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1.5, 3.5, 5.5]
    with open(file_name, 'r') as f:
        assert f.read() == 'Position 1: 1.5\nPosition 2: 3.5\nPosition 3: 5.5\n'

    # Test case 4: Data list with missing values
    data_list = [('a', 1, 2), ('b', 3, np.nan), ('c', 5, 6)]
    file_name = 'test_output.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [1.5, np.nan, 5.5]
    with open(file_name, 'r') as f:
        assert f.read() == 'Position 1: 1.5\nPosition 2: nan\nPosition 3: 5.5\n'