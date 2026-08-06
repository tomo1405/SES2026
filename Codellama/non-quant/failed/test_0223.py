import pytest
from src_0223 import task_func

def test_task_func():
    # Test case 1: empty list
    list_input = []
    cumsum, ax = task_func(list_input)
    assert cumsum == []
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

    # Test case 2: list with one element
    list_input = [1]
    cumsum, ax = task_func(list_input)
    assert cumsum == [1]
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

    # Test case 3: list with multiple elements
    list_input = [1, 2, 3, 4, 5]
    cumsum, ax = task_func(list_input)
    assert cumsum == [1, 3, 6, 10, 15]
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

    # Test case 4: list with negative elements
    list_input = [-1, -2, -3, -4, -5]
    cumsum, ax = task_func(list_input)
    assert cumsum == [-1, -3, -6, -10, -15]
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

    # Test case 5: list with mixed elements
    list_input = [1, 2, -3, 4, -5]
    cumsum, ax = task_func(list_input)
    assert cumsum == [1, 3, -1, 7, -4]
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"