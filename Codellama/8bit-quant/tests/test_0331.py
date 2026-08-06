import pytest
from src_0331 import task_func

def test_task_func():
    # Test case 1: k is less than list_length
    list_length = 5
    k = 3
    numbers, largest_numbers = task_func(list_length, k)
    assert len(largest_numbers) == k
    assert all(largest_numbers[i] >= largest_numbers[i+1] for i in range(k-1))

    # Test case 2: k is equal to list_length
    list_length = 5
    k = 5
    numbers, largest_numbers = task_func(list_length, k)
    assert len(largest_numbers) == k
    assert all(largest_numbers[i] >= largest_numbers[i+1] for i in range(k-1))

    # Test case 3: k is greater than list_length
    list_length = 5
    k = 10
    numbers, largest_numbers = task_func(list_length, k)
    assert len(largest_numbers) == list_length
    assert all(largest_numbers[i] >= largest_numbers[i+1] for i in range(list_length-1))