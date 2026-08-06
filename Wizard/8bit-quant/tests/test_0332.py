python
import bisect
import random
import pytest

def task_func(num, list_length=5, min_value=0, max_value=0):
    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    sorted_list = numbers.copy()
    bisect.insort(sorted_list, num)
    return numbers, sorted_list

def test_task_func():
    # Test case 1: num is already in the list
    num = 3
    numbers, sorted_list = task_func(num)
    assert numbers == sorted_list

    # Test case 2: num is not in the list
    num = 10
    numbers, sorted_list = task_func(num)
    assert numbers + [num] == sorted_list

    # Test case 3: list_length is not an integer
    with pytest.raises(TypeError):
        task_func(1, list_length='a')

    # Test case 4: min_value is greater than max_value
    with pytest.raises(ValueError):
        task_func(1, min_value=10, max_value=5)