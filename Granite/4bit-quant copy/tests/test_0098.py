import math
import itertools
from functools import reduce
def task_func(numbers):
    sum_log_products = 0

    for r in range(1, len(numbers) + 1):
        combinations = itertools.combinations(numbers, r)
        for combination in combinations:
            product = reduce(lambda x, y: x * y, combination)
            sum_log_products += math.log(product)

    return sum_log_products
import pytest

def test_task_func():
    numbers = [1, 2, 3, 4]
    expected_result = math.log(reduce(lambda x, y: x * y, numbers))
    actual_result = task_func(numbers)
    assert actual_result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_negative_numbers():
    numbers = [-1, -2, -3, -4]
    expected_result = math.log(reduce(lambda x, y: x * y, numbers))
    actual_result = task_func(numbers)
    assert actual_result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_zero():
    numbers = [0, 1, 2, 3]
    expected_result = math.log(reduce(lambda x, y: x * y, numbers))
    actual_result = task_func(numbers)
    assert actual_result == expected_result, "Task function returned an incorrect result"