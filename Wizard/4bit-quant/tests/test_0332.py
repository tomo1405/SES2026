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
    # Test case 1
    num = 3
    list_length = 5
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 2
    num = 7
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 3
    num = 1
    list_length = 1
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 4
    num = 9
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 5
    num = 5
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 6
    num = 5
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 7
    num = 5
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 8
    num = 5
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 9
    num = 5
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]

    # Test case 10
    num = 5
    list_length = 10
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == sorted(numbers)
    assert sorted_list == sorted(numbers) + [num]