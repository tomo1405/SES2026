import heapq
import random
from src_0334 import task_func
import pytest

def test_task_func():
    k = 3
    list_length = 10
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(smallest_numbers) == k
    assert all(number in numbers for number in smallest_numbers)
    assert heapq.nsmallest(k, numbers) == smallest_numbers

def test_task_func_invalid_k():
    k = -1
    list_length = 10
    min_value = 0
    max_value = 100
    with pytest.raises(ValueError):
        task_func(k, list_length, min_value, max_value)

def test_task_func_invalid_list_length():
    k = 3
    list_length = -1
    min_value = 0
    max_value = 100
    with pytest.raises(ValueError):
        task_func(k, list_length, min_value, max_value)

def test_task_func_invalid_min_value():
    k = 3
    list_length = 10
    min_value = 100
    max_value = 0
    with pytest.raises(ValueError):
        task_func(k, list_length, min_value, max_value)

def test_task_func_invalid_max_value():
    k = 3
    list_length = 10
    min_value = 0
    max_value = 0
    with pytest.raises(ValueError):
        task_func(k, list_length, min_value, max_value)