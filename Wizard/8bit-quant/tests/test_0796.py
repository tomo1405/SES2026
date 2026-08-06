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

    # Test case 6: List with all non-numeric elements
    assert task_func(['a', 'b', 'c', 'd']) == deque(['a', 'b', 'c', 'd'])

    # Test case 7: List with all numeric elements
    assert task_func([1, 2, 3, 4, 5]) == deque([3, 4, 5, 1, 2])

    # Test case 8: List with all negative numeric elements
    assert task_func([-1, -2, -3, -4, -5]) == deque([-3, -4, -5, -1, -2])

    # Test case 9: List with all zero elements
    assert task_func([0, 0, 0, 0, 0]) == deque([0, 0, 0, 0, 0])

    # Test case 10: List with all elements of the same type
    assert task_func([1, 1, 1, 1, 1]) == deque([1, 1, 1, 1, 1])

    # Test case 11: List with all elements of different types
    assert task_func([1, 2, 'a', 'b', True, False, None]) == deque([2, 'a', 'b', True, False, None, 1])

    # Test case 12: List with all elements of different types and some zero elements
    assert task_func([1, 2, 'a', 'b', True, False, None, 0, 0, 0]) == deque([2, 'a', 'b', True, False, None, 1, 0, 0, 0])

    # Test case 13: List with all elements of different types and some negative elements
    assert task_func([1, 2, 'a', 'b', True, False, None, -1, -2, -3]) == deque([2, 'a', 'b', True, False, None, -3, -2, -1, 1])

    # Test case 14: List with all elements of different types and some negative and zero elements
    assert task_func([1, 2, 'a', 'b', True, False, None, -1, -2, -3, 0, 0, 0]) == deque([2, 'a', 'b', True, False, None, -3, -2, -1, 1, 0, 0, 0])

    # Test case 15: List with all elements of different types and some negative and zero elements and some repeated elements
    assert task_func([1, 2, 'a', 'b', True, False, None, -1, -2, -3, 0, 0, 0, 1, 1, 1, 1, 1]) == deque([2, 'a', 'b', True, False, None, -3, -2, -1, 1, 0, 0, 0, 1, 1, 1, 1, 1])

    # Test case 16: List with all elements of different types and some negative and zero elements and some repeated elements and some non-numeric elements
    assert task_func([1, 2, 'a', 'b', True, False, None, -1, -2, -3, 0, 0, 0, 1, 1, 1, 1, 1, 'c', 'd', 'e']) == deque([2, 'a', 'b', True, False, None, -3, -2, -1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 'c', 'd', 'e'])

    # Test case 17: List with all elements of different types and some negative and zero elements and some repeated elements and some non-numeric elements and some non-unique elements
    assert task_func([1, 2, 'a', 'b', True, False, None, -1, -2, -3, 0, 0, 0, 1, 1, 1, 1, 1, 'c', 'd', 'e', 1, 2, 'a', 'b', True, False, None, -1, -2, -3, 0, 0, 0, 1, 1, 1, 1, 1, 'c', 'd', 'e']) == deque([2, 'a', 'b', True, False, None, -3, -2, -1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 'c', 'd', 'e', 1, 2, 'a', 'b', True, False, None, -1, -2, -3, 0, 0, 0, 1, 1, 1, 1, 1, 'c', 'd', 'e'])