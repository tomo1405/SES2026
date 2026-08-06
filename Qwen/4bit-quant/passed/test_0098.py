import pytest
from src_0098 import task_func
import math
import itertools
from functools import reduce

def test_task_func_with_empty_list():
    assert task_func([]) == 0

def test_task_func_with_single_element():
    assert task_func([1]) == 0

def test_task_func_with_two_elements():
    assert task_func([1, 2]) == math.log(1) + math.log(2) + math.log(1*2)

def test_task_func_with_three_elements():
    numbers = [1, 2, 3]
    expected = (math.log(1) + math.log(2) + math.log(3) +
                math.log(1*2) + math.log(1*3) + math.log(2*3) +
                math.log(1*2*3))
    assert task_func(numbers) == expected

def test_task_func_with_negative_numbers():
    with pytest.raises(ValueError):
        task_func([-1, 2, 3])

def test_task_func_with_zero_in_list():
    with pytest.raises(ValueError):
        task_func([0, 2, 3])