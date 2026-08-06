import pytest
from src_0872 import task_func


def test_task_func():
    data_list = [
        (1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 16),
    ]
    file_name = 'test_file.txt'
    mean_values = task_func(data_list, file_name)
    assert mean_values == [2.5, 6.5, 10.5, 14.5]

    # Check that the file was written correctly
    with open(file_name, 'r') as f:
        lines = f.readlines()
        assert lines[0] == 'Position 1: 2.5\n'
        assert lines[1] == 'Position 2: 6.5\n'
        assert lines[2] == 'Position 3: 10.5\n'
        assert lines[3] == 'Position 4: 14.5\n'