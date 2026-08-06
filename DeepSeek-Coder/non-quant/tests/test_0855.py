import pytest
from src_0855 import task_func
from itertools import permutations
from functools import reduce
import math

def test_task_func_valid_input():
    numbers = [1, 2, 3]
    expected_sums = [reduce(lambda a, b: a + b, [math.factorial(n) for n in permutation]) for permutation in all_permutations]
    expected_permutations = list(permutations(numbers))
    sums, permutations = task_func(numbers)
    assert sums == expected_sums
    assert permutations == expected_permutations

def test_task_func_invalid_input_not_list():
    with pytest.raises(TypeError):
        task_func("not_a_list")

def test_task_func_invalid_input_not_integers():
    with pytest.raises(TypeError):
        task_func([1, "2", 3])

def test_task_func_invalid_input_negative_numbers():
    with pytest.raises(ValueError):
        task_func([1, 2, -3])

def test_task_func_empty_list():
    result = task_func([])
    assert result == ([], [])