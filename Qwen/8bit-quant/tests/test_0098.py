import pytest
from src_0098 import task_func
import math
import itertools
from functools import reduce

def test_task_func_with_empty_list():
    assert task_func([]) == 0

def test_task_func_with_single_element():
    assert math.isclose(task_func([2]), math.log(2))

def test_task_func_with_two_elements():
    assert math.isclose(task_func([2, 3]), math.log(2) + math.log(3) + math.log(6))

def test_task_func_with_three_elements():
    numbers = [2, 3, 4]
    expected = (math.log(2) + math.log(3) + math.log(4) +
                math.log(2*3) + math.log(2*4) + math.log(3*4) +
                math.log(2*3*4))
    assert math.isclose(task_func(numbers), expected)

def test_task_func_with_negative_numbers():
    with pytest.raises(ValueError):
        task_func([-2, 3])

def test_task_func_with_zero_in_list():
    with pytest.raises(ValueError):
        task_func([2, 0, 4])

def test_task_func_with_large_numbers():
    numbers = [10**5, 10**6, 10**7]
    expected = (math.log(10**5) + math.log(10**6) + math.log(10**7) +
                math.log(10**5 * 10**6) + math.log(10**5 * 10**7) + math.log(10**6 * 10**7) +
                math.log(10**5 * 10**6 * 10**7))
    assert math.isclose(task_func(numbers), expected)