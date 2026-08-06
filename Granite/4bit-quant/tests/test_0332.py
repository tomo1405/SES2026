import random

from src_0332 import task_func


def test_task_func():
    num = random.randint(0, 100)
    list_length = random.randint(1, 100)
    min_value = random.randint(-100, 100)
    max_value = random.randint(-100, 100)
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert min(numbers) >= min_value
    assert max(numbers) <= max_value
    assert num in sorted_list
    assert sorted_list == sorted(sorted_list)