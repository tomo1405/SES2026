import pytest
from src_0334 import task_func

def test_task_func_k_is_zero():
    numbers, smallest_numbers = task_func(0)
    assert numbers == []
    assert smallest_numbers == []

def test_task_func_k_is_one():
    numbers, smallest_numbers = task_func(1)
    assert len(numbers) == 1
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)

def test_task_func_k_is_greater_than_one():
    numbers, smallest_numbers = task_func(2)
    assert len(numbers) == 2
    assert len(smallest_numbers) == 2
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)

def test_task_func_list_length_is_zero():
    numbers, smallest_numbers = task_func(1, 0)
    assert numbers == []
    assert smallest_numbers == []

def test_task_func_list_length_is_one():
    numbers, smallest_numbers = task_func(1, 1)
    assert len(numbers) == 1
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)

def test_task_func_list_length_is_greater_than_one():
    numbers, smallest_numbers = task_func(2, 3)
    assert len(numbers) == 3
    assert len(smallest_numbers) == 2
    assert smallest_numbers[0] == min(numbers)
    assert smallest_numbers[1] == min(numbers)

def test_task_func_min_value_is_zero():
    numbers, smallest_numbers = task_func(1, 1, 0)
    assert len(numbers) == 1
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)

def test_task_func_min_value_is_greater_than_zero():
    numbers, smallest_numbers = task_func(1, 1, 1)
    assert len(numbers) == 1
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)

def test_task_func_max_value_is_less_than_min_value():
    numbers, smallest_numbers = task_func(1, 1, 1, 0)
    assert len(numbers) == 1
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)

def test_task_func_max_value_is_greater_than_min_value():
    numbers, smallest_numbers = task_func(1, 1, 0, 1)
    assert len(numbers) == 1
    assert len(smallest_numbers) == 1
    assert smallest_numbers[0] == min(numbers)