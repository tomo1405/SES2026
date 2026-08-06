import pytest
from src_0864 import task_func

def test_task_func():
    # Test case 1: empty list
    assert task_func([]) == []

    # Test case 2: single element list
    assert task_func([1]) == [1]

    # Test case 3: multiple element list
    assert task_func([1, 2, 3]) == [1, 4, 9]

    # Test case 4: list of lists
    assert task_func([[1, 2], [3, 4]]) == [[1, 4], [9, 16]]

    # Test case 5: list of lists with different lengths
    assert task_func([[1, 2, 3], [4, 5]]) == [[1, 4, 9], [16, 25]]

    # Test case 6: list of lists with different lengths and different values
    assert task_func([[1, 2, 3], [4, 5, 6]]) == [[1, 4, 9], [16, 25, 36]]