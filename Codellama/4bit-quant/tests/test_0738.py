import pytest
from src_0738 import task_func

def test_task_func():
    # Test case 1: empty list
    with pytest.raises(ValueError):
        task_func([])

    # Test case 2: list with one element
    assert task_func([1]) == 1

    # Test case 3: list with multiple elements
    assert task_func([1, 2, 3, 4, 5]) == 3

    # Test case 4: list with negative elements
    assert task_func([-1, -2, -3, -4, -5]) == -3

    # Test case 5: list with mixed elements
    assert task_func([1, 2, -3, 4, -5]) == 2

    # Test case 6: list with duplicate elements
    assert task_func([1, 1, 1, 1, 1]) == 1

    # Test case 7: list with complex elements
    assert task_func([(1, 2), (3, 4), (5, 6)]) == (3, 4)

    # Test case 8: list with nested lists
    assert task_func([[1, 2], [3, 4], [5, 6]]) == [3, 4]

    # Test case 9: list with empty nested lists
    with pytest.raises(ValueError):
        task_func([[], []])

    # Test case 10: list with nested lists with different lengths
    assert task_func([[1, 2], [3, 4, 5]]) == [3, 4, 5]