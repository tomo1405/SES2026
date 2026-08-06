import pytest
from src_0855 import task_func

def test_task_func():
    numbers = [1, 2, 3]
    sums, permutations = task_func(numbers)
    assert sums == [1, 2, 6]
    assert permutations == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

def test_task_func_invalid_input():
    numbers = [1, 2, 3, "a"]
    with pytest.raises(TypeError):
        task_func(numbers)

def test_task_func_invalid_input_2():
    numbers = [1, 2, 3, 4.5]
    with pytest.raises(TypeError):
        task_func(numbers)

def test_task_func_invalid_input_3():
    numbers = [1, 2, 3, -1]
    with pytest.raises(ValueError):
        task_func(numbers)

def test_task_func_empty_input():
    numbers = []
    sums, permutations = task_func(numbers)
    assert sums == []
    assert permutations == []