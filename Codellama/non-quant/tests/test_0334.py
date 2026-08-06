import pytest
from src_0334 import task_func

def test_task_func():
    # Test case 1: k = 1
    numbers, smallest_numbers = task_func(1)
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)

    # Test case 2: k = 2
    numbers, smallest_numbers = task_func(2)
    assert len(smallest_numbers) == 2
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)

    # Test case 3: k = 3
    numbers, smallest_numbers = task_func(3)
    assert len(smallest_numbers) == 3
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)
    assert smallest_numbers[2] == min(numbers)

    # Test case 4: k = 4
    numbers, smallest_numbers = task_func(4)
    assert len(smallest_numbers) == 4
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)
    assert smallest_numbers[2] == min(numbers)
    assert smallest_numbers[3] == min(numbers)

    # Test case 5: k = 5
    numbers, smallest_numbers = task_func(5)
    assert len(smallest_numbers) == 5
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)
    assert smallest_numbers[2] == min(numbers)
    assert smallest_numbers[3] == min(numbers)
    assert smallest_numbers[4] == min(numbers)