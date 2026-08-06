import pytest
from src_0098 import task_func
import math
import itertools
from functools import reduce

def test_task_func_empty_list():
    assert math.isclose(task_func([]), 0.0)

def test_task_func_single_element():
    assert math.isclose(task_func([1]), 0.0)

def test_task_func_two_elements():
    assert math.isclose(task_func([2, 3]), math.log(2) + math.log(3) + math.log(6))

def test_task_func_three_elements():
    numbers = [2, 3, 5]
    expected = (math.log(2) + math.log(3) + math.log(5) +
                math.log(6) + math.log(10) + math.log(15) +
                math.log(30))
    assert math.isclose(task_func(numbers), expected)

def test_task_func_negative_numbers():
    with pytest.raises(ValueError):
        task_func([-1, 2, 3])

def test_task_func_zero_in_list():
    with pytest.raises(ValueError):
        task_func([0, 2, 3])