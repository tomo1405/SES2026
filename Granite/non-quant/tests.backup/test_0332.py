import pytest
from src_0332 import task_func

def test_task_func():
    num = random.randint(0, 100)
    list_length = random.randint(1, 100)
    min_value = random.randint(-100, 100)
    max_value = random.randint(min_value + 1, 100)

    numbers, sorted_list = task_func(num, list_length, min_value, max_value)

    assert len(numbers) == list_length
    assert all(min_value <= num <= max_value for num in numbers)
    assert sorted_list == sorted(sorted_list)
    assert num in sorted_list
    assert bisect.bisect_left(sorted_list, num) == len(numbers)