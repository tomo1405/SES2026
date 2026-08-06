import pytest
from src_0310 import task_func

def test_task_func():
    # Test with a list of lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    scaled_data = task_func(list_of_lists)
    assert scaled_data == [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]

    # Test with an empty list
    list_of_lists = [[], [1, 2, 3], [4, 5, 6]]
    scaled_data = task_func(list_of_lists)
    assert scaled_data == [[0.5, 0.5, 0.5], [0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]

    # Test with a list of lists with different lengths
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    scaled_data = task_func(list_of_lists)
    assert scaled_data == [[0.1, 0.2, 0.3], [0.4, 0.5], [0.6, 0.7, 0.8, 0.9]]

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [], [4, 5, 6], [7, 8, 9]]
    scaled_data = task_func(list_of_lists)
    assert scaled_data == [[0.1, 0.2, 0.3], [0.5, 0.5, 0.5], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]