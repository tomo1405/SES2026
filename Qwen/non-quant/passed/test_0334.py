import pytest
from src_0334 import task_func

def test_task_func_with_default_values():
    k = 3
    numbers, smallest_numbers = task_func(k)
    assert len(numbers) == 5
    assert len(smallest_numbers) == k
    assert all(isinstance(num, int) for num in numbers)
    assert all(isinstance(num, int) for num in smallest_numbers)
    assert smallest_numbers == sorted(numbers)[:k]

def test_task_func_with_custom_list_length():
    k = 2
    list_length = 10
    numbers, smallest_numbers = task_func(k, list_length=list_length)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(isinstance(num, int) for num in numbers)
    assert all(isinstance(num, int) for num in smallest_numbers)
    assert smallest_numbers == sorted(numbers)[:k]

def test_task_func_with_custom_min_max_values():
    k = 4
    min_value = 50
    max_value = 150
    numbers, smallest_numbers = task_func(k, min_value=min_value, max_value=max_value)
    assert len(numbers) == 5
    assert len(smallest_numbers) == k
    assert all(min_value <= num <= max_value for num in numbers)
    assert all(min_value <= num <= max_value for num in smallest_numbers)
    assert smallest_numbers == sorted(numbers)[:k]

def test_task_func_with_k_greater_than_list_length():
    k = 10
    list_length = 5
    numbers, smallest_numbers = task_func(k, list_length=list_length)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == list_length
    assert all(isinstance(num, int) for num in numbers)
    assert all(isinstance(num, int) for num in smallest_numbers)
    assert smallest_numbers == sorted(numbers)

def test_task_func_with_k_zero():
    k = 0
    numbers, smallest_numbers = task_func(k)
    assert len(numbers) == 5
    assert len(smallest_numbers) == 0
    assert all(isinstance(num, int) for num in numbers)
    assert smallest_numbers == []

def test_task_func_with_k_one():
    k = 1
    numbers, smallest_numbers = task_func(k)
    assert len(numbers) == 5
    assert len(smallest_numbers) == 1
    assert all(isinstance(num, int) for num in numbers)
    assert all(isinstance(num, int) for num in smallest_numbers)
    assert smallest_numbers == [min(numbers)]