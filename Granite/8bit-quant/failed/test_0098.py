import math
import itertools
from functools import reduce
from src_0098 import task_func

def test_task_func():
    numbers = [1, 2, 3, 4, 5]
    expected_result = math.log(reduce(lambda x, y: x * y, numbers))
    actual_result = task_func(numbers)
    assert actual_result == expected_result

def test_task_func_with_negative_numbers():
    numbers = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
    expected_result = math.log(reduce(lambda x, y: x * y, numbers))
    actual_result = task_func(numbers)
    assert actual_result == expected_result

def test_task_func_with_zero():
    numbers = [1, 2, 3, 4, 5, 0]
    expected_result = math.log(reduce(lambda x, y: x * y, numbers))
    actual_result = task_func(numbers)
    assert actual_result == expected_result

def test_task_func_with_one_number():
    numbers = [5]
    expected_result = 0
    actual_result = task_func(numbers)
    assert actual_result == expected_result

def test_task_func_with_empty_list():
    numbers = []
    expected_result = 0
    actual_result = task_func(numbers)
    assert actual_result == expected_result