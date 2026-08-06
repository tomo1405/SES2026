import pytest
from src_0334 import task_func

def test_task_func():
    k = 2
    list_length = 5
    min_value = 0
    max_value = 100

    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)

    # Check that the length of numbers is correct
    assert len(numbers) == list_length

    # Check that the numbers are within the specified range
    assert all(min_value <= num <= max_value for num in numbers)

    # Check that the smallest_numbers list contains k elements
    assert len(smallest_numbers) == k

    # Check that the smallest_numbers are actually the smallest in the list
    assert all(num in numbers for num in smallest_numbers)
    assert sorted(smallest_numbers) == sorted(numbers)[:k]

    # Check that the original list is a heap
    assert list(heapq.merge(*([numbers])) == sorted(numbers)

def test_task_func_k_zero():
    k = 0
    numbers, smallest_numbers = task_func(k)
    assert smallest_numbers == []

def test_task_func_k_greater_than_list_length():
    k = 10
    list_length = 5
    numbers, smallest_numbers = task_func(k, list_length)
    assert smallest_numbers == sorted(numbers)

def test_task_func_min_max_values():
    k = 2
    min_value = 10
    max_value = 20
    numbers, smallest_numbers = task_func(k, min_value=min_value, max_value=max_value)
    assert all(min_value <= num <= max_value for num in numbers)

def test_task_func_default_parameters():
    k = 3
    numbers, smallest_numbers = task_func(k)
    assert len(numbers) == 5
    assert len(smallest_numbers) == k