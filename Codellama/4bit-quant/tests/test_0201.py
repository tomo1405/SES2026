import random

from src_0201 import task_func


def test_task_func():
    # Test case 1: n = 0
    numbers, num_greater_value = task_func(0, 0)
    assert numbers == []
    assert num_greater_value == 0

    # Test case 2: n = 1
    numbers, num_greater_value = task_func(1, 0)
    assert numbers == [random.random()]
    assert num_greater_value == 1

    # Test case 3: n = 10
    numbers, num_greater_value = task_func(10, 0)
    assert len(numbers) == 10
    assert num_greater_value == 10

    # Test case 4: value = 0
    numbers, num_greater_value = task_func(10, 0)
    assert len(numbers) == 10
    assert num_greater_value == 10

    # Test case 5: value = 1
    numbers, num_greater_value = task_func(10, 1)
    assert len(numbers) == 10
    assert num_greater_value == 10

    # Test case 6: value = 0.5
    numbers, num_greater_value = task_func(10, 0.5)
    assert len(numbers) == 10
    assert num_greater_value == 5

    # Test case 7: value = 0.75
    numbers, num_greater_value = task_func(10, 0.75)
    assert len(numbers) == 10
    assert num_greater_value == 7

    # Test case 8: value = 1.0
    numbers, num_greater_value = task_func(10, 1.0)
    assert len(numbers) == 10
    assert num_greater_value == 10

    # Test case 9: value = 1.25
    numbers, num_greater_value = task_func(10, 1.25)
    assert len(numbers) == 10
    assert num_greater_value == 10

    # Test case 10: value = 1.5
    numbers, num_greater_value = task_func(10, 1.5)
    assert len(numbers) == 10
    assert num_greater_value == 10

    # Test case 11: value = 1.75
    numbers, num_greater_value = task_func(10, 1.75)
    assert len(numbers) == 10
    assert num_greater_value == 10

    # Test case 12: value = 2.0
    numbers, num_greater_value = task_func(10, 2.0)
    assert len(numbers) == 10
    assert num_greater_value == 10