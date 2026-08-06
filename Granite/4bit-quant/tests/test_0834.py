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
    expected_mode = 5
    expected_numbers = [(5, 200), (6, 199), (7, 198), (8, 197), (9, 196), (10, 195)]

    random.seed(random_seed)
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    actual_mode, actual_numbers = task_func(list_length, range_start, range_end, random_seed)

    assert actual_mode == expected_mode
    assert actual_numbers == expected_numbers

if __name__ == "__main__":
    pytest.main()