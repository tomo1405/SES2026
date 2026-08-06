import pytest
from src_0864 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_sums = [14, 37, 68]

    sums = task_func(list_of_lists)

    assert sums == expected_sums