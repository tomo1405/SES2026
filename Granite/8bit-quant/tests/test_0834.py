import random
from collections import Counter
from statistics import mode
import pytest

def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    random.seed(random_seed)
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    counter = Counter(random_list)
    numbers = ((number, count) for number, count in counter.items())
    return mode(random_list), numbers

def test_task_func():
    random_seed = 42
    list_length = 1000
    range_start = 1
    range_end = 10
    random.seed(random_seed)
    expected_mode = mode([random.randint(range_start, range_end) for _ in range(list_length)])
    expected_counter = Counter([random.randint(range_start, range_end) for _ in range(list_length)])
    actual_mode, actual_numbers = task_func(list_length, range_start, range_end, random_seed)
    assert actual_mode == expected_mode
    assert Counter(actual_numbers) == expected_counter

def test_task_func_with_default_args():
    random_seed = None
    list_length = 1000
    range_start = 1
    range_end = 10
    random.seed()
    expected_mode = mode([random.randint(range_start, range_end) for _ in range(list_length)])
    expected_counter = Counter([random.randint(range_start, range_end) for _ in range(list_length)])
    actual_mode, actual_numbers = task_func(list_length, range_start, range_end, random_seed)
    assert actual_mode == expected_mode
    assert Counter(actual_numbers) == expected_counter