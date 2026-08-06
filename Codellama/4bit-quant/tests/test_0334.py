import pytest
from src_0334 import task_func

def test_task_func():
    # Test case 1: k = 1, list_length = 5, min_value = 0, max_value = 100
    numbers, smallest_numbers = task_func(k=1, list_length=5, min_value=0, max_value=100)
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)

    # Test case 2: k = 2, list_length = 5, min_value = 0, max_value = 100
    numbers, smallest_numbers = task_func(k=2, list_length=5, min_value=0, max_value=100)
    assert len(smallest_numbers) == 2
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)

    # Test case 3: k = 3, list_length = 5, min_value = 0, max_value = 100
    numbers, smallest_numbers = task_func(k=3, list_length=5, min_value=0, max_value=100)
    assert len(smallest_numbers) == 3
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)
    assert smallest_numbers[2] == min(numbers)

    # Test case 4: k = 4, list_length = 5, min_value = 0, max_value = 100
    numbers, smallest_numbers = task_func(k=4, list_length=5, min_value=0, max_value=100)
    assert len(smallest_numbers) == 4
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)
    assert smallest_numbers[2] == min(numbers)
    assert smallest_numbers[3] == min(numbers)

    # Test case 5: k = 5, list_length = 5, min_value = 0, max_value = 100
    numbers, smallest_numbers = task_func(k=5, list_length=5, min_value=0, max_value=100)
    assert len(smallest_numbers) == 5
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)
    assert smallest_numbers[2] == min(numbers)
    assert smallest_numbers[3] == min(numbers)
    assert smallest_numbers[4] == min(numbers)