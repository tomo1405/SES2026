import pytest
from src_0312 import task_func

def test_task_func():
    # Test case 1: empty list
    list_of_lists = []
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 0, 'median': 0, 'mode': 0}

    # Test case 2: list with one element
    list_of_lists = [[1]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 1, 'median': 1, 'mode': 1}

    # Test case 3: list with multiple elements
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}

    # Test case 4: list with multiple elements and different sizes
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}

    # Test case 5: list with multiple elements and different sizes
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}

    # Test case 6: list with multiple elements and different sizes
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}

    # Test case 7: list with multiple elements and different sizes
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}

    # Test case 8: list with multiple elements and different sizes
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}

    # Test case 9: list with multiple elements and different sizes
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}

    # Test case 10: list with multiple elements and different sizes
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    size = 5
    seed = 0
    result = task_func(list_of_lists, size, seed)
    assert result == {'mean': 5, 'median': 5, 'mode': 5}