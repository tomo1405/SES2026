import pytest
from src_0334 import task_func

def test_task_func_k_greater_than_list_length():
    k = 6
    list_length = 5
    numbers, smallest_numbers = task_func(k, list_length)
    assert len(smallest_numbers) == list_length

def test_task_func_k_zero():
    k = 0
    list_length = 5
    numbers, smallest_numbers = task_func(k, list_length)
    assert smallest_numbers == []

def test_task_func_k_negative():
    k = -1
    list_length = 5
    numbers, smallest_numbers = task_func(k, list_length)
    assert smallest_numbers == []

def test_task_func_min_max_values():
    min_value = 10
    max_value = 20
    k = 3
    list_length = 5
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert all(min_value <= num <= max_value for num in numbers)

def test_task_func_smallest_numbers():
    k = 3
    list_length = 10
    numbers, smallest_numbers = task_func(k, list_length)
    assert sorted(smallest_numbers) == sorted(numbers)[:k]

def test_task_func_heap_property():
    k = 3
    list_length = 10
    numbers, smallest_numbers = task_func(k, list_length)
    assert all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))