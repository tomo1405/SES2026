python
import pytest
from src_0796 import task_func

def test_task_func():
    # Test case 1: Empty list
    assert task_func([]) == deque()

    # Test case 2: List with non-numeric elements
    assert task_func([1, 2, 'a', 'b']) == deque([2, 'a', 'b', 1])

    # Test case 3: List with numeric elements
    assert task_func([1, 2, 3, 4, 5]) == deque([3, 4, 5, 1, 2])

    # Test case 4: List with negative numeric elements
    assert task_func([-1, -2, -3, -4, -5]) == deque([-3, -4, -5, -1, -2])

    # Test case 5: List with mixed numeric and non-numeric elements
    assert task_func([1, 2, 'a', 'b', 3, 4, 5]) == deque([4, 5, 1, 2, 'a', 'b', 3])

    # Test case 6: List with only numeric elements
    assert task_func([1, 2, 3, 4, 5]) == deque([3, 4, 5, 1, 2])

    # Test case 7: List with only negative numeric elements
    assert task_func([-1, -2, -3, -4, -5]) == deque([-3, -4, -5, -1, -2])

    # Test case 8: List with only one numeric element
    assert task_func([1]) == deque([1])

    # Test case 9: List with only one negative numeric element
    assert task_func([-1]) == deque([-1])

    # Test case 10: List with only non-numeric elements
    assert task_func(['a', 'b', 'c']) == deque(['a', 'b', 'c'])