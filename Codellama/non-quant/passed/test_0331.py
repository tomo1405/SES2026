import pytest
from src_0331 import task_func

def test_task_func():
    # Test case 1: list_length = 5, k = 3
    numbers, largest_numbers = task_func(list_length=5, k=3)
    assert len(numbers) == 5
    assert len(largest_numbers) == 3
    assert all(largest_numbers[i] >= largest_numbers[i+1] for i in range(len(largest_numbers)-1))

    # Test case 2: list_length = 10, k = 5
    numbers, largest_numbers = task_func(list_length=10, k=5)
    assert len(numbers) == 10
    assert len(largest_numbers) == 5
    assert all(largest_numbers[i] >= largest_numbers[i+1] for i in range(len(largest_numbers)-1))

    # Test case 3: list_length = 15, k = 10
    numbers, largest_numbers = task_func(list_length=15, k=10)
    assert len(numbers) == 15
    assert len(largest_numbers) == 10
    assert all(largest_numbers[i] >= largest_numbers[i+1] for i in range(len(largest_numbers)-1))