python
import heapq
import random
import pytest

def task_func(list_length: int, k: int):
    numbers = [random.randint(0, 100) for _ in range(list_length)]
    heapq.heapify(numbers)
    largest_numbers = heapq.nlargest(k, numbers)
    return numbers, largest_numbers

def test_task_func():
    # Test case 1
    assert task_func(5, 3) == ([99, 98, 97, 96, 95], [99, 98, 97])

    # Test case 2
    assert task_func(10, 5) == ([99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [99, 98, 97, 96, 95])

    # Test case 3
    assert task_func(1, 1) == ([42], [42])

    # Test case 4
    assert task_func(0, 0) == ([], [])

    # Test case 5
    assert task_func(100, 100) == ([99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [99, 98, 97, 96, 95, 94, 93, 92, 91, 90])